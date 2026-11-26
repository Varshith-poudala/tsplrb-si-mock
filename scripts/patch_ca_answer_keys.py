import json
import os

def patch_file(filepath, patches):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    is_dict = isinstance(data, dict)
    questions = data.get("questions", []) if is_dict else data

    modified_count = 0
    for q in questions:
        qn = q.get("qNumber", q.get("id"))
        if qn in patches:
            p = patches[qn]
            for key, val in p.items():
                q[key] = val
            modified_count += 1
            print(f"Patched {filepath} Q{qn}: correct_option -> {q.get('correct_option')}")

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {modified_count} questions in {filepath}\n")

# --- MOCK 12 PATCHES ---
mock12_patches = {
    190: {
        "question_en": "What Is The Rank Of India In “World Happiness Report 2026”?",
        "question_te": "ప్రపంచ సంతోష నివేదిక 2026 (World Happiness Report 2026) లో భారతదేశం ర్యాంక్ ఎంత?",
        "options_en": ["110", "116", "120", "130"],
        "options_te": ["110వ", "116వ", "120వ", "130వ"],
        "correct_option": 1,
        "explanation_en": "Published By: UN Sustainable Development Solutions Network (SDSN). India’s Rank: 116th. Finland ranked 1st (happiest country), followed by Iceland (2nd) and Denmark (3rd). Afghanistan ranked last.",
        "explanation_te": "సరైన సమాధానం: 116వ. (UN సస్టైనబుల్ డెవలప్‌మెంట్ సొల్యూషన్స్ నెట్‌వర్క్ విడుదల చేసిన ప్రపంచ సంతోష నివేదిక 2026లో భారతదేశం 116వ ర్యాంకులో నిలిచింది. ఫిన్‌లాండ్ ప్రథమ స్థానంలో నిలవగా, ఐస్‌లాండ్ 2వ స్థానంలో, డెన్మార్క్ 3వ స్థానంలో ఉన్నాయి. ఆఫ్ఘనిస్తాన్ చివరి స్థానంలో ఉంది.)"
    },
    191: {
        "question_en": "What Is The Rank Of India In ‘World Press Freedom Index 2026’?",
        "question_te": "ప్రపంచ పత్రికా స్వేచ్ఛ సూచిక 2026 (World Press Freedom Index 2026) లో భారతదేశం ర్యాంక్ ఎంత?",
        "options_en": ["120", "140", "157", "170"],
        "options_te": ["120వ", "140వ", "157వ", "170వ"],
        "correct_option": 2,
        "explanation_en": "Released by: Reporters Without Borders (RSF). India’s Rank: 157th out of 180 countries. Top Countries: 1. Norway, 2. Netherlands, 3. Estonia. Last Rank: Eritrea (180th).",
        "explanation_te": "సరైన సమాధానం: 157వ. (రిపోర్టర్స్ వితౌట్ బోర్డర్స్ (RSF) విడుదల చేసిన ప్రపంచ పత్రికా స్వేచ్ఛ సూచిక 2026లో 180 దేశాలలో భారతదేశం 157వ స్థానంలో నిలిచింది. నార్వే మొదటి స్థానంలో నిలవగా, నెదర్లాండ్స్ 2వ, ఎస్టోనియా 3వ స్థానంలో ఉన్నాయి. ఎరిట్రియా 180వ స్థానంలో ఉంది.)"
    },
    192: {
        "question_en": "According To SIPRI, What Was India’s Global Rank In Defence Spending In 2025?",
        "question_te": "SIPRI ప్రకారం, 2025లో సైనిక రక్షణ వ్యయంలో ప్రపంచంలో భారతదేశం ర్యాంక్ ఎంత?",
        "options_en": ["3rd", "5th", "7th", "10th"],
        "options_te": ["3వ", "5వ", "7వ", "10వ"],
        "correct_option": 1,
        "explanation_en": "According to SIPRI (Stockholm International Peace Research Institute) Report: Top 5 Military Spenders (2025): 1. United States, 2. China, 3. Russia, 4. Germany, 5. India ($92.1 Billion).",
        "explanation_te": "సరైన సమాధానం: 5వ. (SIPRI నివేదిక ప్రకారం, 2025లో సైనిక రక్షణ వ్యయంలో భారతదేశం $92.1 బిలియన్ల ఖర్చుతో ప్రపంచంలో 5వ స్థానంలో నిలిచింది. మొదటి నాలుగు స్థానాల్లో అమెరికా, చైనా, రష్యా, జర్మనీ ఉన్నాయి.)"
    },
    193: {
        "question_en": "Which Country Ranks 3rd In Renewable Energy Capacity Globally?",
        "question_te": "ప్రపంచంలో పునరుత్పాదక ఇంధన సామర్థ్యంలో (Renewable Energy Capacity) 3వ స్థానంలో ఉన్న దేశం ఏది?",
        "options_en": ["China", "USA", "India", "Germany"],
        "options_te": ["చైనా", "అమెరికా", "భారతదేశం", "జర్మనీ"],
        "correct_option": 2,
        "explanation_en": "According to International Renewable Energy Agency (IRENA) Global Ranking: 1st: China (2,258 GW), 2nd: United States (468 GW), 3rd: India (over 250 GW installed RE capacity).",
        "explanation_te": "సరైన సమాధానం: భారతదేశం. (ఇంటర్నేషనల్ రెన్యూవబుల్ ఎనర్జీ ఏజెన్సీ (IRENA) ప్రకారం పునరుత్పాదక ఇంధన సామర్థ్యంలో చైనా 1వ స్థానంలో, అమెరికా 2వ స్థానంలో మరియు భారతదేశం 250 GW పైగా సామర్థ్యంతో 3వ స్థానంలో ఉన్నాయి.)"
    },
    194: {
        "question_en": "Which Country Was The Largest Arms Importer During 2021–25?",
        "question_te": "2021–25 కాలంలో ప్రపంచంలోనే అత్యధికంగా ఆయుధాలను దిగుమతి చేసుకున్న దేశం ఏది?",
        "options_en": ["India", "China", "Saudi Arabia", "Ukraine"],
        "options_te": ["భారతదేశం", "చైనా", "సౌదీ అరేబియా", "ఉక్రెయిన్"],
        "correct_option": 3,
        "explanation_en": "According to SIPRI (Stockholm International Peace Research Institute): World’s Largest Arms Importers (2021–25): 1. Ukraine, 2. India, 3. Saudi Arabia. The largest global arms supplier was the USA.",
        "explanation_te": "సరైన సమాధానం: ఉక్రెయిన్. (SIPRI నివేదిక ప్రకారం 2021–25 కాలంలో ప్రపంచంలోనే అత్యధికంగా ఆయుధాలను దిగుమతి చేసుకున్న దేశంగా ఉక్రెయిన్ (1వ స్థానం) నిలిచింది, భారతదేశం 2వ స్థానంలో, సౌదీ అరేబియా 3వ స్థానంలో ఉన్నాయి. అమెరికా ప్రధాన సరఫరాదారు.)"
    },
    196: {
        "question_en": "What Is The Rank Of India In “Henley Passport Index 2026”?",
        "question_te": "హెన్లీ పాస్‌పోర్ట్ ఇండెక్స్ 2026 (Henley Passport Index 2026) లో భారతదేశం ర్యాంక్ ఎంత?",
        "options_en": ["80", "87", "78", "90"],
        "options_te": ["80వ", "87వ", "78వ", "90వ"],
        "correct_option": 2,
        "explanation_en": "According to Henley Passport Index 2026, India's passport ranks 78th globally, granting Indian passport holders visa-free access to 56 destinations. Singapore ranks 1st.",
        "explanation_te": "సరైన సమాధానం: 78వ. (హెన్లీ పాస్‌పోర్ట్ ఇండెక్స్ 2026 లో భారతదేశం 78వ ర్యాంకు సాధించింది, 56 దేశాలకు వీసా రహిత ప్రవేశం లభిస్తుంది. సింగపూర్ మొదటి స్థానంలో నిలిచింది.)"
    },
    197: {
        "question_en": "What Is India’s Rank In The Global Soft Power Index 2026?",
        "question_te": "గ్లోబల్ సాఫ్ట్ పవర్ ఇండెక్స్ 2026 (Global Soft Power Index 2026) లో భారతదేశం ర్యాంక్ ఎంత?",
        "options_en": ["28", "32", "40", "50"],
        "options_te": ["28వ", "32వ", "40వ", "50వ"],
        "correct_option": 1,
        "explanation_en": "Published by Brand Finance: Global Soft Power Index 2026 assesses nations across culture, diplomacy, values, governance, and business. India ranked 32nd globally. The United States ranked 1st.",
        "explanation_te": "సరైన సమాధానం: 32వ. (బ్రాండ్ ఫైనాన్స్ విడుదల చేసిన గ్లోబల్ సాఫ్ట్ పవర్ ఇండెక్స్ 2026 లో సంస్కృతి, దౌత్యం, విలువలు మరియు పాలన ఆధారంగా భారతదేశం 32వ ర్యాంకును పొందింది. అమెరికా అగ్రస్థానంలో నిలిచింది.)"
    },
    198: {
        "question_en": "What Is India’s Rank In Corruption Perceptions Index 2025?",
        "question_te": "ట్రాన్స్‌పరెన్సీ ఇంటర్నేషనల్ విడుదల చేసిన అవినీతి అవగాహన సూచిక 2025 (CPI 2025) లో భారతదేశం ర్యాంక్ ఎంత?",
        "options_en": ["84", "91", "96", "102"],
        "options_te": ["84వ", "91వ", "96వ", "102వ"],
        "correct_option": 1,
        "explanation_en": "Published by Transparency International: Corruption Perceptions Index (CPI) 2025 ranks 180 countries. India scored 38 and ranked 91st globally. Denmark topped the index as the least corrupt nation.",
        "explanation_te": "సరైన సమాధానం: 91వ. (ట్రాన్స్‌పరెన్సీ ఇంటర్నేషనల్ విడుదల చేసిన అవినీతి అవగాహన సూచిక 2025 (CPI) లో భారతదేశం 38 స్కోరుతో 91వ స్థానంలో నిలిచింది. డెన్మార్క్ ప్రథమ స్థానంలో నిలిచింది.)"
    },
    199: {
        "question_en": "What Is India’s Rank In The Network Readiness Index 2025?",
        "question_te": "నెట్‌వర్క్ రెడీనెస్ ఇండెక్స్ 2025 (Network Readiness Index 2025) లో భారతదేశం ర్యాంక్ ఎంత?",
        "options_en": ["38", "45", "52", "60"],
        "options_te": ["38వ", "45వ", "52వ", "60వ"],
        "correct_option": 1,
        "explanation_en": "Published by Portulans Institute: Network Readiness Index 2025 measures technology, people, governance, and impact. India secured 45th rank globally. The USA ranked 1st.",
        "explanation_te": "సరైన సమాధానం: 45వ. (పోర్తులాన్స్ ఇన్‌స్టిట్యూట్ విడుదల చేసిన నెట్‌వర్క్ రెడీనెస్ ఇండెక్స్ 2025 లో భారతదేశం 45వ స్థానంలో నిలిచింది. అమెరికా మొదటి స్థానంలో నిలిచింది.)"
    }
}

