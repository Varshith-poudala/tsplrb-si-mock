import json
from pathlib import Path

SELECTED_ARITH_IDS = [
    4, 6, 8, 12, 13, 16, 21, 22, 23,
    32, 34, 39, 42, 47, 52, 53, 60,
    61, 62, 66, 68, 73,
    82, 84, 87, 92,
    96, 97, 105, 107, 110,
    112, 117, 118, 120,
    125, 129, 131, 134,
    136, 143, 146, 148,
    154, 155, 162,
    166, 168, 171, 175,
]


def get_arithmetic_questions():
    bank_path = Path(__file__).resolve().parent.parent / "public" / "data" / "master_aptitude_reasoning_bank.json"
    with open(bank_path, "r", encoding="utf-8") as f:
        mb = json.load(f)["questions"]
    by_id = {q["id"]: q for q in mb}

    assert len(SELECTED_ARITH_IDS) == 50, f"Expected 50 arithmetic Qs, got {len(SELECTED_ARITH_IDS)}"
    questions = []
    for idx, bid in enumerate(SELECTED_ARITH_IDS, start=1):
        src = by_id[bid]
        questions.append({
            "id": idx,
            "qNumber": idx,
            "section": "Arithmetic & Quantitative Reasoning",
            "topic": src["topic"],
            "difficulty": "Hard",
            "question_en": src["question_en"],
            "question_te": src["question_te"],
            "options_en": list(src["options_en"]),
            "options_te": list(src["options_te"]),
            "correct_option": int(src["correct_option"]),
            "explanation_en": src["explanation_en"],
            "explanation_te": src["explanation_te"],
        })
    return questions
