import re
import json

with open('/tmp/studynow_ca_2026_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('\x0c')

def has_telugu(s):
    return any('\u0c00' <= char <= '\u0c7f' for char in s)

extracted = []

for p_idx, page in enumerate(pages):
    raw_lines = [l.strip() for l in page.split('\n') if l.strip()]
    if not raw_lines:
        continue
    
    # Filter header
    lines = []
    for l in raw_lines:
        if l == str(p_idx + 1) or 'LAST 6 MONTHS' in l or l == 'StudyNow':
            continue
        lines.append(l)
    
    if len(lines) < 5:
        continue

    # English question usually at top
    q_en_lines = []
    opt_en = {'A': '', 'B': '', 'C': '', 'D': ''}
    curr_opt = None
    
    # Let's find where Telugu question starts
    te_start_idx = -1
    for i, l in enumerate(lines):
        if has_telugu(l) and not (l.startswith(('A.', 'B.', 'C.', 'D.', 'ఎ.', 'బి.', 'సి.', 'డి.'))):
            te_start_idx = i
            break
    
    # If no Telugu question found, maybe Telugu is interleaved or later
    # Let's inspect line by line
    extracted.append({
        'page': p_idx + 1,
        'line_count': len(lines),
        'first_line': lines[0],
        'te_start_idx': te_start_idx
    })

print(f"Candidate question pages: {len(extracted)}")
