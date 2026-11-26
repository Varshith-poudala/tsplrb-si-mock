import json
from collections import Counter

def audit_and_patch_mock12():
    filepath = "public/data/mock_test_full_200_12.json"
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    qs = data["questions"]
    print("Initial Mock 12 count:", len(qs))
    print("Initial Correct Option Distribution:", Counter(q["correct_option"] for q in qs))

    # 1. Fix Q86 (Reasoning)
    # The word POLICEMAN has only one 'E'. 'PEACE' requires two 'E's, so it CANNOT be formed.
    q86 = qs[85]
    print("\nPatching Q86...")
    q86["options_en"][3] = "PEACE"
    q86["options_te"][3] = "PEACE"
    q86["correct_option"] = 3
    q86["explanation_en"] = "The word 'PEACE' requires two 'E's (P-E-A-C-E), but the word 'POLICEMAN' contains only one 'E'. Therefore, 'PEACE' cannot be formed from 'POLICEMAN'."
    q86["explanation_te"] = "సరైన సమాధానం: PEACE. ('POLICEMAN' పదంలో 'E' అక్షరం ఒక్కసారి మాత్రమే ఉంది, కానీ 'PEACE' పదానికి రెండు 'E'లు అవసరం. కాబట్టి ఈ పదాన్ని రూపొందించలేము.)"

    # 2. Fix Q195 (GS Current Affairs)
    # Fiscal Health Index 2026 was launched by NITI Aayog (Option 2)
    q195 = qs[194]
    print("Patching Q195...")
    q195["correct_option"] = 2
    q195["explanation_en"] = "NITI Aayog launched the Fiscal Health Index (FHI) to evaluate the fiscal management, revenue mobilisation, and debt sustainability of Indian states using CAG data. Top-performing states: 1. Odisha, 2. Goa, 3. Jharkhand. NE & Himalayan States: Arunachal Pradesh & Uttarakhand."
    q195["explanation_te"] = "సరైన సమాధానం: నీతి ఆయోగ్. (భారత రాష్ట్రాల ఆర్థిక నిర్వహణ, ఆదాయ సమీకరణ మరియు రుణ స్థిరత్వాన్ని అంచనా వేయడానికి నీతి ఆయోగ్ 'ఫిస్కల్ హెల్త్ ఇండెక్స్ 2026'ను విడుదల చేసింది. ఇందులో ఒడిశా 1వ స్థానంలో, గోవా 2వ స్థానంలో, జార్ఖండ్ 3వ స్థానంలో నిలిచాయి.)"

    # 3. Rebalance options in General Studies Q101 to Q188
    # Count fixed options from non-rebalanced questions: Q1-Q100 and Q189-Q200
    fixed_counts = Counter()
    for i, q in enumerate(qs):
        if not (100 <= i < 188 and q["correct_option"] == 0):
            fixed_counts[q["correct_option"]] += 1

    print("\nFixed counts from non-rebalanced questions:", fixed_counts)
    # Target is ~50 per option out of 200 questions
    needed = {k: 50 - fixed_counts[k] for k in range(4)}
    # Avoid negative numbers
    for k in needed:
        if needed[k] < 0:
            needed[k] = 0

    p0 = [0] * needed[0]
    p1 = [1] * needed[1]
    p2 = [2] * needed[2]
    p3 = [3] * needed[3]

    interleaved = []
    while p0 or p1 or p2 or p3:
        for p in [p3, p2, p0, p1]:
            if p:
                interleaved.append(p.pop(0))

    rebalanced_count = 0
    idx_target = 0
    for i in range(100, 188):
        q = qs[i]
        if q["correct_option"] == 0:
            tgt = interleaved[idx_target % len(interleaved)]
            idx_target += 1
            if tgt != 0:
                o_en = list(q["options_en"])
                o_te = list(q["options_te"])
                # Swap 0 and tgt
                o_en[0], o_en[tgt] = o_en[tgt], o_en[0]
                o_te[0], o_te[tgt] = o_te[tgt], o_te[0]
                q["options_en"] = o_en
                q["options_te"] = o_te
                q["correct_option"] = tgt
                
                # Make sure explanation_te cleanly highlights the correct option
                if not q["explanation_te"].startswith("సరైన సమాధానం:"):
                    q["explanation_te"] = f"సరైన సమాధానం: {o_te[tgt]}. ({q['explanation_te']})"
                
                rebalanced_count += 1
            else:
                if not q["explanation_te"].startswith("సరైన సమాధానం:"):
                    q["explanation_te"] = f"సరైన సమాధానం: {q['options_te'][0]}. ({q['explanation_te']})"

    print(f"Successfully rebalanced {rebalanced_count} questions in GS.")
    final_dist = Counter(q["correct_option"] for q in qs)
    print("Final Mock 12 Overall Correct Option Distribution:", final_dist)

    # 4. Save updated mock 12
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved changes to {filepath}")

    # 5. Sync to scripts/mock12_gs.py
    gs_qs = [q for q in qs if q.get("section") == "General Studies" or 101 <= q.get("qNumber", 0) <= 200]
    with open("scripts/mock12_gs.py", "w", encoding="utf-8") as f:
        f.write("mock12_gs = " + json.dumps(gs_qs, ensure_ascii=False, indent=4) + "\n")
    print("Synced to scripts/mock12_gs.py")

if __name__ == "__main__":
    audit_and_patch_mock12()
