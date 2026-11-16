import re

with open('/tmp/studynow_ca_2026_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('\x0c')
print(f"Total pages: {len(pages)}")

parsed_questions = []

for p_idx, page in enumerate(pages):
    lines = [l.strip() for l in page.split('\n') if l.strip()]
    if not lines:
        continue
    # Filter header
    content_lines = []
    for l in lines:
        if l == str(p_idx + 1) or 'LAST 6 MONTHS' in l or l == 'StudyNow':
            continue
        content_lines.append(l)
    
    if not content_lines:
        continue
    
    # Let's inspect the first line
    # Usually starts with number e.g. "1. Which State..." or just "Which State..." or "How Many..."
    parsed_questions.append({
        'page': p_idx + 1,
        'lines': content_lines
    })

print(f"Parsed {len(parsed_questions)} page blocks")
