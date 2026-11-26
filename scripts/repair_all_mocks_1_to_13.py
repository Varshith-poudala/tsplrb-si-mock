#!/usr/bin/env python3
"""
Master QA Repair & Rebalance Script for Mock Tests 1-13,
master_aptitude_reasoning_bank.json, and reference_studynow_ca_2026.json.

Fixes:
1. All broken math/logic premises & wrong answer keys across Mocks 1-11, 13, and Master Bank.
2. All leaked draft/scratchpad notes ("Wait...", "Let's make...") in explanations.
3. All StudyNow PDF OCR-garbled Telugu strings, merged inline options, and leaked English phrases.
4. Safe option-slot rebalancing across skewed mocks (Mocks 1, 2, 4, 5, 6, 7, 8, 9, 10, 11)
   while strictly preserving anchored options ("All of the above", "(A)-(D)", "Option A", etc.).
"""
import glob
import json
import os
import re
from collections import Counter

ANCHOR_RE = re.compile(
    r"\b(?:all of the above|none of the above|both\s*\(?[ab1]\s*(?:and|&)\s*[bc2]|"
    r"neither\s*\(?[ab1]|option\s*[a-d1-4]|choice\s*[a-d1-4])\b|\([A-D]\)|"
    r"(?:పైవన్నీ|పైవేవీ కావు|పై రెండు|ఎ మరియు బి)",
    re.I,
)


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def patch_qs_by_key(questions, patch_map, id_field="qNumber"):
    updated = 0
    for q in questions:
        k = q.get(id_field, q.get("id"))
        if k in patch_map:
            for field, val in patch_map[k].items():
                q[field] = val
            updated += 1
    return updated


def rebalance_mock(questions):
    """Balance correct_option counts close to 50 each (within 15%-35%) without touching anchored questions."""
    dist = Counter(q["correct_option"] for q in questions)
    total = len(questions)
    max_p = max(dist.values()) / total * 100
    min_p = min(dist.get(i, 0) for i in range(4)) / total * 100
    if max_p <= 35.0 and min_p >= 15.0:
        return False, dist

    # Identify anchored vs movable indices
    fixed_counts = Counter()
    movable_indices = []
    for i, q in enumerate(questions):
        blob = (
            q.get("question_en", "")
            + " "
            + q.get("question_te", "")
            + " "
            + " ".join(q.get("options_en", []))
            + " "
            + " ".join(q.get("options_te", []))
            + " "
            + q.get("explanation_en", "")
        )
        if ANCHOR_RE.search(blob):
            fixed_counts[q["correct_option"]] += 1
        else:
            movable_indices.append(i)

    # Target ~50 per option out of 200
    target_per_opt = total // 4
    needed = {k: max(0, target_per_opt - fixed_counts[k]) for k in range(4)}
    # Trim or pad pool to match len(movable_indices)
    pool = []
    for k in range(4):
        pool.extend([k] * needed[k])
    while len(pool) < len(movable_indices):
        least = min(range(4), key=lambda x: fixed_counts[x] + pool.count(x))
        pool.append(least)
    while len(pool) > len(movable_indices):
        most = max(range(4), key=lambda x: pool.count(x))
        pool.remove(most)

    # Sort pool smoothly interleaved by cycling options
    buckets = {k: [k] * pool.count(k) for k in range(4)}
    interleaved = []
    while any(buckets.values()):
        for k in (0, 1, 2, 3):
            if buckets[k]:
                interleaved.append(buckets[k].pop())

    for idx, tgt in zip(movable_indices, interleaved):
        q = questions[idx]
        curr = q["correct_option"]
        if curr != tgt:
            o_en = list(q["options_en"])
            o_te = list(q["options_te"])
            o_en[curr], o_en[tgt] = o_en[tgt], o_en[curr]
            o_te[curr], o_te[tgt] = o_te[tgt], o_te[curr]
            q["options_en"] = o_en
            q["options_te"] = o_te
            q["correct_option"] = tgt

    new_dist = Counter(q["correct_option"] for q in questions)
    return True, new_dist


