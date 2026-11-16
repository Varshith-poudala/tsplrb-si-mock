import json

with open('public/data/reference_studynow_ca_2026.json', 'r', encoding='utf-8') as f:
    studynow = json.load(f)

with open('public/data/reference_science_tech_ca_2026.json', 'r', encoding='utf-8') as f:
    sci_tech = json.load(f)

# Mock 1 questions to avoid
with open('public/data/mock_test_full_200.json', 'r', encoding='utf-8') as f:
    m1 = json.load(f)
m1_texts = set(q.get('question_en', '').lower()[:30] for q in m1['questions'])

# Mock 2 questions to avoid
with open('public/data/mock_test_full_200_2.json', 'r', encoding='utf-8') as f:
    m2 = json.load(f)
m2_texts = set(q.get('question_en', '').lower()[:30] for q in m2['questions'])

used_texts = m1_texts | m2_texts

# Filter studynow candidates that are not already used and are well-formed
candidates = []
for q in studynow:
    en_q = q['question_en'].strip()
    prefix = en_q.lower()[:30]
    if prefix in used_texts:
        continue
    if len(q['options_en']) != 4 or not all(q['options_en']):
        continue
    if len(q['options_te']) != 4 or not all(q['options_te']):
        continue
    if len(en_q) < 15:
        continue
    candidates.append(q)
    used_texts.add(prefix)

print(f"Available fresh unique 2026 candidates from StudyNow: {len(candidates)}")
print(f"Available fresh unique 2026 candidates from Sci-Tech: {len(sci_tech)}")

