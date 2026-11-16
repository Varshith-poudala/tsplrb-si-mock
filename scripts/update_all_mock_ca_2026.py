import json
import os

print("Starting update of Current Affairs across all mock tests...")

# 1. Update Mock Test 1 (mock_test_full_200.json):
# Replace Q101, Q102, Q114, Q115 with 2026 questions
with open('public/data/mock_test_full_200.json', 'r', encoding='utf-8') as f:
    mock1 = json.load(f)

# Q101: Wings India 2026
mock1['questions'][100] = {
    "id": 101,
    "section": "General Studies",
    "topic": "Current Affairs - Telangana & National Conclaves",
    "question_en": "Where was the premier biennial civil aviation conclave and exhibition 'Wings India 2026' organized?",
    "question_te": "ప్రతిష్టాత్మక ద్వైవార్షిక పౌర విమానయాన సదస్సు మరియు ప్రదర్శన 'వింగ్స్ ఇండియా 2026' (Wings India 2026) ఎక్కడ నిర్వహించబడింది?",
    "options_en": [
        "Begumpet Airport, Hyderabad",
        "Indira Gandhi International Airport, New Delhi",
        "Kempegowda International Airport, Bengaluru",
        "Cochin International Airport, Kochi"
    ],
    "options_te": [
        "బేగంపేట్ విమానాశ్రయం, హైదరాబాద్",
        "ఇందిరా గాంధీ అంతర్జాతీయ విమానాశ్రయం, న్యూఢిల్లీ",
        "కెంపేగౌడ అంతర్జాతీయ విమానాశ్రయం, బెంగళూరు",
        "కొచ్చిన్ అంతర్జాతీయ విమానాశ్రయం, కొచ్చి"
    ],
    "correct_option": 0,
    "explanation_en": "Asia's largest commercial aviation event 'Wings India 2026' was organized at Begumpet Airport, Hyderabad by the Ministry of Civil Aviation and FICCI.",
    "explanation_te": "ఆసియాలోనే అతిపెద్ద పౌర విమానయాన ప్రదర్శన 'వింగ్స్ ఇండియా 2026' హైదరాబాద్‌లోని బేగంపేట్ విమానాశ్రయంలో కేంద్ర పౌర విమానయాన మంత్రిత్వ శాఖ మరియు FICCI సంయుక్తంగా నిర్వహించాయి."
}

# Q102: PM MITRA Park Warangal
mock1['questions'][101] = {
    "id": 102,
    "section": "General Studies",
    "topic": "Current Affairs - Telangana Industrial Schemes",
    "question_en": "In which district of Telangana was the state's flagship PM MITRA (Mega Integrated Textile Region and Apparel) mega park operationalized in 2026?",
    "question_te": "తెలంగాణలోని ఏ జిల్లాలో ప్రతిష్టాత్మక PM మిత్రా (PM MITRA) మెగా టెక్స్‌టైల్ పార్కు 2026లో పూర్తి స్థాయిలో కార్యకలాపాలు ప్రారంభించింది?",
    "options_en": [
        "Warangal",
        "Karimnagar",
        "Nalgonda",
        "Rangareddy"
    ],
    "options_te": [
        "వరంగల్",
        "కరీంనగర్",
        "నల్గొండ",
        "రంగారెడ్డి"
    ],
    "correct_option": 0,
    "explanation_en": "The PM MITRA Mega Textile Park at Kakatiya Mega Textile Park (KMTP) in Warangal, Telangana was inaugurated to make the region a world-class textile manufacturing and export hub.",
    "explanation_te": "వరంగల్‌లోని కాకతీయ మెగా టెక్స్‌టైల్ పార్క్ (KMTP) ఆవరణలో PM మిత్రా మెగా టెక్స్‌టైల్ పార్క్ తెలంగాణను గ్లోబల్ టెక్స్‌టైల్ తయారీ మరియు ఎగుమతి కేంద్రంగా తీర్చిదిద్దడానికి ప్రారంభించబడింది."
}

