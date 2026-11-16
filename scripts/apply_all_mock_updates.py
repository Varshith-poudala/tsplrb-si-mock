import json

print("Writing curated 2026 Current Affairs to Mock 3, Mock 4, and Mock 5...")

# =========================================================================
# MOCK TEST 3: Q101 to Q120
# =========================================================================
mock3_questions = [
    {
        "id": 101,
        "section": "General Studies",
        "topic": "Current Affairs - Sports 2026",
        "question_en": "Which state emerged as the overall champion of the inaugural Khelo India Tribal Games 2026?",
        "question_te": "ప్రారంభ 'ఖేలో ఇండియా ట్రైబల్ గేమ్స్ 2026' (Khelo India Tribal Games 2026) లో ఓవరాల్ ఛాంపియన్‌గా నిలిచిన రాష్ట్రం ఏది?",
        "options_en": ["Odisha", "Jharkhand", "Chhattisgarh", "Karnataka"],
        "options_te": ["ఒడిశా", "జార్ఖండ్", "ఛత్తీస్‌గఢ్", "కర్ణాటక"],
        "correct_option": 3,
        "explanation_en": "Karnataka emerged as the overall champion of the 1st Khelo India Tribal Games 2026 hosted by Chhattisgarh. The official mascot was 'Morveer' (symbolizing bravery).",
        "explanation_te": "ఛత్తీస్‌గఢ్‌లో జరిగిన మొదటి ఖేలో ఇండియా ట్రైబల్ గేమ్స్ 2026లో కర్ణాటక ఓవరాల్ ఛాంపియన్‌గా నిలిచింది. అధికారిక చిహ్నం (Mascot) 'మోర్‌వీర్'."
    },
    {
        "id": 102,
        "section": "General Studies",
        "topic": "Current Affairs - Sports & Para Athletics 2026",
        "question_en": "Who became the world's first quadruple amputee (person without all four functional limbs) to win an international gold medal in Para Archery in 2026?",
        "question_te": "పారా ఆర్చరీలో అంతర్జాతీయ స్వర్ణ పతకం సాధించిన ప్రపంచంలోనే మొట్టమొదటి 'క్వాడ్రపుల్ యాంపుటీ' (నాలుగు అవయవాలు లేని క్రీడాకారిణి) ఎవరు?",
        "options_en": ["Payal Nag", "Sheetal Devi", "Deepa Malik", "Avani Lekhara"],
        "options_te": ["పాయల్ నాగ్", "శీతల్ దేవి", "దీపా మాలిక్", "అవని లేఖరా"],
        "correct_option": 0,
        "explanation_en": "Payal Nag, an Indian para archer from Odisha, scripted history by winning gold at the World Archery Para Series in Bangkok, defeating Sheetal Devi in the final.",
        "explanation_te": "ఒడిశాకు చెందిన భారత పారా ఆర్చర్ పాయల్ నాగ్ బ్యాంకాక్‌లో జరిగిన వరల్డ్ ఆర్చరీ పారా సిరీస్‌లో స్వర్ణం గెలిచి సరికొత్త చరిత్ర సృష్టించారు."
    },
    {
        "id": 103,
        "section": "General Studies",
        "topic": "Current Affairs - Sports 2026",
        "question_en": "How many total medals did India win at the 2026 Asian Wrestling Championships held in Bishkek, Kyrgyzstan?",
        "question_te": "కిర్గిజిస్తాన్‌లోని బిష్కెక్‌లో జరిగిన 2026 ఆసియా రెజ్లింగ్ ఛాంపియన్‌షిప్‌లో భారతదేశం మొత్తం ఎన్ని పతకాలు గెలుచుకుంది?",
        "options_en": ["17", "14", "21", "10"],
        "options_te": ["17", "14", "21", "10"],
        "correct_option": 0,
        "explanation_en": "India won 17 medals (2 Gold, 7 Silver, 8 Bronze) finishing 5th in the medal tally. Gold medalists included Sujeet Kalkal (65kg) and Abhimanyou Mandwal (70kg).",
        "explanation_te": "భారత్ మొత్తం 17 పతకాలు (2 స్వర్ణాలు, 7 రజతాలు, 8 కాంస్యాలు) సాధించి పతకాల పట్టికలో 5వ స్థానంలో నిలిచింది."
    },
    {
        "id": 104,
        "section": "General Studies",
        "topic": "Current Affairs - Cricket 2026",
        "question_en": "Who scored the fastest century in T20 World Cup history in 2026 by reaching 100 runs in just 33 balls?",
        "question_te": "కేవలం 33 బంతుల్లోనే శతకం సాధించి T20 ప్రపంచ కప్ చరిత్రలోనే అత్యంత వేగవంతమైన సెంచరీ నమోదు చేసిన బ్యాటర్ ఎవరు?",
        "options_en": ["Glenn Maxwell", "Jos Buttler", "Finn Allen", "Virat Kohli"],
        "options_te": ["గ్లెన్ మాక్స్‌వెల్", "జాస్ బట్లర్", "ఫిన్ అలెన్", "విరాట్ కోహ్లీ"],
        "correct_option": 2,
        "explanation_en": "New Zealand cricketer Finn Allen smashed a century in just 33 balls against South Africa, breaking the record for the fastest century in T20 World Cup history.",
        "explanation_te": "న్యూజిలాండ్ ఓపెనర్ ఫిన్ అలెన్ దక్షిణాఫ్రికాపై 33 బంతుల్లోనే సెంచరీ సాధించి T20 ప్రపంచ కప్ చరిత్రలో సరికొత్త ప్రపంచ రికార్డు సృష్టించాడు."
    },
    {
        "id": 105,
        "section": "General Studies",
        "topic": "Current Affairs - Badminton 2026",
        "question_en": "Who won the Men’s Singles crown at the prestigious All England Open Badminton Championships 2026?",
        "question_te": "ప్రతిష్టాత్మక 'ఆల్ ఇంగ్లాండ్ ఓపెన్ బ్యాడ్మింటన్ 2026' పురుషుల సింగిల్స్ టైటిల్‌ను ఎవరు గెలుచుకున్నారు?",
        "options_en": ["Lin Chun-yi", "Viktor Axelsen", "Lee Zii Jia", "Lakshya Sen"],
        "options_te": ["లిన్ చున్-యి", "విక్టర్ ఆక్సెల్సన్", "లీ జీ జియా", "లక్ష్య సేన్"],
        "correct_option": 0,
        "explanation_en": "Lin Chun-yi of China won the Men’s Singles title at the All England Open 2026, defeating India's Lakshya Sen in the final. Women's singles was won by Wang Zhiyi.",
        "explanation_te": "ఆల్ ఇంగ్లాండ్ ఓపెన్ 2026 పురుషుల సింగిల్స్ ఫైనల్లో భారత స్టార్ షట్లర్ లక్ష్య సేన్‌ను ఓడించి చైనాకు చెందిన లిన్ చున్-యి టైటిల్ కైవసం చేసుకున్నాడు."
    },
    {
        "id": 106,
        "section": "General Studies",
        "topic": "Current Affairs - Cricket 2026",
        "question_en": "Which country won the ICC Under-19 Men’s Cricket World Cup 2026 hosted jointly by Zimbabwe and Namibia?",
        "question_te": "జింబాబ్వే మరియు నమీబియా సంయుక్తంగా ఆతిథ్యమిచ్చిన '2026 ICC అండర్-19 పురుషుల ప్రపంచ కప్'ను ఏ దేశం గెలుచుకుంది?",
        "options_en": ["India", "England", "Australia", "Sri Lanka"],
        "options_te": ["భారతదేశం", "ఇంగ్లాండ్", "ఆస్ట్రేలియా", "శ్రీలంక"],
        "correct_option": 0,
        "explanation_en": "India won their record-extending 6th Under-19 World Cup title by defeating England in the final. Vaibhav Sooryavanshi was named Player of the Series.",
        "explanation_te": "ఫైనల్లో ఇంగ్లాండ్‌ను ఓడించి భారత్ రికార్డు స్థాయిలో 6వ సారి అండర్-19 ప్రపంచ కప్‌ను కైవసం చేసుకుంది. వైభవ్ సూర్యవంశీ ప్లేయర్ ఆఫ్ ది సిరీస్‌గా నిలిచాడు."
    },
    {
        "id": 107,
        "section": "General Studies",
        "topic": "Current Affairs - Motorsport 2026",
        "question_en": "Who scripted history by winning the Chinese Grand Prix 2026 at age 19, becoming the 2nd youngest winner in Formula 1 history?",
        "question_te": "19 సంవత్సరాల వయస్సులో చైనీస్ గ్రాండ్ ప్రిక్స్ 2026 గెలిచి, ఫార్ములా 1 చరిత్రలో రెండవ అతి పిన్న వయస్కుడైన విజేతగా నిలిచినది ఎవరు?",
        "options_en": ["Max Verstappen", "Lewis Hamilton", "Andrea Kimi Antonelli", "Charles Leclerc"],
        "options_te": ["మాక్స్ వెర్‌స్టాపెన్", "లూయిస్ హామిల్టన్", "ఆండ్రియా కిమి ఆంటోనెల్లి", "చార్లెస్ లెక్‌లెర్క్"],
        "correct_option": 2,
        "explanation_en": "Italian sensation Andrea Kimi Antonelli won the Chinese Grand Prix 2026 at 19 years of age, becoming the second-youngest race winner in Formula One history after Max Verstappen.",
        "explanation_te": "ఇటలీకి చెందిన 19 ఏళ్ల రేసర్ ఆండ్రియా కిమి ఆంటోనెల్లి చైనీస్ గ్రాండ్ ప్రిక్స్ 2026 గెలిచి F1 చరిత్రలో రెండో అతి పిన్న వయస్కుడిగా రికార్డుకెక్కాడు."
    },
    {
        "id": 108,
        "section": "General Studies",
        "topic": "Current Affairs - Tennis 2026",
        "question_en": "Who clinched the Men's Singles title at the ATP Delhi Open Tennis Championship 2026?",
        "question_te": "ATP ఢిల్లీ ఓపెన్ టెన్నిస్ ఛాంపియన్‌షిప్ 2026 పురుషుల సింగిల్స్ టైటిల్‌ను ఎవరు గెలుచుకున్నారు?",
        "options_en": ["Stefanos Sakellaridis", "Oliver Crawford", "Jay Clarke", "Rei Sakamoto"],
        "options_te": ["స్టెఫానోస్ సకెల్లారిడిస్", "ఆలివర్ క్రాఫోర్డ్", "జే క్లార్క్", "రే సకమోటో"],
        "correct_option": 0,
        "explanation_en": "Stefanos Sakellaridis of Greece won the Men's Singles trophy at the Delhi Open 2026. India's Siddhant Banthia won the doubles title with Alexander Donski.",
        "explanation_te": "గ్రీస్‌కు చెందిన స్టెఫానోస్ సకెల్లారిడిస్ ఢిల్లీ ఓపెన్ 2026 సింగిల్స్ టైటిల్ గెలుచుకున్నాడు."
    },
    {
        "id": 109,
        "section": "General Studies",
        "topic": "Current Affairs - Cricket 2026",
        "question_en": "Which country won the 2026 ICC Men’s T20 World Cup, clinching their historic 3rd title at Ahmedabad?",
        "question_te": "అహ్మదాబాద్‌లోని నరేంద్ర మోదీ స్టేడియంలో జరిగిన ఫైనల్లో విజయం సాధించి '2026 ICC పురుషుల T20 ప్రపంచ కప్' (3వ టైటిల్) గెలుచుకున్న దేశం ఏది?",
        "options_en": ["Australia", "India", "South Africa", "New Zealand"],
        "options_te": ["ఆస్ట్రేలియా", "భారతదేశం", "దక్షిణాఫ్రికా", "న్యూజిలాండ్"],
        "correct_option": 1,
        "explanation_en": "India won the 2026 ICC Men's T20 World Cup (10th edition) jointly hosted by India and Sri Lanka, defeating New Zealand in the final at Narendra Modi Stadium, Ahmedabad.",
        "explanation_te": "భారత్, శ్రీలంక సంయుక్తంగా నిర్వహించిన 10వ T20 ప్రపంచ కప్ ఫైనల్లో న్యూజిలాండ్‌ను ఓడించి భారత్ 3వ సారి ఛాంపియన్‌గా నిలిచింది."
    },
    {
        "id": 110,
        "section": "General Studies",
        "topic": "Current Affairs - Tennis 2026",
        "question_en": "Who won the Men’s Singles crown at the Australian Open 2026 held in Melbourne?",
        "question_te": "మెల్‌బోర్న్‌లో జరిగిన 'ఆస్ట్రేలియన్ ఓపెన్ 2026' పురుషుల సింగిల్స్ కిరీటాన్ని ఎవరు గెలుచుకున్నారు?",
        "options_en": ["Novak Djokovic", "Daniil Medvedev", "Carlos Alcaraz", "Jannik Sinner"],
        "options_te": ["నొవాక్ జొకోవిచ్", "డానియల్ మెద్వెదేవ్", "కార్లోస్ అల్కరాజ్", "జానిక్ సిన్నర్"],
        "correct_option": 2,
        "explanation_en": "Spain's Carlos Alcaraz captured the Australian Open 2026 Men's Singles title, continuing his remarkable Grand Slam dominance.",
        "explanation_te": "స్పెయిన్ సంచలనం కార్లోస్ అల్కరాజ్ ఆస్ట్రేలియన్ ఓపెన్ 2026 పురుషుల సింగిల్స్ గ్రాండ్‌స్లామ్ టైటిల్‌ను గెలుచుకున్నాడు."
    },
    {
        "id": 111,
        "section": "General Studies",
        "topic": "Current Affairs - Domestic Cricket 2026",
        "question_en": "Which team scripted history by winning their maiden Ranji Trophy championship title in the 2025–26 season?",
        "question_te": "2025–26 సీజన్‌లో మొట్టమొదటిసారిగా ప్రతిష్టాత్మక 'రంజీ ట్రోఫీ' ఛాంపియన్‌షిప్ టైటిల్‌ను కైవసం చేసుకుని చరిత్ర సృష్టించిన జట్టు ఏది?",
        "options_en": ["Vidarbha", "Saurashtra", "Jammu & Kashmir", "Karnataka"],
        "options_te": ["విదర్భ", "సౌరాష్ట్ర", "జమ్మూ & కాశ్మీర్", "కర్ణాటక"],
        "correct_option": 2,
        "explanation_en": "Jammu & Kashmir won their historic first-ever Ranji Trophy title in the 2025–26 domestic cricket season, beating defending champions Mumbai in a stunning upset.",
        "explanation_te": "2025–26 దేశవాళీ సీజన్‌లో జమ్మూ & కాశ్మీర్ చరిత్రలో తొలిసారి రంజీ ట్రోఫీని కైవసం చేసుకుని రికార్డు సృష్టించింది."
    },
    {
        "id": 112,
        "section": "General Studies",
        "topic": "Current Affairs - Global Sports 2026",
        "question_en": "Which country is hosting the 2026 Winter Olympic Games across the cities of Milan and Cortina d'Ampezzo?",
        "question_te": "మిలన్ మరియు కోర్టినా డి'అంపెజ్జో నగరాల్లో 2026 వింటర్ ఒలింపిక్ క్రీడలకు ఆతిథ్యమిస్తున్న దేశం ఏది?",
        "options_en": ["France", "Italy", "Canada", "Switzerland"],
        "options_te": ["ఫ్రాన్స్", "ఇటలీ", "కెనడా", "స్విట్జర్లాండ్"],
        "correct_option": 1,
        "explanation_en": "The XXV Olympic Winter Games (Milano Cortina 2026) are hosted by Italy from 6 to 22 February 2026.",
        "explanation_te": "2026 శీతాకాల ఒలింపిక్స్ (మిలానో కోర్టినా 2026) కు ఇటలీ ఆతిథ్యమిచ్చింది."
    },
    {
        "id": 113,
        "section": "General Studies",
        "topic": "Current Affairs - Football 2026",
        "question_en": "Which team won the 79th National Football Championship for the Santosh Trophy (2025–26)?",
        "question_te": "79వ జాతీయ ఫుట్‌బాల్ ఛాంపియన్‌షిప్ 'సంతోష్ ట్రోఫీ (2025–26)' విజేతగా నిలిచిన జట్టు ఏది?",
        "options_en": ["Services", "Goa", "Kerala", "West Bengal"],
        "options_te": ["సర్వీసెస్", "గోవా", "కేరళ", "పశ్చిమ బెంగాల్"],
        "correct_option": 0,
        "explanation_en": "Services football team clinched the 79th Santosh Trophy title in 2026, defeating Goa in the final match.",
        "explanation_te": "గోవాపై ఫైనల్లో విజయం సాధించి సర్వీసెస్ జట్టు 79వ సంతోష్ ట్రోఫీ టైటిల్‌ను గెలుచుకుంది."
    },
    {
        "id": 114,
        "section": "General Studies",
        "topic": "Current Affairs - Women's Cricket 2026",
        "question_en": "Which team won the 2026 Women’s Premier League (WPL) cricket title, defeating Delhi Capitals in the final?",
        "question_te": "ఫైనల్లో ఢిల్లీ క్యాపిటల్స్‌ను ఓడించి '2026 ఉమెన్స్ ప్రీమియర్ లీగ్ (WPL)' టైటిల్‌ను గెలుచుకున్న జట్టు ఏది?",
        "options_en": ["Royal Challengers Bengaluru (RCB)", "Mumbai Indians", "Gujarat Giants", "UP Warriorz"],
        "options_te": ["రాయల్ ఛాలెంజర్స్ బెంగళూరు (RCB)", "ముంబై ఇండియన్స్", "గుజరాత్ జెయింట్స్", "యూపీ వారియర్స్"],
        "correct_option": 0,
        "explanation_en": "Royal Challengers Bengaluru (RCB) won the 2026 Women's Premier League title, defeating Delhi Capitals in the final.",
        "explanation_te": "రాయల్ ఛాలెంజర్స్ బెంగళూరు (RCB) మహిళల జట్టు ఫైనల్లో ఢిల్లీ క్యాపిటల్స్‌పై విజయం సాధించి 2026 WPL ట్రోఫీని గెలుచుకుంది."
    },
    {
        "id": 115,
        "section": "General Studies",
        "topic": "Current Affairs - Domestic Cricket 2026",
        "question_en": "Which team won the 33rd edition of the prestigious 2025–26 Vijay Hazare Trophy one-day cricket tournament?",
        "question_te": "ప్రతిష్టాత్మక 2025–26 విజయ్ హజారే ట్రోఫీ వన్డే క్రికెట్ టోర్నమెంట్ (33వ ఎడిషన్) విజేతగా నిలిచిన జట్టు ఏది?",
        "options_en": ["Maharashtra", "Karnataka", "Vidarbha", "Delhi"],
        "options_te": ["మహారాష్ట్ర", "కర్ణాటక", "విదర్భ", "ఢిల్లీ"],
        "correct_option": 2,
        "explanation_en": "Vidarbha defeated Saurashtra to lift the 2025–26 Vijay Hazare Trophy. Aman Mokhade was named Player of the Series.",
        "explanation_te": "సౌరాష్ట్రను ఓడించి విదర్భ జట్టు 2025–26 విజయ్ హజారే ట్రోఫీని కైవసం చేసుకుంది. అమన్ మోఖాడే ప్లేయర్ ఆఫ్ ది సిరీస్‌గా నిలిచాడు."
    },
    {
        "id": 116,
        "section": "General Studies",
        "topic": "Current Affairs - Chess 2026",
        "question_en": "Who became India’s 94th Chess Grandmaster in 2026, also becoming the first ever Grandmaster from Assam and Northeast India?",
        "question_te": "2026లో భారతదేశపు 94వ చెస్ గ్రాండ్‌మాస్టర్‌గా మరియు అస్సాం అలాగే ఈశాన్య భారతదేశం నుండి మొట్టమొదటి గ్రాండ్‌మాస్టర్‌గా అవతరించినది ఎవరు?",
        "options_en": ["Aaryan Varshney", "R Praggnanandhaa", "Mayank Chakraborty", "Arjun Erigaisi"],
        "options_te": ["ఆర్యన్ వర్ష్ణేయ్", "ఆర్ ప్రజ్ఞానంద", "మయాంక్ చక్రవర్తి", "అర్జున్ ఎరిగైసి"],
        "correct_option": 2,
        "explanation_en": "Mayank Chakraborty became India's 94th Grandmaster and the first ever GM from Assam and the entire Northeastern region. (93rd was Aarav Dengla; 92nd was Aaryan Varshney).",
        "explanation_te": "అస్సాంకు చెందిన మయాంక్ చక్రవర్తి భారతదేశపు 94వ చెస్ గ్రాండ్‌మాస్టర్‌గా నిలిచారు. మొత్తం ఈశాన్య రాష్ట్రాల నుండి GM అయిన తొలి ఆటగాడు ఈయనే."
    },
    {
        "id": 117,
        "section": "General Studies",
        "topic": "Current Affairs - Domestic Cricket 2026",
        "question_en": "Which state team won their maiden Syed Mushtaq Ali Trophy (SMAT 2025–26) T20 title in 2026?",
        "question_te": "2026లో తమ మొట్టమొదటి సయ్యద్ ముస్తాక్ అలీ ట్రోఫీ (SMAT 2025–26) T20 టైటిల్‌ను గెలుచుకున్న జట్టు ఏది?",
        "options_en": ["Jharkhand", "Mumbai", "Karnataka", "Baroda"],
        "options_te": ["జార్ఖండ్", "ముంబై", "కర్ణాటక", "బరోడా"],
        "correct_option": 0,
        "explanation_en": "Jharkhand won their maiden Syed Mushtaq Ali Trophy (18th edition) by beating Haryana in the final. Anukul Roy was awarded Player of the Tournament.",
        "explanation_te": "ఫైనల్లో హర్యానాను ఓడించి జార్ఖండ్ జట్టు చరిత్రలో తొలిసారి సయ్యద్ ముస్తాక్ అలీ T20 ట్రోఫీని కైవసం చేసుకుంది."
    },
    {
        "id": 118,
        "section": "General Studies",
        "topic": "Current Affairs - Global Reports 2026",
        "question_en": "What is India's rank in the 'World Happiness Report 2026' published by the UN Sustainable Development Solutions Network (SDSN)?",
        "question_te": "ఐక్యరాజ్యసమితి SDSN విడుదల చేసిన 'వరల్డ్ హ్యాపీనెస్ రిపోర్ట్ 2026' (World Happiness Report 2026) లో భారతదేశం ర్యాంక్ ఎంత?",
        "options_en": ["110th", "116th", "120th", "130th"],
        "options_te": ["110వ", "116వ", "120వ", "130వ"],
        "correct_option": 1,
        "explanation_en": "India ranked 116th in the World Happiness Report 2026. Finland ranked 1st as the happiest country for the 8th consecutive year, followed by Iceland and Denmark.",
        "explanation_te": "వరల్డ్ హ్యాపీనెస్ రిపోర్ట్ 2026లో భారత్ 116వ స్థానంలో నిలిచింది. ఫిన్లాండ్ వరుసగా 8వ సారి అగ్రస్థానంలో నిలిచింది."
    },
    {
        "id": 119,
        "section": "General Studies",
        "topic": "Current Affairs - Global Indices 2026",
        "question_en": "What is India’s rank in the 'World Press Freedom Index 2026' published by Reporters Without Borders (RSF)?",
        "question_te": "'రిపోర్టర్స్ వితౌట్ బోర్డర్స్ (RSF)' ప్రచురించిన 'ప్రపంచ పత్రికా స్వేచ్ఛా సూచిక 2026' (World Press Freedom Index 2026) లో భారత్ ర్యాంక్ ఎంత?",
        "options_en": ["120th", "140th", "157th", "170th"],
        "options_te": ["120వ", "140వ", "157వ", "170వ"],
        "correct_option": 2,
        "explanation_en": "India was ranked 157th among 180 countries in the World Press Freedom Index 2026. Norway topped the index for the 10th consecutive year.",
        "explanation_te": "వరల్డ్ ప్రెస్ ఫ్రీడమ్ ఇండెక్స్ 2026లో 180 దేశాలలో భారత్ 157వ స్థానంలో నిలిచింది. నార్వే అగ్రస్థానంలో ఉంది."
    },
    {
        "id": 120,
        "section": "General Studies",
        "topic": "Current Affairs - Global Defence 2026",
        "question_en": "According to the SIPRI Report 2026, what was India's global rank in military/defence spending ($92.1 Billion)?",
        "question_te": "స్టాక్‌హోమ్ ఇంటర్నేషనల్ పీస్ రీసెర్చ్ ఇన్‌స్టిట్యూట్ (SIPRI) నివేదిక 2026 ప్రకారం, రక్షణ వ్యయంలో ($92.1 బిలియన్లు) భారతదేశం ప్రపంచంలో ఎన్నో స్థానంలో ఉంది?",
        "options_en": ["3rd", "5th", "7th", "10th"],
        "options_te": ["3వ స్థానం", "5వ స్థానం", "7వ స్థానం", "10వ స్థానం"],
        "correct_option": 1,
        "explanation_en": "According to SIPRI, India ranked as the 5th largest military spender globally ($92.1 Billion), following the United States, China, Russia, and Germany.",
        "explanation_te": "SIPRI నివేదిక ప్రకారం అమెరికా, చైనా, రష్యా, జర్మనీల తర్వాత భారత్ 92.1 బిలియన్ డాలర్ల వ్యయంతో ప్రపంచంలో 5వ అతిపెద్ద రక్షణ బడ్జెట్ కలిగిన దేశంగా నిలిచింది."
    }
]

