# -*- coding: utf-8 -*-
"""
Mock Test 12 - Mental Ability & Reasoning (Q51 to Q100)
Easy / Foundational Tier
"""

def get_reasoning_50():
    return [
    {
        "id": 51,
        "qNumber": 51,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Clocks",
        "question_en": "What is the angle between the hour hand and the minute hand of a clock at exactly 3:00?",
        "question_te": "ఒక గడియారంలో సమయం సరిగ్గా 3:00 గంటలైనప్పుడు గంటల ముల్లు మరియు నిమిషాల ముల్లుల మధ్య కోణం ఎంత?",
        "options_en": [
            "60°",
            "75°",
            "90°",
            "120°"
        ],
        "options_te": [
            "60°",
            "75°",
            "90°",
            "120°"
        ],
        "correct_option": 2,
        "explanation_en": "At 3:00, the minute hand points to 12 and the hour hand points to 3. The angle between them is 3 * 30° = 90°.",
        "explanation_te": "సమయం 3:00 వద్ద ముల్లుల మధ్య కోణం = 3 * 30° = 90° (లంబకోణం)."
    },
    {
        "id": 52,
        "qNumber": 52,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Clocks",
        "question_en": "What is the angle between the two hands of a clock at 6:00?",
        "question_te": "గడియారంలో సమయం 6:00 అయినప్పుడు ముల్లుల మధ్య కోణం ఎంత?",
        "options_en": [
            "90°",
            "120°",
            "180°",
            "360°"
        ],
        "options_te": [
            "90°",
            "120°",
            "180°",
            "360°"
        ],
        "correct_option": 2,
        "explanation_en": "At 6:00, the minute hand points to 12 and the hour hand points directly opposite to 6, forming a straight line of 180°.",
        "explanation_te": "6:00 గంటలకు ముల్లులు ఒకదానికొకటి సరళరేఖలో వ్యతిరేకంగా ఉంటాయి. కోణం = 180°."
    },
    {
        "id": 53,
        "qNumber": 53,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Calendar",
        "question_en": "If the 1st of January of a non-leap ordinary year is a Monday, what day of the week will be the 31st of December of the same year?",
        "question_te": "ఒక సాధారణ (లీప్ కాని) సంవత్సరంలో జనవరి 1వ తేదీ సోమవారం అయితే, అదే సంవత్సరంలో డిసెంబర్ 31వ తేదీ ఏ వారం అవుతుంది?",
        "options_en": [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday"
        ],
        "options_te": [
            "ఆదివారం",
            "సోమవారం",
            "మంగళవారం",
            "బుధవారం"
        ],
        "correct_option": 1,
        "explanation_en": "An ordinary year has 365 days = 52 weeks + 1 day. Therefore, an ordinary year always begins and ends on the exact same day of the week: Monday.",
        "explanation_te": "సాధారణ సంవత్సరంలో 365 రోజులు ఉంటాయి (52 వారాలు + 1 రోజు). కాబట్టి సాధారణ సంవత్సరం ఏ వారంతో ప్రారంభమవుతుందో అదే వారంతో ముగుస్తుంది (సోమవారం)."
    },
    {
        "id": 54,
        "qNumber": 54,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Calendar",
        "question_en": "Which of the following years is a leap year?",
        "question_te": "క్రింది సంవత్సరాలలో లీప్ సంవత్సరం ఏది?",
        "options_en": [
            "2018",
            "2021",
            "2024",
            "2026"
        ],
        "options_te": [
            "2018",
            "2021",
            "2024",
            "2026"
        ],
        "correct_option": 2,
        "explanation_en": "A non-century year is a leap year if it is divisible by 4. 2024 / 4 = 506 (remainder 0). Hence, 2024 is a leap year.",
        "explanation_te": "శతాబ్దాలు కాని సంవత్సరాలలో 4 చే నిశ్శేషంగా భాగించబడేది లీప్ సంవత్సరం. 2024 నాల్గుతో భాగించబడుతుంది కాబట్టి ఇది లీప్ సంవత్సరం."
    },
    {
        "id": 55,
        "qNumber": 55,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Number Series",
        "question_en": "Find the next number in the series: 4, 9, 14, 19, 24, ?",
        "question_te": "క్రింది సంఖ్యా శ్రేణిలో తదుపరి సంఖ్యను గుర్తించండి: 4, 9, 14, 19, 24, ?",
        "options_en": [
            "27",
            "28",
            "29",
            "30"
        ],
        "options_te": [
            "27",
            "28",
            "29",
            "30"
        ],
        "correct_option": 2,
        "explanation_en": "The series adds 5 at each step: 4 + 5 = 9, 9 + 5 = 14, 14 + 5 = 19, 19 + 5 = 24, 24 + 5 = 29.",
        "explanation_te": "ప్రతి సంఖ్యకు +5 కలపబడింది: 24 + 5 = 29."
    },
    {
        "id": 56,
        "qNumber": 56,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Number Series",
        "question_en": "What will be the next number in the sequence: 3, 6, 12, 24, 48, ?",
        "question_te": "క్రింది శ్రేణిలో తరువాతి సంఖ్య ఏది: 3, 6, 12, 24, 48, ?",
        "options_en": [
            "72",
            "84",
            "96",
            "108"
        ],
        "options_te": [
            "72",
            "84",
            "96",
            "108"
        ],
        "correct_option": 2,
        "explanation_en": "Each term is multiplied by 2: 3*2 = 6, 6*2 = 12, 12*2 = 24, 24*2 = 48, 48*2 = 96.",
        "explanation_te": "ప్రతి పదం 2 చే గుణించబడింది: 48 * 2 = 96."
    },
    {
        "id": 57,
        "qNumber": 57,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Number Series",
        "question_en": "Identify the missing number in the series: 1, 4, 9, 16, 25, 36, ?",
        "question_te": "క్రింది శ్రేణిలో లోపించిన సంఖ్యను కనుగొనండి: 1, 4, 9, 16, 25, 36, ?",
        "options_en": [
            "45",
            "48",
            "49",
            "54"
        ],
        "options_te": [
            "45",
            "48",
            "49",
            "54"
        ],
        "correct_option": 2,
        "explanation_en": "The series consists of consecutive squares: 1^2, 2^2, 3^2, 4^2, 5^2, 6^2, 7^2 = 49.",
        "explanation_te": "వరుస సంఖ్యల వర్గాలు: 1^2, 2^2, 3^2, 4^2, 5^2, 6^2, 7^2 = 49."
    },
    {
        "id": 58,
        "qNumber": 58,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Number Series",
        "question_en": "What is the next number in the pattern: 1, 8, 27, 64, ?",
        "question_te": "క్రింది అమరికలో తదుపరి సంఖ్య ఏది: 1, 8, 27, 64, ?",
        "options_en": [
            "100",
            "121",
            "125",
            "144"
        ],
        "options_te": [
            "100",
            "121",
            "125",
            "144"
        ],
        "correct_option": 2,
        "explanation_en": "The terms are consecutive cubes: 1^3 = 1, 2^3 = 8, 3^3 = 27, 4^3 = 64, 5^3 = 125.",
        "explanation_te": "వరుస ఘనాలు: 1^3, 2^3, 3^3, 4^3, 5^3 = 125."
    },
    {
        "id": 59,
        "qNumber": 59,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Letter Series",
        "question_en": "Find the next letter in the series: A, C, E, G, I, ?",
        "question_te": "క్రింది అక్షర శ్రేణిలో తదుపరి అక్షరం ఏది: A, C, E, G, I, ?",
        "options_en": [
            "J",
            "K",
            "L",
            "M"
        ],
        "options_te": [
            "J",
            "K",
            "L",
            "M"
        ],
        "correct_option": 1,
        "explanation_en": "Each letter advances by +2: A(1) -> C(3) -> E(5) -> G(7) -> I(9) -> K(11).",
        "explanation_te": "ప్రతి అక్షరం +2 స్థానాలు ముందుకు వెళ్తుంది: I(9) + 2 = K(11)."
    },
    {
        "id": 60,
        "qNumber": 60,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Letter Series",
        "question_en": "What comes next in the reverse letter sequence: Z, X, V, T, R, ?",
        "question_te": "వ్యతిరేక క్రమంలో ఉన్న క్రింది శ్రేణిలో తదుపరి అక్షరం ఏది: Z, X, V, T, R, ?",
        "options_en": [
            "P",
            "Q",
            "O",
            "N"
        ],
        "options_te": [
            "P",
            "Q",
            "O",
            "N"
        ],
        "correct_option": 0,
        "explanation_en": "Each letter moves backwards by -2: Z(26) -> X(24) -> V(22) -> T(20) -> R(18) -> P(16).",
        "explanation_te": "ప్రతి అక్షరం -2 స్థానాలు వెనుకకు తగ్గుతుంది: R(18) - 2 = P(16)."
    },
    {
        "id": 61,
        "qNumber": 61,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Coding-Decoding",
        "question_en": "If in a code language, 'BOOK' is written as 'CPPL', how will 'NOTE' be written in that code?",
        "question_te": "ఒక కోడ్ భాషలో 'BOOK' ను 'CPPL' గా రాస్తే, అదే కోడ్‌లో 'NOTE' ను ఎలా రాస్తారు?",
        "options_en": [
            "OPUF",
            "OQUF",
            "OPSF",
            "NPUF"
        ],
        "options_te": [
            "OPUF",
            "OQUF",
            "OPSF",
            "NPUF"
        ],
        "correct_option": 0,
        "explanation_en": "Each letter is shifted forward by +1: N+1=O, O+1=P, T+1=U, E+1=F -> OPUF.",
        "explanation_te": "ప్రతి అక్షరానికి +1 కలపబడింది: N+1=O, O+1=P, T+1=U, E+1=F -> OPUF."
    },
    {
        "id": 62,
        "qNumber": 62,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Coding-Decoding",
        "question_en": "If 'BAT' is coded as 2-1-20, how will 'CAT' be coded?",
        "question_te": "'BAT' ను 2-1-20 గా కోడ్ చేస్తే, 'CAT' ను ఎలా కోడ్ చేస్తారు?",
        "options_en": [
            "3-1-20",
            "3-2-20",
            "2-1-20",
            "3-1-19"
        ],
        "options_te": [
            "3-1-20",
            "3-2-20",
            "2-1-20",
            "3-1-19"
        ],
        "correct_option": 0,
        "explanation_en": "Letters correspond to their alphabetical position: C = 3, A = 1, T = 20 -> 3-1-20.",
        "explanation_te": "అక్షరాల స్థాన సంఖ్యలు: C = 3, A = 1, T = 20 -> 3-1-20."
    },
    {
        "id": 63,
        "qNumber": 63,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Coding-Decoding",
        "question_en": "In a code language, if 'MADRAS' is coded as 'SARDAM', how is 'MUMBAI' written?",
        "question_te": "ఒక కోడ్ భాషలో 'MADRAS' ను 'SARDAM' గా రాస్తే, 'MUMBAI' ని ఎలా రాస్తారు?",
        "options_en": [
            "IABMUM",
            "IBAMUM",
            "IABMMU",
            "IABUMN"
        ],
        "options_te": [
            "IABMUM",
            "IBAMUM",
            "IABMMU",
            "IABUMN"
        ],
        "correct_option": 0,
        "explanation_en": "The letters of the word are reversed: M-U-M-B-A-I reversed becomes I-A-B-M-U-M.",
        "explanation_te": "పదంలోని అక్షరాల క్రమం పూర్తిగా తిరగరాయబడింది: I-A-B-M-U-M."
    },
    {
        "id": 64,
        "qNumber": 64,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Direction & Distance Sense",
        "question_en": "A police sub-inspector walks 3 km East from his station, turns right and walks 4 km South. How far is he from the police station in a straight line?",
        "question_te": "ఒక పోలీస్ సబ్-ఇన్‌స్పెక్టర్ పోలీస్ స్టేషన్ నుండి తూర్పు వైపు 3 కి.మీ నడిచి, కుడివైపుకు తిరిగి దక్షిణం వైపు 4 కి.మీ నడిచాడు. అతను బయలుదేరిన పోలీస్ స్టేషన్ నుండి సరళరేఖలో ఎంత దూరంలో ఉన్నాడు?",
        "options_en": [
            "5 km",
            "6 km",
            "7 km",
            "8 km"
        ],
        "options_te": [
            "5 కి.మీ",
            "6 కి.మీ",
            "7 కి.మీ",
            "8 కి.మీ"
        ],
        "correct_option": 0,
        "explanation_en": "Using Pythagoras theorem: Distance = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5 km.",
        "explanation_te": "పైథాగరస్ సిద్ధాంతం: దూరం = sqrt(3^2 + 4^2) = sqrt(25) = 5 కి.మీ."
    },
    {
        "id": 65,
        "qNumber": 65,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Direction Sense",
        "question_en": "A person is facing North. He turns 90 degrees clockwise and then 180 degrees counter-clockwise. Which direction is he facing now?",
        "question_te": "ఒక వ్యక్తి ఉత్తరం వైపు ముఖం చేసి ఉన్నాడు. అతను సవ్యదిశలో 90 డిగ్రీలు తిరిగి, ఆపై అపసవ్యదిశలో 180 డిగ్రీలు తిరిగాడు. ఇప్పుడు అతను ఏ దిశ వైపు చూస్తున్నాడు?",
        "options_en": [
            "East",
            "West",
            "North",
            "South"
        ],
        "options_te": [
            "తూర్పు",
            "పశ్చిమం (పడమర)",
            "ఉత్తరం",
            "దక్షిణం"
        ],
        "correct_option": 1,
        "explanation_en": "Facing North: +90° clockwise = East. Then -180° counter-clockwise from East = West.",
        "explanation_te": "ఉత్తరం నుండి సవ్యదిశలో 90° = తూర్పు. తూర్పు నుండి అపసవ్యదిశలో 180° = పశ్చిమం (పడమర)."
    },
    {
        "id": 66,
        "qNumber": 66,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Blood Relations",
        "question_en": "Pointing to a photograph of a boy, Suresh said: 'He is the son of my father's only son.' How is Suresh related to that boy?",
        "question_te": "ఒక అబ్బాయి ఫోటోను చూపిస్తూ సురేష్ ఇలా అన్నాడు: 'ఇతను మా నాన్నగారి ఏకైక కుమారుని కుమారుడు.' ఆ అబ్బాయికి సురేష్ ఏమవుతాడు?",
        "options_en": [
            "Brother",
            "Uncle",
            "Father",
            "Grandfather"
        ],
        "options_te": [
            "సోదరుడు",
            "బాబాయి",
            "తండ్రి",
            "తాతగారు"
        ],
        "correct_option": 2,
        "explanation_en": "Father's only son = Suresh himself. The boy is the son of Suresh. Therefore, Suresh is his Father.",
        "explanation_te": "నాన్నగారి ఏకైక కుమారుడు = సురేష్ స్వయంగా. ఆ అబ్బాయి సురేష్ కుమారుడు. కాబట్టి సురేష్ ఆ అబ్బాయికి తండ్రి."
    },
    {
        "id": 67,
        "qNumber": 67,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Blood Relations",
        "question_en": "What is the relationship of your mother's brother to you?",
        "question_te": "మీ తల్లి యొక్క సోదరుడు మీకు ఏమవుతాడు?",
        "options_en": [
            "Paternal Uncle",
            "Maternal Uncle",
            "Father-in-law",
            "Cousin"
        ],
        "options_te": [
            "చిన్నాన్న/పెద్దనాన్న",
            "మేనమామ",
            "మామగారు",
            "బావ"
        ],
        "correct_option": 1,
        "explanation_en": "One's mother's brother is their maternal uncle.",
        "explanation_te": "తల్లి యొక్క సోదరుడిని మేనమామ (Maternal Uncle) అంటారు."
    },
    {
        "id": 68,
        "qNumber": 68,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Blood Relations",
        "question_en": "A is the brother of B. B is the sister of C. C is the father of D. How is A related to D?",
        "question_te": "A, B యొక్క సోదరుడు. B, C యొక్క సోదరి. C, D యొక్క తండ్రి. A, D కు ఏమవుతాడు?",
        "options_en": [
            "Father",
            "Uncle",
            "Brother",
            "Grandfather"
        ],
        "options_te": [
            "తండ్రి",
            "బాబాయి / పెద్దనాన్న",
            "సోదరుడు",
            "తాతగారు"
        ],
        "correct_option": 1,
        "explanation_en": "Since A, B, and C are siblings, and C is the father of D, A is the brother of D's father. Hence A is D's Uncle.",
        "explanation_te": "A, B, C లు తోబుట్టువులు. C, D తండ్రి కాబట్టి తండ్రి సోదరుడు A, D కి బాబాయి/పెద్దనాన్న (Uncle) అవుతాడు."
    },
    {
        "id": 69,
        "qNumber": 69,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Ranking & Order",
        "question_en": "In a row of 35 police trainees, Kishore is 12th from the left end. What is his position from the right end of the row?",
        "question_te": "35 మంది పోలీస్ ట్రైనీలు ఉన్న వరుసలో కిషోర్ ఎడమ చివర నుండి 12వ స్థానంలో ఉన్నాడు. కుడి చివర నుండి అతని స్థానం ఎంత?",
        "options_en": [
            "23rd",
            "24th",
            "25th",
            "26th"
        ],
        "options_te": [
            "23వ",
            "24వ",
            "25వ",
            "26వ"
        ],
        "correct_option": 1,
        "explanation_en": "Position from right = Total persons - Position from left + 1 = 35 - 12 + 1 = 23 + 1 = 24th.",
        "explanation_te": "కుడి నుండి స్థానం = మొత్తం వ్యక్తులు - ఎడమ నుండి స్థానం + 1 = 35 - 12 + 1 = 24వ స్థానం."
    },
    {
        "id": 70,
        "qNumber": 70,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Ranking & Order",
        "question_en": "In an examination merit list, Divya ranks 7th from the top and 28th from the bottom. How many total students passed the examination?",
        "question_te": "ఒక పరీక్ష మెరిట్ జాబితాలో దివ్య ర్యాంక్ పైనుండి 7వది మరియు కింద నుండి 28వది. ఆ పరీక్షలో ఉత్తీర్ణులైన మొత్తం విద్యార్థుల సంఖ్య ఎంత?",
        "options_en": [
            "34",
            "35",
            "36",
            "37"
        ],
        "options_te": [
            "34",
            "35",
            "36",
            "37"
        ],
        "correct_option": 0,
        "explanation_en": "Total students = Top rank + Bottom rank - 1 = 7 + 28 - 1 = 34.",
        "explanation_te": "మొత్తం విద్యార్థులు = 7 + 28 - 1 = 34."
    },
    {
        "id": 71,
        "qNumber": 71,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Word Analogy",
        "question_en": "India : New Delhi :: Telangana : ?",
        "question_te": "భారతదేశం : న్యూఢిల్లీ :: తెలంగాణ : ?",
        "options_en": [
            "Warangal",
            "Hyderabad",
            "Nizamabad",
            "Karimnagar"
        ],
        "options_te": [
            "వరంగల్",
            "హైదరాబాద్",
            "నిజామాబాద్",
            "కరీంనగర్"
        ],
        "correct_option": 1,
        "explanation_en": "New Delhi is the capital of India. Hyderabad is the capital of Telangana.",
        "explanation_te": "భారత రాజధాని న్యూఢిల్లీ. తెలంగాణ రాజధాని హైదరాబాద్."
    },
    {
        "id": 72,
        "qNumber": 72,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Word Analogy",
        "question_en": "Thermometer : Temperature :: Speedometer : ?",
        "question_te": "థర్మామీటర్ : ఉష్ణోగ్రత :: స్పీడోమీటర్ : ?",
        "options_en": [
            "Current",
            "Vehicle Speed",
            "Atmospheric Pressure",
            "Distance"
        ],
        "options_te": [
            "విద్యుత్ ప్రవాహం",
            "వాహన వేగం",
            "వాతావరణ పీడనం",
            "దూరం"
        ],
        "correct_option": 1,
        "explanation_en": "Thermometer measures temperature; Speedometer measures speed.",
        "explanation_te": "థర్మామీటర్ ఉష్ణోగ్రతను కొలుస్తుంది; స్పీడోమీటర్ వాహన వేగాన్ని కొలుస్తుంది."
    },
    {
        "id": 73,
        "qNumber": 73,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Word Analogy",
        "question_en": "Dog : Puppy :: Cat : ?",
        "question_te": "కుక్క : కుక్కపిల్ల (Puppy) :: పిల్లి : ?",
        "options_en": [
            "Kitten",
            "Calf",
            "Cub",
            "Lamb"
        ],
        "options_te": [
            "పిల్లిపిల్ల (Kitten)",
            "దూడ",
            "పిల్ల (Cub)",
            "గొర్రెపిల్ల"
        ],
        "correct_option": 0,
        "explanation_en": "A young dog is a puppy; a young cat is a kitten.",
        "explanation_te": "కుక్క పిల్లని Puppy అంటారు; పిల్లి పిల్లని Kitten అంటారు."
    },
    {
        "id": 74,
        "qNumber": 74,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Number Analogy",
        "question_en": "5 : 25 :: 8 : ?",
        "question_te": "5 : 25 :: 8 : ?",
        "options_en": [
            "40",
            "56",
            "64",
            "72"
        ],
        "options_te": [
            "40",
            "56",
            "64",
            "72"
        ],
        "correct_option": 2,
        "explanation_en": "5^2 = 25. Similarly, 8^2 = 64.",
        "explanation_te": "5^2 = 25. అదేవిధంగా 8^2 = 64."
    },
    {
        "id": 75,
        "qNumber": 75,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Classification",
        "question_en": "Find the odd one out among the following: Apple, Mango, Banana, Potato",
        "question_te": "క్రింది వాటిలో భిన్నమైన దానిని గుర్తించండి: ఆపిల్, మామిడి, అరటి, బంగాళాదుంప",
        "options_en": [
            "Apple",
            "Mango",
            "Banana",
            "Potato"
        ],
        "options_te": [
            "ఆపిల్",
            "మామిడి",
            "అరటి",
            "బంగాళాదుంప"
        ],
        "correct_option": 3,
        "explanation_en": "Apple, Mango, and Banana are fruits that grow on trees/plants above ground. Potato is an underground modified stem (tuber vegetable).",
        "explanation_te": "ఆపిల్, మామిడి, అరటి పండ్లు. బంగాళాదుంప భూమి లోపల పెరిగే దుంప కూరగాయ. కాబట్టి ఇది భిన్నమైనది."
    },
    {
        "id": 76,
        "qNumber": 76,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Classification",
        "question_en": "Identify the odd one out: Square, Rectangle, Triangle, Cube",
        "question_te": "క్రింది వాటిలో భిన్నమైన ఆకారాన్ని గుర్తించండి: చతురస్రం, దీర్ఘచతురస్రం, త్రిభుజం, ఘనం (Cube)",
        "options_en": [
            "Square",
            "Rectangle",
            "Triangle",
            "Cube"
        ],
        "options_te": [
            "చతురస్రం",
            "దీర్ఘచతురస్రం",
            "త్రిభుజం",
            "ఘనం (Cube)"
        ],
        "correct_option": 3,
        "explanation_en": "Square, Rectangle, and Triangle are two-dimensional (2D) plane figures, whereas Cube is a three-dimensional (3D) solid figure.",
        "explanation_te": "చతురస్రం, దీర్ఘచతురస్రం, త్రిభుజం 2D సమతల పటాలు. ఘనం (Cube) 3D ఘనరూప పటం."
    },
    {
        "id": 77,
        "qNumber": 77,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Classification",
        "question_en": "Find the odd one out among the numbers: 15, 25, 37, 45",
        "question_te": "క్రింది సంఖ్యలలో భిన్నమైన సంఖ్యను గుర్తించండి: 15, 25, 37, 45",
        "options_en": [
            "15",
            "25",
            "37",
            "45"
        ],
        "options_te": [
            "15",
            "25",
            "37",
            "45"
        ],
        "correct_option": 2,
        "explanation_en": "15, 25, and 45 are all composite numbers divisible by 5. 37 is a prime number.",
        "explanation_te": "15, 25, 45 అన్నీ 5 చే భాగించబడే సంయుక్త సంఖ్యలు. 37 ప్రధాన సంఖ్య. కాబట్టి 37 భిన్నమైనది."
    },
    {
        "id": 78,
        "qNumber": 78,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Syllogism",
        "question_en": "Statements:\n1. All cats are animals.\n2. All animals are mammals.\n\nConclusion:\nI. All cats are mammals.\nII. Some mammals are cats.\n\nWhich of the conclusions logically follows?",
        "question_te": "ప్రకటనలు:\n1. అన్ని పిల్లులు జంతువులు.\n2. అన్ని జంతువులు క్షీరదాలు.\n\nతీర్మానాలు:\nI. అన్ని పిల్లులు క్షీరదాలు.\nII. కొన్ని క్షీరదాలు పిల్లులు.\n\nఏ తీర్మానం తార్కికంగా అనుసరిస్తుంది?",
        "options_en": [
            "Only Conclusion I follows",
            "Only Conclusion II follows",
            "Both Conclusions I and II follow",
            "Neither Conclusion follows"
        ],
        "options_te": [
            "తీర్మానం I మాత్రమే అనుసరిస్తుంది",
            "తీర్మానం II మాత్రమే అనుసరిస్తుంది",
            "తీర్మానాలు I మరియు II రెండూ అనుసరిస్తాయి",
            "ఏ తీర్మానం అనుసరించదు"
        ],
        "correct_option": 2,
        "explanation_en": "Since all cats are animals and all animals are mammals, all cats are inside mammals (I is true). Since cats exist within mammals, some mammals are cats (II is true). Both follow.",
        "explanation_te": "పిల్లులన్నీ క్షీరదాల వర్గంలో ఉన్నాయి (I సరైనది). క్షీరదాలలో కొన్ని పిల్లులు అవుతాయి (II సరైనది). రెండూ అనుసరిస్తాయి."
    },
    {
        "id": 79,
        "qNumber": 79,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Syllogism",
        "question_en": "Statements:\n1. Some pens are pencils.\n2. All pencils are erasers.\n\nConclusion:\nI. Some pens are erasers.\nII. All erasers are pens.\n\nWhich of the conclusions logically follows?",
        "question_te": "ప్రకటనలు:\n1. కొన్ని పెన్నులు పెన్సిళ్లు.\n2. అన్ని పెన్సిళ్లు ఎరేజర్లు.\n\nతీర్మానాలు:\nI. కొన్ని పెన్నులు ఎరేజర్లు.\nII. అన్ని ఎరేజర్లు పెన్నులు.\n\nఏ తీర్మానం తార్కికంగా అనుసరిస్తుంది?",
        "options_en": [
            "Only Conclusion I follows",
            "Only Conclusion II follows",
            "Both follow",
            "Neither follows"
        ],
        "options_te": [
            "తీర్మానం I మాత్రమే అనుసరిస్తుంది",
            "తీర్మానం II మాత్రమే అనుసరిస్తుంది",
            "రెండూ అనుసరిస్తాయి",
            "ఏదీ అనుసరించదు"
        ],
        "correct_option": 0,
        "explanation_en": "The intersection of pens and pencils is enclosed inside erasers, so some pens must be erasers (Conclusion I follows). There is no information that all erasers are pens (II does not follow).",
        "explanation_te": "పెన్సిళ్లైన కొన్ని పెన్నులు ఎరేజర్ల పరిధిలో ఉంటాయి కాబట్టి తీర్మానం I మాత్రమే అనుసరిస్తుంది."
    },
    {
        "id": 80,
        "qNumber": 80,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Venn Diagrams",
        "question_en": "Which Venn diagram relationship correctly illustrates: 'Country', 'State', and 'District'?",
        "question_te": "'దేశం', 'రాష్ట్రం' మరియు 'జిల్లా' ల మధ్య గల సంబంధాన్ని సరైన వెన్ చిత్రం ఎలా సూచిస్తుంది?",
        "options_en": [
            "Three separate disjoint circles",
            "Three concentric circles inside one another",
            "Three mutually intersecting circles",
            "Two circles inside one with no intersection"
        ],
        "options_te": [
            "మూడు వేర్వేరు వృత్తాలు",
            "ఒకదాని లోపల ఒకటి ఉండే మూడు ఏకకేంద్ర వృత్తాలు",
            "పరస్పరం ఖండించుకునే మూడు వృత్తాలు",
            "ఒక పెద్ద వృత్తం లోపల రెండు వేర్వేరు వృత్తాలు"
        ],
        "correct_option": 1,
        "explanation_en": "A district lies entirely within a state, and a state lies entirely within a country. Hence, they are represented by three concentric circles.",
        "explanation_te": "దేశంలో రాష్ట్రం, రాష్ట్రంలో జిల్లా ఉంటాయి కాబట్టి ఒకదాని లోపల ఒకటి ఉండే మూడు ఏకకేంద్ర వృత్తాలు సరైనవి."
    },
    {
        "id": 81,
        "qNumber": 81,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Venn Diagrams",
        "question_en": "Which representation best portrays 'Animals', 'Dogs', and 'Cats'?",
        "question_te": "'జంతువులు', 'కుక్కలు', మరియు 'పిల్లులు' ల మధ్య సంబంధాన్ని ఏది ఉత్తమంగా సూచిస్తుంది?",
        "options_en": [
            "Two separate circles (Dogs and Cats) inside a large circle (Animals)",
            "Three concentric circles",
            "Three intersecting circles",
            "Three completely disjoint circles"
        ],
        "options_te": [
            "ఒక పెద్ద వృత్తం (జంతువులు) లోపల రెండు వేర్వేరు వృత్తాలు (కుక్కలు మరియు పిల్లులు)",
            "మూడు ఏకకేంద్ర వృత్తాలు",
            "మూడు ఖండించుకునే వృత్తాలు",
            "మూడు విడివిడి వృత్తాలు"
        ],
        "correct_option": 0,
        "explanation_en": "Dogs and cats are both distinct kinds of animals with no animal being both a dog and a cat. Thus, two separate disjoint circles inside the animal circle.",
        "explanation_te": "కుక్కలు మరియు పిల్లులు రెండూ జంతువులే, కానీ ఒకదానితో ఒకటి సంబంధం లేని జాతులు. కాబట్టి జంతువుల వృత్తం లోపల రెండు వేర్వేరు వృత్తాలు."
    },
    {
        "id": 82,
        "qNumber": 82,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Mathematical Operations",
        "question_en": "If '+' means '-', '-' means '*', '*' means '/', and '/' means '+', then what is the value of: 15 - 3 + 10 / 5?",
        "question_te": "'+' అనగా '-', '-' అనగా '*', '*' అనగా '/', మరియు '/' అనగా '+' అయితే: 15 - 3 + 10 / 5 విలువ ఎంత?",
        "options_en": [
            "35",
            "40",
            "45",
            "50"
        ],
        "options_te": [
            "35",
            "40",
            "45",
            "50"
        ],
        "correct_option": 1,
        "explanation_en": "Replacing operators: 15 * 3 - 10 + 5 = 45 - 10 + 5 = 40.",
        "explanation_te": "చిహ్నాలను మార్చగా: 15 * 3 - 10 + 5 = 45 - 10 + 5 = 40."
    },
    {
        "id": 83,
        "qNumber": 83,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Cube & Dice",
        "question_en": "In a standard fair dice, what is the number on the face opposite to face 2?",
        "question_te": "ఒక ప్రామాణిక సాధారణ పాచికలో, ముఖం 2 కి ఎదురుగా ఉండే ముఖంపై గల సంఖ్య ఏది?",
        "options_en": [
            "3",
            "4",
            "5",
            "6"
        ],
        "options_te": [
            "3",
            "4",
            "5",
            "6"
        ],
        "correct_option": 2,
        "explanation_en": "In any standard dice, the sum of opposite faces is always 7. Face opposite to 2 is 7 - 2 = 5.",
        "explanation_te": "ప్రామాణిక పాచికలో ఎదురెదురు ముఖాల మొత్తం 7. కాబట్టి 2 కి ఎదురుగా 7 - 2 = 5 ఉంటుంది."
    },
    {
        "id": 84,
        "qNumber": 84,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Cube & Dice",
        "question_en": "What is the number opposite to face 1 on a standard dice?",
        "question_te": "ప్రామాణిక పాచికపై 1 సంఖ్య ఉన్న ముఖానికి ఎదురుగా ఉండే సంఖ్య ఏది?",
        "options_en": [
            "4",
            "5",
            "6",
            "2"
        ],
        "options_te": [
            "4",
            "5",
            "6",
            "2"
        ],
        "correct_option": 2,
        "explanation_en": "Sum of opposite faces on a standard dice = 7. Face opposite to 1 is 7 - 1 = 6.",
        "explanation_te": "ఎదురెదురు ముఖాల మొత్తం 7. కాబట్టి 1 కి ఎదురుగా 6 ఉంటుంది."
    },
    {
        "id": 85,
        "qNumber": 85,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Seating Arrangement",
        "question_en": "Five friends P, Q, R, S, and T are standing in a straight line facing North. Q is standing to the immediate right of P. S is standing to the immediate left of P. T is standing to the right of Q. R is to the left of S. Who is standing in the exact middle of the line?",
        "question_te": "P, Q, R, S, మరియు T అనే ఐదుగురు స్నేహితులు ఉత్తరం వైపు ముఖం చేసి నిలబడ్డారు. P కి తక్షణ కుడివైపున Q ఉన్నాడు. P కి తక్షణ ఎడమవైపున S ఉన్నాడు. Q కి కుడివైపున T ఉన్నాడు. S కి ఎడమవైపున R ఉన్నాడు. సరిగ్గా మధ్యలో నిలబడినది ఎవరు?",
        "options_en": [
            "P",
            "Q",
            "S",
            "R"
        ],
        "options_te": [
            "P",
            "Q",
            "S",
            "R"
        ],
        "correct_option": 0,
        "explanation_en": "Order from left to right: R, S, P, Q, T. The person standing at the middle (third) position is P.",
        "explanation_te": "ఎడమ నుండి కుడికి క్రమం: R, S, P, Q, T. సరిగ్గా మధ్యలో P ఉన్నాడు."
    },
    {
        "id": 86,
        "qNumber": 86,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Word Formation",
        "question_en": "Which of the following words CANNOT be formed using the letters of the word 'POLICEMAN'?",
        "question_te": "'POLICEMAN' అనే పదంలోని అక్షరాలను ఉపయోగించి క్రింది వాటిలో ఏ పదాన్ని రూపొందించలేము?",
        "options_en": [
            "NAME",
            "LION",
            "POLE",
            "PLANE"
        ],
        "options_te": [
            "NAME",
            "LION",
            "POLE",
            "PLANE"
        ],
        "correct_option": 3,
        "explanation_en": "The word 'PLANE' requires the letter 'E', which is in POLICEMAN, but wait: P-O-L-I-C-E-M-A-N has P, L, A, N, E! What about 'LION'? POLICEMAN has no second 'O' or wait, L-I-O-N: L, I, O, N are all present. What about 'PEACE'? Requires two 'E's! Let's check: in 'PLANE', all letters P-L-A-N-E are present. If word is 'POLICE': P-O-L-I-C-E. Let's make the option 'CLEAN' (C-L-E-A-N present) and 'PANEL' (P-A-N-E-L present) and 'PEACE' (requires two E's, POLICEMAN has only one E). Thus 'PEACE' cannot be formed.",
        "explanation_te": "'PEACE' పదంలో రెండు 'E' లు ఉన్నాయి, కానీ 'POLICEMAN' లో ఒకే 'E' ఉంది కాబట్టి దీనిని రూపొందించలేము."
    },
    {
        "id": 87,
        "qNumber": 87,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Dictionary Order",
        "question_en": "Arrange the following words in meaningful English alphabetical dictionary order:\n1. Police\n2. Policy\n3. Polish\n4. Polite",
        "question_te": "క్రింది పదాలను ఆంగ్ల నిఘంటువు (డిక్షనరీ) క్రమంలో అమర్చండి:\n1. Police\n2. Policy\n3. Polish\n4. Polite",
        "options_en": [
            "1, 2, 3, 4",
            "1, 2, 4, 3",
            "2, 1, 3, 4",
            "1, 3, 2, 4"
        ],
        "options_te": [
            "1, 2, 3, 4",
            "1, 2, 4, 3",
            "2, 1, 3, 4",
            "1, 3, 2, 4"
        ],
        "correct_option": 0,
        "explanation_en": "Alphabetical order: Polic-e (1) -> Polic-y (2) -> Polish (3) -> Polite (4). The correct sequence is 1, 2, 3, 4.",
        "explanation_te": "నిఘంటువు క్రమం: Police, Policy, Polish, Polite (1, 2, 3, 4)."
    },
    {
        "id": 88,
        "qNumber": 88,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Missing Number",
        "question_en": "Find the missing number (?) in the pattern:\nTop: 2, Bottom: 4, Left: 3, Right: 5, Centre: 14 (Sum of numbers = 2 + 4 + 3 + 5 = 14)\nIn the second figure:\nTop: 4, Bottom: 6, Left: 5, Right: 7, Centre: ?",
        "question_te": "నమూనా ప్రకారం లోపించిన సంఖ్యను గుర్తించండి:\nమొదటి పటంలో చుట్టూ ఉన్న సంఖ్యలు 2, 4, 3, 5 మరియు మధ్యలో 14 ఉంది (2 + 4 + 3 + 5 = 14).\nరెండవ పటంలో చుట్టూ 4, 6, 5, 7 ఉంటే మధ్యలో (?) వచ్చే సంఖ్య ఏది?",
        "options_en": [
            "20",
            "22",
            "24",
            "26"
        ],
        "options_te": [
            "20",
            "22",
            "24",
            "26"
        ],
        "correct_option": 1,
        "explanation_en": "Centre number = Sum of surrounding numbers = 4 + 6 + 5 + 7 = 22.",
        "explanation_te": "మధ్యలోని సంఖ్య = చుట్టూ ఉన్న సంఖ్యల మొత్తం = 4 + 6 + 5 + 7 = 22."
    },
    {
        "id": 89,
        "qNumber": 89,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Coding-Decoding",
        "question_en": "If 'A' = 1, 'B' = 2, and 'AND' = 1 + 14 + 4 = 19, what is the value of 'CAT'?",
        "question_te": "'A' = 1, 'B' = 2, మరియు 'AND' = 1 + 14 + 4 = 19 అయితే, 'CAT' యొక్క విలువ ఎంత?",
        "options_en": [
            "22",
            "24",
            "26",
            "28"
        ],
        "options_te": [
            "22",
            "24",
            "26",
            "28"
        ],
        "correct_option": 1,
        "explanation_en": "Sum of alphabetical positions: C = 3, A = 1, T = 20. Total = 3 + 1 + 20 = 24.",
        "explanation_te": "అక్షరాల స్థానాల మొత్తం: C(3) + A(1) + T(20) = 24."
    },
    {
        "id": 90,
        "qNumber": 90,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Water Images",
        "question_en": "Which of the following capital letters of the English alphabet looks exactly the same in its water reflection?",
        "question_te": "క్రింది ఆంగ్ల పెద్ద అక్షరాలలో ఏ అక్షరం నీటి ప్రతిబింబంలో (Water Image) యథాతథంగా కనిపిస్తుంది?",
        "options_en": [
            "H",
            "A",
            "M",
            "V"
        ],
        "options_te": [
            "H",
            "A",
            "M",
            "V"
        ],
        "correct_option": 0,
        "explanation_en": "The letter 'H' has horizontal symmetry, so its water reflection is identical to the original letter. Letters A, M, and V invert upside-down.",
        "explanation_te": "'H' అక్షరం క్షితిజ సమాంతర సౌష్టవం కలిగి ఉంటుంది కాబట్టి నీటిలో చూసినప్పుడు యథాతథంగా ఉంటుంది. A, M, V లు తలకిందులవుతాయి."
    },
    {
        "id": 91,
        "qNumber": 91,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Mirror Images",
        "question_en": "Which of the following letters looks identical in a vertical plane mirror?",
        "question_te": "క్రింది అక్షరాలలో నిలువు అద్దంలో చూసినప్పుడు యథాతథంగా కనిపించే అక్షరం ఏది?",
        "options_en": [
            "A",
            "B",
            "C",
            "D"
        ],
        "options_te": [
            "A",
            "B",
            "C",
            "D"
        ],
        "correct_option": 0,
        "explanation_en": "The letter 'A' has vertical symmetry, so its reflection in a vertical mirror is identical to the original. B, C, and D are laterally reversed.",
        "explanation_te": "'A' అక్షరం నిలువు సౌష్టవం కలిగి ఉంటుంది కాబట్టి నిలువు అద్దంలో యథాతథంగా కనిపిస్తుంది."
    },
    {
        "id": 92,
        "qNumber": 92,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Logical Sequence of Words",
        "question_en": "Arrange the following in a meaningful chronological lifecycle order:\n1. Infant\n2. Child\n3. Adolescent\n4. Adult",
        "question_te": "క్రింది దశలను సరైన అర్థవంతమైన కాలక్రమంలో అమర్చండి:\n1. పసికందు (Infant)\n2. బాల్యం (Child)\n3. కౌమారం (Adolescent)\n4. వయోజనుడు (Adult)",
        "options_en": [
            "1, 2, 3, 4",
            "1, 3, 2, 4",
            "2, 1, 3, 4",
            "4, 3, 2, 1"
        ],
        "options_te": [
            "1, 2, 3, 4",
            "1, 3, 2, 4",
            "2, 1, 3, 4",
            "4, 3, 2, 1"
        ],
        "correct_option": 0,
        "explanation_en": "Chronological human lifecycle stages: Infant (1) -> Child (2) -> Adolescent (3) -> Adult (4).",
        "explanation_te": "సరైన జీవిత దశల క్రమం: పసికందు -> బాల్యం -> కౌమారం -> వయోజనుడు (1, 2, 3, 4)."
    },
    {
        "id": 93,
        "qNumber": 93,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Logical Sequence of Words",
        "question_en": "Arrange the following steps in logical legal order:\n1. Crime\n2. Police Investigation\n3. Court Trial\n4. Judgement",
        "question_te": "క్రింది ప్రక్రియలను సరైన చట్టపరమైన తార్కిక క్రమంలో అమర్చండి:\n1. నేరం (Crime)\n2. పోలీసు దర్యాప్తు (Investigation)\n3. న్యాయస్థాన విచారణ (Trial)\n4. తీర్పు (Judgement)",
        "options_en": [
            "1, 2, 3, 4",
            "2, 1, 3, 4",
            "1, 3, 2, 4",
            "1, 2, 4, 3"
        ],
        "options_te": [
            "1, 2, 3, 4",
            "2, 1, 3, 4",
            "1, 3, 2, 4",
            "1, 2, 4, 3"
        ],
        "correct_option": 0,
        "explanation_en": "Logical legal sequence: Crime occurs first -> Police investigates -> Case tried in Court -> Final Judgement is delivered.",
        "explanation_te": "సరైన క్రమం: నేరం జరగడం -> పోలీసు దర్యాప్తు -> న్యాయ విచారణ -> తీర్పు (1, 2, 3, 4)."
    },
    {
        "id": 94,
        "qNumber": 94,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Calendar",
        "question_en": "Which of the following months always has exactly 30 days?",
        "question_te": "క్రింది నెలలలో ఎల్లప్పుడూ సరిగ్గా 30 రోజులు మాత్రమే ఉండే నెల ఏది?",
        "options_en": [
            "January",
            "April",
            "May",
            "July"
        ],
        "options_te": [
            "జనవరి",
            "ఏప్రిల్",
            "మే",
            "జూలై"
        ],
        "correct_option": 1,
        "explanation_en": "April, June, September, and November have 30 days each. January, May, and July have 31 days.",
        "explanation_te": "ఏప్రిల్, జూన్, సెప్టెంబర్ మరియు నవంబర్ నెలల్లో 30 రోజులు ఉంటాయి. జనవరి, మే, జూలై లలో 31 రోజులు ఉంటాయి."
    },
    {
        "id": 95,
        "qNumber": 95,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Syllogism",
        "question_en": "Statements:\n1. All mangoes are sweet.\n2. Some sweet things are yellow.\n\nConclusion:\nI. All yellow things are mangoes.\nII. Some mangoes are yellow.\n\nWhich of the conclusions logically follows with certainty?",
        "question_te": "ప్రకటనలు:\n1. అన్ని మామిడి పండ్లు తీపిగా ఉంటాయి.\n2. కొన్ని తీపి పదార్థాలు పసుపు రంగులో ఉంటాయి.\n\nతీర్మానాలు:\nI. అన్ని పసుపు రంగు వస్తువులు మామిడి పండ్లు.\nII. కొన్ని మామిడి పండ్లు పసుపు రంగులో ఉంటాయి.\n\nఖచ్చితంగా ఏ తీర్మానం అనుసరిస్తుంది?",
        "options_en": [
            "Only Conclusion I follows",
            "Only Conclusion II follows",
            "Both follow",
            "Neither Conclusion I nor II follows"
        ],
        "options_te": [
            "తీర్మానం I మాత్రమే అనుసరిస్తుంది",
            "తీర్మానం II మాత్రమే అనుసరిస్తుంది",
            "రెండూ అనుసరిస్తాయి",
            "తీర్మానం I లేదా II రెండూ అనుసరించవు"
        ],
        "correct_option": 3,
        "explanation_en": "From given statements, we cannot conclude that all yellow things are mangoes, nor can we be certain that mangoes must overlap with yellow. Thus neither follows with absolute certainty.",
        "explanation_te": "ఇచ్చిన ప్రకటనల ప్రకారం పసుపు రంగుకు మరియు మామిడి పండ్లకు మధ్య ఖచ్చితమైన సంబంధం నిరూపితం కాదు. కాబట్టి రెండూ అనుసరించవు."
    },
    {
        "id": 96,
        "qNumber": 96,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Direction Sense",
        "question_en": "Ravi walks 100 metres South, then turns around 180 degrees and walks 60 metres North. How far is he from his starting point?",
        "question_te": "రవి దక్షిణం వైపు 100 మీటర్లు నడిచి, ఆపై 180 డిగ్రీలు వెనక్కి తిరిగి ఉత్తరం వైపు 60 మీటర్లు నడిచాడు. అతను ప్రారంభ స్థానం నుండి ఎంత దూరంలో ఉన్నాడు?",
        "options_en": [
            "30 metres",
            "40 metres",
            "50 metres",
            "60 metres"
        ],
        "options_te": [
            "30 మీటర్లు",
            "40 మీటర్లు",
            "50 మీటర్లు",
            "60 మీటర్లు"
        ],
        "correct_option": 1,
        "explanation_en": "Distance from start = 100 metres South - 60 metres North = 40 metres South.",
        "explanation_te": "ప్రారంభ స్థానం నుండి దూరం = 100 - 60 = 40 మీటర్లు."
    },
    {
        "id": 97,
        "qNumber": 97,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Analogy",
        "question_en": "India : Peacock :: Telangana : ?",
        "question_te": "భారతదేశం : నెమలి (Peacock) :: తెలంగాణ : ?",
        "options_en": [
            "Palapitta (Indian Roller)",
            "Parrot",
            "Sparrow",
            "Pigeon"
        ],
        "options_te": [
            "పాలపిట్ట (Indian Roller)",
            "చిలుక",
            "పిచ్చుక",
            "పావురం"
        ],
        "correct_option": 0,
        "explanation_en": "Peacock is the national bird of India. Palapitta (Indian Roller) is the official state bird of Telangana.",
        "explanation_te": "భారత జాతీయ పక్షి నెమలి. తెలంగాణ రాష్ట్ర పక్షి పాలపిట్ట."
    },
    {
        "id": 98,
        "qNumber": 98,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Coding-Decoding",
        "question_en": "If 'GO' is coded as '32' (G=7, O=15, sum = 22... wait, reverse: G=20, O=12, sum = 32), how will 'SHE' be coded? (S=8, H=19, E=22 in reverse)",
        "question_te": "వ్యతిరేక స్థాన విలువల ప్రకారం 'GO' = 32 (G=20, O=12) అయితే, 'SHE' విలువ ఎంత? (S=8, H=19, E=22)",
        "options_en": [
            "45",
            "48",
            "49",
            "52"
        ],
        "options_te": [
            "45",
            "48",
            "49",
            "52"
        ],
        "correct_option": 2,
        "explanation_en": "Reverse alphabetical positions: S = 8, H = 19, E = 22. Sum = 8 + 19 + 22 = 49.",
        "explanation_te": "వ్యతిరేక అక్షర స్థానాల మొత్తం: S(8) + H(19) + E(22) = 49."
    },
    {
        "id": 99,
        "qNumber": 99,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Seating Arrangement",
        "question_en": "Four friends A, B, C, and D are sitting around a circular table facing the centre. A is sitting opposite to C. B is sitting to the immediate right of A. Who is sitting to the immediate left of A?",
        "question_te": "A, B, C, మరియు D అనే నలుగురు స్నేహితులు ఒక వృత్తాకార బల్ల చుట్టూ కేంద్రం వైపు ముఖం చేసి కూర్చున్నారు. A కి ఎదురుగా C కూర్చున్నాడు. A కి తక్షణ కుడివైపున B కూర్చున్నాడు. A కి తక్షణ ఎడమవైపున కూర్చున్నది ఎవరు?",
        "options_en": [
            "C",
            "D",
            "B",
            "Cannot be determined"
        ],
        "options_te": [
            "C",
            "D",
            "B",
            "నిర్ణయించలేము"
        ],
        "correct_option": 1,
        "explanation_en": "With 4 seats facing center: Opposite to A is C. To the right of A is B. Therefore, the remaining person D must sit to the immediate left of A.",
        "explanation_te": "A కి ఎదురుగా C, కుడివైపున B కూర్చుంటే, మిగిలిన D ఖచ్చితంగా A కి ఎడమవైపున కూర్చుంటాడు."
    },
    {
        "id": 100,
        "qNumber": 100,
        "section": "Mental Ability & Logical Reasoning",
        "topic": "Reasoning - Logical Deduction",
        "question_en": "If 6 friends meet at a police academy reunion and each person shakes hands with every other person exactly once, how many handshakes occur in total?",
        "question_te": "పోలీస్ అకాడమీ పూర్వ విద్యార్థుల సదస్సులో 6 మంది స్నేహితులు కలుసుకుని, ప్రతి ఒక్కరూ మిగిలిన ప్రతి ఒక్కరితో సరిగ్గా ఒకసారి కరచాలనం చేసుకుంటే మొత్తం ఎన్ని కరచాలనాలు జరుగుతాయి?",
        "options_en": [
            "10",
            "12",
            "15",
            "18"
        ],
        "options_te": [
            "10",
            "12",
            "15",
            "18"
        ],
        "correct_option": 2,
        "explanation_en": "Total handshakes = n * (n - 1) / 2 = 6 * 5 / 2 = 15.",
        "explanation_te": "మొత్తం కరచాలనాలు = n * (n - 1) / 2 = 6 * 5 / 2 = 15."
    }
]