# --- MOCK 11 PATCHES ---
mock11_patches = {
    193: {
        "question_en": "Who Took The Most Wickets In The 2026 ICC Men’s T20 World Cup?",
        "question_te": "2026 ICC పురుషుల T20 ప్రపంచ కప్‌లో అత్యధిక వికెట్లు తీసిన బౌలర్లు ఎవరు?",
        "options_en": ["Shaheen Afridi", "Jasprit Bumrah & Varun Chakravarthy", "Trent Boult", "Adam Zampa"],
        "options_te": ["షాహీన్ అఫ్రిది", "జస్‌ప్రీత్ బుమ్రా & వరుణ్ చక్రవర్తి", "ట్రెంట్ బౌల్ట్", "ఆడమ్ జంపా"],
        "correct_option": 1,
        "explanation_en": "Most Wickets: Jasprit Bumrah and Varun Chakravarthy jointly took 14 wickets each in the tournament, leading the bowling charts. Most runs were scored by Sahibzada Farhan (PAK).",
        "explanation_te": "సరైన సమాధానం: జస్‌ప్రీత్ బుమ్రా & వరుణ్ చక్రవర్తి. (2026 ICC పురుషుల T20 ప్రపంచ కప్‌లో జస్‌ప్రీత్ బుమ్రా మరియు వరుణ్ చక్రవర్తి చెరో 14 వికెట్లు తీసి సంయుక్తంగా అత్యధిక వికెట్ల వీరులుగా నిలిచారు.)"
    },
    200: {
        "question_en": "Who Became India’s 94th Chess Grandmaster?",
        "question_te": "భారతదేశపు 94వ చెస్ గ్రాండ్‌మాస్టర్‌గా ఎవరు నిలిచారు?",
        "options_en": ["Aaryan Varshney", "R Praggnanandhaa", "Mayank Chakraborty", "Arjun Erigaisi"],
        "options_te": ["ఆర్యన్ వర్ష్ణే", "ఆర్. ప్రజ్ఞానంద", "మయాంక్ చక్రవర్తి", "అర్జున్ ఎరిగైసి"],
        "correct_option": 2,
        "explanation_en": "Mayank Chakraborty became India's 94th Grandmaster, and the first-ever Grandmaster from Assam and the entire Northeastern region of India. (92nd GM: Aaryan Varshney; 93rd GM: Aarav Dengla).",
        "explanation_te": "సరైన సమాధానం: మయాంక్ చక్రవర్తి. (మయాంక్ చక్రవర్తి భారతదేశపు 94వ చెస్ గ్రాండ్‌మాస్టర్‌గా నిలిచారు. అలాగే అస్సాం మరియు మొత్తం ఈశాన్య భారతదేశం నుండి తొలి గ్రాండ్‌మాస్టర్‌గా నిలిచారు.)"
    }
}

