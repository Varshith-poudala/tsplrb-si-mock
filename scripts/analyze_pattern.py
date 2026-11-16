import re

with open('/tmp/studynow_ca_2026_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('\x0c')

for p_num in range(1, 25):
    page = pages[p_num - 1]
    lines = [l.strip() for l in page.split('\n') if l.strip()]
    content = [l for l in lines if l != str(p_num) and 'LAST 6 MONTHS' not in l and l != 'StudyNow']
    if not content:
        continue
    
    # Let's see English question lines
    # Option lines start with A., B., C., D.
    print(f"=== Page {p_num} ===")
    for idx, l in enumerate(content):
        print(f"[{idx}] {l}")

