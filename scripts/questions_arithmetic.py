#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part A: Arithmetic (Questions 1 to 50)
Covers all 19 TSPLRB SI syllabus topics with complete bilingual English & Telugu.
"""

def get_arithmetic_50():
    items = [
        # 1. Number Systems & Remainder
        {
            "id": 1,
            "qNumber": 1,
            "section": "Arithmetic",
            "topic": "Number Systems & Remainders",
            "question_en": "What is the remainder when (77^77 + 77) is divided by 78?",
            "question_te": "(77^77 + 77) ను 78 చేత భాగించినప్పుడు వచ్చే శేషం ఎంత?",
            "options_en": ["76", "77", "1", "0"],
            "options_te": ["76", "77", "1", "0"],
            "correct_option": 0,
            "explanation_en": "77 ≡ -1 (mod 78). Therefore, (77^77 + 77) ≡ (-1)^77 + (-1) = -1 - 1 = -2 ≡ 76 (mod 78). Hence the remainder is 76.",
            "explanation_te": "77 ≡ -1 (mod 78). కాబట్టి (-1)^77 + (-1) = -2 ≡ 76 (mod 78). సరైన శేషం 76."
        },
        # 2. LCM & Signals
        {
            "id": 2,
            "qNumber": 2,
            "section": "Arithmetic",
            "topic": "HCF and LCM",
            "question_en": "Traffic lights at three junctions change every 48, 72 and 108 seconds respectively. If all change simultaneously at 08:20:00 hours, at what time will they change together next?",
            "question_te": "మూడు వేర్వేరు రోడ్డు క్రాసింగ్‌ల వద్ద ట్రాఫిక్ సిగ్నల్ లైట్లు వరుసగా ప్రతి 48, 72 మరియు 108 సెకన్లకు మారుతాయి. అవన్నీ ఉదయం 08:20:00 గంటలకు కలిసి మారితే, మళ్లీ ఏ సమయానికి ఏకకాలంలో మారుతాయి?",
            "options_en": ["08:27:12 hrs", "08:25:36 hrs", "08:26:12 hrs", "08:28:00 hrs"],
            "options_te": ["08:27:12 గంటలకు", "08:25:36 గంటలకు", "08:26:12 గంటలకు", "08:28:00 గంటలకు"],
            "correct_option": 0,
            "explanation_en": "LCM(48, 72, 108) = 432 seconds = 7 minutes 12 seconds. Adding to 08:20:00 gives 08:27:12 hours.",
            "explanation_te": "48, 72, 108 ల క.సా.గు = 432 సెకన్లు = 7 నిమిషాల 12 సెకన్లు. 08:20:00 కు కలిపితే 08:27:12 గంటలు వస్తుంది."
        },
        # 3. Unit Digit
        {
            "id": 3,
            "qNumber": 3,
            "section": "Arithmetic",
            "topic": "Unit Digit Calculation",
            "question_en": "What is the unit digit of the product (2137^753 * 549^241 * 342^123)?",
            "question_te": "(2137^753 * 549^241 * 342^123) లబ్దంలో ఒకట్ల స్థానంలోని అంకె ఎంత?",
            "options_en": ["6", "8", "4", "2"],
            "options_te": ["6", "8", "4", "2"],
            "correct_option": 2,
            "explanation_en": "Unit digit of 7^753: 753%4=1 => 7^1=7. Unit digit of 9^241: 9^odd = 9. Unit digit of 2^123: 123%4=3 => 2^3=8. Product = 7 * 9 * 8 = 504 => Unit digit is 4.",
            "explanation_te": "7^753 యొక్క ఒకట్ల అంకె: 7. 9^241 యొక్క ఒకట్ల అంకె: 9. 2^123 యొక్క ఒకట్ల అంకె: 8. లబ్దం = 7 * 9 * 8 = 504. ఒకట్ల స్థానంలోని అంకె 4."
        },
        # 4. Trailing Zeros
        {
            "id": 4,
            "qNumber": 4,
            "section": "Arithmetic",
            "topic": "Trailing Zeros in Factorials",
            "question_en": "Find the number of trailing zeros in the value of 100! (factorial 100).",
            "question_te": "100! (100 ఫ్యాక్టోరియల్) విలువలో చివరన ఉండే సున్నాల సంఖ్య ఎంత?",
            "options_en": ["20", "24", "25", "22"],
            "options_te": ["20", "24", "25", "22"],
            "correct_option": 1,
            "explanation_en": "Number of trailing zeros = [100/5] + [100/25] = 20 + 4 = 24 zeros.",
            "explanation_te": "సున్నాల సంఖ్య = [100/5] + [100/25] = 20 + 4 = 24."
        },
        # 5. Recurring Decimal
        {
            "id": 5,
            "qNumber": 5,
            "section": "Arithmetic",
            "topic": "Recurring Decimals to Fractions",
            "question_en": "Express the recurring decimal 0.47̅ (where 7 is recurring) as a rational fraction in simplest form.",
            "question_te": "0.47̅ (7 మాత్రమే పునరావృతమవుతుంది) అనే ఆవర్తన దశాంశాన్ని అకరణీయ భిన్న రూపంలో రాయండి.",
            "options_en": ["43/90", "47/99", "43/99", "47/90"],
            "options_te": ["43/90", "47/99", "43/99", "47/90"],
            "correct_option": 0,
            "explanation_en": "0.47̅ = (47 - 4) / 90 = 43 / 90.",
            "explanation_te": "0.47̅ = (47 - 4) / 90 = 43 / 90."
        },
        # 6. Averages - Replaced Person
        {
            "id": 6,
            "qNumber": 6,
            "section": "Arithmetic",
            "topic": "Averages - Weight Replacement",
            "question_en": "The average weight of 8 persons increases by 2.5 kg when a new person comes in place of one of them weighing 65 kg. What is the weight of the new person?",
            "question_te": "65 కిలోల బరువున్న వ్యక్తి స్థానంలో ఒక కొత్త వ్యక్తి రావడం వల్ల 8 మంది వ్యక్తుల సగటు బరువు 2.5 కిలోలు పెరిగింది. కొత్త వ్యక్తి బరువు ఎంత?",
            "options_en": ["76 kg", "80 kg", "85 kg", "82.5 kg"],
            "options_te": ["76 కిలోలు", "80 కిలోలు", "85 కిలోలు", "82.5 కిలోలు"],
            "correct_option": 2,
            "explanation_en": "Total increase = 8 * 2.5 = 20 kg. Weight of new person = 65 + 20 = 85 kg.",
            "explanation_te": "మొత్తం బరువు పెరుగుదల = 8 * 2.5 = 20 కిలోలు. కొత్త వ్యక్తి బరువు = 65 + 20 = 85 కిలోలు."
        },
        # 7. Averages - Batting
        {
            "id": 7,
            "qNumber": 7,
            "section": "Arithmetic",
            "topic": "Averages - Cricket Batting",
            "question_en": "A batsman makes a score of 87 runs in his 17th innings and thus increases his average by 3 runs. Find his average after the 17th innings.",
            "question_te": "ఒక బ్యాట్స్‌మన్ తన 17వ ఇన్నింగ్స్‌లో 87 పరుగులు చేసి, తద్వారా తన సగటును 3 పరుగులు పెంచుకున్నాడు. 17వ ఇన్నింగ్స్ తర్వాత అతని సగటు ఎంత?",
            "options_en": ["36", "39", "38", "42"],
            "options_te": ["36", "39", "38", "42"],
            "correct_option": 1,
            "explanation_en": "Let old average be A. 16A + 87 = 17(A + 3) => 16A + 87 = 17A + 51 => A = 36. New average = 36 + 3 = 39.",
            "explanation_te": "పాత సగటు A అనుకుంటే: 16A + 87 = 17(A + 3) => A = 36. కొత్త సగటు = 36 + 3 = 39."
        },
        # 8. Percentages - Price and Consumption
        {
            "id": 8,
            "qNumber": 8,
            "section": "Arithmetic",
            "topic": "Percentages & Expenditure",
            "question_en": "If the price of petrol increases by 25%, by what percent must a driver reduce petrol consumption so that monthly fuel expenditure remains unchanged?",
            "question_te": "పెట్రోల్ ధర 25% పెరిగితే, నెలవారీ ఇంధన ఖర్చు మారకుండా ఉండాలంటే ఒక డ్రైవర్ తన పెట్రోల్ వినియోగాన్ని ఎంత శాతం తగ్గించుకోవాలి?",
            "options_en": ["20%", "25%", "16.67%", "15%"],
            "options_te": ["20%", "25%", "16.67%", "15%"],
            "correct_option": 0,
            "explanation_en": "Reduction % = [r / (100 + r)] * 100 = [25 / 125] * 100 = 20%.",
            "explanation_te": "వినియోగ తగ్గింపు = [25 / (100 + 25)] * 100 = 20%."
        },
        # 9. Percentages - Exam Pass Marks
        {
            "id": 9,
            "qNumber": 9,
            "section": "Arithmetic",
            "topic": "Percentages - Pass Criteria",
            "question_en": "A candidate secures 32% marks in an exam and fails by 16 marks. Another candidate secures 44% marks and gets 32 marks more than minimum pass marks. What are the total maximum marks of the exam?",
            "question_te": "ఒక అభ్యర్థి పరీక్షలో 32% మార్కులు సాధించి 16 మార్కులతో ఫెయిల్ అయ్యాడు. మరొక అభ్యర్థి 44% మార్కులు సాధించి ఉత్తీర్ణత మార్కుల కంటే 32 మార్కులు ఎక్కువ పొందాడు. ఆ పరీక్షలోని గరిష్ట మార్కులు ఎంత?",
            "options_en": ["400", "500", "350", "450"],
            "options_te": ["400", "500", "350", "450"],
            "correct_option": 0,
            "explanation_en": "Difference in percentage = 44% - 32% = 12%. Difference in marks = 32 - (-16) = 48 marks. 12% = 48 => 100% = (48/12) * 100 = 400 marks.",
            "explanation_te": "శాతాల తేడా = 12%. మార్కుల తేడా = 48. 12% = 48 అయితే 100% = 400 మార్కులు."
        },
        # 10. Profit & Loss - Successive Discounts
        {
            "id": 10,
            "qNumber": 10,
            "section": "Arithmetic",
            "topic": "Profit & Loss - Successive Discounts",
            "question_en": "An article with marked price ₹2,500 is sold after two successive discounts of 20% and 10%. What is the final selling price?",
            "question_te": "రూ. 2,500 ప్రకటన వెల కలిగిన ఒక వస్తువు వరుసగా 20% మరియు 10% తగ్గింపులతో విక్రయించబడింది. ఆ వస్తువు చివరి అమ్మకపు వెల ఎంత?",
            "options_en": ["₹1,750", "₹1,800", "₹1,850", "₹1,900"],
            "options_te": ["₹1,750", "₹1,800", "₹1,850", "₹1,900"],
            "correct_option": 1,
            "explanation_en": "SP = 2500 * (1 - 0.20) * (1 - 0.10) = 2500 * 0.8 * 0.9 = 2500 * 0.72 = ₹1,800.",
            "explanation_te": "అమ్మకపు వెల = 2500 * 0.8 * 0.9 = రూ. 1,800."
        },
        # 11. Profit & Loss - Same Selling Price
        {
            "id": 11,
            "qNumber": 11,
            "section": "Arithmetic",
            "topic": "Profit & Loss - Equal Selling Price",
            "question_en": "A dealer sells two bikes for ₹48,000 each. On one he gains 20% and on the other he loses 20%. What is his overall gain or loss percentage?",
            "question_te": "ఒక డీలర్ రెండు బైకులను ఒక్కొక్కటి రూ. 48,000 చొప్పున విక్రయించాడు. ఒకదానిపై 20% లాభం, రెండవదానిపై 20% నష్టం వచ్చింది. మొత్తం లావాదేవీలో అతని నికర లాభ లేదా నష్ట శాతం ఎంత?",
            "options_en": ["No profit no loss", "4% loss", "4% gain", "2% loss"],
            "options_te": ["లాభం లేదు నష్టం లేదు", "4% నష్టం", "4% లాభం", "2% నష్టం"],
            "correct_option": 1,
            "explanation_en": "When SP is identical and gain% = loss% = x%, there is always an overall loss of (x/10)^2 % = (20/10)^2 = 4% loss.",
            "explanation_te": "అమ్మకపు వెల సమానమై ఒకదానిపై x% లాభం, మరొకదానిపై x% నష్టం వచ్చినప్పుడు ఎల్లప్పుడూ నష్టమే వస్తుంది. నష్ట శాతం = (x/10)^2 = 4% నష్టం."
        },
        # 12. Profit & Loss - Dishonest Dealer
        {
            "id": 12,
            "qNumber": 12,
            "section": "Arithmetic",
            "topic": "Profit & Loss - Dishonest Trader",
            "question_en": "A dishonest grocer professes to sell his goods at cost price, but uses a false weight of 900 grams instead of a 1 kg weight. What is his actual profit percentage?",
            "question_te": "ఒక వ్యాపారి వస్తువులను కొన్నవెలకే విక్రయిస్తున్నట్లు నమ్మిస్తూ, 1 కిలో తూకానికి బదులుగా 900 గ్రాముల తప్పుడు తూకాన్ని ఉపయోగిస్తున్నాడు. అతని అసలు లాభ శాతం ఎంత?",
            "options_en": ["10%", "11 1/9%", "12.5%", "9 1/11%"],
            "options_te": ["10%", "11 1/9%", "12.5%", "9 1/11%"],
            "correct_option": 1,
            "explanation_en": "Gain % = [Error / (True value - Error)] * 100 = [100 / 900] * 100 = 100 / 9 = 11 1/9%.",
            "explanation_te": "లాభ శాతం = [100 / 900] * 100 = 11 1/9%."
        },
        # 13. Simple Interest - Doubling Rule
        {
            "id": 13,
            "qNumber": 13,
            "section": "Arithmetic",
            "topic": "Simple Interest - Time to Multiply",
            "question_en": "A sum of money invested at simple interest doubles itself in 8 years. In how many years will it become 4 times of itself at the same rate?",
            "question_te": "బారువడ్డీ ప్రకారం ఒక నిర్దిష్ట అసలు మొత్తం 8 సంవత్సరాలలో రెట్టింపు అవుతుంది. అదే వడ్డీ రేటుతో అది 4 రెట్లు కావడానికి ఎన్ని సంవత్సరాలు పడుతుంది?",
            "options_en": ["16 years", "20 years", "24 years", "32 years"],
            "options_te": ["16 సంవత్సరాలు", "20 సంవత్సరాలు", "24 సంవత్సరాలు", "32 సంవత్సరాలు"],
            "correct_option": 2,
            "explanation_en": "At SI: Doubling means interest = 1P in 8 years. Becoming 4 times means interest = 3P. Time required = 3 * 8 = 24 years.",
            "explanation_te": "బారువడ్డీలో అసలు రెట్టింపు కావడానికి 8 సంవత్సరాలలో P వడ్డీ వస్తుంది. 4 రెట్లు కావాలంటే 3P వడ్డీ రావాలి. సమయం = 3 * 8 = 24 సంవత్సరాలు."
        },
        # 14. Compound Interest - Doubling Rule
        {
            "id": 14,
            "qNumber": 14,
            "section": "Arithmetic",
            "topic": "Compound Interest - Exponential Growth",
            "question_en": "A sum of money placed at compound interest doubles itself in 5 years. In how many years will it amount to 8 times of itself at the same compound interest rate?",
            "question_te": "చక్రవడ్డీ ప్రకారం ఒక మొత్తం 5 సంవత్సరాలలో రెట్టింపు అవుతుంది. అదే వడ్డీ రేటుతో అది 8 రెట్లు కావడానికి ఎన్ని సంవత్సరాలు పడుతుంది?",
            "options_en": ["15 years", "20 years", "25 years", "10 years"],
            "options_te": ["15 సంవత్సరాలు", "20 సంవత్సరాలు", "25 సంవత్సరాలు", "10 సంవత్సరాలు"],
            "correct_option": 0,
            "explanation_en": "At CI: 2^1 times in 5 years. 8 times = 2^3 times. Time required = 3 * 5 = 15 years.",
            "explanation_te": "చక్రవడ్డీలో: 2^1 రెట్లు 5 సంవత్సరాలలో. 8 రెట్లు = 2^3 రెట్లు. కాలం = 3 * 5 = 15 సంవత్సరాలు."
        },
        # 15. Difference CI and SI 2 Years
        {
            "id": 15,
            "qNumber": 15,
            "section": "Arithmetic",
            "topic": "CI & SI Difference Formula",
            "question_en": "The difference between simple interest and compound interest on a certain sum for 2 years at 8% per annum is ₹192. What is the principal sum?",
            "question_te": "వార్షిక 8% వడ్డీ రేటుతో 2 సంవత్సరాలకు ఒక మొత్తంపై అయ్యే బారువడ్డీ మరియు చక్రవడ్డీల మధ్య వ్యత్యాసం రూ. 192. ఆ అసలు ఎంత?",
            "options_en": ["₹30,000", "₹25,000", "₹28,000", "₹32,000"],
            "options_te": ["₹30,000", "₹25,000", "₹28,000", "₹32,000"],
            "correct_option": 0,
            "explanation_en": "Diff = P*(r/100)^2 => 192 = P*(8/100)^2 => P = 192 * 10000 / 64 = ₹30,000.",
            "explanation_te": "తేడా = P*(r/100)^2 => P = 192 * 10000 / 64 = రూ. 30,000."
        },
        # 16. CI Half-Yearly
        {
            "id": 16,
            "qNumber": 16,
            "section": "Arithmetic",
            "topic": "Compound Interest - Half Yearly",
            "question_en": "What is the compound interest on ₹10,000 for 1 year at 10% per annum, compounded half-yearly?",
            "question_te": "వార్షిక 10% వడ్డీ రేటుతో రూ. 10,000 పై 1 సంవత్సరానికి అర్ధ వార్షిక చక్రవడ్డీ పద్ధతిలో అయ్యే చక్రవడ్డీ ఎంత?",
            "options_en": ["₹1,000", "₹1,025", "₹1,050", "₹1,100"],
            "options_te": ["₹1,000", "₹1,025", "₹1,050", "₹1,100"],
            "correct_option": 1,
            "explanation_en": "Rate per half-year = 10/2 = 5%. Periods = 2. Amount = 10000 * (1.05)^2 = 10000 * 1.1025 = ₹11,025. CI = 11,025 - 10,000 = ₹1,025.",
            "explanation_te": "అర్ధ వార్షిక రేటు = 5%, కాలాలు = 2. మొత్తం = 10000 * 1.1025 = రూ. 11,025. చక్రవడ్డీ = రూ. 1,025."
        },
        # 17. Ratio Compounding
        {
            "id": 17,
            "qNumber": 17,
            "section": "Arithmetic",
            "topic": "Compounded Ratios",
            "question_en": "If A : B = 2 : 3, B : C = 4 : 5, and C : D = 6 : 7, what is the ratio of A : D?",
            "question_te": "A : B = 2 : 3, B : C = 4 : 5 మరియు C : D = 6 : 7 అయితే, A : D నిష్పత్తి ఎంత?",
            "options_en": ["16 : 35", "8 : 35", "12 : 35", "24 : 35"],
            "options_te": ["16 : 35", "8 : 35", "12 : 35", "24 : 35"],
            "correct_option": 0,
            "explanation_en": "A/D = (A/B) * (B/C) * (C/D) = (2/3) * (4/5) * (6/7) = (2 * 4 * 2) / (1 * 5 * 7) = 16 / 35.",
            "explanation_te": "A/D = (2/3) * (4/5) * (6/7) = 16 / 35."
        },
        # 18. Coins Ratio
        {
            "id": 18,
            "qNumber": 18,
            "section": "Arithmetic",
            "topic": "Ratio and Proportion - Coins",
            "question_en": "A bag contains ₹1, 50 paise and 25 paise coins in ratio 5 : 6 : 8. If total value is ₹240, find the number of 25 paise coins.",
            "question_te": "ఒక సంచిలో రూ. 1, 50 పైసలు మరియు 25 పైసల నాణేలు 5 : 6 : 8 నిష్పత్తిలో ఉన్నాయి. మొత్తం విలువ రూ. 240 అయితే, 25 పైసల నాణేల సంఖ్య ఎంత?",
            "options_en": ["192", "240", "160", "200"],
            "options_te": ["192", "240", "160", "200"],
            "correct_option": 0,
            "explanation_en": "Value per ratio unit = 5*(1) + 6*(0.5) + 8*(0.25) = 5 + 3 + 2 = ₹10. Units = 240/10 = 24. Number of 25p coins = 8 * 24 = 192.",
            "explanation_te": "ఒక యూనిట్ విలువ = 5 + 3 + 2 = రూ. 10. యూనిట్లు = 24. 25 పైసల నాణేలు = 8 * 24 = 192."
        },
        # 19. Ages
        {
            "id": 19,
            "qNumber": 19,
            "section": "Arithmetic",
            "topic": "Problems on Ages",
            "question_en": "Five years ago, the ratio of the ages of a father and his son was 7 : 2. Five years hence, the ratio of their ages will be 9 : 4. What is the current age of the father?",
            "question_te": "ఐదు సంవత్సరాల క్రితం తండ్రి మరియు కొడుకుల వయస్సుల నిష్పత్తి 7 : 2. ఐదేళ్ల తర్వాత వారి వయస్సుల నిష్పత్తి 9 : 4 అవుతుంది. ప్రస్తుతం తండ్రి వయస్సు ఎంత?",
            "options_en": ["40 years", "45 years", "35 years", "50 years"],
            "options_te": ["40 సంవత్సరాలు", "45 సంవత్సరాలు", "35 సంవత్సరాలు", "50 సంవత్సరాలు"],
            "correct_option": 0,
            "explanation_en": "Difference in ratio units between 5 yrs ago and 5 yrs hence (10 yrs gap) = 9 - 7 = 2 units, and 4 - 2 = 2 units. 2 units = 10 years => 1 unit = 5 years. Father's age 5 yrs ago = 7 * 5 = 35 years. Present age = 35 + 5 = 40 years.",
            "explanation_te": "10 సంవత్సరాల తేడాకు 2 యూనిట్లు = 10 ఏళ్లు => 1 యూనిట్ = 5 ఏళ్లు. 5 ఏళ్ల క్రితం తండ్రి వయస్సు = 35. ప్రస్తుత వయస్సు = 40 సంవత్సరాలు."
        },
        # 20. Time and Work - A, B, C Cyclical
        {
            "id": 20,
            "qNumber": 20,
            "section": "Arithmetic",
            "topic": "Time & Work - Pair Efficiencies",
            "question_en": "A and B can do a work in 10 days, B and C in 12 days, and C and A in 15 days. In how many days can A, B, and C together complete the entire work?",
            "question_te": "A మరియు B లు ఒక పనిని 10 రోజుల్లో, B మరియు C లు 12 రోజుల్లో, C మరియు A లు 15 రోజుల్లో పూర్తి చేయగలరు. ముగ్గురూ కలిసి ఆ పనిని ఎన్ని రోజుల్లో పూర్తి చేయగలరు?",
            "options_en": ["8 days", "6 days", "7.5 days", "9 days"],
            "options_te": ["8 రోజులు", "6 రోజులు", "7.5 రోజులు", "9 రోజులు"],
            "correct_option": 0,
            "explanation_en": "LCM(10, 12, 15) = 60 units. (A+B) = 6, (B+C) = 5, (C+A) = 4. Adding: 2(A+B+C) = 15 => (A+B+C) = 7.5 units/day. Time required = 60 / 7.5 = 8 days.",
            "explanation_te": "మొత్తం పని = 60 యూనిట్లు. 2(A+B+C) = 15 => A+B+C = 7.5 యూనిట్లు/రోజు. కాలం = 60 / 7.5 = 8 రోజులు."
        },
        # 21. Time and Work - Men or Women
        {
            "id": 21,
            "qNumber": 21,
            "section": "Arithmetic",
            "topic": "Time and Work - Men vs Women",
            "question_en": "12 men or 18 women can harvest a field in 14 days. In how many days can 8 men and 16 women together harvest the same field?",
            "question_te": "12 మంది పురుషులు లేదా 18 మంది స్త్రీలు ఒక పొలాన్ని 14 రోజుల్లో కోయగలరు. 8 మంది పురుషులు మరియు 16 మంది స్త్రీలు కలిసి అదే పొలాన్ని ఎన్ని రోజుల్లో కోయగలరు?",
            "options_en": ["9 days", "10 days", "8 days", "12 days"],
            "options_te": ["9 రోజులు", "10 రోజులు", "8 రోజులు", "12 రోజులు"],
            "correct_option": 0,
            "explanation_en": "12M = 18W => 1M = 1.5W. Total work = 18W * 14 = 252 woman-days. Required group: 8M + 16W = 8*(1.5) + 16 = 12 + 16 = 28 women. Time = 252 / 28 = 9 days.",
            "explanation_te": "12 పురుషులు = 18 స్త్రీలు => 1 పురుషుడు = 1.5 స్త్రీలు. మొత్తం పని = 18 * 14 = 252 స్త్రీ-రోజులు. బృందం = 8(1.5) + 16 = 28 స్త్రీలు. సమయం = 252 / 28 = 9 రోజులు."
        },
        # 22. Time and Work - Alternate Days
        {
            "id": 22,
            "qNumber": 22,
            "section": "Arithmetic",
            "topic": "Time & Work - Alternate Days",
            "question_en": "A can complete a work in 12 days and B can complete it in 18 days. If they work on alternate days starting with A, in how many days will the work finish?",
            "question_te": "A ఒక పనిని 12 రోజుల్లో, B అదే పనిని 18 రోజుల్లో చేస్తారు. మొదటి రోజు A తో ప్రారంభించి రోజు విడిచి రోజు పనిచేస్తే, ఆ పని ఎన్ని రోజుల్లో పూర్తవుతుంది?",
            "options_en": ["14 1/3 days", "14 1/2 days", "15 days", "13 2/3 days"],
            "options_te": ["14 1/3 రోజులు", "14 1/2 రోజులు", "15 రోజులు", "13 2/3 రోజులు"],
            "correct_option": 0,
            "explanation_en": "Work = 36 units. A = 3, B = 2. In 2 days = 5 units. In 14 days = 35 units. 1 unit remains, done by A in 1/3 day. Total = 14 1/3 days.",
            "explanation_te": "పని = 36 యూనిట్లు. 14 రోజుల్లో 35 యూనిట్లు పూర్తవుతాయి. మిగిలిన 1 యూనిట్‌ను A 1/3 రోజులో చేస్తాడు. మొత్తం = 14 1/3 రోజులు."
        },
        # 23. Pipes and Cisterns - Filling and Emptying
        {
            "id": 23,
            "qNumber": 23,
            "section": "Arithmetic",
            "topic": "Pipes and Cisterns",
            "question_en": "Pipe A can fill a tank in 16 hours and Pipe B can empty it in 24 hours. When both pipes are opened simultaneously in an empty tank, how long will it take to fill completely?",
            "question_te": "పైప్ A ట్యాంకును 16 గంటల్లో నింపగలదు, పైప్ B 24 గంటల్లో ఖాళీ చేయగలదు. రెండు పైపులను ఏకకాలంలో తెరిస్తే ట్యాంక్ నిండటానికి ఎన్ని గంటలు పడుతుంది?",
            "options_en": ["40 hours", "48 hours", "36 hours", "32 hours"],
            "options_te": ["40 గంటలు", "48 గంటలు", "36 గంటలు", "32 గంటలు"],
            "correct_option": 1,
            "explanation_en": "Net rate = (1/16) - (1/24) = (3 - 2)/48 = 1/48 tank per hour. Total time = 48 hours.",
            "explanation_te": "నికర రేటు = 1/16 - 1/24 = 1/48. పట్టే సమయం = 48 గంటలు."
        },
        # 24. Pipes - Leak in Cistern
        {
            "id": 24,
            "qNumber": 24,
            "section": "Arithmetic",
            "topic": "Pipes - Tank with Leak",
            "question_en": "A pump can fill a water tank in 2 hours. Because of a leak at the bottom, it takes 2 1/3 hours to fill the tank. In how many hours can the leak alone empty the full tank?",
            "question_te": "ఒక పంపు నీటి ట్యాంకును 2 గంటల్లో నింపగలదు. అడుగున ఉన్న లీకేజీ కారణంగా ట్యాంక్ నిండటానికి 2 1/3 గంటలు పట్టింది. ఆ లీకేజీ మాత్రమే పూర్తి ట్యాంకును ఎన్ని గంటల్లో ఖాళీ చేస్తుంది?",
            "options_en": ["14 hours", "12 hours", "16 hours", "10 hours"],
            "options_te": ["14 గంటలు", "12 గంటలు", "16 గంటలు", "10 గంటలు"],
            "correct_option": 0,
            "explanation_en": "Leak rate = (1/2) - (1 / (7/3)) = (1/2) - (3/7) = (7 - 6)/14 = 1/14 per hour. Time to empty = 14 hours.",
            "explanation_te": "లీకేజీ రేటు = 1/2 - 3/7 = 1/14. ఖాళీ చేయడానికి పట్టే సమయం = 14 గంటలు."
        },
        # 25. Time Speed Distance - Fractional Speed
        {
            "id": 25,
            "qNumber": 25,
            "section": "Arithmetic",
            "topic": "Time Speed & Distance - Late Arrival",
            "question_en": "Walking at 3/4th of his normal speed, a person reaches his office 20 minutes late. What is his usual time to reach the office?",
            "question_te": "ఒక వ్యక్తి తన సాధారణ వేగంలో 3/4 వంతు వేగంతో నడిస్తే ఆఫీసుకు 20 నిమిషాలు ఆలస్యంగా చేరుకుంటాడు. అతని సాధారణ ప్రయాణ సమయం ఎంత?",
            "options_en": ["50 mins", "60 mins", "80 mins", "75 mins"],
            "options_te": ["50 నిమిషాలు", "60 నిమిషాలు", "80 నిమిషాలు", "75 నిమిషాలు"],
            "correct_option": 1,
            "explanation_en": "Time becomes 4/3 of T. Extra time = (4/3 - 1)T = T/3 = 20 mins => T = 60 minutes.",
            "explanation_te": "సమయం 4/3T అవుతుంది. అదనపు సమయం T/3 = 20 నిమిషాలు => T = 60 నిమిషాలు."
        },
        # 26. Trains - Platform
        {
            "id": 26,
            "qNumber": 26,
            "section": "Arithmetic",
            "topic": "Problems on Trains - Platform Crossing",
            "question_en": "A 240 m long train moving at 72 km/h crosses a platform in 25 seconds. What is the length of the platform?",
            "question_te": "గంటకు 72 కిమీ వేగంతో వెళ్తున్న 240 మీటర్ల పొడవున్న రైలు ఒక ప్లాట్‌ఫారమ్‌ను 25 సెకన్లలో దాటుతుంది. ఆ ప్లాట్‌ఫారమ్ పొడవు ఎంత?",
            "options_en": ["260 m", "240 m", "300 m", "280 m"],
            "options_te": ["260 మీటర్లు", "240 మీటర్లు", "300 మీటర్లు", "280 మీటర్లు"],
            "correct_option": 0,
            "explanation_en": "Speed = 72 * 5/18 = 20 m/s. Distance = 20 * 25 = 500 m. Platform length = 500 - 240 = 260 m.",
            "explanation_te": "వేగం = 20 మీ/సె. దూరం = 500 మీ. ప్లాట్‌ఫారమ్ పొడవు = 500 - 240 = 260 మీటర్లు."
        },
        # 27. Trains - Opposite Directions
        {
            "id": 27,
            "qNumber": 27,
            "section": "Arithmetic",
            "topic": "Trains - Opposite Direction Crossing",
            "question_en": "Two trains 140 m and 160 m long are running towards each other on parallel lines at speeds of 60 km/h and 48 km/h. In how many seconds will they cross each other completely?",
            "question_te": "140 మీ మరియు 160 మీ పొడవు గల రెండు రైళ్లు సమాంతర పట్టాలపై ఎదురెదురుగా గంటకు 60 కిమీ మరియు 48 కిమీ వేగంతో వస్తున్నాయి. అవి ఒకదానినొకటి పూర్తిగా దాటడానికి ఎన్ని సెకన్లు పడుతుంది?",
            "options_en": ["10 seconds", "12 seconds", "9 seconds", "15 seconds"],
            "options_te": ["10 సెకన్లు", "12 సెకన్లు", "9 సెకన్లు", "15 సెకన్లు"],
            "correct_option": 0,
            "explanation_en": "Total distance = 140 + 160 = 300 m. Relative speed = 60 + 48 = 108 km/h = 108 * (5/18) = 30 m/s. Time = 300 / 30 = 10 seconds.",
            "explanation_te": "దూరం = 300 మీ. సాపేక్ష వేగం = 108 కిమీ/గం = 30 మీ/సె. సమయం = 300 / 30 = 10 సెకన్లు."
        },
        # 28. Boats and Streams
        {
            "id": 28,
            "qNumber": 28,
            "section": "Arithmetic",
            "topic": "Boats and Streams",
            "question_en": "A boat travels 36 km downstream in 3 hours and 24 km upstream in 4 hours. What is the speed of the river current?",
            "question_te": "ఒక పడవ ప్రవాహ దిశలో 36 కిమీ దూరాన్ని 3 గంటల్లో, ఎదురు దిశలో 24 కిమీ దూరాన్ని 4 గంటల్లో ప్రయాణిస్తుంది. ప్రవాహ వేగం ఎంత?",
            "options_en": ["3 km/h", "2.5 km/h", "4 km/h", "2 km/h"],
            "options_te": ["గంటకు 3 కిమీ", "గంటకు 2.5 కిమీ", "గంటకు 4 కిమీ", "గంటకు 2 కిమీ"],
            "correct_option": 0,
            "explanation_en": "Downstream speed = 36/3 = 12 km/h. Upstream speed = 24/4 = 6 km/h. Current speed = (12 - 6)/2 = 3 km/h.",
            "explanation_te": "ప్రవాహ దిశలో వేగం = 12 కిమీ/గం, ఎదురు వేగం = 6 కిమీ/గం. ప్రవాహ వేగం = (12 - 6)/2 = 3 కిమీ/గం."
        },
        # 29. Alligation & Mixtures
        {
            "id": 29,
            "qNumber": 29,
            "section": "Arithmetic",
            "topic": "Alligation and Mixtures",
            "question_en": "In what ratio must rice at ₹48/kg be mixed with rice at ₹60/kg so that selling the mixture at ₹62.70/kg yields 10% profit?",
            "question_te": "కిలో రూ. 48 గల బియ్యాన్ని కిలో రూ. 60 గల బియ్యంతో ఏ నిష్పత్తిలో కలిపి, ఆ మిశ్రమాన్ని కిలో రూ. 62.70 కు విక్రయిస్తే 10% లాభం వస్తుంది?",
            "options_en": ["1 : 3", "2 : 3", "3 : 4", "1 : 2"],
            "options_te": ["1 : 3", "2 : 3", "3 : 4", "1 : 2"],
            "correct_option": 0,
            "explanation_en": "CP of mixture = 62.70 / 1.10 = ₹57/kg. Ratio = (60 - 57) : (57 - 48) = 3 : 9 = 1 : 3.",
            "explanation_te": "మిశ్రమం కొన్నవెల = రూ. 57. నిష్పత్తి = (60 - 57) : (57 - 48) = 1 : 3."
        },
        # 30. Mixtures - Milk and Water
        {
            "id": 30,
            "qNumber": 30,
            "section": "Arithmetic",
            "topic": "Mixtures - Adding Water",
            "question_en": "A 45-litre mixture contains milk and water in the ratio 7 : 2. How much water must be added to make the ratio of milk to water 7 : 3?",
            "question_te": "45 లీటర్ల మిశ్రమంలో పాలు మరియు నీళ్లు 7 : 2 నిష్పత్తిలో ఉన్నాయి. పాలు మరియు నీళ్ల నిష్పత్తి 7 : 3 కావడానికి ఎన్ని లీటర్ల నీటిని కలపాలి?",
            "options_en": ["5 litres", "6 litres", "4 litres", "7.5 litres"],
            "options_te": ["5 లీటర్లు", "6 లీటర్లు", "4 లీటర్లు", "7.5 లీటర్లు"],
            "correct_option": 0,
            "explanation_en": "Total parts = 7 + 2 = 9 parts = 45 L => 1 part = 5 L. Milk = 35 L, Water = 10 L. For 7:3 ratio with 35 L milk, water needed = 3 parts = 15 L. Water to add = 15 - 10 = 5 litres.",
            "explanation_te": "1 భాగం = 5 లీటర్లు. పాలు = 35 లీ, నీళ్లు = 10 లీ. 7:3 నిష్పత్తికి నీళ్లు 15 లీటర్లు కావాలి. కలపాల్సిన నీరు = 15 - 10 = 5 లీటర్లు."
        },
        # 31. Partnership - Equal Profit
        {
            "id": 31,
            "qNumber": 31,
            "section": "Arithmetic",
            "topic": "Partnership - Profit Sharing",
            "question_en": "A invests ₹40,000 for 12 months, B invests ₹60,000 for 8 months and C invests ₹80,000 for 6 months. In an annual profit of ₹36,000, what is B's share?",
            "question_te": "A రూ. 40,000 ను 12 నెలలు, B రూ. 60,000 ను 8 నెలలు, C రూ. 80,000 ను 6 నెలలు పెట్టుబడిగా పెట్టారు. వార్షిక లాభం రూ. 36,000 లో B వాటా ఎంత?",
            "options_en": ["₹12,000", "₹14,000", "₹10,000", "₹16,000"],
            "options_te": ["₹12,000", "₹14,000", "₹10,000", "₹16,000"],
            "correct_option": 0,
            "explanation_en": "Ratio = (40*12) : (60*8) : (80*6) = 480 : 480 : 480 = 1 : 1 : 1. B's share = 36000 / 3 = ₹12,000.",
            "explanation_te": "నిష్పత్తి = 1 : 1 : 1. B వాటా = 36000 / 3 = రూ. 12,000."
        },
        # 32. Mensuration 2D - Wire Square to Circle
        {
            "id": 32,
            "qNumber": 32,
            "section": "Arithmetic",
            "topic": "Mensuration 2D - Perimeter and Area",
            "question_en": "A wire when bent in the shape of a square encloses 484 cm². If the same wire is bent into a circle, what is the enclosed area (π = 22/7)?",
            "question_te": "ఒక తీగను చతురస్రాకారంలో వంచినప్పుడు అది 484 చ.సెం.మీ వైశాల్యాన్ని ఆక్రమిస్తుంది. అదే తీగను వృత్తాకారంలో వంచితే ఆ వృత్త వైశాల్యం ఎంత?",
            "options_en": ["616 cm²", "628 cm²", "594 cm²", "642 cm²"],
            "options_te": ["616 చ.సెం.మీ", "628 చ.సెం.మీ", "594 చ.సెం.మీ", "642 చ.సెం.మీ"],
            "correct_option": 0,
            "explanation_en": "Side a = √484 = 22 cm. Perimeter = 4 * 22 = 88 cm. 2πr = 88 => r = 14 cm. Area = π * r^2 = (22/7)*14*14 = 616 cm².",
            "explanation_te": "చతురస్రం భుజం = 22 సెం.మీ, చుట్టుకొలత = 88 సెం.మీ. వృత్త వ్యాసార్థం r = 14 సెం.మీ. వైశాల్యం = 616 చ.సెం.మీ."
        },
        # 33. Mensuration 2D - Equilateral Triangle
        {
            "id": 33,
            "qNumber": 33,
            "section": "Arithmetic",
            "topic": "Mensuration 2D - Equilateral Triangle",
            "question_en": "What is the area of an equilateral triangle each of whose sides measures 12 cm?",
            "question_te": "ప్రతి భుజం 12 సెం.మీ కొలత కలిగిన సమబాహు త్రిభుజం వైశాల్యం ఎంత?",
            "options_en": ["36√3 cm²", "24√3 cm²", "48√3 cm²", "72 cm²"],
            "options_te": ["36√3 చ.సెం.మీ", "24√3 చ.సెం.మీ", "48√3 చ.సెం.మీ", "72 చ.సెం.మీ"],
            "correct_option": 0,
            "explanation_en": "Area = (√3 / 4) * a^2 = (√3 / 4) * 144 = 36√3 cm².",
            "explanation_te": "వైశాల్యం = (√3 / 4) * a^2 = 36√3 చ.సెం.మీ."
        },
        # 34. Mensuration 2D - Rhombus
        {
            "id": 34,
            "qNumber": 34,
            "section": "Arithmetic",
            "topic": "Mensuration 2D - Rhombus Perimeter",
            "question_en": "The diagonals of a rhombus are 16 cm and 12 cm. What is the perimeter of the rhombus?",
            "question_te": "ఒక రాంబస్ యొక్క కర్ణాలు 16 సెం.మీ మరియు 12 సెం.మీ. ఆ రాంబస్ చుట్టుకొలత ఎంత?",
            "options_en": ["40 cm", "36 cm", "48 cm", "56 cm"],
            "options_te": ["40 సెం.మీ", "36 సెం.మీ", "48 సెం.మీ", "56 సెం.మీ"],
            "correct_option": 0,
            "explanation_en": "Half-diagonals are 8 cm and 6 cm. Side = √(8^2 + 6^2) = √(64 + 36) = √100 = 10 cm. Perimeter = 4 * 10 = 40 cm.",
            "explanation_te": "సగం కర్ణాలు 8 మరియు 6 సెం.మీ. భుజం = √(8^2 + 6^2) = 10 సెం.మీ. చుట్టుకొలత = 4 * 10 = 40 సెం.మీ."
        },
        # 35. Mensuration 3D - Melting Cylinder into Spheres
        {
            "id": 35,
            "qNumber": 35,
            "section": "Arithmetic",
            "topic": "Mensuration 3D - Recasting",
            "question_en": "A metallic cylinder of radius 6 cm and height 36 cm is melted into solid spheres of radius 3 cm each. How many such spheres can be formed?",
            "question_te": "వ్యాసార్థం 6 సెం.మీ మరియు ఎత్తు 36 సెం.మీ కలిగిన లోహపు స్థూపాన్ని కరిగించి 3 సెం.మీ వ్యాసార్థం గల ఘన గోళాలుగా మార్చితే, ఎన్ని గోళాలు ఏర్పడతాయి?",
            "options_en": ["36", "48", "32", "24"],
            "options_te": ["36", "48", "32", "24"],
            "correct_option": 0,
            "explanation_en": "Volume cylinder = π * 6^2 * 36 = 1296π. Volume sphere = (4/3)π * 3^3 = 36π. Number of spheres = 1296 / 36 = 36.",
            "explanation_te": "స్థూపం ఘనపరిమాణం = 1296π. గోళం ఘనపరిమాణం = 36π. గోళాల సంఖ్య = 36."
        },
        # 36. Mensuration 3D - Diagonal of Cuboid
        {
            "id": 36,
            "qNumber": 36,
            "section": "Arithmetic",
            "topic": "Mensuration 3D - Cuboid Diagonal",
            "question_en": "Find the length of the longest rod that can be placed in a room of dimensions 12 m long, 9 m broad and 8 m high.",
            "question_te": "12 మీ పొడవు, 9 మీ వెడల్పు మరియు 8 మీ ఎత్తు గల ఒక గదిలో ఉంచగల అత్యంత పొడవైన కర్ర పొడవు ఎంత?",
            "options_en": ["17 m", "15 m", "19 m", "20 m"],
            "options_te": ["17 మీటర్లు", "15 మీటర్లు", "19 మీటర్లు", "20 మీటర్లు"],
            "correct_option": 0,
            "explanation_en": "Diagonal = √(l^2 + b^2 + h^2) = √(144 + 81 + 64) = √289 = 17 m.",
            "explanation_te": "కర్ణం = √(144 + 81 + 64) = √289 = 17 మీటర్లు."
        },
        # 37. Permutations - Vowels Together
        {
            "id": 37,
            "qNumber": 37,
            "section": "Arithmetic",
            "topic": "Permutations & Combinations",
            "question_en": "In how many distinct ways can the letters of the word 'POLICE' be arranged such that all vowels always remain together?",
            "question_te": "'POLICE' అనే పదంలోని అక్షరాలను, అచ్చులన్నీ ఎల్లప్పుడూ కలిసి ఉండేలా ఎన్ని రకాలుగా అమర్చవచ్చు?",
            "options_en": ["144", "120", "240", "720"],
            "options_te": ["144", "120", "240", "720"],
            "correct_option": 0,
            "explanation_en": "Letters = 6 (Vowels O, I, E = 3; Consonants P, L, C = 3). Total units = 3 + 1 = 4 => 4! = 24. Vowels arrange in 3! = 6. Total = 24 * 6 = 144.",
            "explanation_te": "మొత్తం యూనిట్లు = 4 => 4! = 24. అచ్చులు తమలో తాము = 3! = 6. మొత్తం = 24 * 6 = 144."
        },
        # 38. Combinations - Committee Formation
        {
            "id": 38,
            "qNumber": 38,
            "section": "Arithmetic",
            "topic": "Combinations - Committee Selection",
            "question_en": "From a group of 7 men and 6 women, in how many ways can a committee of 5 persons be formed consisting of at least 3 men?",
            "question_te": "7 గురు పురుషులు మరియు 6 గురు స్త్రీలు ఉన్న ఒక సమూహం నుండి కనీసం 3 గురు పురుషులు ఉండేలా 5 గురితో ఒక కమిటీని ఎన్ని రకాలుగా ఏర్పాటు చేయవచ్చు?",
            "options_en": ["756", "720", "680", "840"],
            "options_te": ["756", "720", "680", "840"],
            "correct_option": 0,
            "explanation_en": "Cases: (3M, 2W) + (4M, 1W) + (5M, 0W) = 7C3*6C2 + 7C4*6C1 + 7C5*6C0 = 35*15 + 35*6 + 21*1 = 525 + 210 + 21 = 756 ways.",
            "explanation_te": "(3 పురుషులు, 2 స్త్రీలు) + (4 పురుషులు, 1 స్త్రీ) + (5 పురుషులు, 0 స్త్రీలు) = 525 + 210 + 21 = 756 రకాలు."
        },
        # 39. Probability - Drawing Kings
        {
            "id": 39,
            "qNumber": 39,
            "section": "Arithmetic",
            "topic": "Probability - Cards Without Replacement",
            "question_en": "Two cards are drawn at random without replacement from a pack of 52 playing cards. What is the probability that both cards are Kings?",
            "question_te": "52 పేక ముక్కల కట్ట నుండి తిరిగి ఉంచకుండా రెండు కార్డులను తీస్తే, ఆ రెండు కూడా రాజులు (Kings) అయ్యే సంభావ్యత ఎంత?",
            "options_en": ["1 / 221", "1 / 169", "2 / 221", "1 / 26"],
            "options_te": ["1 / 221", "1 / 169", "2 / 221", "1 / 26"],
            "correct_option": 0,
            "explanation_en": "Probability = (4/52) * (3/51) = (1/13) * (1/17) = 1 / 221.",
            "explanation_te": "సంభావ్యత = (4/52) * (3/51) = 1 / 221."
        },
        # 40. Probability - Two Dice Sum
        {
            "id": 40,
            "qNumber": 40,
            "section": "Arithmetic",
            "topic": "Probability - Pair of Dice",
            "question_en": "Two standard unbiased dice are thrown simultaneously. What is the probability that the sum of the numbers appearing on top is 8?",
            "question_te": "రెండు పాచికలను ఒకేసారి దొర్లించినప్పుడు వాటిపై కనిపించే సంఖ్యల మొత్తం 8 అయ్యే సంభావ్యత ఎంత?",
            "options_en": ["5 / 36", "1 / 6", "7 / 36", "1 / 9"],
            "options_te": ["5 / 36", "1 / 6", "7 / 36", "1 / 9"],
            "correct_option": 0,
            "explanation_en": "Favorable outcomes for sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) = 5 outcomes. Total possible outcomes = 36. Probability = 5/36.",
            "explanation_te": "మొత్తం 8 వచ్చే జతలు: (2,6), (3,5), (4,4), (5,3), (6,2) = 5. మొత్తం అవకాశాలు = 36. సంభావ్యత = 5/36."
        },
        # 41. DI - Table 1
        {
            "id": 41,
            "qNumber": 41,
            "section": "Arithmetic",
            "topic": "Data Interpretation - District Police Recruitment",
            "question_en": "The total sales of a police recruitment prep book across 5 Telangana districts is 45,000 copies. If Warangal accounts for 24% and Karimnagar accounts for 18%, what is the difference in sales between Warangal and Karimnagar?",
            "question_te": "తెలంగాణలోని 5 జిల్లాలలో పోలీస్ రిక్రూట్‌మెంట్ పుస్తకం మొత్తం అమ్మకాలు 45,000 కాపీలు. వరంగల్ వాటా 24%, కరీంనగర్ వాటా 18% అయితే, ఆ రెండు జిల్లాల అమ్మకాల మధ్య వ్యత్యాసం ఎంత?",
            "options_en": ["2,700", "3,150", "2,400", "2,250"],
            "options_te": ["2,700", "3,150", "2,400", "2,250"],
            "correct_option": 0,
            "explanation_en": "Difference in percentage = 24% - 18% = 6%. Difference in copies = 6% of 45,000 = 0.06 * 45000 = 2,700 copies.",
            "explanation_te": "శాతాల తేడా = 6%. కాపీల తేడా = 45000 లో 6% = 2,700 కాపీలు."
        },
        # 42. DI - Bar Graph
        {
            "id": 42,
            "qNumber": 42,
            "section": "Arithmetic",
            "topic": "Data Interpretation - Growth Calculation",
            "question_en": "A security training academy trained 400 candidates in 2022, 520 candidates in 2023, and 650 candidates in 2024. What is the percentage increase in trained candidates from 2022 to 2024?",
            "question_te": "ఒక సెక్యూరిటీ అకాడమీ 2022లో 400 మంది, 2023లో 520 మంది, 2024లో 650 మంది అభ్యర్థులకు శిక్షణ ఇచ్చింది. 2022 నుండి 2024 నాటికి శిక్షణ పొందిన అభ్యర్థుల సంఖ్యలో పెరుగుదల శాతం ఎంత?",
            "options_en": ["62.5%", "60%", "55%", "65%"],
            "options_te": ["62.5%", "60%", "55%", "65%"],
            "correct_option": 0,
            "explanation_en": "Increase = 650 - 400 = 250. Percentage increase = (250 / 400) * 100 = 62.5%.",
            "explanation_te": "పెరుగుదల = 250. పెరుగుదల శాతం = (250 / 400) * 100 = 62.5%."
        },
        # 43. Divisibility Rule of 11
        {
            "id": 43,
            "qNumber": 43,
            "section": "Arithmetic",
            "topic": "Divisibility Rules - 11",
            "question_en": "If the 7-digit number 5432*71 is completely divisible by 11, what single digit must replace the asterisk (*) ?",
            "question_te": "5432*71 అనే 7 అంకెల సంఖ్య 11 చేత నిశ్శేషంగా భాగించబడితే, నక్షత్రం (*) స్థానంలో ఉండాల్సిన అంకె ఏది?",
            "options_en": ["6", "1", "3", "5"],
            "options_te": ["6", "1", "3", "5"],
            "correct_option": 0,
            "explanation_en": "Sum of odd-place digits (from right): 1 + * + 3 + 5 = 9 + *. Sum of even-place digits: 7 + 2 + 4 = 13. Difference = (9 + *) - 13 = * - 4. For divisibility by 11, * - 4 = 0 or 11 => * = 4? Wait: odd positions from right: 1st=1, 3rd=*, 5th=3, 7th=5 => sum=9+*. Even positions: 2nd=7, 4th=2, 6th=4 => sum=13. If * = 4, 13 - 13 = 0. Let's make options [4, 6, 2, 8] with correct 4.",
            "options_en": ["4", "6", "2", "8"],
            "options_te": ["4", "6", "2", "8"],
            "correct_option": 0,
            "explanation_en": "Odd-place sum = 1 + * + 3 + 5 = 9 + *. Even-place sum = 7 + 2 + 4 = 13. Difference = 13 - (9 + *) = 4 - * = 0 => * = 4.",
            "explanation_te": "బేసి స్థానాల మొత్తం = 9 + *. సరి స్థానాల మొత్తం = 13. తేడా సున్నా కావాలంటే * = 4 కావాలి."
        },
        # 44. Simplification - Surds
        {
            "id": 44,
            "qNumber": 44,
            "section": "Arithmetic",
            "topic": "Simplification - Surds",
            "question_en": "What is the value of: √(72 + √(72 + √(72 + ... ∞))) ?",
            "question_te": "√(72 + √(72 + √(72 + ... ∞))) యొక్క విలువ ఎంత?",
            "options_en": ["9", "8", "12", "72"],
            "options_te": ["9", "8", "12", "72"],
            "correct_option": 0,
            "explanation_en": "For √(n(n+1) + ...), result is (n+1). Since 72 = 8 * 9, the answer is the larger consecutive factor, which is 9.",
            "explanation_te": "72 = 8 * 9 (వరుస సంఖ్యల లబ్దం). ప్లస్ (+) గుర్తు ఉన్నప్పుడు పెద్ద సంఖ్య 9 సమాధానం అవుతుంది."
        },
        # 45. Ratio - Third Proportional
        {
            "id": 45,
            "qNumber": 45,
            "section": "Arithmetic",
            "topic": "Proportions - Third Proportional",
            "question_en": "What is the third proportional to 16 and 24?",
            "question_te": "16 మరియు 24 ల తృతీయ అనుపాతం ఎంత?",
            "options_en": ["36", "32", "40", "48"],
            "options_te": ["36", "32", "40", "48"],
            "correct_option": 0,
            "explanation_en": "Third proportional to a and b = b^2 / a = 24^2 / 16 = 576 / 16 = 36.",
            "explanation_te": "తృతీయ అనుపాతం = b^2 / a = (24 * 24) / 16 = 36."
        },
        # 46. Ratio - Mean Proportional
        {
            "id": 46,
            "qNumber": 46,
            "section": "Arithmetic",
            "topic": "Proportions - Mean Proportional",
            "question_en": "What is the mean proportional between 0.08 and 0.18?",
            "question_te": "0.08 మరియు 0.18 ల మధ్యమ అనుపాతం ఎంత?",
            "options_en": ["0.12", "0.14", "0.16", "0.09"],
            "options_te": ["0.12", "0.14", "0.16", "0.09"],
            "correct_option": 0,
            "explanation_en": "Mean proportional = √(0.08 * 0.18) = √0.0144 = 0.12.",
            "explanation_te": "మధ్యమ అనుపాతం = √(0.08 * 0.18) = √0.0144 = 0.12."
        },
        # 47. Circular Track
        {
            "id": 47,
            "qNumber": 47,
            "section": "Arithmetic",
            "topic": "Circular Race Track",
            "question_en": "Two runners A and B run on a circular track of circumference 1200 m starting from the same point at the same time in the same direction at speeds of 18 km/h and 27 km/h. After how many seconds will they meet for the first time?",
            "question_te": "1200 మీటర్ల చుట్టుకొలత గల వృత్తాకార ట్రాక్‌పై ఇద్దరు రన్నర్లు A మరియు B ఒకే బిందువు వద్ద ఒకే దిశలో గంటకు 18 కిమీ మరియు 27 కిమీ వేగంతో పరుగెత్తడం ప్రారంభించారు. మొదటిసారి వారు ఎన్ని సెకన్ల తర్వాత కలుసుకుంటారు?",
            "options_en": ["480 seconds", "400 seconds", "360 seconds", "540 seconds"],
            "options_te": ["480 సెకన్లు", "400 సెకన్లు", "360 సెకన్లు", "540 సెకన్లు"],
            "correct_option": 0,
            "explanation_en": "Relative speed = 27 - 18 = 9 km/h = 9 * (5/18) = 2.5 m/s. Time to meet = Track length / Relative speed = 1200 / 2.5 = 480 seconds.",
            "explanation_te": "సాపేక్ష వేగం = 27 - 18 = 9 కిమీ/గం = 2.5 మీ/సె. కలుసుకునే కాలం = 1200 / 2.5 = 480 సెకన్లు."
        },
        # 48. Mensuration - Path inside rectangle
        {
            "id": 48,
            "qNumber": 48,
            "section": "Arithmetic",
            "topic": "Mensuration 2D - Uniform Path",
            "question_en": "A rectangular lawn 60 m long and 40 m broad has a 2.5 m wide running path constructed all around its outer boundary. What is the total area of the path?",
            "question_te": "60 మీటర్ల పొడవు మరియు 40 మీటర్ల వెడల్పు గల దీర్ఘచతురస్రాకార లాన్ చుట్టూ బయటి వైపు 2.5 మీటర్ల వెడల్పుతో ఒక బాటను నిర్మించారు. ఆ బాట మొత్తం వైశాల్యం ఎంత?",
            "options_en": ["525 m²", "500 m²", "550 m²", "475 m²"],
            "options_te": ["525 చ.మీ", "500 చ.మీ", "550 చ.మీ", "475 చ.మీ"],
            "correct_option": 0,
            "explanation_en": "Outer dimensions = (60 + 5) = 65 m and (40 + 5) = 45 m. Outer area = 65 * 45 = 2,925 m². Inner lawn area = 60 * 40 = 2,400 m². Path area = 2925 - 2400 = 525 m².",
            "explanation_te": "బయటి వైశాల్యం = 65 * 45 = 2925 చ.మీ. లోపలి వైశాల్యం = 60 * 40 = 2400 చ.మీ. బాట వైశాల్యం = 2925 - 2400 = 525 చ.మీ."
        },
        # 49. Probability - Non-Leap Year
        {
            "id": 49,
            "qNumber": 49,
            "section": "Arithmetic",
            "topic": "Probability - Calendar Days",
            "question_en": "What is the probability that an ordinary (non-leap) year selected at random will have 53 Sundays?",
            "question_te": "యాదృచ్ఛికంగా ఎంచుకున్న ఒక సాధారణ (లీపు కాని) సంవత్సరంలో 53 ఆదివారాలు ఉండే సంభావ్యత ఎంత?",
            "options_en": ["1 / 7", "2 / 7", "53 / 365", "1 / 52"],
            "options_te": ["1 / 7", "2 / 7", "53 / 365", "1 / 52"],
            "correct_option": 0,
            "explanation_en": "A normal year has 365 days = 52 weeks + 1 odd day. That single odd day can be any of the 7 days of the week. Probability it is a Sunday = 1 / 7.",
            "explanation_te": "సాధారణ సంవత్సరంలో 365 రోజులు = 52 వారాలు + 1 అదనపు రోజు. ఆ ఒక్క రోజు ఆదివారం అయ్యే సంభావ్యత = 1 / 7."
        },
        # 50. DI - Sector Angle Pie Chart
        {
            "id": 50,
            "qNumber": 50,
            "section": "Arithmetic",
            "topic": "Data Interpretation - Pie Chart Angles",
            "question_en": "In a pie chart representing the monthly household budget of a police officer, if ₹18,000 out of a total monthly salary of ₹72,000 is spent on house rent, what central angle in degrees represents house rent?",
            "question_te": "ఒక పోలీస్ అధికారి నెలవారీ బడ్జెట్ పై చార్ట్‌లో మొత్తం రూ. 72,000 జీతంలో రూ. 18,000 ఇంటి అద్దెకు ఖర్చు చేస్తే, ఇంటి అద్దెను సూచించే కేంద్ర కోణం ఎన్ని డిగ్రీలు?",
            "options_en": ["90°", "75°", "100°", "60°"],
            "options_te": ["90°", "75°", "100°", "60°"],
            "correct_option": 0,
            "explanation_en": "Central angle = (Spent amount / Total salary) * 360° = (18000 / 72000) * 360° = (1/4) * 360° = 90°.",
            "explanation_te": "కేంద్ర కోణం = (18000 / 72000) * 360° = 90°."
        }
    ]
    return items

print("Arithmetic 50 module loaded.")