# -------------------------------------------------------------------------
# 1. MASTER APTITUDE & REASONING BANK PATCHES (public/data/master_aptitude_reasoning_bank.json)
# -------------------------------------------------------------------------
MASTER_BANK_PATCHES = {
    12: {
        "explanation_en": (
            "Distance sound travels in (12 - 11 = 1) minute equals distance the car travels in 11 minutes. "
            "Speed_car * 11 = 330 * 1 => Speed_car = 30 m/s = 30 * (18/5) = 108 km/h."
        ),
    },
    25: {
        "explanation_en": (
            "Let downstream speed be D and upstream speed be U. 36/D + 24/U = 6 and 48/D + 40/U = 9. "
            "Solving gives D = 12 km/h and U = 8 km/h. Speed of stream = (D - U)/2 = (12 - 8)/2 = 2 km/h."
        ),
    },
    132: {
        "question_en": (
            "A reward of Rs. 3,250 is divided among four police personnel P, Q, R, and S such that "
            "P's share / Q's share = Q's share / R's share = R's share / S's share = 2/3. What is the share received by P?"
        ),
        "question_te": (
            "రూ. 3,250 రివార్డును నలుగురు పోలీస్ సిబ్బంది P, Q, R మరియు S లకు "
            "P వాటా / Q వాటా = Q వాటా / R వాటా = R వాటా / S వాటా = 2/3 అయ్యేలా పంచారు. P పొందిన వాటా ఎంత?"
        ),
        "options_en": ["Rs. 360", "Rs. 480", "Rs. 240", "Rs. 400"],
        "options_te": ["రూ. 360", "రూ. 480", "రూ. 240", "రూ. 400"],
        "correct_option": 3,
        "explanation_en": (
            "P : Q = Q : R = R : S = 2 : 3. Combining gives P : Q : R : S = 8 : 12 : 18 : 27. "
            "Total parts = 8 + 12 + 18 + 27 = 65. P's share = (8 / 65) * 3250 = 8 * 50 = Rs. 400."
        ),
        "explanation_te": (
            "సరైన సమాధానం: రూ. 400. (ఉమ్మడి నిష్పత్తి P : Q : R : S = 8 : 12 : 18 : 27, మొత్తం = 65 భాగాలు. "
            "P వాటా = (8 / 65) * 3250 = రూ. 400.)"
        ),
    },
    148: {
        "question_en": (
            "A starts a venture with an investment of Rs. 50,000. After 4 months, B joins with Rs. 60,000, "
            "while A withdraws Rs. 15,000 from his capital. At the end of the year, the total profit earned is Rs. 88,000. "
            "What is A's share of the profit?"
        ),
        "question_te": (
            "A రూ. 50,000 పెట్టుబడితో ఒక వ్యాపారాన్ని ప్రారంభించాడు. 4 నెలల తర్వాత B రూ. 60,000 తో చేరగా, "
            "A తన పెట్టుబడి నుండి రూ. 15,000 ఉపసంహరించుకున్నాడు. సంవత్సరాంతంలో మొత్తం లాభం రూ. 88,000 అయితే, A వాటా ఎంత?"
        ),
        "options_en": ["Rs. 42,000", "Rs. 40,000", "Rs. 48,000", "Rs. 44,000"],
        "options_te": ["రూ. 42,000", "రూ. 40,000", "రూ. 48,000", "రూ. 44,000"],
        "correct_option": 3,
        "explanation_en": (
            "A's equivalent monthly capital = (50,000 * 4) + (35,000 * 8) = 200,000 + 280,000 = Rs. 480,000. "
            "B's equivalent capital = 60,000 * 8 = Rs. 480,000. Ratio A : B = 1 : 1. A's share = 88,000 / 2 = Rs. 44,000."
        ),
        "explanation_te": (
            "A పెట్టుబడి = (50,000 * 4) + (35,000 * 8) = 4,80,000. B పెట్టుబడి = 60,000 * 8 = 4,80,000. "
            "నిష్పత్తి = 1 : 1. కాబట్టి A వాటా = 88,000 / 2 = రూ. 44,000."
        ),
    },
    197: {
        "question_en": (
            "A defective clock loses 16 minutes in 24 hours. It was set right at 12 noon on Monday. "
            "What is the true time when the clock indicates 5:00 AM on the following Friday?"
        ),
        "question_te": (
            "ఒక లోపభూయిష్ట గడియారం ప్రతి 24 గంటలకు 16 నిమిషాలు వెనుకబడుతుంది. సోమవారం మధ్యాహ్నం 12 గంటలకు దానిని సరిచేశారు. "
            "ఆ తర్వాత వచ్చే శుక్రవారం ఉదయం 5:00 గంటలను ఆ గడియారం చూపినప్పుడు అసలు సరైన సమయం ఎంత?"
        ),
        "options_en": ["5:45 AM on Friday", "6:00 AM on Friday", "6:15 AM on Friday", "5:30 AM on Friday"],
        "options_te": ["శుక్రవారం ఉదయం 5:45", "శుక్రవారం ఉదయం 6:00", "శుక్రవారం ఉదయం 6:15", "శుక్రవారం ఉదయం 5:30"],
        "correct_option": 1,
        "explanation_en": (
            "Defective clock covers 23 hrs 44 mins (356/15 hrs) for every 24 true hours, so True / Defective = 24 / (356/15) = 90 / 89. "
            "Elapsed defective time from Monday 12:00 noon to Friday 5:00 AM = 89 hours. "
            "True elapsed time = (90 / 89) * 89 = 90 hours, which is 6:00 AM on Friday."
        ),
        "explanation_te": (
            "సరైన సమాధానం: శుక్రవారం ఉదయం 6:00. (లోపభూయిష్ట గడియారం 89 గంటలు = అసలు సమయం 90 గంటలు. "
            "సోమవారం మధ్యాహ్నం 12 నుండి 90 గంటలు అనగా శుక్రవారం ఉదయం 6:00 అవుతుంది.)"
        ),
    },
    205: {
        "options_en": ["2:15", "1:45", "1:15", "2:45"],
        "options_te": ["2:15", "1:45", "1:15", "2:45"],
        "correct_option": 0,
        "explanation_en": "Water image formula: Subtract the given time from 18:30 (when minutes <= 30). 18:30 - 4:15 = 14:15 = 2:15.",
        "explanation_te": "సరైన సమాధానం: 2:15. (గడియారపు నీటి ప్రతిబింబ సూత్రం: 18:30 - 4:15 = 14:15 = 2:15.)",
    },
    256: {
        "options_en": ["E", "D", "B", "C"],
        "options_te": ["E", "D", "B", "C"],
        "correct_option": 1,
        "explanation_en": (
            "Placing officers counter-clockwise around positions 1 to 8 facing centre: A=1, C=6 (3rd left of A), "
            "E=4 (since C is 2nd right of E), B=8 (2nd right of C). D cannot sit next to A (2,8) or C (5,7), so D=3. "
            "F=5 (2nd right of D), G=2 (not next to C), leaving H=7. Position 7 (H) is directly opposite Position 3 (D)."
        ),
        "explanation_te": (
            "సరైన సమాధానం: D. (కూర్చున్న క్రమం ప్రకారం 1:A, 2:G, 3:D, 4:E, 5:F, 6:C, 7:H, 8:B. కాబట్టి H (7) కి ఎదురుగా D (3) ఉంటాడు.)"
        ),
    },
    260: {
        "options_en": ["P", "R", "S", "Q"],
        "options_te": ["P", "R", "S", "Q"],
        "correct_option": 1,
        "explanation_en": (
            "Order from top (7) to bottom (1): 7:R, 6:P, 5:Q, 4:U, 3:S, 2:V, 1:T. "
            "Here R is immediately above P; Q and U sit between P and S; V is immediately below S; T is at the bottom. "
            "Therefore, Box R is at the top-most position."
        ),
        "explanation_te": (
            "సరైన సమాధానం: R. (పై నుండి కిందకు అమరిక: 7:R, 6:P, 5:Q, 4:U, 3:S, 2:V, 1:T. కాబట్టి అన్నింటికంటే పైన R పెట్టె ఉంటుంది.)"
        ),
    },
    276: {
        "options_en": ["KLORXV", "KQRNXV", "LROPYV", "KRORXV"],
        "options_te": ["KLORXV", "KQRNXV", "LROPYV", "KRORXV"],
        "correct_option": 0,
        "explanation_en": (
            "Each letter is replaced by its opposite alphabetical letter (sum of positions = 27): "
            "P->K, O->L, L->O, I->R, C->X, E->V. Hence POLICE is coded as KLORXV."
        ),
    },
    279: {
        "question_en": "If 'COP' = 34 and 'DSP' = 39, what will be the code for 'SI'?",
        "question_te": "'COP' = 34 మరియు 'DSP' = 39 అయితే, 'SI' యొక్క సంఖ్యా కోడ్ ఎంత?",
        "explanation_en": (
            "Sum of alphabetical positional values: C(3) + O(15) + P(16) = 34, and D(4) + S(19) + P(16) = 39. "
            "Therefore, SI = S(19) + I(9) = 28."
        ),
    },
    280: {
        "question_en": (
            "In a special code, vowels are replaced by their immediate next vowel (A->E, E->I, I->O, O->U, U->A) "
            "and consonants are replaced by the immediate next letter in the alphabet (+1). How is 'PRISON' coded?"
        ),
        "question_te": (
            "ఒక ప్రత్యేక కోడ్‌లో అచ్చులను వాటి తర్వాతి అచ్చుతోను (A->E, E->I, I->O, O->U, U->A), "
            "హల్లులను వాటి తర్వాతి అక్షరంతోను (+1) మార్చారు. 'PRISON' అనే పదం ఎలా కోడ్ చేయబడుతుంది?"
        ),
        "options_en": ["OPPTON", "QSOTUP", "NPOUNM", "OQOUOM"],
        "options_te": ["OPPTON", "QSOTUP", "NPOUNM", "OQOUOM"],
        "correct_option": 1,
        "explanation_en": (
            "Consonants (+1) and vowels (next vowel): P(+1)=Q, R(+1)=S, I->O, S(+1)=T, O->U, N(+1)=P => QSOTUP."
        ),
        "explanation_te": (
            "సరైన సమాధానం: QSOTUP. (హల్లులకు +1 మరియు అచ్చులకు తర్వాతి అచ్చు వేయగా: P->Q, R->S, I->O, S->T, O->U, N->P => QSOTUP.)"
        ),
    },
    285: {
        "question_en": "If 'BEAT' is coded as 'GJFY', what is the pattern and how will 'SOUP' be coded?",
        "question_te": "'BEAT' ను 'GJFY' గా కోడ్ చేస్తే, అదే విధానంలో 'SOUP' ను ఎలా కోడ్ చేస్తారు?",
        "explanation_en": (
            "Each letter is shifted forward by +5: B(+5)=G, E(+5)=J, A(+5)=F, T(+5)=Y => GJFY. "
            "Applying +5 to SOUP: S(19)+5=X, O(15)+5=T, U(21)+5=Z, P(16)+5=U => XTZU."
        ),
    },
    288: {
        "question_en": "If 'LEAD' is written as 'EBFM', how is 'GOLD' written in that same cipher code?",
        "question_te": "'LEAD' ను 'EBFM' గా రాస్తే, అదే కోడ్‌లో 'GOLD' ను ఎలా రాస్తారు?",
        "explanation_en": (
            "Reverse the word LEAD -> DAEL, then add +1 to each letter: D+1=E, A+1=B, E+1=F, L+1=M => EBFM. "
            "Applying the same rule to GOLD: Reverse -> DLOG; add +1 to each letter -> EMPH."
        ),
    },
    289: {
        "correct_option": 0,
        "explanation_en": (
            "Input: 45 12 78 34 89. Step 1: 12 45 78 34 89 (12 moved left). Step 2: 12 34 45 78 89 (34 moved left). "
            "The sequence is now completely sorted in ascending order in 2 steps."
        ),
    },
    291: {
        "correct_option": 2,
        "explanation_en": (
            "Word: I N V E S T I G A T I O N. Interchanging adjacent pairs: (1,2)->NI, (3,4)->EV, (5,6)->TS, (7,8)->GI. "
            "Hence, the 7th letter from the left is G."
        ),
    },
    298: {
        "question_en": (
            "A patrol vehicle drives 12 km North from a police station, then turns right and drives 8 km, "
            "and finally turns right and drives 6 km South. How far and in which direction is the vehicle from the police station?"
        ),
        "question_te": (
            "ఒక పెట్రోలింగ్ వాహనం పోలీస్ స్టేషన్ నుండి ఉత్తరం వైపు 12 కి.మీ ప్రయాణించి, కుడివైపు తిరిగి 8 కి.మీ, "
            "చివరగా కుడివైపు తిరిగి 6 కి.మీ దక్షిణం వైపు ప్రయాణించింది. ఆ వాహనం పోలీస్ స్టేషన్ నుండి ఎంత దూరంలో మరియు ఏ దిశలో ఉంది?"
        ),
        "explanation_en": (
            "Net North displacement = 12 - 6 = 6 km North. Net East displacement = 8 km East. "
            "Shortest distance = sqrt(6^2 + 8^2) = sqrt(36 + 64) = 10 km, North-East."
        ),
    },
    309: {
        "correct_option": 0,
        "explanation_en": (
            "Around the square table facing centre, P is opposite R, so S must sit opposite Q. "
            "Since S faces North, Q sits directly opposite S and faces South."
        ),
    },
}


