import json
import os
import sys

sys.path.append('scripts')
from questions_pool import GEOGRAPHY_POOL, ECONOMY_POOL, POLITY_POOL, HISTORY_POOL

print("=== REBALANCING PHASES 2 & 3 (MOCKS 2, 5, 6, 7, 8, 9) ===")

# Load faculty curated bank
with open('public/data/faculty_curated_bank.json') as f:
    fc_qs = json.load(f).get('questions', [])

polity_fc = [q for q in fc_qs if 'polity' in q.get('subject', '').lower()]
tsm_fc = [q for q in fc_qs if 'movement' in q.get('subject', '').lower() or 'movement' in q.get('topic', '').lower() or 'telangana history' in q.get('subject', '').lower()]

def make_q(q_num, section, topic, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
    return {
        "id": q_num,
        "qNumber": q_num,
        "section": section,
        "topic": topic,
        "question_en": q_en.strip(),
        "question_te": q_te.strip(),
        "options_en": [str(o).strip() for o in opts_en],
        "options_te": [str(o).strip() for o in opts_te],
        "correct_option": corr,
        "explanation_en": exp_en.strip(),
        "explanation_te": exp_te.strip()
    }

def rebalance_mock_file(test_id, filename):
    filepath = os.path.join('public', 'data', filename)
    with open(filepath) as f:
        data = json.load(f)
    raw_qs = data.get('questions', data)
    
    print(f"\nProcessing {filename} (current length: {len(raw_qs)})...")
    
    new_qs = []
    
    # 1. Part A: Arithmetic (Q1-Q50)
    for i in range(50):
        q = raw_qs[i].copy()
        q['id'] = i + 1
        q['qNumber'] = i + 1
        q['section'] = 'Arithmetic'
        new_qs.append(q)
        
    # 2. Part B: Reasoning (Q51-Q100)
    for i in range(50, 100):
        q = raw_qs[i].copy()
        q['id'] = i + 1
        q['qNumber'] = i + 1
        q['section'] = 'Reasoning'
        new_qs.append(q)
        
    # 3. Part C: General Studies (Q101-Q200) - Exact 100 Blueprint:
    # -------------------------------------------------------------
    # (a) Q101-Q114 (14 Qs): General Science
    # Find up to 14 science questions in raw_qs or create
    sci_found = []
    for q in raw_qs[100:]:
        txt = (q.get('question_en', '') + ' ' + q.get('topic', '')).lower()
        if any(k in txt for k in ['physics', 'chemistry', 'biology', 'vitamin', 'disease', 'acid', 'metal', 'isro', 'drdo', 'satellite', 'sound', 'light', 'lens', 'plant', 'cell', 'blood', 'organ']):
            sci_found.append(q)
            if len(sci_found) == 14: break
            
    while len(sci_found) < 14:
        # fallback from raw_qs Q101-Q114
        sci_found.append(raw_qs[100 + len(sci_found)])
        
    for idx, sq in enumerate(sci_found[:14]):
        q = sq.copy()
        q_num = 101 + idx
        q['id'] = q_num
        q['qNumber'] = q_num
        q['section'] = 'General Studies'
        new_qs.append(q)
        
    # (b) Q115-Q130 (16 Qs): Current Affairs
    ca_found = []
    for q in raw_qs[100:]:
        txt = (q.get('question_en', '') + ' ' + q.get('topic', '')).lower()
        if any(k in txt for k in ['current affairs', 'summit', 'award', '2024', '2025', '2026', 'minister', 'chief justice', 'brics', 'sco', 'olympics', 'cup', 'scheme']):
            if q not in sci_found and q not in ca_found:
                ca_found.append(q)
                if len(ca_found) == 16: break
                
    while len(ca_found) < 16:
        ca_found.append(raw_qs[114 + len(ca_found)])
        
    for idx, cq in enumerate(ca_found[:16]):
        q = cq.copy()
        q_num = 115 + idx
        q['id'] = q_num
        q['qNumber'] = q_num
        q['section'] = 'General Studies'
        new_qs.append(q)
        
    # (c) Q131-Q144 (14 Qs): Geography of India & Telangana
    # Inject from GEOGRAPHY_POOL
    for idx, gq in enumerate(GEOGRAPHY_POOL[:14]):
        q_num = 131 + idx
        new_qs.append(make_q(
            q_num, 'General Studies', gq['topic'],
            gq['question_en'], gq['question_te'],
            gq['options_en'], gq['options_te'],
            gq['correct_option'], gq['explanation_en'], gq['explanation_te']
        ))
        
    # (d) Q145-Q158 (14 Qs): Economy of India & Telangana
    # Inject from ECONOMY_POOL
    for idx, eq in enumerate(ECONOMY_POOL[:14]):
        q_num = 145 + idx
        new_qs.append(make_q(
            q_num, 'General Studies', eq['topic'],
            eq['question_en'], eq['question_te'],
            eq['options_en'], eq['options_te'],
            eq['correct_option'], eq['explanation_en'], eq['explanation_te']
        ))
        
    # (e) Q159-Q175 (17 Qs): Indian Polity & Governance
    polity_found = []
    for q in raw_qs[100:]:
        txt = (q.get('question_en', '') + ' ' + q.get('topic', '')).lower()
        if any(k in txt for k in ['polity', 'constitution', 'article ', 'amendment', 'lok sabha', 'rajya sabha', 'president', 'supreme court', 'high court', 'governor', 'fundamental right', 'dpsp', 'panchayat']):
            if q not in sci_found and q not in ca_found:
                polity_found.append(q)
                if len(polity_found) == 17: break
                
    # If not enough, fill from POLITY_POOL & faculty bank
    pool_idx = 0
    while len(polity_found) < 17 and pool_idx < len(POLITY_POOL):
        polity_found.append(POLITY_POOL[pool_idx])
        pool_idx += 1
    fc_idx = 0
    while len(polity_found) < 17 and fc_idx < len(polity_fc):
        polity_found.append(polity_fc[fc_idx])
        fc_idx += 1
        
    for idx, pq in enumerate(polity_found[:17]):
        q = pq.copy()
        q_num = 159 + idx
        q['id'] = q_num
        q['qNumber'] = q_num
        q['section'] = 'General Studies'
        new_qs.append(q)
        
    # (f) Q176-Q188 (13 Qs): Indian History & National Movement
    # Inject from HISTORY_POOL
    for idx, hq in enumerate(HISTORY_POOL[:13]):
        q_num = 176 + idx
        new_qs.append(make_q(
            q_num, 'General Studies', hq['topic'],
            hq['question_en'], hq['question_te'],
            hq['options_en'], hq['options_te'],
            hq['correct_option'], hq['explanation_en'], hq['explanation_te']
        ))
        
    # (g) Q189-Q200 (12 Qs): Telangana History, Culture & State Formation
    tsm_found = []
    for q in raw_qs[100:]:
        txt = (q.get('question_en', '') + ' ' + q.get('topic', '')).lower()
        if any(k in txt for k in ['movement', 'mulki', '1969', 'fazal ali', 'gentlemen', 'telangana agitation', 'appointed day', 'operation polo', 'million march', 'satavahana', 'kakatiya', 'qutb shahi', 'asaf jahi', 'bathukamma', 'bonalu']):
            if q not in sci_found and q not in ca_found and q not in polity_found:
                tsm_found.append(q)
                if len(tsm_found) == 12: break
                
    fc_t_idx = 0
    while len(tsm_found) < 12 and fc_t_idx < len(tsm_fc):
        tsm_found.append(tsm_fc[fc_t_idx])
        fc_t_idx += 1
        
    for idx, tq in enumerate(tsm_found[:12]):
        q = tq.copy()
        q_num = 189 + idx
        q['id'] = q_num
        q['qNumber'] = q_num
        q['section'] = 'General Studies'
        new_qs.append(q)
        
    print(f"Result for {filename}: {len(new_qs)} questions assembled.")
    assert len(new_qs) == 200, f"Error: {len(new_qs)} != 200"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump({"testId": test_id, "questions": new_qs}, f, ensure_ascii=False, indent=2)
    print(f"✅ Successfully rebalanced {filename}")

# Execute Phase 2 & 3
targets = [
    ('tsplrb-si-mock-full-200-7', 'mock_test_full_200_7.json'),
    ('tsplrb-si-mock-full-200-8', 'mock_test_full_200_8.json'),
    ('tsplrb-si-mock-full-200-9', 'mock_test_full_200_9.json'),
    ('tsplrb-si-mock-full-200-2', 'mock_test_full_200_2.json'),
    ('tsplrb-si-mock-full-200-5', 'mock_test_full_200_5.json'),
    ('tsplrb-si-mock-full-200-6', 'mock_test_full_200_6.json'),
]

for t_id, fname in targets:
    rebalance_mock_file(t_id, fname)

print("\n🎉 ALL MOCK FILES REBALANCED SUCCESSFULLY!")
