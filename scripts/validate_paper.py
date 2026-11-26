#!/usr/bin/env python3
"""
Reusable Quality Assurance (QA) Validator for TSPLRB 200-Question Mock Papers.
Run before committing or syncing any newly generated or edited mock test paper.

Usage:
  python3 scripts/validate_paper.py public/data/mock_test_full_200_12.json
  python3 scripts/validate_paper.py --all
"""
import argparse
import glob
import json
import re
import sys
from collections import Counter

DRAFT_ARTIFACT_PAT = re.compile(
    r"\b(?:wait\s*[:,?]|let's\s+(?:make|adjust|check|test|specify|change)|lets\s+(?:make|adjust)|let us make|check option|fix this)\b",
    re.I,
)
# Detect merged options like "ఒడిశా బి. జార్ఖండ్ సి. కర్ణాటక" without flagging initials like "సి. రాజగోపాలాచారి"
MERGED_OPT_PAT = re.compile(
    r"(?:.+?\s+(?:బి|సి|డి)\.\s+.+?\s+(?:సి|డి)\.\s+|.+?\s+[B-D]\.\s+.+?\s+[C-D]\.\s+)"
)
OCR_GARBLE_HINTS = [
    "భార్తదేశ్",
    "రాయంక్",
    "ఉకెియి",
    "చరన",
    "అమరికా",
    "సోనము",
    "పరపంచ",
    "ముంబర",
    "కరాటక",
    "బరలడ",
    "జటల్",
    "యొక్ ",
]