# --- MOCK 9 PATCHES ---
mock9_patches = {
    124: {
        "question_en": "Which State Became The Overall Champion Of Khelo India Tribal Games 2026?",
        "question_te": "ఖేలో ఇండియా ట్రైబల్ గేమ్స్ 2026లో ఏ రాష్ట్రం ఓవరాల్ ఛాంపియన్‌గా నిలిచింది?",
        "options_en": ["Odisha", "Jharkhand", "Chhattisgarh", "Karnataka"],
        "options_te": ["ఒడిశా", "జార్ఖండ్", "ఛత్తీస్‌గఢ్", "కర్ణాటక"],
        "correct_option": 3,
        "explanation_en": "Khelo India Tribal Games 2026 (1st Edition): Hosted by Chhattisgarh (Mascot: 'Morveer'). Overall Champion was Karnataka.",
        "explanation_te": "సరైన సమాధానం: కర్ణాటక. (మొదటి ఎడిషన్ ఖేలో ఇండియా ట్రైబల్ గేమ్స్ 2026 ఛత్తీస్‌గఢ్ ఆతిథ్యంలో జరిగాయి (మస్కట్: మోర్వీర్). కర్ణాటక రాష్ట్రం ఓవరాల్ ఛాంపియన్‌గా నిలిచింది.)"
    }
}

