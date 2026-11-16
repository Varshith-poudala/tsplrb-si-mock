#!/usr/bin/env python3
"""
Full 200-Question Paper Generator for TSPLRB SI Prelims Examination.
Follows the official TSPLRB Syllabus:
  Part A: Arithmetic (Q1 - 50)
  Part B: Reasoning & Mental Ability (Q51 - 100)
  Part C: General Studies (Q101 - 200)
    - Current Affairs & Events of National & International Importance (Q101 - 115)
    - General Science & Environment / Tech (Q116 - 130)
    - History of India & Indian National Movement (Q131 - 145)
    - Geography of India & Telangana (Q146 - 157)
    - Indian Polity & Governance (Q158 - 170)
    - Indian Economy & Telangana Economy (Q171 - 180)
    - Telangana History, Society, Culture, Arts & Literature (Q181 - 190)
    - Telangana Movement & State Formation (Q191 - 200)
"""

import json
import os

# Import Part A (1-50) and Part B (51-100) from generate_day3_questions.py
from generate_day3_questions import questions as base_100_questions

gs_questions = [
    # =========================================================================
    # 1. ULTRA-LATEST CURRENT AFFAIRS & CONTEMPORARY EVENTS (Q101 - Q115)
    # =========================================================================
    {
        "id": 101,
        "section": "General Studies",
        "topic": "Current Affairs - Telangana Administration",
        "question_en": "What is the primary mandate of 'HYDRAA' (Hyderabad Disaster Response and Asset Protection Agency) established by the Government of Telangana in 2024?",
        "question_te": "2024 లో తెలంగాణ ప్రభుత్వం ప్రత్యేకంగా ఏర్పాటు చేసిన 'హైడ్రా' (HYDRAA) ఏజెన్సీ యొక్క ముఖ్య విధులు ఏమిటి?",
        "options_en": ["Disaster management and protection of lakes, water bodies (FTL/buffer zones) and government properties from encroachments", "Recruitment of sub-inspectors and constables across the state", "Issuing commercial building permits and municipal trade licenses", "Collection of property taxes and municipal electricity bills"],
        "options_te": ["విపత్తుల నిర్వహణతో పాటు చెరువులు, కుంటలు (FTL/బఫర్ జోన్లు) మరియు ప్రభుత్వ ఆస్తులను ఆక్రమణల నుండి రక్షించడం", "రాష్ట్రవ్యాప్తంగా పోలీసుల నియామకాలు చేపట్టడం", "వాణిజ్య భవన నిర్మాణ అనుమతులు జారీ చేయడం", "ఆస్తి పన్నులు మరియు విద్యుత్ బిల్లుల వసూలు"],
        "correct_option": 0,
        "explanation_en": "HYDRAA was created via G.O. Ms. No. 99 in July 2024 covering the Telangana Core Urban Region (ORR area) for disaster response, flood mitigation, and clearing encroachments on water bodies and public lands.",
        "explanation_te": "హైదరాబాద్ ఔటర్ రింగ్ రోడ్ (ORR) పరిధిలోని చెరువులు, నాలాలు, ప్రభుత్వ భూములను ఆక్రమణల నుండి కాపాడటానికి మరియు వరద విపత్తుల నిర్వహణ కోసం తెలంగాణ ప్రభుత్వం 'హైడ్రా' (HYDRAA) ను ఏర్పాటు చేసింది."
    },
    {
        "id": 102,
        "section": "General Studies",
        "topic": "Current Affairs - Telangana Education & Industry",
        "question_en": "Who was appointed as the Chairperson of the Board of Governors of the newly established 'Young India Skills University' in Telangana in 2024?",
        "question_te": "తెలంగాణ ప్రభుత్వం 2024 లో ముచ్చర్ల వద్ద ఏర్పాటు చేసిన 'యంగ్ ఇండియా స్కిల్స్ యూనివర్సిటీ' గవర్నింగ్ బోర్డు చైర్మన్‌గా ఎవరు నియమితులయ్యారు?",
        "options_en": ["Anand Mahindra (Chairman, Mahindra Group)", "Ratan Tata (Former Chairman, Tata Sons)", "N. R. Narayana Murthy (Founder, Infosys)", "Azim Premji (Former Chairman, Wipro)"],
        "options_te": ["ఆనంద్ మహీంద్రా (మహీంద్రా గ్రూప్ ఛైర్మన్)", "రతన్ టాటా", "ఎన్. ఆర్. నారాయణ మూర్తి", "అజీమ్ ప్రేమ్‌జీ"],
        "correct_option": 0,
        "explanation_en": "Industrialist Anand Mahindra was appointed as the first Chairman of the Board of Governors of the Young India Skills University, established to impart industry-ready technical skills to youth.",
        "explanation_te": "యువతకు పరిశ్రమలకు అవసరమైన ఆధునిక సాంకేతిక నైపుణ్యాలను అందించేందుకు ఏర్పాటైన 'యంగ్ ఇండియా స్కిల్స్ యూనివర్సిటీ' చైర్మన్‌గా ప్రముఖ పారిశ్రామికవేత్త ఆనంద్ మహీంద్రా నియమితులయ్యారు."
    },
    {
        "id": 103,
        "section": "General Studies",
        "topic": "Current Affairs - Telangana Culture & Symbols",
        "question_en": "In 2024, the Government of Telangana officially adopted which song, penned by renowned poet Andesri with music by M. M. Keeravani, as the official State Song of Telangana?",
        "question_te": "2024 లో తెలంగాణ ప్రభుత్వం అధికారిక రాష్ట్ర గీతంగా ఆమోదించిన, ప్రజాకవి అందెశ్రీ రచించిన గీతం ఏది?",
        "options_en": ["Jaya Jaya He Telangana Janani Jayaketanam", "Palle Kanneeru Peduthundo", "Na Telangana Koti Rathanala Veena", "Nageti Sallalla Na Telangana"],
        "options_te": ["జయ జయహే తెలంగాణ జననీ జయకేతనం (Jaya Jaya He Telangana)", "పల్లె కన్నీరు పెడుతుందో", "నా తెలంగాణ కోటి రతనాల వీణ", "నాగేటి సాళ్ళల్లో నా తెలంగాణ"],
        "correct_option": 0,
        "explanation_en": "'Jaya Jaya He Telangana Janani Jayaketanam', authored by Praja Kavi Andesri and re-orchestrated by Oscar-winner M. M. Keeravani, was officially notified as Telangana's State Song in June 2024.",
        "explanation_te": "ప్రజాకవి అందెశ్రీ రచించి, ఎం. ఎం. కీరవాణి సంగీత స్వరకల్పన చేసిన 'జయ జయహే తెలంగాణ జననీ జయకేతనం' గేయాన్ని ప్రభుత్వం అధికారిక రాష్ట్ర గీతంగా నోటిఫై చేసింది."
    },
    {
        "id": 104,
        "section": "General Studies",
        "topic": "Current Affairs - Sports",
        "question_en": "In September 2024, the Indian contingent created history at the 45th FIDE Chess Olympiad held in Budapest, Hungary by achieving which unprecedented feat?",
        "question_te": "సెప్టెంబర్ 2024 లో బుడాపెస్ట్ (హంగేరి) లో జరిగిన 45వ చెస్ ఒలింపియాడ్‌లో భారతదేశం ఏ చారిత్రాత్మక ఘనత సాధించింది?",
        "options_en": ["Historic double Gold medals in both Men's Open and Women's team sections", "Winning the Silver medal behind China", "Winning only individual bronze medals", "Finishing outside the top 5 ranking"],
        "options_te": ["పురుషుల ఓపెన్ మరియు మహిళల విభాగాలలో చారిత్రాత్మక డబుల్ స్వర్ణ పతకాలు (Double Gold)", "చైనా వెనుక రజత పతకం సాధించడం", "వ్యక్తిగత కాంస్య పతకం మాత్రమే పొందడం", "టాప్-5 బయట నిలవడం"],
        "correct_option": 0,
        "explanation_en": "India scripted history at the 45th Chess Olympiad 2024 in Budapest by winning Gold in both Open (featuring D. Gukesh, Arjun Erigaisi, Praggnanandhaa) and Women's sections.",
        "explanation_te": "బుడాపెస్ట్ 45వ చెస్ ఒలింపియాడ్‌లో డి. గుకేశ్, అర్జున్ ఎరిగైసి వంటి యువ గ్రాండ్‌మాస్టర్ల అద్భుత ప్రదర్శనతో భారత్ ఓపెన్ మరియు మహిళల విభాగాల రెండింటిలోనూ చారిత్రాత్మక స్వర్ణాలు గెలిచింది."
    },
    {
        "id": 105,
        "section": "General Studies",
        "topic": "Current Affairs - Constitutional Appointments",
        "question_en": "Who was sworn in as the 51st Chief Justice of India (CJI) in November 2024, succeeding Justice D. Y. Chandrachud?",
        "question_te": "నవంబర్ 2024 లో జస్టిస్ డి.వై. చంద్రచూడ్ పదవీ విరమణ అనంతరం భారత 51వ ప్రధాన న్యాయమూర్తిగా (CJI) ప్రమాణ స్వీకారం చేసినది ఎవరు?",
        "options_en": ["Justice Sanjiv Khanna", "Justice B. R. Gavai", "Justice Surya Kant", "Justice Hima Kohli"],
        "options_te": ["జస్టిస్ సంజీవ్ ఖన్నా (Justice Sanjiv Khanna)", "జస్టిస్ బి. ఆర్. గవాయ్", "జస్టిస్ సూర్యకాంత్", "జస్టిస్ హిమా కోహ్లీ"],
        "correct_option": 0,
        "explanation_en": "Justice Sanjiv Khanna took oath as the 51st Chief Justice of India on 11 November 2024 administered by President Droupadi Murmu at Rashtrapati Bhavan.",
        "explanation_te": "భారత 51వ ప్రధాన న్యాయమూర్తిగా జస్టిస్ సంజీవ్ ఖన్నా 2024 నవంబర్ 11న రాష్ట్రపతి ద్రౌపది ముర్ము సమక్షంలో ప్రమాణ స్వీకారం చేశారు."
    },
    {
        "id": 106,
        "section": "General Studies",
        "topic": "Current Affairs - Sports",
        "question_en": "India won the 2024 ICC Men's T20 World Cup in Barbados by defeating which country in the final under Rohit Sharma's captaincy?",
        "question_te": "రోహిత్ శర్మ సారథ్యంలో జూన్ 2024 లో బార్బడోస్‌లో జరిగిన ఫైనల్లో ఏ జట్టును ఓడించి భారతదేశం ఐసీసీ పురుషుల టీ20 ప్రపంచ కప్‌ను కైవసం చేసుకుంది?",
        "options_en": ["South Africa", "Australia", "England", "Pakistan"],
        "options_te": ["దక్షిణాఫ్రికా (South Africa)", "ఆస్ట్రేలియా", "ఇంగ్లాండ్", "పాకిస్తాన్"],
        "correct_option": 0,
        "explanation_en": "India defeated South Africa by 7 runs in the ICC Men's T20 World Cup final at Kensington Oval, Barbados on 29 June 2024 to lift their second T20 World Cup title.",
        "explanation_te": "2024 జూన్ 29న బార్బడోస్‌లో జరిగిన ఉత్కంఠభరిత ఫైనల్‌లో దక్షిణాఫ్రికాను 7 పరుగుల తేడాతో ఓడించి భారత్ రెండోసారి టీ20 ప్రపంచకప్ ఛాంపియన్‌గా నిలిచింది."
    },
    {
        "id": 107,
        "section": "General Studies",
        "topic": "Current Affairs - International Awards",
        "question_en": "The 2024 Nobel Peace Prize was awarded to which grassroots organization of atomic bomb survivors from Hiroshima and Nagasaki for their dedication to achieving a nuclear-free world?",
        "question_te": "అణ్వాయుధ రహిత ప్రపంచం కోసం పోరాడుతున్న హిరోషిమా, నాగసాకి అణుబాంబు బాధితుల ఏ జపనీస్ సంస్థకు 2024 నోబెల్ శాంతి బహుమతి లభించింది?",
        "options_en": ["Nihon Hidankyo", "Memorial", "White Helmets", "Amnesty International"],
        "options_te": ["నిహోన్ హిడాంక్యో (Nihon Hidankyo - జపాన్)", "మెమోరియల్", "వైట్ హెల్మెట్స్", "ఆమ్నెస్టీ ఇంటర్నేషనల్"],
        "correct_option": 0,
        "explanation_en": "The Norwegian Nobel Committee awarded the 2024 Nobel Peace Prize to Japanese organization 'Nihon Hidankyo' (hibakusha survivors) for demonstrating that nuclear weapons must never be used again.",
        "explanation_te": "అణ్వాయుధాలు మానవాళికి ఎంతటి పెనుముప్పో ప్రపంచానికి చాటిచెప్పిన హిరోషిమా, నాగసాకి బాధితుల జపనీస్ సంస్థ 'నిహోన్ హిడాంక్యో' కు 2024 నోబెల్ శాంతి పురస్కారం దక్కింది."
    },
    {
        "id": 108,
        "section": "General Studies",
        "topic": "Current Affairs - Science & Technology",
        "question_en": "The 2024 Nobel Prize in Chemistry was awarded to David Baker, Demis Hassabis, and John M. Jumper for revolutionary breakthroughs in:",
        "question_te": "2024 రసాయన శాస్త్ర నోబెల్ బహుమతిని డేవిడ్ బేకర్, డెమిస్ హస్సాబిస్, జాన్ జంపర్‌లకు ఏ రంగంలో చేసిన సంచలనాత్మక పరిశోధనలకు గాను ప్రదానం చేశారు?",
        "options_en": ["Computational protein design and AI-based protein structure prediction (AlphaFold)", "Discovery of CRISPR-Cas9 genetic scissors", "Development of lithium-ion batteries", "Synthesis of quantum dots"],
        "options_te": ["కంప్యూటేషనల్ ప్రోటీన్ డిజైన్ మరియు ఆర్టిఫిషియల్ ఇంటెలిజెన్స్ (AlphaFold) ఆధారిత ప్రోటీన్ నిర్మాణాల అంచనా", "CRISPR-Cas9 జన్యు కత్తెరల ఆవిష్కరణ", "లిథియం అయాన్ బ్యాటరీల అభివృద్ధి", "క్వాంటమ్ చుక్కల సంశ్లేషణ"],
        "correct_option": 0,
        "explanation_en": "One half was awarded to David Baker for computational protein design, and the other half jointly to Demis Hassabis and John M. Jumper (Google DeepMind) for AlphaFold2 protein structure prediction.",
        "explanation_te": "ప్రోటీన్ల సంక్లిష్ట త్రీ-డైమెన్షనల్ నిర్మాణాలను AI సాంకేతికత (AlphaFold) ద్వారా కచ్చితంగా అంచనా వేసినందుకు డెమిస్ హస్సాబిస్, జాన్ జంపర్ మరియు డేవిడ్ బేకర్‌లకు ఈ అవార్డు లభించింది."
    },
    {
        "id": 109,
        "section": "General Studies",
        "topic": "Current Affairs - Telangana Tech Initiatives",
        "question_en": "At the Global AI Summit 2024 held in Hyderabad, the Government of Telangana announced the establishment of a dedicated 200-acre innovation hub named:",
        "question_te": "హైదరాబాద్‌లో నిర్వహించిన గ్లోబల్ ఏఐ సమ్మిట్ 2024 వేదికగా తెలంగాణ ప్రభుత్వం 200 ఎకరాల్లో అభివృద్ధి చేయనున్న నూతన సాంకేతిక హబ్ పేరు ఏమిటి?",
        "options_en": ["AI City (Telangana Artificial Intelligence City)", "Silicon Valley TG", "Cyber Park Telangana", "Robotics Corridor"],
        "options_te": ["ఏఐ సిటీ (AI City - తెలంగాణ ఆర్టిఫిషియల్ ఇంటెలిజెన్స్ సిటీ)", "సిలికాన్ వ్యాలీ టిజి", "సైబర్ పార్క్ తెలంగాణ", "రోబోటిక్స్ కారిడార్"],
        "correct_option": 0,
        "explanation_en": "During the Global AI Summit in September 2024, Chief Minister A. Revanth Reddy unveiled plans for a 200-acre dedicated 'AI City' near Hyderabad to position Telangana as a global AI capital.",
        "explanation_te": "2024 సెప్టెంబర్‌లో హైదరాబాద్‌లో జరిగిన గ్లోబల్ ఏఐ సదస్సులో తెలంగాణను కృత్రిమ మేధస్సు రంగంలో అగ్రగామిగా నిలిపేందుకు 200 ఎకరాలలో 'ఏఐ సిటీ' ని ఏర్పాటు చేస్తున్నట్లు ప్రకటించారు."
    },
    {
        "id": 110,
        "section": "General Studies",
        "topic": "Current Affairs - International Summits",
        "question_en": "Which country chaired and hosted the 19th G20 Leaders' Summit in November 2024 under the motto 'Building a Just World and a Sustainable Planet'?",
        "question_te": "నవంబర్ 2024 లో 'న్యాయమైన ప్రపంచం మరియు సుస్థిర భూగ్రహ నిర్మాణం' అనే నినాదంతో 19వ జి-20 (G20) శిఖరాగ్ర సదస్సుకు ఆతిథ్యమిచ్చిన దేశం ఏది?",
        "options_en": ["Brazil (Rio de Janeiro)", "South Africa", "Indonesia", "India"],
        "options_te": ["బ్రెజిల్ - రియో డి జనీరో (Brazil)", "దక్షిణాఫ్రికా", "ఇండోనేషియా", "భారతదేశం"],
        "correct_option": 0,
        "explanation_en": "The 19th G20 Summit was hosted in Rio de Janeiro, Brazil under President Luiz Inacio Lula da Silva in November 2024, focusing on social inclusion and fighting hunger.",
        "explanation_te": "నవంబర్ 2024 లో బ్రెజిల్‌లోని రియో డి జనీరో నగరంలో అధ్యక్షుడు లూలా డా సిల్వా అధ్యక్షతన 19వ జి-20 శిఖరాగ్ర సమావేశం ఘనంగా జరిగింది."
    },
    {
        "id": 111,
        "section": "General Studies",
        "topic": "Current Affairs - Climate & Environment",
        "question_en": "The 29th UN Climate Change Conference of the Parties (COP29) was held in November 2024 in which host city?",
        "question_te": "నవంబర్ 2024 లో ఐక్యరాజ్యసమితి 29వ అంతర్జాతీయ వాతావరణ మార్పుల సదస్సు (COP29) ఏ నగరంలో జరిగింది?",
        "options_en": ["Baku, Azerbaijan", "Dubai, UAE", "Sharm El-Sheikh, Egypt", "Glasgow, UK"],
        "options_te": ["బాకు, అజర్‌బైజాన్ (Baku, Azerbaijan)", "దుబాయ్, యుఏఈ", "షార్మ్ ఎల్-షేక్, ఈజిప్ట్", "గ్లాస్గో, బ్రిటన్"],
        "correct_option": 0,
        "explanation_en": "COP29 was held in Baku, Azerbaijan in November 2024, designated as the 'Finance COP' for finalizing the New Collective Quantified Goal (NCQG) on climate finance.",
        "explanation_te": "2024 నవంబర్‌లో అజర్‌బైజాన్ రాజధాని బాకు నగరంలో COP29 వాతావరణ సదస్సు నిర్వహించబడింది. వాతావరణ నిధుల సమీకరణే దీని ప్రధాన ఎజెండా."
    },
    {
        "id": 112,
        "section": "General Studies",
        "topic": "Current Affairs - Sports",
        "question_en": "At the Paris 2024 Paralympic Games, the Indian contingent recorded its highest-ever medal tally in history by winning how many total medals?",
        "question_te": "పారిస్ 2024 పారాలింపిక్ క్రీడలలో భారత అథ్లెట్లు చారిత్రాత్మక రికార్డు సృష్టిస్తూ గెలుచుకున్న మొత్తం పతకాల సంఖ్య ఎంత?",
        "options_en": ["29 medals (7 Gold, 9 Silver, 13 Bronze)", "19 medals (5 Gold, 8 Silver, 6 Bronze)", "24 medals (6 Gold, 8 Silver, 10 Bronze)", "35 medals (10 Gold, 12 Silver, 13 Bronze)"],
        "options_te": ["29 పతకాలు (7 స్వర్ణాలు, 9 రజతాలు, 13 కాంస్యాలు)", "19 పతకాలు", "24 పతకాలు", "35 పతకాలు"],
        "correct_option": 0,
        "explanation_en": "India achieved its best-ever Paralympic performance at Paris 2024 with 29 medals (7 Gold, 9 Silver, 13 Bronze), finishing 18th in the overall medals table.",
        "explanation_te": "పారిస్ 2024 పారాలింపిక్స్‌లో భారతదేశం 7 బంగారు పతకాలతో కలిపి మొత్తం 29 పతకాలు సాధించి చరిత్ర సృష్టించింది."
    },
    {
        "id": 113,
        "section": "General Studies",
        "topic": "Current Affairs - Infrastructure & Transport",
        "question_en": "India's first-ever 'Namo Bharat Rapid Rail' (Vande Metro) intercity train service was inaugurated in September 2024 connecting which two cities?",
        "question_te": "సెప్టెంబర్ 2024 లో భారతదేశపు మొట్టమొదటి 'నమో భారత్ రాపిడ్ రైలు' (వందే మెట్రో) ఏ రెండు నగరాల మధ్య ప్రారంభించబడింది?",
        "options_en": ["Ahmedabad and Bhuj (Gujarat)", "Delhi and Meerut (NCR)", "Secunderabad and Warangal", "Mumbai and Pune"],
        "options_te": ["అహ్మదాబాద్ మరియు భుజ్ (గుజరాత్)", "ఢిల్లీ మరియు మీరట్", "సికింద్రాబాద్ మరియు వరంగల్", "ముంబై మరియు పూణే"],
        "correct_option": 0,
        "explanation_en": "Prime Minister Narendra Modi flagged off India's first Namo Bharat Rapid Rail (formerly Vande Metro) between Ahmedabad and Bhuj in Gujarat on 16 September 2024.",
        "explanation_te": "భారతదేశపు మొట్టమొదటి నమో భారత్ రాపిడ్ రైలు (వందే మెట్రో) 2024 సెప్టెంబర్ 16న గుజరాత్‌లోని అహ్మదాబాద్ నుండి భుజ్ మధ్య ప్రారంభమైంది."
    },
    {
        "id": 114,
        "section": "General Studies",
        "topic": "Current Affairs - Telangana Welfare Schemes",
        "question_en": "Under the 'Gruha Jyothi' guarantee scheme implemented across Telangana in 2024, how much free domestic electricity is provided to eligible households?",
        "question_te": "తెలంగాణ ప్రభుత్వం 2024 లో ప్రవేశపెట్టిన 'గృహజ్యోతి' గ్యారెంటీ పథకం క్రింద అర్హులైన పేద కుటుంబాలకు గృహ వినియోగానికి ఎన్ని యూనిట్ల వరకు ఉచిత విద్యుత్ లభిస్తుంది?",
        "options_en": ["Up to 200 units per month", "Up to 100 units per month", "Up to 300 units per month", "Up to 150 units per month"],
        "options_te": ["నెలకు 200 యూనిట్ల వరకు (Up to 200 units/month)", "నెలకు 100 యూనిట్లు", "నెలకు 300 యూనిట్లు", "నెలకు 150 యూనిట్లు"],
        "correct_option": 0,
        "explanation_en": "The Gruha Jyothi scheme provides up to 200 units of free power per month to all domestic consumers holding white ration cards across Telangana.",
        "explanation_te": "ఆరు గ్యారెంటీలలో ఒకటైన గృహజ్యోతి పథకం ద్వారా అర్హులైన నివాస గృహాలకు నెలకు 200 యూనిట్ల వరకు ఉచిత కరెంట్‌ను ప్రభుత్వం అందిస్తోంది."
    },
    {
        "id": 115,
        "section": "General Studies",
        "topic": "Current Affairs - Telangana Urban Rejuvenation",
        "question_en": "What is the primary objective of the comprehensive 'Musi Riverfront Development Project' (MRDP) undertaken by the Government of Telangana?",
        "question_te": "తెలంగాణ ప్రభుత్వం చేపట్టిన 'మూసీ రివర్‌ఫ్రంట్ డెవలప్‌మెంట్ ప్రాజెక్ట్' (MRDP) యొక్క ముఖ్య ఉద్దేశం ఏమిటి?",
        "options_en": ["Comprehensive ecological cleaning, flood mitigation, rejuvenation and economic riverfront zone along a 55 km stretch", "Construction of a mega industrial chemical manufacturing corridor", "Complete diversion of Musi water to other states", "Establishing a coal-fired thermal power generation station"],
        "options_te": ["55 కిలోమీటర్ల మేర మూసీ నదిని శుభ్రపరిచి, మురుగు తొలగించి, పర్యావరణహిత పర్యాటక మరియు ఆర్థిక రివర్‌ఫ్రంట్‌గా తీర్చిదిద్దడం", "రసాయన పారిశ్రామిక వాడను నిర్మించడం", "మూసీ నది నీటిని ఇతర రాష్ట్రాలకు తరలించడం", "బొగ్గు ఆధారిత థర్మల్ విద్యుత్ కేంద్రాన్ని ఏర్పాటు చేయడం"],
        "correct_option": 0,
        "explanation_en": "The Musi Riverfront Development Project aims to revitalize the Musi river over a 55 km stretch across Hyderabad with sewerage treatment plants, check dams, recreational promenades, and economic hubs.",
        "explanation_te": "హైదరాబాద్ నగరంలోని మూసీ నది కాలుష్యాన్ని నివారించి, పర్యావరణ పరిరక్షణతో పాటు లండన్ థేమ్స్ నది తరహాలో పర్యాటక, ఆర్థిక రివర్‌ఫ్రంట్‌గా అభివృద్ధి చేయడం దీని లక్ష్యం."
    },

    # =========================================================================
    # 2. GENERAL SCIENCE & ENVIRONMENT / TECH (Q116 - Q130)
    # =========================================================================
    {
        "id": 116,
        "section": "General Studies",
        "topic": "General Science - Physics",
        "question_en": "Optical fibres used in modern high-speed telecommunication transmit light signals based on the principle of:",
        "question_te": "ఆధునిక టెలికమ్యూనికేషన్స్‌లో సమాచార ప్రసారానికి ఉపయోగించే ఆప్టికల్ ఫైబర్లు ఏ సూత్రం ఆధారంగా పనిచేస్తాయి?",
        "options_en": ["Total Internal Reflection", "Diffraction of light", "Polarisation of light", "Photoelectric effect"],
        "options_te": ["సంపూర్ణాంతర పరావర్తనం (Total Internal Reflection)", "కాంతి వివర్తనం", "కాంతి ధ్రువణం", "కాంతి విద్యుత్ ఫలితం"],
        "correct_option": 0,
        "explanation_en": "Optical fibres work on the phenomenon of Total Internal Reflection (TIR), where light travelling from a denser to a rarer medium is reflected back into the core when incident at an angle greater than the critical angle.",
        "explanation_te": "కాంతి సాంద్రతర యానకం నుండి విరళ యానకంలోకి ప్రయాణించేటప్పుడు పతన కోణం సందిగ్ధ కోణం కంటే ఎక్కువైనప్పుడు 'సంపూర్ణాంతర పరావర్తనం' చెంది ప్రసారమవుతుంది."
    },
    {
        "id": 117,
        "section": "General Studies",
        "topic": "General Science - Physics (Sound)",
        "question_en": "What is the audible frequency range of sound for a healthy human ear?",
        "question_te": "ఆరోగ్యవంతమైన మానవ చెవి వినగలిగే ధ్వని పౌనఃపున్య పరిధి (శ్రవ్య పరిధి) ఎంత?",
        "options_en": ["20 Hz to 20,000 Hz", "Below 20 Hz only", "20,000 Hz to 50,000 Hz", "5 Hz to 500 Hz"],
        "options_te": ["20 Hz నుండి 20,000 Hz వరకు", "20 Hz కంటే తక్కువ మాత్రమే", "20,000 Hz నుండి 50,000 Hz వరకు", "5 Hz నుండి 500 Hz వరకు"],
        "correct_option": 0,
        "explanation_en": "The audible sound frequency range for humans is approximately 20 Hz to 20 kHz (20,000 Hz). Frequencies below 20 Hz are infrasonic, and above 20 kHz are ultrasonic.",
        "explanation_te": "మానవ శ్రవ్య అవధి 20 హెర్ట్జ్ (Hz) నుండి 20,000 హెర్ట్జ్ (Hz). 20 Hz కంటే తక్కువ ఉన్నవి పరశ్రవ్యాలు, 20,000 Hz కంటే ఎక్కువ ఉన్నవి అతిధ్వనులు."
    },
    {
        "id": 118,
        "section": "General Studies",
        "topic": "General Science - Chemistry (pH Scale)",
        "question_en": "What is the approximate normal pH value of human blood?",
        "question_te": "మానవ రక్తం యొక్క సాధారణ పి.హెచ్ (pH) విలువ సుమారుగా ఎంత ఉంటుంది?",
        "options_en": ["7.35 - 7.45", "6.0 - 6.5", "8.5 - 9.0", "5.0 - 5.5"],
        "options_te": ["7.35 - 7.45", "6.0 - 6.5", "8.5 - 9.0", "5.0 - 5.5"],
        "correct_option": 0,
        "explanation_en": "Normal arterial blood pH is tightly regulated between 7.35 and 7.45, making it slightly alkaline (basic).",
        "explanation_te": "మానవ రక్తం కొద్దిగా క్షార గుణాన్ని కలిగి ఉంటుంది. దీని సాధారణ pH విలువ 7.35 నుండి 7.45 మధ్య ఉంటుంది."
    },
    {
        "id": 119,
        "section": "General Studies",
        "topic": "General Science - Chemistry (Everyday Chemicals)",
        "question_en": "What is the chemical name and formula of 'Plaster of Paris'?",
        "question_te": "'ప్లాస్టర్ ఆఫ్ పారిస్' (Plaster of Paris) యొక్క రసాయన నామం మరియు ఫార్ములా ఏది?",
        "options_en": ["Calcium sulphate hemihydrate (CaSO4 . 1/2 H2O)", "Calcium sulphate dihydrate (CaSO4 . 2H2O)", "Calcium carbonate (CaCO3)", "Calcium oxychloride (CaOCl2)"],
        "options_te": ["కాల్షియం సల్ఫేట్ హెమీహైడ్రేట్ (CaSO4 . 1/2 H2O)", "కాల్షియం సల్ఫేట్ డైహైడ్రేట్ (CaSO4 . 2H2O)", "కాల్షియం కార్బోనేట్ (CaCO3)", "బ్లీచింగ్ పౌడర్ (CaOCl2)"],
        "correct_option": 0,
        "explanation_en": "Plaster of Paris is calcium sulphate hemihydrate, CaSO4 . 0.5 H2O, obtained by heating gypsum (CaSO4 . 2H2O) to 373 K.",
        "explanation_te": "జిప్సమ్‌ను 373 K వద్ద వేడి చేసినప్పుడు నీటి అణువులను కోల్పోయి ప్లాస్టర్ ఆఫ్ పారిస్ (CaSO4 . 1/2 H2O) ఏర్పడుతుంది."
    },
    {
        "id": 120,
        "section": "General Studies",
        "topic": "General Science - Biology (Vitamins)",
        "question_en": "Deficiency of Vitamin D in growing children leads to which of the following skeletal diseases?",
        "question_te": "పెరుగుతున్న పిల్లలలో విటమిన్ డి (Vitamin D) లోపం వల్ల వచ్చే ఎముకల వ్యాధి ఏది?",
        "options_en": ["Rickets", "Scurvy", "Beri-beri", "Pellagra"],
        "options_te": ["రికెట్స్ (Rickets)", "స్కర్వీ (Scurvy)", "బెరి-బెరి (Beri-beri)", "పెల్లాగ్రా (Pellagra)"],
        "correct_option": 0,
        "explanation_en": "Vitamin D deficiency impairs calcium absorption, leading to soft, weak bones known as Rickets in children and Osteomalacia in adults.",
        "explanation_te": "విటమిన్ డి లోపం వల్ల ఎముకలు మెత్తబడి వంకర్లు తిరిగే 'రికెట్స్' వ్యాధి పిల్లల్లో వస్తుంది. పెద్దలలో ఇది ఆస్టియోమలేసియాకు దారితీస్తుంది."
    },
    {
        "id": 121,
        "section": "General Studies",
        "topic": "General Science - Biology (Blood)",
        "question_en": "Which human blood group is known as the 'Universal Donor' because its red blood cells lack both A and B antigens?",
        "question_te": "ఎర్ర రక్త కణాలపై A మరియు B యాంటిజెన్లు రెండూ లేకపోవడం వల్ల ఏ రక్త వర్గాన్ని 'విశ్వ దాత' (Universal Donor) అని పిలుస్తారు?",
        "options_en": ["O negative (O-)", "AB positive (AB+)", "A positive (A+)", "B negative (B-)"],
        "options_te": ["ఓ నెగెటివ్ (O-)", "ఎబి పాజిటివ్ (AB+)", "ఎ పాజిటివ్ (A+)", "బి నెగెటివ్ (B-)"],
        "correct_option": 0,
        "explanation_en": "Blood group O negative (O-) has neither A, B antigens nor Rh factor on RBCs, making it safe for transfusion to any ABO/Rh recipient.",
        "explanation_te": "O- రక్త వర్గం ఎటువంటి A, B యాంటిజెన్లు మరియు Rh కారకం కలిగి ఉండదు కాబట్టి దీనిని ఏ వర్గం వారికైనా సురక్షితంగా ఎక్కించవచ్చు. అందుకే 'విశ్వదాత' అంటారు."
    },
    {
        "id": 122,
        "section": "General Studies",
        "topic": "General Science - Biology (Endocrine System)",
        "question_en": "Which hormone produced by the beta cells of the Islets of Langerhans in the pancreas regulates glucose levels in the blood?",
        "question_te": "క్లోమ గ్రంథి (Pancreas) లోని లాంగర్‌హాన్ కణాల బీటా కణాలు స్రవించే ఏ హార్మోన్ రక్తంలో గ్లూకోజ్ స్థాయిలను నియంత్రిస్తుంది?",
        "options_en": ["Insulin", "Thyroxine", "Adrenaline", "Glucagon"],
        "options_te": ["ఇన్సులిన్ (Insulin)", "థైరాక్సిన్ (Thyroxine)", "అడ్రినలిన్ (Adrenaline)", "గ్లూకగాన్ (Glucagon)"],
        "correct_option": 0,
        "explanation_en": "Insulin is secreted by beta cells of the pancreas; it facilitates the uptake of glucose into cells, lowering blood glucose levels. Its insufficiency causes Diabetes Mellitus.",
        "explanation_te": "క్లోమ గ్రంథిలోని బీటా కణాలు ఇన్సులిన్‌ను ఉత్పత్తి చేస్తాయి. ఇది రక్తంలోని గ్లూకోజ్ శాతాన్ని తగ్గిస్తుంది. దీని లోపం వల్ల మధుమేహం (డయాబెటిస్) వస్తుంది."
    },
    {
        "id": 123,
        "section": "General Studies",
        "topic": "General Science - Diseases & Pathogens",
        "question_en": "Malaria is caused by which microscopic organism and transmitted through the bite of which vector?",
        "question_te": "మలేరియా వ్యాధి ఏ సూక్ష్మజీవి వల్ల వస్తుంది మరియు ఏ దోమ కాటు ద్వారా మానవులకు వ్యాపిస్తుంది?",
        "options_en": ["Plasmodium protozoan, female Anopheles mosquito", "Aedes aegypti mosquito, Dengue virus", "Culex mosquito, Wuchereria bancrofti", "Salmonella bacteria, housefly"],
        "options_te": ["ప్లాస్మోడియం ప్రోటోజోవా, ఆడ అనాఫిలిస్ దోమ", "ఏడిస్ ఈజిప్టి దోమ, డెంగ్యూ వైరస్", "క్యూలెక్స్ దోమ, ఫైలేరియా", "సాల్మొనెల్లా బ్యాక్టీరియా, ఈగ"],
        "correct_option": 0,
        "explanation_en": "Malaria is caused by the protozoan parasite Plasmodium (such as P. falciparum, P. vivax) and is transmitted to humans by the bite of infected female Anopheles mosquitoes.",
        "explanation_te": "మలేరియా ప్లాస్మోడియం అనే ఏకకణ ప్రోటోజోవా పరాన్నజీవి వల్ల వస్తుంది. ఇది ఆడ అనాఫిలిస్ దోమ కాటు ద్వారా వ్యాపిస్తుంది."
    },
    {
        "id": 124,
        "section": "General Studies",
        "topic": "General Science - Physics (Optics)",
        "question_en": "The phenomenon of dispersion of light into its constituent seven colours in a glass prism occurs because:",
        "question_te": "గాజు పట్టకం ద్వారా తెల్లని కాంతి ప్రయాణించినప్పుడు ఏడు రంగులుగా విడిపోవడానికి (కాంతి విక్షేపణం) గల కారణం ఏమిటి?",
        "options_en": ["Different colours of light travel at different speeds and refract by different angles in glass", "Total internal reflection inside the prism", "Light colours have the same wavelength in glass", "Diffraction along the sharp edges of the prism"],
        "options_te": ["వివిధ రంగుల కాంతి వేర్వేరు తరంగదైర్ఘ్యాలు కలిగి ఉండి, గాజులో వేర్వేరు వక్రీభవన గుణకాలతో వేర్వేరు కోణాల్లో వంగుతాయి", "పట్టకం లోపల సంపూర్ణాంతర పరావర్తనం", "గాజులో అన్ని రంగుల తరంగదైర్ఘ్యం ఒకేలా ఉండటం", "పట్టకం అంచుల వద్ద కాంతి వివర్తనం"],
        "correct_option": 0,
        "explanation_en": "Different wavelengths of light travel with different velocities in a medium. Red refracts the least (longest wavelength) and violet refracts the most (shortest wavelength), producing a spectrum.",
        "explanation_te": "గాజులో వివిధ రంగుల వేగాలు వేర్వేరుగా ఉంటాయి. ఎరుపు రంగు తక్కువగా, ఊదా రంగు ఎక్కువగా వంగుతాయి. దీనివల్ల వర్ణపటం ఏర్పడుతుంది."
    },
    {
        "id": 125,
        "section": "General Studies",
        "topic": "Environment & Ecology - Tiger Reserves",
        "question_en": "Which is the largest Tiger Reserve in Telangana, spanning across the Nallamala forest hills?",
        "question_te": "నల్లమల అటవీ కొండలలో విస్తరించి ఉన్న తెలంగాణలోని అతిపెద్ద పులుల అభయారణ్యం (Tiger Reserve) ఏది?",
        "options_en": ["Amrabad Tiger Reserve", "Kawal Tiger Reserve", "Pakhal Wildlife Sanctuary", "Kinnerasani Wildlife Sanctuary"],
        "options_te": ["అమ్రాబాద్ టైగర్ రిజర్వ్ (Amrabad)", "కవ్వాల్ టైగర్ రిజర్వ్ (Kawal)", "పాఖాల వన్యప్రాణి సంరక్షణ కేంద్రం", "కిన్నెరసాని వన్యప్రాణి కేంద్రం"],
        "correct_option": 0,
        "explanation_en": "Amrabad Tiger Reserve in Nagarkurnool and Nalgonda districts covers part of the Nallamala forest and is the largest tiger reserve in Telangana (second largest in India).",
        "explanation_te": "నాగర్‌కర్నూల్ మరియు నల్గొండ జిల్లాల్లోని నల్లమల అటవీ ప్రాంతంలో విస్తరించి ఉన్న అమ్రాబాద్ టైగర్ రిజర్వ్ తెలంగాణలో అతిపెద్ద పులుల సంరక్షణ కేంద్రం."
    },
    {
        "id": 126,
        "section": "General Studies",
        "topic": "Environment & Ecology - Greenhouse Gases",
        "question_en": "Which of the following is the most potent greenhouse gas in terms of Global Warming Potential (GWP) over a 20-year timescale, though shorter-lived than CO2?",
        "question_te": "వాతావరణంలో తక్కువ కాలం ఉన్నప్పటికీ, కార్బన్ డయాక్సైడ్ (CO2) కంటే 20 ఏళ్ల కాలంలో అనేక రెట్లు అధిక గ్లోబల్ వార్మింగ్ సామర్థ్యం గల గ్రీన్‌హౌస్ వాయువు ఏది?",
        "options_en": ["Methane (CH4)", "Nitrogen (N2)", "Argon (Ar)", "Oxygen (O2)"],
        "options_te": ["మీథేన్ (CH4)", "నైట్రోజన్ (N2)", "ఆర్గాన్ (Ar)", "ఆక్సిజన్ (O2)"],
        "correct_option": 0,
        "explanation_en": "Methane (CH4) has a Global Warming Potential over 80 times greater than carbon dioxide on a 20-year horizon, making it a critical focus for rapid climate action.",
        "explanation_te": "మీథేన్ వాయువు కార్బన్ డయాక్సైడ్ కంటే సుమారు 80 రెట్లు అధిక వేడిని పట్టి ఉంచగల శక్తిని (GWP) కలిగి ఉన్న బలమైన గ్రీన్‌హౌస్ వాయువు."
    },
    {
        "id": 127,
        "section": "General Studies",
        "topic": "General Science - Chemistry (Metals)",
        "question_en": "Which metal remains in liquid state at normal room temperature (25 degrees C)?",
        "question_te": "గది ఉష్ణోగ్రత (25 డిగ్రీల సెంటీగ్రేడ్) వద్ద ద్రవ రూపంలో ఉండే ఏకైక లోహం ఏది?",
        "options_en": ["Mercury (Hg)", "Bromine (Br)", "Sodium (Na)", "Lead (Pb)"],
        "options_te": ["పాదరసం (Mercury - Hg)", "బ్రోమిన్ (Bromine - అలోహం)", "సోడియం (Sodium)", "సీసం (Lead)"],
        "correct_option": 0,
        "explanation_en": "Mercury (Hg) is the only metal that is liquid at standard room temperature. Bromine is also liquid, but it is a non-metal.",
        "explanation_te": "గది ఉష్ణోగ్రత వద్ద ద్రవ రూపంలో ఉండే ఏకైక లోహం పాదరసం (Hg). బ్రోమిన్ కూడా ద్రవ రూపంలో ఉంటుంది కానీ అది అలోహం."
    },
    {
        "id": 128,
        "section": "General Studies",
        "topic": "General Science - Physics (Units)",
        "question_en": "Light year is a unit used to measure which physical quantity?",
        "question_te": "'కాంతి సంవత్సరం' (Light Year) అనేది దేనిని కొలవడానికి ఉపయోగించే ప్రామాణిక ప్రమాణం?",
        "options_en": ["Astronomical distance", "Time duration", "Speed of light", "Intensity of sunlight"],
        "options_te": ["ఖగోళ దూరం (Astronomical Distance)", "కాల వ్యవధి", "కాంతి వేగం", "సూర్యరశ్మి తీవ్రత"],
        "correct_option": 0,
        "explanation_en": "A light-year is the astronomical distance that light travels in vacuum in one Julian year (approx. 9.46 * 10^12 km).",
        "explanation_te": "కాంతి ఒక సంవత్సర కాలంలో శూన్యంలో ప్రయాణించే మొత్తం దూరాన్ని 'కాంతి సంవత్సరం' అంటారు. ఇది ఖగోళ దూరాలను కొలవడానికి ప్రమాణం."
    },
    {
        "id": 129,
        "section": "General Studies",
        "topic": "Environment & Ecology - Protected Areas",
        "question_en": "Pakhal Wildlife Sanctuary and Pakhal Lake, originally constructed by the Kakatiyas, are located in which district of Telangana?",
        "question_te": "కాకతీయుల కాలంలో నిర్మించబడిన పాఖాల సరస్సు మరియు పాఖాల వన్యప్రాణి సంరక్షణ కేంద్రం తెలంగాణలోని ఏ జిల్లాలో ఉన్నాయి?",
        "options_en": ["Warangal", "Nizamabad", "Khammam", "Mahabubnagar"],
        "options_te": ["వరంగల్ (Warangal)", "నిజామాబాద్", "ఖమ్మం", "మహబూబ్‌నగర్"],
        "correct_option": 0,
        "explanation_en": "Pakhal Wildlife Sanctuary is situated around the man-made Pakhal Lake (built in 1213 CE by Kakatiya ruler Ganapati Deva) in Warangal district.",
        "explanation_te": "కాకతీయ గణపతిదేవుని కాలంలో నిర్మితమైన పాఖాల సరస్సు మరియు పరిసర అభయారణ్యం వరంగల్ జిల్లాలో విస్తరించి ఉన్నాయి."
    },
    {
        "id": 130,
        "section": "General Studies",
        "topic": "General Science - Physics (Radioactivity)",
        "question_en": "Which radioactive isotope is widely used in medicine for the treatment of thyroid disorders and thyroid cancer?",
        "question_te": "థైరాయిడ్ గ్రంథి సమస్యలు మరియు క్యాన్సర్ చికిత్సలో వైద్యరంగంలో విస్తృతంగా ఉపయోగించే రేడియోధార్మిక ఐసోటోప్ ఏది?",
        "options_en": ["Iodine-131", "Cobalt-60", "Carbon-14", "Uranium-238"],
        "options_te": ["అయోడిన్-131 (Iodine-131)", "కోబాల్ట్-60", "కార్బన్-14", "యురేనియం-238"],
        "correct_option": 0,
        "explanation_en": "Radioactive Iodine-131 (I-131) is taken up selectively by thyroid tissue and is used to destroy overactive thyroid tissue or thyroid cancer cells.",
        "explanation_te": "థైరాయిడ్ గ్రంథి వ్యాధులు మరియు క్యాన్సర్ చికిత్సలో రేడియోధార్మిక 'అయోడిన్-131' ను ఉపయోగిస్తారు."
    },

    # =========================================================================
    # 3. HISTORY OF INDIA & INDIAN NATIONAL MOVEMENT (Q131 - Q145)
    # =========================================================================
    {
        "id": 131,
        "section": "General Studies",
        "topic": "Ancient Indian History - Indus Valley",
        "question_en": "At which Indus Valley Civilization site was a massive artificial brick dockyard discovered, providing evidence of maritime trade?",
        "question_te": "సింధు నాగరికత కాలంలో సముద్ర వ్యాపారానికి నిదర్శనంగా ఇటుకలతో నిర్మించిన భారీ రేవు (డార్క్‌యార్డ్) ఏ ప్రదేశంలో బయల్పడింది?",
        "options_en": ["Lothal", "Harappa", "Kalibangan", "Mohenjo-daro"],
        "options_te": ["లోథాల్ (Lothal)", "హరప్పా (Harappa)", "కాలిబంగన్ (Kalibangan)", "మొహంజొదారో (Mohenjo-daro)"],
        "correct_option": 0,
        "explanation_en": "Lothal in Gujarat had a tidal dockyard connected to the Bhogavo river, serving as a major maritime trade port during the Indus Valley Civilization.",
        "explanation_te": "గుజరాత్‌లోని లోథాల్ వద్ద సింధు నాగరికత కాలం నాటి ప్రపంచంలోనే మొట్టమొదటి టైడల్ డాక్‌యార్డ్ (ఓడరేవు) బయల్పడింది."
    },
    {
        "id": 132,
        "section": "General Studies",
        "topic": "Ancient Indian History - Mauryan Empire",
        "question_en": "The Kalinga War, which led Emperor Ashoka to embrace Buddhism and preach Dhamma, took place in which year BCE?",
        "question_te": "అశోక చక్రవర్తి బౌద్ధమతాన్ని స్వీకరించి యుద్ధాలకు స్వస్తి పలకడానికి కారణమైన చారిత్రాత్మక 'కళింగ యుద్ధం' ఏ సంవత్సరంలో (BCE) జరిగింది?",
        "options_en": ["261 BCE", "326 BCE", "232 BCE", "185 BCE"],
        "options_te": ["క్రీ.పూ. 261 (261 BCE)", "క్రీ.పూ. 326", "క్రీ.పూ. 232", "క్రీ.పూ. 185"],
        "correct_option": 0,
        "explanation_en": "Ashoka fought the Kalinga War in 261 BCE (the 8th year of his coronation), as recorded in his Major Rock Edict XIII.",
        "explanation_te": "అశోకుని 13వ శిలాశాసనం ప్రకారం, అతను పట్టాభిషేకం జరిగిన 8వ సంవత్సరంలో అనగా క్రీ.పూ. 261 లో కళింగ యుద్ధం చేశాడు."
    },
    {
        "id": 133,
        "section": "General Studies",
        "topic": "Ancient Indian History - Gupta Empire",
        "question_en": "The famous iron pillar which has stood for centuries without rusting is located at Mehrauli, Delhi, and bears an inscription honoring which Gupta ruler?",
        "question_te": "ఢిల్లీలోని మెహ్రౌలీ వద్ద శతాబ్దాలుగా తుప్పు పట్టకుండా ఉన్న ప్రసిద్ధ ఇనుప స్తంభం ఏ గుప్త పాలకుని ఘనతను తెలుపుతుంది?",
        "options_en": ["Chandragupta II (Vikramaditya)", "Samudragupta", "Kumaragupta I", "Skandagupta"],
        "options_te": ["రెండవ చంద్రగుప్తుడు (విక్రమాదిత్యుడు)", "సముద్రగుప్తుడు", "మొదటి కుమారగుప్తుడు", "స్కందగుప్తుడు"],
        "correct_option": 0,
        "explanation_en": "The Mehrauli Iron Pillar in Delhi contains an inscription mentioning King 'Chandra', identified by historians as Chandragupta II Vikramaditya.",
        "explanation_te": "మెహ్రౌలీ ఇనుప స్తంభంపై 'చంద్ర' అనే రాజు విజయాల ప్రశస్తి ఉంది. ఆ రాజు రెండవ చంద్రగుప్తుడు (విక్రమాదిత్యుడు) అని చరిత్రకారులు నిర్ధారించారు."
    },
    {
        "id": 134,
        "section": "General Studies",
        "topic": "Medieval Indian History - Delhi Sultanate",
        "question_en": "Which Sultan of the Delhi Sultanate introduced the market control regulations, fixed prices for commodities, and established the price control department (Diwan-i-Riyasat)?",
        "question_te": "ఢిల్లీ సుల్తానేట్ పాలనలో వస్తువుల ధరలను నియంత్రించి, మార్కెట్ సంస్కరణలను అమలు చేస్తూ 'దివాన్-ఇ-రియాసత్' విభాగాన్ని ఏర్పాటు చేసిన సుల్తాన్ ఎవరు?",
        "options_en": ["Alauddin Khilji", "Muhammad bin Tughlaq", "Balban", "Firoz Shah Tughlaq"],
        "options_te": ["అల్లావుద్దీన్ ఖిల్జీ (Alauddin Khilji)", "మహ్మద్ బిన్ తుగ్లక్", "బాల్బన్", "ఫిరోజ్ షా తుగ్లక్"],
        "correct_option": 0,
        "explanation_en": "Alauddin Khilji introduced strict market control reforms to maintain a large standing army at low cost, fixing prices of essential goods.",
        "explanation_te": "భారీ సైన్యాన్ని తక్కువ ఖర్చుతో నిర్వహించడానికి నిత్యావసర వస్తువుల ధరలను కట్టడి చేస్తూ మార్కెట్ సంస్కరణలు తెచ్చిన సుల్తాన్ అల్లావుద్దీన్ ఖిల్జీ."
    },
    {
        "id": 135,
        "section": "General Studies",
        "topic": "Medieval Indian History - Vijayanagara Empire",
        "question_en": "The great Vijayanagara emperor Sri Krishnadevaraya authored which celebrated Telugu political-administrative epic?",
        "question_te": "విజయనగర సామ్రాజ్య చక్రవర్తి శ్రీకృష్ణదేవరాయలు రాజనీతి మరియు పరిపాలనా విశేషాలను వివరిస్తూ రచించిన ప్రసిద్ధ తెలుగు ప్రబంధం ఏది?",
        "options_en": ["Amuktamalyada", "Manu Charitra", "Parijatapaharanam", "Kavyalankara Sangrahamu"],
        "options_te": ["ఆముక్తమాల్యద (Amuktamalyada)", "మనుచరిత్ర", "పారిజాతాపహరణం", "కావ్యాలంకార సంగ్రహము"],
        "correct_option": 0,
        "explanation_en": "Sri Krishnadevaraya authored 'Amuktamalyada' in Telugu, which narrates the story of Andal (Goda Devi) and includes his famous thoughts on statecraft.",
        "explanation_te": "గోదాదేవి కథతో పాటు పరిపాలన మరియు రాజనీతి సూత్రాలను వివరిస్తూ శ్రీకృష్ణదేవరాయలు రచించిన కావ్యం 'ఆముక్తమాల్యద'."
    },
    {
        "id": 136,
        "section": "General Studies",
        "topic": "Medieval Indian History - Mughal Empire",
        "question_en": "Akbar promulgated a syncretic religious ideology in 1582 CE aiming for universal peace and harmony. What was it called?",
        "question_te": "1582 లో అక్బర్ చక్రవర్తి సర్వమత సామరస్యం కోసం ప్రతిపాదించిన సమన్వయ మత సిద్ధాంతం పేరు ఏమిటి?",
        "options_en": ["Din-i-Ilahi", "Sulh-i-Kul", "Ibadat Khana", "Jizya"],
        "options_te": ["దీన్-ఇ-ఇలాహీ (Din-i-Ilahi)", "సుల్హ్-ఇ-కుల్", "ఇబాదత్ ఖానా", "జిజియా"],
        "correct_option": 0,
        "explanation_en": "Akbar established 'Din-i-Ilahi' (Religion of God) in 1582 CE, drawing ethical elements from Islam, Hinduism, Jainism, and Zoroastrianism.",
        "explanation_te": "అన్ని మతాలలోని ఉన్నత విలువలను మేళవించి 1582 లో అక్బర్ ప్రారంభించిన నూతన జీవన మార్గం 'దీన్-ఇ-ఇలాహీ'."
    },
    {
        "id": 137,
        "section": "General Studies",
        "topic": "Modern Indian History - 1857 Revolt",
        "question_en": "Who led the 1857 armed revolt against the British East India Company in the Rohilkhand region (Bareilly)?",
        "question_te": "1857 ప్రథమ స్వాతంత్ర్య సంగ్రామంలో బరేలీ (రోహిల్‌ఖండ్) ప్రాంతంలో తిరుగుబాటుకు నాయకత్వం వహించినది ఎవరు?",
        "options_en": ["Khan Bahadur Khan", "Kunwar Singh", "Maulvi Ahmadullah", "Bakht Khan"],
        "options_te": ["ఖాన్ బహదూర్ ఖాన్ (Khan Bahadur Khan)", "కున్వర్ సింగ్ (బీహార్)", "మౌల్వీ అహ్మదుల్లా", "భక్త్ ఖాన్"],
        "correct_option": 0,
        "explanation_en": "In Bareilly (Rohilkhand), the 1857 revolt was led by Khan Bahadur Khan, a descendant of the former ruler of Rohilkhand.",
        "explanation_te": "1857 తిరుగుబాటులో బరేలీ ప్రాంతానికి ఖాన్ బహదూర్ ఖాన్ నాయకత్వం వహించి బ్రిటిష్ వారిపై పోరాడారు."
    },
    {
        "id": 138,
        "section": "General Studies",
        "topic": "Modern Indian History - Socio-Religious Reform",
        "question_en": "Who founded the 'Satyashodhak Samaj' in Maharashtra in 1873 to fight against caste discrimination and advocate for the education of women and lower castes?",
        "question_te": "కులవివక్షకు వ్యతిరేకంగా, మహిళలు మరియు అణగారిన వర్గాల విద్యావ్యాప్తి కోసం 1873 లో మహారాష్ట్రలో 'సత్యశోధక్ సమాజ్' ను స్థాపించిన సంఘ సంస్కర్త ఎవరు?",
        "options_en": ["Jyotirao Phule", "Dr. B. R. Ambedkar", "Gopal Ganesh Agarkar", "Atmaram Pandurang"],
        "options_te": ["జ్యోతిరావ్ ఫూలే (Jyotirao Phule)", "డా. బి. ఆర్. అంబేద్కర్", "గోపాల్ గణేష్ అగార్కర్", "ఆత్మారామ్ పాండురంగ్"],
        "correct_option": 0,
        "explanation_en": "Mahatma Jyotirao Phule founded the Satyashodhak Samaj on 24 September 1873 to liberate the Shudra and Ati-Shudra communities from social exploitation.",
        "explanation_te": "బడుగు, బలహీన వర్గాల హక్కులు మరియు స్త్రీ విద్య కోసం మహాత్మా జ్యోతిరావ్ ఫూలే 1873 లో 'సత్యశోధక్ సమాజ్' ను స్థాపించారు."
    },
    {
        "id": 139,
        "section": "General Studies",
        "topic": "Indian National Movement - Swadeshi",
        "question_en": "The Partition of Bengal announced by Lord Curzon in 1905 directly sparked which nationwide political agitation?",
        "question_te": "1905 లో లార్డ్ కర్జన్ ప్రకటించిన బెంగాల్ విభజనకు వ్యతిరేకంగా దేశవ్యాప్తంగా ఉవ్వెత్తున ఎగసిపడిన ఉద్యమం ఏది?",
        "options_en": ["Swadeshi and Vandemataram Movement", "Non-Cooperation Movement", "Civil Disobedience Movement", "Home Rule Movement"],
        "options_te": ["స్వదేశీ మరియు వందేమాతరం ఉద్యమం", "సహాయ నిరాకరణ ఉద్యమం", "శాసనోల్లంఘన ఉద్యమం", "హోమ్‌రూల్ ఉద్యమం"],
        "correct_option": 0,
        "explanation_en": "The partition of Bengal on 16 October 1905 led to the Swadeshi and Boycott movement across India, with the song 'Vande Mataram' becoming its anthem.",
        "explanation_te": "1905 బెంగాల్ విభజన ప్రకటనతో విదేశీ వస్తు బహిష్కరణ, స్వదేశీ ఉత్పత్తుల ప్రోత్సాహమే లక్ష్యంగా 'వందేమాతరం (స్వదేశీ) ఉద్యమం' ప్రారంభమైంది."
    },
    {
        "id": 140,
        "section": "General Studies",
        "topic": "Indian National Movement - Non-Cooperation",
        "question_en": "Mahatma Gandhi abruptly suspended the Non-Cooperation Movement in February 1922 following which violent incident?",
        "question_te": "1922 ఫిబ్రవరిలో జరిగిన ఏ హింసాత్మక సంఘటన కారణంగా మహాత్మా గాంధీ సహాయ నిరాకరణ ఉద్యమాన్ని అర్ధాంతరంగా నిలిపివేశారు?",
        "options_en": ["Chauri Chaura incident", "Jallianwala Bagh massacre", "Kakori train action", "Lahore conspiracy incident"],
        "options_te": ["చౌరీ చౌరా సంఘటన (Chauri Chaura)", "జలియన్‌వాలా బాగ్ దురంతం", "కాకోరి సంఘటన", "లాహోర్ కుట్ర కేసు"],
        "correct_option": 0,
        "explanation_en": "On 4 February 1922 at Chauri Chaura (Gorakhpur, UP), a crowd set fire to a police station, killing 22 policemen. Due to the violation of non-violence, Gandhi withdrew the movement.",
        "explanation_te": "ఉత్తరప్రదేశ్‌లోని చౌరీ చౌరా వద్ద నిరసనకారులు పోలీస్ స్టేషన్‌కు నిప్పు పెట్టడంతో 22 మంది పోలీసులు మరణించారు. అహింసా సిద్ధాంతం ఉల్లంఘనకు గురికావడంతో గాంధీజీ ఉద్యమాన్ని విరమించారు."
    },
    {
        "id": 141,
        "section": "General Studies",
        "topic": "Indian National Movement - Civil Disobedience",
        "question_en": "Mahatma Gandhi began the historic Salt March (Dandi March) on 12 March 1930 from which ashram?",
        "question_te": "1930 మార్చి 12న మహాత్మా గాంధీ చారిత్రాత్మక ఉప్పు సత్యాగ్రహం (దండి మార్చ్) ను ఏ ఆశ్రమం నుండి ప్రారంభించారు?",
        "options_en": ["Sabarmati Ashram (Ahmedabad)", "Wardha Ashram", "Sevagram Ashram", "Phoenix Settlement"],
        "options_te": ["సబర్మతి ఆశ్రమం (అహ్మదాబాద్)", "వార్ధా ఆశ్రమం", "సేవాగ్రామ్ ఆశ్రమం", "ఫీనిక్స్ ఆశ్రమం"],
        "correct_option": 0,
        "explanation_en": "Gandhi marched 240 miles from Sabarmati Ashram in Ahmedabad to the coastal village of Dandi with 78 volunteers to break the British salt monopoly.",
        "explanation_te": "గాంధీజీ 78 మంది అనుచరులతో అహ్మదాబాద్‌లోని సబర్మతి ఆశ్రమం నుండి బయలుదేరి దండి వద్ద ఉప్పు చట్టాన్ని ఉల్లంఘించి శాసనోల్లంఘన ఉద్యమాన్ని ప్రారంభించారు."
    },
    {
        "id": 142,
        "section": "General Studies",
        "topic": "Indian National Movement - Round Table Conferences",
        "question_en": "In which Round Table Conference held in London did Mahatma Gandhi participate as the sole representative of the Indian National Congress?",
        "question_te": "లండన్‌లో జరిగిన ఏ రౌండ్ టేబుల్ సమావేశానికి భారత జాతీయ కాంగ్రెస్ ఏకైక ప్రతినిధిగా మహాత్మా గాంధీ హాజరయ్యారు?",
        "options_en": ["Second Round Table Conference (1931)", "First Round Table Conference (1930)", "Third Round Table Conference (1932)", "All three conferences"],
        "options_te": ["రెండవ రౌండ్ టేబుల్ సమావేశం (1931)", "మొదటి రౌండ్ టేబుల్ సమావేశం (1930)", "మూడవ రౌండ్ టేబుల్ సమావేశం (1932)", "పై మూడు సమావేశాలకూ"],
        "correct_option": 0,
        "explanation_en": "Following the Gandhi-Irwin Pact of 1931, Gandhi represented the Indian National Congress only at the Second Round Table Conference in London.",
        "explanation_te": "గాంధీ-ఇర్విన్ ఒడంబడిక ప్రకారం మహాత్మా గాంధీ కాంగ్రెస్ తరపున 1931 లో జరిగిన రెండవ రౌండ్ టేబుల్ సమావేశంలో మాత్రమే పాల్గొన్నారు."
    },
    {
        "id": 143,
        "section": "General Studies",
        "topic": "Indian National Movement - Quit India",
        "question_en": "Mahatma Gandhi gave the famous call 'Do or Die' (కరో యా మరో) during which major freedom movement?",
        "question_te": "మహాత్మా గాంధీ 'డూ ఆర్ డై' (కరో యా మరో - సాధించు లేదా మరణించు) అనే చారిత్రాత్మక నినాదాన్ని ఏ ఉద్యమ సమయంలో ఇచ్చారు?",
        "options_en": ["Quit India Movement (1942)", "Non-Cooperation Movement (1920)", "Civil Disobedience Movement (1930)", "Champaran Satyagraha (1917)"],
        "options_te": ["క్విట్ ఇండియా ఉద్యమం (1942)", "సహాయ నిరాకరణ ఉద్యమం (1920)", "శాసనోల్లంఘన ఉద్యమం (1930)", "చంపారన్ సత్యాగ్రహం (1917)"],
        "correct_option": 0,
        "explanation_en": "On 8 August 1942 at the Gowalia Tank Maidan in Bombay, Gandhi gave the mantra 'Do or Die' launching the Quit India Movement.",
        "explanation_te": "1942 ఆగస్టు 8న బొంబాయిలోని గోవాలియా ట్యాంక్ మైదానంలో క్విట్ ఇండియా తీర్మానం సందర్భంగా గాంధీజీ 'డూ ఆర్ డై' నినాదాన్ని ఇచ్చారు."
    },
    {
        "id": 144,
        "section": "General Studies",
        "topic": "Indian National Movement - INA",
        "question_en": "Netaji Subhas Chandra Bose established the Provisional Government of Free India (Azad Hind) in October 1943 in:",
        "question_te": "నేతాజీ సుభాష్ చంద్రబోస్ అక్టోబర్ 1943 లో తాత్కాలిక స్వతంత్ర భారత ప్రభుత్వాన్ని (ఆజాద్ హింద్) ఎక్కడ స్థాపించారు?",
        "options_en": ["Singapore", "Tokyo", "Berlin", "Rangoon"],
        "options_te": ["సింగపూర్ (Singapore)", "టోక్యో", "బెర్లిన్", "రంగూన్"],
        "correct_option": 0,
        "explanation_en": "Subhas Chandra Bose proclaimed the Arzi Hukumat-e-Azad Hind (Provisional Government of Free India) in Singapore on 21 October 1943.",
        "explanation_te": "1943 అక్టోబర్ 21న సింగపూర్‌లో నేతాజీ సుభాష్ చంద్రబోస్ 'ఆజాద్ హింద్' తాత్కాలిక ప్రభుత్వాన్ని ఏర్పాటు చేశారు."
    },
    {
        "id": 145,
        "section": "General Studies",
        "topic": "Modern Indian History - INC Sessions",
        "question_en": "Who presided over the historic 1929 Lahore session of the Indian National Congress where the resolution for 'Purna Swaraj' (Complete Independence) was adopted?",
        "question_te": "'పూర్ణ స్వరాజ్' (సంపూర్ణ స్వాతంత్ర్యం) తీర్మానాన్ని ఆమోదించిన 1929 చారిత్రాత్మక లాహోర్ కాంగ్రెస్ సమావేశానికి అధ్యక్షత వహించినది ఎవరు?",
        "options_en": ["Jawaharlal Nehru", "Subhas Chandra Bose", "Sardar Vallabhbhai Patel", "Motilal Nehru"],
        "options_te": ["జవహర్‌లాల్ నెహ్రూ (Jawaharlal Nehru)", "సుభాష్ చంద్రబోస్", "సర్దార్ వల్లభ్‌భాయ్ పటేల్", "మోతీలాల్ నెహ్రూ"],
        "correct_option": 0,
        "explanation_en": "Under the presidency of Jawaharlal Nehru, the INC passed the historic Purna Swaraj resolution at its Lahore session in December 1929.",
        "explanation_te": "1929 డిసెంబర్‌లో లాహోర్‌లో జరిగిన జాతీయ కాంగ్రెస్ సదస్సుకు జవహర్‌లాల్ నెహ్రూ అధ్యక్షత వహించారు. ఈ సదస్సులోనే 'పూర్ణ స్వరాజ్' తీర్మానం ఆమోదించబడింది."
    },

    # =========================================================================
    # 4. GEOGRAPHY OF INDIA & TELANGANA (Q146 - Q157)
    # =========================================================================
    {
        "id": 146,
        "section": "General Studies",
        "topic": "Indian Geography - Physical Divisions",
        "question_en": "Which pass connects Srinagar to Leh across the Zanskar range in Ladakh?",
        "question_te": "లడఖ్‌లోని జస్కర్ శ్రేణి గుండా శ్రీనగర్ మరియు లేహ్ లను కలిపే ప్రసిద్ధ కనుమ ఏది?",
        "options_en": ["Zojila Pass", "Nathu La Pass", "Shipki La Pass", "Bomdi La Pass"],
        "options_te": ["జోజిలా కనుమ (Zojila Pass)", "నాథులా కనుమ (సిక్కిం)", "షిప్కిలా కనుమ (హిమాచల్)", "బొమ్‌డిలా కనుమ (అరుణాచల్)"],
        "correct_option": 0,
        "explanation_en": "Zoji La is a strategic high mountain pass in the Himalayas in the Union Territory of Ladakh connecting the Kashmir Valley with the Indus Valley in Ladakh.",
        "explanation_te": "కాశ్మీర్ లోయలోని శ్రీనగర్ నుండి లడఖ్‌లోని లేహ్ పట్టణాన్ని కలిపే కీలకమైన హిమాలయ కనుమ 'జోజిలా'."
    },
    {
        "id": 147,
        "section": "General Studies",
        "topic": "Indian Geography - Rivers & Drainage",
        "question_en": "Which is the largest peninsular river system in India, also known as 'Dakshin Ganga'?",
        "question_te": "భారతదేశంలోనే అతిపెద్ద ద్వీపకల్ప నదీ వ్యవస్థ మరియు 'దక్షిణ గంగ' అని పిలువబడే నది ఏది?",
        "options_en": ["Godavari", "Krishna", "Cauvery", "Mahanadi"],
        "options_te": ["గోదావరి (Godavari)", "కృష్ణా (Krishna)", "కావేరి (Cauvery)", "మహానది (Mahanadi)"],
        "correct_option": 0,
        "explanation_en": "The Godavari is the longest and largest river in Peninsular India (1,465 km), originating at Trimbakeshwar in Maharashtra and flowing into the Bay of Bengal.",
        "explanation_te": "మహారాష్ట్రలోని త్రయంబకేశ్వర్ వద్ద జన్మించి 1465 కి.మీ ప్రవహించే గోదావరి నది భారతదేశంలోనే అతిపెద్ద ద్వీపకల్ప నది. దీనిని 'దక్షిణ గంగ' అని పిలుస్తారు."
    },
    {
        "id": 148,
        "section": "General Studies",
        "topic": "Telangana Geography - Rivers",
        "question_en": "At which historic location in Telangana does the River Godavari enter the state from Maharashtra?",
        "question_te": "గోదావరి నది మహారాష్ట్ర నుండి తెలంగాణ రాష్ట్రంలోకి ప్రవేశించే సరిహద్దు ప్రాంతం ఏది?",
        "options_en": ["Kandakurthi (Nizamabad district)", "Basar (Nirmal district)", "Bhadrachalam", "Dharmapuri (Jagtial)"],
        "options_te": ["కందకుర్తి (నిజామాబాద్ జిల్లా)", "బాసర (నిర్మల్ జిల్లా)", "భద్రాచలం", "ధర్మపురి (జగిత్యాల)"],
        "correct_option": 0,
        "explanation_en": "River Godavari enters Telangana at Kandakurthi in Nizamabad district, where it forms a Triveni Sangam with the Manjeera and Haridra rivers.",
        "explanation_te": "గోదావరి నది నిజామాబాద్ జిల్లాలోని కందకుర్తి వద్ద తెలంగాణలోకి ప్రవేశిస్తుంది. ఇక్కడ మంజీరా, హరిద్ర నదులతో కలిసి త్రివేణి సంగమం ఏర్పడుతుంది."
    },
    {
        "id": 149,
        "section": "General Studies",
        "topic": "Telangana Geography - Tributaries",
        "question_en": "Which major tributary joins the Godavari river on its left bank and is formed by the confluence of the Penganga, Wardha, and Wainganga rivers?",
        "question_te": "పెన్ గంగ, వార్ధా మరియు వైన్ గంగ నదుల కలయిక ద్వారా ఏర్పడి గోదావరి నదిలో కలిసే అతిపెద్ద ఉపనది ఏది?",
        "options_en": ["Pranahita", "Manjeera", "Indravati", "Sabari"],
        "options_te": ["ప్రాణహిత (Pranahita)", "మంజీరా", "ఇంద్రావతి", "శబరి"],
        "correct_option": 0,
        "explanation_en": "The Pranahita river is formed by the combined waters of Wardha, Penganga, and Wainganga, and is the largest tributary of the Godavari by discharge volume.",
        "explanation_te": "వార్ధా, పెన్‌గంగ, వైన్‌గంగ నదుల సంగమంతో ప్రాణహిత నది ఏర్పడుతుంది. ఇది గోదావరి నదికి గల అతిపెద్ద ఉపనది."
    },
    {
        "id": 150,
        "section": "General Studies",
        "topic": "Telangana Geography - Irrigation",
        "question_en": "The Sriram Sagar Project (SRSP / Pochampad Project), a lifeline for northern Telangana agriculture, is built across which river?",
        "question_te": "ఉత్తర తెలంగాణ రైతులకు జీవనాడి అయిన శ్రీరాంసాగర్ ప్రాజెక్ట్ (పోచంపాడు) ఏ నదిపై నిర్మించబడింది?",
        "options_en": ["Godavari", "Krishna", "Manjeera", "Musi"],
        "options_te": ["గోదావరి (Godavari)", "కృష్ణా", "మంజీరా", "మూసీ"],
        "correct_option": 0,
        "explanation_en": "The Sriram Sagar Project (SRSP) is built across the Godavari River in Nizamabad district of Telangana.",
        "explanation_te": "శ్రీరాంసాగర్ ప్రాజెక్ట్ (పోచంపాడు) నిజామాబాద్ జిల్లా వద్ద గోదావరి నదిపై నిర్మించబడిన ప్రముఖ నీటిపారుదల ప్రాజెక్టు."
    },
    {
        "id": 151,
        "section": "General Studies",
        "topic": "Telangana Geography - Minerals",
        "question_en": "The Singareni Collieries Company Limited (SCCL), the premier coal mining company of Telangana, extracts coal from which geological valley basin?",
        "question_te": "తెలంగాణలోని ప్రముఖ బొగ్గు గనుల సంస్థ అయిన సింగరేణి కాలరీస్ (SCCL) ఏ నదీ లోయ పరివాహక ప్రాంతం నుండి బొగ్గును వెలికితీస్తుంది?",
        "options_en": ["Pranahita-Godavari Valley", "Krishna-Tungabhadra Valley", "Narmada Valley", "Damodar Valley"],
        "options_te": ["ప్రాణహిత - గోదావరి లోయ", "కృష్ణా - తుంగభద్ర లోయ", "నర్మదా లోయ", "దామోదర్ లోయ"],
        "correct_option": 0,
        "explanation_en": "SCCL mines coal deposits situated in the Pranahita-Godavari valley belt spanning Khammam, Bhadradri Kothagudem, Jayashankar Bhupalpally, Peddapalli, Mancherial, and Asifabad.",
        "explanation_te": "సింగరేణి సంస్థ ప్రాణహిత - గోదావరి నదీ లోయలోని గోండ్వానా బొగ్గు నిల్వల నుండి బొగ్గును వెలికితీస్తుంది."
    },
    {
        "id": 152,
        "section": "General Studies",
        "topic": "Indian Geography - Soils",
        "question_en": "Black cotton soils (Regur soils), ideal for cotton cultivation, are predominantly rich in which type of clay mineral with high water retention?",
        "question_te": "పత్తి పంటకు ఎంతో అనుకూలమైన నల్లరేగడి నేలలు (రెగూర్ నేలలు) నీటిని నిల్వ ఉంచుకునే ఏ బంకమట్టి ఖనిజాన్ని ఎక్కువగా కలిగి ఉంటాయి?",
        "options_en": ["Montmorillonite", "Kaolinite", "Illite", "Bauxite"],
        "options_te": ["మాంట్‌మోరిల్లోనైట్ (Montmorillonite)", "కావోలినైట్", "ఇల్లైట్", "బాక్సైట్"],
        "correct_option": 0,
        "explanation_en": "Black soils are rich in montmorillonite clay minerals, which swell when wet and contract forming cracks when dry, conferring high moisture-retentive capacity.",
        "explanation_te": "నల్లరేగడి నేలలు అధిక నీటి నిల్వ సామర్థ్యాన్ని ఇచ్చే మాంట్‌మోరిల్లోనైట్ అనే క్లే ఖనిజాన్ని కలిగి ఉంటాయి."
    },
    {
        "id": 153,
        "section": "General Studies",
        "topic": "Telangana Geography - Demographics & Borders",
        "question_en": "Which of the following states does NOT share a territorial border with Telangana?",
        "question_te": "క్రింది రాష్ట్రాలలో తెలంగాణ రాష్ట్రంతో సరిహద్దును పంచుకోని రాష్ట్రం ఏది?",
        "options_en": ["Odisha", "Maharashtra", "Karnataka", "Chhattisgarh"],
        "options_te": ["ఒడిశా (Odisha)", "మహారాష్ట్ర", "కర్ణాటక", "ఛత్తీస్‌గఢ్"],
        "correct_option": 0,
        "explanation_en": "Telangana is surrounded by Maharashtra, Karnataka, Chhattisgarh, and Andhra Pradesh. It does not share a direct border with Odisha.",
        "explanation_te": "తెలంగాణ రాష్ట్రం మహారాష్ట్ర, కర్ణాటక, ఛత్తీస్‌గఢ్, ఆంధ్రప్రదేశ్‌లతో మాత్రమే సరిహద్దులను పంచుకుంటుంది. ఒడిశాతో నేరుగా సరిహద్దు లేదు."
    },
    {
        "id": 154,
        "section": "General Studies",
        "topic": "Indian Geography - Climate & Monsoons",
        "question_en": "The Coromandel Coast of Tamil Nadu receives the bulk of its annual rainfall during the months of October to December from which monsoon winds?",
        "question_te": "తమిళనాడులోని కోరమాండల్ తీర ప్రాంతం అక్టోబర్ నుండి డిసెంబర్ నెలల కాలంలో ఏ ఋతుపవనాల వల్ల అత్యధిక వర్షపాతాన్ని పొందుతుంది?",
        "options_en": ["North-East (Retreating) Monsoon", "South-West Monsoon", "Western Disturbances", "Nor'westers"],
        "options_te": ["ఈశాన్య (తిరోగమన) ఋతుపవనాలు", "నైరుతి ఋతుపవనాలు", "పశ్చిమ విక్షోభాలు", "నార్వెస్టర్లు"],
        "correct_option": 0,
        "explanation_en": "The Coromandel coast receives its main rainfall from the North-East monsoon (October to December) as winds pick up moisture over the Bay of Bengal.",
        "explanation_te": "బంగాళాఖాతం మీదుగా వీచే ఈశాన్య ఋతుపవనాల వలన అక్టోబర్-డిసెంబర్ శీతాకాలంలో తమిళనాడు కోరమాండల్ తీరానికి భారీ వర్షాలు కురుస్తాయి."
    },
    {
        "id": 155,
        "section": "General Studies",
        "topic": "Telangana Geography - Plateaus & Hills",
        "question_en": "The highest peak in Telangana is located in which hill range of the state?",
        "question_te": "తెలంగాణ రాష్ట్రంలోని అత్యంత ఎత్తైన శిఖరం ఏ కొండల శ్రేణిలో కలదు?",
        "options_en": ["Doli Gutta (Bhadradri Kothagudem - 965 m)", "Ananthagiri Hills (Vikarabad)", "Rachakonda Hills", "Nirmal Hills"],
        "options_te": ["డోలి గుట్ట (భద్రాద్రి కొత్తగూడెం జిల్లా - 965 మీ)", "అనంతగిరి కొండలు (వికారాబాద్)", "రాచకొండ గుట్టలు", "నిర్మల్ కొండలు"],
        "correct_option": 0,
        "explanation_en": "Doli Gutta (approx. 965 m above sea level), located in the border hills of Bhadradri Kothagudem and Chhattisgarh, is the highest peak in Telangana.",
        "explanation_te": "భద్రాద్రి కొత్తగూడెం జిల్లా సరిహద్దులో గల 'డోలి గుట్ట' (దాదాపు 965 మీటర్ల ఎత్తు) తెలంగాణలోని అత్యున్నత శిఖరం."
    },
    {
        "id": 156,
        "section": "General Studies",
        "topic": "Indian Geography - Multipurpose Dams",
        "question_en": "The Nagarjuna Sagar Dam, one of the earliest large masonry dams in India, is built across which river?",
        "question_te": "భారతదేశంలో తొలి రాతి కట్టడం ప్రాజెక్టులలో ఒకటైన నాగార్జున సాగర్ డ్యామ్ ఏ నదిపై నిర్మించబడింది?",
        "options_en": ["Krishna", "Godavari", "Tungabhadra", "Pennar"],
        "options_te": ["కృష్ణా నది (Krishna)", "గోదావరి", "తుంగభద్ర", "పెన్నా నది"],
        "correct_option": 0,
        "explanation_en": "Nagarjuna Sagar Dam is a major masonry dam built across the Krishna River between Nalgonda district of Telangana and Palnadu district of Andhra Pradesh.",
        "explanation_te": "నాగార్జునసాగర్ ప్రాజెక్ట్ నల్గొండ మరియు పల్నాడు సరిహద్దులో కృష్ణా నదిపై నిర్మించబడిన ప్రతిష్టాత్మక బహుళార్ధసాధక ప్రాజెక్టు."
    },
    {
        "id": 157,
        "section": "General Studies",
        "topic": "Telangana Geography - Forests",
        "question_en": "As per the Forest Survey of India, which district in Telangana has the largest total geographical area under forest cover?",
        "question_te": "భారత అటవీ సర్వే నివేదిక ప్రకారం తెలంగాణలో అత్యధిక అటవీ విస్తీర్ణం కలిగిన జిల్లా ఏది?",
        "options_en": ["Bhadradri Kothagudem", "Mulugu", "Adilabad", "Khammam"],
        "options_te": ["భద్రాద్రి కొత్తగూడెం (Bhadradri Kothagudem)", "ములుగు", "ఆదిలాబాద్", "ఖమ్మం"],
        "correct_option": 0,
        "explanation_en": "Bhadradri Kothagudem district has the largest total area under forest cover in Telangana state.",
        "explanation_te": "తెలంగాణ రాష్ట్రంలో విస్తీర్ణం పరంగా అత్యధిక అటవీ ప్రాంతాన్ని కలిగి ఉన్న జిల్లా భద్రాద్రి కొత్తగూడెం."
    },

    # =========================================================================
    # 5. INDIAN POLITY & GOVERNANCE (Q158 - Q170)
    # =========================================================================
    {
        "id": 158,
        "section": "General Studies",
        "topic": "Indian Polity - Preamble",
        "question_en": "Which three words were added to the Preamble of the Indian Constitution by the 42nd Constitutional Amendment Act of 1976?",
        "question_te": "1976 నాటి 42వ రాజ్యాంగ సవరణ చట్టం ద్వారా భారత రాజ్యాంగ పీఠిక (Preamble) కు చేర్చబడిన మూడు పదాలు ఏవి?",
        "options_en": ["Socialist, Secular, and Integrity", "Sovereign, Democratic, Republic", "Liberty, Equality, Fraternity", "Justice, Unity, Dignity"],
        "options_te": ["సామ్యవాద, లౌకిక మరియు సమగ్రత (Socialist, Secular, Integrity)", "సార్వభౌమ, ప్రజాస్వామ్య, గణతంత్ర", "స్వేచ్ఛ, సమానత్వం, సౌభ్రాతృత్వం", "న్యాయం, ఐక్యత, గౌరవం"],
        "correct_option": 0,
        "explanation_en": "The 42nd Amendment Act (1976) introduced three words into the Preamble: 'Socialist', 'Secular', and 'Integrity'.",
        "explanation_te": "1976 లో 42వ సవరణ ద్వారా పీఠికలో 'సామ్యవాద', 'లౌకిక' మరియు 'సమగ్రత' అనే మూడు పదాలను చేర్చారు."
    },
    {
        "id": 159,
        "section": "General Studies",
        "topic": "Indian Polity - Fundamental Rights",
        "question_en": "Which Article of the Indian Constitution guarantees the 'Right to Constitutional Remedies', described by Dr. B. R. Ambedkar as the 'Heart and Soul of the Constitution'?",
        "question_te": "డాక్టర్ బి. ఆర్. అంబేద్కర్ 'రాజ్యాంగానికి ఆత్మ మరియు హృదయం' గా అభివర్ణించిన 'రాజ్యాంగ పరిహారపు హక్కు' ఏ నిబంధనలో ఉంది?",
        "options_en": ["Article 32", "Article 21", "Article 19", "Article 14"],
        "options_te": ["ఆర్టికల్ 32 (Article 32)", "ఆర్టికల్ 21", "ఆర్టికల్ 19", "ఆర్టికల్ 14"],
        "correct_option": 0,
        "explanation_en": "Article 32 empowers citizens to directly approach the Supreme Court for the enforcement of Fundamental Rights via writs.",
        "explanation_te": "ప్రాథమిక హక్కుల రక్షణ కోసం సుప్రీంకోర్టును ఆశ్రయించే హక్కును కల్పించే ఆర్టికల్ 32 ని అంబేద్కర్ రాజ్యాంగానికి హృదయం మరియు ఆత్మ అని పేర్కొన్నారు."
    },
    {
        "id": 160,
        "section": "General Studies",
        "topic": "Indian Polity - Writs",
        "question_en": "Which writ literally translates to 'We Command' and is issued by higher courts to compel a public official or authority to perform a mandatory statutory duty?",
        "question_te": "'మేము ఆదేశిస్తున్నాము' (We Command) అనే అర్థం కలిగి, ఒక ప్రభుత్వ అధికారి తన చట్టబద్ధమైన విధిని నిర్వర్తించేలా ఉన్నత న్యాయస్థానాలు జారీ చేసే రిట్ ఏది?",
        "options_en": ["Mandamus", "Habeas Corpus", "Quo Warranto", "Certiorari"],
        "options_te": ["మాండమస్ (Mandamus)", "హేబియస్ కార్పస్ (Habeas Corpus)", "కో-వారెంటో (Quo Warranto)", "సెర్షియోరరై (Certiorari)"],
        "correct_option": 0,
        "explanation_en": "The writ of Mandamus commands an inferior court, tribunal, board, or public officer to perform an official or legal duty they have failed or refused to do.",
        "explanation_te": "ప్రభుత్వ అధికారి లేదా సంస్థ తమ విధుల నిర్వహణలో విఫలమైనప్పుడు ఆ విధిని నిర్వర్తించాలని ఆదేశిస్తూ ఇచ్చే రిట్ 'మాండమస్'."
    },
    {
        "id": 161,
        "section": "General Studies",
        "topic": "Indian Polity - Directive Principles (DPSP)",
        "question_en": "The Directive Principles of State Policy (DPSP) contained in Part IV of the Indian Constitution were borrowed from which country's constitution?",
        "question_te": "భారత రాజ్యాంగంలోని 4వ భాగంలో గల ఆదేశిక సూత్రాలు (DPSP) ఏ దేశ రాజ్యాంగం నుండి గ్రహించబడ్డాయి?",
        "options_en": ["Ireland", "United Kingdom", "USA", "Australia"],
        "options_te": ["ఐర్లాండ్ (Ireland)", "బ్రిటన్", "అమెరికా", "ఆస్ట్రేలియా"],
        "correct_option": 0,
        "explanation_en": "The Directive Principles of State Policy (Articles 36–51) were borrowed from the Constitution of Ireland (1937).",
        "explanation_te": "భారత రాజ్యాంగ నిర్మాతలు ఆదేశిక సూత్రాల భావనను ఐరిష్ (ఐర్లాండ్) రాజ్యాంగం నుండి స్వీకరించారు."
    },
    {
        "id": 162,
        "section": "General Studies",
        "topic": "Indian Polity - President",
        "question_en": "Under which Article of the Indian Constitution can the President grant pardons, reprieves, respites, or remissions of punishment to convicted persons?",
        "question_te": "భారత రాజ్యాంగంలోని ఏ అధికరణం ప్రకారం రాష్ట్రపతి క్షమాభిక్ష (Pardon) ప్రసాదించే విశేషాధికారాన్ని కలిగి ఉంటారు?",
        "options_en": ["Article 72", "Article 61", "Article 74", "Article 123"],
        "options_te": ["ఆర్టికల్ 72 (Article 72)", "ఆర్టికల్ 61", "ఆర్టికల్ 74", "ఆర్టికల్ 123"],
        "correct_option": 0,
        "explanation_en": "Article 72 empowers the President of India to grant pardons, reprieves, respites, or remissions of punishment or to suspend, remit or commute sentences.",
        "explanation_te": "రాజ్యాంగంలోని 72వ అధికరణం రాష్ట్రపతికి శిక్షలను తగ్గించే, రద్దు చేసే లేదా క్షమాభిక్ష పెట్టే అధికారాన్ని కల్పిస్తుంది."
    },
    {
        "id": 163,
        "section": "General Studies",
        "topic": "Indian Polity - Parliament & Money Bill",
        "question_en": "Who has the final constitutional authority to certify whether a particular legislative bill is a 'Money Bill' or not?",
        "question_te": "ఒక బిల్లు 'ద్రవ్య బిల్లు' (Money Bill) అవునా కాదా అని తుది నిర్ణయం తీసుకుని ధృవీకరించే అధికారం ఎవరికి ఉంది?",
        "options_en": ["Speaker of Lok Sabha", "President of India", "Chairman of Rajya Sabha", "Finance Minister"],
        "options_te": ["లోక్‌సభ స్పీకర్ (Speaker of Lok Sabha)", "రాష్ట్రపతి", "రాజ్యసభ చైర్మన్", "కేంద్ర ఆర్థిక మంత్రి"],
        "correct_option": 0,
        "explanation_en": "Under Article 110(3), the decision of the Speaker of the Lok Sabha on whether a bill is a Money Bill is final and conclusive.",
        "explanation_te": "110(3) అధికరణం ప్రకారం ఒక బిల్లు ద్రవ్య బిల్లా కాదా అని నిర్ణయించే అంతిమ అధికారం లోక్‌సభ స్పీకర్‌కు మాత్రమే ఉంటుంది."
    },
    {
        "id": 164,
        "section": "General Studies",
        "topic": "Indian Polity - Rajya Sabha",
        "question_en": "What is the term of office of a member of the Rajya Sabha, and what fraction of its members retire every two years?",
        "question_te": "రాజ్యసభ సభ్యుని పదవీకాలం ఎంత, మరియు ప్రతి రెండు సంవత్సరాలకు ఎంత భాగం సభ్యులు పదవీ విరమణ చేస్తారు?",
        "options_en": ["6 years term, one-third (1/3) retire every two years", "5 years term, half (1/2) retire every two years", "6 years term, one-fourth (1/4) retire every two years", "Permanent without retirement"],
        "options_te": ["6 సంవత్సరాల పదవీకాలం, ప్రతి 2 సంవత్సరాలకు 1/3 వంతు సభ్యులు విరమణ చేస్తారు", "5 సంవత్సరాలు, సగం మంది విరమణ", "6 సంవత్సరాలు, 1/4 వంతు విరమణ", "శాశ్వత సభ, పదవీ విరమణ ఉండదు"],
        "correct_option": 0,
        "explanation_en": "Rajya Sabha is a permanent body not subject to dissolution. Members serve for 6 years, with one-third retiring every two years (Article 83).",
        "explanation_te": "రాజ్యసభ శాశ్వత సభ. దీని సభ్యుల పదవీకాలం 6 సంవత్సరాలు. ప్రతి రెండేళ్లకు మూడో వంతు (1/3) సభ్యులు పదవీ విరమణ పొందుతారు."
    },
    {
        "id": 165,
        "section": "General Studies",
        "topic": "Indian Polity - Judiciary",
        "question_en": "By which constitutional writ can the Supreme Court or High Courts quash an illegal appointment of an individual to a public office?",
        "question_te": "చట్టబద్ధమైన అర్హత లేకుండా ఒక వ్యక్తి ప్రభుత్వ పదవిని ఆక్రమించినప్పుడు ఆ నియామకాన్ని రద్దు చేయడానికి న్యాయస్థానాలు జారీ చేసే రిట్ ఏది?",
        "options_en": ["Quo Warranto", "Prohibition", "Certiorari", "Mandamus"],
        "options_te": ["కో-వారెంటో (Quo Warranto)", "ప్రొహిబిషన్ (Prohibition)", "సెర్షియోరరై", "మాండమస్"],
        "correct_option": 0,
        "explanation_en": "The writ of Quo Warranto (literally 'By what authority') is issued to prevent illegal usurpation of a public office by a person.",
        "explanation_te": "'ఏ అధికారంతో' ఈ పదవిలో ఉన్నారో తెలపాలని ప్రశ్నిస్తూ ప్రభుత్వ పదవుల దురాక్రమణను నిరోధించే రిట్ 'కో-వారెంటో'."
    },
    {
        "id": 166,
        "section": "General Studies",
        "topic": "Indian Polity - Constitutional Bodies",
        "question_en": "The Comptroller and Auditor General of India (CAG) is appointed under which Article of the Constitution?",
        "question_te": "భారత కంప్ట్రోలర్ అండ్ ఆడిటర్ జనరల్ (కాగ్ - CAG) నియామకం రాజ్యాంగంలోని ఏ నిబంధన ప్రకారం జరుగుతుంది?",
        "options_en": ["Article 148", "Article 280", "Article 324", "Article 76"],
        "options_te": ["ఆర్టికల్ 148 (Article 148)", "ఆర్టికల్ 280 (ఆర్థిక సంఘం)", "ఆర్టికల్ 324 (ఎన్నికల సంఘం)", "ఆర్టికల్ 76 (అటార్నీ జనరల్)"],
        "correct_option": 0,
        "explanation_en": "Article 148 provides for an independent Comptroller and Auditor General of India appointed by the President.",
        "explanation_te": "148వ అధికరణం ప్రకారం భారత రాష్ట్రపతి కాగ్‌ను నియమిస్తారు. ప్రభుత్వ ఆదాయ వ్యయాల ఆడిటింగ్‌ను ఇది పర్యవేక్షిస్తుంది."
    },
    {
        "id": 167,
        "section": "General Studies",
        "topic": "Indian Polity - Panchayati Raj",
        "question_en": "The 73rd Constitutional Amendment Act, 1992 added which Schedule to the Indian Constitution containing 29 functional subjects for Panchayats?",
        "question_te": "73వ రాజ్యాంగ సవరణ చట్టం ద్వారా పంచాయతీలకు 29 విధులను కేటాయిస్తూ భారత రాజ్యాంగానికి ఏ షెడ్యూల్‌ను చేర్చారు?",
        "options_en": ["11th Schedule", "12th Schedule", "10th Schedule", "9th Schedule"],
        "options_te": ["11వ షెడ్యూల్ (11th Schedule)", "12వ షెడ్యూల్ (మున్సిపాలిటీలు)", "10వ షెడ్యూల్ (పార్టీ ఫిరాయింపులు)", "9వ షెడ్యూల్"],
        "correct_option": 0,
        "explanation_en": "The 73rd Amendment added the 11th Schedule containing 29 subjects for Panchayati Raj Institutions, while the 74th Amendment added the 12th Schedule for Municipalities.",
        "explanation_te": "73వ సవరణ ద్వారా గ్రామీణ స్థానిక సంస్థలకు (పంచాయతీలకు) 29 అంశాలతో కూడిన 11వ షెడ్యూల్‌ను చేర్చారు."
    },
    {
        "id": 168,
        "section": "General Studies",
        "topic": "Indian Polity - Anti-Defection",
        "question_en": "The Anti-Defection Law was introduced into the Constitution by which Amendment Act under the 10th Schedule?",
        "question_te": "పార్టీ ఫిరాయింపుల నిరోధక చట్టాన్ని (Anti-Defection Law) 10వ షెడ్యూల్ రూపంలో ఏ రాజ్యాంగ సవరణ ద్వారా చేర్చారు?",
        "options_en": ["52nd Amendment Act, 1985", "44th Amendment Act, 1978", "61st Amendment Act, 1988", "86th Amendment Act, 2002"],
        "options_te": ["52వ రాజ్యాంగ సవరణ చట్టం, 1985", "44వ రాజ్యాంగ సవరణ చట్టం, 1978", "61వ రాజ్యాంగ సవరణ చట్టం (ఓటు హక్కు 18 ఏళ్లు)", "86వ రాజ్యాంగ సవరణ చట్టం (విద్యా హక్కు)"],
        "correct_option": 0,
        "explanation_en": "The 52nd Constitutional Amendment Act of 1985 added the 10th Schedule to disqualify lawmakers switching political parties after elections.",
        "explanation_te": "1985 లో 52వ రాజ్యాంగ సవరణ చట్టం ద్వారా రాజకీయ పార్టీల ఫిరాయింపులను అరికట్టడానికి 10వ షెడ్యూల్‌ను రాజ్యాంగంలో చేర్చారు."
    },
    {
        "id": 169,
        "section": "General Studies",
        "topic": "Indian Polity - Emergency Provisions",
        "question_en": "Financial Emergency under Article 360 of the Indian Constitution has been proclaimed in India how many times so far?",
        "question_te": "భారత రాజ్యాంగంలోని 360వ నిబంధన క్రింద ఆర్థిక అత్యవసర పరిస్థితి (Financial Emergency) దేశంలో ఇప్పటివరకు ఎన్నిసార్లు విధించబడింది?",
        "options_en": ["Never (0 times)", "Once (1991)", "Twice", "Three times"],
        "options_te": ["ఎన్నడూ విధించలేదు (0 సార్లు)", "ఒకసారి (1991 లో)", "రెండు సార్లు", "మూడు సార్లు"],
        "correct_option": 0,
        "explanation_en": "Financial Emergency under Article 360 has never been declared in India so far, even during the severe balance-of-payments economic crisis of 1991.",
        "explanation_te": "భారతదేశంలో 360వ ఆర్టికల్ ప్రకారం ఆర్థిక అత్యవసర పరిస్థితిని ఇప్పటివరకు ఒక్కసారి కూడా విధించలేదు."
    },
    {
        "id": 170,
        "section": "General Studies",
        "topic": "Indian Polity - State Legislature",
        "question_en": "Under Article 169 of the Constitution, what is the procedure required to create or abolish a Legislative Council (Vidhan Parishad) in a state?",
        "question_te": "169వ నిబంధన ప్రకారం ఒక రాష్ట్రంలో శాసనమండలి (విధాన పరిషత్) ను రద్దు చేయడానికి లేదా ఏర్పాటు చేయడానికి అవసరమైన ప్రక్రియ ఏమిటి?",
        "options_en": ["State Assembly passes resolution by special majority, followed by simple majority Act of Parliament", "Governor's ordinance alone", "Presidential notification without Parliament", "Resolution by Rajya Sabha alone"],
        "options_te": ["రాష్ట్ర అసెంబ్లీ ప్రత్యేక మెజారిటీతో తీర్మానం చేసి పంపిన తర్వాత, పార్లమెంట్ సాధారణ మెజారిటీతో చట్టం చేయడం", "గవర్నర్ ఆర్డినెన్స్ ద్వారా మాత్రమే", "పార్లమెంట్‌తో సంబంధం లేకుండా రాష్ట్రపతి ఉత్తర్వు", "రాజ్యసభ సాధారణ తీర్మానం ద్వారా"],
        "correct_option": 0,
        "explanation_en": "The State Legislative Assembly must pass a resolution by a majority of total membership and not less than two-thirds of members present and voting, after which Parliament may pass a simple majority law.",
        "explanation_te": "శాసనసభ ప్రత్యేక మెజారిటీతో (2/3 హాజరైన సభ్యులు) తీర్మానం చేయాలి, ఆపై పార్లమెంటు సాధారణ మెజారిటీతో చట్టం చేసి శాసనమండలిని రద్దు లేదా ఏర్పాటు చేస్తుంది."
    },

    # =========================================================================
    # 6. INDIAN ECONOMY & TELANGANA ECONOMY (Q171 - Q180)
    # =========================================================================
    {
        "id": 171,
        "section": "General Studies",
        "topic": "Indian Economy - Banking & Monetary Policy",
        "question_en": "What is the 'Repo Rate' in the Reserve Bank of India's monetary policy operations?",
        "question_te": "రిజర్వ్ బ్యాంక్ ఆఫ్ ఇండియా (RBI) ద్రవ్య విధానంలో 'రెపో రేటు' (Repo Rate) అనగా ఏమిటి?",
        "options_en": ["The rate at which the RBI lends short-term funds to commercial banks against government securities", "The rate at which commercial banks park excess funds with RBI", "The interest rate commercial banks charge from general public", "The long-term lending rate for infrastructure projects"],
        "options_te": ["వాణిజ్య బ్యాంకులకు స్వల్పకాలిక నిధుల కోసం ఆర్‌బీఐ ఇచ్చే రుణాలపై విధించే వడ్డీ రేటు", "ఆర్‌బీఐ వద్ద బ్యాంకులు తమ మిగులు నిధులను దాచుకున్నప్పుడు ఆర్‌బీఐ ఇచ్చే వడ్డీ రేటు", "సామాన్య ప్రజలకు బ్యాంకులు ఇచ్చే రుణాల వడ్డీ రేటు", "దీర్ఘకాలిక మౌలిక సదుపాయాల ప్రాజెక్టుల వడ్డీ రేటు"],
        "correct_option": 0,
        "explanation_en": "Repo Rate (Repurchase Option Rate) is the benchmark interest rate at which the central bank (RBI) lends money to commercial banks against approved securities.",
        "explanation_te": "వాణిజ్య బ్యాంకులు ప్రభుత్వ సెక్యూరిటీలను తనఖా పెట్టి ఆర్‌బీఐ నుండి స్వల్పకాలిక రుణాలు తీసుకునే వడ్డీ రేటును రెపో రేటు అంటారు."
    },
    {
        "id": 172,
        "section": "General Studies",
        "topic": "Indian Economy - Inflation",
        "question_en": "Which index is officially adopted by the RBI's Monetary Policy Committee (MPC) as the primary headline measure to target retail inflation in India?",
        "question_te": "భారతదేశంలో ద్రవ్యోల్బణాన్ని నియంత్రించడానికి రిజర్వ్ బ్యాంక్ ద్రవ్య విధాన కమిటీ (MPC) ప్రామాణికంగా తీసుకునే సూచిక ఏది?",
        "options_en": ["Consumer Price Index (CPI - Combined)", "Wholesale Price Index (WPI)", "Index of Industrial Production (IIP)", "GDP Deflator"],
        "options_te": ["వినియోగదారుల ధరల సూచిక (CPI - Combined)", "హోల్‌సేల్ ధరల సూచిక (WPI)", "పారిశ్రామికోత్పత్తి సూచిక (IIP)", "జీడీపీ డిఫ్లేటర్"],
        "correct_option": 0,
        "explanation_en": "Following the Urjit Patel Committee recommendations, the RBI adopted the All-India Consumer Price Index (CPI-Combined) for headline inflation targeting (4% +/- 2%).",
        "explanation_te": "ఆర్‌బీఐ వినియోగదారుల స్థాయిలోని చిల్లర ద్రవ్యోల్బణాన్ని కొలవడానికి 'కన్స్యూమర్ ప్రైస్ ఇండెక్స్ (CPI)' ని అధికారిక కొలమానంగా ఉపయోగిస్తుంది."
    },
    {
        "id": 173,
        "section": "General Studies",
        "topic": "Indian Economy - National Income",
        "question_en": "Gross Domestic Product (GDP) is defined as the total market value of:",
        "question_te": "స్థూల దేశీయోత్పత్తి (GDP) అనగా ఒక నిర్దిష్ట కాలంలో:",
        "options_en": ["All final goods and services produced within the domestic territory of a country in a year", "All intermediate goods produced by multinational corporations", "Total assets owned by Indian citizens living abroad", "Net profit generated exclusively by government public sector units"],
        "options_te": ["ఒక సంవత్సర కాలంలో దేశ భౌగోళిక సరిహద్దుల లోపల ఉత్పత్తి చేయబడిన అన్ని అంతిమ వస్తువులు మరియు సేవల మార్కెట్ విలువ", "బహుళజాతి సంస్థలు ఉత్పత్తి చేసిన మధ్యంతర వస్తువుల విలువ", "విదేశాల్లో నివసించే భారతీయుల ఆస్తుల మొత్తం", "ప్రభుత్వ రంగ సంస్థలు ఆర్జించిన నికర లాభం మాత్రమే"],
        "correct_option": 0,
        "explanation_en": "GDP measures the monetary value of all final goods and services produced within a nation's geographical boundaries during a specified time period (usually 1 year).",
        "explanation_te": "ఒక ఆర్థిక సంవత్సరంలో దేశ సరిహద్దులలో ఉత్పత్తి అయిన మొత్తం అంతిమ వస్తు, సేవల ద్రవ్య విలువే స్థూల దేశీయోత్పత్తి (GDP)."
    },
    {
        "id": 174,
        "section": "General Studies",
        "topic": "Indian Economy - Fiscal Policy",
        "question_en": "What is 'Fiscal Deficit' in the Union or State Budget?",
        "question_te": "ప్రభుత్వ బడ్జెట్‌లో 'ద్రవ్య లోటు' (Fiscal Deficit) అనగా ఏమిటి?",
        "options_en": ["Total Expenditure minus Total Receipts (excluding borrowings)", "Total Revenue Expenditure minus Revenue Receipts", "Monetary deficit printed by RBI", "Difference between exports and imports"],
        "options_te": ["రుణాలు మినహాయించి మొత్తం వ్యయం నుండి మొత్తం ఆదాయాన్ని తీసివేయగా వచ్చే లోటు (ప్రభుత్వ నికర అప్పుల మొత్తం)", "రెవెన్యూ వ్యయం నుండి రెవెన్యూ ఆదాయం తీసివేయగా వచ్చేది", "ఆర్‌బీఐ ముద్రించిన కొత్త కరెన్సీ పరిమాణం", "ఎగుమతులు మరియు దిగుమతుల మధ్య తేడా"],
        "correct_option": 0,
        "explanation_en": "Fiscal Deficit = Total Expenditure - (Revenue Receipts + Non-debt Capital Receipts). It reflects the total borrowing requirements of the government from all sources.",
        "explanation_te": "ప్రభుత్వం బడ్జెట్ అవసరాల కోసం ఆ సంవత్సరంలో చేయవలసిన మొత్తం రుణాల పరిమాణాన్నే ద్రవ్య లోటు అంటారు."
    },
    {
        "id": 175,
        "section": "General Studies",
        "topic": "Indian Economy - GST",
        "question_en": "Goods and Services Tax (GST) in India, implemented on 1 July 2017, is what type of tax?",
        "question_te": "2017 జూలై 1 నుండి దేశవ్యాప్తంగా అమల్లోకి వచ్చిన వస్తు మరియు సేవల పన్ను (GST) ఏ రకమైన పన్ను?",
        "options_en": ["Comprehensive destination-based indirect consumption tax", "Direct income tax on corporate profits", "Origin-based manufacturing excise duty", "Progressive wealth tax"],
        "options_te": ["గమ్యస్థాన ఆధారిత సమగ్ర పరోక్ష వినియోగ పన్ను (Destination-based Indirect Tax)", "కార్పొరేట్ లాభాలపై ప్రత్యక్ష పన్ను", "ఉత్పత్తి ఆధారిత ఎక్సైజ్ సుంకం", "వ్యక్తిగత సంపద పన్ను"],
        "correct_option": 0,
        "explanation_en": "GST is a comprehensive, multi-stage, destination-based indirect tax levied on value addition at each stage of supply of goods and services.",
        "explanation_te": "GST అనేది వస్తువులు మరియు సేవల సరఫరాపై విధించే గమ్యస్థాన ఆధారిత (Destination-based) బహుళ అంచెల పరోక్ష పన్ను."
    },
    {
        "id": 176,
        "section": "General Studies",
        "topic": "Telangana Economy - Industrial Sector",
        "question_en": "Telangana accounts for approximately what fraction of India's total pharmaceutical exports, earning Hyderabad the title 'Pharma Capital of India'?",
        "question_te": "భారతదేశం నుండి ఎగుమతి అయ్యే ఔషధాలలో (Pharma exports) సుమారుగా ఎంత భాగం వాటాను తెలంగాణ కలిగి ఉంది?",
        "options_en": ["One-third (approx. 33% - 35%)", "5% to 10%", "65% to 70%", "Less than 2%"],
        "options_te": ["మూడింట ఒక వంతు (సుమారు 33% - 35%)", "5% నుండి 10% మాత్రమే", "65% నుండి 70%", "2% కంటే తక్కువ"],
        "correct_option": 0,
        "explanation_en": "Telangana accounts for over 35% of national pharmaceutical production and about one-third of the country's bulk drug exports.",
        "explanation_te": "దేశవ్యాప్తంగా తయారయ్యే బల్క్ డ్రగ్స్ మరియు ఔషధ ఎగుమతులలో మూడో వంతుకు పైగా (35%) వాటాను తెలంగాణ అందిస్తూ ఔషధ రాజధానిగా నిలిచింది."
    },
    {
        "id": 177,
        "section": "General Studies",
        "topic": "Telangana Economy - IT Sector",
        "question_en": "Which premier industrial corridor in western Hyderabad serves as the primary hub for IT/ITeS services and software exports from Telangana?",
        "question_te": "తెలంగాణ సాఫ్ట్‌వేర్ ఎగుమతులు మరియు ఐటీ రంగానికి ప్రధాన కేంద్రంగా ఉన్న హైదరాబాద్‌లోని ప్రముఖ ఐటీ కారిడార్ ఏది?",
        "options_en": ["HITEC City (Madhapur - Gachibowli cluster)", "Maheswaram Hardware Park", "Cherlapally Industrial Estate", "Nacharam Industrial Area"],
        "options_te": ["హైటెక్ సిటీ (మాదాపూర్ - గచ్చిబౌలి క్లస్టర్)", "మహేశ్వరం హార్డ్‌వేర్ పార్క్", "చర్లపల్లి ఇండస్ట్రియల్ ఎస్టేట్", "నాచారం పారిశ్రామిక వాడ"],
        "correct_option": 0,
        "explanation_en": "HITEC City and the Financial District (Gachibowli-Madhapur) form the core of Telangana's IT exports, employing over 900,000 technology professionals.",
        "explanation_te": "హైటెక్ సిటీ మరియు ఫైనాన్షియల్ డిస్ట్రిక్ట్ తెలంగాణ రాష్ట్ర ఐటీ ఎగుమతులకు అంతర్జాతీయ వేదికగా నిలుస్తున్నాయి."
    },
    {
        "id": 178,
        "section": "General Studies",
        "topic": "Telangana Economy - Agriculture & Irrigation",
        "question_en": "The flagship programme 'Mission Kakatiya' was undertaken by the Government of Telangana for the restoration of:",
        "question_te": "తెలంగాణ ప్రభుత్వం ప్రతిష్టాత్మకంగా చేపట్టిన 'మిషన్ కాకతీయ' కార్యక్రమం దేని పునరుద్ధరణ కోసం ఉద్దేశించబడింది?",
        "options_en": ["Chain of traditional minor irrigation tanks and ponds", "Canal dredging of Krishna river", "Solar pump installations in drylands", "Underground drainage systems in municipalities"],
        "options_te": ["సాంప్రదాయ గొలుసుకట్టు చెరువులు మరియు కుంటల పునరుద్ధరణ", "కృష్ణా నది కాలువల పూడికతీత", "రైతులకు సోలార్ పంపుల పంపిణీ", "పట్టణాల్లో భూగర్భ మురుగునీటి పారుదల"],
        "correct_option": 0,
        "explanation_en": "Mission Kakatiya (Mana Ooru - Mana Cheruvu) aimed at de-silting and restoring over 46,000 minor irrigation tanks across villages in Telangana.",
        "explanation_te": "కాకతీయుల కాలం నాటి గొలుసుకట్టు చెరువుల్లో పూడికతీసి, భూగర్భ జలాల పెంపునకు చేపట్టిన బృహత్తర పథకమే 'మిషన్ కాకతీయ'."
    },
    {
        "id": 179,
        "section": "General Studies",
        "topic": "Telangana Economy - Drinking Water",
        "question_en": "Which project was implemented in Telangana to provide safe treated surface drinking water via tap connection to every rural household?",
        "question_te": "తెలంగాణలోని ప్రతి గ్రామీణ గృహానికి నల్లా ద్వారా స్వచ్ఛమైన శుద్ధి చేసిన తాగునీటిని అందించడానికి చేపట్టిన ప్రాజెక్టు ఏది?",
        "options_en": ["Mission Bhagiratha", "Mission Kakatiya", "Jal Jeevan Telangana", "Palamuru Lift Irrigation"],
        "options_te": ["మిషన్ భగీరథ (Mission Bhagiratha)", "మిషన్ కాకతీయ", "జల్ జీవన్ తెలంగాణ", "పాలమూరు ఎత్తిపోతల"],
        "correct_option": 0,
        "explanation_en": "Mission Bhagiratha is a dedicated drinking water grid project providing piped potable drinking water from Godavari and Krishna reservoirs to every household.",
        "explanation_te": "గోదావరి, కృష్ణా నదుల జలాలను శుద్ధి చేసి పైప్‌లైన్ల గ్రిడ్ ద్వారా ప్రతి ఇంటికీ తాగునీరు అందించే పథకమే 'మిషన్ భగీరథ'."
    },
    {
        "id": 180,
        "section": "General Studies",
        "topic": "Indian Economy - Planning & NITI Aayog",
        "question_en": "NITI Aayog (National Institution for Transforming India) replaced the Planning Commission on which date?",
        "question_te": "భారత ప్రణాళికా సంఘం (Planning Commission) స్థానంలో 'నీతి ఆయోగ్' (NITI Aayog) ఎప్పుడు ఏర్పాటయింది?",
        "options_en": ["1 January 2015", "15 August 2014", "1 April 2016", "26 January 2015"],
        "options_te": ["1 జనవరి 2015 (1 January 2015)", "15 ఆగస్టు 2014", "1 ఏప్రిల్ 2016", "26 జనవరి 2015"],
        "correct_option": 0,
        "explanation_en": "NITI Aayog was formed on 1 January 2015 via a Union Cabinet resolution, serving as the premier policy think tank for cooperative federalism.",
        "explanation_te": "కేంద్ర కేబినెట్ తీర్మానం ద్వారా పాత ప్రణాళికా సంఘం స్థానంలో 2015 జనవరి 1వ తేదీన నీతి ఆయోగ్ ఏర్పాటయింది."
    },

    # =========================================================================
    # 7. TELANGANA HISTORY, SOCIETY, CULTURE, HERITAGE, ARTS (Q181 - Q190)
    # =========================================================================
    {
        "id": 181,
        "section": "General Studies",
        "topic": "Telangana History - Satavahanas",
        "question_en": "The early capital of the Satavahana dynasty, where Roman coins and coins of King Chimuka were excavated, is located at:",
        "question_te": "రోమన్ నాణేలు మరియు మొదటి శాతవాహన రాజు శ్రీముఖుని నాణేలు బయల్పడిన శాతవాహనుల తొలి రాజధాని ప్రదేశం ఏది?",
        "options_en": ["Kotilingala (Jagtial district)", "Dhanyakataka", "Pratishthanapura", "Nelakondapalli"],
        "options_te": ["కోటిలింగాల (జగిత్యాల జిల్లా)", "ధాన్యకటకం", "ప్రతిష్ఠానపురం (పైఠాన్)", "నేలకొండపల్లి"],
        "correct_option": 0,
        "explanation_en": "Kotilingala on the banks of river Godavari in present Jagtial district was the earliest capital of the Satavahanas under King Simuka.",
        "explanation_te": "జగిత్యాల జిల్లా గోదావరి తీరాన ఉన్న కోటిలింగాల వద్ద శాతవాహన వంశ స్థాపకుడైన శ్రీముఖుని నాణేలు లభించాయి. ఇది వారి తొలి రాజధాని."
    },
    {
        "id": 182,
        "section": "General Studies",
        "topic": "Telangana History - Kakatiyas",
        "question_en": "Which famous Italian traveler visited the Kakatiya kingdom during the reign of Queen Rudrama Devi and lavishly praised her governance and Warangal's prosperity?",
        "question_te": "కాకతీయ రాణి రుద్రమదేవి పాలనా కాలంలో ఓరుగల్లును సందర్శించి, ఆమె పరిపాలనా దక్షతను మరియు రాజ్య సంపదను ప్రశంసించిన ఇటాలియన్ యాత్రికుడు ఎవరు?",
        "options_en": ["Marco Polo", "Nicolo de Conti", "Ibn Battuta", "Domingo Paes"],
        "options_te": ["మార్కో పోలో (Marco Polo)", "నికోలో డి కాంటి", "ఇబన్ బటూటా", "డొమింగో పేస్"],
        "correct_option": 0,
        "explanation_en": "Venetian traveler Marco Polo visited the Kakatiya port city of Motupalli and the kingdom in 1292–1293 CE, praising Rani Rudrama Devi's justice and the finest muslins.",
        "explanation_te": "ఇటలీకి చెందిన వెనీస్ యాత్రికుడు మార్కో పోలో మోటుపల్లి రేవు ద్వారా కాకతీయ రాజ్యాన్ని సందర్శించి రాణి రుద్రమదేవి పాలనను కొనియాడారు."
    },
    {
        "id": 183,
        "section": "General Studies",
        "topic": "Telangana History - Qutb Shahis",
        "question_en": "The iconic monument 'Charminar' in Hyderabad was constructed in 1591 CE by which Qutb Shahi Sultan to commemorate the eradication of plague?",
        "question_te": "హైదరాబాద్ నగరంలోని ప్రసిద్ధ 'చార్మినార్' ను ప్లేగు వ్యాధి నిర్మూలనకు చిహ్నంగా 1591 లో నిర్మించిన కుతుబ్‌షాహీ సుల్తాన్ ఎవరు?",
        "options_en": ["Muhammad Quli Qutb Shah", "Sultan Quli Qutb Shah", "Ibrahim Qutb Shah", "Abdullah Qutb Shah"],
        "options_te": ["మహ్మద్ కులీ కుతుబ్ షా (Muhammad Quli Qutb Shah)", "సుల్తాన్ కులీ కుతుబ్ షా", "ఇబ్రహీం కుతుబ్ షా", "అబ్దుల్లా కుతుబ్ షా"],
        "correct_option": 0,
        "explanation_en": "Muhammad Quli Qutb Shah, the 5th Sultan of the dynasty and founder of Hyderabad city, constructed the Charminar in 1591 CE.",
        "explanation_te": "హైదరాబాద్ నగర నిర్మాత అయిన 5వ కుతుబ్‌షాహీ సుల్తాన్ మహ్మద్ కులీ కుతుబ్ షా 1591 లో చార్మినార్‌ను నిర్మించారు."
    },
    {
        "id": 184,
        "section": "General Studies",
        "topic": "Telangana History - Asaf Jahis",
        "question_en": "Who established the premier higher educational institution 'Osmania University' in Hyderabad in 1917?",
        "question_te": "1917 లో హైదరాబాద్‌లో ప్రఖ్యాత 'ఉస్మానియా విశ్వవిద్యాలయం' (Osmania University) ను స్థాపించిన నిజాం పాలకుడు ఎవరు?",
        "options_en": ["Mir Osman Ali Khan (Nizam VII)", "Mahbub Ali Khan (Nizam VI)", "Afzal-ud-Daulah (Nizam V)", "Nasir-ud-Daulah (Nizam IV)"],
        "options_te": ["మీర్ ఉస్మాన్ అలీ ఖాన్ (7వ నిజాం)", "మహబూబ్ అలీ ఖాన్ (6వ నిజాం)", "అఫ్జల్ ఉద్-దౌలా", "నాసిర్ ఉద్-దౌలా"],
        "correct_option": 0,
        "explanation_en": "Mir Osman Ali Khan, the 7th and last Nizam of Hyderabad, established Osmania University via a royal firman in 1917.",
        "explanation_te": "హైదరాబాద్ 7వ నిజాం అయిన మీర్ ఉస్మాన్ అలీ ఖాన్ 1917 లో జారీ చేసిన ఫర్మానా ద్వారా ఉస్మానియా విశ్వవిద్యాలయం ఏర్పాటయింది."
    },
    {
        "id": 185,
        "section": "General Studies",
        "topic": "Telangana Culture - Festivals",
        "question_en": "The floral festival 'Bathukamma', the cultural identity of Telangana women, is celebrated primarily during which Hindu lunar festival season?",
        "question_te": "తెలంగాణ మహిళల ఆత్మగౌరవ ప్రతీక అయిన పూల పండుగ 'బతుకమ్మ' ప్రధానంగా ఏ నవరాత్రుల కాలంలో జరుపుకుంటారు?",
        "options_en": ["Sharad Navratri (ending on Durgashtami / Saddula Bathukamma)", "Sankranti", "Holi", "Vasantha Navratri"],
        "options_te": ["శరన్నవరాత్రులు (ఎంగిలిపూల బతుకమ్మ నుండి సద్దుల బతుకమ్మ వరకు)", "సంక్రాంతి", "హోలీ పండుగ", "వసంత నవరాత్రులు"],
        "correct_option": 0,
        "explanation_en": "Bathukamma is a 9-day floral festival celebrated during Bhadrapada Amavasya (Mahalaya Amavasya / Engili Pula Bathukamma) to Ashwayuja Ashtami (Saddula Bathukamma).",
        "explanation_te": "భాద్రపద అమావాస్య (ఎంగిలిపూల బతుకమ్మ) నుండి ఆశ్వయుజ అష్టమి (సద్దుల బతుకమ్మ) వరకు 9 రోజుల పాటు ప్రకృతిని, గౌరమ్మను పూజిస్తూ బతుకమ్మను జరుపుకుంటారు."
    },
    {
        "id": 186,
        "section": "General Studies",
        "topic": "Telangana Culture - Jatharas",
        "question_en": "The historic Sammakka-Saralamma Jathara, celebrating tribal valor against Kakatiya feudal taxes, takes place at Medaram in which district?",
        "question_te": "కాకతీయుల అన్యాయపు పన్నులకు వ్యతిరేకంగా వీరోచిత పోరాటం చేసిన గిరిజన వీరవనితల స్మృత్యర్థం జరిగే 'సమ్మక్క-సారలమ్మ మేడారం జాతర' ఏ జిల్లాలో జరుగుతుంది?",
        "options_en": ["Mulugu district", "Khammam district", "Adilabad district", "Nalgonda district"],
        "options_te": ["ములుగు జిల్లా (Mulugu)", "ఖమ్మం జిల్లా", "ఆదిలాబాద్ జిల్లా", "నల్గొండ జిల్లా"],
        "correct_option": 0,
        "explanation_en": "Medaram Jathara is celebrated biennially in the forests of Medaram, Tadvai mandal of Mulugu district, attracting over a crore devotees.",
        "explanation_te": "ఆసియాలోనే అతిపెద్ద గిరిజన జాతరగా గుర్తింపు పొందిన సమ్మక్క-సారలమ్మ జాతర ములుగు జిల్లా తాడ్వాయి మండలంలోని మేడారంలో రెండేళ్లకొకసారి జరుగుతుంది."
    },
    {
        "id": 187,
        "section": "General Studies",
        "topic": "Telangana Arts - Dance",
        "question_en": "Which ancient martial dance form of the Kakatiya warrior era, revived by Nataraja Ramakrishna, is known as the warrior dance of Telangana?",
        "question_te": "కాకతీయుల కాలం నాటి యుద్ధ నృత్య రీతిగా ప్రసిద్ధి చెంది, నటరాజ రామకృష్ణ గారి కృషి వల్ల పునరుజ్జీవనం పొందిన తెలంగాణ సాంప్రదాయ నృత్యం ఏది?",
        "options_en": ["Perini Sivatandavam", "Kuchipudi", "Bharatanatyam", "Gussadi"],
        "options_te": ["పేరిణి శివతాండవం (Perini Sivatandavam)", "కూచిపూడి", "భరతనాట్యం", "గుస్సాడీ నృత్యం"],
        "correct_option": 0,
        "explanation_en": "Perini Sivatandavam is an ancient dance of Telangana performed by male warriors in Kakatiya times before entering the battlefield to invoke Lord Shiva.",
        "explanation_te": "రామప్ప శిల్పాల ఆధారంగా డాక్టర్ నటరాజ రామకృష్ణ పునరుద్ధరించిన కాకతీయుల కాలం నాటి పురుషుల వీర నృత్యమే 'పేరిణి శివతాండవం'."
    },
    {
        "id": 188,
        "section": "General Studies",
        "topic": "Telangana Literature - Great Poets",
        "question_en": "Who penned the inspiring revolutionary line: 'నా తెలంగాణ కోటి రతనాల వీణ' (Na Telangana Koti Rathanala Veena)?",
        "question_te": "'నా తెలంగాణ కోటి రతనాల వీణ' అనే చారిత్రాత్మక విప్లవ నినాదాత్మక గేయాన్ని రచించిన తెలంగాణ మహాకవి ఎవరు?",
        "options_en": ["Dasarathi Krishnamacharyulu", "Kaloji Narayana Rao", "Vattikota Alwarswamy", "Suravaram Pratapa Reddy"],
        "options_te": ["దాశరథి కృష్ణమాచార్యులు (Dasarathi)", "కాళోజీ నారాయణరావు", "వట్టికోట ఆళ్వారుస్వామి", "సురవరం ప్రతాపరెడ్డి"],
        "correct_option": 0,
        "explanation_en": "Mahakavi Dasarathi Krishnamacharyulu wrote 'Na Telangana Koti Rathanala Veena' in Nizam's prison at Indur (Nizamabad) fort.",
        "explanation_te": "నిజాం జైలు గోడలపై బొగ్గుతో 'నా తెలంగాణ కోటి రతనాల వీణ' అని రాసిన విప్లవ కవి దాశరథి కృష్ణమాచార్యులు."
    },
    {
        "id": 189,
        "section": "General Studies",
        "topic": "Telangana Literature - Praja Kavi",
        "question_en": "The birth anniversary of which renowned people's poet ('Praja Kavi') on September 9 is celebrated as 'Telangana Bhasha Dinotsavam' (Language Day)?",
        "question_te": "సెప్టెంబర్ 9వ తేదీన ఎవరి జయంతిని పురస్కరించుకుని తెలంగాణ ప్రభుత్వం 'తెలంగాణ భాషా దినోత్సవం' గా అధికారికంగా నిర్వహిస్తుంది?",
        "options_en": ["Kaloji Narayana Rao", "Bammera Pothana", "Palgukuriki Somanatha", "C. Narayana Reddy"],
        "options_te": ["కాళోజీ నారాయణరావు (Kaloji)", "బమ్మెర పోతన", "పాల్కురికి సోమనాథుడు", "సి. నారాయణ రెడ్డి"],
        "correct_option": 0,
        "explanation_en": "The birth anniversary of Padma Vibhushan Kaloji Narayana Rao on 9 September is celebrated as Telangana Language Day in honor of his literary and democratic contribution.",
        "explanation_te": "'పుట్టుక నీది చావు నీది బతుకంతా దేశానిది' అని చాటిన ప్రజాకవి కాళోజీ నారాయణరావు జన్మదినమైన సెప్టెంబర్ 9ని 'తెలంగాణ భాషా దినోత్సవం' గా జరుపుకుంటారు."
    },
    {
        "id": 190,
        "section": "General Studies",
        "topic": "Telangana Heritage - GI Tags",
        "question_en": "Which famous tie-and-dye weaving cluster of Yadadri Bhuvanagiri district earned the first Geographical Indication (GI) tag in Telangana for its geometric design sarees?",
        "question_te": "ప్రత్యేకమైన 'టై అండ్ డై' (ఇక్కత్) పద్ధతిలో తయారయ్యే నేత చీరలకు తెలంగాణ నుండి తొలిసారిగా భౌగోళిక గుర్తింపు (GI Tag) పొందిన ప్రసిద్ధ పట్టణం ఏది?",
        "options_en": ["Pochampally (Pochampally Ikat)", "Gadwal", "Narayanpet", "Siddipet Gollabhama"],
        "options_te": ["పోచంపల్లి ఇక్కత్ (Pochampally)", "గద్వాల", "నారాయణపేట", "సిద్దిపేట గొల్లభామ"],
        "correct_option": 0,
        "explanation_en": "Pochampally Ikat received India's first textile Geographical Indication (GI) status in 2004 for its traditional double ikat geometric designs.",
        "explanation_te": "యాదాద్రి భువనగిరి జిల్లాలోని భూదాన్ పోచంపల్లి ఇక్కత్ వస్త్రాలకు 2004 లో మొట్టమొదటి భౌగోళిక గుర్తింపు (GI Tag) లభించింది."
    },

    # =========================================================================
    # 8. TELANGANA MOVEMENT & STATE FORMATION (Q191 - Q200)
    # =========================================================================
    {
        "id": 191,
        "section": "General Studies",
        "topic": "Telangana Movement - Integration",
        "question_en": "The Indian military action codenamed 'Operation Polo' that led to the accession of Hyderabad State into the Indian Union concluded on which date?",
        "question_te": "హైదరాబాద్ సంస్థానం భారతదేశంలో విలీనం కావడానికి కారణమైన 'ఆపరేషన్ పోలో' సైనిక చర్య ఏ తేదీన ముగిసింది?",
        "options_en": ["17 September 1948", "15 August 1947", "26 January 1950", "1 November 1956"],
        "options_te": ["17 సెప్టెంబర్ 1948 (17 September 1948)", "15 ఆగస్టు 1947", "26 జనవరి 1950", "1 నవంబర్ 1956"],
        "correct_option": 0,
        "explanation_en": "Operation Polo ended on 17 September 1948 when the Nizam's commander-in-chief Major General El Edroos surrendered to Indian forces led by Major General J.N. Chaudhuri.",
        "explanation_te": "1948 సెప్టెంబర్ 13న ప్రారంభమైన ఆపరేషన్ పోలో పోలీస్ చర్య సెప్టెంబర్ 17న నిజాం సైన్యం లొంగిపోవడంతో ముగిసింది. ఆ రోజున హైదరాబాద్ సంస్థానం భారత్‌లో విలీనమైంది."
    },
    {
        "id": 192,
        "section": "General Studies",
        "topic": "Telangana Movement - 1952 Mulki Agitation",
        "question_en": "During the 1952 Mulki agitation in Hyderabad against the appointment of non-locals, four protesters were killed in police firing at which iconic educational institution on 3 September 1952?",
        "question_te": "1952 ముల్కీ ఉద్యమ సమయంలో స్థానికేతరుల నియామకాలకు వ్యతిరేకంగా శాంతియుతంగా నిరసన తెలుపుతున్న విద్యార్థులపై సెప్టెంబర్ 3, 1952 న పోలీసులు కాల్పులు జరిపిన విద్యాసంస్థ ఏది?",
        "options_en": ["City College, Hyderabad", "Nizam College", "Chaderghat High School", "Vivek Vardhini College"],
        "options_te": ["సిటీ కాలేజ్, హైదరాబాద్ (City College)", "నిజాం కాలేజ్", "చాదర్‌ఘాట్ హైస్కూల్", "వివేక్ వర్ధిని కాలేజ్"],
        "correct_option": 0,
        "explanation_en": "The City College firing incident occurred on 3 September 1952 during the 'Ghair-Mulki Go Back' protests, sparking a judicial inquiry under Justice Pingali Jaganmohan Reddy.",
        "explanation_te": "1952 సెప్టెంబర్ 3న సిటీ కాలేజీ వద్ద నిరసన తెలుపుతున్న వారిపై పోలీసులు జరిపిన కాల్పుల్లో నలుగురు విద్యార్థులు మరణించారు. దీనిపై జస్టిస్ జగన్మోహన్ రెడ్డి కమిషన్ ఏర్పాటయింది."
    },
    {
        "id": 193,
        "section": "General Studies",
        "topic": "Telangana Movement - States Reorganisation Commission",
        "question_en": "What did the States Reorganisation Commission (SRC / Fazal Ali Commission) recommend in 1955 regarding Telangana?",
        "question_te": "1955 లో ఫజల్ అలీ నేతృత్వంలోని రాష్ట్రాల పునర్వ్యవస్థీకరణ కమిషన్ (SRC) తెలంగాణ ప్రాంతం గురించి ఏ సిఫార్సు చేసింది?",
        "options_en": ["Telangana should be maintained as a separate State (Hyderabad State) initially for at least 5 years", "Immediate unconditional merger with Andhra State", "Division of Telangana among neighbouring four states", "Creation of a Union Territory"],
        "options_te": ["తెలంగాణను కనీసం 5 సంవత్సరాల పాటు ప్రత్యేక రాష్ట్రంగా కొనసాగించాలి, ఆపై 2/3 మెజారిటీ ఉంటేనే విలీనం చేయాలి", "ఎటువంటి షరతులు లేకుండా వెంటనే ఆంధ్రతో కలపాలి", "తెలంగాణను నాలుగు పొరుగు రాష్ట్రాలకు పంచాలి", "కేంద్రపాలిత ప్రాంతంగా మార్చాలి"],
        "correct_option": 0,
        "explanation_en": "Paragraphs 386–389 of the SRC Report explicitly cautioned against immediate merger and recommended Telangana remain a separate state for at least 5 years.",
        "explanation_te": "ఫజల్ అలీ కమిషన్ తెలంగాణ ఆర్థికంగా స్వయం సమృద్ధి కలిగి ఉందని, కనీసం 5 ఏళ్లపాటు ప్రత్యేక హైదరాబాద్ రాష్ట్రంగానే ఉంచి శాసనసభ 2/3 వంతు కోరితేనే విలీనం చేయాలని సిఫార్సు చేసింది."
    },
    {
        "id": 194,
        "section": "General Studies",
        "topic": "Telangana Movement - Gentlemen's Agreement",
        "question_en": "The 'Gentlemen's Agreement' safeguarding Telangana's interests prior to the formation of Andhra Pradesh was signed on 20 February 1956 at which venue?",
        "question_te": "ఆంధ్రప్రదేశ్ అవతరణకు ముందు తెలంగాణ హక్కుల రక్షణ కోసం ఫిబ్రవరి 20, 1956 న 'పెద్దమనుషుల ఒప్పందం' (Gentlemen's Agreement) ఎక్కడ జరిగింది?",
        "options_en": ["Hyderabad House, New Delhi", "Raj Bhavan, Hyderabad", "Rashtrapati Nilayam", "Kurnool Guest House"],
        "options_te": ["హైదరాబాద్ హౌస్, న్యూఢిల్లీ (Hyderabad House, New Delhi)", "రాజ్ భవన్, హైదరాబాద్", "రాష్ట్రపతి నిలయం, సికింద్రాబాద్", "కర్నూలు అతిథి గృహం"],
        "correct_option": 0,
        "explanation_en": "The Gentlemen's Agreement was signed at Hyderabad House in New Delhi on 20 February 1956 by 4 leaders each from Telangana and Andhra regions.",
        "explanation_te": "1956 ఫిబ్రవరి 20న ఢిల్లీలోని హైదరాబాద్ హౌస్‌లో తెలంగాణ మరియు ఆంధ్ర ప్రాంతాల నుండి నలుగురేసి చొప్పున మొత్తం 8 మంది పెద్దమనుషులు ఈ ఒప్పందంపై సంతకాలు చేశారు."
    },
    {
        "id": 195,
        "section": "General Studies",
        "topic": "Telangana Movement - 1969 Agitation",
        "question_en": "The 1969 separate Telangana agitation started in January 1969 with an indefinite hunger strike undertaken by student Ravindranath at which town?",
        "question_te": "1969 ప్రత్యేక తెలంగాణ ఉద్యమానికి నాంది పలికిన విద్యార్థి రవీంద్రనాథ్ ఆమరణ నిరాహార దీక్ష ఏ పట్టణంలో ప్రారంభమైంది?",
        "options_en": ["Khammam", "Warangal", "Hyderabad", "Nalgonda"],
        "options_te": ["ఖమ్మం (Khammam)", "వరంగల్", "హైదరాబాద్", "నల్గొండ"],
        "correct_option": 0,
        "explanation_en": "On 8 January 1969, an undergraduate student named Annabathula Ravindranath went on a fast-unto-death in Khammam demanding implementation of Telangana safeguards.",
        "explanation_te": "1969 జనవరి 8న ఖమ్మం గాంధీ చౌక్ వద్ద అన్నాబత్తుల రవీంద్రనాథ్ తెలంగాణ రక్షణల అమలు కోరుతూ ఆమరణ నిరాహార దీక్ష ప్రారంభించడంతో 1969 ఉద్యమం మొదలైంది."
    },
    {
        "id": 196,
        "section": "General Studies",
        "topic": "Telangana Movement - Political Phase",
        "question_en": "In the 1971 parliamentary general elections, the Telangana Praja Samithi (TPS) led by Dr. M. Channa Reddy contested on a separate Telangana plank and won how many Lok Sabha seats?",
        "question_te": "1971 లోక్‌సభ ఎన్నికల్లో ప్రత్యేక తెలంగాణే ధ్యేయంగా పోటీ చేసిన డాక్టర్ మర్రి చెన్నారెడ్డి నేతృత్వంలోని 'తెలంగాణ ప్రజా సమితి' (TPS) ఎన్ని సీట్లు గెలుచుకుంది?",
        "options_en": ["10 out of 14 seats", "5 out of 14 seats", "14 out of 14 seats", "2 out of 14 seats"],
        "options_te": ["14 లో 10 లోక్‌సభ స్థానాలు (10 out of 14 seats)", "5 స్థానాలు", "14 స్థానాలు", "2 స్థానాలు"],
        "correct_option": 0,
        "explanation_en": "The Telangana Praja Samithi swept the 1971 elections by winning 10 out of the total 14 Lok Sabha seats in the Telangana region, demonstrating overwhelming mass support.",
        "explanation_te": "తెలంగాణలోని మొత్తం 14 లోక్‌సభ స్థానాల్లో 10 స్థానాలను తెలంగాణ ప్రజా సమితి భారీ మెజారిటీతో కైవసం చేసుకుని తెలంగాణ ప్రజాభిప్రాయాన్ని చాటిచెప్పింది."
    },
    {
        "id": 197,
        "section": "General Studies",
        "topic": "Telangana Movement - Presidential Order",
        "question_en": "Which Article was inserted into the Constitution of India via the 32nd Amendment Act in 1973 to implement the Six-Point Formula in Andhra Pradesh?",
        "question_te": "1973 లో ఆరు సూత్రాల పథకం (Six-Point Formula) అమలు కోసం 32వ రాజ్యాంగ సవరణ ద్వారా భారత రాజ్యాంగంలో చేర్చబడిన ఆర్టికల్ ఏది?",
        "options_en": ["Article 371-D", "Article 370", "Article 371-A", "Article 356"],
        "options_te": ["ఆర్టికల్ 371-D (Article 371-D)", "ఆర్టికల్ 370", "ఆర్టికల్ 371-A", "ఆర్టికల్ 356"],
        "correct_option": 0,
        "explanation_en": "Article 371-D provided special provisions for equitable opportunities in public employment and education across different regions of Andhra Pradesh, leading to the 1975 Presidential Order.",
        "explanation_te": "ఆరు సూత్రాల పథకం అమలు కోసం 371-D అధికరణాన్ని రాజ్యాంగంలో చేర్చారు. దీని ఆధారంగానే 1975 రాష్ట్రపతి ఉత్తర్వులు (జోనల్ వ్యవస్థ) జారీ అయ్యాయి."
    },
    {
        "id": 198,
        "section": "General Studies",
        "topic": "Telangana Movement - Final Phase",
        "question_en": "On which historic date did the Union Home Minister P. Chidambaram make the announcement that 'the process of forming the state of Telangana will be initiated'?",
        "question_te": "కేంద్ర హోంమంత్రి పి. చిదంబరం 'ప్రత్యేక తెలంగాణ రాష్ట్ర ఏర్పాటు ప్రక్రియను ప్రారంభిస్తున్నాం' అని చారిత్రాత్మక ప్రకటన ఏ రోజు రాత్రి చేశారు?",
        "options_en": ["9 December 2009", "29 November 2009", "23 December 2009", "2 June 2014"],
        "options_te": ["9 డిసెంబర్ 2009 (9 December 2009)", "29 నవంబర్ 2009", "23 డిసెంబర్ 2009", "2 జూన్ 2014"],
        "correct_option": 0,
        "explanation_en": "Following K. Chandrashekar Rao's 11-day fast-unto-death and massive statewide student mobilization, Union Home Minister P. Chidambaram announced the statehood decision on midnight of 9 December 2009.",
        "explanation_te": "కెసిఆర్ చేపట్టిన ఆమరణ నిరాహార దీక్షకు మద్దతుగా ఉద్యమం ఉధృతమవడంతో 2009 డిసెంబర్ 9 అర్ధరాత్రి కేంద్ర ప్రభుత్వం తెలంగాణ ప్రక్రియను ప్రారంభిస్తున్నట్లు ప్రకటించింది."
    },
    {
        "id": 199,
        "section": "General Studies",
        "topic": "Telangana Movement - Mass Agitations",
        "question_en": "The historic 'Million March' organized by the Telangana Joint Action Committee (TJAC) on Tank Bund in Hyderabad took place on:",
        "question_te": "తెలంగాణ జేఏసీ (TJAC) ఆధ్వర్యంలో హైదరాబాద్ ట్యాంక్ బండ్ పై నిర్వహించిన చారిత్రాత్మక 'మిలియన్ మార్చ్' ఏ రోజున జరిగింది?",
        "options_en": ["10 March 2011", "9 December 2009", "30 September 2012", "19 October 2013"],
        "options_te": ["10 మార్చి 2011 (10 March 2011)", "9 డిసెంబర్ 2009", "30 సెప్టెంబర్ 2012", "19 అక్టోబర్ 2013"],
        "correct_option": 0,
        "explanation_en": "The Million March (inspired by Cairo's Tahrir Square) was held on 10 March 2011 on Tank Bund, defying police barricades and curfew.",
        "explanation_te": "ఈజిప్ట్ విప్లవం స్ఫూర్తితో 2011 మార్చి 10వ తేదీన లక్షలాది మంది ప్రజలు ఆంక్షలను ఛేదించి ట్యాంక్ బండ్‌పై 'మిలియన్ మార్చ్' నిర్వహించారు."
    },
    {
        "id": 200,
        "section": "General Studies",
        "topic": "Telangana State Formation - Appointed Day",
        "question_en": "On which 'Appointed Day' did Telangana officially come into existence as the 29th State of the Republic of India?",
        "question_te": "భారత గణతంత్రంలో 29వ రాష్ట్రంగా తెలంగాణ అధికారికంగా ఆవిర్భవించిన 'నియమిత దినం' (Appointed Day) ఏది?",
        "options_en": ["2 June 2014", "18 February 2014", "1 March 2014", "15 August 2014"],
        "options_te": ["2 జూన్ 2014 (2 June 2014)", "18 ఫిబ్రవరి 2014", "1 మార్చి 2014", "15 ఆగస్టు 2014"],
        "correct_option": 0,
        "explanation_en": "Under the Andhra Pradesh Reorganisation Act, 2014, the central government notified 2 June 2014 as the 'Appointed Day' marking the official birth of Telangana state.",
        "explanation_te": "ఆంధ్రప్రదేశ్ పునర్వ్యవస్థీకరణ చట్టం 2014 ప్రకారం కేంద్ర ప్రభుత్వం 2014 జూన్ 2వ తేదీని నియమిత దినంగా ప్రకటించడంతో తెలంగాణ నూతన రాష్ట్రంగా ఆవిర్భవించింది."
    }
]

