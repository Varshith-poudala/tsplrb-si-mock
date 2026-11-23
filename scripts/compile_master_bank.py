# -*- coding: utf-8 -*-
"""
Compile the Master Aptitude & Reasoning Bank (350 Questions)
- 175 Arithmetic & Quantitative Reasoning (Q1 to Q175)
- 175 Mental Ability & Logical Reasoning (Q176 to Q350)
- 100% Bilingual (English & Telugu)
- Balanced option distribution (~25% each A, B, C, D)
- 0 Duplicates against Mocks 1-12
- 0 Internal Duplicates
- Output: public/data/master_aptitude_reasoning_bank.json
"""
import sys, os, glob, json
from datetime import datetime

sys.path.append('scripts')
import build_arithmetic_part1
import build_arithmetic_part2
import build_arithmetic_part3
import build_reasoning_part1
import build_reasoning_part2
import build_reasoning_part3

def make_q(id_num, section, topic, diff, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
    return {
        "id": id_num,
        "section": section,
        "topic": topic,
        "difficulty": diff,
        "question_en": q_en.strip(),
        "question_te": q_te.strip(),
        "options_en": [str(o).strip() for o in opts_en],
        "options_te": [str(o).strip() for o in opts_te],
        "correct_option": int(corr),
        "explanation_en": exp_en.strip(),
        "explanation_te": exp_te.strip()
    }

REPLACEMENTS = {
    # 17: Platform & Post (Internal collision override)
    17: make_q(
        17, "Arithmetic & Quantitative Reasoning", "Speed, Distance & Time - Platform & Post", "Medium",
        "Running at a uniform speed, a railway express train passes a telegraph post in 9 seconds and completely crosses a railway platform 260 metres long in 22 seconds. What is the length of the train?",
        "ఒక రైల్వే ఎక్స్‌ప్రెస్ రైలు సమవేగంతో ప్రయాణిస్తూ ఒక టెలిగ్రాఫ్ స్తంభాన్ని 9 సెకన్లలో మరియు 260 మీటర్ల పొడవు గల ప్లాట్‌ఫారమ్‌ను 22 సెకన్లలో దాటుతుంది. ఆ రైలు పొడవు ఎంత?",
        ["180 metres", "200 metres", "160 metres", "220 metres"],
        ["180 మీటర్లు", "200 మీటర్లు", "160 మీటర్లు", "220 మీటర్లు"],
        0,
        "Time taken to cover platform alone = 22 - 9 = 13 seconds.\nSpeed of train = 260 / 13 = 20 m/s.\nLength of train = Speed * Time to cross post = 20 * 9 = 180 metres.",
        "ప్లాట్‌ఫారమ్‌ను దాటడానికి పట్టిన సమయం = 22 - 9 = 13 సెకన్లు.\nరైలు వేగం = 260 / 13 = 20 మీ/సె.\nరైలు పొడవు = 20 * 9 = 180 మీటర్లు."
    ),

    # 32: Rhombus (Mock deduplication override)
    32: make_q(
        32, "Arithmetic & Quantitative Reasoning", "Mensuration 2D - Rhombus", "Hard",
        "A rhombus-shaped obstacle course has a perimeter of 116 metres and one of its diagonals measures 42 metres. What is the area of the obstacle course in square metres?",
        "రాంబస్ ఆకారంలో ఉన్న ఒక అడ్డంకుల గ్రౌండ్ చుట్టుకొలత 116 మీటర్లు మరియు దాని ఒక కర్ణం పొడవు 42 మీటర్లు. చదరపు మీటర్లలో ఆ గ్రౌండ్ వైశాల్యం ఎంత?",
        ["840 sq m", "820 sq m", "860 sq m", "800 sq m"],
        ["840 చ.మీ", "820 చ.మీ", "860 చ.మీ", "800 చ.మీ"],
        0,
        "Side of rhombus a = 116 / 4 = 29 m. Half diagonal d1 / 2 = 21 m.\nOther half diagonal = sqrt(29^2 - 21^2) = sqrt(841 - 441) = sqrt(400) = 20 m => d2 = 40 m.\nArea = (1/2) * d1 * d2 = (1/2) * 42 * 40 = 840 sq m.",
        "రాంబస్ భుజం a = 29 మీ. కర్ణం d1/2 = 21 మీ.\nరెండవ అర్థ కర్ణం = sqrt(29^2 - 21^2) = 20 మీ => d2 = 40 మీ.\nవైశాల్యం = (1/2) * 42 * 40 = 840 చ.మీ."
    ),

    # 36: Melting Solids (Mock deduplication override)
    36: make_q(
        36, "Arithmetic & Quantitative Reasoning", "Mensuration 3D - Melting Solids", "Hard",
        "Three solid lead spheres having diameters of 6 cm, 8 cm, and 10 cm respectively are melted together to form a single solid sphere. What is the surface area of the newly formed sphere? (Take pi = 22/7)",
        "వరుసగా 6 సెం.మీ, 8 సెం.మీ మరియు 10 సెం.మీ వ్యాసాలు గల మూడు ఘన సీసపు గోళాలను కరిగించి ఒకే ఘన గోళంగా తయారు చేశారు. కొత్తగా ఏర్పడిన గోళం ఉపరితల వైశాల్యం ఎంత? (pi = 22/7)",
        ["452.57 sq cm", "420.25 sq cm", "484.50 sq cm", "436.00 sq cm"],
        ["452.57 చ.సెం.మీ", "420.25 చ.సెం.మీ", "484.50 చ.సెం.మీ", "436.00 చ.సెం.మీ"],
        0,
        "Radii of the 3 spheres are 3 cm, 4 cm, and 5 cm.\nTotal volume = (4/3)*pi*(3^3 + 4^3 + 5^3) = (4/3)*pi*(27 + 64 + 125) = (4/3)*pi*216.\nNew radius R^3 = 216 => R = 6 cm.\nSurface area = 4 * pi * R^2 = 4 * (22/7) * 36 = (88 * 36) / 7 = 3168 / 7 = 452.57 sq cm.",
        "మూడు గోళాల వ్యాసార్థాలు 3, 4, 5 సెం.మీ.\nనూతన వ్యాసార్థం R^3 = 27 + 64 + 125 = 216 => R = 6 సెం.మీ.\nఉపరితల వైశాల్యం = 4 * pi * 36 = 452.57 చ.సెం.మీ."
    ),

    # 38: Hemisphere Dome (Mock deduplication override)
    38: make_q(
        38, "Arithmetic & Quantitative Reasoning", "Mensuration 3D - Hemisphere Dome", "Medium",
        "A hemispherical security dome atop a police headquarters building has an internal radius of 14 metres. What is the total expenditure incurred in painting its inner curved surface at the rate of Rs. 15 per square metre? (Take pi = 22/7)",
        "పోలీస్ హెడ్‌క్వార్టర్స్ భవనంపై గల ఒక అర్థగోళాకార సెక్యూరిటీ డోమ్ అంతర్గత వ్యాసార్థం 14 మీటర్లు. చదరపు మీటరుకు రూ. 15 చొప్పున దాని లోపలి వక్రతల ఉపరితలానికి పెయింట్ వేయడానికి అయ్యే మొత్తం ఖర్చు ఎంత? (pi = 22/7)",
        ["Rs. 18,480", "Rs. 17,600", "Rs. 19,250", "Rs. 16,800"],
        ["రూ. 18,480", "రూ. 17,600", "రూ. 19,250", "రూ. 16,800"],
        0,
        "Inner curved surface area of hemisphere = 2 * pi * r^2 = 2 * (22/7) * 14^2 = 2 * 22 * 28 = 1,232 sq m.\nTotal cost = 1,232 * 15 = Rs. 18,480.",
        "అర్థగోళ లోపలి వక్రతల వైశాల్యం = 2 * pi * r^2 = 2 * (22/7) * 196 = 1,232 చ.మీ.\nమొత్తం ఖర్చు = 1,232 * 15 = రూ. 18,480."
    ),

    # 41: Circular Lawn Path (Mock deduplication override)
    41: make_q(
        41, "Arithmetic & Quantitative Reasoning", "Mensuration 2D - Circular Lawn Path", "Medium",
        "A circular police lawn has a radius of 28 metres. A gravel walking path of uniform width 3.5 metres is constructed completely around its outside perimeter. Find the total expenditure incurred in gravelling the path at Rs. 20 per square metre. (Take pi = 22/7)",
        "28 మీటర్ల వ్యాసార్థం గల ఒక వృత్తాకార పోలీస్ లాన్ చుట్టూ బయటి వైపు 3.5 మీటర్ల సమాన వెడల్పుతో నడక దారి నిర్మించబడింది. చదరపు మీటరుకు రూ. 20 చొప్పున ఆ దారికి గ్రావెల్ వేయడానికి అయ్యే మొత్తం ఖర్చు ఎంత? (pi = 22/7)",
        ["Rs. 13,090", "Rs. 12,500", "Rs. 13,850", "Rs. 11,900"],
        ["రూ. 13,090", "రూ. 12,500", "రూ. 13,850", "రూ. 11,900"],
        0,
        "Inner radius r = 28 m. Outer radius R = 28 + 3.5 = 31.5 m.\nArea of path = pi * (R^2 - r^2) = (22/7) * (31.5 + 28) * (31.5 - 28) = (22/7) * 59.5 * 3.5 = 22 * 59.5 * 0.5 = 654.5 sq m.\nTotal expenditure = 654.5 * 20 = Rs. 13,090.",
        "లోపలి వ్యాసార్థం r = 28 మీ. వెలుపలి వ్యాసార్థం R = 31.5 మీ.\nదారి వైశాల్యం = (22/7) * 59.5 * 3.5 = 654.5 చ.మీ.\nమొత్తం ఖర్చు = 654.5 * 20 = రూ. 13,090."
    ),

    # 61: Three Workers Alternate Days (Mock deduplication override)
    61: make_q(
        61, "Arithmetic & Quantitative Reasoning", "Time & Work - Three Workers Alternate Days", "Hard",
        "Three cyber forensic technicians X, Y, and Z can independently audit a crime server database in 12, 15, and 20 days respectively. If they work on alternate days in cyclical rotation starting with X on the first day, then Y on the second day, and Z on the third day, in how many days will the entire audit be finished?",
        "ముగ్గురు సైబర్ ఫోరెన్సిక్ నిపుణులు X, Y మరియు Z లు ఒక క్రైమ్ సర్వర్ డేటాబేస్‌ను వరుసగా 12, 15 మరియు 20 రోజుల్లో స్వతంత్రంగా ఆడిట్ చేయగలరు. మొదటి రోజు X, రెండవ రోజు Y మరియు మూడవ రోజు Z చొప్పున రోజు మార్చి రోజు చక్రీయ క్రమంలో పనిచేస్తే, ఆ ఆడిట్ మొత్తం ఎన్ని రోజుల్లో పూర్తవుతుంది?",
        ["15 days", "16 days", "14 1/2 days", "18 days"],
        ["15 రోజులు", "16 రోజులు", "14 1/2 రోజులు", "18 రోజులు"],
        0,
        "Total work = LCM(12, 15, 20) = 60 units.\nEfficiencies: X = 5 units/day, Y = 4 units/day, Z = 3 units/day.\nWork completed in 1 cycle (3 days) = 5 + 4 + 3 = 12 units.\nNumber of complete 3-day cycles to finish 60 units = 60 / 12 = 5 cycles.\nTotal time required = 5 cycles * 3 days = 15 days.",
        "మొత్తం పని = LCM(12, 15, 20) = 60 యూనిట్లు. సామర్థ్యాలు: X = 5, Y = 4, Z = 3.\nఒక సైకిల్ (3 రోజులు) లో పూర్తయ్యే పని = 5 + 4 + 3 = 12 యూనిట్లు.\n60 యూనిట్లకు పట్టే సైకిల్స్ = 60 / 12 = 5 సైకిల్స్.\nమొత్తం రోజులు = 5 * 3 = 15 రోజులు."
    ),

    # 87: Waste Pipe Flow (Internal collision override)
    87: make_q(
        87, "Arithmetic & Quantitative Reasoning", "Pipes & Cisterns - Waste Pipe Flow", "Hard",
        "In a water storage facility, two filling pipes A and B fill a cistern in 10 hours and 12 hours respectively. An outlet waste pipe discharges water at 80 gallons per hour. When all three pipes operate simultaneously, the empty cistern is completely filled in 20 hours. What is the capacity of the cistern?",
        "ఒక నీటి నిల్వ కేంద్రంలో రెండు పైపులు A మరియు B ఒక తొట్టిని వరుసగా 10 గంటలు మరియు 12 గంటల్లో నింపగలవు. ఒక వ్యర్థపు పైపు గంటకు 80 గ్యాలన్ల నీటిని ఖాళీ చేస్తుంది. మూడు పైపులు కలిసి పనిచేసినప్పుడు ఖాళీ తొట్టి 20 గంటల్లో నిండుతుంది. ఆ తొట్టి సామర్థ్యం ఎంత?",
        ["600 gallons", "720 gallons", "800 gallons", "540 gallons"],
        ["600 గ్యాలన్లు", "720 గ్యాలన్లు", "800 గ్యాలన్లు", "540 గ్యాలన్లు"],
        0,
        "Rate of waste pipe C: (1/10) + (1/12) - (1/C) = (1/20)\n1/C = (1/10 + 1/12 - 1/20) = (6 + 5 - 3) / 60 = 8 / 60 = 2 / 15 tank/hour.\nTime for waste pipe to empty full tank = 15 / 2 = 7.5 hours.\nCapacity = 7.5 hours * 80 gallons/hour = 600 gallons.",
        "వ్యర్థపు పైప్ C వేగం = 1/10 + 1/12 - 1/20 = 8/60 = 2/15 తొట్టి/గంట.\nఖాళీ చేయడానికి పట్టే కాలం = 7.5 గంటలు.\nసామర్థ్యం = 7.5 * 80 = 600 గ్యాలన్లు."
    ),

    # 96: False Weight and Markup (Mock deduplication override)
    96: make_q(
        96, "Arithmetic & Quantitative Reasoning", "Profit, Loss & Discount - False Weight and Markup", "Hard",
        "A fraudulent ration dealer marks his goods 15% above the cost price, but also cheats his customers by delivering only 920 grams for every 1 kilogram requested. What is his actual net profit percentage?",
        "ఒక రేషన్ డీలర్ తన సరుకులపై కొన్న ధర కంటే 15% అధికంగా ధరను నిర్ణయిస్తూ, ప్రతి 1 కిలోగ్రాముకు బదులుగా కేవలం 920 గ్రాములను మాత్రమే ఇచ్చి వినియోగదారులను మోసం చేస్తాడు. అతని వాస్తవ నికర లాభ శాతం ఎంత?",
        ["25%", "22.5%", "24%", "20%"],
        ["25%", "22.5%", "24%", "20%"],
        0,
        "Let cost price of 1,000 grams = Rs. 100.\nDealer delivers 920 grams => actual cost price to dealer = Rs. 92.\nSelling price charged by dealer = 100 * (1 + 0.15) = Rs. 115.\nNet profit = 115 - 92 = Rs. 23 on a cost of Rs. 92.\nNet profit percentage = (23 / 92) * 100 = 1/4 * 100 = 25%.",
        "1,000 గ్రాముల కొన్న ధర = రూ. 100 అనుకుంటే, డీలర్ ఇచ్చే 920 గ్రాముల ఖరీదు = రూ. 92.\nడీలర్ నిర్ణయించిన అమ్మకపు ధర = రూ. 115.\nనికర లాభం = 115 - 92 = రూ. 23.\nలాభ శాతం = (23 / 92) * 100 = 25%."
    ),

    # 111: Principal from 2-Year Difference (Mock deduplication override)
    111: make_q(
        111, "Arithmetic & Quantitative Reasoning", "Simple & Compound Interest - Principal from 2-Year Difference", "Hard",
        "If the difference between compound interest (compounded annually) and simple interest on a certain principal sum of money for 2 years at 12% per annum is Rs. 144, what is the value of the principal sum?",
        "ఒక నిర్దిష్ట అసలు మొత్తంపై సంవత్సరానికి 12% వడ్డీ రేటుతో 2 సంవత్సరాలకు అయ్యే చక్రవడ్డీ మరియు బారువడ్డీల మధ్య వ్యత్యాసం రూ. 144 అయితే, ఆ అసలు మొత్తం ఎంత?",
        ["Rs. 10,000", "Rs. 12,000", "Rs. 9,600", "Rs. 10,500"],
        ["రూ. 10,000", "రూ. 12,000", "రూ. 9,600", "రూ. 10,500"],
        0,
        "Formula: CI - SI = P * (R / 100)^2 for 2 years.\n144 = P * (12 / 100)^2 => 144 = P * (144 / 10,000)\nP = (144 * 10,000) / 144 = Rs. 10,000.",
        "2 సంవత్సరాల వ్యత్యాసం: CI - SI = P * (R / 100)^2.\n144 = P * (144 / 10,000) => అసలు P = రూ. 10,000."
    ),

    # 112: Principal from 3-Year Difference (Mock deduplication override)
    112: make_q(
        112, "Arithmetic & Quantitative Reasoning", "Simple & Compound Interest - Principal from 3-Year Difference", "Hard",
        "A financial investor noted that on a certain principal sum invested for 3 years at an annual interest rate of 5% per annum, the difference between the compound interest and simple interest amounted to exactly Rs. 122. What was the principal sum invested?",
        "ఒక మొత్తంపై వార్షికంగా 5% వడ్డీ రేటుతో 3 సంవత్సరాలకు అయ్యే చక్రవడ్డీ మరియు బారువడ్డీల మధ్య వ్యత్యాసం రూ. 122. ఆ పెట్టుబడి పెట్టిన అసలు మొత్తం ఎంత?",
        ["Rs. 16,000", "Rs. 15,000", "Rs. 18,000", "Rs. 14,500"],
        ["రూ. 16,000", "రూ. 15,000", "రూ. 18,000", "రూ. 14,500"],
        0,
        "Formula for 3 years: Difference = P * (R/100)^2 * (3 + R/100)\n122 = P * (5/100)^2 * (3 + 0.05) = P * (1/400) * (305 / 100) = P * (305 / 40,000) = P * (61 / 8,000)\nP = (122 * 8,000) / 61 = 2 * 8,000 = Rs. 16,000.",
        "3 సంవత్సరాల వ్యత్యాస సూత్రం: 122 = P * (5/100)^2 * 3.05 = P * (61 / 8,000).\nఅసలు P = (122 * 8000) / 61 = రూ. 16,000."
    ),

    # 114: Doubling Formula (Internal collision override)
    114: make_q(
        114, "Arithmetic & Quantitative Reasoning", "Simple & Compound Interest - Doubling Formula", "Medium",
        "Under annual compound interest, a fixed monetary deposit doubles its initial value in 5 years. In how many years will it grow to become 8 times its original principal value at the same interest rate?",
        "వార్షిక చక్రవడ్డీ ప్రకారం ఒక ఫిక్స్డ్ డిపాజిట్ 5 సంవత్సరాలలో రెట్టింపు అవుతుంది. అదే వడ్డీ రేటుతో అది 8 రెట్లు కావడానికి ఎన్ని సంవత్సరాలు పడుతుంది?",
        ["15 years", "20 years", "25 years", "12 years"],
        ["15 సంవత్సరాలు", "20 సంవత్సరాలు", "25 సంవత్సరాలు", "12 సంవత్సరాలు"],
        0,
        "At CI, if a sum becomes 2^1 times in 5 years, it becomes 2^n times in (n * 5) years.\nHere 8 = 2^3 => n = 3.\nTime required = 3 * 5 = 15 years.",
        "చక్రవడ్డీ వద్ద: 2^1 రెట్లు కావడానికి 5 సంవత్సరాలు పడితే, 8 రెట్లు (2^3) కావడానికి = 3 * 5 = 15 సంవత్సరాలు పడుతుంది."
    ),

    # 120: Quarterly Compounding (Internal collision override)
    120: make_q(
        120, "Arithmetic & Quantitative Reasoning", "Simple & Compound Interest - Quarterly Compounding", "Hard",
        "Calculate the compound interest accrued on a principal deposit of Rs. 16,000 for a duration of 9 months at 20% per annum, when the interest is compounded on a quarterly basis.",
        "రూ. 16,000 అసలుపై 20% వార్షిక వడ్డీ రేటుతో ప్రతి త్రైమాసికానికి (Quarterly) చక్రవడ్డీ లెక్కించినప్పుడు 9 నెలలకు అయ్యే చక్రవడ్డీ ఎంత?",
        ["Rs. 2,522", "Rs. 2,400", "Rs. 2,610", "Rs. 2,480"],
        ["రూ. 2,522", "రూ. 2,400", "రూ. 2,610", "రూ. 2,480"],
        0,
        "Quarterly rate r = 20% / 4 = 5%. Time = 9 months = 3 quarters (n = 3).\nAmount = 16,000 * (1 + 0.05)^3 = 16,000 * (1.05)^3 = 16,000 * 1.157625 = Rs. 18,522.\nCompound Interest = 18,522 - 16,000 = Rs. 2,522.",
        "త్రైమాసిక వడ్డీ రేటు = 5%, n = 3 త్రైమాసికాలు.\nమొత్తం = 16,000 * (1.05)^3 = రూ. 18,522.\nచక్రవడ్డీ = 18,522 - 16,000 = రూ. 2,522."
    ),

    # 121: Price Decrease Consumption Increase (Mock deduplication override)
    121: make_q(
        121, "Arithmetic & Quantitative Reasoning", "Percentages - Price Decrease Consumption Increase", "Medium",
        "The price of diesel used by a highway patrol unit decreased by 20%. By what percentage can the police patrol unit increase its diesel consumption such that its total fuel expenditure remains constant?",
        "హైవే పెట్రోలింగ్ యూనిట్ ఉపయోగించే డీజిల్ ధర 20% తగ్గింది. వారి మొత్తం ఇంధన ఖర్చు మారకుండా ఉండాలంటే ఆ యూనిట్ తమ డీజిల్ వినియోగాన్ని ఎంత శాతం పెంచుకోవచ్చు?",
        ["25%", "20%", "16 2/3%", "22.5%"],
        ["25%", "20%", "16 2/3%", "22.5%"],
        0,
        "Formula: % increase in consumption = [r / (100 - r)] * 100\nIncrease = [20 / (100 - 20)] * 100 = (20 / 80) * 100 = 1/4 * 100 = 25%.",
        "సూత్రం: వినియోగంలో పెరుగుదల శాతం = [r / (100 - r)] * 100.\nపెరుగుదల = [20 / 80] * 100 = 25%."
    ),

    # 137: Grain Blending Ratio (Mock deduplication override)
    137: make_q(
        137, "Arithmetic & Quantitative Reasoning", "Mixtures & Alligation - Grain Blending Ratio", "Medium",
        "In what ratio must a merchant blend two varieties of basmati rice priced at Rs. 85 per kg and Rs. 115 per kg respectively, so that by selling the blended rice at Rs. 120 per kg he secures a profit of 20%?",
        "ఒక వ్యాపారి కిలో రూ. 85 మరియు కిలో రూ. 115 ఖరీదు చేసే రెండు రకాల బాస్మతి బియ్యాన్ని ఏ నిష్పత్తిలో కలిపి, ఆ మిశ్రమాన్ని కిలో రూ. 120 కు విక్రయించడం ద్వారా 20% లాభం పొందగలడు?",
        ["1 : 1", "2 : 3", "3 : 2", "1 : 2"],
        ["1 : 1", "2 : 3", "3 : 2", "1 : 2"],
        0,
        "Mean Cost Price of mixture = Selling Price / (1 + Profit%) = 120 / 1.20 = Rs. 100 per kg.\nBy Alligation rule:\nCheaper (85)        Dearer (115)\n            Mean (100)\n(115 - 100) = 15    (100 - 85) = 15\nRatio = 15 : 15 = 1 : 1.",
        "సగటు కొన్న ధర = 120 / 1.20 = రూ. 100 / కి.గ్రా.\nఅలిగేషన్ సూత్రం: (115 - 100) : (100 - 85) = 15 : 15 = 1 : 1."
    ),

    # 155: Large Power Remainder (Mock deduplication override)
    155: make_q(
        155, "Arithmetic & Quantitative Reasoning", "Number Systems - Large Power Remainder", "Hard",
        "What is the remainder when 2^100 is divided by 17?",
        "2^100 ను 17 చే భాగించినప్పుడు వచ్చే శేషం ఎంత?",
        ["16", "1", "4", "8"],
        ["16", "1", "4", "8"],
        0,
        "2^4 = 16 = 17 - 1 = -1 (mod 17).\n2^8 = (-1)^2 = 1 (mod 17).\n100 = 12 * 8 + 4 => 2^100 = (2^8)^12 * 2^4 = 1^12 * 16 = 16.\nRemainder is 16.",
        "2^4 = 16 = -1 (mod 17). 2^8 = 1 (mod 17).\n2^100 = (2^8)^12 * 2^4 = 1 * 16 = 16. శేషం = 16."
    ),

    # 164: Divisibility by 72 (Mock deduplication override)
    164: make_q(
        164, "Arithmetic & Quantitative Reasoning", "Number Systems - Divisibility by 72", "Hard",
        "If the 9-digit number 985x3678y is completely divisible by 72, what is the value of (4x - 3y)? (where x and y are single digits)",
        "తొమ్మిది అంకెల సంఖ్య 985x3678y అనేది 72 చే నిశ్శేషంగా భాగింపబడితే, (4x - 3y) యొక్క విలువ ఎంత? (ఇక్కడ x మరియు y లు ఏక అంకెలు)",
        ["4", "2", "6", "0"],
        ["4", "2", "6", "0"],
        0,
        "A number is divisible by 72 if it is divisible by both 8 and 9.\nFor divisibility by 8, last 3 digits 78y must be divisible by 8: 784 / 8 = 98 => y = 4.\nFor divisibility by 9, sum of digits must be divisible by 9:\n9 + 8 + 5 + x + 3 + 6 + 7 + 8 + 4 = 50 + x.\nFor (50 + x) to be a multiple of 9, x must be 4 (50 + 4 = 54 = 9 * 6).\nSo x = 4 and y = 4.\nRequired value: (4x - 3y) = 4(4) - 3(4) = 16 - 12 = 4.",
        "72 భాజనీయత = 8 మరియు 9 లచే భాగించబడాలి.\nచివరి మూడు అంకెలు 78y కావున y = 4.\nఅంకెల మొత్తం 50 + x అనేది 9 చే భాగించబడాలి కావున x = 4.\n(4x - 3y) = 16 - 12 = 4."
    ),

    # 170: Two Dice Product Even (Mock deduplication override)
    170: make_q(
        170, "Arithmetic & Quantitative Reasoning", "Probability - Two Dice Product Even", "Medium",
        "Two fair six-sided dice are rolled simultaneously. What is the probability that the product of the two numbers obtained is an even number?",
        "రెండు నిష్పాక్షిక ఆరు ముఖాల పాచికలను ఒకేసారి దొర్లించినప్పుడు, ఆ రెండు సంఖ్యల లబ్ధం ఒక సరి సంఖ్య అయ్యే సంభావ్యత ఎంత?",
        ["3 / 4", "1 / 2", "2 / 3", "5 / 8"],
        ["3 / 4", "1 / 2", "2 / 3", "5 / 8"],
        0,
        "Total possible outcomes = 6 * 6 = 36.\nThe product of two integers is odd ONLY if both numbers are odd.\nOdd outcomes on single die = {1, 3, 5} (3 choices).\nOutcomes where product is odd = 3 * 3 = 9 outcomes.\nOutcomes where product is even = Total - Odd outcomes = 36 - 9 = 27 outcomes.\nProbability = 27 / 36 = 3 / 4.",
        "మొత్తం ఫలితాలు = 36.\nరెండు సంఖ్యలు బేసి సంఖ్యలు అయినప్పుడు మాత్రమే లబ్ధం బేసి సంఖ్య అవుతుంది = 3 * 3 = 9.\nలబ్ధం సరి సంఖ్య అయ్యే ఫలితాలు = 36 - 9 = 27.\nసంభావ్యత = 27 / 36 = 3 / 4."
    ),

    # 171: One Spade and One Heart (Mock deduplication override)
    171: make_q(
        171, "Arithmetic & Quantitative Reasoning", "Probability - One Spade and One Heart", "Hard",
        "From a well-shuffled pack of 52 playing cards, two cards are drawn at random simultaneously. What is the probability that one card is a Spade and the other card is a Heart?",
        "బాగా కలిపిన 52 పేక ముక్కల కట్ట నుండి ఒకేసారి యాదృచ్ఛికంగా రెండు కార్డులను తీశారు. అందులో ఒక కార్డు స్పేడ్ (Spade) మరియు మరొక కార్డు హార్ట్ (Heart) అయ్యే సంభావ్యత ఎంత?",
        ["13 / 102", "1 / 16", "13 / 204", "1 / 8"],
        ["13 / 102", "1 / 16", "13 / 204", "1 / 8"],
        0,
        "Total ways of choosing 2 cards from 52 = 52C2 = (52 * 51) / 2 = 1,326.\nNumber of ways to choose 1 Spade (from 13) = 13C1 = 13.\nNumber of ways to choose 1 Heart (from 13) = 13C1 = 13.\nFavourable ways = 13 * 13 = 169.\nProbability = 169 / 1,326 = 13 / 102.",
        "మొత్తం ఎంపికలు = 52C2 = 1,326.\nఅనుకూల ఎంపికలు = 13C1 * 13C1 = 169.\nసంభావ్యత = 169 / 1,326 = 13 / 102."
    ),

    # 188: 400-Year Leap Count (Mock deduplication override)
    188: make_q(
        188, "Mental Ability & Logical Reasoning", "Calendar - 400-Year Leap Count", "Hard",
        "How many total leap years are there in a continuous span of 400 consecutive years?",
        "400 వరుస సంవత్సరాల కాలవ్యవధిలో మొత్తం ఎన్ని లీపు సంవత్సరాలు ఉంటాయి?",
        ["97 leap years", "100 leap years", "96 leap years", "98 leap years"],
        ["97 లీపు సంవత్సరాలు", "100 లీపు సంవత్సరాలు", "96 లీపు సంవత్సరాలు", "98 లీపు సంవత్సరాలు"],
        0,
        "In 400 consecutive years:\nNormal division 400 / 4 = 100 potential leap years.\nHowever, century years divisible by 100 but not by 400 are NOT leap years (Years 100, 200, 300 are 3 non-leap century years).\nThe 400th year IS a leap year (divisible by 400).\nTotal leap years = 100 - 3 = 97 leap years.",
        "400 / 4 = 100 లీపు సంవత్సరాలు అనుకుంటాం, కానీ 100, 200, 300 లు లీపు సంవత్సరాలు కావు (400వ సంవత్సరం లీపు సంవత్సరం).\nకావున మొత్తం లీపు సంవత్సరాలు = 100 - 3 = 97."
    ),

    # 191: Angle at 6:40 (Mock deduplication override)
    191: make_q(
        191, "Mental Ability & Logical Reasoning", "Clocks - Angle at 6:40", "Medium",
        "What is the exact acute angle formed between the hour hand and the minute hand of a clock at 6:40?",
        "ఒక గడియారంలో సమయం 6:40 అయినప్పుడు గంటల ముల్లు మరియు నిమిషాల ముల్లుల మధ్య ఏర్పడే ఖచ్చితమైన అల్పకోణం ఎంత?",
        ["40 degrees", "45 degrees", "35 degrees", "50 degrees"],
        ["40 డిగ్రీలు", "45 డిగ్రీలు", "35 డిగ్రీలు", "50 డిగ్రీలు"],
        0,
        "Formula: theta = |30 * H - (11 / 2) * M|\nFor H = 6, M = 40:\ntheta = |30 * 6 - (11 / 2) * 40| = |180 - 220| = |-40| = 40 degrees.",
        "సూత్రం: theta = |30H - (11/2)M|.\ntheta = |30 * 6 - (11/2) * 40| = |180 - 220| = 40 డిగ్రీలు."
    ),

    # 212: Portrait Wife Relation (Mock deduplication override)
    212: make_q(
        212, "Mental Ability & Logical Reasoning", "Blood Relations - Portrait Wife Relation", "Hard",
        "Pointing to a lady in police uniform in a photograph, a senior officer remarked: \"Her only brother's daughter is the sister of my wife.\" How is the lady in the photograph related to the officer's wife?",
        "ఫోటోలోని ఒక మహిళా పోలీస్ అధికారిణిని చూపిస్తూ ఒక సీనియర్ అధికారి ఇలా అన్నాడు: \"ఆమె యొక్క ఏకైక సోదరుడి కుమార్తె నా భార్యకు సోదరి అవుతుంది\". ఆ ఫోటోలోని మహిళ ఆ అధికారి భార్యకు ఏమవుతుంది?",
        ["Paternal Aunt (Father's sister)", "Maternal Aunt", "Mother", "Sister"],
        ["మేనత్త (Paternal Aunt)", "పినతల్లి", "తల్లి", "సోదరి"],
        0,
        "\"Her only brother's daughter is the sister of my wife.\"\nThis means the lady's brother is the father of the officer's wife.\nThe father's sister is the Paternal Aunt (Menatta).\nTherefore, the lady is the Paternal Aunt of the officer's wife.",
        "ఆమె సోదరుడి కుమార్తె అధికారి భార్యకు సోదరి, అంటే ఆ మహిళ సోదరుడు అధికారి భార్యకు తండ్రి.\nతండ్రి యొక్క సోదరి = మేనత్త (Paternal Aunt)."
    ),

    # 299: Radar Screen Rotation (Mock deduplication override)
    299: make_q(
        299, "Mental Ability & Logical Reasoning", "Direction Sense - Radar Screen Rotation", "Hard",
        "On a malfunctioning police radar screen, North-West is displayed as East, and South-West is displayed as North. Under this exact angular rotation calibration, what will South be displayed as?",
        "లోపభూయిష్టమైన ఒక పోలీస్ రాడార్ స్క్రీన్‌పై వాయువ్యం (North-West) తూర్పుగాను, నైరుతి (South-West) ఉత్తరంగాను చూపబడుతున్నాయి. ఇదే కోణీయ మార్పు ప్రకారం, దక్షిణం (South) ఏ దిశగా చూపబడుతుంది?",
        ["North-West", "South-East", "North-East", "West"],
        ["వాయువ్యం (North-West)", "ఆగ్నేయం", "ఈశాన్యం", "పశ్చిమం"],
        0,
        "North-West (315 deg) is rotated to East (90 deg), which corresponds to a clockwise rotation of 135 degrees (315 + 135 = 450 mod 360 = 90 deg).\nSimilarly, South-West (225 deg) rotated +135 deg clockwise gives (225 + 135 = 360 = 0 deg North).\nRotating South (180 deg) by 135 deg clockwise:\n180 + 135 = 315 deg = North-West.\nTherefore, South will be displayed as North-West.",
        "వాయువ్యం 135 డిగ్రీలు సవ్యదిశలో తిరిగి తూర్పు అయింది.\nదక్షిణం (180 డిగ్రీలు) 135 డిగ్రీలు సవ్యదిశలో తిరిగితే 315 డిగ్రీల వద్ద గల వాయువ్యం (North-West) అవుతుంది."
    ),

    # 348: Triangles with Base Dividers (Mock deduplication override)
    348: make_q(
        348, "Mental Ability & Logical Reasoning", "Figure Counting - Triangles with Base Dividers", "Medium",
        "A large triangle has lines drawn from its top vertex to the base, dividing the base into 4 equal segments. A horizontal line is also drawn across the triangle parallel to the base. What is the total number of triangles in the entire figure?",
        "ఒక పెద్ద త్రిభుజం పై శీర్షం నుండి భూమికి గీసిన రేఖలు భూమిని 4 సమాన భాగాలుగా విభజించాయి. అలాగే భూమికి సమాంతరంగా త్రిభుజం గుండా ఒక అడ్డ రేఖ కూడా గీయబడింది. ఆ పూర్తి పటంలో గల మొత్తం త్రిభుజాల సంఖ్య ఎంత?",
        ["20 triangles", "16 triangles", "24 triangles", "18 triangles"],
        ["20 త్రిభుజాలు", "16 త్రిభుజాలు", "24 త్రిభుజాలు", "18 త్రిభుజాలు"],
        0,
        "Formula: Triangles in a base divided into n segments = n * (n + 1) / 2.\nHere base is divided into 4 segments => 4 * 5 / 2 = 10 triangles.\nSince there are 2 horizontal levels (base and parallel horizontal line), each level supports 10 triangles.\nTotal triangles = 10 * 2 = 20 triangles.",
        "భూమిపై 4 విభాగాలు కలవు: 4 * 5 / 2 = 10 త్రిభుజాలు.\nరెండు సమాంతర స్థాయిలు ఉన్నాయి కాబట్టి మొత్తం త్రిభుజాలు = 10 * 2 = 20 త్రిభుజాలు."
    )
}

def compile_bank():
    print("Compiling Master Aptitude & Reasoning Bank...")
    
    # 1. Collect all raw questions
    all_raw = (
        build_arithmetic_part1.get_part1() +
        build_arithmetic_part2.get_part2() +
        build_arithmetic_part3.get_part3() +
        build_reasoning_part1.get_reasoning_part1() +
        build_reasoning_part2.get_reasoning_part2() +
        build_reasoning_part3.get_reasoning_part3()
    )
    
    # 2. Apply unique overrides
    processed_qs = []
    for q in all_raw:
        if q['id'] in REPLACEMENTS:
            processed_qs.append(REPLACEMENTS[q['id']])
        else:
            processed_qs.append(q)
            
    assert len(processed_qs) == 350, f"Expected 350 questions, found {len(processed_qs)}"
    
    # 3. Clean bracket tags and balance options
    corr_dist = {}
    for q in processed_qs:
        # Strip any bracket tags if present
        for tag in ['[Advanced]', '[Speed]', '[Hard]', '[Medium]', '[Easy]', '[TSPLRB]']:
            q['question_en'] = q['question_en'].replace(tag, '').strip()
            q['question_te'] = q['question_te'].replace(tag, '').strip()
            
        # Deterministic balanced option shuffling
        curr_corr = q['correct_option']
        target_corr = (q['id'] * 7 + 3) % 4
        if curr_corr != target_corr:
            q['options_en'][curr_corr], q['options_en'][target_corr] = q['options_en'][target_corr], q['options_en'][curr_corr]
            q['options_te'][curr_corr], q['options_te'][target_corr] = q['options_te'][target_corr], q['options_te'][curr_corr]
            q['correct_option'] = target_corr
            
        corr_dist[q['correct_option']] = corr_dist.get(q['correct_option'], 0) + 1
        
        # Verify 4 options each
        assert len(q['options_en']) == 4, f"Q{q['id']} options_en != 4"
        assert len(q['options_te']) == 4, f"Q{q['id']} options_te != 4"
        assert 0 <= q['correct_option'] <= 3, f"Q{q['id']} invalid correct_option"
        assert q['question_en'] and q['question_te'], f"Q{q['id']} missing text"
        assert q['explanation_en'] and q['explanation_te'], f"Q{q['id']} missing explanation"

    print("Options distribution across 350 questions:", corr_dist)
    
    # 4. Deduplication against all 12 existing mocks
    existing_mocks = sorted(glob.glob('public/data/mock_test_full_200*.json'))
    existing_en = set()
    for m in existing_mocks:
        with open(m, 'r', encoding='utf-8') as f:
            data = json.load(f)
            qs = data if isinstance(data, list) else data.get('questions', [])
            for eq in qs:
                en = eq.get('question_en', eq.get('question', '')).strip().lower()
                if en:
                    norm = "".join(ch for ch in en[:60] if ch.isalnum())
                    existing_en.add(norm)
                    
    dups = []
    for q in processed_qs:
        q_norm = "".join(ch for ch in q['question_en'][:60].lower() if ch.isalnum())
        if q_norm in existing_en:
            dups.append((q['id'], q['question_en'][:50]))
            
    if dups:
        print(f"ERROR: Found {len(dups)} duplicate questions against existing mocks!")
        for d in dups:
            print("Dup:", d)
        sys.exit(1)
        
    print("Zero duplicates verified against all 12 mock tests!")
    
    # 5. Check internal duplicates
    seen_internal = {}
    for q in processed_qs:
        norm = "".join(ch for ch in q['question_en'][:50].lower() if ch.isalnum())
        if norm in seen_internal:
            prev_id = seen_internal[norm]
            print(f"ERROR: Internal duplicate found between Q{prev_id} and Q{q['id']}!")
            print("Stem:", q['question_en'][:60])
            sys.exit(1)
        seen_internal[norm] = q['id']
    print("Zero internal duplicates verified among all 350 questions!")
    
    # 6. Format final JSON bank
    bank_data = {
        "bank_name": "TSPLRB SI Master Aptitude & Reasoning Question Bank (2026 High-Yield PWT)",
        "total_questions": len(processed_qs),
        "arithmetic_questions_count": 175,
        "reasoning_questions_count": 175,
        "version": "1.0.0",
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "description": "Production-grade, fully bilingual (English & Telugu) master question bank covering 100% of the TSPLRB SI Preliminary Written Test (PWT) quantitative aptitude and logical reasoning syllabus with detailed step-by-step mathematical solutions and shortcut tricks.",
        "questions": processed_qs
    }
    
    out_path = 'public/data/master_aptitude_reasoning_bank.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(bank_data, f, indent=2, ensure_ascii=False)
        
    file_size_kb = os.path.getsize(out_path) / 1024
    print(f"Successfully created {out_path} ({file_size_kb:.1f} KB)")
    print(f"Total Questions: {len(processed_qs)}")
    print(f"Arithmetic: Q1 to Q175 (175 questions)")
    print(f"Reasoning: Q176 to Q350 (175 questions)")

if __name__ == '__main__':
    compile_bank()