# --- MOCK 7 PATCHES ---
mock7_patches = {
    8: {
        "question_en": "Find the total number of even factors of the number 1440.",
        "question_te": "1440 సంఖ్య యొక్క మొత్తం సరి కారణాంకాల (Even Factors) సంఖ్యను కనుగొనండి.",
        "options_en": ["24", "28", "30", "36"],
        "options_te": ["24", "28", "30", "36"],
        "correct_option": 2,
        "explanation_en": "Prime factorization of 1440 = 2^5 * 3^2 * 5^1. For even factors, power of 2 can be 1, 2, 3, 4, 5 (5 choices); power of 3 can be 0, 1, 2 (3 choices); power of 5 can be 0, 1 (2 choices). Total even factors = 5 * 3 * 2 = 30.",
        "explanation_te": "సరైన సమాధానం: 30. (1440 = 2^5 * 3^2 * 5^1. మొత్తం కారణాంకాల సంఖ్య = (5+1)(2+1)(1+1) = 36. బేసి కారణాంకాల సంఖ్య = 1 * (2+1)(1+1) = 6. సరి కారణాంకాల సంఖ్య = 36 - 6 = 30.)"
    },
    37: {
        "question_en": "If α and β are the roots of the equation x² - 6x + 8 = 0, find the value of (α/β + β/α).",
        "question_te": "x² - 6x + 8 = 0 సమీకరణం యొక్క మూలాలు α మరియు β అయితే, (α/β + β/α) విలువ ఎంత?",
        "options_en": ["3/2", "5/2", "7/2", "9/2"],
        "options_te": ["3/2", "5/2", "7/2", "9/2"],
        "correct_option": 1,
        "explanation_en": "For x² - 6x + 8 = 0, roots are α = 4, β = 2. Sum of roots α + β = 6, product of roots αβ = 8. (α/β + β/α) = (α² + β²) / αβ = [(α + β)² - 2αβ] / αβ = [36 - 16] / 8 = 20/8 = 5/2.",
        "explanation_te": "సరైన సమాధానం: 5/2. (మూలాల మొత్తం α + β = 6, మూలాల లబ్దం αβ = 8. (α/β + β/α) = (α² + β²) / αβ = [(α + β)² - 2αβ] / αβ = (36 - 16) / 8 = 20/8 = 5/2.)"
    },
    115: {
        "question_en": "Who Is The Author Of The Book \"Mahatma Gandhi & The Environment\"?",
        "question_te": "\"మహాత్మా గాంధీ & ది ఎన్విరాన్‌మెంట్\" (Mahatma Gandhi & The Environment) పుస్తక రచయిత ఎవరు?",
        "options_en": ["Ramachandra Guha", "Rajmohan Gandhi", "T. N. Khoshoo", "Arundhati Roy"],
        "options_te": ["రామచంద్ర గుహ", "రాజ్‌మోహన్ గాంధీ", "టి. ఎన్. ఖోషూ", "అరుంధతి రాయ్"],
        "correct_option": 2,
        "explanation_en": "\"Mahatma Gandhi and the Environment: Analysing Gandhian Environmental Thought\" was authored by eminent environmental scientist Dr. T. N. Khoshoo.",
        "explanation_te": "సరైన సమాధానం: టి. ఎన్. ఖోషూ. (\"మహాత్మా గాంధీ అండ్ ది ఎన్విరాన్‌మెంట్\" గ్రంథాన్ని ప్రముఖ పర్యావరణ శాస్త్రవేత్త డాక్టర్ టి. ఎన్. ఖోషూ రచించారు.)"
    },
    116: {
        "question_en": "Who Is The Author Of The Book “The Chola Tigers: Avengers Of Somnath”?",
        "question_te": "\"ది చోళ టైగర్స్: అవెంజర్స్ ఆఫ్ సోమనాథ్\" పుస్తక రచయిత ఎవరు?",
        "options_en": ["R. Nagaswamy", "K. A. Nilakanta Sastri", "R. Kannan", "Amish Tripathi"],
        "options_te": ["ఆర్. నాగస్వామి", "కె. ఎ. నీలకంఠ శాస్త్రి", "ఆర్. కన్నన్", "అమిష్ త్రిపాఠి"],
        "correct_option": 3,
        "explanation_en": "\"The Chola Tigers: Avengers of Somnath\" is written by acclaimed bestselling author Amish Tripathi (along with The Immortal Writers’ Circle).",
        "explanation_te": "సరైన సమాధానం: అమిష్ త్రిపాఠి. (\"ది చోళ టైగర్స్: అవెంజర్స్ ఆఫ్ సోమనాథ్\" పుస్తకాన్ని ప్రముఖ రచయిత అమిష్ త్రిపాఠి రచించారు.)"
    },
    117: {
        "question_en": "Who Is The Author Of The Book “Dapaan: Tales From Kashmir’s Conflict”?",
        "question_te": "\"దపాన్: టేల్స్ ఫ్రమ్ కాశ్మీర్స్ కాన్ఫ్లిక్ట్\" పుస్తక రచయిత ఎవరు?",
        "options_en": ["Arundhati Roy", "Shashi Tharoor", "Kiran Desai", "Ipsita Chakravarty"],
        "options_te": ["అరుంధతి రాయ్", "శశి థరూర్", "కిరణ్ దేశాయ్", "ఇప్సితా చక్రవర్తి"],
        "correct_option": 3,
        "explanation_en": "\"Dapaan: Tales from Kashmir's Conflict\" was authored by journalist and author Ipsita Chakravarty.",
        "explanation_te": "సరైన సమాధానం: ఇప్సితా చక్రవర్తి. (\"దపాన్: టేల్స్ ఫ్రమ్ కాశ్మీర్స్ కాన్ఫ్లిక్ట్\" పుస్తకాన్ని ఇప్సితా చక్రవర్తి రచించారు.)"
    },
    118: {
        "question_en": "Who Is The Author Of The Book Titled “Demography, Representation, Delimitation”?",
        "question_te": "\"డెమోగ్రఫీ, రిప్రజెంటేషన్, డీలిమిటేషన్\" పుస్తక రచయిత ఎవరు?",
        "options_en": ["Shashi Tharoor", "Bibek Debroy", "Ramesh Pokhriyal Nishank", "Ravi K Mishra"],
        "options_te": ["శశి థరూర్", "బిబేక్ దేబ్రాయ్", "రమేష్ పోఖ్రియాల్ నిశాంక్", "రవి కె. మిశ్రా"],
        "correct_option": 3,
        "explanation_en": "\"Demography, Representation, Delimitation: The North-South Divide in India\" is authored by Ravi K. Mishra.",
        "explanation_te": "సరైన సమాధానం: రవి కె. మిశ్రా. (\"డెమోగ్రఫీ, రిప్రజెంటేషన్, డీలిమిటేషన్\" పుస్తకాన్ని రవి కె. మిశ్రా రచించారు.)"
    },
    119: {
        "question_en": "Who Is The Author Of The Book \"M. S. Swaminathan: The Man Who Fed India\"?",
        "question_te": "\"ఎం. ఎస్. స్వామినాథన్: ది మ్యాన్ హూ ఫెడ్ ఇండియా\" పుస్తక రచయిత ఎవరు?",
        "options_en": ["A Bhattacharya", "Priyambada Jayakumar", "Shashi Tharoor", "Chetan Bhagat"],
        "options_te": ["ఎ. భట్టాచార్య", "ప్రియంబదా జయకుమార్", "శశి థరూర్", "చేతన్ భగత్"],
        "correct_option": 1,
        "explanation_en": "\"M. S. Swaminathan: The Man Who Fed India\", chronicling the life of the Father of the Green Revolution in India, is authored by Priyambada Jayakumar.",
        "explanation_te": "సరైన సమాధానం: ప్రియంబదా జయకుమార్. (భారత హరిత విప్లవ పితామహుడు డాక్టర్ ఎం.ఎస్. స్వామినాథన్ జీవిత చరిత్ర \"ఎం. ఎస్. స్వామినాథన్: ది మ్యాన్ హూ ఫెడ్ ఇండియా\" పుస్తకాన్ని ప్రియంబదా జయకుమార్ రచించారు.)"
    },
    120: {
        "question_en": "Who Is The Author Of The Book \"Justice Denied Justice Lost\"?",
        "question_te": "\"జస్టిస్ డినైడ్ జస్టిస్ లాస్ట్\" (Justice Denied Justice Lost) పుస్తక రచయిత ఎవరు?",
        "options_en": ["Arundhati Bhattacharya", "Ravish Kumar", "Kanchan Chakraborty", "Barkha Dutt"],
        "options_te": ["అరుంధతి భట్టాచార్య", "రవీష్ కుమార్", "కాంచన్ చక్రవర్తి", "బర్ఖా దత్"],
        "correct_option": 2,
        "explanation_en": "\"Justice Denied Justice Lost\" is authored by Kanchan Chakraborty.",
        "explanation_te": "సరైన సమాధానం: కాంచన్ చక్రవర్తి. (\"జస్టిస్ డినైడ్ జస్టిస్ లాస్ట్\" పుస్తకాన్ని కాంచన్ చక్రవర్తి రచించారు.)"
    },
    121: {
        "question_en": "Who Is The Author Of The Book \"PMO: Prime Minister’s Office Through The Years\"?",
        "question_te": "\"పీఎంఓ: ప్రైమ్ మినిస్టర్స్ ఆఫీస్ త్రూ ది ఇయర్స్\" పుస్తక రచయిత ఎవరు?",
        "options_en": ["Sanjay Baru", "Himanshu Roy", "P. N. Haksar", "Vinay Sitapati"],
        "options_te": ["సంజయ్ బారు", "హిమాంశు రాయ్", "పి. ఎన్. హక్సర్", "వినయ్ సీతాపతి"],
        "correct_option": 1,
        "explanation_en": "\"PMO: Prime Minister's Office Through The Years\" is authored by Prof. Himanshu Roy.",
        "explanation_te": "సరైన సమాధానం: హిమాంశు రాయ్. (\"పీఎంఓ: ప్రైమ్ మినిస్టర్స్ ఆఫీస్ త్రూ ది ఇయర్స్\" గ్రంథాన్ని ప్రొఫెసర్ హిమాంశు రాయ్ రచించారు.)"
    },
    122: {
        "question_en": "Who Is The Author Of The Book \"Operation SINDOOR: The Untold Story Of India’s Deep Strikes Inside Pakistan\"?",
        "question_te": "\"ఆపరేషన్ సిందూర్: ది అన్‌టోల్డ్ స్టోరీ ఆఫ్ ఇండియాస్ డీప్ స్ట్రైక్స్ ఇన్‌సైడ్ పాకిస్తాన్\" పుస్తక రచయిత ఎవరు?",
        "options_en": ["Vikram Singh", "Kanwal Jeet Singh Dhillon", "Ajay Kumar", "Anand Ranganathan"],
        "options_te": ["విక్రమ్ సింగ్", "కన్వల్ జీత్ సింగ్ ధిల్లాన్", "అజయ్ కుమార్", "ఆనంద్ రంగనాథన్"],
        "correct_option": 1,
        "explanation_en": "\"Operation SINDOOR: The Untold Story Of India’s Deep Strikes Inside Pakistan\" is authored by Lt. Gen. K. J. S. 'Tiny' Dhillon (Retd.).",
        "explanation_te": "సరైన సమాధానం: కన్వల్ జీత్ సింగ్ ధిల్లాన్. (\"ఆపరేషన్ సిందూర్: ది అన్‌టోల్డ్ స్టోరీ ఆఫ్ ఇండియాస్ డీప్ స్ట్రైక్స్ ఇన్‌సైడ్ పాకిస్తాన్\" పుస్తకాన్ని లెఫ్టినెంట్ జనరల్ కె.జె.ఎస్. 'టైనీ' ధిల్లాన్ రచించారు.)"
    },
    123: {
        "question_en": "Who Is The Author Of The Book “Mother Mary Comes To Me”?",
        "question_te": "\"మదర్ మేరీ కమ్స్ టు మీ\" (Mother Mary Comes To Me) పుస్తక రచయిత ఎవరు?",
        "options_en": ["Kiran Desai", "Jhumpa Lahiri", "Arundhati Roy", "Anita Desai"],
        "options_te": ["కిరణ్ దేశాయ్", "జుంపా లాహిరి", "అరుంధతి రాయ్", "అనితా దేశాయ్"],
        "correct_option": 2,
        "explanation_en": "\"Mother Mary Comes To Me\" is a memoir authored by Booker Prize-winning author Arundhati Roy.",
        "explanation_te": "సరైన సమాధానం: అరుంధతి రాయ్. (\"మదర్ మేరీ కమ్స్ టు మీ\" పుస్తకాన్ని బుకర్ ప్రైజ్ గ్రహీత అరుంధతి రాయ్ రచించారు.)"
    },
    126: {
        "question_en": "Which Film Won The Best Film Award At Oscars 2026?",
        "question_te": "2026 ఆస్కార్ అవార్డులలో ఏ చిత్రం 'ఉత్తమ చిత్రం' (Best Picture) అవార్డును గెలుచుకుంది?",
        "options_en": ["Hamnet", "Sinners", "One Battle After Another", "Frankenstein"],
        "options_te": ["హ్యామ్నెట్", "సిన్నర్స్", "వన్ బ్యాటిల్ ఆఫ్టర్ అనదర్", "ఫ్రాంకెన్‌స్టీన్"],
        "correct_option": 2,
        "explanation_en": "At the 98th Academy Awards (Oscars 2026), 'One Battle After Another' (directed by Paul Thomas Anderson) won Best Picture and Best Director.",
        "explanation_te": "సరైన సమాధానం: వన్ బ్యాటిల్ ఆఫ్టర్ అనదర్. (98వ అకాడమీ అవార్డులు (ఆస్కార్స్ 2026) లో పాల్ థామస్ ఆండర్సన్ దర్శకత్వం వహించిన 'వన్ బ్యాటిల్ ఆఫ్టర్ అనదర్' చిత్రం ఉత్తమ చిత్రంగా (Best Picture) అవార్డు గెలుచుకుంది.)"
    },
    130: {
        "question_en": "Which Indian Film Won A BAFTA Award In 2026?",
        "question_te": "2026లో ఏ భారతీయ చిత్రం BAFTA అవార్డును గెలుచుకుంది?",
        "options_en": ["Homebound", "RRR", "Boong", "12th Fail"],
        "options_te": ["హోమ్‌బౌండ్", "RRR", "బూంగ్", "12త్ ఫెయిల్"],
        "correct_option": 2,
        "explanation_en": "\"Boong\", a Manipuri film directed by Lakshmipriya Devi, became the first Indian film to win a BAFTA Award in the Best Children's & Family Film category.",
        "explanation_te": "సరైన సమాధానం: బూంగ్. (లక్ష్మీప్రియా దేవి దర్శకత్వం వహించిన మణిపురి చిత్రం 'బూంగ్' (Boong) 2026 బాఫ్టా (BAFTA) అవార్డులలో ఉత్తమ చిల్డ్రన్స్ & ఫ్యామిలీ ఫిల్మ్ విభాగంలో అవార్డు గెలుచుకున్న తొలి భారతీయ చిత్రంగా నిలిచింది.)"
    }
}

