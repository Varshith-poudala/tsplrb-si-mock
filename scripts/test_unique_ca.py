import json
import re

# Load all 5 mock tests
used_texts = []
for f in ['mock_test_full_200.json', 'mock_test_full_200_2.json', 'mock_test_full_200_3.json', 'mock_test_full_200_4.json', 'mock_test_full_200_5.json']:
    with open('public/data/' + f) as fl:
        d = json.load(fl)
        for q in d['questions']:
            used_texts.append(q.get('question_en', '').lower())

def is_similar(q_text):
    q_words = set(re.findall(r'\b[a-z]{4,}\b', q_text.lower()))
    for u in used_texts:
        u_words = set(re.findall(r'\b[a-z]{4,}\b', u))
        overlap = len(q_words & u_words)
        if overlap >= 5 and overlap / max(len(q_words), 1) > 0.6:
            return True
    return False

with open('public/data/reference_studynow_ca_2026.json') as f:
    studynow = json.load(f)

truly_unused = []
for q in studynow:
    if len(q['explanation_en']) > 15 and not q['explanation_en'].startswith('Correct Answer:'):
        if not is_similar(q['question_en']):
            truly_unused.append(q)

print(f"Truly unused StudyNow questions: {len(truly_unused)}")
for i in range(min(10, len(truly_unused))):
    print(f"{i+1}: {truly_unused[i]['question_en'][:70]}")
