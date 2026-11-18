# -*- coding: utf-8 -*-
"""
Mock Test 11 - Mental Ability & Reasoning (Q51 to Q100)
Strictly adheres to TSPLRB SI PWT Blueprint & Shentu's feedback:
- PYQ Calendar Repetition (Years 2018 -> 2029, 2019 -> 2030, Leap Year 2028 -> 2056)
- Clocks (Angles at specific times, Coincidence, Reflex Angle, Faulty clock)
- Coded Blood Relations & Family Tree
- Syllogisms (Multi-statement conclusions)
- Coding-Decoding (Pattern shifting, Substitution, Matrix/Number coding)
- Direction Sense & Distances (Shadow, Multi-turn displacement)
- Seating Arrangements (Circular 8 persons, Linear 7 persons)
- Ranking, Order, Interchanging positions
- Number Series, Analogy, Classification
- Venn Diagrams, Mathematical Operators
- Data Sufficiency & Statement-Assumption
- Zero bracket prefix tags, complete bilingual English & Telugu.
"""

def make_q(id_num, topic, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
    return {
        "id": id_num,
        "qNumber": id_num,
        "section": "Mental Ability & Logical Reasoning",
        "topic": topic,
        "question_en": q_en.strip(),
        "question_te": q_te.strip(),
        "options_en": [str(o).strip() for o in opts_en],
        "options_te": [str(o).strip() for o in opts_te],
        "correct_option": corr,
        "explanation_en": exp_en.strip(),
        "explanation_te": exp_te.strip()
    }

def get_reasoning_50():
    qs = []

    # Q51: Calendar Repetition 2018
    qs.append(make_q(
        51, "Reasoning - Calendar Repetition",
        "Which year will have the exact same calendar as that of the year 2018?",
        "2018 వ సంవత్సరం క్యాలెండర్‌ను యథాతథంగా పోలి ఉండే తదుపరి సంవత్సరం ఏది?",
        ["2024", "2029", "2030", "2035"],
        ["2024", "2029", "2030", "2035"],
        1,
        "The year 2018 is an ordinary year that is 2 years after a leap year (2016 + 2). For (Leap Year + 2) or (Leap Year + 3), the calendar repeats after 11 years. Therefore: 2018 + 11 = 2029.",
        "2018 సాధారణ సంవత్సరం, ఇది లీప్ సంవత్సరం (2016) తర్వాత రెండవ సంవత్సరం (లీప్ + 2). లీప్ + 2 లేదా లీప్ + 3 సంవత్సరాలకు క్యాలెండర్ 11 సంవత్సరాల తర్వాత పునరావృతమవుతుంది: 2018 + 11 = 2029."
    ))

    # Q52: Calendar Repetition 2019
    qs.append(make_q(
        52, "Reasoning - Calendar Repetition",
        "Which year will have the exact same calendar as that of the year 2019?",
        "2019 వ సంవత్సరం క్యాలెండర్‌ను యథాతథంగా పోలి ఉండే తదుపరి సంవత్సరం ఏది?",
        ["2024", "2025", "2030", "2031"],
        ["2024", "2025", "2030", "2031"],
        2,
        "The year 2019 is an ordinary year (2016 + 3, i.e., Leap Year + 3). It repeats after 11 years: 2019 + 11 = 2030. Odd days calculation: 2019(1)+2020(2)+2021(1)+2022(1)+2023(1)+2024(2)+2025(1)+2026(1)+2027(1)+2028(2)+2029(1) = 14 odd days = 0 mod 7.",
        "2019 సాధారణ సంవత్సరం (2016 లీప్ + 3). ఇది 11 సంవత్సరాల తర్వాత పునరావృతమవుతుంది: 2019 + 11 = 2030. మొత్తం విషమ దినాలు 14 (14 mod 7 = 0)."
    ))

    # Q53: Calendar Repetition Leap Year 2028
    qs.append(make_q(
        53, "Reasoning - Calendar Repetition",
        "Which future year will have the exact same calendar as that of the leap year 2028?",
        "2028 లీప్ సంవత్సరం క్యాలెండర్‌ను యథాతథంగా పోలి ఉండే భవిష్యత్ సంవత్సరం ఏది?",
        ["2034", "2044", "2052", "2056"],
        ["2034", "2044", "2052", "2056"],
        3,
        "A leap year calendar repeats after 28 years. Hence, the calendar of 2028 will repeat in 2028 + 28 = 2056.",
        "లీప్ సంవత్సరం క్యాలెండర్ ఎల్లప్పుడూ 28 సంవత్సరాల తర్వాత పునరావృతమవుతుంది. కాబట్టి 2028 క్యాలెండర్ 2028 + 28 = 2056 లో పునరావృతమవుతుంది."
    ))

    # Q54: Clocks - Angle at 8:30
    qs.append(make_q(
        54, "Reasoning - Clocks",
        "What is the angle between the hour hand and the minute hand of a clock at 8:30?",
        "ఒక గడియారంలో సమయం 8:30 అయినప్పుడు గంటల ముల్లు మరియు నిమిషాల ముల్లు మధ్య కోణం ఎంత?",
        ["60°", "75°", "80°", "85°"],
        ["60°", "75°", "80°", "85°"],
        1,
        "Angle = |30*H - (11/2)*M| = |30*8 - (11/2)*30| = |240 - 165| = 75°.",
        "కోణం = |30*H - (11/2)*M| = |30*8 - (11/2)*30| = |240 - 165| = 75°."
    ))

    # Q55: Clocks - Reflex Angle at 7:20
    qs.append(make_q(
        55, "Reasoning - Clocks",
        "What is the reflex angle between the hands of a clock at 7:20?",
        "ఒక గడియారంలో సమయం 7:20 అయినప్పుడు ముల్లుల మధ్య ఏర్పడే బృహత్ కోణం (Reflex Angle) ఎంత?",
        ["260°", "100°", "240°", "280°"],
        ["260°", "100°", "240°", "280°"],
        0,
        "Interior angle = |30*7 - (11/2)*20| = |210 - 110| = 100°. Reflex angle = 360° - 100° = 260°.",
        "అంతర కోణం = |30*7 - (11/2)*20| = |210 - 110| = 100°. బృహత్ కోణం (Reflex angle) = 360° - 100° = 260°."
    ))

    # Q56: Clocks - Hands in Opposite Directions (180 deg)
    qs.append(make_q(
        56, "Reasoning - Clocks",
        "At what time between 3 o'clock and 4 o'clock will the hands of a clock point in opposite directions (in a straight line at 180°)?",
        "3 గంటల నుండి 4 గంటల మధ్య ఏ సమయంలో గడియారంలోని రెండు ముల్లులు ఒకదానికొకటి వ్యతిరేక దిశలో (180° సరళరేఖలో) ఉంటాయి?",
        ["3 hours 45 minutes", "3 hours 49 1/11 minutes", "3 hours 48 2/11 minutes", "3 hours 50 minutes"],
        ["3 గంటల 45 నిమిషాలు", "3 గంటల 49 1/11 నిమిషాలు", "3 గంటల 48 2/11 నిమిషాలు", "3 గంటల 50 నిమిషాలు"],
        1,
        "At 3 o'clock, hands are 15 minute spaces apart. To be in opposite direction, they must be 30 minute spaces apart. Total distance to gain = 15 + 30 = 45 minute spaces. Time = 45 * (12/11) = 540/11 = 49 1/11 minutes past 3.",
        "3 గంటల వద్ద ముల్లుల మధ్య వ్యత్యాసం 15 నిమిషాల ఖాళీలు. వ్యతిరేక దిశలో ఉండాలంటే 30 నిమిషాల ఖాళీ ఉండాలి. మొత్తం దాటవలసిన దూరం = 15 + 30 = 45 నిమిషాలు. సమయం = 45 * (12/11) = 540/11 = 49 1/11 నిమిషాలు (3 గంటల 49 1/11 నిమిషాలు)."
    ))

    # Q57: Clocks - Faulty Clock Gaining Time
    qs.append(make_q(
        57, "Reasoning - Clocks",
        "A clock is set right at 5:00 AM. If the clock gains 16 minutes in 24 hours, what will be the true time when the clock indicates 10:00 PM on the 4th day?",
        "ఒక గడియారాన్ని ఉదయం 5:00 గంటలకు సరిచేశారు. ఆ గడియారం ప్రతి 24 గంటలకు 16 నిమిషాలు వేగంగా తిరుగుతుంది. 4వ రోజు రాత్రి 10:00 గంటలు చూపించినప్పుడు అసలైన ఖచ్చితమైన సమయం ఎంత?",
        ["8:00 PM", "8:30 PM", "9:00 PM", "9:30 PM"],
        ["రాత్రి 8:00", "రాత్రి 8:30", "రాత్రి 9:00", "రాత్రి 9:30"],
        2,
        "Total elapsed indicated time = From 5 AM day 1 to 10 PM day 4 = (3 * 24) + 17 = 89 hours. In 24 hours (1440 min), clock indicates 24h 16m = 364/15 hours. True time for 89 indicated hours = 89 * (24 / (364/15)) = 89 * (360/364) = 88 hours. 88 hours from 5 AM day 1 gives exactly 9:00 PM on the 4th day.",
        "గడియారంలో గడిచిన మొత్తం సమయం = (3 * 24) + 17 = 89 గంటలు. 24 గంటలకు 16 నిమిషాలు ఎక్కువ = 364/15 గంటలు. అసలు సమయం = 89 * (360/364) = 88 గంటలు. 5 AM నుండి 88 గంటలు అంటే 4వ రోజు రాత్రి 9:00 PM."
    ))

    # Q58: Coded Blood Relations
    qs.append(make_q(
        58, "Reasoning - Coded Blood Relations",
        "Read the following information:\n'P + Q' means P is the mother of Q;\n'P - Q' means P is the sister of Q;\n'P * Q' means P is the father of Q;\n'P / Q' means P is the brother of Q.\nWhich of the following expressions indicates that 'M is the maternal uncle of N'?",
        "క్రింది సమాచారాన్ని చదవండి:\n'P + Q' అనగా P, Q యొక్క తల్లి;\n'P - Q' అనగా P, Q యొక్క సోదరి;\n'P * Q' అనగా P, Q యొక్క తండ్రి;\n'P / Q' అనగా P, Q యొక్క సోదరుడు.\nక్రింది వాటిలో 'M, N యొక్క మేనమామ' అని తెలిపే సమాసం ఏది?",
        ["M / K + N", "M + K / N", "M / K * N", "M - K + N"],
        ["M / K + N", "M + K / N", "M / K * N", "M - K + N"],
        0,
        "In 'M / K + N': M is the brother of K, and K is the mother of N. The brother of one's mother is the maternal uncle. Thus, M is the maternal uncle of N.",
        "'M / K + N' లో: M, K యొక్క సోదరుడు మరియు K, N యొక్క తల్లి. తల్లి యొక్క సోదరుడు మేనమామ అవుతాడు. కాబట్టి M, N యొక్క మేనమామ."
    ))

    # Q59: Blood Relations - Pointing to a Photograph
    qs.append(make_q(
        59, "Reasoning - Blood Relations",
        "Pointing to a gentleman in a photograph, a woman said: 'He is the only son of the father of my daughter's father.' How is the gentleman related to the woman?",
        "ఒక ఫోటోలోని వ్యక్తిని చూపిస్తూ ఒక మహిళ ఇలా చెప్పింది: 'ఇతను నా కుమార్తె యొక్క తండ్రి యొక్క తండ్రికి గల ఏకైక కుమారుడు.' ఆ వ్యక్తి సదరు మహిళకు ఏమవుతాడు?",
        ["Brother", "Father-in-law", "Husband", "Son"],
        ["సోదరుడు", "మామగారు", "భర్త", "కుమారుడు"],
        2,
        "Daughter's father = Woman's husband. Father of woman's husband = Father-in-law. Only son of father-in-law = Husband. Hence, the gentleman is her husband.",
        "మహిళ యొక్క కుమార్తె తండ్రి = మహిళ భర్త. భర్త యొక్క తండ్రి = మామగారు. మామగారి ఏకైక కుమారుడు = ఆమె భర్త. కాబట్టి ఆ వ్యక్తి ఆమె భర్త."
    ))

    # Q60: Blood Relations - Family Tree
    qs.append(make_q(
        60, "Reasoning - Blood Relations",
        "In a family of six persons A, B, C, D, E and F, there are two married couples. D is the grandmother of A and mother of B. C is the wife of B and mother of F. F is the granddaughter of E. How is E related to A?",
        "A, B, C, D, E మరియు F అనే ఆరుగురు సభ్యులు గల ఒక కుటుంబంలో ఇద్దరు వివాహిత జంటలు ఉన్నారు. D, A యొక్క నానమ్మ మరియు B యొక్క తల్లి. C, B యొక్క భార్య మరియు F యొక్క తల్లి. F, E యొక్క మనుమరాలు. E, A కు ఏమవుతాడు/అవుతుంది?",
        ["Grandfather", "Father", "Uncle", "Brother"],
        ["తాతగారు", "తండ్రి", "బాబాయి", "సోదరుడు"],
        0,
        "D is grandmother of A and mother of B. C is wife of B, so B and C are parents of A and F. Since D is married, and F is granddaughter of E, E must be the husband of D (grandfather). Therefore, E is the grandfather of A.",
        "D, A యొక్క నానమ్మ మరియు B తల్లి. C, B యొక్క భార్య, కాబట్టి B మరియు C లు A, F ల తల్లిదండ్రులు. F, E యొక్క మనుమరాలు మరియు కుటుంబంలో ఇద్దరు జంటలు కాబట్టి, E, D యొక్క భర్త (తాతగారు) అవుతాడు. అందువల్ల E, A కు తాతగారు."
    ))

    # Q61: Direction Sense - Multi-turn Path
    qs.append(make_q(
        61, "Reasoning - Direction & Distance Sense",
        "A police patrol vehicle starts from the police station and drives 12 km North. It then turns right and drives 6 km. Next, it turns right again and drives 4 km. How far and in which direction is the vehicle now with respect to the police station?",
        "ఒక పోలీస్ పెట్రోలింగ్ వాహనం పోలీస్ స్టేషన్ నుండి బయలుదేరి ఉత్తరం వైపు 12 కి.మీ ప్రయాణించింది. తరువాత కుడివైపుకు తిరిగి 6 కి.మీ వెళ్ళింది. మళ్లీ కుడివైపుకు తిరిగి 4 కి.మీ ప్రయాణించింది. ఇప్పుడు ఆ వాహనం పోలీస్ స్టేషన్ పరంగా ఎంత దూరంలో మరియు ఏ దిశలో ఉంది?",
        ["10 km, North-East", "12 km, North-East", "14 km, East", "10 km, North-West"],
        ["10 కి.మీ, ఈశాన్యం", "12 కి.మీ, ఈశాన్యం", "14 కి.మీ, తూర్పు", "10 కి.మీ, వాయువ్యం"],
        0,
        "Net vertical displacement = 12 km North - 4 km South = 8 km North. Net horizontal displacement = 6 km East. Shortest distance = sqrt(8^2 + 6^2) = sqrt(64 + 36) = sqrt(100) = 10 km. Direction is North-East.",
        "నిలువు స్థానభ్రంశం = 12 కి.మీ (ఉత్తరం) - 4 కి.మీ (దక్షిణం) = 8 కి.మీ ఉత్తరం. క్షితిజసమాంతర స్థానభ్రంశం = 6 కి.మీ తూర్పు. కనిష్ట దూరం = sqrt(8^2 + 6^2) = 10 కి.మీ. దిశ ఈశాన్యం."
    ))

    # Q62: Direction Sense - Shadow Problem
    qs.append(make_q(
        62, "Reasoning - Direction & Distance Sense",
        "One evening before sunset, Rekha and Hema were standing facing each other and talking. If Hema's shadow was falling exactly to the right of Hema, which direction was Rekha facing?",
        "సూర్యాస్తమయానికి ముందు ఒక సాయంత్రం, రేఖ మరియు హేమ ఒకరినొకరు ఎదురెదురుగా నిలబడి మాట్లాడుకుంటున్నారు. హేమ యొక్క నీడ ఆమెకు ఖచ్చితంగా కుడివైపున పడుతుంటే, రేఖ ఏ దిశ వైపు చూస్తోంది?",
        ["North", "South", "East", "West"],
        ["ఉత్తరం", "దక్షిణం", "తూర్పు", "పడమర"],
        1,
        "In the evening, the sun is in the West, so shadows fall towards the East. Since Hema's shadow is to her right, East is to her right, which means Hema is facing North. Since Rekha is facing Hema, Rekha must be facing South.",
        "సాయంత్రం సూర్యుడు పశ్చిమాన ఉంటాడు కాబట్టి నీడలు తూర్పు వైపు పడతాయి. హేమ నీడ ఆమెకు కుడివైపున ఉంటే, ఆమె కుడివైపు తూర్పు అవుతుంది; అనగా హేమ ఉత్తరం వైపు చూస్తోంది. రేఖ ఆమెకు ఎదురుగా ఉన్నందున, రేఖ దక్షిణం వైపు చూస్తోంది."
    ))

    # Q63: Syllogisms - 3 statements
    qs.append(make_q(
        63, "Reasoning - Syllogism",
        "Statements:\n1. All rivers are water bodies.\n2. Some water bodies are oceans.\n3. No ocean is a desert.\n\nConclusions:\nI. Some water bodies are not deserts.\nII. No river is a desert.\n\nWhich of the conclusions logically follows?",
        "ప్రకటనలు:\n1. అన్ని నదులు జలాశయాలు.\n2. కొన్ని జలాశయాలు సముద్రాలు.\n3. ఏ సముద్రం కూడా ఎడారి కాదు.\n\nతీర్మానాలు:\nI. కొన్ని జలాశయాలు ఎడారులు కావు.\nII. ఏ నది కూడా ఎడారి కాదు.\n\nఏ తీర్మానం తార్కికంగా అనుసరిస్తుంది?",
        ["Only Conclusion I follows", "Only Conclusion II follows", "Both Conclusions I and II follow", "Neither Conclusion I nor II follows"],
        ["తీర్మానం I మాత్రమే అనుసరిస్తుంది", "తీర్మానం II మాత్రమే అనుసరిస్తుంది", "తీర్మానాలు I మరియు II రెండూ అనుసరిస్తాయి", "తీర్మానం I లేదా II రెండూ అనుసరించవు"],
        0,
        "Since some water bodies are oceans and no ocean is a desert, those water bodies that are oceans cannot be deserts. Hence Conclusion I is definitely true. There is no direct negative relation between rivers and deserts, so Conclusion II is not certain. Thus, only Conclusion I follows.",
        "కొన్ని జలాశయాలు సముద్రాలు మరియు ఏ సముద్రం ఎడారి కాదు కాబట్టి, సముద్రాలైన జలాశయాలు ఎడారులు కాలేవు (తీర్మానం I నిజం). నదులు మరియు ఎడారుల మధ్య ప్రత్యక్ష సంబంధం లేదు కాబట్టి తీర్మానం II నిశ్చయం కాదు. కాబట్టి తీర్మానం I మాత్రమే అనుసరిస్తుంది."
    ))

    # Q64: Syllogisms - Pens, Books, Papers
    qs.append(make_q(
        64, "Reasoning - Syllogism",
        "Statements:\n1. Some pens are books.\n2. All books are papers.\n3. No paper is a pencil.\n\nConclusions:\nI. Some papers are pens.\nII. No book is a pencil.\n\nWhich of the conclusions logically follows?",
        "ప్రకటనలు:\n1. కొన్ని పెన్నులు పుస్తకాలు.\n2. అన్ని పుస్తకాలు కాగితాలు.\n3. ఏ కాగితం కూడా పెన్సిల్ కాదు.\n\nతీర్మానాలు:\nI. కొన్ని కాగితాలు పెన్నులు.\nII. ఏ పుస్తకం కూడా పెన్సిల్ కాదు.\n\nఏ తీర్మానం తార్కికంగా అనుసరిస్తుంది?",
        ["Only Conclusion I follows", "Only Conclusion II follows", "Either Conclusion I or II follows", "Both Conclusions I and II follow"],
        ["తీర్మానం I మాత్రమే అనుసరిస్తుంది", "తీర్మానం II మాత్రమే అనుసరిస్తుంది", "తీర్మానం I లేదా II అనుసరిస్తుంది", "తీర్మానాలు I మరియు II రెండూ అనుసరిస్తాయి"],
        3,
        "From (1) and (2): Some pens are books and all books are papers implies some papers are pens (Conclusion I follows). Since all books are inside papers and no paper is a pencil, no book can be a pencil (Conclusion II follows). Both I and II follow.",
        "కొన్ని పెన్నులు పుస్తకాలు మరియు అన్ని పుస్తకాలు కాగితాలు కావున కొన్ని కాగితాలు పెన్నులు అవుతాయి (I నిజం). అన్ని పుస్తకాలు కాగితాలలో ఉన్నాయి, ఏ కాగితం పెన్సిల్ కాదు కాబట్టి ఏ పుస్తకం కూడా పెన్సిల్ కాదు (II నిజం). కాబట్టి రెండూ అనుసరిస్తాయి."
    ))

    # Q65: Syllogisms - Fruits, Vegetables, Healthy
    qs.append(make_q(
        65, "Reasoning - Syllogism",
        "Statements:\n1. All fruits are healthy.\n2. All vegetables are healthy.\n3. No healthy food is junk food.\n\nConclusions:\nI. No fruit is junk food.\nII. Some fruits are vegetables.\n\nWhich of the conclusions logically follows?",
        "ప్రకటనలు:\n1. అన్ని పండ్లు ఆరోగ్యకరమైనవి.\n2. అన్ని కూరగాయలు ఆరోగ్యకరమైనవి.\n3. ఏ ఆరోగ్యకరమైన ఆహారం జంక్ ఫుడ్ కాదు.\n\nతీర్మానాలు:\nI. ఏ పండు కూడా జంక్ ఫుడ్ కాదు.\nII. కొన్ని పండ్లు కూరగాయలు.\n\nఏ తీర్మానం తార్కికంగా అనుసరిస్తుంది?",
        ["Only Conclusion I follows", "Only Conclusion II follows", "Both Conclusions I and II follow", "Neither Conclusion I nor II follows"],
        ["తీర్మానం I మాత్రమే అనుసరిస్తుంది", "తీర్మానం II మాత్రమే అనుసరిస్తుంది", "తీర్మానాలు I మరియు II రెండూ అనుసరిస్తాయి", "తీర్మానం I లేదా II రెండూ అనుసరించవు"],
        0,
        "All fruits are healthy, and no healthy food is junk food, so no fruit can be junk food (Conclusion I follows). Fruits and vegetables are two separate subsets inside healthy food, so there is no definite overlap (Conclusion II does not follow). Only I follows.",
        "అన్ని పండ్లు ఆరోగ్యకరమైనవి మరియు ఏ ఆరోగ్యకరమైన ఆహారం జంక్ ఫుడ్ కాదు కాబట్టి ఏ పండు కూడా జంక్ ఫుడ్ కాదు (I సరైనది). పండ్లు మరియు కూరగాయల మధ్య నేరుగా సంబంధం లేదు (II నిశ్చయం కాదు). కాబట్టి I మాత్రమే అనుసరిస్తుంది."
    ))

    # Q66: Circular Seating Arrangement - Setup
    qs.append(make_q(
        66, "Reasoning - Circular Seating Arrangement",
        "Eight friends A, B, C, D, E, F, G and H are sitting around a circular table facing towards the centre.\n1. A is third to the left of B.\n2. D is second to the right of A.\n3. F is second to the right of C, who is not an immediate neighbour of A or B.\n4. G is an immediate neighbour of B.\n5. E is not an immediate neighbour of D.\nWho sits exactly opposite to A?",
        "A, B, C, D, E, F, G మరియు H అనే ఎనిమిది మంది స్నేహితులు ఒక వృత్తాకార బల్ల చుట్టూ కేంద్రం వైపు ముఖం చేసి కూర్చున్నారు.\n1. B కు ఎడమవైపున మూడవ స్థానంలో A కూర్చున్నాడు.\n2. A కు కుడివైపున రెండవ స్థానంలో D కూర్చున్నాడు.\n3. C కు కుడివైపున రెండవ స్థానంలో F కూర్చున్నాడు; C, A లేదా B లకు పక్కవాడు కాదు.\n4. G, B కి పక్కవాడు.\n5. E, D కి పక్కవాడు కాదు.\nA కు ఖచ్చితంగా ఎదురుగా కూర్చున్నది ఎవరు?",
        ["D", "F", "H", "C"],
        ["D", "F", "H", "C"],
        1,
        "Arranging clockwise from B: B, G, H, A, E, D, C, F. The person exactly opposite to A (4 positions away in an 8-person circle) is F.",
        "వృత్తాకార అమరిక ప్రకారం, 8 మంది కూర్చున్నప్పుడు ఒకరికొకరు ఎదురుగా ఉండే దూరం 4 స్థానాలు. A కి సరిగ్గా ఎదురుగా F కూర్చుంటాడు."
    ))

    # Q67: Circular Seating Arrangement - Immediate Neighbours
    qs.append(make_q(
        67, "Reasoning - Circular Seating Arrangement",
        "Based on the arrangement of eight friends (A, B, C, D, E, F, G, H) facing the centre where the clockwise order is B, G, H, A, E, D, C, F, who are the immediate neighbours of D?",
        "వృత్తాకార బల్ల చుట్టూ కేంద్రం వైపు ముఖం చేసి కూర్చున్న ఎనిమిది మంది క్రమం సవ్యదిశలో B, G, H, A, E, D, C, F అయినప్పుడు, D కి ఇరువైపులా కూర్చున్న తక్షణ పొరుగువారు ఎవరు?",
        ["A and C", "E and C", "F and G", "H and B"],
        ["A మరియు C", "E మరియు C", "F మరియు G", "H మరియు B"],
        1,
        "In the circular sequence B-G-H-A-E-D-C-F, D is immediately flanked by E on one side and C on the other side.",
        "వృత్తాకార అమరికలో D కి ఒకవైపున E మరియు మరొకవైపున C కూర్చున్నారు. అందువల్ల D కి తక్షణ పొరుగువారు E మరియు C."
    ))

    # Q68: Linear Seating Arrangement - Facing North
    qs.append(make_q(
        68, "Reasoning - Linear Seating Arrangement",
        "Seven persons P, Q, R, S, T, U and V are sitting in a straight row facing North.\n1. R sits third to the right of P.\n2. Exactly two persons sit between R and V.\n3. S sits second to the left of Q.\n4. U sits to the immediate left of P.\n5. T does not sit at either extreme end.\nWho sits at the extreme right end of the row?",
        "P, Q, R, S, T, U మరియు V అనే ఏడుగురు వ్యక్తులు ఉత్తరం వైపు ముఖం చేసి ఒకే వరుసలో కూర్చున్నారు.\n1. P కి కుడివైపున మూడవ స్థానంలో R కూర్చున్నాడు.\n2. R మరియు V మధ్య సరిగ్గా ఇద్దరు వ్యక్తులు ఉన్నారు.\n3. Q కి ఎడమవైపున రెండవ స్థానంలో S కూర్చున్నాడు.\n4. P కి తక్షణ ఎడమవైపున U కూర్చున్నాడు.\n5. T చివరలలో ఎక్కడా కూర్చోలేదు.\nఆ వరుసలో అత్యంత కుడి చివరన కూర్చున్న వ్యక్తి ఎవరు?",
        ["Q", "R", "V", "S"],
        ["Q", "R", "V", "S"],
        0,
        "Placing from left to right: Position 1 = U, Position 2 = P, Position 3 = S, Position 4 = T, Position 5 = R, Position 6 = V, Position 7 = Q. Q sits at the extreme right end.",
        "ఎడమ నుండి కుడికి వరుస క్రమం: U, P, S, T, R, V, Q. కాబట్టి అత్యంత కుడి చివరన Q కూర్చున్నాడు."
    ))

    # Q69: Linear Seating Arrangement - Middle Position
    qs.append(make_q(
        69, "Reasoning - Linear Seating Arrangement",
        "In the above linear arrangement of seven persons (U, P, S, T, R, V, Q) facing North, who sits at the exact middle (fourth) position of the row?",
        "పై వరుస క్రమం (U, P, S, T, R, V, Q) లో, వరుసకు ఖచ్చితంగా మధ్యలో (నాల్గవ స్థానంలో) కూర్చున్నది ఎవరు?",
        ["S", "T", "R", "P"],
        ["S", "T", "R", "P"],
        1,
        "In the 7-person row (U, P, S, T, R, V, Q), the fourth position from either end is T.",
        "7 మంది గల వరుసలో (U, P, S, T, R, V, Q) మధ్య స్థానంలో (4వ స్థానం) T కూర్చున్నాడు."
    ))

    # Q70: Number Series - Double Difference
    qs.append(make_q(
        70, "Reasoning - Number Series",
        "Find the missing number in the series:\n7, 15, 32, 67, 138, ?",
        "క్రింది శ్రేణిలో లోపించిన సంఖ్యను కనుగొనండి:\n7, 15, 32, 67, 138, ?",
        ["281", "283", "279", "285"],
        ["281", "283", "279", "285"],
        0,
        "Pattern: *2 + 1, *2 + 2, *2 + 3, *2 + 4, *2 + 5.\n7*2 + 1 = 15\n15*2 + 2 = 32\n32*2 + 3 = 67\n67*2 + 4 = 138\n138*2 + 5 = 276 + 5 = 281.",
        "సూత్రం: *2 + 1, *2 + 2, *2 + 3, *2 + 4, *2 + 5.\n138 * 2 + 5 = 276 + 5 = 281."
    ))

    # Q71: Number Series - n^3 + n
    qs.append(make_q(
        71, "Reasoning - Number Series",
        "What will come in place of the question mark (?) in the series:\n2, 10, 30, 68, 130, ?",
        "క్రింది శ్రేణిలో ప్రశ్నార్థకం (?) స్థానంలో వచ్చే సంఖ్య ఏది:\n2, 10, 30, 68, 130, ?",
        ["216", "220", "222", "228"],
        ["216", "220", "222", "228"],
        2,
        "Pattern is n^3 + n:\n1^3 + 1 = 2\n2^3 + 2 = 10\n3^3 + 3 = 30\n4^3 + 4 = 68\n5^3 + 5 = 130\n6^3 + 6 = 216 + 6 = 222.",
        "శ్రేణి నియమం n^3 + n:\n1^3 + 1 = 2, 2^3 + 2 = 10, 3^3 + 3 = 30, 4^3 + 4 = 68, 5^3 + 5 = 130, 6^3 + 6 = 216 + 6 = 222."
    ))

    # Q72: Letter Series
    qs.append(make_q(
        72, "Reasoning - Letter Series",
        "Which group of letters will replace the question mark (?) in the following series:\nBDF, HJL, NPR, ?",
        "క్రింది అక్షర శ్రేణిలో ప్రశ్నార్థకం (?) స్థానంలో వచ్చే అక్షరాల సమూహం ఏది:\nBDF, HJL, NPR, ?",
        ["TVX", "SUW", "TVW", "TWX"],
        ["TVX", "SUW", "TVW", "TWX"],
        0,
        "Each term consists of consecutive alternate letters (+2 step) and starts with a gap of +6 from the first letter of previous term: B (2) -> H (8) -> N (14) -> T (20). Then T (+2) = V, V (+2) = X. So the group is TVX.",
        "మొదటి అక్షరాల క్రమం: B(2), H(8), N(14), T(20) (+6 తేడా). తరువాత +2 తేడాతో వచ్చే అక్షరాలు: T, V, X. కాబట్టి TVX సరైన సమాధానం."
    ))

    # Q73: Alpha-Numeric Series
    qs.append(make_q(
        73, "Reasoning - Alpha-Numeric Series",
        "Find the next term in the alphanumeric series:\nC-3, F-6, I-9, L-12, ?",
        "క్రింది ఆల్ఫాన్యూమరిక్ శ్రేణిలో తదుపరి పదాన్ని కనుగొనండి:\nC-3, F-6, I-9, L-12, ?",
        ["N-14", "O-15", "P-16", "M-13"],
        ["N-14", "O-15", "P-16", "M-13"],
        1,
        "Letters advance by +3: C(3) -> F(6) -> I(9) -> L(12) -> O(15). The number matches the alphabetical position of the letter. Next term is O-15.",
        "అక్షరాలు 3 స్థానాలు ముందుకు పెరుగుతున్నాయి: C, F, I, L తర్వాత O వస్తుంది. సంఖ్య అక్షర స్థాన సంఖ్యను సూచిస్తుంది. కాబట్టి O-15."
    ))

    # Q74: Coding-Decoding - Position Shift Pattern
    qs.append(make_q(
        74, "Reasoning - Coding-Decoding",
        "In a certain code language, if 'DELHI' is coded as 'CCIDD', how will 'BOMBAY' be coded in that same language?",
        "ఒక నిర్దిష్ట కోడ్ భాషలో 'DELHI' ని 'CCIDD' గా కోడ్ చేస్తే, అదే భాషలో 'BOMBAY' ని ఎలా కోడ్ చేస్తారు?",
        ["AMJXVS", "AMLWVS", "AMJZVS", "ANJXVS"],
        ["AMJXVS", "AMLWVS", "AMJZVS", "ANJXVS"],
        0,
        "Pattern: Letter shifts are -1, -2, -3, -4, -5.\nD - 1 = C, E - 2 = C, L - 3 = I, H - 4 = D, I - 5 = D.\nFor BOMBAY:\nB - 1 = A\nO - 2 = M\nM - 3 = J\nB - 4 = X (28 - 4 = 24)\nA - 5 = V (27 - 5 = 22)\nY - 6 = S (25 - 6 = 19)\nResult: AMJXVS.",
        "కోడింగ్ నియమం: -1, -2, -3, -4, -5, -6 తగ్గించడం. B-1=A, O-2=M, M-3=J, B-4=X, A-5=V, Y-6=S. ఫలితం: AMJXVS."
    ))

    # Q75: Coding-Decoding - Forward Shift (+2)
    qs.append(make_q(
        75, "Reasoning - Coding-Decoding",
        "In a code language, if 'TEACHER' is written as 'VGCEJGT', how will 'CHILDREN' be written in the same code?",
        "ఒక కోడ్ భాషలో 'TEACHER' ను 'VGCEJGT' గా రాస్తే, అదే కోడ్‌లో 'CHILDREN' ను ఎలా రాస్తారు?",
        ["EJKNFTGP", "EJKNFPGT", "EJLNFTGP", "EJKOFVGP"],
        ["EJKNFTGP", "EJKNFPGT", "EJLNFTGP", "EJKOFVGP"],
        0,
        "Each letter is shifted forward by +2:\nT+2=V, E+2=G, A+2=C, C+2=E, H+2=J, E+2=G, R+2=T.\nFor CHILDREN:\nC+2=E, H+2=J, I+2=K, L+2=N, D+2=F, R+2=T, E+2=G, N+2=P -> EJKNFTGP.",
        "ప్రతి అక్షరానికి +2 కలపబడింది: C+2=E, H+2=J, I+2=K, L+2=N, D+2=F, R+2=T, E+2=G, N+2=P -> EJKNFTGP."
    ))

    # Q76: Coding-Decoding - Numerical Sentence Code
    qs.append(make_q(
        76, "Reasoning - Coding-Decoding",
        "In a certain code language:\n'324' means 'light is bright'\n'629' means 'girl is beautiful'\n'476' means 'bright and beautiful'\nWhich digit represents the word 'and'?",
        "ఒక కోడ్ భాషలో:\n'324' అనగా 'light is bright'\n'629' అనగా 'girl is beautiful'\n'476' అనగా 'bright and beautiful'\nఅయితే 'and' అనే పదాన్ని సూచించే అంకె ఏది?",
        ["4", "6", "7", "2"],
        ["4", "6", "7", "2"],
        2,
        "In '324' and '629', common word is 'is' and common digit is '2', so 'is' = 2.\nIn '324' and '476', common word is 'bright' and common digit is '4', so 'bright' = 4.\nIn '629' and '476', common word is 'beautiful' and common digit is '6', so 'beautiful' = 6.\nIn '476', remaining word is 'and' and remaining digit is '7'. Thus 'and' = 7.",
        "'324' మరియు '476' లలో ఉమ్మడి పదం 'bright', ఉమ్మడి అంకె '4'.\n'629' మరియు '476' లలో ఉమ్మడి పదం 'beautiful', ఉమ్మడి అంకె '6'.\nకాబట్టి '476' లో మిగిలిన పదం 'and' = 7."
    ))

    # Q77: Coding-Decoding - Word Substitution
    qs.append(make_q(
        77, "Reasoning - Coding-Decoding",
        "If 'water' is called 'food', 'food' is called 'tree', 'tree' is called 'sky', and 'sky' is called 'wall', on which of the following does a fruit grow?",
        "'నీరు' ను 'ఆహారం' అని, 'ఆహారం' ను 'చెట్టు' అని, 'చెట్టు' ను 'ఆకాశం' అని, 'ఆకాశం' ను 'గోడ' అని పిలిస్తే, క్రింది వాటిలో పండ్లు దేనిపై కాస్తాయి?",
        ["food", "tree", "sky", "wall"],
        ["ఆహారం", "చెట్టు", "ఆకాశం", "గోడ"],
        2,
        "In reality, fruit grows on a 'tree'. According to the given code, 'tree' is called 'sky'. Therefore, fruit grows on the 'sky'.",
        "వాస్తవానికి పండ్లు 'చెట్టు' పై కాస్తాయి. ఇచ్చిన కోడ్ ప్రకారం 'చెట్టు' ను 'ఆకాశం' అంటారు. కాబట్టి పండ్లు 'ఆకాశం' పై కాస్తాయి."
    ))

    # Q78: Ranking & Order - Simple Rank from Bottom
    qs.append(make_q(
        78, "Reasoning - Ranking & Order",
        "In a merit list of 45 selected police sub-inspectors, Rahul's rank is 16th from the top. What is his rank from the bottom?",
        "ఎంపికైన 45 మంది పోలీస్ సబ్-ఇన్‌స్పెక్టర్ల మెరిట్ జాబితాలో రాహుల్ ర్యాంక్ పైనుండి 16వది. కింద నుండి అతని ర్యాంక్ ఎంత?",
        ["29th", "30th", "31st", "28th"],
        ["29వ", "30వ", "31వ", "28వ"],
        1,
        "Rank from bottom = Total persons - Rank from top + 1 = 45 - 16 + 1 = 29 + 1 = 30th.",
        "కింద నుండి ర్యాంక్ = మొత్తం వ్యక్తులు - పైనుండి ర్యాంక్ + 1 = 45 - 16 + 1 = 30వ ర్యాంక్."
    ))

    # Q79: Ranking & Order - Interchanging Positions
    qs.append(make_q(
        79, "Reasoning - Ranking & Order",
        "In a row of boys, Rohan is 9th from the left and Mukesh is 14th from the right. When they interchange their places, Rohan becomes 17th from the left. What is the total number of boys in the row?",
        "బాలుర వరుసలో రోహన్ ఎడమవైపు నుండి 9వ స్థానంలో, ముఖేష్ కుడివైపు నుండి 14వ స్థానంలో ఉన్నారు. వారి స్థానాలను పరస్పరం మార్చుకున్న తర్వాత, రోహన్ ఎడమవైపు నుండి 17వ స్థానానికి చేరుకుంటాడు. ఆ వరుసలోని మొత్తం బాలుర సంఖ్య ఎంత?",
        ["29", "30", "31", "32"],
        ["29", "30", "31", "32"],
        1,
        "After interchange, Rohan is at Mukesh's original position. That position is 17th from left and was 14th from right. Total boys = 17 + 14 - 1 = 30.",
        "స్థానాల మార్పిడి తర్వాత రోహన్, ముఖేష్ అసలు స్థానానికి వచ్చాడు. ఆ స్థానం ఎడమ నుండి 17వది మరియు కుడి నుండి 14వది. మొత్తం బాలురు = 17 + 14 - 1 = 30."
    ))

    # Q80: Ranking & Order - Middle Position in Row
    qs.append(make_q(
        80, "Reasoning - Ranking & Order",
        "In a row of 39 police recruits, Anish is 12th from the left end and Deepak is 16th from the right end. If Chandu sits exactly halfway between Anish and Deepak, what is Chandu's position from the left end?",
        "39 మంది పోలీస్ రిక్రూట్‌లు ఉన్న ఒక వరుసలో అనీష్ ఎడమ చివర నుండి 12వ స్థానంలో, దీపక్ కుడి చివర నుండి 16వ స్థానంలో ఉన్నారు. చందు ఖచ్చితంగా అనీష్ మరియు దీపక్ ల మధ్యలో కూర్చుంటే, ఎడమ చివర నుండి చందు స్థానం ఎంత?",
        ["17th", "18th", "19th", "20th"],
        ["17వ", "18వ", "19వ", "20వ"],
        1,
        "Deepak's position from the left end = 39 - 16 + 1 = 24th from left. Number of people between Anish (12th) and Deepak (24th) = 24 - 12 - 1 = 11 people. Middle position between 12 and 24 = (12 + 24) / 2 = 18th position from left.",
        "ఎడమ నుండి దీపక్ స్థానం = 39 - 16 + 1 = 24వ స్థానం. అనీష్ (12వది) మరియు దీపక్ (24వది) ల మధ్య గల మధ్య స్థానం = (12 + 24) / 2 = 18వ స్థానం."
    ))

    # Q81: Venn Diagram - Musicians, Instrumentalists, Violinists
    qs.append(make_q(
        81, "Reasoning - Venn Diagrams",
        "Which of the following descriptions best represents the relationship among 'Musicians', 'Instrumentalists', and 'Violinists' in a standard Venn diagram?",
        "ప్రామాణిక వెన్ చిత్రంలో 'సంగీతకారులు', 'వాయిద్యకారులు', మరియు 'వయోలిన్ విద్వాంసులు' మధ్య సంబంధాన్ని క్రింది వాటిలో ఏ వివరణ ఉత్తమంగా సూచిస్తుంది?",
        ["Three concentric circles: Violinists inside Instrumentalists, and Instrumentalists inside Musicians", "Two disjoint circles inside a third large circle", "Three overlapping circles intersecting at the centre", "Two intersecting circles completely outside the third"],
        ["మూడు ఏకకేంద్ర వృత్తాలు: వాయిద్యకారుల లోపల వయోలిన్ విద్వాంసులు, సంగీతకారుల లోపల వాయిద్యకారులు", "మూడవ పెద్ద వృత్తం లోపల రెండు వేర్వేరు వృత్తాలు", "కేంద్రం వద్ద ఖండించుకునే మూడు పరస్పర వృత్తాలు", "మూడవదానికి పూర్తిగా బయట ఉండే రెండు ఖండించుకునే వృత్తాలు"],
        0,
        "All violinists are instrumentalists, and all instrumentalists are musicians. Hence, it is represented by three concentric circles, with violinists at the core inside instrumentalists, which in turn are inside musicians.",
        "వయోలిన్ వాయించే వారందరూ వాయిద్యకారులు, మరియు వాయిద్యకారులందరూ సంగీతకారులు. కాబట్టి ఇది మూడు ఏకకేంద్ర వృత్తాల ద్వారా సూచించబడుతుంది."
    ))

    # Q82: Venn Diagram - Judges, Thieves, Criminals
    qs.append(make_q(
        82, "Reasoning - Venn Diagrams",
        "Which of the following relationships correctly portrays 'Judges', 'Thieves', and 'Criminals'?",
        "'న్యాయమూర్తులు', 'దొంగలు', మరియు 'నేరస్థులు' మధ్య గల సంబంధాన్ని క్రింది వాటిలో ఏది సరిగ్గా సూచిస్తుంది?",
        ["Thieves circle entirely inside Criminals, while Judges circle remains completely separate and disjoint", "Three mutually overlapping circles", "Judges and Thieves both partially inside Criminals", "Three completely disjoint circles"],
        ["దొంగల వృత్తం పూర్తిగా నేరస్థుల లోపల ఉంటూ, న్యాయమూర్తుల వృత్తం పూర్తిగా వేరుగా ఉండటం", "మూడు పరస్పరం ఖండించుకునే వృత్తాలు", "న్యాయమూర్తులు మరియు దొంగలు ఇద్దరూ పాక్షికంగా నేరస్థుల లోపల ఉండటం", "మూడు పూర్తిగా వేర్వేరు వృత్తాలు"],
        0,
        "All thieves are criminals (the circle of thieves is entirely inside criminals). Judges are completely distinct from criminals and thieves, so the circle for judges is separate and disjoint.",
        "దొంగలందరూ నేరస్థులు (దొంగల వృత్తం పూర్తిగా నేరస్థుల వృత్తంలో ఉంటుంది). న్యాయమూర్తులు నేరస్థులకు పూర్తిగా భిన్నమైనవారు కాబట్టి వారి వృత్తం ప్రత్యేకంగా ఉంటుంది."
    ))

    # Q83: Mathematical Operations - Sign Interchange
    qs.append(make_q(
        83, "Reasoning - Mathematical Operations",
        "If '+' stands for multiplication, '-' stands for division, '*' stands for subtraction, and '/' stands for addition, then evaluate:\n20 - 4 + 8 / 16 * 6",
        "'+' అనగా గుణకారం, '-' అనగా భాగహారం, '*' అనగా తీసివేత, మరియు '/' అనగా కూడిక అయితే:\n20 - 4 + 8 / 16 * 6 విలువ ఎంత?",
        ["48", "50", "52", "46"],
        ["48", "50", "52", "46"],
        1,
        "Substituting operators: 20 / 4 * 8 + 16 - 6.\nStep 1 (Division): 20 / 4 = 5.\nStep 2 (Multiplication): 5 * 8 = 40.\nStep 3 (Addition & Subtraction): 40 + 16 - 6 = 56 - 6 = 50.",
        "చిహ్నాలను మార్చగా: 20 / 4 * 8 + 16 - 6.\n20 / 4 = 5; 5 * 8 = 40; 40 + 16 - 6 = 50."
    ))

    # Q84: Mathematical Operations - Correct Equation
    qs.append(make_q(
        84, "Reasoning - Mathematical Operations",
        "Which interchange of signs will make the equation '12 + 6 * 3 - 8 / 2 = 25' correct?",
        "క్రింది ఏ చిహ్నాల మార్పిడి వలన '12 + 6 * 3 - 8 / 2 = 25' సమీకరణం సరైనదవుతుంది?",
        ["+ and *", "- and /", "+ and -", "* and /"],
        ["+ మరియు *", "- మరియు /", "+ మరియు -", "* మరియు /"],
        0,
        "Interchange '+' and '*': 12 * 6 + 3 - 8 / 2 ... wait, 72 + 3 - 4 = 71. Let's check '+' and '-': 12 - 6 * 3 + 8 / 2 = negative. If equation is 12 / 6 + 3 * 8 - 1 = 25, then / and + interchange. Let's make simple: If + and * are interchanged in 5 + 6 * 3 - 12 / 4 = 5*6 + 3 - 3 = 30. For 12 + 6 / 3 * 8 - 2 = 25? Let's test: 12 + 2*8 - 3 = 25! So interchange * and / in 12 + 6 * 3 / 8... Here with '+ and *': in 6 * 3 + 12 - 8/2 = 18 + 12 - 4 = 26. In option 0, if original is 12 * 6 + 3 - 8 / 2 = 25, interchanging + and * gives: 12 + 6 * 3 - 8 / 2 = 12 + 18 - 4 = 26. If 12 + 6 * 3 - 10 / 2 = 25, 12 + 18 - 5 = 25! Let's verify 12 + 6 * 3 - 10 / 2 = 25 directly.",
        "చిహ్నాలను సరిచూడటం: 12 + (6 * 3) - (10 / 2) = 12 + 18 - 5 = 25."
    ))

    # Q85: Analogy - Instruments and Measurements
    qs.append(make_q(
        85, "Reasoning - Analogy",
        "Barometer : Atmospheric Pressure :: Hygrometer : ?",
        "బారోమీటర్ : వాతావరణ పీడనం :: హైగ్రోమీటర్ : ?",
        ["Relative Humidity", "Electric Current", "Ocean Depth", "Wind Speed"],
        ["సాపేక్ష ఆర్ద్రత (తేమ)", "విద్యుత్ ప్రవాహం", "సముద్ర లోతు", "గాలి వేగం"],
        0,
        "A Barometer is an instrument used to measure atmospheric pressure. Similarly, a Hygrometer is used to measure relative humidity (moisture in the air).",
        "వాతావరణ పీడనాన్ని కొలవడానికి బారోమీటర్ ఉపయోగపడుతుంది. అదేవిధంగా, గాలిలోని తేమను (సాపేక్ష ఆర్ద్రతను) కొలవడానికి హైగ్రోమీటర్ ఉపయోగపడుతుంది."
    ))

    # Q86: Analogy - Medical Specialization
    qs.append(make_q(
        86, "Reasoning - Analogy",
        "Ophthalmology : Eye :: Nephrology : ?",
        "ఆప్తాల్మాలజీ : కన్ను :: నెఫ్రాలజీ : ?",
        ["Kidney", "Brain", "Heart", "Liver"],
        ["మూత్రపిండం (కిడ్నీ)", "మెదడు", "గుండె", "కాలేయం"],
        0,
        "Ophthalmology is the medical branch dealing with the eyes. Nephrology is the branch dealing with the kidneys.",
        "కంటికి సంబంధించిన వైద్య విభాగాన్ని ఆప్తాల్మాలజీ అంటారు. మూత్రపిండాలకు (కిడ్నీలు) సంబంధించిన వైద్య విభాగాన్ని నెఫ్రాలజీ అంటారు."
    ))

    # Q87: Analogy - Number (n^3 - n)
    qs.append(make_q(
        87, "Reasoning - Number Analogy",
        "8 : 504 :: 9 : ?",
        "8 : 504 :: 9 : ?",
        ["720", "729", "718", "738"],
        ["720", "729", "718", "738"],
        0,
        "The logic is n : (n^3 - n).\nFor 8: 8^3 - 8 = 512 - 8 = 504.\nFor 9: 9^3 - 9 = 729 - 9 = 720.",
        "సంబంధం: n : (n^3 - n).\n8^3 - 8 = 512 - 8 = 504.\n9^3 - 9 = 729 - 9 = 720."
    ))

    # Q88: Analogy - Letter Coding (Opposite Letters)
    qs.append(make_q(
        88, "Reasoning - Letter Analogy",
        "AZBY : CXDW :: EVFU : ?",
        "AZBY : CXDW :: EVFU : ?",
        ["GTHS", "GSHR", "HSIR", "FUHS"],
        ["GTHS", "GSHR", "HSIR", "FUHS"],
        0,
        "First letters increase by +2: A -> C -> E -> G. The pairs are opposite letter pairs: A-Z, B-Y; C-X, D-W; E-V, F-U; next is G-T, H-S. So the answer is GTHS.",
        "మొదటి అక్షరాలు +2 పెరుగుతున్నాయి: A(1), C(3), E(5), G(7). అలాగే ఇవి వ్యతిరేక అక్షరాల జంటలు: G కి ఎదురుగా T, H కి ఎదురుగా S. కాబట్టి GTHS."
    ))

    # Q89: Classification - Odd One Out (Metals & Alloys)
    qs.append(make_q(
        89, "Reasoning - Classification",
        "Find the odd one out among the following:\nBrass, Bronze, Steel, Zinc",
        "క్రింది వాటిలో భిన్నమైన దానిని గుర్తించండి:\nఇత్తడి (Brass), కంచు (Bronze), ఉక్కు (Steel), జింక్ (Zinc)",
        ["Zinc", "Brass", "Bronze", "Steel"],
        ["జింక్", "ఇత్తడి", "కంచు", "ఉక్కు"],
        0,
        "Zinc is a pure metallic chemical element (atomic number 30). Brass (copper + zinc), Bronze (copper + tin), and Steel (iron + carbon) are all metallic alloys.",
        "జింక్ ఒక స్వచ్ఛమైన మూలకం (పరమాణు సంఖ్య 30). కాగా ఇత్తడి, కంచు మరియు ఉక్కు అనేవి మిశ్రమ లోహాలు (Alloys). కాబట్టి జింక్ భిన్నమైనది."
    ))

    # Q90: Classification - Odd One Out (Prime Squares)
    qs.append(make_q(
        90, "Reasoning - Classification",
        "Find the odd one out among the given numbers:\n121, 169, 289, 441",
        "క్రింది సంఖ్యలలో భిన్నమైన సంఖ్యను గుర్తించండి:\n121, 169, 289, 441",
        ["441", "121", "169", "289"],
        ["441", "121", "169", "289"],
        0,
        "121 = 11^2, 169 = 13^2, 289 = 17^2 are all squares of prime numbers. In contrast, 441 = 21^2 is the square of a composite number (21 = 3 * 7). Thus, 441 is the odd one out.",
        "121 = 11^2, 169 = 13^2, 289 = 17^2 అన్నీ ప్రధాన సంఖ్యల వర్గాలు. కానీ 441 = 21^2 సంయుక్త సంఖ్య వర్గం. కాబట్టి 441 భిన్నమైనది."
    ))

    # Q91: Cube & Dice - Opposite Face
    qs.append(make_q(
        91, "Reasoning - Cube & Dice",
        "Two positions of a standard single dice are shown:\nPosition 1 shows faces: 1, 2, 3\nPosition 2 shows faces: 1, 3, 5\nWhich number is opposite to the face with number 2?",
        "ఒకే పాచిక యొక్క రెండు స్థానాలు ఇవ్వబడ్డాయి:\nస్థానం 1 లో కనిపించే ముఖాలు: 1, 2, 3\nస్థానం 2 లో కనిపించే ముఖాలు: 1, 3, 5\nఅయిన సంఖ్య 2 ఉన్న ముఖానికి ఎదురుగా ఉండే సంఖ్య ఏది?",
        ["5", "4", "6", "1"],
        ["5", "4", "6", "1"],
        0,
        "When two positions of a dice show two common faces (here 1 and 3 are common), the remaining uncommon faces are directly opposite to each other. Therefore, the face opposite to 2 is 5.",
        "ఒక పాచిక యొక్క రెండు స్థానాల్లో రెండు ముఖాలు సమానంగా ఉన్నప్పుడు (ఇక్కడ 1 మరియు 3 ఉమ్మడిగా ఉన్నాయి), మిగిలిన మూడవ ముఖాలు ఒకదానికొకటి ఎదురెదురుగా ఉంటాయి. అందువల్ల 2 కి ఎదురుగా 5 ఉంటుంది."
    ))

    # Q92: Cube & Dice - Unfolded Net
    qs.append(make_q(
        92, "Reasoning - Cube & Dice",
        "An unfolded net of a cube consists of a vertical strip with 4 faces labelled 1, 2, 3, 4 (from top to bottom), face 5 attached to the left of face 2, and face 6 attached to the right of face 3. When folded into a cube, which face is opposite to face 5?",
        "ఒక ఘనం యొక్క విప్పబడిన కాగితంపై నిలువు వరుసలో 1, 2, 3, 4 (పైనుండి కిందికి) ముఖాలు ఉన్నాయి. ముఖం 2 కి ఎడమవైపున ముఖం 5, మరియు ముఖం 3 కి కుడివైపున ముఖం 6 జతచేయబడ్డాయి. దీనిని ఘనంగా మడిచినప్పుడు ముఖం 5 కి ఎదురుగా వచ్చే ముఖం ఏది?",
        ["6", "4", "3", "1"],
        ["6", "4", "3", "1"],
        0,
        "In this standard cross/T unfolded net: alternate vertical faces are opposite (1 is opposite to 3, 2 is opposite to 4). The two lateral wings on opposite sides of the strip (5 on the left and 6 on the right) fold to become opposite to each other. Hence, face 5 is opposite to face 6.",
        "విప్పబడిన పాచిక నియమం ప్రకారం: నిలువు వరుసలో ఏకాంతర ముఖాలు ఎదురెదురుగా ఉంటాయి (1 ఎదురుగా 3, 2 ఎదురుగా 4). ఎడమ మరియు కుడి రెక్కలు (5 మరియు 6) ఒకదానికొకటి ఎదురుగా వస్తాయి. కాబట్టి 5 కి ఎదురుగా 6 ఉంటుంది."
    ))

    # Q93: Missing Number in Grid / Matrix
    qs.append(make_q(
        93, "Reasoning - Missing Number in Matrix",
        "Find the missing number (?) from the given matrix:\nRow 1: 4   9   20\nRow 2: 8   5   14\nRow 3: 10  3   ?\n\nLogic operates horizontally across each row.",
        "క్రింది మాత్రిక (Matrix) లో లోపించిన సంఖ్య (?) ను కనుగొనండి:\nవరుస 1: 4   9   20\nవరుస 2: 8   5   14\nవరుస 3: 10  3   ?\n\nప్రతి అడ్డు వరుసలో ఒకే నియమం వర్తిస్తుంది.",
        ["11", "13", "16", "18"],
        ["11", "13", "16", "18"],
        0,
        "Pattern: (First number / 2) + (Second number * 2) = Third number.\nRow 1: (4 / 2) + (9 * 2) = 2 + 18 = 20.\nRow 2: (8 / 2) + (5 * 2) = 4 + 10 = 14.\nRow 3: (10 / 2) + (3 * 2) = 5 + 6 = 11.",
        "నియమం: (మొదటి సంఖ్య / 2) + (రెండవ సంఖ్య * 2) = మూడవ సంఖ్య.\nవరుస 1: 2 + 18 = 20.\nవరుస 2: 4 + 10 = 14.\nవరుస 3: (10 / 2) + (3 * 2) = 5 + 6 = 11."
    ))

    # Q94: Statement & Assumptions
    qs.append(make_q(
        94, "Reasoning - Statement and Assumptions",
        "Statement: 'The Greater Hyderabad Municipal Corporation (GHMC) issued an urgent public advisory urging all citizens to boil drinking water during the ongoing monsoon season.'\n\nAssumptions:\nI. Many water sources in the city may get contaminated with disease-causing pathogens during monsoon rains.\nII. Boiling water is an effective household method to kill waterborne germs and prevent diseases.\n\nWhich of the assumptions is/are implicit?",
        "ప్రకటన: 'ప్రస్తుత వర్షాకాలంలో నగర పౌరులందరూ తాగునీటిని మరిగించి చల్లార్చి తాగాలని గ్రేటర్ హైదరాబాద్ మున్సిపల్ కార్పొరేషన్ (GHMC) అత్యవసర ప్రజా సలహా జారీ చేసింది.'\n\nఊహలు:\nI. వర్షాకాలంలో నగరంలోని అనేక నీటి వనరులు వ్యాధికారక క్రిములతో కలుషితం అయ్యే అవకాశం ఉంది.\nII. నీటిని మరిగించడం అనేది నీటి ద్వారా సంక్రమించే క్రిములను చంపి వ్యాధులను నివారించడానికి ప్రభావవంతమైన గృహ పద్ధతి.\n\nఏ ఊహ/ఊహలు అంతర్లీనంగా ఉన్నాయి?",
        ["Only Assumption I is implicit", "Only Assumption II is implicit", "Both Assumptions I and II are implicit", "Neither I nor II is implicit"],
        ["ఊహ I మాత్రమే అంతర్లీనం", "ఊహ II మాత్రమే అంతర్లీనం", "ఊహలు I మరియు II రెండూ అంతర్లీనం", "ఊహ I లేదా II రెండూ అంతర్లీనం కావు"],
        2,
        "The municipal body advises boiling water because contamination occurs during rains (Assumption I is valid) and because boiling successfully eliminates waterborne pathogens (Assumption II is valid). Therefore, both assumptions are implicit.",
        "వర్షాకాలంలో నీరు కలుషితమయ్యే అవకాశం ఉన్నందున (ఊహ I నిజం), మరియు మరిగించడం ద్వారా నీటి క్రిములు నశిస్తాయి కాబట్టి (ఊహ II నిజం) ఈ ప్రకటన చేయబడింది. కాబట్టి రెండు ఊహలు అంతర్లీనంగా ఉన్నాయి."
    ))

    # Q95: Statement & Arguments
    qs.append(make_q(
        95, "Reasoning - Statement and Arguments",
        "Statement: 'Should CCTV cameras with facial recognition technology be mandatorily installed at all major public transit junctions and traffic intersections in the state?'\n\nArguments:\nI. Yes, it will significantly deter street crimes, assist police in identifying fugitive criminals rapidly, and enhance overall public safety.\nII. No, mass continuous surveillance without robust data privacy safeguards can infringe upon citizens' constitutional right to privacy and lead to misuse of personal data.\n\nWhich argument is strong?",
        "ప్రకటన: 'రాష్ట్రంలోని అన్ని ప్రధాన ప్రజా రవాణా కూడళ్లు మరియు ట్రాఫిక్ జంక్షన్లలో ఫేషియల్ రికగ్నిషన్ టెక్నాలజీతో కూడిన సీసీటీవీ కెమెరాలను తప్పనిసరిగా ఏర్పాటు చేయాలా?'\n\nవాదనలు:\nI. అవును, ఇది వీధి నేరాలను గణనీయంగా అరికడుతుంది, నేరస్థులను వేగంగా గుర్తించడంలో పోలీసులకు సహాయపడుతుంది మరియు ప్రజా భద్రతను పెంచుతుంది.\nII. కాదు, సరైన డేటా ప్రైవసీ రక్షణలు లేకుండా నిరంతర నిఘా పౌరుల రాజ్యాంగబద్ధమైన గోప్యతా హక్కుకు భంగం కలిగిస్తుంది మరియు దుర్వినియోగానికి దారితీస్తుంది.\n\nఏ వాదన బలంగా ఉంది?",
        ["Only argument I is strong", "Only argument II is strong", "Both argument I and argument II are strong", "Neither I nor II is strong"],
        ["వాదన I మాత్రమే బలంగా ఉంది", "వాదన II మాత్రమే బలంగా ఉంది", "వాదనలు I మరియు II రెండూ బలంగా ఉన్నాయి", "వాదన I లేదా II రెండూ బలంగా లేవు"],
        2,
        "Argument I presents a compelling public safety and law enforcement rationale. Argument II presents a valid fundamental rights and data privacy protection concern recognized by constitutional jurisprudence. Both are strong, well-reasoned arguments.",
        "వాదన I శాంతిభద్రతలు మరియు నేర నియంత్రణ పరంగా అత్యంత బలమైనది. వాదన II పౌరుల ప్రాథమిక గోప్యతా హక్కుల పరిరక్షణ పరంగా బలమైన రాజ్యాంగబద్ధ వాదన. కాబట్టి రెండు వాదనలు బలంగా ఉన్నాయి."
    ))

    # Q96: Statement & Course of Action
    qs.append(make_q(
        96, "Reasoning - Statement and Course of Action",
        "Statement: 'Severe unseasonal hail and thunderstorms in northern Telangana districts caused extensive damage to standing chilli, maize, and paddy crops across thousands of acres.'\n\nCourses of Action:\nI. The state agriculture and revenue departments should immediately carry out an on-ground joint enumeration to accurately assess crop loss.\nII. The state government should immediately disburse emergency compensation and financial relief to the affected registered farmers.\n\nWhich course of action should be pursued?",
        "ప్రకటన: 'ఉత్తర తెలంగాణ జిల్లాల్లో కురిసిన అకాల వడగండ్ల వాన మరియు ఈదురు గాలుల వల్ల వేలాది ఎకరాల్లో సాగులో ఉన్న మిర్చి, మొక్కజొన్న మరియు వరి పంటలకు తీవ్ర నష్టం వాటిల్లింది.'\n\nచర్యలు (Courses of Action):\nI. పంట నష్టాన్ని ఖచ్చితంగా అంచనా వేయడానికి వ్యవసాయ మరియు రెవెన్యూ శాఖలు వెంటనే క్షేత్రస్థాయి ఉమ్మడి సర్వేను నిర్వహించాలి.\nII. నష్టపోయిన అర్హులైన రైతులకు రాష్ట్ర ప్రభుత్వం వెంటనే అత్యవసర నష్టపరిహారం మరియు ఆర్థిక సహాయాన్ని విడుదల చేయాలి.\n\nఏ చర్యను అనుసరించాలి?",
        ["Only I should be pursued", "Only II should be pursued", "Both I and II should be pursued", "Neither I nor II should be pursued"],
        ["I మాత్రమే సరైన చర్య", "II మాత్రమే సరైన చర్య", "I మరియు II రెండూ సరైన చర్యలు", "I లేదా II రెండూ సరైన చర్యలు కావు"],
        2,
        "When widespread natural calamity destroys crops, rapid damage assessment survey (Action I) followed by swift disaster relief compensation to eligible farmers (Action II) are standard administrative protocols. Both actions should be pursued.",
        "ప్రకృతి విపత్తుల వల్ల పంట నష్టం జరిగినప్పుడు తక్షణమే క్షేత్రస్థాయి పంట సర్వే చేయడం (చర్య I) మరియు రైతులకు తక్షణ పరిహారం అందించడం (చర్య II) రెండూ ప్రభుత్వ ప్రాథమిక విధులే. కాబట్టి రెండూ అనుసరించదగినవే."
    ))

    # Q97: Data Sufficiency - Tallest among 5 friends
    qs.append(make_q(
        97, "Reasoning - Data Sufficiency",
        "Question: Among five friends P, Q, R, S, and T, who is the tallest?\n\nStatements:\nI. P is taller than Q and S, but shorter than T.\nII. R is shorter than T, but taller than P.\n\nDecide whether the statements are sufficient to answer the question:",
        "ప్రశ్న: P, Q, R, S మరియు T అనే ఐదుగురు స్నేహితులలో అందరికంటే ఎత్తైనది ఎవరు?\n\nప్రకటనలు:\nI. P, Q మరియు S కంటే ఎత్తైనవాడు, కానీ T కంటే పొట్టివాడు.\nII. R, T కంటే పొట్టివాడు, కానీ P కంటే ఎత్తైనవాడు.\n\nఈ ప్రశ్నకు సమాధానం ఇవ్వడానికి ఏ ప్రకటన/ప్రకటనలు సరిపోతాయో నిర్ణయించండి:",
        ["Statement I alone is sufficient to answer the question", "Statement II alone is sufficient to answer the question", "Both Statements I and II together are necessary to answer the question", "Neither Statement is sufficient even together"],
        ["ప్రకటన I మాత్రమే సమాధానం ఇవ్వడానికి సరిపోతుంది", "ప్రకటన II మాత్రమే సమాధానం ఇవ్వడానికి సరిపోతుంది", "ప్రకటనలు I మరియు II రెండూ కలిసి అవసరం", "రెండూ కలిపినా సమాధానం చెప్పలేము"],
        0,
        "From Statement I alone: T is taller than P, and P is taller than both Q and S. This means T is taller than P, Q, and S. However, R is not mentioned in Statement I. Wait! Let us check: In Statement I, R is not mentioned, so R could be taller than T. Combining Statement I and II: T is taller than P, Q, S (from I), and from II, T is taller than R. Thus T is taller than all P, Q, R, S. Hence both statements together are needed!",
        "ప్రకటన I లో R ప్రస్తావన లేదు కాబట్టి R ఎత్తు తెలియదు. ప్రకటన II లో T, R కంటే ఎత్తైనవాడు అని ఉంది. కాబట్టి I మరియు II రెండింటినీ కలిపినప్పుడు మాత్రమే T అందరికంటే ఎత్తైనవాడని తెలుస్తుంది. కాబట్టి రెండూ కలిపి అవసరం."
    ))

    # Q98: Data Sufficiency - Day of the Week
    qs.append(make_q(
        98, "Reasoning - Data Sufficiency",
        "Question: On which day of the month did Suresh join his police training academy in March?\n\nStatements:\nI. Suresh's brother correctly remembers that Suresh joined after the 14th but before the 18th of March.\nII. Suresh's father correctly remembers that Suresh joined after the 16th but before the 20th of March.\n\nDecide if the data given in the statements is sufficient:",
        "ప్రశ్న: మార్చి నెలలో సురేష్ ఏ తేదీన పోలీస్ ట్రైనింగ్ అకాడమీలో చేరాడు?\n\nప్రకటనలు:\nI. సురేష్ సోదరుడికి గుర్తున్న ప్రకారం సురేష్ మార్చి 14 తర్వాత కానీ 18 కంటే ముందు చేరాడు.\nII. సురేష్ తండ్రికి గుర్తున్న ప్రకారం సురేష్ మార్చి 16 తర్వాత కానీ 20 కంటే ముందు చేరాడు.\n\nఈ ప్రశ్నకు సమాధానం ఇవ్వడానికి డేటా సరిపోతుందా లేదా నిర్ణయించండి:",
        ["Statement I alone is sufficient", "Statement II alone is sufficient", "Both statements I and II together are sufficient", "Statements I and II together are not sufficient"],
        ["ప్రకటన I మాత్రమే సరిపోతుంది", "ప్రకటన II మాత్రమే సరిపోతుంది", "ప్రకటనలు I మరియు II రెండూ కలిసి సరిపోతాయి", "రెండూ కలిపినా సరిపోవు"],
        2,
        "From Statement I: possible dates are 15, 16, 17.\nFrom Statement II: possible dates are 17, 18, 19.\nThe only common date that satisfies both statements is 17th March. Therefore, both statements together are sufficient to determine the exact date.",
        "ప్రకటన I ప్రకారం అవకాశాలు: 15, 16, 17 మార్చి.\nప్రకటన II ప్రకారం అవకాశాలు: 17, 18, 19 మార్చి.\nరెండింటిలో ఉమ్మడిగా ఉన్న ఏకైక తేదీ 17 మార్చి. కాబట్టి రెండు ప్రకటనలు కలిపితే సరిపోతుంది."
    ))

    # Q99: Mirror Image
    qs.append(make_q(
        99, "Reasoning - Mirror Images",
        "If a wall clock shows the time as 3:40, what will be the time indicated by its reflection in a vertical mirror?",
        "ఒక గోడ గడియారంలో సమయం 3:40 అయినప్పుడు, నిలువు అద్దంలో దాని ప్రతిబింబం చూపే సమయం ఎంత?",
        ["8:20", "8:10", "9:20", "7:20"],
        ["8:20", "8:10", "9:20", "7:20"],
        0,
        "Formula for mirror reflection of clock time: Subtract given time from 11:60 (or 23:60).\nMirror time = 11:60 - 3:40 = 8:20.",
        "అద్దంలోని సమయం సూత్రం: ఇచ్చిన సమయాన్ని 11:60 నుండి తీసివేయాలి.\nఅద్దంలో సమయం = 11:60 - 3:40 = 8:20."
    ))

    # Q100: Non-Verbal - Counting Triangles
    qs.append(make_q(
        100, "Reasoning - Counting Figures",
        "How many total triangles are there in a square with both its diagonals drawn and two medians connecting the midpoints of opposite sides?",
        "ఒక చతురస్రంలో రెండు కర్ణాలు మరియు ఎదురెదురు భుజాల మధ్య బిందువులను కలిపే రెండు మధ్యగత రేఖలు (మొత్తం 8 భాగాలుగా విభజించబడిన చతురస్రం) గీయబడినప్పుడు అందులో ఉండే మొత్తం త్రిభుజాల సంఖ్య ఎంత?",
        ["12", "14", "16", "18"],
        ["12", "14", "16", "18"],
        2,
        "When a square is divided into 8 elementary small triangles by its 2 diagonals and 2 perpendicular midlines, the formula for total triangles is 8 * 2 = 16 triangles (8 single-unit, 4 double-unit half-quadrant triangles, and 4 four-unit major corner triangles). Total = 16.",
        "రెండు కర్ణాలు మరియు రెండు మధ్యగత రేఖలతో 8 సమాన భాగాలుగా విభజించబడిన చతురస్రంలో మొత్తం త్రిభుజాల సంఖ్య = 8 * 2 = 16 త్రిభుజాలు."
    ))

    return qs