# --- MOCK 6 PATCHES ---
mock6_patches = {
    109: {
        "question_en": "India’s First Indigenous Hydrogen Fuel Cell Passenger Ferry Vessel Was Launched In Which City?",
        "question_te": "భారతదేశపు మొట్టమొదటి స్వదేశీ హైడ్రోజన్ ఫ్యూయెల్ సెల్ ప్యాసింజర్ ఫెర్రీ బోట్ ఏ నగరంలో ప్రారంభించబడింది?",
        "options_en": ["Prayagraj", "Patna", "Kolkata", "Varanasi"],
        "options_te": ["ప్రయాగ్‌రాజ్", "పాట్నా", "కోల్‌కతా", "వారణాసి"],
        "correct_option": 3,
        "explanation_en": "India’s first indigenous zero-emission hydrogen fuel cell passenger catamaran was built by Cochin Shipyard Limited and flagged off for commercial operations at Namo Ghat in Varanasi, Uttar Pradesh, on River Ganga.",
        "explanation_te": "సరైన సమాధానం: వారణాసి. (కొచ్చిన్ షిప్‌యార్డ్ నిర్మించిన భారతదేశపు మొట్టమొదటి స్వదేశీ హైడ్రోజన్ ఫ్యూయెల్ సెల్ ప్యాసింజర్ ఫెర్రీ నౌకను ఉత్తరప్రదేశ్‌లోని వారణాసిలోని నమో ఘాట్ వద్ద గంగా నదిపై ప్రారంభించారు.)"
    },
    116: {
        "question_en": "Which State Won The “Best State For Promotion Of Aviation And Ecosystem” Award At Wings India 2026?",
        "question_te": "వింగ్స్ ఇండియా 2026 లో \"బెస్ట్ స్టేట్ ఫర్ ప్రమోషన్ ఆఫ్ ఏవియేషన్ అండ్ ఎకోసిస్టమ్\" అవార్డును ఏ రాష్ట్రం గెలుచుకుంది?",
        "options_en": ["Himachal Pradesh", "Uttarakhand", "Sikkim", "Arunachal Pradesh"],
        "options_te": ["హిమాచల్ ప్రదేశ్", "ఉత్తరాఖండ్", "సిక్కిం", "అరుణాచల్ ప్రదేశ్"],
        "correct_option": 1,
        "explanation_en": "At Wings India 2026 held at Begumpet Airport, Hyderabad, Uttarakhand was awarded 'Best State for Promotion of Aviation and Ecosystem' for its rapid expansion of regional air connectivity and heliports.",
        "explanation_te": "సరైన సమాధానం: ఉత్తరాఖండ్. (హైదరాబాద్‌లోని బేగంపేట విమానాశ్రయంలో జరిగిన వింగ్స్ ఇండియా 2026 సదస్సులో హెలిపోర్టులు, ప్రాంతీయ విమానయాన విస్తరణకు గాను ఉత్తరాఖండ్ రాష్ట్రం \"బెస్ట్ స్టేట్ ఫర్ ప్రమోషన్ ఆఫ్ ఏవియేషన్ అండ్ ఎకోసిస్టమ్\" అవార్డును గెలుచుకుంది.)"
    },
    118: {
        "question_en": "India’s First LNG–Diesel Dual-Fuel DEMU Train Was Flagged Off From Which City?",
        "question_te": "భారతదేశపు మొట్టమొదటి ఎల్‌ఎన్‌జి-డీజిల్ డ్యూయల్-ఫ్యూయెల్ డీఈఎమ్‌యు (DEMU) రైలు ఏ నగరం నుండి ప్రారంభించబడింది?",
        "options_en": ["Surat", "Vadodara", "Ahmedabad", "Rajkot"],
        "options_te": ["సూరత్", "వడోదర", "అహ్మదాబాద్", "రాజ్‌కోట్"],
        "correct_option": 2,
        "explanation_en": "India’s first LNG-Diesel dual-fuel DEMU train was retrofitted at Sabarmati Coach Depot and flagged off by Union Home Minister Amit Shah from Sabarmati in Ahmedabad, Gujarat, on the Sabarmati–Mahesana section.",
        "explanation_te": "సరైన సమాధానం: అహ్మదాబాద్. (భారతదేశపు తొలి ఎల్‌ఎన్‌జి-డీజిల్ డ్యూయల్ ఫ్యూయెల్ డీఈఎమ్‌యు రైలును గుజరాత్‌లోని అహ్మదాబాద్ (సబర్మతి) నుండి సబర్మతి-మహేసానా మార్గంలో ప్రారంభించారు.)"
    },
    120: {
        "question_en": "Which State Became The First In India To Introduce A Dedicated ‘Elderly Budget’ In FY 2026–27?",
        "question_te": "2026–27 ఆర్థిక సంవత్సర బడ్జెట్‌లో వృద్ధుల కోసం ప్రత్యేక 'ఎల్డర్లీ బడ్జెట్' (Elderly Budget) ప్రవేశపెట్టిన దేశంలోనే మొదటి రాష్ట్రం ఏది?",
        "options_en": ["Tamil Nadu", "Kerala", "Karnataka", "Maharashtra"],
        "options_te": ["తమిళనాడు", "కేరళ", "కర్ణాటక", "మహారాష్ట్ర"],
        "correct_option": 1,
        "explanation_en": "Kerala became the first state in India to introduce a dedicated 'Elderly Budget' (Senior Citizen Budget) in its 2026–27 State Budget, targeting geriatric health, social welfare, and care infrastructure.",
        "explanation_te": "సరైన సమాధానం: కేరళ. (కేరళ రాష్ట్రం తన 2026–27 బడ్జెట్‌లో వృద్ధుల సంక్షేమం, ఆరోగ్య సంరక్షణ కోసం దేశంలోనే మొట్టమొదటిసారిగా ప్రత్యేక 'ఎల్డర్లీ బడ్జెట్'ను ప్రవేశపెట్టింది.)"
    },
    125: {
        "question_en": "Which Large Metropolis (Population Over 7 Million) Is Set To Become India's First Large Slum-Free City?",
        "question_te": "70 లక్షలకు పైగా జనాభా కలిగిన భారత మెట్రో నగరాల్లో తొలి స్లమ్-ఫ్రీ (మురికివాడల రహిత) నగరంగా నిలిచే దిశగా ఉన్న నగరం ఏది?",
        "options_en": ["Mumbai", "Hyderabad", "Surat", "Pune"],
        "options_te": ["ముంబై", "హైదరాబాద్", "సూరత్", "పూణే"],
        "correct_option": 2,
        "explanation_en": "Surat (Gujarat), with a population exceeding 7 million, is recognized as India's first large mega-city on track to become completely slum-free through intensive in-situ slum redevelopment and affordable housing projects. (Chandigarh was the first small city).",
        "explanation_te": "సరైన సమాధానం: సూరత్. (70 లక్షల పైగా జనాభా ఉన్న నగరాల్లో గుజరాత్‌లోని సూరత్ నగరం విస్తృత గృహ నిర్మాణ పథకాలు, రీడెవలప్‌మెంట్ ద్వారా భారతదేశపు మొట్టమొదటి పెద్ద స్లమ్-ఫ్రీ నగరంగా నిలిచింది.)"
    },
    127: {
        "question_en": "India’s First Sleeper Vande Bharat Train Connects Which Cities?",
        "question_te": "భారతదేశపు మొట్టమొదటి వందే భారత్ స్లీపర్ రైలు ఏ నగరాల మధ్య నడుస్తుంది?",
        "options_en": ["Delhi – Mumbai", "Kolkata – Guwahati", "Chennai – Bengaluru", "Patna – Ranchi"],
        "options_te": ["ఢిల్లీ – ముంబై", "కోల్‌కతా – గౌహతి", "చెన్నై – బెంగళూరు", "పాట్నా – రాంచీ"],
        "correct_option": 1,
        "explanation_en": "India’s first Vande Bharat Sleeper train connects Howrah (Kolkata) in West Bengal with Kamakhya (Guwahati) in Assam, covering a distance of 972 km.",
        "explanation_te": "సరైన సమాధానం: కోల్‌కతా – గౌహతి. (భారతదేశపు మొట్టమొదటి వందే భారత్ స్లీపర్ రైలు హౌరా (కోల్‌కతా) మరియు కామాఖ్య (గౌహతి) నగరాల మధ్య 972 కి.మీ దూరాన్ని కలుపుతూ ప్రారంభించబడింది.)"
    },
    128: {
        "question_en": "Which City Has Become Uttar Pradesh’s First Zero Fresh Waste Dump City?",
        "question_te": "ఉత్తరప్రదేశ్‌లో 100% ఘన వ్యర్థాలను శాస్త్రీయంగా శుద్ధి చేస్తూ తొలి జీరో ఫ్రెష్ వేస్ట్ డంప్ నగరంగా (Zero Fresh Waste Dump City) ఏది అవతరించింది?",
        "options_en": ["Kanpur", "Varanasi", "Lucknow", "Prayagraj"],
        "options_te": ["కాన్పూర్", "వారణాసి", "లక్నో", "ప్రయాగ్‌రాజ్"],
        "correct_option": 2,
        "explanation_en": "Lucknow became Uttar Pradesh's first zero fresh waste dump city by scientifically processing 100% of its municipal solid waste daily under the Swachh Bharat Mission-Urban.",
        "explanation_te": "సరైన సమాధానం: లక్నో. (స్వచ్ఛ భారత్ మిషన్-అర్బన్ కింద ప్రతిరోజూ 100% మున్సిపల్ ఘన వ్యర్థాలను శాస్త్రీయంగా శుద్ధి చేస్తూ ఉత్తరప్రదేశ్‌లోనే తొలి జీరో ఫ్రెష్ వేస్ట్ డంప్ సిటీగా లక్నో నిలిచింది.)"
    },
    129: {
        "question_en": "India’s First AI-Enabled State University Pilot Project Has Been Launched At Which University?",
        "question_te": "భారతదేశంలో తొలిసారిగా ఆర్టిఫిషియల్ ఇంటెలిజెన్స్ (AI) ఆధారిత స్టేట్ యూనివర్సిటీ పైలట్ ప్రాజెక్ట్ ఏ విశ్వవిద్యాలయంలో ప్రారంభించబడింది?",
        "options_en": ["Delhi University", "Banaras Hindu University", "Aligarh Muslim University", "CCSU Meerut"],
        "options_te": ["ఢిల్లీ విశ్వవిద్యాలయం", "బనారస్ హిందూ విశ్వవిద్యాలయం", "అలీఘర్ ముస్లిం విశ్వవిద్యాలయం", "సీసీఎస్‌యూ మీరట్"],
        "correct_option": 3,
        "explanation_en": "India’s first AI-enabled state university pilot project was launched at Chaudhary Charan Singh University (CCSU), Meerut, in strategic partnership with Google Cloud.",
        "explanation_te": "సరైన సమాధానం: సీసీఎస్‌యూ మీరట్. (గూగుల్ క్లౌడ్ సహకారంతో భారతదేశంలోనే మొట్టమొదటి ఏఐ ఆధారిత రాష్ట్ర విశ్వవిద్యాలయ పైలట్ ప్రాజెక్ట్‌ను చౌదరి చరణ్ సింగ్ విశ్వవిద్యాలయం (CCSU), మీరట్‌లో ప్రారంభించారు.)"
    }
}

