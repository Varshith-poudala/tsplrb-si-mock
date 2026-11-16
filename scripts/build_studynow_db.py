import re
import json

with open('/tmp/studynow_ca_2026_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('\x0c')

def has_telugu(s):
    return any('\u0c00' <= char <= '\u0c7f' for char in s)

cleaned_questions = []

for p_idx, page in enumerate(pages):
    p_num = p_idx + 1
    raw_lines = [l.strip() for l in page.split('\n') if l.strip()]
    lines = [l for l in raw_lines if l != str(p_num) and 'LAST 6 MONTHS' not in l and l != 'StudyNow']
    if len(lines) < 4:
        continue

    # 1. English question: lines until first English option (A. ...)
    q_en_parts = []
    idx = 0
    while idx < len(lines):
        l = lines[idx]
        if re.match(r'^[A-D]\.\s*', l) or has_telugu(l):
            break
        q_en_parts.append(l)
        idx += 1
    
    q_en = " ".join(q_en_parts)
    q_en = re.sub(r'^\d+[\.\)]\s*', '', q_en).strip()
    
    # Skip if question is too short or is a summary slide
    if len(q_en) < 10 or 'Tableau Award' in q_en or 'New Governors' in q_en or 'PRARAMBH 2026' in q_en:
        continue

    en_opts = {}
    te_opts = {}
    te_q_parts = []
    notes = []
    
    found_te_q = False
    
    while idx < len(lines):
        l = lines[idx]
        m_en = re.match(r'^([A-D])\.\s*(.*)', l)
        m_te = re.match(r'^([A-Dఎబిసిడి])\.\s*(.*)', l)
        
        if has_telugu(l) and not m_te and not (found_te_q and len(te_opts) > 0):
            te_q_parts.append(l)
            found_te_q = True
        elif m_te and has_telugu(m_te.group(2)):
            let = m_te.group(1)
            te_map = {'ఎ': 'A', 'బి': 'B', 'సి': 'C', 'డి': 'D', 'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}
            let = te_map.get(let, let)
            te_opts[let] = m_te.group(2).strip()
        elif m_en and not has_telugu(m_en.group(2)):
            let = m_en.group(1)
            if let not in en_opts:
                en_opts[let] = m_en.group(2).strip()
            else:
                notes.append(l)
        else:
            if has_telugu(l):
                if te_opts and len(te_opts) < 4 and list(te_opts.keys())[-1]:
                    last_k = list(te_opts.keys())[-1]
                    te_opts[last_k] += " " + l
                else:
                    notes.append(l)
            else:
                notes.append(l)
        idx += 1

    te_q = " ".join(te_q_parts).strip()
    notes_text = " ".join(notes).strip()
    
    # If English options missing or incomplete, handle
    if len(en_opts) < 4:
        continue
        
    opts_en_list = [en_opts.get('A', ''), en_opts.get('B', ''), en_opts.get('C', ''), en_opts.get('D', '')]
    opts_te_list = [
        te_opts.get('A', opts_en_list[0]),
        te_opts.get('B', opts_en_list[1]),
        te_opts.get('C', opts_en_list[2]),
        te_opts.get('D', opts_en_list[3])
    ]
    
    # Match correct option
    correct_idx = 0
    # Clean up notes
    best_match = -1
    for opt_i, opt_val in enumerate(opts_en_list):
        if not opt_val:
            continue
        v_clean = opt_val.strip().lower()
        if len(v_clean) >= 3 and v_clean in notes_text.lower():
            best_match = opt_i
            break
            
    if best_match != -1:
        correct_idx = best_match
    else:
        m_ans = re.search(r'(?:ans|answer|correct)\s*[:\-–]?\s*([a-d])\b', notes_text, re.IGNORECASE)
        if m_ans:
            letter = m_ans.group(1).upper()
            correct_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}.get(letter, 0)

    cleaned_questions.append({
        'id': len(cleaned_questions) + 1,
        'page': p_num,
        'question_en': q_en,
        'question_te': te_q if te_q else q_en,
        'options_en': opts_en_list,
        'options_te': opts_te_list,
        'correct_option': correct_idx,
        'explanation_en': notes_text if notes_text else f"Correct Answer: {opts_en_list[correct_idx]}",
        'explanation_te': f"సరైన సమాధానం: {opts_te_list[correct_idx]}." + (f" ({notes_text})" if notes_text else "")
    })

print(f"Successfully cleaned: {len(cleaned_questions)} questions")
with open('public/data/reference_studynow_ca_2026.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_questions, f, ensure_ascii=False, indent=2)
