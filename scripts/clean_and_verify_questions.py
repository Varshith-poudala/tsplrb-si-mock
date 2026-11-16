import re
import json

with open('/tmp/studynow_ca_2026_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('\x0c')

def has_telugu(s):
    return any('\u0c00' <= char <= '\u0c7f' for char in s)

verified_questions = []

for p_idx, page in enumerate(pages):
    p_num = p_idx + 1
    raw_lines = [l.strip() for l in page.split('\n') if l.strip()]
    lines = [l for l in raw_lines if l != str(p_num) and 'LAST 6 MONTHS' not in l and l != 'StudyNow']
    if len(lines) < 4:
        continue

    # English question lines until first A.
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
    
    if len(q_en) < 10 or 'Tableau Award' in q_en or 'New Governors' in q_en or 'PRARAMBH 2026' in q_en:
        continue

    # Options parsing
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
            val = m_te.group(2).strip()
            
            # Check if this line contains inline options like 'బి. ... సి. ...'
            inline_splits = re.split(r'\s+([బిసిడిBCDbcd])\.\s*', val)
            if len(inline_splits) > 1:
                te_opts[let] = inline_splits[0].strip()
                for i in range(1, len(inline_splits), 2):
                    sub_let = te_map.get(inline_splits[i], inline_splits[i].upper())
                    te_opts[sub_let] = inline_splits[i+1].strip()
            else:
                te_opts[let] = val
        elif m_en and not has_telugu(m_en.group(2)):
            let = m_en.group(1)
            if let not in en_opts:
                en_opts[let] = m_en.group(2).strip()
            else:
                notes.append(l)
        else:
            if has_telugu(l):
                # Check for inline telugu options inside a line
                inline_splits = re.split(r'\s+([బిసిడిBCDbcd])\.\s*', l)
                if len(inline_splits) > 1 and len(te_opts) > 0:
                    for i in range(1, len(inline_splits), 2):
                        te_map = {'ఎ': 'A', 'బి': 'B', 'సి': 'C', 'డి': 'D', 'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}
                        sub_let = te_map.get(inline_splits[i], inline_splits[i].upper())
                        te_opts[sub_let] = inline_splits[i+1].strip()
                else:
                    notes.append(l)
            else:
                notes.append(l)
        idx += 1

    if len(en_opts) < 4:
        continue

    te_q = " ".join(te_q_parts).strip()
    notes_text = " ".join(notes).strip()
    
    opts_en_list = [en_opts.get('A', ''), en_opts.get('B', ''), en_opts.get('C', ''), en_opts.get('D', '')]
    opts_te_list = [
        te_opts.get('A', opts_en_list[0]),
        te_opts.get('B', opts_en_list[1]),
        te_opts.get('C', opts_en_list[2]),
        te_opts.get('D', opts_en_list[3])
    ]
    
    # Precise Answer Detection
    # Look for high-priority markers first:
    # 1. Champion / Winner / Champions
    correct_idx = 0
    ans_found = False
    
    # Priority patterns in notes
    priority_patterns = [
        r'(?:champion|champions|winner|winners)\s*[:\-–]?\s*([^\n\r\.\,\–]+)',
        r'(?:rank|ind\s*rank|ind‘s\s*rank|ind’s\s*rank)\s*[:\-–\→]?\s*([^\n\r\.\,\–]+)',
        r'(?:singles|men’s singles|women’s singles)\s*[:\-–]?\s*([^\n\r\.\,\–\(]+)',
        r'(?:gold|gold in)\s*[:\-–]?\s*([^\n\r\.\,\–]+)',
        r'(?:inaugurated by|launched by|appointed as|president)\s*[:\-–\→]?\s*([^\n\r\.\,\–]+)',
        r'(?:where|held in)\s*[:\-–]?\s*([^\n\r\.\,\–]+)'
    ]
    
    for pat in priority_patterns:
        m = re.search(pat, notes_text, re.IGNORECASE)
        if m:
            target_str = m.group(1).strip().lower()
            for opt_i, opt_val in enumerate(opts_en_list):
                if opt_val.lower().strip() in target_str or (len(opt_val) >= 4 and opt_val.lower().strip() in target_str):
                    correct_idx = opt_i
                    ans_found = True
                    break
        if ans_found:
            break
            
    if not ans_found:
        # Match option text anywhere in notes (excluding host/runner-up if possible)
        for opt_i, opt_val in enumerate(opts_en_list):
            v = opt_val.strip().lower()
            if len(v) >= 4 and v in notes_text.lower():
                # make sure it's not preceded by 'runner-up' or 'defeated'
                if not re.search(r'(?:runners?-up|defeated|runner up)\s*[:\-–]?\s*' + re.escape(v), notes_text.lower()):
                    correct_idx = opt_i
                    ans_found = True
                    break
                    
    verified_questions.append({
        'page': p_num,
        'question_en': q_en,
        'question_te': te_q if te_q else q_en,
        'options_en': opts_en_list,
        'options_te': opts_te_list,
        'correct_option': correct_idx,
        'explanation_en': notes_text if notes_text else f"Correct Answer: {opts_en_list[correct_idx]}",
        'explanation_te': f"సరైన సమాధానం: {opts_te_list[correct_idx]}." + (f" ({notes_text})" if notes_text else "")
    })

print(f"Total verified questions: {len(verified_questions)}")
with open('/tmp/studynow_verified.json', 'w', encoding='utf-8') as f:
    json.dump(verified_questions, f, ensure_ascii=False, indent=2)