# --- MOCK 1 & MOCK 3 PATCHES (Father-son age question) ---
mock1_3_patches = {
    8: {
        "question_en": "The ratio of the present ages of a father and son is 7 : 3. Eight years ago, the ratio of their ages was 5 : 1. What will be the father's age 5 years from now?",
        "question_te": "ఒక తండ్రి మరియు కొడుకుల ప్రస్తుత వయస్సుల నిష్పత్తి 7 : 3. ఎనిమిది సంవత్సరాల క్రితం వారి వయస్సుల నిష్పత్తి 5 : 1 గా ఉండేది. ఇప్పటి నుండి 5 సంవత్సరాల తర్వాత తండ్రి వయస్సు ఎంత అవుతుంది?",
        "options_en": ["33 years", "37 years", "40 years", "47 years"],
        "options_te": ["33 సంవత్సరాలు", "37 సంవత్సరాలు", "40 సంవత్సరాలు", "47 సంవత్సరాలు"],
        "correct_option": 0,
        "explanation_en": "Let present ages be 7x and 3x. Eight years ago: (7x - 8) / (3x - 8) = 5/1 => 7x - 8 = 15x - 40 => 8x = 32 => x = 4. Father's present age = 7 * 4 = 28 years. After 5 years, father's age = 28 + 5 = 33 years.",
        "explanation_te": "సరైన సమాధానం: 33 సంవత్సరాలు. (ప్రస్తుత వయస్సులు 7x, 3x అనుకుందాం. 8 సంవత్సరాల క్రితం: (7x - 8) / (3x - 8) = 5/1 => 7x - 8 = 15x - 40 => 8x = 32 => x = 4. తండ్రి ప్రస్తుత వయస్సు = 7 * 4 = 28 సంవత్సరాలు. 5 సంవత్సరాల తర్వాత తండ్రి వయస్సు = 28 + 5 = 33 సంవత్సరాలు.)"
    }
}

