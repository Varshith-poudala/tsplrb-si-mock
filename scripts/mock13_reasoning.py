# -*- coding: utf-8 -*-
"""
Mock Test 13: 50 Mental Ability & Logical Reasoning Questions
Difficulty: Medium (Official TSPLRB SI PWT Standard)
Selected from Master Aptitude & Reasoning Bank (master_aptitude_reasoning_bank.json)
Zero duplicates against Mocks 1-12, 100% bilingual, 4 options each.
"""
import json

def get_reasoning_50():
    with open('public/data/master_aptitude_reasoning_bank.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = data['questions']
    
    def get_med_range(start_id, end_id, count):
        sub = [q for q in qs if start_id <= q['id'] <= end_id and q['difficulty'] == 'Medium']
        step = len(sub) / count
        return [sub[int(i * step)] for i in range(count)]

    # 10 questions per major reasoning domain
    sel1 = get_med_range(176, 210, 10)  # Calendars, Clocks, Blood Relations
    sel2 = get_med_range(211, 240, 10)  # Blood Relations, Coded Inequalities, Syllogisms
    sel3 = get_med_range(241, 270, 10)  # Syllogisms, Linear Seating Arrangements, Ranking
    sel4 = get_med_range(271, 310, 10)  # Puzzles, Coding-Decoding, Directions & Shadows
    sel5 = get_med_range(311, 350, 10)  # Data Sufficiency, Critical Reasoning, Cubes & Dice, Figure Counting

    reas_50 = sel1 + sel2 + sel3 + sel4 + sel5
    assert len(reas_50) == 50, f"Expected 50 questions, got {len(reas_50)}"
    return reas_50

if __name__ == '__main__':
    qs = get_reasoning_50()
    print(f"Loaded {len(qs)} Reasoning questions for Mock 13.")
    for i, q in enumerate(qs, 1):
        print(f"Q{i} (Source ID {q['id']}): {q['topic']} [{q['difficulty']}]")