# Balance correct option distribution across GS questions (A, B, C, D)
for idx, q in enumerate(gs_questions):
    target_idx = (idx * 3 + 1) % 4
    cur_idx = q["correct_option"]
    if cur_idx != target_idx:
        q["options_en"][cur_idx], q["options_en"][target_idx] = q["options_en"][target_idx], q["options_en"][cur_idx]
        q["options_te"][cur_idx], q["options_te"][target_idx] = q["options_te"][target_idx], q["options_te"][cur_idx]
        q["correct_option"] = target_idx

# Combine all 200 questions:
all_200_questions = base_100_questions + gs_questions

print(f"Total Combined Questions: {len(all_200_questions)}")

os.makedirs('public/data', exist_ok=True)
output_path = 'public/data/mock_test_full_200.json'

payload = {
    "testId": "tsplrb-si-mock-full-200",
    "title": "TSPLRB SI Prelims Full-Length Mock Test (200 Questions)",
    "title_te": "తెలంగాణ ఎస్సై ప్రిలిమ్స్ పూర్తి స్థాయి మాక్ టెస్ట్ (200 ప్రశ్నలు)",
    "exam": "Telangana State Police Sub-Inspector (SI) Preliminary Written Test",
    "paper": "Paper I & II Complete Pattern: Arithmetic, Reasoning & General Studies",
    "totalQuestions": 200,
    "totalMarks": 200,
    "durationMinutes": 180,
    "marksPerQuestion": 1.0,
    "negativeMarking": 0.20,
    "sections": [
        {"id": "arithmetic", "name": "Part A: Arithmetic", "start": 1, "end": 50, "count": 50},
        {"id": "reasoning", "name": "Part B: Reasoning & Mental Ability", "start": 51, "end": 100, "count": 50},
        {"id": "general_studies", "name": "Part C: General Studies", "start": 101, "end": 200, "count": 100}
    ],
    "questions": all_200_questions
}

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"✅ Generated {len(all_200_questions)} verified questions in {output_path}")