# Update Mock 3
with open('public/data/mock_test_full_200_3.json', 'r', encoding='utf-8') as f:
    mock3 = json.load(f)

for idx, q_new in enumerate(mock3_questions):
    mock3['questions'][100 + idx] = q_new

with open('public/data/mock_test_full_200_3.json', 'w', encoding='utf-8') as f:
    json.dump(mock3, f, ensure_ascii=False, indent=2)

print("Mock Test 3 updated: Q101 to Q120 are 100% 2026 CA!")

# =========================================================================
# MOCK TEST 4: Q101 to Q120 (Replacing old 2018/2019 questions)
# =========================================================================
mock4_questions = [
    {
        "id": 101,
        "section": "General Studies",
        "topic": "Current Affairs - Renewable Energy 2026",
        "question_en": "According to the International Renewable Energy Agency (IRENA) 2026 data, which country ranks 3rd in total installed renewable energy capacity globally?",
        "question_te": "అంతర్జాతీయ పునరుత్పాదక ఇంధన సంస్థ (IRENA) 2026 నివేదిక ప్రకారం, ప్రపంచవ్యాప్తంగా మొత్తం పునరుత్పాదక ఇంధన స్థాపిత సామర్థ్యంలో 3వ స్థానంలో ఉన్న దేశం ఏది?",
        "options_en": ["China", "United States", "India", "Germany"],
        "options_te": ["చైనా", "అమెరికా", "భారతదేశం", "జర్మనీ"],
        "correct_option": 2,
        "explanation_en": "India ranks 3rd globally in total renewable energy installed capacity (250.52 GW), trailing only China (1st) and the United States (2nd).",
        "explanation_te": "ప్రపంచ పునరుత్పాదక ఇంధన సామర్థ్యంలో చైనా (1వ), అమెరికా (2వ) ల తర్వాత భారత్ 250.52 GW తో ప్రపంచంలో 3వ స్థానంలో నిలిచింది."
    },
    {
        "id": 102,
        "section": "General Studies",
        "topic": "Current Affairs - Global Arms Trade 2026",
        "question_en": "According to the SIPRI Trends in International Arms Transfers report, which country remained the world’s largest arms importer during 2021–2025?",
        "question_te": "SIPRI అంతర్జాతీయ ఆయుధ బదిలీల నివేదిక ప్రకారం, 2021–2025 కాలంలో ప్రపంచంలోనే అతిపెద్ద ఆయుధ దిగుమతిదారుగా నిలిచిన దేశం ఏది?",
        "options_en": ["Saudi Arabia", "India", "Qatar", "Ukraine"],
        "options_te": ["సౌదీ అరేబియా", "భారతదేశం", "ఖతార్", "ఉక్రెయిన్"],
        "correct_option": 1,
        "explanation_en": "India remained the world's leading arms importer, accounting for 9.8% of total global arms imports according to the latest SIPRI assessment.",
        "explanation_te": "ప్రపంచ ఆయుధ దిగుమతుల్లో 9.8% వాటాతో భారతదేశం ప్రపంచంలోనే అత్యధిక ఆయుధాలను దిగుమతి చేసుకునే దేశంగా కొనసాగింది."
    },
    {
        "id": 103,
        "section": "General Studies",
        "topic": "Current Affairs - Global Indices 2026",
        "question_en": "What is India's rank in the 'Corruption Perceptions Index (CPI) 2025/2026' released by Transparency International?",
        "question_te": "ట్రాన్స్‌పరెన్సీ ఇంటర్నేషనల్ విడుదల చేసిన 'అవినీతి అవగాహన సూచిక (CPI) 2025/2026' లో భారతదేశం ర్యాంక్ ఎంత?",
        "options_en": ["84th", "91st", "96th", "102nd"],
        "options_te": ["84వ", "91వ", "96వ", "102వ"],
        "correct_option": 1,
        "explanation_en": "India secured 91st rank with a score of 39. Denmark was ranked 1st as the least corrupt nation globally.",
        "explanation_te": "కరప్షన్ పర్సెప్షన్స్ ఇండెక్స్‌లో భారత్ 39 స్కోర్‌తో 91వ స్థానంలో నిలిచింది. డెన్మార్క్ అత్యంత తక్కువ అవినీతి గల దేశంగా అగ్రస్థానంలో నిలిచింది."
    },
    {
        "id": 104,
        "section": "General Studies",
        "topic": "Current Affairs - Higher Education 2026",
        "question_en": "Which Indian premier institution topped the QS Asia University Rankings 2026 among all Indian participating universities?",
        "question_te": "QS ఆసియా యూనివర్సిటీ ర్యాంకింగ్స్ 2026లో పాల్గొన్న అన్ని భారతీయ విద్యాసంస్థల్లో అగ్రస్థానంలో నిలిచిన భారతీయ సంస్థ ఏది?",
        "options_en": ["IIT Bombay", "IIT Delhi", "IISc Bengaluru", "IIT Madras"],
        "options_te": ["IIT బాంబే", "IIT ఢిల్లీ", "IISc బెంగళూరు", "IIT మద్రాస్"],
        "correct_option": 1,
        "explanation_en": "IIT Delhi achieved the top rank among all Indian universities in the QS Asia University Rankings 2026.",
        "explanation_te": "QS ఆసియా విశ్వవిద్యాలయాల ర్యాంకింగ్స్ 2026లో భారతీయ విద్యాసంస్థల్లో IIT ఢిల్లీ అగ్రస్థానంలో నిలిచింది."
    },
    {
        "id": 105,
        "section": "General Studies",
        "topic": "Current Affairs - Agriculture Awards 2026",
        "question_en": "Who was conferred with the prestigious 13th Prof. M.S. Swaminathan Award 2026 for outstanding leadership in agricultural research and climate resilience?",
        "question_te": "వ్యవసాయ పరిశోధన మరియు వాతావరణ సమర్థతలో విశేష కృషికి గాను ప్రతిష్టాత్మక 13వ 'ప్రొఫెసర్ ఎం.ఎస్. స్వామినాథన్ అవార్డు 2026' ఎవరికి ప్రదానం చేయబడింది?",
        "options_en": ["Dr. Ch. Srinivasa Rao", "Dr. Himanshu Pathak", "Dr. Soumya Swaminathan", "Dr. Trilochan Mohapatra"],
        "options_te": ["డా. సిహెచ్. శ్రీనివాసరావు", "డా. హిమాంశు పాఠక్", "డా. సౌమ్యా స్వామినాథన్", "డా. త్రిలోచన్ మహాపాత్ర"],
        "correct_option": 0,
        "explanation_en": "Dr. Ch. Srinivasa Rao (Director, NAARM Hyderabad) was honored with the Prof. M.S. Swaminathan Award 2026 for pioneering work in rainfed agriculture and climate change adaptation.",
        "explanation_te": "వర్షాధార వ్యవసాయం మరియు వాతావరణ మార్పుల అధ్యయనంలో చేసిన విశిష్ట సేవలకు గాను హైదరాబాద్ NAARM డైరెక్టర్ డాక్టర్ సిహెచ్. శ్రీనివాసరావుకు ఈ అవార్డు లభించింది."
    },
    {
        "id": 106,
        "section": "General Studies",
        "topic": "Current Affairs - Cinema 2026",
        "question_en": "Which Indian film made history by winning a prestigious BAFTA (British Academy of Film and Television Arts) Award in 2026?",
        "question_te": "2026 బ్రిటిష్ అకాడమీ (BAFTA) అవార్డులలో ప్రతిష్టాత్మక పురస్కారం గెలుచుకుని చరిత్ర సృష్టించిన భారతీయ చిత్రం ఏది?",
        "options_en": ["Boong", "All We Imagine as Light", "Santosh", "Article 370"],
        "options_te": ["బూంగ్ (Boong)", "ఆల్ వి ఇమాజిన్ యాజ్ లైట్", "సంతోష్", "ఆర్టికల్ 370"],
        "correct_option": 0,
        "explanation_en": "Manipuri film 'Boong' directed by Lakshmipriya Devi won the prestigious BAFTA Award 2026 in London.",
        "explanation_te": "లక్ష్మీప్రియా దేవి దర్శకత్వం వహించిన మణిపురి చిత్రం 'బూంగ్' లండన్‌లో జరిగిన ప్రతిష్టాత్మక BAFTA 2026 అవార్డును గెలుచుకుంది."
    },
    {
        "id": 107,
        "section": "General Studies",
        "topic": "Current Affairs - International Honours 2026",
        "question_en": "Who won the 2026 Grammy Award for Best Audio Book, Narration & Storytelling Recording for the audiobook album 'Meditations'?",
        "question_te": "'మెడిటేషన్స్' (Meditations) ఆడియోబుక్ ఆల్బమ్‌కు గాను బెస్ట్ ఆడియో బుక్, కథనం & వాయిస్ రికార్డింగ్ విభాగంలో 2026 గ్రామీ అవార్డును ఎవరు గెలుచుకున్నారు?",
        "options_en": ["14th Dalai Lama", "Anoushka Shankar", "Kendrick Lamar", "Barack Obama"],
        "options_te": ["14వ దలైలామా", "అనూష్క శంకర్", "కెండ్రిక్ లామార్", "బరాక్ ఒబామా"],
        "correct_option": 0,
        "explanation_en": "Tibetan spiritual leader, the 14th Dalai Lama, won the Grammy Award 2026 for the spoken-word audio album 'Meditations'.",
        "explanation_te": "టిబెటన్ ఆధ్యాత్మిక గురువు 14వ దలైలామా 'మెడిటేషన్స్' ఆడియోబుక్ రికార్డింగ్‌కు ప్రతిష్టాత్మక గ్రామీ పురస్కారాన్ని అందుకున్నారు."
    },
    {
        "id": 108,
        "section": "General Studies",
        "topic": "Current Affairs - Judiciary & Governance 2026",
        "question_en": "India’s First Fully Paperless and Digital District Court was inaugurated in 2026 in which state?",
        "question_te": "2026లో భారతదేశపు మొట్టమొదటి పూర్తి కాగిత రహిత (Paperless) డిజిటల్ జిల్లా కోర్టు ఏ రాష్ట్రంలో ప్రారంభించబడింది?",
        "options_en": ["Kerala", "Gujarat", "Maharashtra", "Tamil Nadu"],
        "options_te": ["కేరళ", "గుజరాత్", "మహారాష్ట్ర", "తమిళనాడు"],
        "correct_option": 0,
        "explanation_en": "India's first fully paperless district court was inaugurated at Kalpetta in Wayanad district of Kerala by Chief Justice of India Surya Kant.",
        "explanation_te": "కేరళలోని వాయనాడ్ జిల్లా కల్పేట్టాలో భారతదేశపు తొలి పూర్తి పేపర్‌లెస్ జిల్లా కోర్టును సుప్రీంకోర్టు ప్రధాన న్యాయమూర్తి ప్రారంభించారు."
    },
    {
        "id": 109,
        "section": "General Studies",
        "topic": "Current Affairs - Global Tech Regulations 2026",
        "question_en": "Which European nation became the first to enact landmark legislation banning social media access for children under the age of 15?",
        "question_te": "15 ఏళ్లలోపు పిల్లలకు సోషల్ మీడియా వాడకాన్ని పూర్తిగా నిషేధిస్తూ చట్టం చేసిన మొట్టమొదటి యూరోపియన్ దేశం ఏది?",
        "options_en": ["France", "United Kingdom", "Germany", "Sweden"],
        "options_te": ["ఫ్రాన్స్", "యునైటెడ్ కింగ్‌డమ్", "జర్మనీ", "స్వీడన్"],
        "correct_option": 0,
        "explanation_en": "France became the first European nation to legally ban children under 15 from accessing social media platforms without parental consent and digital age verification.",
        "explanation_te": "పిల్లల మానసిక ఆరోగ్యాన్ని రక్షించడానికి 15 ఏళ్లలోపు పిల్లలకు సోషల్ మీడియాను నిషేధిస్తూ ఫ్రాన్స్ చట్టం చేసింది."
    },
    {
        "id": 110,
        "section": "General Studies",
        "topic": "Current Affairs - Agriculture Insurance 2026",
        "question_en": "Which district became the first in India to achieve 100% crop insurance coverage under the Pradhan Mantri Fasal Bima Yojana (PMFBY)?",
        "question_te": "ప్రధానమంత్రి ఫసల్ బీమా యోజన (PMFBY) కింద 100% పంటల బీమా సాధించిన భారతదేశపు మొట్టమొదటి జిల్లా ఏది?",
        "options_en": ["Alwar (Rajasthan)", "Indore (Madhya Pradesh)", "Karimnagar (Telangana)", "Surat (Gujarat)"],
        "options_te": ["ఆల్వార్ (రాజస్థాన్)", "ఇండోర్ (మధ్యప్రదేశ్)", "కరీంనగర్ (తెలంగాణ)", "సూరత్ (గుజరాత్)"],
        "correct_option": 0,
        "explanation_en": "Alwar district in Rajasthan became India's first district to achieve 100% saturation and coverage under PMFBY.",
        "explanation_te": "రాజస్థాన్‌లోని ఆల్వార్ జిల్లా PMFBY కింద 100 శాతం పంటల బీమా విస్తరణ సాధించిన దేశంలోనే తొలి జిల్లాగా నిలిచింది."
    },
    {
        "id": 111,
        "section": "General Studies",
        "topic": "Current Affairs - Urban Infrastructure 2026",
        "question_en": "India’s First 'Musical Highway' that produces rhythmic notes through tire vibration was inaugurated in which state/city?",
        "question_te": "వాహనాల టైర్ల రాపిడి ద్వారా సంగీత ధ్వనులను ఉత్పత్తి చేసే భారతదేశపు మొట్టమొదటి 'మ్యూజికల్ రోడ్' (Musical Road) ఎక్కడ ప్రారంభించబడింది?",
        "options_en": ["Mumbai (Maharashtra)", "Bengaluru (Karnataka)", "Hyderabad (Telangana)", "Gandhinagar (Gujarat)"],
        "options_te": ["ముంబై (మహారాష్ట్ర)", "బెంగళూరు (కర్ణాటక)", "హైదరాబాద్ (తెలంగాణ)", "గాంధీనగర్ (గుజరాత్)"],
        "correct_option": 0,
        "explanation_en": "India's first Musical Road was inaugurated on a stretch in Maharashtra/Mumbai, engineered to curb speeding and awaken drowsy drivers through road surface grooves.",
        "explanation_te": "డ్రైవర్లు నిద్రమత్తులోకి జారకుండా మరియు అతివేగాన్ని నియంత్రించడానికి ముంబైలో రోడ్డుపై ప్రత్యేక గాడులతో సంగీతం వినిపించేలా ఈ మ్యూజికల్ రోడ్డును రూపొందించారు."
    },
    {
        "id": 112,
        "section": "General Studies",
        "topic": "Current Affairs - Rapid Transit 2026",
        "question_en": "India’s First Namo Bharat Regional Rapid Transit System (RRTS) network connects which two major urban centers?",
        "question_te": "భారతదేశపు మొట్టమొదటి 'నమో భారత్' రీజినల్ ర్యాపిడ్ ట్రాన్సిట్ సిస్టమ్ (RRTS) ఏ రెండు ప్రధాన నగరాలను కలుపుతుంది?",
        "options_en": ["Delhi – Meerut", "Mumbai – Pune", "Ahmedabad – Vadodara", "Bengaluru – Mysuru"],
        "options_te": ["ఢిల్లీ – మీరట్", "ముంబై – పూణే", "అహ్మదాబాద్ – వడోదర", "బెంగళూరు – మైసూరు"],
        "correct_option": 0,
        "explanation_en": "India's first Namo Bharat semi-high speed transit corridor connects Delhi, Ghaziabad, and Meerut, operating at speeds up to 160 km/h.",
        "explanation_te": "గంటకు 160 కి.మీ వేగంతో ప్రయాణించే భారతదేశపు తొలి సెమీ హైస్పీడ్ రీజినల్ నమో భారత్ రైలు ఢిల్లీ మరియు మీరట్‌ల మధ్య నడుస్తుంది."
    },
    {
        "id": 113,
        "section": "General Studies",
        "topic": "Current Affairs - Higher Education & AI 2026",
        "question_en": "India’s First AI-Enabled State University Pilot Project was launched at which institution in collaboration with Google Cloud?",
        "question_te": "గూగుల్ క్లౌడ్ (Google Cloud) భాగస్వామ్యంతో భారతదేశపు మొట్టమొదటి AI-ఆధారిత రాష్ట్ర విశ్వవిద్యాలయ పైలట్ ప్రాజెక్ట్ ఏ యూనివర్సిటీలో ప్రారంభించబడింది?",
        "options_en": ["CCSU Meerut", "Delhi University", "Osmania University", "Anna University"],
        "options_te": ["చౌదరి చరణ్ సింగ్ యూనివర్సిటీ (CCSU) మీరట్", "ఢిల్లీ యూనివర్సిటీ", "ఉస్మానియా యూనివర్సిటీ", "అన్నా యూనివర్సిటీ"],
        "correct_option": 0,
        "explanation_en": "Chaudhary Charan Singh University (CCSU), Meerut launched India’s first AI-enabled state university initiative integrating AI tutoring and automated evaluation.",
        "explanation_te": "ఉత్తరప్రదేశ్‌లోని చౌదరి చరణ్ సింగ్ విశ్వవిద్యాలయం (CCSU) మీరట్ గూగుల్ భాగస్వామ్యంతో తొలి AI ఆధారిత స్టేట్ యూనివర్సిటీ ప్రాజెక్టును ప్రారంభించింది."
    },
    {
        "id": 114,
        "section": "General Studies",
        "topic": "Current Affairs - Tourism & Engineering 2026",
        "question_en": "India’s First State-of-the-Art Glass Floor Suspension Bridge ('Bajrang Setu') was constructed in which city?",
        "question_te": "భారతదేశపు మొట్టమొదటి అద్దాల అంతస్తుతో కూడిన గ్లాస్ సస్పెన్షన్ వంతెన ('బజరంగ్ సేతు') ఏ నగరంలో నిర్మించబడింది?",
        "options_en": ["Rishikesh (Uttarakhand)", "Manali (Himachal Pradesh)", "Gangtok (Sikkim)", "Munnar (Kerala)"],
        "options_te": ["రిషికేష్ (ఉత్తరాఖండ్)", "మనాలి (హిమాచల్ ప్రదేశ్)", "గ్యాంగ్‌టక్ (సిక్కిం)", "మున్నార్ (కేరళ)"],
        "correct_option": 0,
        "explanation_en": "Bajrang Setu, India's first iconic glass-bottom suspension bridge across the holy Ganga river, was built at Rishikesh in Uttarakhand.",
        "explanation_te": "ఉత్తరాఖండ్‌లోని రిషికేష్‌లో గంగా నదిపై సుప్రసిద్ధ లక్ష్మణ్ ఝూలా స్థానంలో భారతదేశపు తొలి గాజు అంతస్తు గల 'బజరంగ్ సేతు' కేబుల్ వంతెనను నిర్మించారు."
    },
    {
        "id": 115,
        "section": "General Studies",
        "topic": "Current Affairs - Infrastructure 2026",
        "question_en": "Prime Minister Narendra Modi inaugurated India’s first underwater twin tube road-and-rail tunnel connecting which two regions in Kerala?",
        "question_te": "కేరళలోని ఏ రెండు ప్రాంతాలను కలుపుతూ నిర్మించిన భారతదేశపు తొలి నీటి అడుగున రోడ్డు-రైలు సొరంగ మార్గాన్ని ప్రధానమంత్రి నరేంద్ర మోదీ ప్రారంభించారు?",
        "options_en": ["Vypin to Fort Kochi", "Kollam to Alappuzha", "Ernakulam to Mattancherry", "Kozhikode to Beypore"],
        "options_te": ["వైపిన్ నుండి ఫోర్ట్ కొచ్చి", "కొల్లాం నుండి అలప్పుజా", "ఎర్నాకులం నుండి మట్టాంచెర్రీ", "కోజికోడ్ నుండి బేపూర్"],
        "correct_option": 0,
        "explanation_en": "India's landmark underwater tunnel connecting Vypin island and Fort Kochi was developed to decongest maritime traffic and revolutionize urban mobility in Kerala.",
        "explanation_te": "కొచ్చిలోని వైపిన్ ద్వీపాన్ని మరియు చారిత్రక ఫోర్ట్ కొచ్చిని కలుపుతూ నీటి అడుగున నిర్మించిన సొరంగ మార్గాన్ని ప్రారంభించారు."
    },
    {
        "id": 116,
        "section": "General Studies",
        "topic": "Current Affairs - Political Leadership 2026",
        "question_en": "Who was appointed as the 16th and youngest National President of the Bharatiya Janata Party (BJP) in January 2026?",
        "question_te": "జనవరి 2026లో భారతీయ జనతా పార్టీ (BJP) 16వ మరియు అతి పిన్న వయస్కుడైన జాతీయ అధ్యక్షుడిగా ఎవరు నియమితులయ్యారు?",
        "options_en": ["Nitin Nabin", "J.P. Nadda", "Amit Shah", "Rajnath Singh"],
        "options_te": ["నితిన్ నబిన్", "జె.పి. నడ్డా", "అమిత్ షా", "రాజ్‌నాథ్ సింగ్"],
        "correct_option": 0,
        "explanation_en": "Nitin Nabin from Bihar was appointed as the 16th National President of the Bharatiya Janata Party, succeeding J.P. Nadda.",
        "explanation_te": "బీహార్‌కు చెందిన నితిన్ నబిన్ జె.పి. నడ్డా స్థానంలో బీజేపీ 16వ జాతీయ అధ్యక్షుడిగా బాధ్యతలు స్వీకరించారు."
    },
    {
        "id": 117,
        "section": "General Studies",
        "topic": "Current Affairs - Passports & Mobility 2026",
        "question_en": "What is India's rank in the 'Henley Passport Index 2026', offering visa-free or visa-on-arrival access to 56 nations?",
        "question_te": "56 దేశాలకు వీసా రహిత ప్రవేశాన్ని అందిస్తూ 'హెన్లీ పాస్‌పోర్ట్ ఇండెక్స్ 2026' లో భారతదేశం సాధించిన ర్యాంక్ ఎంత?",
        "options_en": ["78th", "80th", "87th", "90th"],
        "options_te": ["78వ", "80వ", "87వ", "90వ"],
        "correct_option": 0,
        "explanation_en": "India secured 78th rank in the Henley Passport Index 2026. Singapore, Japan, and South Korea held the top ranks as the world's most powerful passports.",
        "explanation_te": "హెన్లీ పాస్‌పోర్ట్ ఇండెక్స్ 2026లో భారత పాస్‌పోర్ట్ 78వ స్థానంలో నిలిచింది. సింగపూర్, జపాన్‌లు అగ్రస్థానంలో ఉన్నాయి."
    },
    {
        "id": 118,
        "section": "General Studies",
        "topic": "Current Affairs - Maritime Infrastructure 2026",
        "question_en": "Which deep-water seaport in Kerala operationalized commercial container transhipment for the world’s largest cargo mega-vessels in 2026?",
        "question_te": "ప్రపంచంలోనే అతిపెద్ద కంటైనర్ నౌకలను హ్యాండిల్ చేస్తూ 2026లో పూర్తిస్థాయి ట్రాన్స్‌షిప్‌మెంట్ కార్యకలాపాలు ప్రారంభించిన కేరళలోని డీప్ వాటర్ ఓడరేవు ఏది?",
        "options_en": ["Vizhinjam International Seaport", "Cochin Port", "Beypore Port", "Kollam Port"],
        "options_te": ["విళింజం అంతర్జాతీయ ఓడరేవు", "కొచ్చిన్ పోర్ట్", "బేపూర్ పోర్ట్", "కొల్లాం పోర్ట్"],
        "correct_option": 0,
        "explanation_en": "Vizhinjam International Seaport in Thiruvananthapuram, Kerala operationalized automated container berths capable of berthing ultra-large container vessels.",
        "explanation_te": "కేరళ రాజధాని తిరువనంతపురంలోని విళింజం అంతర్జాతీయ డీప్‌వాటర్ పోర్టు ప్రపంచ శ్రేణి మెగా కంటైనర్ నౌకల కోసం వాణిజ్య కార్యకలాపాలను ప్రారంభించింది."
    },
    {
        "id": 119,
        "section": "General Studies",
        "topic": "Current Affairs - Green Mobility 2026",
        "question_en": "Under the 'Hydrogen for Heritage' initiative, Indian Railways commenced commercial passenger trials of India’s 1st Hydrogen-Powered Train on which section?",
        "question_te": "'హైడ్రోజన్ ఫర్ హెరిటేజ్' కార్యక్రమంలో భాగంగా భారతీయ రైల్వే దేశంలోనే తొలి హైడ్రోజన్ ఆధారిత ప్యాసింజర్ రైలు ట్రయల్స్‌ను ఏ సెక్షన్‌లో నిర్వహించింది?",
        "options_en": ["Jind – Sonipat section (Haryana)", "Kalka – Shimla route", "Nilgiri Mountain Railway", "Darjeeling Himalayan section"],
        "options_te": ["జింద్ – సోనిపట్ సెక్షన్ (హర్యానా)", "కాల్కా – సిమ్లా రూట్", "నీలగిరి మౌంటైన్ రైల్వే", "డార్జిలింగ్ హిమాలయన్ సెక్షన్"],
        "correct_option": 0,
        "explanation_en": "India’s first hydrogen fuel cell-powered passenger train was trial tested on the Jind-Sonipat 89-km heritage corridor in Haryana by Northern Railway.",
        "explanation_te": "హర్యానాలోని జింద్ - సోనిపట్ సెక్షన్‌లో పర్యావరణహిత జీరో-ఎమిషన్ హైడ్రోజన్ రైలును విజయవంతంగా పరీక్షించారు."
    },
    {
        "id": 120,
        "section": "General Studies",
        "topic": "Current Affairs - Science & Technology 2026",
        "question_en": "What was the official national theme for the celebration of 'National Science Day' on 28 February 2026 across India?",
        "question_te": "28 ఫిబ్రవరి 2026న దేశవ్యాప్తంగా నిర్వహించిన 'జాతీయ సైన్స్ దినోత్సవం' (National Science Day) యొక్క అధికారిక నినాదం (Theme) ఏమిటి?",
        "options_en": [
            "Indigenous Technologies for Viksit Bharat",
            "Global Science for Global Wellbeing",
            "Future of STI: Impacts on Education and Work",
            "Integrated Approach in Science and Technology"
        ],
        "options_te": [
            "వికసిత్ భారత్ కోసం స్వదేశీ సాంకేతికతలు (Indigenous Technologies for Viksit Bharat)",
            "గ్లోబల్ సైన్స్ ఫర్ గ్లోబల్ వెల్‌బీయింగ్",
            "ఫ్యూచర్ ఆఫ్ ఎస్టీఐ: ఎడ్యుకేషన్ అండ్ వర్క్",
            "ఇంటిగ్రేటెడ్ అప్రోచ్ ఇన్ సైన్స్ అండ్ టెక్నాలజీ"
        ],
        "correct_option": 0,
        "explanation_en": "National Science Day 2026 celebrated Sir C.V. Raman's discovery of the Raman Effect under the theme 'Indigenous Technologies for Viksit Bharat'.",
        "explanation_te": "భారత శాస్త్రవేత్త సర్ సి.వి. రామన్ 'రామన్ ఎఫెక్ట్' ఆవిష్కరణను పురస్కరించుకుని 2026 సైన్స్ డేను 'వికసిత్ భారత్ కోసం స్వదేశీ సాంకేతికతలు' అనే థీమ్‌తో నిర్వహించారు."
    }
]

