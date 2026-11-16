import re
import json

with open('/tmp/studynow_ca_2026_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('\x0c')

def has_telugu(s):
    return any('\u0c00' <= char <= '\u0c7f' for char in s)

for p_num in range(1, 11):
    page = pages[p_num - 1]
    raw_lines = [l.strip() for l in page.split('\n') if l.strip()]
    lines = [l for l in raw_lines if l != str(p_num) and 'LAST 6 MONTHS' not in l and l != 'StudyNow']
    
    # 1. English question: lines before first line starting with A.
    q_en_parts = []
    idx = 0
    while idx < len(lines):
        l = lines[idx]
        if re.match(r'^[A-D]\.\s*', l):
            break
        if has_telugu(l):
            break
        q_en_parts.append(l)
        idx += 1
    
    q_en = " ".join(q_en_parts)
    q_en = re.sub(r'^\d+[\.\)]\s*', '', q_en).strip()
    
    # Next, we look for English options A, B, C, D
    # and Telugu question & Telugu options & notes
    en_opts = {}
    te_opts = {}
    te_q_parts = []
    notes = []
    
    # State tracking
    found_te_q = False
    
    while idx < len(lines):
        l = lines[idx]
        m_en = re.match(r'^([A-D])\.\s*(.*)', l)
        m_te = re.match(r'^([ఎబిసిడి])\.\s*(.*)', l)
        
        if m_en:
            opt_letter = m_en.group(1)
            opt_val = m_en.group(2).strip()
            if not found_te_q and not has_telugu(opt_val):
                en_opts[opt_letter] = opt_val
            elif has_telugu(opt_val):
                te_opts[opt_letter] = opt_val
            else:
                # Could be second set of options or note
                if opt_letter not in en_opts:
                    en_opts[opt_letter] = opt_val
                else:
                    notes.append(l)
        elif m_te:
            te_letter_map = {'ఎ': 'A', 'బి': 'B', 'సి': 'C', 'డి': 'D'}
            let = te_letter_map[m_te.group(1)]
            te_opts[let] = m_te.group(2).strip()
        elif has_telugu(l):
            if not en_opts or len(en_opts) >= 2:
                if not te_opts:
                    te_q_parts.append(l)
                    found_te_q = True
                else:
                    notes.append(l)
            else:
                te_q_parts.append(l)
                found_te_q = True
        else:
            # English text after options
            notes.append(l)
        idx += 1
        
    te_q = " ".join(te_q_parts).strip()
    notes_str = "\n".join(notes)
    
    print(f"=== Question {p_num} ===")
    print(f"EN Q: {q_en}")
    print(f"EN Options: {en_opts}")
    print(f"TE Q: {te_q}")
    print(f"TE Options: {te_opts}")
    print(f"Notes:\n{notes_str}")
    print("-" * 50)
