import json
from pathlib import Path

# 44 verified unused Hard Reasoning items from master_aptitude_reasoning_bank.json
SELECTED_REAS_IDS = [
    178, 183, 188, 189, 190,
    192, 194, 195, 196, 197, 203,
    206, 209, 211, 212, 220,
    222, 224, 226, 229, 230,
    236, 237, 238, 242, 245, 249, 252, 253,
    258, 259, 260, 261, 266, 269,
    276, 280,
    283, 286, 289, 292,
    297, 299, 347,
]

CUSTOM_HARD_REASONING = [
    {
        "topic": "Data Sufficiency - Marks & Order Ranking",
        "question_en": "Five police recruits P, Q, R, S, and T scored distinct marks in a mock drill. Who scored the second highest marks?\nStatements:\nI. Q scored more than both S and T, but less than P.\nII. R did not score the highest, and S scored more than T.\nChoose the correct sufficiency option:",
        "question_te": "ఒక మాక్ డ్రిల్‌లో ఐదుగురు పోలీస్ అభ్యర్థులు P, Q, R, S మరియు T లు వేర్వేరు మార్కులు సాధించారు. వీరిలో రెండవ అత్యధిక మార్కులు సాధించినది ఎవరు?\nప్రకటనలు:\nI. Q, S మరియు T ఇద్దరి కంటే ఎక్కువ మార్కులు సాధించాడు, కానీ P కంటే తక్కువ సాధించాడు.\nII. R అత్యధిక మార్కులు సాధించలేదు, మరియు S, T కంటే ఎక్కువ మార్కులు సాధించాడు.\nసరైన సమాచార ఆప్షన్‌ను ఎంచుకోండి:",
        "options_en": [
            "Statement I alone is sufficient, while II alone is not",
            "Statement II alone is sufficient, while I alone is not",
            "Both Statements I and II together are necessary to answer",
            "Neither Statement I nor II, even together, is sufficient to answer"
        ],
        "options_te": [
            "ప్రకటన I మాత్రమే సరిపోతుంది, కానీ II సరిపోదు",
            "ప్రకటన II మాత్రమే సరిపోతుంది, కానీ I సరిపోదు",
            "సమాధానం కోసం ప్రకటనలు I మరియు II రెండూ కలిపి అవసరం",
            "ప్రకటనలు I మరియు II రెండూ కలిపి కూడా సమాధానం చెప్పడానికి సరిపోవు"
        ],
        "correct_option": 3,
        "explanation_en": "From I: P > Q > {S, T}, leaving R's position unknown. Adding II: R is not the highest, so P must be highest (P > R or Q > R). However, both orders P > R > Q > S > T (second highest: R) and P > Q > R > S > T (second highest: Q) satisfy all clues. Thus, both statements together are still insufficient.",
        "explanation_te": "ప్రకటన I నుండి P > Q > {S, T} అని తెలుస్తుంది. II జతచేస్తే P గరిష్టం అవుతాడు, కానీ R రెండవ స్థానంలో (P > R > Q > S > T) లేదా మూడవ స్థానంలో (P > Q > R > S > T) ఉండవచ్చు. కనుక రెండవ అత్యధిక స్కోరు ఎవరిదో నిర్ధారించలేము."
    },
    {
        "topic": "Cubes & Dice - Painted Surfaces Analysis",
        "question_en": "A solid wooden cube is painted Red on two adjacent faces, Blue on the two faces opposite to those Red faces, and Green on the remaining two opposite faces. It is then cut into 125 identical smaller cubes. How many smaller cubes have paint of at least two different colours, including at least one Red face?",
        "question_te": "ఒక ఘనపు చెక్క బ్లాక్ యొక్క రెండు ప్రక్కనే ఉన్న ముఖాలకు ఎరుపు రంగు, ఆ ఎరుపు ముఖాలకు ఎదురుగా ఉన్న రెండు ముఖాలకు నీలం రంగు, మరియు మిగిలిన రెండు ఎదురెదురు ముఖాలకు ఆకుపచ్చ రంగు వేసి, దానిని 125 సమానమైన చిన్న ఘనాలుగా కత్తిరించారు. కనీసం ఒక ఎరుపు ముఖంతో సహా కనీసం రెండు వేర్వేరు రంగులు కలిగిన చిన్న ఘనాలు ఎన్ని ఉంటాయి?",
        "options_en": ["24", "27", "26", "30"],
        "options_te": ["24", "27", "26", "30"],
        "correct_option": 0,
        "explanation_en": "Here n = 5 (each edge has 3 non-corner middle cubes). Orient Red on Front (+x) and Right (+y), Blue on Back (-x) and Left (-y), and Green on Top/Bottom (+-z). Corners (8 total): only the 2 (-x,-y,+-z) corners lack Red, so 6 corners have Red and Green (and Blue on 4 of them), all having >=2 distinct colours. Edges (12 total, 3 inner cubes each): the common edge (+x,+y) between the two Red faces has ONLY Red colour (excluded); the 6 edges (+x,-y), (-x,+y), (+x,+-z), and (+y,+-z) each pair Red with Blue or Green, contributing 6 * 3 = 18 cubes. Total = 6 + 18 = 24 smaller cubes.",
        "explanation_te": "125 చిన్న ఘనాలు అనగా n = 5 (ప్రతి అంచుపై 3 మధ్య ఘనాలు). ఎరుపు రెండు పక్కపక్క ముఖాల ఉమ్మడి అంచుపై ఉన్న 3 చిన్న ఘనాలకు కేవలం ఎరుపు రంగు మాత్రమే ఉంటుంది కనుక వాటిని మినహాయించాలి. ఎరుపు + ఇతర రంగు ఉన్న 6 మూల ఘనాలు + 6 ఇతర ఎరుపు అంచులపై 6 * 3 = 18 ఘనాలు. మొత్తం = 6 + 18 = 24."
    },
    {
        "topic": "Number Series - Wrong Number Pattern",
        "question_en": "Find the wrong number in the following number series:\n3, 4, 12, 45, 194, 1005",
        "question_te": "క్రింది సంఖ్యా శ్రేణిలో తప్పుగా ఉన్న సంఖ్యను గుర్తించండి:\n3, 4, 12, 45, 194, 1005",
        "options_en": ["12", "45", "194", "1005"],
        "options_te": ["12", "45", "194", "1005"],
        "correct_option": 2,
        "explanation_en": "The series follows the rule: Next term = (Previous term * k) + k^2 for k = 1, 2, 3, 4, 5: 3*1 + 1^2 = 4; 4*2 + 2^2 = 12; 12*3 + 3^2 = 45; 45*4 + 4^2 = 180 + 16 = 196 (not 194); 196*5 + 5^2 = 980 + 25 = 1005. Hence, 194 is the wrong number.",
        "explanation_te": "శ్రేణి నియమం (* k + k^2): 3*1 + 1 = 4; 4*2 + 4 = 12; 12*3 + 9 = 45; 45*4 + 16 = 196 (194 కాదు); 196*5 + 25 = 1005. కాబట్టి 194 తప్పు సంఖ్య."
    },
    {
        "topic": "Coding-Decoding - Mixed Vowel Forward & Consonant Reverse Sum",
        "question_en": "In a certain numerical cipher, 'LAW' is coded as '20' and 'CASE' is coded as '38'. How will 'JUSTICE' be coded in that same cipher?",
        "question_te": "ఒక నిర్దిష్ట సంఖ్యా కోడ్ భాషలో 'LAW' ను '20' గా మరియు 'CASE' ను '38' గా కోడ్ చేస్తే, అదే కోడ్ భాషలో 'JUSTICE' ను ఎలా కోడ్ చేస్తారు?",
        "options_en": ["89", "91", "95", "85"],
        "options_te": ["89", "91", "95", "85"],
        "correct_option": 1,
        "explanation_en": "Rule: Vowels take their forward alphabetical positions (A=1, E=5, I=9, O=15, U=21) while consonants take reverse alphabetical positions (27 - pos). For LAW: L(15)+A(1)+W(4) = 20. For CASE: C(24)+A(1)+S(8)+E(5) = 38. Applying to JUSTICE: J(27-10=17) + U(21) + S(27-19=8) + T(27-20=7) + I(9) + C(27-3=24) + E(5) = 17 + 21 + 8 + 7 + 9 + 24 + 5 = 91.",
        "explanation_te": "నియమం: అచ్చులకు సహజ స్థాన విలువ (A=1, E=5, I=9, O=15, U=21) మరియు హల్లులకు వ్యతిరేక స్థాన విలువ (27 - స్థానం) కూడాలి. JUSTICE = J(17)+U(21)+S(8)+T(7)+I(9)+C(24)+E(5) = 91."
    },
    {
        "topic": "Direction Sense - Morning Shadow & Shortest Distance",
        "question_en": "One morning at 7:00 AM after sunrise, Inspector Vikram and Inspector Arjun stood facing each other in an open ground. Vikram observed that Arjun's shadow fell directly to Arjun's left. From that spot, Vikram walked 12 km in the direction Arjun was initially facing, then turned right and walked 5 km to reach an outpost. What is the shortest distance and direction of the outpost from the starting point?",
        "question_te": "ఒకరోజు ఉదయం 7:00 గంటలకు సూర్యోదయం తర్వాత ఇన్‌స్పెక్టర్ విక్రమ్ మరియు ఇన్‌స్పెక్టర్ అర్జున్ మైదానంలో ఒకరికొకరు ఎదురెదురుగా నిలబడి ఉన్నారు. అర్జున్ నీడ సరిగ్గా అర్జున్ ఎడమవైపున పడుతుండటాన్ని విక్రమ్ గమనించాడు. ఆ స్థానం నుండి విక్రమ్, అర్జున్ మొదట్లో చూస్తున్న దిశలో 12 కి.మీ నడిచి, ఆపై కుడివైపు తిరిగి 5 కి.మీ నడిచి అవుట్‌పోస్ట్ చేరుకున్నాడు. ప్రారంభ స్థానం నుండి అవుట్‌పోస్ట్ ఎంత కనిష్ట దూరంలో మరియు ఏ దిశలో ఉంది?",
        "options_en": ["13 km North-West", "13 km North-East", "17 km North-East", "13 km South-East"],
        "options_te": ["13 కి.మీ వాయువ్యం", "13 కి.మీ ఈశాన్యం", "17 కి.మీ ఈశాన్యం", "13 కి.మీ ఆగ్నేయం"],
        "correct_option": 1,
        "explanation_en": "At 7:00 AM, the Sun is in the East, so all shadows fall towards the West. Since Arjun's shadow falls to his left, West must be on Arjun's left, meaning Arjun faces North initially. Vikram walks 12 km North, turns right (East), and walks 5 km East. Shortest distance = sqrt(12^2 + 5^2) = 13 km in the North-East direction.",
        "explanation_te": "ఉదయం నీడ పడమర దిశలో పడుతుంది. పడమర అర్జున్ ఎడమవైపు కావున అర్జున్ ఉత్తరం వైపు చూస్తున్నాడు. విక్రమ్ ఉత్తరంగా 12 కి.మీ మరియు తూర్పుగా 5 కి.మీ నడవగా, ప్రారంభ స్థానం నుండి కనిష్ట దూరం sqrt(12^2 + 5^2) = 13 కి.మీ మరియు దిశ ఈశాన్యం."
    },
    {
        "topic": "Venn Diagrams - 3-Set Analytical Evaluation",
        "question_en": "In a departmental evaluation of 120 SI candidates: 65 passed Firing Drill, 55 passed Obstacle Run, and 50 passed Legal Aptitude. Further, 25 passed both Firing Drill and Obstacle Run, 20 passed both Obstacle Run and Legal Aptitude, and 18 passed both Firing Drill and Legal Aptitude. If 5 candidates failed in all three tests, how many candidates passed ONLY the Firing Drill?",
        "question_te": "120 మంది ఎస్సై అభ్యర్థుల పరీక్షలో 65 మంది ఫైరింగ్ డ్రిల్‌లో, 55 మంది ఆబ్‌స్టాకిల్ రన్‌లో మరియు 50 మంది లీగల్ ఆప్టిట్యూడ్‌లో ఉత్తీర్ణులయ్యారు. అలాగే 25 మంది ఫైరింగ్ డ్రిల్ & ఆబ్‌స్టాకిల్ రన్ రెండింటిలోనూ, 20 మంది ఆబ్‌స్టాకిల్ రన్ & లీగల్ ఆప్టిట్యూడ్ రెండింటిలోనూ, మరియు 18 మంది ఫైరింగ్ డ్రిల్ & లీగల్ ఆప్టిట్యూడ్ రెండింటిలోనూ ఉత్తీర్ణులయ్యారు. 5 గురు అభ్యర్థులు మూడు పరీక్షల్లోనూ విఫలమైతే, కేవలం ఫైరింగ్ డ్రిల్‌లో మాత్రమే ఉత్తీర్ణులైన అభ్యర్థులు ఎంతమంది?",
        "options_en": ["22", "30", "35", "38"],
        "options_te": ["22", "30", "35", "38"],
        "correct_option": 1,
        "explanation_en": "Candidates passing at least one test = 120 - 5 = 115. Let x be candidates who passed all three tests. By Inclusion-Exclusion: 115 = 65 + 55 + 50 - 25 - 20 - 18 + x => 115 = 107 + x => x = 8. Candidates passing only Firing + Obstacle = 25 - 8 = 17; only Firing + Legal = 18 - 8 = 10. Hence, candidates passing ONLY Firing Drill = 65 - (17 + 10 + 8) = 30.",
        "explanation_te": "కనీసం ఒక పరీక్షలో పాస్ అయినవారు = 120 - 5 = 115. మూడింటిలో పాస్ అయినవారు x = 115 - (65+55+50 - 25-20-18) = 115 - 107 = 8. కేవలం ఫైరింగ్ డ్రిల్‌లో మాత్రమే పాస్ అయినవారు = 65 - (25 - 8) - (18 - 8) - 8 = 65 - 35 = 30."
    },
]