# -------------------------------------------------------------------------
# 2. PER-MOCK SPECIFIC QUESTION PATCHES
# -------------------------------------------------------------------------
MOCK_PATCHES = {
    "public/data/mock_test_full_200.json": {
        5: {
            "correct_option": 0,
            "explanation_en": (
                "Required greatest divisor = HCF(148 - 4, 246 - 6, 623 - 11) = HCF(144, 240, 612). "
                "Since 144 = 12 * 12, 240 = 12 * 20, and 612 = 12 * 51 (with gcd(12, 20, 51) = 1), HCF = 12. "
                "(All remainders 4, 6, 11 are strictly less than 12)."
            ),
            "explanation_te": "సరైన సమాధానం: 12. (HCF(144, 240, 612) = 12. కావున గరిష్ట సంఖ్య 12.)",
        },
        84: {
            "options_en": ["32F", "32Y", "32Z", "32W"],
            "options_te": ["32F", "32Y", "32Z", "32W"],
            "correct_option": 0,
            "explanation_en": (
                "Numbers double each step: 2, 4, 8, 16, 32. Letters also correspond to doubling alphabetical positions "
                "(mod 26): B(2), D(4), H(8), P(16), next 16 * 2 = 32; wrapping past 26 gives 32 - 26 = 6th letter F => 32F."
            ),
            "explanation_te": (
                "సరైన సమాధానం: 32F. (సంఖ్యలు రెట్టింపు అవుతున్నాయి: 2, 4, 8, 16, 32. "
                "అక్షర స్థానాలు రెట్టింపు అవుతూ 26 తర్వాత మళ్ళీ A నుండి లెక్కిస్తే 16*2 = 32 -> 32-26 = 6వ అక్షరం F => 32F.)"
            ),
        },
    },
    "public/data/mock_test_full_200_2.json": {
        63: {
            "question_en": "LOCKER : KNBJDQ :: GLOBAL : ?",
            "question_te": "LOCKER : KNBJDQ :: GLOBAL : ?",
            "explanation_en": (
                "Each letter is shifted by -1: L(-1)=K, O(-1)=N, C(-1)=B, K(-1)=J, E(-1)=D, R(-1)=Q => KNBJDQ. "
                "Applying -1 to GLOBAL: G(-1)=F, L(-1)=K, O(-1)=N, B(-1)=A, A(-1)=Z, L(-1)=K => FKNAZK."
            ),
        },
        67: {
            "question_en": "Find the odd letter pair: EV, GT, JQ, MO",
            "question_te": "కింది వాటిలో భిన్నమైన అక్షరాల జతను గుర్తించండి: EV, GT, JQ, MO",
            "options_en": ["MO", "EV", "GT", "JQ"],
            "options_te": ["MO", "EV", "GT", "JQ"],
            "correct_option": 0,
            "explanation_en": (
                "Opposite letter pairs sum to 27: E(5)+V(22)=27, G(7)+T(20)=27, J(10)+Q(17)=27. "
                "However, M(13)+O(15)=28, so MO is the odd pair out."
            ),
        },
        71: {
            "question_en": (
                "If 'P + Q' means P is the mother of Q, 'P - Q' means P is the sister of Q, and 'P * Q' means P is the brother of Q. "
                "Which of the following means 'M is the maternal uncle of T'?"
            ),
            "question_te": (
                "'P + Q' అంటే P అనునది Q యొక్క తల్లి, 'P - Q' అంటే P అనునమె Q యొక్క సోదరి, మరియు 'P * Q' అంటే P అనునతడు Q యొక్క సోదరుడు. "
                "అయితే 'M అనునతడు T యొక్క మేనమామ' అని క్రింది వాటిలో ఏది తెలియజేస్తుంది?"
            ),
            "explanation_en": (
                "In 'M * K + T', M * K means M is the brother of K, and K + T means K is the mother of T. "
                "Therefore, M is the brother of T's mother, making M the maternal uncle of T."
            ),
        },
    },
    "public/data/mock_test_full_200_3.json": {
        5: {
            "correct_option": 0,
            "explanation_en": (
                "Required greatest divisor = HCF(148 - 4, 246 - 6, 623 - 11) = HCF(144, 240, 612). "
                "Since 144 = 12 * 12, 240 = 12 * 20, and 612 = 12 * 51 (with gcd(12, 20, 51) = 1), HCF = 12."
            ),
            "explanation_te": "సరైన సమాధానం: 12. (HCF(144, 240, 612) = 12. కావున గరిష్ట సంఖ్య 12.)",
        },
    },
    "public/data/mock_test_full_200_5.json": {
        64: {
            "options_en": ["32F", "32Y", "32Z", "32W"],
            "options_te": ["32F", "32Y", "32Z", "32W"],
            "correct_option": 0,
            "explanation_en": (
                "Numbers double each step: 2, 4, 8, 16, 32. Letters also correspond to doubling alphabetical positions "
                "(mod 26): B(2), D(4), H(8), P(16), next 16 * 2 = 32; wrapping past 26 gives 32 - 26 = 6th letter F => 32F."
            ),
            "explanation_te": (
                "సరైన సమాధానం: 32F. (సంఖ్యలు రెట్టింపు అవుతున్నాయి: 2, 4, 8, 16, 32. "
                "అక్షర స్థానాలు రెట్టింపు అవుతూ 26 తర్వాత మళ్ళీ A నుండి లెక్కిస్తే 16*2 = 32 -> 6వ అక్షరం F => 32F.)"
            ),
        },
    },
    "public/data/mock_test_full_200_6.json": {
        117: {
            "question_te": "భారతదేశపు మొట్టమొదటి పూర్తిగా కాగిత రహిత జిల్లా కోర్టు (Paperless District Court) ఏ రాష్ట్రంలో ప్రారంభించబడింది?",
            "options_te": ["బీహార్", "గుజరాత్", "మహారాష్ట్ర", "కేరళ"],
            "explanation_te": "సరైన సమాధానం: కేరళ. (భారత ప్రధాన న్యాయమూర్తి జస్టిస్ సూర్యకాంత్ కేరళలోని వయనాడ్ జిల్లా కల్పెట్టాలో దేశంలోనే తొలి కాగిత రహిత జిల్లా కోర్టును ప్రారంభించారు.)",
        },
        119: {
            "question_en": "Which Country Became The First In Europe To Pass A Law Banning Social Media For Children Under 15?",
            "question_te": "ఐరోపాలో 15 ఏళ్లలోపు పిల్లలకు సోషల్ మీడియాను నిషేధించే చట్టాన్ని ఆమోదించిన మొదటి దేశం ఏది?",
            "options_te": ["ఫ్రాన్స్", "జర్మనీ", "స్పెయిన్", "ఇటలీ"],
            "correct_option": 0,
            "explanation_en": "France became the first country in Europe (EU) to pass a statutory ban on social media for children under 15, following Australia's world-first under-16 ban.",
            "explanation_te": "సరైన సమాధానం: ఫ్రాన్స్. (ఆస్ట్రేలియా తర్వాత ఐరోపాలో 15 ఏళ్లలోపు పిల్లలకు సోషల్ మీడియాను నిషేధించే చట్టాన్ని ఆమోదించిన మొదటి దేశంగా ఫ్రాన్స్ నిలిచింది.)",
        },
        121: {
            "question_te": "భారతదేశంలో 'బర్డ్ అట్లాస్' (పక్షుల అట్లాస్) ను ప్రచురించిన రెండవ రాష్ట్రం ఏది?",
            "options_te": ["గోవా", "తమిళనాడు", "కర్ణాటక", "ఒడిశా"],
            "explanation_te": "సరైన సమాధానం: గోవా. (భారతదేశంలో కేరళ మొదటి రాష్ట్రంగా నిలవగా, గోవా రెండవ రాష్ట్రంగా బర్డ్ అట్లాస్‌ను ప్రచురించింది.)",
        },
        122: {
            "question_te": "భారతదేశంలో 100% బీమా కవరేజీని సాధించిన మొదటి జిల్లా ఏది?",
            "options_te": ["ఇండోర్", "జైపూర్", "సూరత్", "అల్వార్"],
            "explanation_te": "సరైన సమాధానం: అల్వార్. ('అందరికీ బీమా 2047' లక్ష్యంలో భాగంగా రాజస్థాన్‌లోని అల్వార్ జిల్లా దేశంలో 100% బీమా కవరేజీ సాధించిన తొలి జిల్లాగా నిలిచింది.)",
        },
        123: {
            "question_te": "భారతదేశపు మొట్టమొదటి మ్యూజికల్ రోడ్ (Musical Road) ఏ నగరంలో ప్రారంభించబడింది?",
            "options_te": ["ముంబై", "పూణే", "బెంగళూరు", "అహ్మదాబాద్"],
            "explanation_te": "సరైన సమాధానం: ముంబై. (ముంబై కోస్టల్ రోడ్డుపై వాహనాలు నిర్దిష్ట వేగంతో వెళ్ళినప్పుడు 'జై హో' గీతం వినిపించే దేశంలోనే తొలి మ్యూజికల్ రోడ్డును ప్రారంభించారు.)",
        },
        124: {
            "question_en": "India’s First Namo Bharat Rapid Rail Transit System Connects Which Two Cities?",
            "question_te": "భారతదేశపు మొట్టమొదటి 'నమో భారత్' రాపిడ్ రైల్ ట్రాన్సిట్ వ్యవస్థ ఏ రెండు నగరాలను కలుపుతుంది?",
            "options_te": ["ఢిల్లీ – జైపూర్", "ఢిల్లీ – మీరట్", "ఢిల్లీ – చండీగఢ్", "ఢిల్లీ – ఆగ్రా"],
            "explanation_te": "సరైన సమాధానం: ఢిల్లీ – మీరట్. (ప్రధానమంత్రి నరేంద్ర మోదీ ప్రారంభించిన భారతదేశపు తొలి నమో భారత్ రాపిడ్ రైల్ (RRTS) కారిడార్ ఢిల్లీ మరియు మీరట్‌లను కలుపుతుంది.)",
        },
        126: {
            "question_te": "వాణిజ్యపరంగా బయో-బిటుమెన్ (Bio-Bitumen) ను ఉత్పత్తి చేసిన ప్రపంచంలోనే మొదటి దేశం ఏది?",
            "options_te": ["చైనా", "జపాన్", "భారతదేశం", "ఫ్రాన్స్"],
            "explanation_te": "సరైన సమాధానం: భారతదేశం. (పంట అవశేషాల నుండి లిగ్నిన్ ద్వారా వాణిజ్యపరంగా బయో-బిటుమెన్‌ను ఉత్పత్తి చేసిన ప్రపంచంలోనే తొలి దేశంగా భారతదేశం నిలిచింది.)",
        },
        130: {
            "question_te": "భారతదేశపు మొట్టమొదటి అటవీ విశ్వవిద్యాలయం (Forest University) ఎక్కడ ఏర్పాటు కానుంది?",
            "options_te": ["జబల్‌పూర్", "డెహ్రాడూన్", "షిల్లాంగ్", "గోరఖ్‌పూర్"],
            "explanation_te": "సరైన సమాధానం: గోరఖ్‌పూర్. (ఉత్తరప్రదేశ్‌లోని గోరఖ్‌పూర్‌లో భారతదేశపు మొట్టమొదటి అటవీ విశ్వవిద్యాలయాన్ని ఏర్పాటు చేయనున్నారు.)",
        },
    },
    "public/data/mock_test_full_200_7.json": {
        125: {
            "question_te": "2026 ప్రొఫెసర్ ఎం.ఎస్. స్వామినాథన్ అవార్డును ఎవరు అందుకున్నారు?",
            "options_te": ["డాక్టర్ సిహెచ్. శ్రీనివాసరావు", "రతన్ లాల్", "ఎం.ఎస్. స్వామినాథన్", "అశోక్ గులాటీ"],
            "explanation_te": "సరైన సమాధానం: డాక్టర్ సిహెచ్. శ్రీనివాసరావు. (భారత హరిత విప్లవ పితామహుడు ఎం.ఎస్. స్వామినాథన్ పేరిట ఇచ్చే 2026 ప్రతిష్టాత్మక అవార్డును డాక్టర్ సిహెచ్. శ్రీనివాసరావు అందుకున్నారు.)",
        },
        127: {
            "question_te": "\"ఏబెల్ ప్రైజ్ 2026\" (Abel Prize 2026) పురస్కారాన్ని ఎవరు పొందారు?",
            "options_te": ["డెన్నిస్ పి. సుల్లివన్", "గెర్డ్ ఫాల్టింగ్స్", "లూయిస్ కాఫరెల్లి", "మసాకి కాశీవారా"],
            "explanation_te": "సరైన సమాధానం: గెర్డ్ ఫాల్టింగ్స్. (గణితశాస్త్ర నోబెల్‌గా పిలువబడే 2026 ఏబెల్ ప్రైజ్‌ను జర్మన్ గణిత శాస్త్రవేత్త గెర్డ్ ఫాల్టింగ్స్ గెలుచుకున్నారు.)",
        },
        128: {
            "question_te": "2025 సంవత్సరానికి గాను 60వ జ్ఞానపీఠ అవార్డు ఎవరికి లభించింది?",
            "options_te": ["ఆర్. వైరముత్తు", "నరేష్ మెహతా", "లీలాధర్ మండలోయ్", "నాగార్జున్"],
            "explanation_te": "సరైన సమాధానం: ఆర్. వైరముత్తు. (భారతదేశపు అత్యున్నత సాహిత్య పురస్కారమైన 60వ జ్ఞానపీఠ అవార్డు (2025) తమిళ కవి మరియు గీత రచయిత ఆర్. వైరముత్తుకు లభించింది.)",
        },
        129: {
            "question_te": "స్టాక్‌హోమ్ వాటర్ ప్రైజ్ 2026ను ఎవరు గెలుచుకున్నారు?",
            "options_te": ["గుంటర్ బ్లోష్ల్", "రోజర్ ఫాల్కనర్", "సునీతా నరైన్", "కావేహ్ మదాని"],
            "explanation_te": "సరైన సమాధానం: కావేహ్ మదాని. ('జల నోబెల్'గా పిలువబడే స్టాక్‌హోమ్ వాటర్ ప్రైజ్ 2026ను ఇరానియన్ శాస్త్రవేత్త కావేహ్ మదాని గెలుచుకున్నారు.)",
        },
        159: {
            "question_en": "Which State Police Has Been Awarded With The President’s Police Colour Award 2026?",
            "question_te": "ఏ రాష్ట్ర పోలీసులకు 'ప్రెసిడెంట్స్ పోలీస్ కలర్ అవార్డు (నిషాన్) 2026' లభించింది?",
            "options_te": ["సిక్కిం", "అస్సాం", "మేఘాలయ", "బీహార్"],
            "explanation_en": "The President’s Police Colour (Nishaan), the highest ceremonial honour granted to a state police force, was awarded to the Sikkim Police in 2026.",
            "explanation_te": "సరైన సమాధానం: సిక్కిం. (పోలీస్ దళాలకు ఇచ్చే అత్యున్నత గౌరవమైన 'ప్రెసిడెంట్స్ పోలీస్ కలర్' అవార్డును 2026లో సిక్కిం పోలీసులకు ప్రదానం చేశారు.)",
        },
    },
    "public/data/mock_test_full_200_8.json": {
        2: {
            "question_en": (
                "If the 8-digit number 789x531y is divisible by 72, what is the value of (6x + 3y) for the largest possible value of y?"
            ),
            "question_te": (
                "789x531y అనే 8-అంకెల సంఖ్య 72 చేత నిశ్శేషంగా భాగించబడినచో, y యొక్క గరిష్ట విలువకు (6x + 3y) విలువ ఎంత?"
            ),
            "explanation_en": (
                "For divisibility by 72 (= 8 * 9), the last 3 digits 31y must be divisible by 8. The only digit making 31y divisible by 8 is y = 2 (312 / 8 = 39). "
                "For divisibility by 9, sum of digits = 7 + 8 + 9 + x + 5 + 3 + 1 + 2 = 35 + x must be a multiple of 9, so x = 1 (36). "
                "Therefore, 6x + 3y = 6(1) + 3(2) = 12."
            ),
            "explanation_te": (
                "సరైన సమాధానం: 12. (72 = 8 * 9. 8 చే భాగించబడాలంటే చివరి మూడు అంకెలు 312 కావాలి కనుక y = 2. "
                "9 చే భాగించబడాలంటే అంకెల మొత్తం 35 + x = 36 కావాలి కనుక x = 1. కాబట్టి 6x + 3y = 6(1) + 3(2) = 12.)"
            ),
        },
    },
    "public/data/mock_test_full_200_9.json": {
        13: {
            "question_en": (
                "P, Q, and R enter into a partnership with investments in the ratio 4 : 5 : 6. After 4 months, P withdraws 25% of his capital, "
                "while Q increases his capital by 20%. If the total annual profit is ₹72,000, find R's share of profit."
            ),
            "question_te": (
                "P, Q మరియు R లు 4 : 5 : 6 నిష్పత్తిలో పెట్టుబడులతో భాగస్వామ్య వ్యాపారాన్ని ప్రారంభించారు. 4 నెలల తర్వాత P తన పెట్టుబడిలో 25% ఉపసంహరించుకోగా, "
                "Q తన పెట్టుబడిని 20% పెంచెను. మొత్తం వార్షిక లాభం ₹72,000 అయితే R యొక్క వాటా ఎంత?"
            ),
            "explanation_en": (
                "Monthly equivalent shares: P = 4*4 + 3*8 = 40; Q = 5*4 + 6*8 = 68; R = 6*12 = 72. "
                "Ratio P : Q : R = 40 : 68 : 72 = 10 : 17 : 18 (Total = 45 parts). "
                "R's share = (18 / 45) * 72,000 = (2/5) * 72,000 = ₹28,800."
            ),
            "explanation_te": (
                "సరైన సమాధానం: ₹28,800. (పెట్టుబడి నిష్పత్తి P : Q : R = 40 : 68 : 72 = 10 : 17 : 18. "
                "మొత్తం 45 భాగాలలో R వాటా = (18 / 45) * 72,000 = ₹28,800.)"
            ),
        },
        15: {
            "question_en": (
                "In an election between two candidates, 10% of the voters did not cast their vote, and 250 votes were declared invalid. "
                "The winning candidate secured 54% of the valid votes and won by a majority of 304 votes. Find the total number of voters enrolled on the voter list."
            ),
            "question_te": (
                "ఇద్దరు అభ్యర్థుల మధ్య జరిగిన ఎన్నికలో 10% మంది ఓటర్లు ఓటు వేయలేదు మరియు 250 ఓట్లు చెల్లనివిగా తేలాయి. "
                "గెలిచిన అభ్యర్థికి చెల్లుబాటు అయిన ఓట్లలో 54% వచ్చి 304 ఓట్ల మెజారిటీతో గెలిచాడు. ఓటర్ల జాబితాలోని మొత్తం ఓటర్ల సంఖ్య ఎంత?"
            ),
            "explanation_en": (
                "Winner's majority margin = 54% - 46% = 8% of valid votes = 304 => Valid votes = 304 / 0.08 = 3,800. "
                "Total votes cast = 3,800 + 250 = 4,050, which equals 90% of enrolled voters. Total voters = 4,050 / 0.90 = 4,500."
            ),
            "explanation_te": (
                "సరైన సమాధానం: 4,500. (మెజారిటీ 8% = 304 => చెల్లుబాటు అయిన ఓట్లు = 3,800. "
                "పోల్ అయిన ఓట్లు = 3,800 + 250 = 4,050 (90%). కాబట్టి మొత్తం నమోదిత ఓటర్లు = 4,500.)"
            ),
        },
        54: {
            "question_en": (
                "Four number-pairs are given, of which three are alike in a certain way and one is different. Select the odd one out:\n"
                "(A) 12 : 142\n(B) 14 : 192\n(C) 16 : 252\n(D) 18 : 320"
            ),
            "question_te": (
                "క్రింది నాలుగు జతలలో మూడు ఒకే నియమాన్ని పాటిస్తాయి, ఒకటి భిన్నంగా ఉంటుంది. ఆ భిన్నమైన జతను గుర్తించండి:\n"
                "(A) 12 : 142\n(B) 14 : 192\n(C) 16 : 252\n(D) 18 : 320"
            ),
            "options_en": ["12 : 142", "14 : 192", "16 : 252", "18 : 320"],
            "options_te": ["12 : 142", "14 : 192", "16 : 252", "18 : 320"],
            "correct_option": 0,
            "explanation_en": (
                "Three pairs follow the rule n : (n^2 - 4): 14^2 - 4 = 192, 16^2 - 4 = 252, and 18^2 - 4 = 320. "
                "However, 12^2 - 4 = 140 (not 142), making 12 : 142 the odd pair."
            ),
            "explanation_te": "సరైన సమాధానం: 12 : 142. (మిగిలిన మూడు జతలు n^2 - 4 సూత్రాన్ని పాటిస్తాయి, కానీ 12^2 - 4 = 140 అవుతుంది, 142 కాదు.)",
        },
        76: {
            "question_en": (
                "Which set of letters when sequentially placed at the gaps in the given letter series shall complete it?\n"
                "a _ c a b _ _ b c a _ c"
            ),
            "question_te": (
                "ఇచ్చిన అక్షర శ్రేణిలోని ఖాళీలలో వరుసగా ఉంచితే శ్రేణి పూర్తయ్యే అక్షరాల సమూహం ఏది?\n"
                "a _ c a b _ _ b c a _ c"
            ),
            "explanation_en": (
                "Placing 'b c a b' in the gaps yields: a [b] c | a b [c] | [a] b c | a [b] c, forming a clean repeating 3-letter block 'a b c'."
            ),
            "explanation_te": "సరైన సమాధానం: b c a b. ('b c a b' ఉంచగా 'a b c / a b c / a b c / a b c' అని పునరావృత శ్రేణి వస్తుంది.)",
        },
        125: {
            "question_te": "IPLలో 200 వికెట్లు తీసిన మొదటి ఫాస్ట్ బౌలర్ ఎవరు?",
            "options_te": ["భువనేశ్వర్ కుమార్", "జస్‌ప్రీత్ బుమ్రా", "మహమ్మద్ షమీ", "ఉమేష్ యాదవ్"],
            "explanation_te": "సరైన సమాధానం: భువనేశ్వర్ కుమార్. (ఐపీఎల్ చరిత్రలో 200 వికెట్లు పడగొట్టిన మొట్టమొదటి ఫాస్ట్ బౌలర్‌గా భువనేశ్వర్ కుమార్ నిలిచారు.)",
        },
        126: {
            "question_te": "పారా ఆర్చరీలో అంతర్జాతీయ స్వర్ణ పతకం సాధించిన మొదటి 'క్వాడ్రపుల్ యాంపుటీ' (నాలుగు అవయవాలు లేని క్రీడాకారిణి) ఎవరు?",
            "options_te": ["పాయల్ నాగ్", "శీతల్ దేవి", "దీపా మాలిక్", "అవని లేఖరా"],
            "explanation_te": "సరైన సమాధానం: పాయల్ నాగ్. (ఒడిశాకు చెందిన పారా ఆర్చర్ పాయల్ నాగ్ వరల్డ్ ఆర్చరీ పారా సిరీస్‌లో శీతల్ దేవిని ఓడించి స్వర్ణ పతకం గెలుచుకున్నారు.)",
        },
        127: {
            "question_te": "2026 ఆసియా రెజ్లింగ్ ఛాంపియన్‌షిప్‌లో భారత్ మొత్తం ఎన్ని పతకాలను గెలుచుకుంది?",
            "explanation_te": "సరైన సమాధానం: 17. (కిర్గిస్తాన్‌లోని బిష్కెక్‌లో జరిగిన 2026 ఆసియా రెజ్లింగ్ ఛాంపియన్‌షిప్‌లో భారత్ 2 స్వర్ణం, 7 రజతం, 8 కాంస్యంతో సహా మొత్తం 17 పతకాలు గెలుచుకుంది.)",
        },
        128: {
            "question_te": "2026 T20 ప్రపంచ కప్ చరిత్రలో అత్యంత వేగవంతమైన సెంచరీని ఎవరు సాధించారు?",
            "options_te": ["గ్లెన్ మాక్స్‌వెల్", "జోస్ బట్లర్", "ఫిన్ అలెన్", "విరాట్ కోహ్లీ"],
            "explanation_te": "సరైన సమాధానం: ఫిన్ అలెన్. (న్యూజిలాండ్ క్రికెటర్ ఫిన్ అలెన్ దక్షిణాఫ్రికాపై కేవలం 33 బంతుల్లో సెంచరీ బాది T20 ప్రపంచ కప్ రికార్డు సృష్టించాడు.)",
        },
        129: {
            "question_te": "ఆల్ ఇంగ్లాండ్ ఓపెన్ బ్యాడ్మింటన్ 2026లో పురుషుల సింగిల్స్ విజేత ఎవరు?",
            "options_te": ["లిన్ చున్-యి", "విక్టర్ అక్సెల్సెన్", "లీ జీ జియా", "లక్ష్య సేన్"],
            "explanation_te": "సరైన సమాధానం: లిన్ చున్-యి. (ఆల్ ఇంగ్లాండ్ ఓపెన్ 2026 ఫైనల్‌లో భారత ఆటగాడు లక్ష్య సేన్‌ను ఓడించి లిన్ చున్-యి టైటిల్ గెలుచుకున్నాడు.)",
        },
        130: {
            "question_te": "2026 ICC అండర్-19 పురుషుల క్రికెట్ ప్రపంచ కప్‌ను ఏ దేశం గెలుచుకుంది?",
            "options_te": ["భారతదేశం", "ఇంగ్లాండ్", "ఆస్ట్రేలియా", "శ్రీలంక"],
            "explanation_te": "సరైన సమాధానం: భారతదేశం. (జింబాబ్వే మరియు నమీబియా ఆతిథ్యం ఇచ్చిన 2026 అండర్-19 ప్రపంచ కప్ ఫైనల్‌లో ఇంగ్లాండ్‌ను ఓడించి భారత్ రికార్డు స్థాయిలో 6వ టైటిల్ గెలుచుకుంది.)",
        },
    },
    "public/data/mock_test_full_200_10.json": {
        31: {
            "explanation_en": (
                "Let coins be 5x, 9x, 4x. Total value in rupees = 5x*(0.50) + 9x*(0.25) + 4x*(0.10) = 5.15x = 206 => x = 40. "
                "Total coins = (5 + 9 + 4) * 40 = 18 * 40 = 720."
            ),
        },
        32: {
            "explanation_en": (
                "Ratio of investment * time = (45000 * 12) : (60000 * 8) = 540 : 480 = 9 : 8 (Total = 17 parts). "
                "B's share = (8 / 17) * 51,000 = 8 * 3,000 = ₹24,000."
            ),
        },
        33: {
            "explanation_en": (
                "Milk = 75 * (4/5) = 60 L and Water = 15 L. Let x litres of water be added so ratio becomes 2 : 1. "
                "60 / (15 + x) = 2 / 1 => 15 + x = 30 => x = 15 litres."
            ),
        },
        39: {
            "explanation_en": (
                "Unit digit of 3^167: 167 mod 4 = 3 => 3^3 = 27 (unit digit 7). "
                "Unit digit of 7^153: 153 mod 4 = 1 => 7^1 = 7. Product = 7 * 7 = 49 => Unit digit = 9."
            ),
        },
        56: {
            "question_en": "In a certain code language, 'POLICE' is coded as 'QNMHDD'. Following the exact same rule, how will 'DETECT' be coded in that language?",
            "question_te": "ఒక నిర్దిష్ట కోడ్ భాషలో 'POLICE' ను 'QNMHDD' గా కోడ్ చేశారు. అదే నియమం ప్రకారం 'DETECT' ను ఎలా కోడ్ చేస్తారు?",
            "explanation_en": (
                "Alternating +1, -1, +1, -1, +1, -1 pattern: P(+1)Q, O(-1)N, L(+1)M, I(-1)H, C(+1)D, E(-1)D => QNMHDD. "
                "Applying to DETECT: D(+1)E, E(-1)D, T(+1)U, E(-1)D, C(+1)D, T(-1)S => EDUDDS."
            ),
        },
        57: {
            "question_en": "If 'DELHI' is coded as 38 and 'MUMBAI' is coded as 59, what is the code for 'HYDERABAD' in that system?",
            "question_te": "'DELHI' ని 38 గాను మరియు 'MUMBAI' ని 59 గాను కోడ్ చేస్తే, అదే విధానంలో 'HYDERABAD' యొక్క కోడ్ ఎంత?",
            "explanation_en": (
                "Sum of alphabetical positions: D(4)+E(5)+L(12)+H(8)+I(9) = 38; M(13)+U(21)+M(13)+B(2)+A(1)+I(9) = 59. "
                "For HYDERABAD: H(8)+Y(25)+D(4)+E(5)+R(18)+A(1)+B(2)+A(1)+D(4) = 68."
            ),
        },
        97: {
            "explanation_en": (
                "Each letter shifts forward by +1: J->K, U->V, S->T, T->U, I->J, C->D, E->F => KVTUJDF. "
                "Applying +1 to HONEST: H->I, O->P, N->O, E->F, S->T, T->U => IPOFTU."
            ),
        },
    },
    "public/data/mock_test_full_200_11.json": {
        31: {
            "explanation_en": (
                "Let total profit = P. A gets 0.10P (salary), leaving 0.90P divided in ratio 3:2. "
                "A's total share = 0.10P + (3/5)*0.90P = 0.64P = ₹64,000 => P = 64,000 / 0.64 = ₹1,00,000."
            ),
        },
        36: {
            "explanation_en": (
                "88 = 8 * 11. For divisibility by 8, last 3 digits 8y6 must be divisible by 8 => y in {1, 5, 9}. "
                "Using the alternating sum rule for 11 on 342x18y6 gives (6+8+x+4) - (y+1+2+3) = 12 + x - y. "
                "With y = 5, 12 + x - 5 = 7 + x => x = 4 (giving 11). Thus x * y = 4 * 5 = 20 (matching the options)."
            ),
        },
        84: {
            "question_en": "Which interchange of signs will make the equation '12 * 6 + 3 - 10 / 2 = 25' correct?",
            "question_te": "క్రింది ఏ చిహ్నాల మార్పిడి వలన '12 * 6 + 3 - 10 / 2 = 25' సమీకరణం సరైనదవుతుంది?",
            "correct_option": 0,
            "explanation_en": (
                "Interchanging '+' and '*' transforms '12 * 6 + 3 - 10 / 2' into '12 + 6 * 3 - 10 / 2' "
                "= 12 + 18 - 5 = 25, making the equation correct."
            ),
            "explanation_te": "సరైన సమాధానం: + మరియు *. ('+' మరియు '*' చిహ్నాలను మార్చగా: 12 + 6 * 3 - 10 / 2 = 12 + 18 - 5 = 25.)",
        },
        189: {
            "question_te": "2026 చైనీస్ గ్రాండ్ ప్రిక్స్ (Chinese Grand Prix 2026) ను ఎవరు గెలుచుకున్నారు?",
            "options_te": ["మాక్స్ వెర్స్టాపెన్", "లూయిస్ హామిల్టన్", "ఆండ్రియా కిమి ఆంటోనెల్లి", "చార్లెస్ లెక్లెర్క్"],
            "explanation_en": "19-year-old Andrea Kimi Antonelli (Italy) won the 2026 Chinese Grand Prix, becoming the second-youngest race winner in Formula 1 history.",
            "explanation_te": "సరైన సమాధానం: ఆండ్రియా కిమి ఆంటోనెల్లి. (ఇటలీకి చెందిన 19 ఏళ్ల ఆండ్రియా కిమి ఆంటోనెల్లి 2026 చైనీస్ గ్రాండ్ ప్రిక్స్‌ను గెలుచుకుని ఫార్ములా 1 చరిత్రలో రెండవ అత్యంత పిన్న వయస్కుడైన విజేతగా నిలిచారు.)",
        },
        190: {
            "question_te": "ఢిల్లీ ఓపెన్ 2026 టెన్నిస్ టోర్నీలో సింగిల్స్ టైటిల్‌ను ఎవరు గెలుచుకున్నారు?",
            "options_te": ["స్టెఫానోస్ సకెల్లారిడిస్", "ఆలివర్ క్రాఫోర్డ్", "జే క్లార్క్", "రే సకమోటో"],
            "explanation_te": "సరైన సమాధానం: స్టెఫానోస్ సకెల్లారిడిస్. (ఢిల్లీ ఓపెన్ 2026 టెన్నిస్ టోర్నమెంట్ సింగిల్స్ టైటిల్‌ను గ్రీస్ ఆటగాడు స్టెఫానోస్ సకెల్లారిడిస్ గెలుచుకున్నాడు.)",
        },
        191: {
            "question_en": "Which Country Won The Title Of ‘2026 ICC Men’s T20 World Cup’?",
            "question_te": "2026 ICC పురుషుల T20 ప్రపంచ కప్ టైటిల్‌ను ఏ దేశం గెలుచుకుంది?",
            "options_te": ["ఆస్ట్రేలియా", "భారతదేశం", "దక్షిణాఫ్రికా", "బంగ్లాదేశ్"],
            "explanation_en": "India won the 10th edition of the 2026 ICC Men's T20 World Cup (their 3rd title), defeating New Zealand in the final at Narendra Modi Stadium, Ahmedabad.",
            "explanation_te": "సరైన సమాధానం: భారతదేశం. (అహ్మదాబాద్‌లోని నరేంద్ర మోదీ స్టేడియంలో జరిగిన 2026 ICC పురుషుల T20 ప్రపంచ కప్ ఫైనల్‌లో న్యూజిలాండ్‌ను ఓడించి భారతదేశం తమ 3వ టైటిల్‌ను గెలుచుకుంది.)",
        },
        192: {
            "question_te": "2026 ICC పురుషుల T20 ప్రపంచ కప్‌లో 'ప్లేయర్ ఆఫ్ ది సిరీస్'గా ఎవరు ఎంపికయ్యారు?",
            "options_te": ["విరాట్ కోహ్లీ", "సంజు శాంసన్", "సూర్యకుమార్ యాదవ్", "జో రూట్"],
            "correct_option": 1,
            "explanation_en": "Sanju Samson was named Player of the Series (Tournament) in the 2026 ICC Men’s T20 World Cup after scoring 321 runs in 5 innings (avg 80.25), including twin 89s in the semi-final and final.",
            "explanation_te": "సరైన సమాధానం: సంజు శాంసన్. (2026 ICC పురుషుల T20 ప్రపంచ కప్‌లో 5 ఇన్నింగ్స్‌లలో 321 పరుగులు చేసి, సెమీ-ఫైనల్ మరియు ఫైనల్‌లో 89 పరుగులతో మెరిసిన సంజు శాంసన్ ప్లేయర్ ఆఫ్ ది టోర్నమెంట్‌గా ఎంపికయ్యారు.)",
        },
        194: {
            "question_en": "Who Won the Men’s Singles Title At “Australian Open 2026”?",
            "question_te": "\"ఆస్ట్రేలియన్ ఓపెన్ 2026\" పురుషుల సింగిల్స్ టైటిల్‌ను ఎవరు గెలుచుకున్నారు?",
            "options_te": ["రాఫెల్ నాదల్", "కార్లోస్ అల్కరాజ్", "రింకీ హిజికాటా", "మెద్వెదేవ్"],
            "explanation_te": "సరైన సమాధానం: కార్లోస్ అల్కరాజ్. (ఆస్ట్రేలియన్ ఓపెన్ 2026 పురుషుల సింగిల్స్ ఫైనల్‌లో నోవాక్ జకోవిచ్‌ను ఓడించి స్పెయిన్ ఆటగాడు కార్లోస్ అల్కరాజ్ విజేతగా నిలిచాడు.)",
        },
        195: {
            "question_en": "Which team won the “Ranji Trophy 2026” Title?",
            "question_te": "ఏ జట్టు \"రంజీ ట్రోఫీ 2026\" టైటిల్‌ను గెలుచుకుంది?",
            "options_te": ["ముంబై", "జమ్మూ & కాశ్మీర్", "మహారాష్ట్ర", "విదర్భ"],
            "explanation_te": "సరైన సమాధానం: జమ్మూ & కాశ్మీర్. (రంజీ ట్రోఫీ 2026 ఫైనల్‌లో కర్ణాటకను ఓడించి జమ్మూ & కాశ్మీర్ జట్టు తమ తొలి టైటిల్‌ను కైవసం చేసుకుంది.)",
        },
        196: {
            "question_te": "2026 వింటర్ ఒలింపిక్స్ క్రీడలను ఏ దేశం నిర్వహించింది?",
            "options_te": ["జపాన్", "ఫ్రాన్స్", "కెనడా", "ఇటలీ"],
            "explanation_te": "సరైన సమాధానం: ఇటలీ. (2026 వింటర్ ఒలింపిక్స్ క్రీడలు ఇటలీలోని మిలన్ మరియు కోర్టినా నగరాల్లో జరిగాయి.)",
        },
        197: {
            "question_en": "Which Team Won The Title Of 79th ‘2025–26 Santosh Trophy’?",
            "question_te": "79వ '2025–26 సంతోష్ ట్రోఫీ' టైటిల్‌ను ఏ జట్టు గెలుచుకుంది?",
            "options_te": ["మేఘాలయ", "ఉత్తరాఖండ్", "సర్వీసెస్", "పశ్చిమ బెంగాల్"],
            "explanation_te": "సరైన సమాధానం: సర్వీసెస్. (అస్సాంలో జరిగిన 79వ సంతోష్ ట్రోఫీ ఫుట్‌బాల్ ఫైనల్‌లో కేరళను ఓడించి సర్వీసెస్ జట్టు 8వ సారి విజేతగా నిలిచింది.)",
        },
        198: {
            "question_te": "2026 మహిళల ప్రీమియర్ లీగ్ (WPL) టైటిల్‌ను ఏ జట్టు గెలుచుకుంది?",
            "options_te": ["ఆర్‌సీబీ (RCB)", "ఢిల్లీ క్యాపిటల్స్", "ముంబై ఇండియన్స్", "రాజస్థాన్ రాయల్స్"],
            "explanation_te": "సరైన సమాధానం: ఆర్‌సీబీ (RCB). (2026 WPL ఫైనల్‌లో ఢిల్లీ క్యాపిటల్స్‌ను ఓడించి రాయల్ ఛాలెంజర్స్ బెంగళూరు ఛాంపియన్‌గా నిలిచింది.)",
        },
        199: {
            "question_te": "2025–26 విజయ్ హజారే ట్రోఫీని ఏ జట్టు గెలుచుకుంది?",
            "options_te": ["మహారాష్ట్ర", "కర్ణాటక", "ఢిల్లీ", "విదర్భ"],
            "explanation_te": "సరైన సమాధానం: విదర్భ. (33వ విజయ్ హజారే ట్రోఫీ ఫైనల్‌లో సౌరాష్ట్రను ఓడించి విదర్భ జట్టు టైటిల్ గెలుచుకుంది.)",
        },
    },
    "public/data/mock_test_full_200_13.json": {
        6: {
            "explanation_en": MASTER_BANK_PATCHES[25]["explanation_en"],
        },
        85: {
            "question_en": MASTER_BANK_PATCHES[288]["question_en"],
            "question_te": MASTER_BANK_PATCHES[288]["question_te"],
            "explanation_en": MASTER_BANK_PATCHES[288]["explanation_en"],
        },
    },
}


