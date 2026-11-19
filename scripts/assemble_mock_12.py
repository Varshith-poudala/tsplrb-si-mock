# -*- coding: utf-8 -*-
"""
Assemble and Validate Mock Test 12 (Easy / Foundational 200Q Paper)
Outputs: public/data/mock_test_full_200_12.json
"""

import json
import glob
import re
import sys

def clean_tag(s):
    if not s: return ""
    s = re.sub(r'^\s*\[[^\]]+\]\s*', '', s)
    return s.strip()

def main():
    import scripts.mock12_arithmetic as ma
    import scripts.mock12_reasoning as mr
    import scripts.mock12_gs as mgs

    q_arith = ma.get_arithmetic_50()
    q_reas = mr.get_reasoning_50()
    q_gs = mgs.get_gs_100()

    print(f"Loaded: Arithmetic={len(q_arith)}, Reasoning={len(q_reas)}, GS={len(q_gs)}")
    all_qs = q_arith + q_reas + q_gs
    assert len(all_qs) == 200, f"Expected 200 questions, got {len(all_qs)}"

    cleaned_qs = []
    seen_mock12_en = set()

    for idx, q in enumerate(all_qs, start=1):
        q_copy = dict(q)
        q_copy["id"] = idx
        q_copy["qNumber"] = idx
        q_copy["question_en"] = clean_tag(q_copy["question_en"])
        q_copy["question_te"] = clean_tag(q_copy["question_te"])
        q_copy["topic"] = clean_tag(q_copy.get("topic", ""))
        q_copy["options_en"] = [clean_tag(str(o)) for o in q_copy["options_en"]]
        q_copy["options_te"] = [clean_tag(str(o)) for o in q_copy["options_te"]]
        q_copy["correct_option"] = int(q_copy["correct_option"])
        q_copy["explanation_en"] = clean_tag(q_copy.get("explanation_en", ""))
        q_copy["explanation_te"] = clean_tag(q_copy.get("explanation_te", ""))

        assert len(q_copy["options_en"]) == 4, f"Q{idx} options_en count != 4"
        assert len(q_copy["options_te"]) == 4, f"Q{idx} options_te count != 4"
        assert 0 <= q_copy["correct_option"] <= 3, f"Q{idx} invalid correct_option"
        assert not q_copy["question_en"].startswith("["), f"Q{idx} has bracket tag: {q_copy['question_en'][:30]}"

        en_norm = q_copy["question_en"].lower().strip()
        if en_norm in seen_mock12_en:
            print(f"WARNING: Internal duplicate detected at Q{idx}: {q_copy['question_en'][:60]}")
        seen_mock12_en.add(en_norm)

        cleaned_qs.append(q_copy)

    # Check external duplicates against Mocks 1-11
    existing_en = {}
    for f in sorted(glob.glob('public/data/mock_test_full_200*.json')):
        if '12' in f: continue
        with open(f) as fp: data = json.load(fp)
        qs = data if isinstance(data, list) else data.get('questions', [])
        for item in qs:
            t = item.get('question_en', '').strip().lower()
            if t: existing_en[t] = f

    ext_dups = 0
    for q in cleaned_qs:
        en_norm = q["question_en"].lower().strip()
        if en_norm in existing_en:
            print(f"WARNING: External duplicate at Q{q['id']} with {existing_en[en_norm]}: {q['question_en'][:60]}")
            ext_dups += 1

    print(f"External duplicates found: {ext_dups}")
    assert ext_dups == 0, f"Found {ext_dups} duplicate questions with existing mocks!"

    payload = {
        "testId": "tsplrb-si-mock-full-200-12",
        "questions": cleaned_qs
    }

    out_path = "public/data/mock_test_full_200_12.json"
    with open(out_path, "w", encoding="utf-8") as out:
        json.dump(payload, out, indent=2, ensure_ascii=False)

    print(f"Successfully generated {out_path} with {len(cleaned_qs)} questions!")

if __name__ == "__main__":
    main()