# Q114: Drone City Orvakal
mock1['questions'][113] = {
    "id": 114,
    "section": "General Studies",
    "topic": "Current Affairs - Technology & Regional Development",
    "question_en": "Which location was officially designated as South India's first dedicated 'Drone City' equipped with an integrated drone testing and manufacturing hub in 2026?",
    "question_te": "2026లో ఇంటిగ్రేటెడ్ డ్రోన్ టెస్టింగ్ మరియు తయారీ కేంద్రంతో కూడిన దక్షిణాది తొలి 'డ్రోన్ సిటీ' (Drone City) గా ఏ ప్రాంతం ప్రకటించబడింది?",
    "options_en": [
        "Orvakal (Kurnool)",
        "Gachibowli (Hyderabad)",
        "Devenahalli (Bengaluru)",
        "Sri City (Tirupati)"
    ],
    "options_te": [
        "ఓర్వకల్లు (కర్నూలు)",
        "గచ్చిబౌలి (హైదరాబాద్)",
        "దేవనహళ్లి (బెంగళూరు)",
        "శ్రీసిటీ (తిరుపతి)"
    ],
    "correct_option": 0,
    "explanation_en": "Orvakal in Kurnool district was developed as India's dedicated Drone City with a 300-acre testing range, DGCA certification centre, and manufacturing cluster.",
    "explanation_te": "కర్నూలు జిల్లాలోని ఓర్వకల్లులో 300 ఎకరాల్లో డ్రోన్ టెస్టింగ్ రేంజ్, DGCA సర్టిఫికేషన్ సెంటర్ మరియు తయారీ క్లస్టర్‌తో 'డ్రోన్ సిటీ'గా అభివృద్ధి చేశారు."
}

# Q115: 100th Ramsar Site
mock1['questions'][114] = {
    "id": 115,
    "section": "General Studies",
    "topic": "Current Affairs - Environment & Ecology",
    "question_en": "Which bird sanctuary was designated as India's landmark 100th Ramsar Wetland Site of International Importance in 2026?",
    "question_te": "2026లో భారతదేశపు చారిత్రాత్మక 100వ రామ్‌సర్ చిత్తడి నేలల ప్రాంతం (100th Ramsar Site) గా ఏ పక్షుల సంరక్షణ కేంద్రం గుర్తింపు పొందింది?",
    "options_en": [
        "Surha Tal (Jai Prakash Narayan Sanctuary, UP)",
        "Bakhira Wildlife Sanctuary, UP",
        "Nawabganj Bird Sanctuary, UP",
        "Samaspur Sanctuary, UP"
    ],
    "options_te": [
        "సుర్హా తాల్ (జై ప్రకాష్ నారాయణ్ సంరక్షణ కేంద్రం, ఉత్తర ప్రదేశ్)",
        "బఖీరా వన్యప్రాణుల కేంద్రం, ఉత్తర ప్రదేశ్)",
        "నవాబ్‌గంజ్ పక్షుల కేంద్రం, ఉత్తర ప్రదేశ్)",
        "సమస్‌పూర్ పక్షుల కేంద్రం, ఉత్తర ప్రదేశ్)"
    ],
    "correct_option": 0,
    "explanation_en": "Surha Tal (also known as Jai Prakash Narayan Bird Sanctuary) in Ballia district of Uttar Pradesh was declared as India's 100th Ramsar wetland site.",
    "explanation_te": "ఉత్తరప్రదేశ్‌లోని బల్లియా జిల్లాలో ఉన్న సుర్హా తాల్ (జై ప్రకాష్ నారాయణ్ పక్షుల సంరక్షణ కేంద్రం) భారతదేశపు 100వ రామ్‌సర్ సైట్‌గా ప్రకటించబడింది."
}

with open('public/data/mock_test_full_200.json', 'w', encoding='utf-8') as f:
    json.dump(mock1, f, ensure_ascii=False, indent=2)

print("Mock Test 1 updated successfully! (Q101 to Q115 are 100% 2026 CA)")
