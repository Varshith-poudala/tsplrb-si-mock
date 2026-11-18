#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebalance Mock 3 and Mock 4 to strict TSPLRB SI PWT Blueprint:
- 50 Arithmetic
- 50 Reasoning
- 100 General Studies:
  * 14 General Science
  * 16 Current Affairs
  * 14 Geography (India & Telangana)
  * 14 Economy (India & Telangana)
  * 17 Indian Polity & Governance
  * 13 Indian History & National Movement
  * 12 Telangana History & State Formation Movement
Total: 200 Questions
"""

import json
import os

print("=== REBALANCING MOCK 3 AND MOCK 4 ===")

# Load faculty curated bank for authentic Polity, TS Movement, and Economy questions
with open('public/data/faculty_curated_bank.json') as f:
    fc_data = json.load(f)
fc_qs = fc_data.get('questions', [])

print(f"Loaded {len(fc_qs)} faculty curated questions.")

def clean_q(q):
    # Ensure options are formatted
    opts_en = q.get('options_en') or (q['options'] if 'options' in q and isinstance(q['options'][0], str) else [o.get('text_en','') for o in q.get('options',[])])
    opts_te = q.get('options_te') or (q['options'] if 'options' in q and isinstance(q['options'][0], str) else [o.get('text_te','') for o in q.get('options',[])])
    
    return {
        "id": q.get('id') or q.get('qNumber'),
        "qNumber": q.get('qNumber') or q.get('id'),
        "section": q.get('section', 'General Studies'),
        "topic": q.get('topic', 'General Studies'),
        "question_en": q.get('question_en', '').strip(),
        "question_te": q.get('question_te', q.get('question_en', '')).strip(),
        "options_en": opts_en,
        "options_te": opts_te,
        "correct_option": q.get('correct_option', 0),
        "explanation_en": q.get('explanation_en', '').strip(),
        "explanation_te": q.get('explanation_te', '').strip()
    }

print("Helper ready.")
