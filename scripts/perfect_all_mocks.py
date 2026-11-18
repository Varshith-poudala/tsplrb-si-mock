import json

# Curated Telangana History & Statehood Movement Questions (12 Qs)
tsm_curated = [
    (
        "Which renowned Prakrit poetic anthology of 700 verses depicting ancient Deccan rural life was composed by Satavahana King Hala?",
        "ప్రాచీన దక్కన్ గ్రామీణ జీవనాన్ని ప్రతిబింబించే 700 శృంగార పద్యాల ప్రాకృత సంకలనం 'గాథా సప్తశతి'ని ఏ శాతవాహన రాజు రచించాడు?",
        ["Brihatkatha", "Gatha Saptasati (గాథా సప్తశతి)", "Lilavati", "Kavyamimamsa"],
        ["బృహత్కథ", "గాథా సప్తశతి (Gatha Saptasati)", "లీలావతి", "కావ్యమీమాంస"],
        1,
        "King Hala, the 17th Satavahana ruler, compiled the celebrated Gatha Saptasati in Maharashtri Prakrit.",
        "శాతవాహన రాజు హాలుడు ప్రాకృత భాషలో గాథా సప్తశతిని రచించాడు."
    ),
    (
        "Which famous Kakatiya sea-trade charter granting protection and customs relief to foreign merchant ships was issued by King Ganapati Deva at Motupalli port?",
        "విదేశీ వర్తక నౌకలకు రక్షణ మరియు సుంకాల రాయితీలను కల్పిస్తూ కాకతీయ చక్రవర్తి గణపతి దేవుడు మోటుపల్లి రేవు వద్ద జారీ చేసిన ప్రసిద్ధ శాసనం ఏది?",
        ["Chandupatla Inscription", "Motupalli Abhaya Sasanam (మోటుపల్లి అభయ శాసనం)", "Bayyaram Inscription", "Malkapuram Inscription"],
        ["చందుపట్ల శాసనం", "మోటుపల్లి అభయ శాసనం (Motupalli Abhaya Sasanam)", "బయ్యారం శాసనం", "మల్కాపురం శాసనం"],
        1,
        "The Motupalli Abhaya Sasanam of Ganapati Deva granted royal protection (Abhaya) to seafaring traders, promoting Kakatiya foreign trade.",
        "కాకతీయ గణపతి దేవుడు విదేశీ వర్తకుల రక్షణ కోసం మోటుపల్లి రేవు వద్ద అభయ శాసనాన్ని వేయించాడు."
    ),
    (
        "Who built the historic 'Charminar' in Hyderabad in 1591 AD to commemorate the cessation of a deadly plague epidemic?",
        "1591 లో ప్లేగు వ్యాధి నిర్మూలనకు గుర్తుగా హైదరాబాద్‌లో చారిత్రక 'చార్మినార్' ను నిర్మించినది ఎవరు?",
        ["Sultan Quli Qutb Shah", "Ibrahim Qutb Shah", "Muhammad Quli Qutb Shah", "Abdullah Qutb Shah"],
        ["సుల్తాన్ కులీ కుతుబ్ షా", "ఇబ్రహీం కుతుబ్ షా", "మహమ్మద్ కులీ కుతుబ్ షా (Muhammad Quli Qutb Shah)", "అబ్దుల్లా కుతుబ్ షా"],
        2,
        "Muhammad Quli Qutb Shah, the 5th Sultan of Golconda and founder of Hyderabad, constructed Charminar in 1591.",
        "హైదరాబాద్ నగర నిర్మాత మహమ్మద్ కులీ కుతుబ్ షా 1591 లో చార్మినార్ నిర్మించాడు."
    ),
    (
        "Who was the Prime Minister (Diwan) of Hyderabad State who introduced the 'Zilabandi' administrative reform in 1865?",
        "1865 లో హైదరాబాద్ రాజ్యంలో పరిపాలనా సౌలభ్యం కోసం 'జిలాబందీ' రెవెన్యూ సంస్కరణను ప్రవేశపెట్టిన ప్రధాని (దివాన్) ఎవరు?",
        ["Salar Jung I (Mir Turab Ali Khan)", "Salar Jung II", "Maharaja Kishen Pershad", "Mir Alam"],
        ["మొదటి సాలార్ జంగ్ (Salar Jung I)", "రెండవ సాలార్ జంగ్", "మహారాజా కిషన్ ప్రసాద్", "మీర్ ఆలం"],
        0,
        "Nawab Mir Turab Ali Khan (Salar Jung I) reorganized the Nizam's dominions into regular districts (Zilabandi) under Subedars and Taluqdars.",
        "మొదటి సాలార్ జంగ్ 1865 లో రాష్ట్రాన్ని సుబాలు, జిల్లాలుగా విభజిస్తూ జిలాబందీ సంస్కరణలను అమలు చేశాడు."
    ),
    (
        "The traditional folk floral festival 'Bathukamma', worshiping nature and Goddess Gauri, concludes on which auspicious day with 'Pedda Bathukamma' (Saddula Bathukamma)?",
        "తెలంగాణ సంస్కృతికి ప్రతీక అయిన 'బతుకమ్మ' పండుగ ఏ పర్వదినం నాడు 'సద్దుల బతుకమ్మ' (పెద్ద బతుకమ్మ) తో ముగుస్తుంది?",
        ["Mahalaya Amavasya (Engili Pula Bathukamma)", "Durgashtami / Mahanavami", "Vijayadasami", "Deepavali"],
        ["మహాలయ అమావాస్య (ఎంగిలిపూల బతుకమ్మ)", "దుర్గాష్టమి / మహర్నవమి (Durgashtami / Saddula Bathukamma)", "విజయదశమి", "దీపావళి"],
        1,
        "Bathukamma begins on Mahalaya Amavasya (Engili Pula Bathukamma) and concludes after 9 days on Durgashtami/Ashwayuja Ashtami with Saddula Bathukamma.",
        "బతుకమ్మ పండుగ 9 రోజుల పాటు జరిగి దుర్గాష్టమి నాడు సద్దుల బతుకమ్మతో ఘనంగా ముగుస్తుంది."
    ),
    (
        "On which date did the Nizam of Hyderabad formally surrender his armed forces to Indian Commander Major General J.N. Chaudhuri, concluding 'Operation Polo'?",
        "ఏ తేదీన నిజాం సైన్యం భారత మేజర్ జనరల్ జె.ఎన్. చౌధురికి లొంగిపోవడంతో 'ఆపరేషన్ పోలో' ముగిసి హైదరాబాద్ రాష్ట్రం భారత్‌లో విలీనమైంది?",
        ["13th September 1948", "17th September 1948", "26th January 1950", "1st November 1956"],
        ["13 సెప్టెంబర్ 1948", "17 సెప్టెంబర్ 1948 (17 September 1948)", "26 జనవరి 1950", "1 నవంబర్ 1956"],
        1,
        "On 17 September 1948, Nizam Mir Osman Ali Khan announced surrender on Deccan Radio, ending the police action Operation Polo.",
        "17 సెప్టెంబర్ 1948న నిజాం సైన్యాలు లొంగిపోవడంతో హైదరాబాద్ సంస్థానం భారత యూనియన్‌లో విలీనమైంది."
    ),
    (
        "The 1952 Non-Mulki Agitation ('Idli Sambar Go Back') began in which town of southern Telangana over the illegal appointment of non-local teachers?",
        "స్థానికేతరుల అక్రమ నియామకాలకు వ్యతిరేకంగా 1952 లో 'నాన్-ముల్కీ ఉద్యమం' దక్షిణ తెలంగాణలోని ఏ పట్టణంలో ప్రారంభమైంది?",
        ["Warangal (Hanamkonda)", "Khammam", "Mahabubnagar", "Nizamabad"],
        ["వరంగల్ (హనుమకొండ)", "ఖమ్మం", "మహబూబ్‌నగర్", "నిజామాబాద్"],
        0,
        "The 1952 Mulki agitation started in Hanamkonda/Warangal in July 1952 protesting the transfer of non-mulki teachers by Divisional Inspector of Schools.",
        "1952 ముల్కీ ఉద్యమం హనుమకొండ/వరంగల్ లో ఉపాధ్యాయుల బదిలీలకు వ్యతిరేకంగా విద్యార్థుల ఆందోళనతో మొదలైంది."
    ),
    (
        "Which commission appointed by the Government of India in 1953 recommended that the Telangana region should initially remain as a separate State of Hyderabad?",
        "1953 లో కేంద్రం నియమించిన ఏ కమిషన్ తెలంగాణ ప్రాంతాన్ని తొలుత ప్రత్యేక హైదరాబాద్ రాష్ట్రంగానే ఉంచాలని సిఫార్సు చేసింది?",
        ["Dhar Commission", "JVP Committee", "States Reorganisation Commission (Fazal Ali Commission)", "Wanchoo Committee"],
        ["ధార్ కమిషన్", "జెవిపి కమిటీ", "ఫజల్ అలీ కమిషన్ (States Reorganisation Commission)", "వాంచూ కమిటీ"],
        2,
        "The Fazal Ali Commission (SRC 1955) in Para 386 recommended retaining Telangana as a separate state, giving it the option to merge after 5 years with a 2/3rd majority.",
        "ఫజల్ అలీ నేతృత్వంలోని రాష్ట్రాల పునర్వ్యవస్థీకరణ కమిషన్ తెలంగాణను ప్రత్యేక రాష్ట్రంగానే కొనసాగించాలని స్పష్టంగా సిఫార్సు చేసింది."
    ),
    (
        "How many key safeguards for Telangana region were agreed upon and signed under the 'Gentlemen's Agreement' on 20th February 1956 in New Delhi?",
        "20 ఫిబ్రవరి 1956న న్యూఢిల్లీలో కుదిరిన 'పెద్దమనుషుల ఒప్పందం' లో తెలంగాణ రక్షణల కోసం ఎన్ని ప్రధాన అంశాలపై సంతకాలు చేశారు?",
        ["8 safeguards", "10 safeguards", "14 safeguards", "16 safeguards"],
        ["8 రక్షణలు", "10 రక్షణలు", "14 రక్షణలు (14 Safeguards)", "16 రక్షణలు"],
        2,
        "The Gentlemen's Agreement signed at Hyderabad House contained 14 specific safeguards relating to Telangana Regional Committee, ministers, revenues, and education.",
        "పెద్దమనుషుల ఒప్పందంలో తెలంగాణ ప్రయోజనాల కోసం 14 రక్షణలతో కూడిన నిబంధనలను పొందుపరిచారు."
    ),
    (
        "Which All-Party Accord was formulated on 19th January 1969 to safeguard non-mulki repatriations and ensure utilization of Telangana surplus revenues?",
        "తెలంగాణ మిగులు నిధుల వినియోగం మరియు స్థానికేతరుల వెనక్కి పంపడంపై 19 జనవరి 1969న ముఖ్యమంత్రి కాసు బ్రహ్మానంద రెడ్డి ఆధ్వర్యంలో జరిగిన ఒప్పందం ఏది?",
        ["Eight-Point Formula", "All-Party Accord (సర్వపార్టీ ఒప్పందం - G.O. 36)", "Six-Point Formula", "Five-Point Formula"],
        ["ఎనిమిది సూత్రాల పథకం", "సర్వపార్టీ ఒప్పందం (All-Party Accord - G.O. 36)", "ఆరు సూత్రాల పథకం", "ఐదు సూత్రాల పథకం"],
        1,
        "The All-Party Accord reached on 19 January 1969 agreed to repatriate non-mulki employees by 28 Feb 1969, leading to the issuance of G.O. 36.",
        "19 జనవరి 1969న కుదిరిన సర్వపార్టీ ఒప్పందం ఆధారంగానే ప్రభుత్వం వివాదాస్పద జీవో 36ను జారీ చేసింది."
    ),
    (
        "Under which Prime Minister was the 'Six-Point Formula' formulated in September 1973, leading to the enactment of Article 371D and Presidential Order 1975?",
        "సెప్టెంబర్ 1973 లో 'ఆరు సూత్రాల పథకం' (Six-Point Formula) ఏ ప్రధానమంత్రి హయాంలో రూపొందించబడి అధికరణం 371D కి దారితీసింది?",
        ["Jawaharlal Nehru", "Indira Gandhi", "Lal Bahadur Shastri", "Morarji Desai"],
        ["జవహర్‌లాల్ నెహ్రూ", "ఇందిరా గాంధీ (Indira Gandhi)", "లాల్ బహదూర్ శాస్త్రి", "మొరార్జీ దేశాయ్"],
        1,
        "Prime Minister Indira Gandhi introduced the Six-Point Formula in 1973, which was incorporated into the Constitution via the 32nd Amendment Act (Article 371D).",
        "ఇందిరా గాంధీ ప్రభుత్వం 1973 లో ఆరు సూత్రాల పథకాన్ని తెచ్చి 32వ రాజ్యాంగ సవరణ ద్వారా అధికరణం 371D ని చేర్చింది."
    ),
    (
        "Under Section 3 of the Andhra Pradesh Reorganisation Act, 2014, how many parliamentary Lok Sabha constituencies were allocated to the newly formed State of Telangana?",
        "ఆంధ్రప్రదేశ్ పునర్వ్యవస్థీకరణ చట్టం, 2014 ప్రకారం నూతన తెలంగాణ రాష్ట్రానికి ఎన్ని లోక్‌సభ నియోజకవర్గాలు కేటాయించబడ్డాయి?",
        ["14 Lok Sabha seats", "17 Lok Sabha seats", "20 Lok Sabha seats", "25 Lok Sabha seats"],
        ["14 లోక్‌సభ స్థానాలు", "17 లోక్‌సభ స్థానాలు (17 Lok Sabha Seats)", "20 లోక్‌సభ స్థానాలు", "25 లోక్‌సభ స్థానాలు"],
        1,
        "The AP Reorganisation Act 2014 allocated 17 Lok Sabha seats and 7 Rajya Sabha seats to Telangana.",
        "2014 పునర్వ్యవస్థీకరణ చట్టం ప్రకారం తెలంగాణకు 17 లోక్‌సభ మరియు 7 రాజ్యసభ స్థానాలు కేటాయించబడ్డాయి."
    )
]