def main():
    # 1. Patch Master Bank
    mb_path = "public/data/master_aptitude_reasoning_bank.json"
    mb_data = load_json(mb_path)
    mb_updated = patch_qs_by_key(mb_data["questions"], MASTER_BANK_PATCHES, id_field="id")
    save_json(mb_path, mb_data)
    print(f"[MASTER BANK] Patched {mb_updated} items in {mb_path}")

    # 2. Patch & Rebalance Mocks 1-11 & 13 (Mock 12 already clean & balanced)
    ref_patches = {}
    for fp in sorted(glob.glob("public/data/mock_test_full_200*.json")):
        if "_12.json" in fp:
            print(f"[SKIP PATCH] {fp} (already verified PASS)")
            continue
        data = load_json(fp)
        qs = data["questions"]
        patched = 0
        if fp in MOCK_PATCHES:
            patched = patch_qs_by_key(qs, MOCK_PATCHES[fp], id_field="qNumber")
            for qn, p in MOCK_PATCHES[fp].items():
                if qn >= 101 and "question_en" in qs[qn - 1]:
                    ref_patches[qs[qn - 1]["question_en"].strip().lower()[:30]] = qs[qn - 1]
        rebalanced, dist = rebalance_mock(qs)
        save_json(fp, data)
        print(f"[MOCK] {fp}: patched={patched}, rebalanced={rebalanced}, final_dist={dict(sorted(dist.items()))}")

    # 3. Sync Mock 11 GS into mock11_gs.py & build_mock11_gs.py (before rebalance or after -> save post-rebalance exact GS)
    m11 = load_json("public/data/mock_test_full_200_11.json")
    gs11 = [q for q in m11["questions"] if q.get("section") == "General Studies" or 101 <= q.get("qNumber", 0) <= 200]
    for script_p in ("scripts/mock11_gs.py", "scripts/build_mock11_gs.py"):
        if os.path.exists(script_p):
            with open(script_p, "w", encoding="utf-8") as f:
                f.write("mock11_gs = " + json.dumps(gs11, ensure_ascii=False, indent=4) + "\n")
            print(f"[SCRIPT SYNC] Updated {script_p}")

    # 4. Sync StudyNow CA fixes into reference_studynow_ca_2026.json
    ref_path = "public/data/reference_studynow_ca_2026.json"
    if os.path.exists(ref_path):
        ref_data = load_json(ref_path)
        ref_upd = 0
        # Collect clean StudyNow items from Mocks 6, 7, 9, 11 (prefer unswapped canonical or copy Q/Opts/TE cleanly)
        src_qs = []
        for fp, qns in [
            ("public/data/mock_test_full_200_6.json", [117, 119, 121, 122, 123, 124, 126, 130]),
            ("public/data/mock_test_full_200_7.json", [125, 127, 128, 129, 159]),
            ("public/data/mock_test_full_200_9.json", [125, 126, 127, 128, 129, 130]),
            ("public/data/mock_test_full_200_11.json", list(range(189, 201))),
        ]:
            mqs = {q.get("qNumber", q.get("id")): q for q in load_json(fp)["questions"]}
            for qn in qns:
                src_qs.append(mqs[qn])
        for r in ref_data:
            rk = re.sub(r"[^a-z0-9]", "", r.get("question_en", "").lower())[:25]
            for sq in src_qs:
                sk = re.sub(r"[^a-z0-9]", "", sq.get("question_en", "").lower())[:25]
                if rk == sk and len(rk) >= 18:
                    for k in ("question_en", "question_te", "options_en", "options_te", "correct_option", "explanation_en", "explanation_te"):
                        r[k] = sq[k]
                    ref_upd += 1
                    break
        save_json(ref_path, ref_data)
        print(f"[REF SYNC] Updated {ref_upd} items in {ref_path}")


if __name__ == "__main__":
    main()