# --- MOCK 10 PATCHES (Alternate days work) ---
mock10_patches = {
    19: {
        "question_en": "A and B working alone can complete a job in 12 days and 16 days respectively. If they work on alternate days with A starting on the first day, in how many days will the entire job be finished?",
        "question_te": "A మరియు B లు ఒంటరిగా ఒక పనిని వరుసగా 12 రోజులు మరియు 16 రోజులలో పూర్తి చేయగలరు. A మొదటి రోజున పనిని ప్రారంభిస్తూ వారు రోజు విడిచి రోజు పనిచేస్తే, మొత్తం పని ఎన్ని రోజుల్లో పూర్తవుతుంది?",
        "options_en": ["13(1/3) days", "13(2/3) days", "13(3/4) days", "14 days"],
        "options_te": ["13(1/3) రోజులు", "13(2/3) రోజులు", "13(3/4) రోజులు", "14 రోజులు"],
        "correct_option": 1,
        "explanation_en": "Total work = LCM(12, 16) = 48 units. Daily efficiencies: A = 4 units/day, B = 3 units/day. In a 2-day cycle: 4 + 3 = 7 units. In 6 two-day cycles (12 days): 6 * 7 = 42 units completed. Remaining work = 48 - 42 = 6 units. Day 13: A completes 4 units (total 46 units completed). Remaining work = 2 units. Day 14: B works with rate 3 units/day, taking 2/3 day. Total time = 12 + 1 + 2/3 = 13(2/3) days.",
        "explanation_te": "సరైన సమాధానం: 13(2/3) రోజులు. (మొత్తం పని = 48 యూనిట్లు. A సామర్థ్యం = 4 యూనిట్లు/రోజు, B = 3 యూనిట్లు/రోజు. 2 రోజుల సైకిల్‌లో = 7 యూనిట్లు. 6 సైకిళ్లలో (12 రోజులు) = 42 యూనిట్లు పూర్తవుతాయి. మిగిలిన పని = 6 యూనిట్లు. 13వ రోజున A 4 యూనిట్లు చేస్తాడు (మొత్తం 46 యూనిట్లు). మిగిలిన 2 యూనిట్లను B (సామర్థ్యం 3) 2/3 రోజులో పూర్తి చేస్తాడు. మొత్తం కాలం = 13(2/3) రోజులు.)"
    }
}

