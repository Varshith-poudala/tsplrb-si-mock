import json
import re

with open('/tmp/studynow_verified.json', 'r', encoding='utf-8') as f:
    all_q = json.load(f)

# Filter for questions with rich, verified notes (not empty / fallback)
verified_pool = []
for q in all_q:
    exp = q['explanation_en']
    if exp.startswith('Correct Answer:') or len(exp) < 15:
        continue
    # Ensure options are clean and have 4 items
    if len(q['options_en']) != 4 or not all(q['options_en']):
        continue
    if len(q['options_te']) != 4 or not all(q['options_te']):
        continue
    if len(q['question_en']) < 15:
        continue
    verified_pool.append(q)

print(f"Total verified pool with detailed notes: {len(verified_pool)}")

# Check duplicate prevention against Mock 1 and Mock 2
with open('public/data/mock_test_full_200.json') as f:
    m1 = json.load(f)
with open('public/data/mock_test_full_200_2.json') as f:
    m2 = json.load(f)

used_en = set()
for q in m1['questions']:
    used_en.add(q.get('question_en', '').strip().lower()[:25])
for q in m2['questions']:
    used_en.add(q.get('question_en', '').strip().lower()[:25])

final_pool = []
for q in verified_pool:
    p = q['question_en'].strip().lower()[:25]
    if p not in used_en:
        final_pool.append(q)
        used_en.add(p)

print(f"Final clean unique pool: {len(final_pool)}")

# We will assign:
# Mock 3: 25 questions (Q101 to Q125)
# Mock 4: 25 questions (Q101 to Q125)
# Mock 5: 25 questions (Q101 to Q125)

mock3_ca = final_pool[0:25]
mock4_ca = final_pool[25:50]
mock5_ca = final_pool[50:75]

print(f"Selected: Mock 3 ({len(mock3_ca)}), Mock 4 ({len(mock4_ca)}), Mock 5 ({len(mock5_ca)})")

# Print sample from each
print("\n--- Sample Mock 3 (Q101) ---")
print("EN:", mock3_ca[0]['question_en'])
print("Ans:", mock3_ca[0]['options_en'][mock3_ca[0]['correct_option']])

print("\n--- Sample Mock 4 (Q101) ---")
print("EN:", mock4_ca[0]['question_en'])
print("Ans:", mock4_ca[0]['options_en'][mock4_ca[0]['correct_option']])

print("\n--- Sample Mock 5 (Q101) ---")
print("EN:", mock5_ca[0]['question_en'])
print("Ans:", mock5_ca[0]['options_en'][mock5_ca[0]['correct_option']])
