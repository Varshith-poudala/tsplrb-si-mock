import json

print("Checking schema requirements...")

def validate_paper(p):
    assert "testId" in p
    assert "title" in p
    assert "questions" in p
    assert len(p["questions"]) == 200
    for idx, q in enumerate(p["questions"], start=1):
        assert q["id"] == idx
        assert len(q["question_en"]) > 0
        assert len(q["question_te"]) > 0
        assert len(q["options_en"]) == 4
        assert len(q["options_te"]) == 4
        assert q["correct_option"] in [0, 1, 2, 3]
        assert len(q["explanation_en"]) > 0
        assert len(q["explanation_te"]) > 0
    print("Schema perfectly valid!")

