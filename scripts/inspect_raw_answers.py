import json

with open('/tmp/studynow_ca_2026_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('\x0c')

# Pages to inspect
test_pages = [
    1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
    37, 38, 39, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 75, 77, 87, 88, 89, 91, 92, 93,
    94, 96, 99, 100, 101, 103, 106, 107, 108, 109, 110, 114, 115, 117, 119, 121, 150, 164, 190, 200
]

for p in test_pages:
    if p <= len(pages):
        raw = pages[p-1].strip()
        lines = [l.strip() for l in raw.split('\n') if l.strip() and l != str(p) and 'LAST 6 MONTHS' not in l and l != 'StudyNow']
        print(f"=== PAGE {p} ===")
        for l in lines:
            print("  ", l)
