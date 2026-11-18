# -*- coding: utf-8 -*-
"""
Assembles and writes public/data/mock_test_full_200_10.json
Performs strict validation against TSPLRB standards and Shentu's feedback.
"""

import os
import json
import re
from collections import Counter

import mock10_arithmetic
import mock10_reasoning
import mock10_gs_part1
import mock10_gs_part2

def assemble():
    print("🚀 Assembling TSPLRB SI Mock Test 10 (Master Model Paper)...")
    
    q_arith = mock10_arithmetic.get_arithmetic_50()
    q_reason = mock10_reasoning.get_reasoning_50()
    q_gs1 = mock10_gs_part1.get_gs_part1()
    q_gs2 = mock10_gs_part2.get_gs_part2()
    
    all_qs = q_arith + q_reason + q_gs1 + q_gs2
    print(f"Total questions compiled: {len(all_qs)}")
    assert len(all_qs) == 200, f"Expected 200 questions, got {len(all_qs)}"
    
    # Re-index id and qNumber to ensure 1..200
    for idx, q in enumerate(all_qs):
        q["id"] = idx + 1
        q["qNumber"] = idx + 1
    
    # 1. Uniqueness check
    texts_en = [q["question_en"].strip() for q in all_qs]
    dupes = len(texts_en) - len(set(texts_en))
    print(f"Duplicate questions count: {dupes}")
    assert dupes == 0, f"Found {dupes} duplicate questions in Mock 10!"
    
    # 2. Tag cleanliness check
    bracket_tags = sum(1 for q in all_qs if re.match(r"^\[.*?\]", q["question_en"]))
    print(f"Bracket prefix tags: {bracket_tags}")
    assert bracket_tags == 0, f"Found {bracket_tags} bracket prefixes in Mock 10!"
    
    # 3. Completeness check
    for q in all_qs:
        assert len(q["options_en"]) == 4, f"Q{q['id']} does not have 4 English options"
        assert len(q["options_te"]) == 4, f"Q{q['id']} does not have 4 Telugu options"
        assert 0 <= q["correct_option"] <= 3, f"Q{q['id']} correct_option {q['correct_option']} out of range"
        assert len(q["question_en"]) > 5, f"Q{q['id']} empty English question"
        assert len(q["question_te"]) > 5, f"Q{q['id']} empty Telugu question"
        assert len(q["explanation_en"]) > 5, f"Q{q['id']} empty English explanation"
        assert len(q["explanation_te"]) > 5, f"Q{q['id']} empty Telugu explanation"
    
    # 4. Blueprint distribution verification
    arith_count = sum(1 for q in all_qs[:50] if "Arithmetic" in q["section"])
    reason_count = sum(1 for q in all_qs[50:100] if "Reasoning" in q["section"])
    gs_count = sum(1 for q in all_qs[100:] if "General Studies" in q["section"])
    
    print(f"Sections: Arithmetic={arith_count}, Reasoning={reason_count}, General Studies={gs_count}")
    assert arith_count == 50
    assert reason_count == 50
    assert gs_count == 100
    
    # 5. Output file
    out_data = {
        "testId": "tsplrb-si-mock-full-200-10",
        "questions": all_qs
    }
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "public", "data", "mock_test_full_200_10.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Successfully written to {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    assemble()