def validate_file(filepath: str) -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    qs = data if isinstance(data, list) else data.get("questions", [])
    issues = []
    warnings = []
    seen_en = {}
    dist = Counter()

    if len(qs) != 200:
        warnings.append(f"Question count is {len(qs)} (expected 200)")

    for idx, q in enumerate(qs, start=1):
        qn = q.get("qNumber", q.get("id", idx))
        q_en = (q.get("question_en") or "").strip()
        q_te = (q.get("question_te") or "").strip()
        opts_en = q.get("options_en") or []
        opts_te = q.get("options_te") or []
        corr = q.get("correct_option")
        exp_en = (q.get("explanation_en") or "").strip()
        exp_te = (q.get("explanation_te") or "").strip()

        # 1. Schema & bounds checks
        if len(opts_en) != 4 or len(opts_te) != 4:
            issues.append(f"Q{qn}: Expected 4 options EN/TE, got {len(opts_en)}/{len(opts_te)}")
            continue
        if not isinstance(corr, int) or not (0 <= corr <= 3):
            issues.append(f"Q{qn}: Invalid correct_option={corr!r}")
            continue
        dist[corr] += 1

        if not q_en or not q_te:
            issues.append(f"Q{qn}: Missing question_en or question_te")
        if any(not str(o).strip() for o in opts_en + opts_te):
            issues.append(f"Q{qn}: Blank option text detected")
        if not exp_en or not exp_te:
            issues.append(f"Q{qn}: Missing explanation_en or explanation_te")

        # 2. Internal duplicate detection
        norm_en = re.sub(r"[^a-z0-9]", "", q_en.lower())
        if norm_en in seen_en:
            issues.append(f"Q{qn}: Duplicate of Q{seen_en[norm_en]}: {q_en[:60]}")
        else:
            seen_en[norm_en] = qn

        # 3. Draft / scratch-note leaks (e.g. "Wait:", "Let's make...")
        for field_name, txt in [("question_en", q_en), ("explanation_en", exp_en), ("explanation_te", exp_te)]:
            m = DRAFT_ARTIFACT_PAT.search(txt)
            if m:
                issues.append(f"Q{qn} ({field_name}): Draft note leak ({m.group(0)!r}): {txt[:100]}")

        # 4. Merged options / OCR garble in Telugu
        for oi, ot in enumerate(opts_te):
            if MERGED_OPT_PAT.search(ot):
                issues.append(f"Q{qn} options_te[{oi}]: Merged option text: {ot[:80]}")
        for garble in OCR_GARBLE_HINTS:
            if garble in q_te or any(garble in o for o in opts_te) or garble in exp_te:
                issues.append(f"Q{qn}: Telugu OCR garble ({garble!r}) detected")
                break

        # 5. Explanation vs correct_option consistency checks
        corr_en = opts_en[corr].strip()
        if corr_en and len(corr_en) >= 3:
            explicit_ans = re.search(
                r"(?:correct answer|answer is|correct option)\s*[:\-]\s*([^\n.;]+)",
                exp_en,
                re.I,
            )
            if explicit_ans:
                stated = explicit_ans.group(1).strip().lower()
                # Check if stated matches a *different* option while NOT matching corr_en
                if corr_en.lower() not in stated:
                    for oi, opt in enumerate(opts_en):
                        if oi != corr and len(opt.strip()) >= 3 and opt.strip().lower() in stated:
                            issues.append(
                                f"Q{qn}: Answer-key mismatch! correct_option={corr} ({corr_en}), "
                                f"but explanation states ({opts_en[oi]})"
                            )
                            break

        # Check Telugu "సరైన సమాధానం: ..." prefix consistency
        m_te_ans = re.match(r"^సరైన సమాధానం\s*:\s*([^\.\(\n]+)", exp_te)
        if m_te_ans:
            stated_te = m_te_ans.group(1).strip().lower()
            corr_te = opts_te[corr].strip().lower()
            if corr_te and corr_te not in stated_te and stated_te not in corr_te:
                # Check if it names another option
                for oi, ot in enumerate(opts_te):
                    ot_l = ot.strip().lower()
                    if oi != corr and len(ot_l) >= 2 and (ot_l in stated_te or stated_te in ot_l):
                        issues.append(
                            f"Q{qn}: Telugu answer mismatch! correct_option={corr} ({opts_te[corr]}), "
                            f"but explanation_te starts with {stated_te!r}"
                        )
                        break

    # 6. Option distribution balance check (should not skew > 35% on a single letter)
    total = sum(dist.values()) or 1
    max_pct = max(dist.values()) / total * 100
    min_pct = min(dist.get(i, 0) for i in range(4)) / total * 100
    if max_pct > 35.0 or min_pct < 15.0:
        warnings.append(
            f"Option distribution skewed: A={dist[0]}, B={dist[1]}, C={dist[2]}, D={dist[3]} "
            f"(min {min_pct:.1f}%, max {max_pct:.1f}%)"
        )

    return {
        "file": filepath,
        "count": len(qs),
        "dist": {k: dist.get(k, 0) for k in range(4)},
        "issues": issues,
        "warnings": warnings,
    }


def main():
    parser = argparse.ArgumentParser(description="Validate TSPLRB mock paper JSON files.")
    parser.add_argument("files", nargs="*", help="Mock JSON files to validate")
    parser.add_argument("--all", action="store_true", help="Validate all public/data/mock_test_full_200*.json files")
    args = parser.parse_args()

    targets = sorted(glob.glob("public/data/mock_test_full_200*.json")) if args.all else args.files
    if not targets:
        parser.print_help()
        sys.exit(2)

    total_issues = 0
    for fpath in targets:
        res = validate_file(fpath)
        status = "PASS" if not res["issues"] and not res["warnings"] else ("FAIL" if res["issues"] else "WARN")
        print(f"[{status}] {res['file']} ({res['count']} Qs) | dist={res['dist']}")
        for w in res["warnings"]:
            print(f"  WARN: {w}")
        for iss in res["issues"]:
            print(f"  FAIL: {iss}")
        total_issues += len(res["issues"])

    print(f"\nSummary: {len(targets)} file(s) scanned, {total_issues} critical issue(s) found.")
    sys.exit(1 if total_issues else 0)


if __name__ == "__main__":
    main()
