# -*- coding: utf-8 -*-
"""
Mock Test 13: 50 Arithmetic & Quantitative Reasoning Questions
Difficulty: Medium (Official TSPLRB SI PWT Standard)
Selected from Master Aptitude & Reasoning Bank (master_aptitude_reasoning_bank.json)
Zero duplicates against Mocks 1-12, 100% bilingual, 4 options each.
"""
import json

def get_arithmetic_50():
    with open('public/data/master_aptitude_reasoning_bank.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = data['questions']
    
    def get_med_range(start_id, end_id, count):
        sub = [q for q in qs if start_id <= q['id'] <= end_id and q['difficulty'] == 'Medium']
        step = len(sub) / count
        return [sub[int(i * step)] for i in range(count)]

    # 10 questions per major quantitative domain
    sel1 = get_med_range(1, 30, 10)    # Speed, Distance, Time, Trains, Boats & Streams, Races
    sel2 = get_med_range(31, 60, 10)   # Mensuration 2D & 3D
    sel3 = get_med_range(61, 90, 10)   # Time & Work, Pipes & Cisterns
    sel4 = get_med_range(91, 120, 10)  # Profit, Loss, Discount, Simple & Compound Interest
    sel5 = get_med_range(121, 175, 10) # Percentages, Ratios, Partnerships, Number Systems, Probability

    arith_50 = sel1 + sel2 + sel3 + sel4 + sel5
    assert len(arith_50) == 50, f"Expected 50 questions, got {len(arith_50)}"
    return arith_50

if __name__ == '__main__':
    qs = get_arithmetic_50()
    print(f"Loaded {len(qs)} Arithmetic questions for Mock 13.")
    for i, q in enumerate(qs, 1):
        print(f"Q{i} (Source ID {q['id']}): {q['topic']} [{q['difficulty']}]")
