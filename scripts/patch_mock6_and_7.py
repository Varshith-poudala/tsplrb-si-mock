import json

# Patch Mock 6 Q143 and Q147
with open('public/data/mock_test_full_200_6.json', 'r', encoding='utf-8') as f:
    m6 = json.load(f)

m6['questions'][142] = {
    "id": 143,
    "section": "General Studies",
    "topic": "Current Affairs - Badminton 2026",
    "question_en": "Who won the Men’s Singles crown at the 2026 BWF India Open Badminton Championship held in New Delhi?",
    "question_te": "న్యూఢిల్లీలో జరిగిన '2026 BWF ఇండియా ఓపెన్ బ్యాడ్మింటన్ ఛాంపియన్‌షిప్' పురుషుల సింగిల్స్ టైటిల్‌ను ఎవరు గెలుచుకున్నారు?",
    "options_en": ["Shi Yuqi", "Viktor Axelsen", "Lakshya Sen", "Lee Zii Jia"],
    "options_te": ["షి యుకి", "విక్టర్ ఆక్సెల్సన్", "లక్ష్య సేన్", "లీ జీ జియా"],
    "correct_option": 0,
    "explanation_en": "China's Shi Yuqi defeated Hong Kong's Lee Cheuk Yiu to clinch the 2026 BWF India Open Super 750 Men's Singles title at K.D. Jadhav Indoor Stadium.",
    "explanation_te": "2026 ఇండియా ఓపెన్ బ్యాడ్మింటన్ పురుషుల సింగిల్స్ ఫైనల్లో చైనా స్టార్ షట్లర్ షి యుకి విజయం సాధించారు."
}

m6['questions'][146] = {
    "id": 147,
    "section": "General Studies",
    "topic": "Current Affairs - Global Tech Summits 2026",
    "question_en": "Which country hosted the AI Action Summit in 2026 bringing together world leaders and technology pioneers to establish global AI safety protocols?",
    "question_te": "గ్లోబల్ AI భద్రతా నిబంధనలను రూపొందించడానికి ప్రపంచ నాయకులు మరియు సాంకేతిక నిపుణులతో '2026 AI యాక్షన్ సమ్మిట్' కు ఆతిథ్యమిచ్చిన దేశం ఏది?",
    "options_en": ["France", "United Kingdom", "South Korea", "Japan"],
    "options_te": ["ఫ్రాన్స్", "యునైటెడ్ కింగ్‌డమ్", "దక్షిణ కొరియా", "జపాన్"],
    "correct_option": 0,
    "explanation_en": "France hosted the global AI Action Summit in Paris in early 2026, building upon the Bletchley Park and Seoul AI safety declarations.",
    "explanation_te": "పారిస్‌లో నిర్వహించిన 2026 అంతర్జాతీయ AI యాక్షన్ సమ్మిట్‌కు ఫ్రాన్స్ ఆతిథ్యమిచ్చింది."
}

with open('public/data/mock_test_full_200_6.json', 'w', encoding='utf-8') as f:
    json.dump(m6, f, ensure_ascii=False, indent=2)

print("Mock 6 patched successfully!")

# Patch Mock 7 Q145
with open('public/data/mock_test_full_200_7.json', 'r', encoding='utf-8') as f:
    m7 = json.load(f)

m7['questions'][144] = {
    "id": 145,
    "section": "General Studies",
    "topic": "Current Affairs - Wildlife & Ecology 2026",
    "question_en": "Which state was officially certified as India's premier 'Tiger State' in the 2026 National Tiger Conservation Assessment with the highest tiger population?",
    "question_te": "2026 జాతీయ పులుల సంరక్షణ అంచనా ప్రకారం అత్యధిక సంఖ్యలో పులులు కలిగిన భారతదేశపు నంబర్ 1 'టైగర్ స్టేట్' గా ఏ రాష్ట్రం నిలిచింది?",
    "options_en": ["Madhya Pradesh", "Karnataka", "Uttarakhand", "Maharashtra"],
    "options_te": ["మధ్యప్రదేశ్", "కర్ణాటక", "ఉత్తరాఖండ్", "మహారాష్ట్ర"],
    "correct_option": 0,
    "explanation_en": "Madhya Pradesh retained its distinguished status as India’s Tiger State in the 2026 assessment, housing the maximum wild tiger population across its 7 tiger reserves.",
    "explanation_te": "2026 జాతీయ అంచనాలో మధ్యప్రదేశ్ తన 7 టైగర్ రిజర్వ్‌లలో అత్యధిక సంఖ్యలో పులులను కలిగి ఉండి 'టైగర్ స్టేట్' హోదాను నిలబెట్టుకుంది."
}

with open('public/data/mock_test_full_200_7.json', 'w', encoding='utf-8') as f:
    json.dump(m7, f, ensure_ascii=False, indent=2)

print("Mock 7 patched successfully!")