# Update Mock 4
with open('public/data/mock_test_full_200_4.json', 'r', encoding='utf-8') as f:
    mock4 = json.load(f)

for idx, q_new in enumerate(mock4_questions):
    mock4['questions'][100 + idx] = q_new

with open('public/data/mock_test_full_200_4.json', 'w', encoding='utf-8') as f:
    json.dump(mock4, f, ensure_ascii=False, indent=2)

print("Mock Test 4 updated: Q101 to Q120 are 100% 2026 CA (replaced all 2018/2019 items)!")

# =========================================================================
# MOCK TEST 5: Q101 to Q120 (Science & Tech 2026 & National Initiatives)
# =========================================================================
mock5_questions = [
    {
        "id": 101,
        "section": "General Studies",
        "topic": "Current Affairs - Judicial Appointments 2026",
        "question_en": "Who assumed office as the 53rd Chief Justice of India (CJI) in 2026, succeeding Justice Sanjiv Khanna?",
        "question_te": "జస్టిస్ సంజీవ్ ఖన్నా అనంతరం 2026లో భారత 53వ ప్రధాన న్యాయమూర్తిగా (CJI) ఎవరు బాధ్యతలు స్వీకరించారు?",
        "options_en": ["Justice Surya Kant", "Justice B.R. Gavai", "Justice Vikram Nath", "Justice J.K. Maheshwari"],
        "options_te": ["జస్టిస్ సూర్య కాంత్", "జస్టిస్ బి.ఆర్. గవాయ్", "జస్టిస్ విక్రమ్ నాథ్", "జస్టిస్ జె.కె. మహేశ్వరి"],
        "correct_option": 0,
        "explanation_en": "Justice Surya Kant took the oath of office as the 53rd Chief Justice of India administered by President Droupadi Murmu.",
        "explanation_te": "రాష్ట్రపతి ద్రౌపది ముర్ము చేతుల మీదుగా జస్టిస్ సూర్య కాంత్ భారత 53వ ప్రధాన న్యాయమూర్తిగా ప్రమాణ స్వీకారం చేశారు."
    },
    {
        "id": 102,
        "section": "General Studies",
        "topic": "Current Affairs - Defence Appointments 2026",
        "question_en": "Who was appointed as the Chief of Defence Staff (CDS) of the Indian Armed Forces in 2026?",
        "question_te": "2026లో భారత త్రివిధ దళాల రక్షణ అధిపతిగా (Chief of Defence Staff - CDS) ఎవరు నియమితులయ్యారు?",
        "options_en": ["Lt. Gen. N.S. Raja Subramani", "Gen. Upendra Dwivedi", "Air Chief Marshal A.P. Singh", "Adm. Dinesh Tripathi"],
        "options_te": ["లెఫ్టినెంట్ జనరల్ ఎన్.ఎస్. రాజా సుబ్రమణి", "జనరల్ ఉపేంద్ర ద్వివేది", "ఎయిర్ చీఫ్ మార్షల్ ఎ.పి. సింగ్", "అడ్మిరల్ దినేష్ త్రిపాఠి"],
        "correct_option": 0,
        "explanation_en": "Lt. Gen. N.S. Raja Subramani was appointed as the Chief of Defence Staff (CDS) to lead the integration and theaterisation of India's armed forces.",
        "explanation_te": "భారత త్రివిధ దళాల సమన్వయం మరియు థియేటరైజేషన్ ప్రక్రియను వేగవంతం చేయడానికి లెఫ్టినెంట్ జనరల్ ఎన్.ఎస్. రాజా సుబ్రమణి CDS గా నియమితులయ్యారు."
    },
    {
        "id": 103,
        "section": "General Studies",
        "topic": "Current Affairs - Security Appointments 2026",
        "question_en": "Who was appointed as the Director General (DG) of the Border Security Force (BSF) in 2026?",
        "question_te": "2026లో సరిహద్దు భద్రతా దళం (BSF) డైరెక్టర్ జనరల్‌గా (DG) ఎవరు నియమితులయ్యారు?",
        "options_en": ["Praveen Kumar", "Daljit Singh Chaudhary", "Anish Dayal Singh", "Rahul Rasgotra"],
        "options_te": ["ప్రవీణ్ కుమార్", "దల్జీత్ సింగ్ చౌదరి", "అనీష్ దయాళ్ సింగ్", "రాహుల్ రస్గోత్రా"],
        "correct_option": 0,
        "explanation_en": "Senior IPS officer Praveen Kumar took charge as the Director General of the Border Security Force (BSF).",
        "explanation_te": "సీనియర్ ఐపీఎస్ అధికారి ప్రవీణ్ కుమార్ సరిహద్దు భద్రతా దళం (BSF) డైరెక్టర్ జనరల్‌గా బాధ్యతలు స్వీకరించారు."
    },
    {
        "id": 104,
        "section": "General Studies",
        "topic": "Current Affairs - Constitutional Appointments 2026",
        "question_en": "Who was appointed as the Central Vigilance Commissioner (CVC) of India in 2026?",
        "question_te": "2026లో భారతదేశ సెంట్రల్ విజిలెన్స్ కమిషనర్‌గా (CVC) ఎవరు నియమితులయ్యారు?",
        "options_en": ["Praveen Vashista", "P.K. Srivastava", "Suresh N. Patel", "Sanjay Kothari"],
        "options_te": ["ప్రవీణ్ వశిష్ట", "పి.కె. శ్రీవాస్తవ", "సురేష్ ఎన్. పటేల్", "సంజయ్ కొఠారి"],
        "correct_option": 0,
        "explanation_en": "Praveen Vashista was appointed as the Central Vigilance Commissioner (CVC) to head India's apex anti-corruption watchdog.",
        "explanation_te": "ప్రవీణ్ వశిష్ట భారతదేశ కేంద్ర నిఘా కమిషనర్‌గా (CVC) నియమితులయ్యారు."
    },
    {
        "id": 105,
        "section": "General Studies",
        "topic": "Current Affairs - Digital Judiciary 2026",
        "question_en": "Which premier constitutional institution launched the 'One Case One Data' digital registry initiative and 'Su Sahay' AI assistance chatbot in 2026?",
        "question_te": "'వన్ కేస్ వన్ డేటా' (One Case One Data) డిజిటల్ రిజిస్ట్రీ మరియు 'సు సహాయ్' (Su Sahay) AI చాట్‌బాట్లను 2026లో ఏ రాజ్యాంగ సంస్థ ప్రారంభించింది?",
        "options_en": ["Supreme Court of India", "NITI Aayog", "Election Commission of India", "Law Commission of India"],
        "options_te": ["భారత సుప్రీంకోర్టు", "నీతి ఆయోగ్", "భారత ఎన్నికల సంఘం", "లా కమిషన్ ఆఫ్ ఇండియా"],
        "correct_option": 0,
        "explanation_en": "The Supreme Court of India rolled out 'One Case One Data' to integrate electronic case files across all High Courts and District Courts with AI legal assistance.",
        "explanation_te": "దేశవ్యాప్తంగా అన్ని హైకోర్టులు మరియు జిల్లా కోర్టుల కేసుల డేటాను ఏకీకృతం చేయడానికి మరియు న్యాయ సేవలను సులభతరం చేయడానికి సుప్రీంకోర్టు ఈ ప్రాజెక్టును ప్రారంభించింది."
    },
    {
        "id": 106,
        "section": "General Studies",
        "topic": "Current Affairs - Defence Day Themes 2026",
        "question_en": "What was the official theme for Indian Army Day celebrated on 15 January 2026?",
        "question_te": "15 జనవరి 2026న నిర్వహించిన భారత సైనిక దినోత్సవం (Indian Army Day 2026) యొక్క అధికారిక నినాదం ఏమిటి?",
        "options_en": [
            "Year of Networking and Data Centricity",
            "In Stride with the Future",
            "Year of Technology Absorption",
            "Nation First Always"
        ],
        "options_te": [
            "నెట్‌వర్కింగ్ మరియు డేటా సెంట్రిసిటీ సంవత్సరం (Year of Networking and Data Centricity)",
            "ఇన్ స్ట్రైడ్ విత్ ది ఫ్యూచర్",
            "టెక్నాలజీ అబ్సార్ప్షన్ సంవత్సరం",
            "నేషన్ ఫస్ట్ ఆల్వేస్"
        ],
        "correct_option": 0,
        "explanation_en": "The Indian Army observed the year 2026 under the central theme 'Year of Networking and Data Centricity' to modernize battlefield communication and digital command systems.",
        "explanation_te": "యుద్ధరంగంలో డిజిటల్ కమ్యూనికేషన్ మరియు ఆధునిక డేటా వ్యవస్థల వినియోగాన్ని పెంపొందించడానికి ఆర్మీ డే 2026 నినాదంగా దీనిని ప్రకటించారు."
    },
    {
        "id": 107,
        "section": "General Studies",
        "topic": "Current Affairs - Science & Technology 2026",
        "question_en": "India’s first indigenous high-performance Micro GPU semiconductor chip was designed and taped out in 2026 by researchers at which institution?",
        "question_te": "భారతదేశపు మొట్టమొదటి స్వదేశీ హై-పెర్ఫార్మెన్స్ మైక్రో GPU సెమీకండక్టర్ చిప్‌ను 2026లో ఏ విద్యాసంస్థ పరిశోధకులు విజయవంతంగా డిజైన్ చేశారు?",
        "options_en": ["IIT Delhi", "IIT Bombay", "IIT Madras", "IISc Bengaluru"],
        "options_te": ["IIT ఢిల్లీ", "IIT బాంబే", "IIT మద్రాస్", "IISc బెంగళూరు"],
        "correct_option": 0,
        "explanation_en": "Researchers at IIT Delhi successfully designed and taped out India's first indigenous Micro GPU tailored for energy-efficient edge AI processing and graphics rendering.",
        "explanation_te": "ఎడ్జ్ AI మరియు గ్రాఫిక్స్ ప్రాసెసింగ్ కోసం భారతదేశపు తొలి స్వదేశీ మైక్రో GPU చిప్‌ను IIT ఢిల్లీ బృందం అభివృద్ధి చేసింది."
    },
    {
        "id": 108,
        "section": "General Studies",
        "topic": "Current Affairs - Quantum Technology 2026",
        "question_en": "India’s first indigenous 20 milli-Kelvin (20 mK) ultra-low temperature Dilution Refrigerator essential for superconducting quantum computers was developed by DRDO in collaboration with which entity?",
        "question_te": "సూపర్‌కండక్టింగ్ క్వాంటం కంప్యూటర్ల నిర్వహణకు కీలకమైన భారతదేశపు తొలి స్వదేశీ 20 మిల్లీ-కెల్విన్ (20 mK) డైల్యూషన్ రిఫ్రిజిరేటర్‌ను DRDO ఏ సంస్థతో కలిసి అభివృద్ధి చేసింది?",
        "options_en": ["ZeroMK Cryogenics", "ISRO Cryogenic Centre", "BARC Mumbai", "BHEL Hyderabad"],
        "options_te": ["జీరో ఎంకే క్రయోజెనిక్స్ (ZeroMK)", "ఇస్రో క్రయోజెనిక్ సెంటర్", "బార్క్ ముంబై", "భెల్ హైదరాబాద్"],
        "correct_option": 0,
        "explanation_en": "DRDO and deep-tech startup ZeroMK co-developed the indigenous 20 mK dilution refrigerator, breaking reliance on Western cryo-cooling imports for India's National Quantum Mission.",
        "explanation_te": "జాతీయ క్వాంటం మిషన్‌లో భాగంగా విదేశీ క్రయో-కూలింగ్ పరికరాలపై ఆధారపడటాన్ని తగ్గించడానికి DRDO మరియు ZeroMK కలిసి ఈ అల్ట్రా-లో టెంపరేచర్ కూలింగ్ వ్యవస్థను రూపొందించాయి."
    },
    {
        "id": 109,
        "section": "General Studies",
        "topic": "Current Affairs - Quantum Tech & Regional Hubs 2026",
        "question_en": "The foundation stone for the mega 'Amaravati Quantum & AI Campus' was laid in 2026 in which state in strategic partnership with global tech giants?",
        "question_te": "ప్రపంచ సాంకేతిక సంస్థల భాగస్వామ్యంతో 'అమరావతి క్వాంటం & AI క్యాంపస్' మెగా ప్రాజెక్టుకు 2026లో ఏ రాష్ట్రంలో శంకుస్థాపన జరిగింది?",
        "options_en": ["Andhra Pradesh", "Telangana", "Karnataka", "Tamil Nadu"],
        "options_te": ["ఆంధ్రప్రదేశ్", "తెలంగాణ", "కర్ణాటక", "తమిళనాడు"],
        "correct_option": 0,
        "explanation_en": "Andhra Pradesh laid the foundation stone for the Amaravati Quantum & AI City hub partnering with Tata Group and global computing leaders to build quantum research infrastructure.",
        "explanation_te": "ఆంధ్రప్రదేశ్ రాజధాని అమరావతిలో అత్యాధునిక క్వాంటం కంప్యూటింగ్ మరియు ఆర్టిఫిషియల్ ఇంటెలిజెన్స్ హబ్‌కు శంకుస్థాపన చేశారు."
    },
    {
        "id": 110,
        "section": "General Studies",
        "topic": "Current Affairs - Health & Vaccines 2026",
        "question_en": "The Central Drugs Standard Control Organisation (CDSCO) approved which innovative live-attenuated tetravalent dengue vaccine in 2026 for clinical use in India?",
        "question_te": "భారత ఔషధ నియంత్రణ సంస్థ (CDSCO) 2026లో ఏ వినూత్న టెట్రావాలెంట్ డెంగ్యూ వ్యాక్సిన్‌కు దేశంలో క్లినికల్ వినియోగానికి ఆమోదం తెలిపింది?",
        "options_en": ["Qdenga", "Dengvaxia", "ZyCoV-D", "Mosquirix"],
        "options_te": ["క్యూడెంగా (Qdenga)", "డెంగ్వాక్సియా", "జైకోవ్-డి", "మోస్కిరిక్స్"],
        "correct_option": 0,
        "explanation_en": "CDSCO approved Takeda's Qdenga, a four-serotype tetravalent dengue vaccine shown to significantly reduce hospitalizations from severe dengue fever.",
        "explanation_te": "తీవ్రమైన డెంగ్యూ జ్వరాన్ని మరియు ఆసుపత్రి చేరికలను సమర్థవంతంగా అరికట్టే టకెడా వారి 'క్యూడెంగా' టెట్రావాలెంట్ వ్యాక్సిన్‌కు భారతదేశంలో ఆమోదం లభించింది."
    },
    {
        "id": 111,
        "section": "General Studies",
        "topic": "Current Affairs - Medical Technology 2026",
        "question_en": "India’s first indigenously developed 1.5 Tesla superconducting MRI scanner was rolled out for clinical adoption under the leadership of which research agency?",
        "question_te": "భారతదేశపు మొట్టమొదటి స్వదేశీ 1.5 టెస్లా సూపర్ కండక్టింగ్ MRI స్కానర్‌ను ఏ పరిశోధనా సంస్థ ఆధ్వర్యంలో రూపొందించి విడుదల చేశారు?",
        "options_en": ["SAMEER (Society for Applied Microwave Electronics)", "CSIR-NCL", "DRDO-INMAS", "ICMR"],
        "options_te": ["సమీర్ (SAMEER)", "సిఎస్ఐఆర్ - ఎన్సీఎల్", "డిఆర్డిఓ - ఇన్మాస్", "ఐసీఎంఆర్"],
        "correct_option": 0,
        "explanation_en": "SAMEER under the Ministry of Electronics and Information Technology developed India's first 1.5T MRI machine to drastically cut diagnostic imaging costs across government hospitals.",
        "explanation_te": "కేంద్ర ఎలక్ట్రానిక్స్ & ఐటీ శాఖ పరిధిలోని 'సమీర్' (SAMEER) దేశీయంగా 1.5 టెస్లా MRI స్కానర్‌ను అభివృద్ధి చేసి వైద్య పరికరాల రంగంలో స్వయం సమృద్ధిని సాధించింది."
    },
    {
        "id": 112,
        "section": "General Studies",
        "topic": "Current Affairs - Biotechnology & Cancer 2026",
        "question_en": "India’s first commercially approved indigenous CAR-T cell gene therapy for cancer treatment ('NexCAR19') was pioneered by which premier institution?",
        "question_te": "క్యాన్సర్ చికిత్స కోసం భారతదేశపు మొట్టమొదటి స్వదేశీ CAR-T సెల్ జన్యు చికిత్స ('NexCAR19') ను ఏ ప్రముఖ విద్యాసంస్థ పరిశోధకులు రూపొందించారు?",
        "options_en": ["IIT Bombay and Tata Memorial Hospital", "IIT Delhi and AIIMS", "IISc Bengaluru and Kidwai", "CSIR-CCMB Hyderabad"],
        "options_te": ["IIT బాంబే మరియు టాటా మెమోరియల్ హాస్పిటల్", "IIT ఢిల్లీ మరియు ఎయిమ్స్", "IISc బెంగళూరు మరియు కిద్వాయ్", "CSIR-CCMB హైదరాబాద్"],
        "correct_option": 0,
        "explanation_en": "NexCAR19, an affordable indigenous CAR-T cell therapy for lymphoma and leukemia, was innovated jointly by IIT Bombay, Tata Memorial Hospital, and ImmunoACT.",
        "explanation_te": "బ్లడ్ క్యాన్సర్ బాధితులకు తక్కువ ఖర్చుతో అత్యున్నత జీన్ థెరపీ అందించడానికి IIT బాంబే మరియు టాటా మెమోరియల్ హాస్పిటల్ సంయుక్తంగా NexCAR19 ను అభివృద్ధి చేశాయి."
    },
    {
        "id": 113,
        "section": "General Studies",
        "topic": "Current Affairs - Deep Tech Wearables 2026",
        "question_en": "India’s first aerospace-grade titanium health smart ring 'Ring One', featuring clinical ECG and NFC contactless payments, was designed by which IIT-incubated startup?",
        "question_te": "క్లినికల్ ఈసీజీ (ECG) మరియు ఎన్‌ఎఫ్‌సీ కాంటాక్ట్‌లెస్ చెల్లింపుల సదుపాయం గల భారతదేశపు తొలి టైటానియం స్మార్ట్ రింగ్ 'రింగ్ వన్' (Ring One) ను ఏ ఐఐటీ ఇంక్యుబేటెడ్ స్టార్టప్ రూపొందించింది?",
        "options_en": ["Muse Wearables (IIT Madras)", "Ultrahuman (IIT Delhi)", "Noise Labs (IIT Kanpur)", "Agnikul (IIT Madras)"],
        "options_te": ["మ్యూజ్ వేరబుల్స్ (IIT మద్రాస్)", "అల్ట్రాహ్యూమన్ (IIT ఢిల్లీ)", "నాయిస్ ల్యాబ్స్ (IIT కాన్పూర్)", "అగ్నికుల్ (IIT మద్రాస్)"],
        "correct_option": 0,
        "explanation_en": "Muse Wearables, incubated at IIT Madras, developed 'Ring One' – India's indigenous smart ring providing continuous BP trend monitoring, medical ECG, and secure payments.",
        "explanation_te": "IIT మద్రాస్ ఇంక్యుబేటెడ్ డీప్‌టెక్ స్టార్టప్ 'మ్యూజ్ వేరబుల్స్' ప్రపంచ స్థాయి హెల్త్ ట్రాకింగ్ మరియు చెల్లింపుల ఫీచర్లతో రింగ్ వన్‌ను ఆవిష్కరించింది."
    },
    {
        "id": 114,
        "section": "General Studies",
        "topic": "Current Affairs - Clean Energy & Manufacturing 2026",
        "question_en": "In 2026, ground was broken for a 20 GWh advanced Lithium-ion cell and battery giga-factory at which coastal industrial hub in Andhra Pradesh?",
        "question_te": "2026లో 20 GWh అత్యాధునిక లిథియం-అయాన్ బ్యాటరీ సెల్ గిగా-ఫ్యాక్టరీ నిర్మాణానికి ఆంధ్రప్రదేశ్‌లోని ఏ తీరప్రాంత పారిశ్రామిక హబ్‌లో శంకుస్థాపన జరిగింది?",
        "options_en": ["Rambilli (Visakhapatnam)", "Sri City (Tirupati)", "Kakinada SEZ", "Machilipatnam"],
        "options_te": ["రాంబిల్లి (విశాఖపట్నం)", "శ్రీసిటీ (తిరుపతి)", "కాకినాడ సెజ్", "మచిలీపట్నం"],
        "correct_option": 0,
        "explanation_en": "Energy giants broke ground for a 20 GWh integrated battery cell giga-factory at Rambilli near Visakhapatnam to power electric vehicles and grid energy storage.",
        "explanation_te": "ఎలక్ట్రిక్ వాహనాలు మరియు గ్రిడ్ ఇంధన నిల్వ కోసం విశాఖపట్నం సమీపంలోని రాంబిల్లిలో 20 GWh మెగా లిథియం-అయాన్ గిగా-ఫ్యాక్టరీ పనులను ప్రారంభించారు."
    },
    {
        "id": 115,
        "section": "General Studies",
        "topic": "Current Affairs - Green Ammonia Projects 2026",
        "question_en": "The world’s largest green ammonia and hydrogen export bunkering facility is being developed at which port region in Andhra Pradesh?",
        "question_te": "ప్రపంచంలోనే అతిపెద్ద గ్రీన్ అమ్మోనియా మరియు గ్రీన్ హైడ్రోజన్ ఎగుమతి ప్రాజెక్ట్ ఆంధ్రప్రదేశ్‌లోని ఏ ఓడరేవు ప్రాంతంలో అభివృద్ధి చేయబడుతోంది?",
        "options_en": ["Kakinada", "Krishnapatnam", "Gangavaram", "Bhavanapadu"],
        "options_te": ["కాకినాడ", "కృష్ణపట్నం", "గంగవరం", "భావనపాడు"],
        "correct_option": 0,
        "explanation_en": "Kakinada in Andhra Pradesh was selected as the hub for developing one of the world's largest commercial-scale green ammonia export facilities powered by renewable energy.",
        "explanation_te": "ఆంధ్రప్రదేశ్‌లోని కాకినాడ పోర్టు పరిసరాల్లో పునరుత్పాదక ఇంధనంతో పనిచేసే ప్రపంచ స్థాయి భారీ గ్రీన్ అమ్మోనియా ఉత్పత్తి మరియు ఎగుమతి హబ్‌ను ఏర్పాటు చేస్తున్నారు."
    },
    {
        "id": 116,
        "section": "General Studies",
        "topic": "Current Affairs - Inland Waterways 2026",
        "question_en": "India’s first indigenous zero-emission Hydrogen Fuel Cell passenger catamaran ferry was deployed for commercial pilgrim and tourist transport at which sacred river city?",
        "question_te": "భారతదేశపు మొట్టమొదటి జీరో-ఎమిషన్ హైడ్రోజన్ ఫ్యూయల్ సెల్ ప్యాసింజర్ ఫెర్రీ పడవ ఏ పవిత్ర నదీ నగరంలో తీర్థయాత్రికులు మరియు పర్యాటకుల రవాణా కోసం ప్రారంభించబడింది?",
        "options_en": ["Varanasi / Prayagraj (Ganga)", "Kolkata (Hooghly)", "Haridwar (Ganga)", "Guwahati (Brahmaputra)"],
        "options_te": ["వారణాసి / ప్రయాగ్‌రాజ్ (గంగా నది)", "కోల్‌కతా (హూగ్లీ)", "హరిద్వార్ (గంగా)", "గౌహతి (బ్రహ్మపుత్ర)"],
        "correct_option": 0,
        "explanation_en": "Built by Cochin Shipyard, India's first indigenous hydrogen fuel cell catamaran passenger ferry was launched on the National Waterway-1 at Varanasi/Prayagraj.",
        "explanation_te": "కొచ్చిన్ షిప్‌యార్డ్ నిర్మించిన దేశపు మొట్టమొదటి హైడ్రోజన్ ఫ్యూయల్ సెల్ క్యాటమరాన్ బోటును గంగా నదిలో వారణాసి మరియు ప్రయాగ్‌రాజ్ ఘాట్ల వద్ద ప్రవేశపెట్టారు."
    },
    {
        "id": 117,
        "section": "General Studies",
        "topic": "Current Affairs - Urban Water Sustainability 2026",
        "question_en": "Which metropolitan city became India’s first large city (population over 7 million) to be officially certified as 'Water Positive' in 2026?",
        "question_te": "2026లో అధికారికంగా 'వాటర్ పాజిటివ్' (Water Positive - వినియోగం కంటే ఎక్కువ నీటిని భూగర్భ జలాశయాలకు అందించే నగరం) గా గుర్తింపు పొందిన భారతదేశపు తొలి మెట్రో నగరం ఏది?",
        "options_en": ["Mumbai", "Bengaluru", "Hyderabad", "Chennai"],
        "options_te": ["ముంబై", "బెంగళూరు", "హైదరాబాద్", "చెన్నై"],
        "correct_option": 0,
        "explanation_en": "Mumbai became India's first mega-city with over 7 million population to achieve certified Water Positive status through extensive wastewater recycling and rainwater recharge.",
        "explanation_te": "మురుగునీటి పునర్వినియోగం మరియు విస్తృత వర్షపు నీటి సంరక్షణ ద్వారా 70 లక్షలకు పైగా జనాభా ఉన్న నగరాల్లో ముంబై తొలి వాటర్ పాజిటివ్ నగరంగా నిలిచింది."
    },
    {
        "id": 118,
        "section": "General Studies",
        "topic": "Current Affairs - Deep Ocean Mission 2026",
        "question_en": "Under India’s flagship Deep Ocean Mission, the indigenous human submersible developed to carry 3 humans to a depth of 6,000 meters in the Indian Ocean is named:",
        "question_te": "భారత 'డీప్ ఓషన్ మిషన్' (Deep Ocean Mission) లో భాగంగా ముగ్గురు శాస్త్రవేత్తలను 6,000 మీటర్ల లోతైన సముద్రంలోకి తీసుకువెళ్లేలా స్వదేశీంగా రూపొందించిన మానవ సహిత సబ్‌మెర్సిబుల్ పేరు ఏమిటి?",
        "options_en": ["MATSYA 6000", "SAMUDRA 5000", "SAGARIKAA", "VARUNA 6000"],
        "options_te": ["మత్స్య 6000 (MATSYA 6000)", "సముద్ర 5000", "సాగరిక", "వరుణ 6000"],
        "correct_option": 0,
        "explanation_en": "MATSYA 6000, developed by the National Institute of Ocean Technology (NIOT), Chennai, underwent wet harbor and sea trials in 2026 to explore deep-sea polymetallic nodules.",
        "explanation_te": "చెన్నైలోని జాతీయ సముద్ర సాంకేతిక సంస్థ (NIOT) అభివృద్ధి చేసిన 'మత్స్య 6000' సముద్ర గర్భంలో లోతైన వనరుల అన్వేషణకు కీలకమైన మానవ సహిత సబ్‌మెర్సిబుల్."
    },
    {
        "id": 119,
        "section": "General Studies",
        "topic": "Current Affairs - Aerospace Innovation 2026",
        "question_en": "Which private Indian space-tech startup successfully launched India's second private rocket powered by a single-piece 3D-printed semi-cryogenic engine ('Agnilet')?",
        "question_te": "సింగిల్-పీస్ 3D-ప్రింటెడ్ సెమీ-క్రయోజెనిక్ ఇంజిన్ ('అగ్నిలెట్') తో స్వదేశీ ప్రైవేట్ రాకెట్‌ను విజయవంతంగా ప్రయోగించిన భారతీయ స్పేస్-టెక్ స్టార్టప్ ఏది?",
        "options_en": ["Agnikul Cosmos", "Skyroot Aerospace", "Pixxel", "Bellatrix Aerospace"],
        "options_te": ["అగ్నికుల్ కాస్మోస్ (Agnikul Cosmos)", "స్కైరూట్ ఏరోస్పేస్", "పిక్సెల్", "బెల్లాట్రిక్స్ ఏరోస్పేస్"],
        "correct_option": 0,
        "explanation_en": "IIT Madras-incubated Agnikul Cosmos achieved the orbital-class flight of Agnibaan powered by the world's first single-piece 3D-printed rocket engine Agnilet.",
        "explanation_te": "IIT మద్రాస్ ఇంక్యుబేటెడ్ అగ్నికుల్ కాస్మోస్ ప్రపంచంలోనే తొలిసారిగా సింగిల్-పీస్ 3D ప్రింటెడ్ ఇంజిన్ గల 'అగ్నిబాణ్' రాకెట్‌ను విజయవంతంగా ప్రయోగించింది."
    },
    {
        "id": 120,
        "section": "General Studies",
        "topic": "Current Affairs - Railway Modernization 2026",
        "question_en": "The prototype of India’s first indigenously designed and manufactured Vande Bharat Sleeper Train for long-distance overnight travel was rolled out from:",
        "question_te": "రాత్రిపూట సుదూర ప్రయాణాల కోసం భారతదేశపు మొట్టమొదటి స్వదేశీ 'వందే భారత్ స్లీపర్ రైలు' (Vande Bharat Sleeper) ప్రోటోటైప్ ఏ తయారీ కేంద్రం నుండి బయటకు వచ్చింది?",
        "options_en": ["BEML (Bengaluru)", "ICF (Chennai)", "RCF (Kapurthala)", "Modern Coach Factory (Raebareli)"],
        "options_te": ["BEML (బెంగళూరు)", "ICF (చెన్నై)", "RCF (కపుర్తలా)", "మోడరన్ కోచ్ ఫ్యాక్టరీ (రాయ్‌బరేలి)"],
        "correct_option": 0,
        "explanation_en": "The prototype 16-coach Vande Bharat Sleeper train designed for 160 km/h overnight operations was manufactured and rolled out by BEML in Bengaluru.",
        "explanation_te": "బెంగళూరులోని భారత్ ఎర్త్ మూవర్స్ లిమిటెడ్ (BEML) కర్మాగారం నుండి అత్యాధునిక ప్రపంచ స్థాయి సౌకర్యాలతో కూడిన తొలి వందే భారత్ స్లీపర్ రైలును విడుదల చేశారు."
    }
]

# Update Mock 5
with open('public/data/mock_test_full_200_5.json', 'r', encoding='utf-8') as f:
    mock5 = json.load(f)

for idx, q_new in enumerate(mock5_questions):
    mock5['questions'][100 + idx] = q_new

with open('public/data/mock_test_full_200_5.json', 'w', encoding='utf-8') as f:
    json.dump(mock5, f, ensure_ascii=False, indent=2)

print("Mock Test 5 updated: Q101 to Q120 are 100% 2026 CA & Science/Tech!")

