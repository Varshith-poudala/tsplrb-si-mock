#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembles TSPLRB SI Prelims Full-Length Mock Test 2 (200 Questions)
into public/data/mock_test_full_200_2.json matching the exact test schema.
"""

import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__)))

from questions_arithmetic import get_arithmetic_50
from questions_reasoning import get_reasoning_50
from questions_science import get_science_30
from questions_current_affairs import get_current_affairs_35
from questions_telangana import get_telangana_35

def assemble_full_paper():
    arith = get_arithmetic_50()
    reas = get_reasoning_50()
    sci = get_science_30()
    ca = get_current_affairs_35()
    tg = get_telangana_35()

    all_raw = arith + reas + sci + ca + tg
    print(f"Total raw questions gathered: {len(all_raw)}")
    assert len(all_raw) == 200, f"Expected 200, got {len(all_raw)}"

    questions = []
    for idx, q in enumerate(all_raw, start=1):
        # Validate fields
        assert "question_en" in q and len(q["question_en"].strip()) > 0, f"Q{idx} missing question_en"
        assert "question_te" in q and len(q["question_te"].strip()) > 0, f"Q{idx} missing question_te"
        assert "options_en" in q and len(q["options_en"]) == 4, f"Q{idx} invalid options_en: {len(q.get('options_en', []))}"
        assert "options_te" in q and len(q["options_te"]) == 4, f"Q{idx} invalid options_te: {len(q.get('options_te', []))}"
        assert q["correct_option"] in [0, 1, 2, 3], f"Q{idx} invalid correct_option: {q.get('correct_option')}"
        assert "explanation_en" in q and len(q["explanation_en"].strip()) > 0, f"Q{idx} missing explanation_en"
        assert "explanation_te" in q and len(q["explanation_te"].strip()) > 0, f"Q{idx} missing explanation_te"

        # Determine section
        if idx <= 50:
            sec_name = "Arithmetic"
        elif idx <= 100:
            sec_name = "Reasoning"
        else:
            sec_name = "General Studies"

        q_clean = {
            "id": idx,
            "section": sec_name,
            "topic": q.get("topic", sec_name),
            "question_en": q["question_en"].strip(),
            "question_te": q["question_te"].strip(),
            "options_en": [str(opt).strip() for opt in q["options_en"]],
            "options_te": [str(opt).strip() for opt in q["options_te"]],
            "correct_option": q["correct_option"],
            "explanation_en": q["explanation_en"].strip(),
            "explanation_te": q["explanation_te"].strip()
        }
        questions.append(q_clean)

    paper = {
        "testId": "tsplrb-si-mock-full-200-2",
        "title": "TSPLRB SI Prelims Full-Length Mock Test 2 (200 Questions)",
        "title_te": "తెలంగాణ ఎస్సై ప్రిలిమ్స్ పూర్తి స్థాయి గ్రాండ్ మాక్ టెస్ట్ 2 (200 ప్రశ్నలు)",
        "exam": "Telangana State Police Sub-Inspector (SI) Preliminary Written Test",
        "paper": "Paper I & II High-Yield Pattern: Arithmetic, Reasoning & General Studies (Reference Curated)",
        "totalQuestions": 200,
        "totalMarks": 200,
        "durationMinutes": 180,
        "marksPerQuestion": 1.0,
        "negativeMarking": 0.2,
        "sections": [
            {
                "id": "arithmetic",
                "name": "Part A: Arithmetic",
                "start": 1,
                "end": 50,
                "count": 50
            },
            {
                "id": "reasoning",
                "name": "Part B: Reasoning & Mental Ability",
                "start": 51,
                "end": 100,
                "count": 50
            },
            {
                "id": "general_studies",
                "name": "Part C: General Studies & Telangana Movement",
                "start": 101,
                "end": 200,
                "count": 100
            }
        ],
        "questions": questions
    }

    out_path = os.path.join(os.path.dirname(__file__), "..", "public", "data", "mock_test_full_200_2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(paper, f, ensure_ascii=False, indent=2)

    file_size_kb = os.path.getsize(out_path) / 1024
    print(f"✅ Successfully written to {out_path} ({file_size_kb:.2f} KB) with {len(questions)} verified bilingual questions!")

if __name__ == "__main__":
    assemble_full_paper()
