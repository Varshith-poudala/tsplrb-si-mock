import json

with open('public/data/mock_test_full_200_3.json') as f:
    m3 = json.load(f).get('questions')

with open('public/data/faculty_curated_bank.json') as f:
    fc = json.load(f).get('questions', [])

print(f"Mock 3 has {len(m3)} questions. FC has {len(fc)} questions.")