# --- MOCK 13 PATCHES (Water image clock) ---
mock13_patches = {
    60: {
        "question_en": "A clock shows 4:15. What would be its water image reflection time?",
        "question_te": "ఒక గడియారంలో సమయం 4:15 అయినప్పుడు, దాని నీటి ప్రతిబింబ సమయం (Water Image) ఎంత అవుతుంది?",
        "options_en": ["2:15", "1:45", "2:45", "1:15"],
        "options_te": ["2:15", "1:45", "2:45", "1:15"],
        "correct_option": 0,
        "explanation_en": "Water image formula for clocks: Subtract the given time from 18:30 (when minutes <= 30). Here, 18:30 - 4:15 = 14:15 = 2:15.",
        "explanation_te": "సరైన సమాధానం: 2:15. (గడియారపు నీటి ప్రతిబింబ సూత్రం: నిమిషాలు <= 30 ఉన్నప్పుడు 18:30 నుండి తీసివేయాలి. 18:30 - 4:15 = 14:15 = 2:15.)"
    }
}

if __name__ == "__main__":
    patch_file("public/data/mock_test_full_200_12.json", mock12_patches)
    patch_file("public/data/mock_test_full_200_11.json", mock11_patches)
    patch_file("public/data/mock_test_full_200_9.json", mock9_patches)
    patch_file("public/data/mock_test_full_200_7.json", mock7_patches)
    patch_file("public/data/mock_test_full_200_6.json", mock6_patches)
    patch_file("public/data/mock_test_full_200.json", mock1_3_patches)
    patch_file("public/data/mock_test_full_200_3.json", mock1_3_patches)
    patch_file("public/data/mock_test_full_200_10.json", mock10_patches)
    patch_file("public/data/mock_test_full_200_13.json", mock13_patches)

    # Also patch reference_studynow_ca_2026.json
    ref_path = "public/data/reference_studynow_ca_2026.json"
    if os.path.exists(ref_path):
        with open(ref_path, "r", encoding="utf-8") as f:
            ref_data = json.load(f)
        
        # Build lookup by matching question_en
        all_ca_patches = {**mock12_patches, **mock11_patches, **mock9_patches, **mock7_patches, **mock6_patches}
        ref_updated = 0
        for r in ref_data:
            r_en = r.get("question_en", "").strip().lower()
            for qn, p in all_ca_patches.items():
                p_en = p["question_en"].strip().lower()
                if r_en == p_en or (len(p_en) > 20 and (r_en.startswith(p_en[:20]) or p_en.startswith(r_en[:20]))):
                    for k, v in p.items():
                        r[k] = v
                    ref_updated += 1
                    break
        with open(ref_path, "w", encoding="utf-8") as f:
            json.dump(ref_data, f, ensure_ascii=False, indent=2)
        print(f"Updated {ref_updated} items in {ref_path}")
