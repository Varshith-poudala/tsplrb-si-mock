import json

with open('public/data/reference_studynow_ca_2026.json') as f:
    studynow = json.load(f)

used_prefixes = set()
for f in ['mock_test_full_200.json', 'mock_test_full_200_2.json', 'mock_test_full_200_3.json', 'mock_test_full_200_4.json', 'mock_test_full_200_5.json']:
    with open('public/data/' + f) as fl:
        d = json.load(fl)
        for q in d['questions']:
            used_prefixes.add(q.get('question_en', '').strip().lower()[:25])

unused_studynow = []
for q in studynow:
    p = q['question_en'].strip().lower()[:25]
    if p not in used_prefixes and len(q['explanation_en']) > 15 and not q['explanation_en'].startswith('Correct Answer:'):
        unused_studynow.append(q)

print(f"Total available: {len(unused_studynow)}")
mock6_ca = unused_studynow[0:25]
mock7_ca = unused_studynow[25:50]

print("Mock 6 CA sample:", mock6_ca[0]['question_en'])
print("Mock 7 CA sample:", mock7_ca[0]['question_en'])
