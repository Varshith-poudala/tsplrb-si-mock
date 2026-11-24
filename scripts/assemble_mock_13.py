# -*- coding: utf-8 -*-
"""
Assemble and Validate Mock Test 13 (Medium • Official Standard PWT Blueprint)
Outputs: public/data/mock_test_full_200_13.json
"""
import json
import glob
import re
import sys
import os

def clean_tag(s):
    if not s: return ""
    return re.sub(r'^\s*\[[^\]]+\]\s*', '', str(s)).strip()

def main():
    sys.path.append('scripts')
    import mock13_arithmetic as ma
    import mock13_reasoning as mr
    import build_mock13_gs as mgs

    q_arith = ma.get_arithmetic_50()
    q_reas = mr.get_reasoning_50()
    q_gs = mgs.get_gs_100()

    print(f"Loaded: Arithmetic={len(q_arith)}, Reasoning={len(q_reas)}, GS={len(q_gs)}")
    all_qs = q_arith + q_reas + q_gs
    assert len(all_qs) == 200, f"Expected 200 questions, got {len(all_qs)}"

    cleaned_qs = []
    seen_mock13_en = set()
    corr_dist = {0: 0, 1: 0, 2: 0, 3: 0}

    for idx, q in enumerate(all_qs, start=1):
        q_copy = dict(q)
        q_copy["id"] = idx
        q_copy["qNumber"] = idx
        q_copy["difficulty"] = "Medium"

        # Set correct section names
        if idx <= 50:
            q_copy["section"] = "Arithmetic & Quantitative Reasoning"
        elif idx <= 100:
            q_copy["section"] = "Mental Ability & Logical Reasoning"
        else:
            q_copy["section"] = "General Studies & Telangana"

        q_copy["question_en"] = clean_tag(q_copy["question_en"])
        q_copy["question_te"] = clean_tag(q_copy["question_te"])
        q_copy["topic"] = clean_tag(q_copy.get("topic", ""))
        q_copy["options_en"] = [clean_tag(str(o)) for o in q_copy["options_en"]]
        q_copy["options_te"] = [clean_tag(str(o)) for o in q_copy["options_te"]]
        q_copy["explanation_en"] = clean_tag(q_copy.get("explanation_en", ""))
        q_copy["explanation_te"] = clean_tag(q_copy.get("explanation_te", ""))

        # Balanced option distribution: exactly 50 each (A, B, C, D)
        curr_corr = int(q_copy["correct_option"])
        target_corr = (idx - 1) % 4
        if curr_corr != target_corr:
            q_copy["options_en"][curr_corr], q_copy["options_en"][target_corr] = q_copy["options_en"][target_corr], q_copy["options_en"][curr_corr]
            q_copy["options_te"][curr_corr], q_copy["options_te"][target_corr] = q_copy["options_te"][target_corr], q_copy["options_te"][curr_corr]
            q_copy["correct_option"] = target_corr
        else:
            q_copy["correct_option"] = curr_corr

        corr_dist[q_copy["correct_option"]] += 1

        assert len(q_copy["options_en"]) == 4, f"Q{idx} options_en count != 4"
        assert len(q_copy["options_te"]) == 4, f"Q{idx} options_te count != 4"
        assert 0 <= q_copy["correct_option"] <= 3, f"Q{idx} invalid correct_option"
        assert not q_copy["question_en"].startswith("["), f"Q{idx} has bracket tag: {q_copy['question_en'][:30]}"
        assert q_copy["question_en"] and q_copy["question_te"], f"Q{idx} missing question text"
        assert q_copy["explanation_en"] and q_copy["explanation_te"], f"Q{idx} missing explanation"

        en_norm = "".join(c for c in q_copy["question_en"].lower() if c.isalnum())
        assert en_norm not in seen_mock13_en, f"Internal duplicate detected at Q{idx}: {q_copy['question_en'][:60]}"
        seen_mock13_en.add(en_norm)

        cleaned_qs.append(q_copy)

    print("Option distribution across 200 questions:", corr_dist)
    assert corr_dist[0] == 50 and corr_dist[1] == 50 and corr_dist[2] == 50 and corr_dist[3] == 50

    # Check external duplicates against Mocks 1-12
    existing_en = {}
    for f in sorted(glob.glob('public/data/mock_test_full_200*.json')):
        if '13' in f: continue
        with open(f, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        qs = data if isinstance(data, list) else data.get('questions', [])
        for item in qs:
            t = item.get('question_en', '').strip().lower()
            if t:
                norm = "".join(c for c in t[:60] if c.isalnum())
                existing_en[norm] = f

    ext_dups = []
    for q in cleaned_qs:
        en_norm = "".join(c for c in q["question_en"].lower()[:60] if c.isalnum())
        if en_norm in existing_en:
            ext_dups.append((q['id'], q['question_en'][:60], existing_en[en_norm]))

    if ext_dups:
        print(f"ERROR: Found {len(ext_dups)} external duplicates with existing mocks!")
        for d in ext_dups:
            print("  Dup:", d)
        sys.exit(1)

    print("Zero duplicates verified against all existing Mocks 1 to 12!")

    payload = {
        "testId": "tsplrb-si-mock-full-200-13",
        "title": "TSPLRB SI Mock Test 13 (Medium • Official Standard PWT Blueprint)",
        "totalQuestions": len(cleaned_qs),
        "durationMinutes": 180,
        "marksPerQuestion": 1.0,
        "negativeMarking": 0.20,
        "questions": cleaned_qs
    }

    out_path = "public/data/mock_test_full_200_13.json"
    with open(out_path, "w", encoding="utf-8") as out:
        json.dump(payload, out, indent=2, ensure_ascii=False)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"Successfully generated {out_path} ({size_kb:.1f} KB) with {len(cleaned_qs)} questions!")

if __name__ == "__main__":
    main()
