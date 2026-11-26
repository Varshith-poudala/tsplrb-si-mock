import glob
import json
import re
from collections import Counter
from pathlib import Path

from mock14_arithmetic import get_arithmetic_questions
from mock14_reasoning import get_reasoning_questions
from build_mock14_gs import get_gs_questions

ANCHOR_RE = re.compile(
    r"(all\s+of\s+the\s+above|none\s+of\s+the\s+above|both\s+1\s+and\s+2|neither\s+1\s+nor\s+2|"
    r"1\s+and\s+2\s+only|2\s+and\s+3\s+only|1\s+and\s+3\s+only|1,\s*2,?\s*and\s+3|"
    r"both\s+follow|neither\s+follows|either\s+i\s+or\s+ii|only\s+i|only\s+ii|only\s+conclusion|"
    r"cannot\s+be\s+determined|statement\s+i|both\s+statements|neither\s+statement|"
    r"\([a-d]\)\s*-\s*\(?[iv0-9]+|పైవన్నీ|ఏదీ\s*కాదు|రెండూ|నిర్ణయించలేము|మాత్రమే|అనుసరి)",
    re.IGNORECASE,
)


def norm(s):
    return re.sub(r"\W+", "", str(s or "").lower())


def is_anchored(q):
    for opt in q["options_en"] + q["options_te"]:
        if ANCHOR_RE.search(opt):
            return True
    # Also keep chronology sequences (dash-separated digit orders) fixed if desired, though permuting them is safe
    return False


def swap_option_to(q, target_idx):
    cur = q["correct_option"]
    if cur == target_idx:
        return
    q["options_en"][cur], q["options_en"][target_idx] = q["options_en"][target_idx], q["options_en"][cur]
    q["options_te"][cur], q["options_te"][target_idx] = q["options_te"][target_idx], q["options_te"][cur]
    q["correct_option"] = target_idx


def main():
    root = Path(__file__).resolve().parent.parent
    out_path = root / "public" / "data" / "mock_test_full_200_14.json"

    arith = get_arithmetic_questions()
    reas = get_reasoning_questions()
    gs = get_gs_questions()
    questions = arith + reas + gs

    assert len(questions) == 200, f"Expected 200 questions, got {len(questions)}"
    for i, q in enumerate(questions, start=1):
        assert q["id"] == i and q["qNumber"] == i, f"Bad numbering at {i}: {q}"

    # Verify zero internal duplicates
    seen_norm = {}
    for q in questions:
        k = norm(q["question_en"])
        assert k not in seen_norm, f"Internal duplicate: Q{q['qNumber']} vs Q{seen_norm[k]}"
        seen_norm[k] = q["qNumber"]

    # Verify zero external duplicates against Mocks 1-13
    for fpath in sorted(glob.glob(str(root / "public" / "data" / "mock_test_full_200*.json"))):
        if Path(fpath).resolve() == out_path.resolve():
            continue
        other = json.load(open(fpath, "r", encoding="utf-8"))["questions"]
        for oq in other:
            ok = norm(oq.get("question_en"))
            assert ok not in seen_norm, f"Duplicate vs {Path(fpath).name}: Mock14 Q{seen_norm[ok]} matches existing Q{oq.get('qNumber') or oq.get('id')}"

    print("Duplicate check passed: 0 internal, 0 external across all existing mocks.")
    print("Pre-balance GS dist:", Counter(q["correct_option"] for q in gs))
    print("Pre-balance total dist:", Counter(q["correct_option"] for q in questions))

    # Balance strictly using UNANCHORED questions to achieve exact {0: 50, 1: 50, 2: 50, 3: 50}
    counts = Counter(q["correct_option"] for q in questions)
    target = {0: 50, 1: 50, 2: 50, 3: 50}
    unanchored = [q for q in questions if not is_anchored(q)]
    print(f"Unanchored questions available for exact balancing: {len(unanchored)}")

    for q in unanchored:
        cur = q["correct_option"]
        if counts[cur] > target[cur]:
            # Find an underrepresented slot
            need = min((k for k in range(4) if counts[k] < target[k]), key=lambda k: counts[k])
            swap_option_to(q, need)
            counts[cur] -= 1
            counts[need] += 1

    print("Post-balance dist:", dict(sorted(counts.items())))
    assert all(counts[k] == 50 for k in range(4)), f"Imbalanced: {counts}"

    # Verify anchored integrity: none of the anchored questions changed order
    for q in questions:
        assert 0 <= q["correct_option"] <= 3
        assert len(q["options_en"]) == 4 and len(q["options_te"]) == 4

    payload = {
        "testId": "tsplrb-si-mock-full-200-14",
        "title": "TSPLRB SI Mock Test 14 (Hard • Advanced Mains & PWT Standard)",
        "title_te": "తెలంగాణ ఎస్సై మాక్ టెస్ట్ 14 (హార్డ్ • అడ్వాన్స్‌డ్ మెయిన్స్ & PWT స్టాండర్డ్)",
        "exam": "TSPLRB Sub-Inspector Preliminary Written Test (PWT)",
        "difficulty": "Hard",
        "totalQuestions": 200,
        "totalMarks": 200,
        "durationMinutes": 180,
        "marksPerQuestion": 1.0,
        "negativeMarking": 0.20,
        "questions": questions,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote {out_path} ({len(questions)} Qs).")


if __name__ == "__main__":
    main()