def get_reasoning_questions():
    bank_path = Path(__file__).resolve().parent.parent / "public" / "data" / "master_aptitude_reasoning_bank.json"
    with open(bank_path, "r", encoding="utf-8") as f:
        mb = json.load(f)["questions"]
    by_id = {q["id"]: q for q in mb}

    assert len(SELECTED_REAS_IDS) == 44, f"Expected 44 MB reasoning Qs, got {len(SELECTED_REAS_IDS)}"
    questions = []
    qnum = 51

    for bid in SELECTED_REAS_IDS:
        src = by_id[bid]
        questions.append({
            "id": qnum,
            "qNumber": qnum,
            "section": "Mental Ability & Logical Reasoning",
            "topic": src["topic"],
            "difficulty": "Hard",
            "question_en": src["question_en"],
            "question_te": src["question_te"],
            "options_en": list(src["options_en"]),
            "options_te": list(src["options_te"]),
            "correct_option": int(src["correct_option"]),
            "explanation_en": src["explanation_en"],
            "explanation_te": src["explanation_te"],
        })
        qnum += 1

    for c in CUSTOM_HARD_REASONING:
        questions.append({
            "id": qnum,
            "qNumber": qnum,
            "section": "Mental Ability & Logical Reasoning",
            "topic": c["topic"],
            "difficulty": "Hard",
            "question_en": c["question_en"],
            "question_te": c["question_te"],
            "options_en": list(c["options_en"]),
            "options_te": list(c["options_te"]),
            "correct_option": int(c["correct_option"]),
            "explanation_en": c["explanation_en"],
            "explanation_te": c["explanation_te"],
        })
        qnum += 1

    assert len(questions) == 50
    return questions
