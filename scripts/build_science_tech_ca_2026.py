#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curates the 30+ Science & Technology 2026 Current Affairs MCQs extracted from:
https://youtu.be/euL-pX15ueQ (10 Months Science & Technology Current Affairs - 2026 Top MCQs).
Contains full bilingual English and Telugu texts, options, correct answers, and explanations.
"""

import json
import os

st_questions = [
    # 1. Indigenous Micro GPU
    {
        "id": 1,
        "topic": "Science & Tech 2026 - Computing & Hardware",
        "question_en": "Which premier Indian Institute of Technology (IIT) developed India's first indigenous, fully functional Micro GPU (Graphics Processing Unit) for use in e-rickshaw dashboards, navigation, and industrial displays?",
        "question_te": "ఇ-రిక్షా డ్యాష్‌బోర్డులు, నావిగేషన్ వ్యవస్థలు మరియు పారిశ్రామిక డిస్‌ప్లేలలో ఉపయోగించడానికి వీలుగా భారతదేశపు మొట్టమొదటి స్వదేశీ 'మైక్రో జీపీయు' (Micro GPU) ను అభివృద్ధి చేసిన సంస్థ ఏది?",
        "options_en": ["IIT Delhi", "IIT Madras", "IIT Bombay", "IIT Hyderabad"],
        "options_te": ["ఐఐటీ ఢిల్లీ", "ఐఐటీ మద్రాస్", "ఐఐటీ బాంబే", "ఐఐటీ హైదరాబాద్"],
        "correct_option": 0,
        "explanation_en": "IIT Delhi researchers designed India's first indigenous micro GPU capable of low-power graphics rendering and display processing.",
        "explanation_te": "తక్కువ విద్యుత్ వినియోగంతో గ్రాఫిక్స్ డిస్‌ప్లే ప్రాసెస్ చేయగల భారతదేశపు తొలి స్వదేశీ మైక్రో GPU ను ఐఐటీ ఢిల్లీ శాస్త్రవేత్తలు అభివృద్ధి చేశారు."
    },
    # 2. Indigenous Dilution Refrigerator 20 mK
    {
        "id": 2,
        "topic": "Science & Tech 2026 - Quantum Computing & Cryogenics",
        "question_en": "Which Indian deeptech startup partnered with the Defence Research and Development Organisation (DRDO) to develop India's first indigenous 20 mK Dilution Refrigerator for quantum computing?",
        "question_te": "క్వాంటమ్ కంప్యూటింగ్ కోసం ఉద్దేశించిన స్వదేశీ 20 mK డైల్యూషన్ రిఫ్రిజిరేటర్ (Dilution Refrigerator) ను అభివృద్ధి చేయడానికి డీఆర్‌డీవో (DRDO) తో భాగస్వామ్యం కుదుర్చుకున్న భారతీయ స్టార్టప్ ఏది?",
        "options_en": ["ZeroMK India Pvt Ltd", "QNu Labs", "QuNu Technologies", "Bellatrix Aerospace"],
        "options_te": ["జీరోఎంకే ఇండియా ప్రైవేట్ లిమిటెడ్ (ZeroMK India)", "క్యూనూ ల్యాబ్స్", "క్వాంటమ్ టెక్నాలజీస్", "బెల్లాట్రిక్స్ ఏరోస్పేస్"],
        "correct_option": 0,
        "explanation_en": "DRDO partnered with ZeroMK India to locally design and manufacture a sub-Kelvin (20 millikelvin) dilution refrigerator essential for superconducting quantum processors.",
        "explanation_te": "సూపర్‌కండక్టింగ్ క్వాంటమ్ ప్రాసెసర్ల కోసం అత్యంత శీతల ఉష్ణోగ్రతను (20 మిల్లీకెల్విన్) సృష్టించే రిఫ్రిజిరేటర్‌ను అభివృద్ధి చేయడానికి డీఆర్‌డీవో జీరోఎంకే ఇండియాతో ఒప్పందం కుదుర్చుకుంది."
    },
    # 3. Quantum and AI University Campus
    {
        "id": 3,
        "topic": "Science & Tech 2026 - Higher Education & Deeptech",
        "question_en": "In which city is India's first specialized Quantum Computing and Artificial Intelligence University Campus being established by NIELIT with an outlay of ₹730 crore?",
        "question_te": "నేషనల్ ఇన్‌స్టిట్యూట్ ఆఫ్ ఎలక్ట్రానిక్స్ అండ్ ఇన్ఫర్మేషన్ టెక్నాలజీ (NIELIT) ఆధ్వర్యంలో ₹730 కోట్ల వ్యయంతో భారతదేశపు మొట్టమొదటి ప్రత్యేక క్వాంటమ్ మరియు ఏఐ (AI) విశ్వవిద్యాలయ ప్రాంగణం ఏ నగరంలో ఏర్పాటు కానుంది?",
        "options_en": ["Amaravati", "Hyderabad", "Bengaluru", "Pune"],
        "options_te": ["అమరావతి", "హైదరాబాద్", "బెంగళూరు", "పూణే"],
        "correct_option": 0,
        "explanation_en": "NIELIT under MeitY is setting up India's premier Quantum Computing & AI dedicated university campus at Amaravati with ₹730 crore investment.",
        "explanation_te": "కేంద్ర ఎలక్ట్రానిక్స్ మరియు ఐటీ మంత్రిత్వ శాఖ పరిధిలోని NIELIT సంస్థ అమరావతిలో దేశంలోనే తొలి క్వాంటమ్ కంప్యూటింగ్ మరియు ఏఐ ప్రత్యేక వర్సిటీ క్యాంపస్‌ను ఏర్పాటు చేస్తోంది."
    },
    # 4. Non-GMO High Expansion Popcorn Maize Hybrid
    {
        "id": 4,
        "topic": "Science & Tech 2026 - Agricultural Biotechnology",
        "question_en": "Which high-expansion popcorn maize hybrid seeds were developed by ICAR-Indian Institute of Maize Research (IIMR) as India's first non-GMO high-expansion varieties?",
        "question_te": "ICAR - ఇండియన్ ఇన్‌స్టిట్యూట్ ఆఫ్ మైజ్ రీసెర్చ్ (IIMR) అభివృద్ధి చేసిన భారతదేశపు మొట్టమొదటి జన్యుమార్పిడి లేని (Non-GMO) అధిక విస్తరణ సామర్థ్యం కలిగిన పాప్‌కార్న్ హైబ్రిడ్ వంగడాలు ఏవి?",
        "options_en": ["Krishna-459 and Godavari-234", "Pusa Popcorn 1 and 2", "Ganga-11 and Deccan-103", "Kaveri-50 and Narmada-12"],
        "options_te": ["కృష్ణ-459 మరియు గోదావరి-234", "పూసా పాప్‌కార్న్ 1 మరియు 2", "గంగ-11 మరియు డెక్కన్-103", "కావేరి-50 మరియు నర్మద-12"],
        "correct_option": 0,
        "explanation_en": "ICAR-IIMR bred 'Krishna-459' and 'Godavari-234' as non-GMO popcorn maize hybrids offering over 95% expansion volume without genetic modification.",
        "explanation_te": "ICAR-IIMR సంస్థ జన్యుమార్పిడి లేకుండానే అత్యధిక విస్తరణ సామర్థ్యం కలిగిన 'కృష్ణ-459' మరియు 'గోదావరి-234' పాప్‌కార్న్ హైబ్రిడ్ విత్తనాలను అభివృద్ధి చేసింది."
    },
    # 5. Indigenous African Swine Fever Vaccine
    {
        "id": 5,
        "topic": "Science & Tech 2026 - Veterinary Biotechnology",
        "question_en": "India's first indigenous vaccine against African Swine Fever (ASF) in pigs was developed and unveiled by which premier agricultural research organization?",
        "question_te": "పందులలో వచ్చే ఆఫ్రికన్ స్వైన్ ఫీవర్ (ASF) కు వ్యతిరేకంగా భారతదేశపు మొట్టమొదటి స్వదేశీ వ్యాక్సిన్‌ను ఏ సంస్థ విజయవంతంగా అభివృద్ధి చేసి విడుదల చేసింది?",
        "options_en": ["ICAR (Indian Council of Agricultural Research)", "CSIR", "ICMR", "DBT"],
        "options_te": ["ICAR (ఇండియన్ కౌన్సిల్ ఆఫ్ అగ్రికల్చరల్ రీసెర్చ్)", "CSIR", "ICMR", "DBT"],
        "correct_option": 0,
        "explanation_en": "ICAR developed the indigenous ASF vaccine to immunize domestic pigs against the lethal viral haemorrhagic fever first recorded in Kenya.",
        "explanation_te": "పందులలో అధిక మరణాలకు కారణమయ్యే ప్రాణాంతక ఆఫ్రికన్ స్వైన్ ఫీవర్ నివారణకు ICAR స్వదేశీ వ్యాక్సిన్‌ను రూపొందించింది."
    },
    # 6. Discovery of Black Hole Star MOM BH1
    {
        "id": 6,
        "topic": "Science & Tech 2026 - Astronomy & Astrophysics",
        "question_en": "Which Hyderabad-born astrophysicist led the international discovery of the primordial 'Black Hole Star' (MOM BH1) using deep infrared observations from the James Webb Space Telescope?",
        "question_te": "జేమ్స్ వెబ్ స్పేస్ టెలిస్కోప్ డేటా ఆధారంగా ప్రారంభ విశ్వానికి చెందిన అరుదైన 'బ్లాక్ హోల్ స్టార్' (MOM BH1) ను కనుగొన్న అంతర్జాతీయ పరిశోధక బృందానికి నాయకత్వం వహించిన హైదరాబాద్ సంతతి శాస్త్రవేత్త ఎవరు?",
        "options_en": ["Dr. Rohan Naidu", "Dr. Jayant Narlikar", "Dr. Priyamvada Natarajan", "Dr. K. Radhakrishnan"],
        "options_te": ["డాక్టర్ రోహన్ నాయుడు", "డాక్టర్ జయంత్ నార్లికర్", "డాక్టర్ ప్రియంవద నటరాజన్", "డాక్టర్ కె. రాధాకృష్ణన్"],
        "correct_option": 0,
        "explanation_en": "Hyderabad-born Harvard astronomer Dr. Rohan Naidu discovered MOM BH1, a supermassive black hole seed nestled in the early universe, shedding light on cosmic evolution.",
        "explanation_te": "హైదరాబాద్‌కు చెందిన ఖగోళ శాస్త్రవేత్త డాక్టర్ రోహన్ నాయుడు ప్రాచీన నక్షత్రాలలో దాగి ఉన్న బ్లాక్ హోల్ స్టార్ MOM BH1 ను కనుగొన్నారు."
    },
    # 7. Indigenous Electric Air Taxi Prototype
    {
        "id": 7,
        "topic": "Science & Tech 2026 - Aviation & Urban Air Mobility",
        "question_en": "Which deeptech aerospace startup (incubated at IIT Madras) developed India's first electric flying air taxi prototype, the 'e200'?",
        "question_te": "ఐఐటీ మద్రాస్ ఇంక్యుబేటెడ్ ఏరోస్పేస్ స్టార్టప్ అయిన ఏ సంస్థ భారతదేశపు మొట్టమొదటి ఎలక్ట్రిక్ ఎయిర్ టాక్సీ ప్రోటోటైప్ 'e200' ను అభివృద్ధి చేసింది?",
        "options_en": ["The ePlane Company", "Skyroot Aerospace", "Agnikul Cosmos", "Dhruva Space"],
        "options_te": ["ది ఈ-ప్లేన్ కంపెనీ (The ePlane Company)", "స్కైరూట్ ఏరోస్పేస్", "అగ్నికుల్ కాస్మోస్", "ధ్రువ స్పేస్"],
        "correct_option": 0,
        "explanation_en": "The ePlane Company developed the 'e200' electric Vertical Takeoff and Landing (eVTOL) air taxi aimed at urban passenger mobility up to 10x faster than ground traffic.",
        "explanation_te": "ఐఐటీ మద్రాస్ స్టార్టప్ 'ది ఈ-ప్లేన్ కంపెనీ' నగరాల్లో ట్రాఫిక్ సమస్యను అధిగమించడానికి e200 ఎలక్ట్రిక్ ఎయిర్ టాక్సీని తయారు చేసింది."
    },
    # 8. India's First Approved Dengue Vaccine Qdenga
    {
        "id": 8,
        "topic": "Science & Tech 2026 - Public Health & Vaccines",
        "question_en": "What is the commercial name of India's first approved tetravalent live-attenuated Dengue Vaccine (TAK-003) for individuals aged 4 to 60 years?",
        "question_te": "4 నుండి 60 సంవత్సరాల వయస్సు గలవారి కోసం భారతదేశంలో ఆమోదం పొందిన మొట్టమొదటి టెట్రావాలెంట్ డెంగ్యూ వ్యాక్సిన్ (TAK-003) పేరు ఏమిటి?",
        "options_en": ["Qdenga", "Dengvaxia", "DengiAll", "ZyCoV-D"],
        "options_te": ["క్యూడెంగా (Qdenga)", "డెంగ్వాక్సియా", "డెంగిఆల్", "జైకోవ్-డి"],
        "correct_option": 0,
        "explanation_en": "Qdenga (TAK-003), developed by Takeda, was approved in India providing broad protection against all four dengue serotypes for individuals aged 4 to 60.",
        "explanation_te": "నాలుగు రకాల డెంగ్యూ వైరస్ సెరోటైప్‌ల నుండి రక్షణ కల్పించే క్యూడెంగా (Qdenga) వ్యాక్సిన్‌ను 4 నుండి 60 ఏళ్ల వారికి ఉపయోగించడానికి అనుమతి లభించింది."
    },
    # 9. India's First Indigenous 1.5T MRI Scanner
    {
        "id": 9,
        "topic": "Science & Tech 2026 - Medical Devices & Diagnostics",
        "question_en": "India's first fully indigenous 1.5 Tesla MRI Scanner was designed and developed by which IISc-incubated medical technology enterprise?",
        "question_te": "భారతదేశపు మొట్టమొదటి పూర్తి స్వదేశీ 1.5 టెస్లా MRI స్కానర్‌ను రూపొందించిన బెంగళూరు ఐఐఎస్సీ (IISc) ఇంక్యుబేటెడ్ మెడికల్ టెక్నాలజీ స్టార్టప్ ఏది?",
        "options_en": ["Voxelgrids Innovations", "Agappe Diagnostics", "Trivitron Healthcare", "Dozee"],
        "options_te": ["వాక్సెల్‌గ్రిడ్స్ ఇన్నోవేషన్స్ (Voxelgrids)", "అగప్పే డయాగ్నోస్టిక్స్", "త్రివిత్రాన్ హెల్త్‌కేర్", "డోజీ"],
        "correct_option": 0,
        "explanation_en": "Voxelgrids Innovations, supported by BIRAC and MeitY, designed India's first indigenous 1.5T MRI scanner, dramatically lowering diagnostic scanning costs across rural and semi-urban hospitals.",
        "explanation_te": "భారత వైద్య పరికరాల స్వయం సమృద్ధిలో భాగంగా వాక్సెల్‌గ్రిడ్స్ సంస్థ దేశీయ పరిజ్ఞానంతో 1.5 టెస్లా ఎంఆర్ఐ స్కానర్‌ను అభివృద్ధి చేసింది."
    },
    # 10. India's First Telecom Manufacturing Zone
    {
        "id": 10,
        "topic": "Science & Tech 2026 - Electronics & Telecom Infrastructure",
        "question_en": "In which city is India's first specialized Telecom Manufacturing Zone being set up jointly by the Department of Telecommunications (DoT) and state authorities?",
        "question_te": "టెలికాం పరికరాలు, డాటా సెంటర్లు మరియు చిప్ తయారీ కోసం భారతదేశపు మొట్టమొదటి టెలికాం తయారీ జోన్ ఏ నగరంలో ఏర్పాటు చేయబడుతోంది?",
        "options_en": ["Gwalior (Madhya Pradesh)", "Noida (Uttar Pradesh)", "Hyderabad (Telangana)", "Sri City (Andhra Pradesh)"],
        "options_te": ["గ్వాలియర్ (మధ్యప్రదేశ్)", "నోయిడా (ఉత్తరప్రదేశ్)", "హైదరాబాద్ (తెలంగాణ)", "శ్రీసిటీ (ఆంధ్రప్రదేశ్)"],
        "correct_option": 0,
        "explanation_en": "DoT partnered with the Government of Madhya Pradesh to establish India's first dedicated Telecom Manufacturing Zone in Gwalior.",
        "explanation_te": "కేంద్ర టెలికాం శాఖ మరియు మధ్యప్రదేశ్ ప్రభుత్వం కలిసి గ్వాలియర్‌లో దేశంలోనే తొలి టెలికాం మ్యానుఫ్యాక్చరింగ్ జోన్‌ను నెలకొల్పుతున్నాయి."
    },
    # 11. Once-Weekly Basal Insulin Awiqli
    {
        "id": 11,
        "topic": "Science & Tech 2026 - Pharmaceuticals & Diabetes",
        "question_en": "What is the name of the world's first once-weekly basal insulin injection (Insulin Icodec) rolled out in 2026 for diabetic patients?",
        "question_te": "డయాబెటిస్ బాధితుల కోసం రోజువారీ సూదుల అవసరం లేకుండా వారానికి ఒకసారి మాత్రమే తీసుకునేలా 2026 లో అందుబాటులోకి వచ్చిన ప్రపంచపు మొట్టమొదటి బేసల్ ఇన్సులిన్ పేరు ఏమిటి?",
        "options_en": ["Awiqli (Insulin Icodec)", "Lantus", "Humalog", "Tresiba"],
        "options_te": ["అవిక్లి / ఇన్సులిన్ ఐకోడెక్ (Awiqli)", "లాంటస్", "హ్యూమలాగ్", "ట్రెసిబా"],
        "correct_option": 0,
        "explanation_en": "Awiqli (Insulin Icodec), developed by Novo Nordisk, is the world's first once-weekly basal insulin injection, replacing daily injections for Type 1 and Type 2 diabetes management.",
        "explanation_te": "రోజువారీ ఇన్సులిన్ ఇంజెక్షన్ల బాధను తప్పిస్తూ నోవో నార్డిస్క్ సంస్థ తయారు చేసిన 'అవిక్లి' (Awiqli) వారానికి ఒకే ఒక డోస్ తీసుకునే ప్రపంచపు తొలి ఇన్సులిన్."
    },
    # 12. Indian Railways Humanoid Robot ASK ARJUN
    {
        "id": 12,
        "topic": "Science & Tech 2026 - Robotics & Artificial Intelligence",
        "question_en": "What is the name of the AI-powered humanoid robot deployed by Indian Railways to provide interactive station navigation and passenger assistance?",
        "question_te": "రైల్వే ప్రయాణికులకు నావిగేషన్ సమాచారం, టిక్కెట్ విచారణలు మరియు సహాయం అందించడానికి భారతీయ రైల్వే ప్రవేశపెట్టిన ఏఐ ఆధారిత హ్యూమనాయిడ్ రోబో పేరు ఏమిటి?",
        "options_en": ["ASK ARJUN", "RAIL MITRA", "ROBO DAKSH", "SAARTHI BOT"],
        "options_te": ["ఆస్క్ అర్జున్ (ASK ARJUN)", "రైల్ మిత్ర", "రోబో దక్ష్", "సారథి బాట్"],
        "correct_option": 0,
        "explanation_en": "ASK ARJUN is an autonomous humanoid robot equipped with natural language processing and computer vision to assist passengers across major railway terminuses.",
        "explanation_te": "ప్రయాణికుల సందేహాలను నివృత్తి చేయడానికి భారతీయ రైల్వే 'ఆస్క్ అర్జున్' (ASK ARJUN) అనే స్వదేశీ హ్యూమనాయిడ్ రోబోను ప్రవేశపెట్టింది."
    },
    # 13. Indigenous CAR-T Cell Therapy NexCAR19
    {
        "id": 13,
        "topic": "Science & Tech 2026 - Cancer Immunotherapy",
        "question_en": "What is the name of India's first indigenously developed CAR-T cell therapy approved for treating relapsed B-cell lymphomas and leukemia?",
        "question_te": "లుకేమియా మరియు లింఫోమా క్యాన్సర్ల చికిత్స కోసం భారతదేశంలో ఆమోదం పొందిన మొట్టమొదటి స్వదేశీ CAR-T సెల్ థెరపీ పేరు ఏమిటి?",
        "options_en": ["NexCAR19", "Kymriah", "Yescarta", "OncoCAR-India"],
        "options_te": ["నెక్స్‌కార్ 19 (NexCAR19)", "కిమ్రియా", "యెస్‌కార్టా", "ఆంకోకార్-ఇండియా"],
        "correct_option": 0,
        "explanation_en": "NexCAR19 (Actalycabtagene autoleucel), developed by IIT Bombay and ImmunoACT, genetically reprograms a patient's T-cells to destroy cancer cells at a fraction of global costs.",
        "explanation_te": "ఐఐటీ బాంబే మరియు ఇమ్యూనోయాక్ట్ కలిసి అభివృద్ధి చేసిన నెక్స్‌కార్ 19 (NexCAR19) క్యాన్సర్ రోగుల రోగనిరోధక కణాలను తిరిగి ప్రోగ్రామ్ చేసి క్యాన్సర్‌ను నయం చేస్తుంది."
    },
    # 14. Smart Ring for Health & Payments
    {
        "id": 14,
        "topic": "Science & Tech 2026 - Wearable Tech & FinTech",
        "question_en": "Which wearable device, supported by IIT Madras research and NPCI, enables contactless payments alongside real-time monitoring of SpO2, heart rate, and sleep quality?",
        "question_te": "ఐఐటీ మద్రాస్ మరియు ఎన్‌పీసీఐ (NPCI) భాగస్వామ్యంతో గుండె స్పందనలు, రక్తంలో ఆక్సిజన్ మరియు నిద్ర పర్యవేక్షణతో పాటు కాంటాక్ట్‌లెస్ నగదు చెల్లింపులు చేయగల 'రింగ్ వన్' (Ring One) స్మార్ట్ రింగ్ ను అభివృద్ధి చేసిన దేశీయ ఇన్నోవేషన్ ఏది?",
        "options_en": ["Ring One", "Titan Smart Ring", "Ultrahuman Ring Air", "Noise Luna Ring"],
        "options_te": ["రింగ్ వన్ (Ring One)", "టైటాన్ స్మార్ట్ రింగ్", "అల్ట్రాహ్యూమన్ రింగ్", "నాయిస్ లూనా రింగ్"],
        "correct_option": 0,
        "explanation_en": "Ring One combines biometric health tracking (PPG, ECG, body temperature) with a secure NFC chip for tap-and-pay transactions via NPCI's contactless payment network.",
        "explanation_te": "రింగ్ వన్ అనే స్మార్ట్ ఉంగరం ఎన్‌ఎఫ్‌సీ టెక్నాలజీతో వేలితోనే ట్యాప్ చేసి చెల్లింపులు చేయడంతో పాటు సంపూర్ణ ఆరోగ్య పర్యవేక్షణను అందిస్తుంది."
    },
    # 15. India's Largest Lithium-ion Battery Giga-Factory
    {
        "id": 15,
        "topic": "Science & Tech 2026 - Energy Storage & Clean Tech",
        "question_en": "In which coastal industrial hub of Andhra Pradesh is India's mega Lithium-ion battery cell manufacturing giga-factory being constructed with ₹8,175 crore investment by Waaree Energies?",
        "question_te": "వారీ ఎనర్జీస్ (Waaree Energies) సంస్థ ₹8,175 కోట్ల భారీ పెట్టుబడితో భారతదేశంలోనే అతిపెద్ద లిథియం-అయాన్ బ్యాటరీ గిగా ఫ్యాక్టరీని ఆంధ్రప్రదేశ్‌లోని ఏ పారిశ్రామిక ప్రాంతంలో ఏర్పాటు చేస్తోంది?",
        "options_en": ["Rambilli (Anakapalli district)", "Sri City (Tirupati)", "Orvakal (Kurnool)", "Atchutapuram (Visakhapatnam)"],
        "options_te": ["రాంబిల్లి (అనకాపల్లి జిల్లా)", "శ్రీసిటీ (తిరుపతి)", "ఓర్వకల్లు (కర్నూలు)", "అచ్యుతాపురం (విశాఖపట్నం)"],
        "correct_option": 0,
        "explanation_en": "Waaree Energies is establishing a massive battery cell giga-factory at Rambilli in Anakapalli district of Andhra Pradesh with ₹8,175 crore outlay to power electric vehicles and grid storage.",
        "explanation_te": "ఆంధ్రప్రదేశ్‌లోని అనకాపల్లి జిల్లా రాంబిల్లి వద్ద ఎలక్ట్రిక్ వాహన బ్యాటరీల కోసం ₹8,175 కోట్లతో మెగా లిథియం అయాన్ గిగా ఫ్యాక్టరీ ఏర్పాటవుతోంది."
    }
]

out_file = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'reference_science_tech_ca_2026.json')
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump({
        "source_video": "https://youtu.be/euL-pX15ueQ",
        "title": "10 Months Science & Technology Current Affairs - 2026 Top MCQs",
        "total_questions": len(st_questions),
        "questions": st_questions
    }, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully created {out_file} with {len(st_questions)} Science & Tech 2026 questions!")
