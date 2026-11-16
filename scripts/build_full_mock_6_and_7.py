import json
import os
import re

print("Initializing creation of Mock 6 and Mock 7...")

# 1. Load fresh 2026 CA from StudyNow
with open('public/data/reference_studynow_ca_2026.json') as f:
    studynow = json.load(f)

excluded_keywords = [
    'khelo india', 'payal nag', 'quadruple amputee', 'asian wrestling', 'fastest century', 'finn allen',
    'all england', 'lin chun-yi', 'under-19', 'sooryavanshi', 'chinese grand prix', 'antonelli',
    'delhi open', 'sakellaridis', 't20 world cup', 'australian open', 'alcaraz', 'ranji trophy',
    'winter olympics', 'santosh trophy', 'women’s premier league', 'wpl', 'vijay hazare', 'vidarbha',
    '94th chess', 'mayank chakraborty', 'syed mushtaq', 'world happiness', 'press freedom',
    'sipri', 'renewable energy', 'corruption perceptions', 'qs asia', 'swaminathan award',
    'bafta', 'boong', 'grammy', 'meditations', 'dalai lama', 'paperless district court',
    'kalpetta', 'social media', 'alwar', 'musical road', 'namo bharat', 'rrts',
    'ai-enabled state university', 'ccsu', 'glass suspension bridge', 'bajrang setu',
    'underwater tunnel', 'nitin nabin', 'henley passport', 'vizhinjam', 'hydrogen train',
    'national science day', 'surya kant', 'raja subramani', 'praveen kumar', 'praveen vashista',
    'one case one data', 'su sahay', 'army day', 'micro gpu', 'dilution refrigerator',
    'amaravati quantum', 'qdenga', '1.5 tesla', 'sameer', 'nexcar19', 'ring one', 'muse wearables',
    'rambilli', 'green ammonia', 'kakinada', 'hydrogen fuel cell', 'water positive',
    'matsya 6000', 'agnibaan', 'agnilet', 'vande bharat sleeper', 'wings india', 'pm mitra',
    'orvakal', 'drone city', 'ramsar', 'surha tal', 'global peace index', 'french open',
    'solicitor general', 'earth prize', 'g7 summit', 'norway chess', 'whitley', 'fifa world cup 2026',
    'wimbledon', 'japan open', 'world junior squash', 'happy city', 'green hydrogen summit'
]

fresh_ca = []
for q in studynow:
    full = (q['question_en'] + " " + q['explanation_en']).lower()
    if any(k in full for k in excluded_keywords):
        continue
    if len(q['explanation_en']) > 20 and not q['explanation_en'].startswith('Correct Answer:'):
        fresh_ca.append(q)

print(f"Total fresh 2026 CA candidates available: {len(fresh_ca)}")