def make_q_dict(topic, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
    return {
        "section": "General Studies",
        "topic": topic,
        "question_en": q_en.strip(),
        "question_te": q_te.strip(),
        "options_en": opts_en,
        "options_te": opts_te,
        "correct_option": corr,
        "explanation_en": exp_en.strip(),
        "explanation_te": exp_te.strip()
    }

# Fix Mock 6 and Mock 7 Q189-Q200 with tsm_curated
for fname in ['mock_test_full_200_6.json', 'mock_test_full_200_7.json']:
    with open(f'public/data/{fname}') as f:
        data = json.load(f)
    qs = data['questions']
    for idx, tq in enumerate(tsm_curated):
        q_num = 189 + idx
        qs[188 + idx] = {
            "id": q_num,
            "qNumber": q_num,
            "section": "General Studies",
            "topic": "Telangana History, Culture & State Formation Movement",
            "question_en": tq[0],
            "question_te": tq[1],
            "options_en": tq[2],
            "options_te": tq[3],
            "correct_option": tq[4],
            "explanation_en": tq[5],
            "explanation_te": tq[6]
        }
    with open(f'public/data/{fname}', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Fixed {fname} Q189-Q200 with Telangana Movement questions.")

# Fix Mock 3 Q101-114 science topic labels
with open('public/data/mock_test_full_200_3.json') as f:
    d3 = json.load(f)
for i in range(100, 114):
    d3['questions'][i]['topic'] = 'General Science & Everyday Technology'
with open('public/data/mock_test_full_200_3.json', 'w', encoding='utf-8') as f:
    json.dump(d3, f, ensure_ascii=False, indent=2)

print("All mock files polished successfully!")
