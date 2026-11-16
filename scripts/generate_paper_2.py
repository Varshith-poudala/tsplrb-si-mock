#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full Paper Generator for TSPLRB SI Prelims Mock Test 2 (200 Questions)
Official PWT Pattern:
- 50 Arithmetic (Q1 - Q50)
- 50 Reasoning (Q51 - Q100)
- 30 General Science (Q101 - Q130) from reference_science_gk_200.json
- 35 Current Affairs 2026 (Q131 - Q165) from reference_current_affairs_400.json
- 35 Telangana History, Movement, Culture & Schemes (Q166 - Q200)
"""

import json
import os

def get_arithmetic_questions():
    return [
        {
            "id": 1,
            "qNumber": 1,
            "section": "Arithmetic",
            "topic": "Number Systems & Divisibility",
            "question_en": "What is the remainder when (77^77 + 77) is divided by 78?",
            "question_te": "(77^77 + 77) ను 78 చేత భాగించినప్పుడు వచ్చే శేషం ఎంత?",
            "options_en": ["76", "77", "1", "0"],
            "options_te": ["76", "77", "1", "0"],
            "correct_option": 0,
            "explanation_en": "77 ≡ -1 (mod 78). Therefore, (77^77 + 77) ≡ (-1)^77 + (-1) = -1 - 1 = -2 ≡ 76 (mod 78). Hence the remainder is 76.",
            "explanation_te": "77 ≡ -1 (mod 78). కాబట్టి (-1)^77 + (-1) = -2 ≡ 76 (mod 78). సరైన శేషం 76."
        },
        {
            "id": 2,
            "qNumber": 2,
            "section": "Arithmetic",
            "topic": "HCF and LCM",
            "question_en": "The traffic lights at three different road junctions change after every 48, 72 and 108 seconds respectively. If all change simultaneously at 08:20:00 hours, at what time will they change together again?",
            "question_te": "మూడు వేర్వేరు రోడ్డు క్రాసింగ్‌ల వద్ద ట్రాఫిక్ సిగ్నల్ లైట్లు వరుసగా ప్రతి 48, 72 మరియు 108 సెకన్లకు మారుతాయి. అవన్నీ ఉదయం 08:20:00 గంటలకు కలిసి మారితే, మళ్లీ ఏ సమయానికి ఏకకాలంలో మారుతాయి?",
            "options_en": ["08:27:12 hrs", "08:25:36 hrs", "08:26:12 hrs", "08:28:00 hrs"],
            "options_te": ["08:27:12 గంటలకు", "08:25:36 గంటలకు", "08:26:12 గంటలకు", "08:28:00 గంటలకు"],
            "correct_option": 0,
            "explanation_en": "LCM(48, 72, 108) = 432 seconds = 7 minutes 12 seconds. Adding to 08:20:00 gives 08:27:12 hours.",
            "explanation_te": "48, 72, 108 ల క.సా.గు = 432 సెకన్లు = 7 నిమిషాల 12 సెకన్లు. 08:20:00 కు కలిపితే 08:27:12 గంటలు వస్తుంది."
        },
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
            "explanation_en": "Unit digit of 7^753: 753%4=1 => 7^1=7. Unit digit of 9^241: 9^odd = 9. Unit digit of 2^123: 123%4=3 => 2^3=8. Product = 7 * 9 * 8 = 504. Unit digit is 4.",
            "explanation_te": "7^753 యొక్క ఒకట్ల అంకె: 7. 9^241 యొక్క ఒకట్ల అంకె: 9. 2^123 యొక్క ఒకట్ల అంకె: 8. లబ్దం = 7 * 9 * 8 = 504. ఒకట్ల స్థానంలోని అంకె 4."
        },
        {
            "id": 4,
            "qNumber": 4,
            "section": "Arithmetic",
            "topic": "Averages - Replaced Person",
            "question_en": "The average weight of 8 persons increases by 2.5 kg when a new person comes in place of one of them weighing 65 kg. What is the weight of the new person?",
            "question_te": "65 కిలోల బరువున్న వ్యక్తి స్థానంలో ఒక కొత్త వ్యక్తి రావడం వల్ల 8 మంది వ్యక్తుల సగటు బరువు 2.5 కిలోలు పెరిగింది. కొత్త వ్యక్తి బరువు ఎంత?",
            "options_en": ["76 kg", "80 kg", "85 kg", "82.5 kg"],
            "options_te": ["76 కిలోలు", "80 కిలోలు", "85 కిలోలు", "82.5 కిలోలు"],
            "correct_option": 2,
            "explanation_en": "Total increase in weight = 8 * 2.5 = 20 kg. Weight of new person = 65 + 20 = 85 kg.",
            "explanation_te": "మొత్తం బరువులో పెరుగుదల = 8 * 2.5 = 20 కిలోలు. కొత్త వ్యక్తి బరువు = 65 + 20 = 85 కిలోలు."
        },
        {
            "id": 5,
            "qNumber": 5,
            "section": "Arithmetic",
            "topic": "Percentages & Consumption",
            "question_en": "If the price of sugar rises by 25%, by what percentage should a household reduce its consumption so that the total expenditure remains unchanged?",
            "question_te": "చక్కెర ధర 25% పెరిగితే, అయ్యే ఖర్చు మారకుండా ఉండాలంటే ఒక కుటుంబం చక్కెర వినియోగాన్ని ఎంత శాతం తగ్గించుకోవాలి?",
            "options_en": ["20%", "25%", "16.67%", "15%"],
            "options_te": ["20%", "25%", "16.67%", "15%"],
            "correct_option": 0,
            "explanation_en": "Reduction % = [r / (100 + r)] * 100 = [25 / 125] * 100 = 20%.",
            "explanation_te": "వినియోగంలో తగ్గింపు శాతం = [25 / (100 + 25)] * 100 = 20%."
        },
        {
            "id": 6,
            "qNumber": 6,
            "section": "Arithmetic",
            "topic": "Profit & Loss - Successive Discounts",
            "question_en": "An article with marked price of ₹2,500 is sold at successive discounts of 20% and 10%. What is the final selling price?",
            "question_te": "రూ. 2,500 ప్రకటన వెల కలిగిన ఒక వస్తువు వరుసగా 20% మరియు 10% తగ్గింపులతో విక్రయించబడింది. ఆ వస్తువు చివరి అమ్మకపు వెల ఎంత?",
            "options_en": ["₹1,750", "₹1,800", "₹1,850", "₹1,900"],
            "options_te": ["₹1,750", "₹1,800", "₹1,850", "₹1,900"],
            "correct_option": 1,
            "explanation_en": "Selling Price = 2500 * (1 - 0.20) * (1 - 0.10) = 2500 * 0.8 * 0.9 = 2500 * 0.72 = ₹1,800.",
            "explanation_te": "అమ్మకపు వెల = 2500 * 0.8 * 0.9 = రూ. 1,800."
        },
        {
            "id": 7,
            "qNumber": 7,
            "section": "Arithmetic",
            "topic": "Simple and Compound Interest Difference",
            "question_en": "The difference between simple interest and compound interest compounded annually on a certain sum of money for 2 years at 8% per annum is ₹192. What is the principal sum?",
            "question_te": "ఒక నిర్దిష్ట అసలుపై వార్షిక 8% వడ్డీ రేటు చొప్పున 2 సంవత్సరాలకు అయ్యే బారువడ్డీ మరియు చక్రవడ్డీల మధ్య వ్యత్యాసం రూ. 192. ఆ అసలు మొత్తం ఎంత?",
            "options_en": ["₹30,000", "₹25,000", "₹28,000", "₹32,000"],
            "options_te": ["₹30,000", "₹25,000", "₹28,000", "₹32,000"],
            "correct_option": 0,
            "explanation_en": "Difference for 2 years = P * (r/100)^2 => 192 = P * (8/100)^2 => 192 = P * (64 / 10000) => P = 192 * 10000 / 64 = 3 * 10000 = ₹30,000.",
            "explanation_te": "2 సంవత్సరాలకు వ్యత్యాసం = P * (r/100)^2. 192 = P * (8/100)^2 => P = రూ. 30,000."
        },
        {
            "id": 8,
            "qNumber": 8,
            "section": "Arithmetic",
            "topic": "Ratio and Proportion - Coins",
            "question_en": "A bag contains ₹1, 50 paise and 25 paise coins in the ratio 5 : 6 : 8. If the total value of all coins in the bag is ₹240, what is the total number of 25 paise coins?",
            "question_te": "ఒక సంచిలో రూ. 1, 50 పైసలు మరియు 25 పైసల నాణేలు 5 : 6 : 8 నిష్పత్తిలో ఉన్నాయి. సంచిలోని మొత్తం నాణేల విలువ రూ. 240 అయితే, 25 పైసల నాణేల సంఖ్య ఎంత?",
            "options_en": ["192", "240", "160", "200"],
            "options_te": ["192", "240", "160", "200"],
            "correct_option": 0,
            "explanation_en": "Value per ratio unit = 5*(1) + 6*(0.50) + 8*(0.25) = 5 + 3 + 2 = ₹10. Number of ratio units = 240 / 10 = 24. Total 25p coins = 8 * 24 = 192 coins.",
            "explanation_te": "ఒక్కో యూనిట్ విలువ = 5(1) + 6(0.50) + 8(0.25) = రూ. 10. యూనిట్ల సంఖ్య = 240 / 10 = 24. 25 పైసల నాణేలు = 8 * 24 = 192."
        },
        {
            "id": 9,
            "qNumber": 9,
            "section": "Arithmetic",
            "topic": "Time and Work - Alternate Days",
            "question_en": "A can complete a work in 12 days and B can complete it in 18 days. If they work on alternate days starting with A on the first day, in how many days will the work be completed?",
            "question_te": "A ఒక పనిని 12 రోజుల్లో, B అదే పనిని 18 రోజుల్లో పూర్తి చేయగలరు. మొదటి రోజు A తో ప్రారంభించి వారు రోజు విడిచి రోజు పనిచేస్తే, ఆ పని ఎన్ని రోజుల్లో పూర్తవుతుంది?",
            "options_en": ["14 1/3 days", "14 1/2 days", "15 days", "13 2/3 days"],
            "options_te": ["14 1/3 రోజులు", "14 1/2 రోజులు", "15 రోజులు", "13 2/3 రోజులు"],
            "correct_option": 0,
            "explanation_en": "LCM of 12 and 18 = 36 units total. Efficiency: A = 3 units/day, B = 2 units/day. In 2 days, they complete 3 + 2 = 5 units. In 14 days (7 cycles of 2 days), work completed = 7 * 5 = 35 units. Remaining work = 36 - 35 = 1 unit. On 15th day, A does 1/3 day. Total time = 14 1/3 days.",
            "explanation_te": "మొత్తం పని = 36 యూనిట్లు. A = 3 యూనిట్లు/రోజు, B = 2 యూనిట్లు/రోజు. 2 రోజుల్లో 5 యూనిట్లు పూర్తవుతాయి. 14 రోజుల్లో = 35 యూనిట్లు. మిగిలిన 1 యూనిట్ పనిని A 1/3 రోజులో చేస్తాడు. మొత్తం కాలం = 14 1/3 రోజులు."
        },
        {
            "id": 10,
            "qNumber": 10,
            "section": "Arithmetic",
            "topic": "Pipes and Cisterns",
            "question_en": "Pipe A can fill a tank in 16 hours and Pipe B can empty it in 24 hours. If both pipes are opened simultaneously when the tank is empty, how many hours will it take to fill the tank completely?",
            "question_te": "పైప్ A ఒక ట్యాంకును 16 గంటల్లో నింపగలదు మరియు పైప్ B దానిని 24 గంటల్లో ఖాళీ చేయగలదు. ట్యాంక్ ఖాళీగా ఉన్నప్పుడు రెండు పైపులను ఏకకాలంలో తెరిస్తే, ట్యాంక్ పూర్తిగా నిండటానికి ఎన్ని గంటలు పడుతుంది?",
            "options_en": ["40 hours", "48 hours", "36 hours", "32 hours"],
            "options_te": ["40 గంటలు", "48 గంటలు", "36 గంటలు", "32 గంటలు"],
            "correct_option": 1,
            "explanation_en": "Total capacity = LCM(16, 24) = 48 units. Net filling rate per hour = (48/16) - (48/24) = 3 - 2 = 1 unit/hr. Time required = 48 / 1 = 48 hours.",
            "explanation_te": "మొత్తం సామర్థ్యం = 48 యూనిట్లు. నికర నింపే రేటు = 3 - 2 = 1 యూనిట్/గంట. పట్టే కాలం = 48 గంటలు."
        },
        {
            "id": 11,
            "qNumber": 11,
            "section": "Arithmetic",
            "topic": "Time, Speed & Distance",
            "question_en": "Walking at 3/4th of his normal speed, a candidate reaches his exam center 20 minutes late. What is his usual time to cover the distance?",
            "question_te": "ఒక అభ్యర్థి తన సాధారణ వేగంలో 3/4 వంతు వేగంతో నడవడం వల్ల పరీక్షా కేంద్రానికి 20 నిమిషాలు ఆలస్యంగా చేరుకుంటాడు. ఆ దూరాన్ని చేరుకోవడానికి అతని సాధారణ సమయం ఎంత?",
            "options_en": ["50 minutes", "60 minutes", "80 minutes", "75 minutes"],
            "options_te": ["50 నిమిషాలు", "60 నిమిషాలు", "80 నిమిషాలు", "75 నిమిషాలు"],
            "correct_option": 1,
            "explanation_en": "Since speed becomes 3/4, time taken becomes 4/3 of normal time. Difference = (4/3 - 1) * T = 1/3 * T = 20 mins => Usual time T = 60 minutes (1 hour).",
            "explanation_te": "వేగం 3/4 అయితే పట్టే కాలం 4/3 రెట్లు అవుతుంది. అదనపు కాలం = 1/3 * T = 20 నిమిషాలు. సాధారణ సమయం T = 60 నిమిషాలు (1 గంట)."
        },
        {
            "id": 12,
            "qNumber": 12,
            "section": "Arithmetic",
            "topic": "Problems on Trains",
            "question_en": "A 240 m long train moving at 72 km/h crosses a railway platform in 25 seconds. What is the length of the platform?",
            "question_te": "గంటకు 72 కిమీ వేగంతో ప్రయాణిస్తున్న 240 మీటర్ల పొడవున్న రైలు ఒక రైల్వే ప్లాట్‌ఫారమ్‌ను 25 సెకన్లలో దాటుతుంది. ఆ ప్లాట్‌ఫారమ్ పొడవు ఎంత?",
            "options_en": ["260 m", "240 m", "300 m", "280 m"],
            "options_te": ["260 మీటర్లు", "240 మీటర్లు", "300 మీటర్లు", "280 మీటర్లు"],
            "correct_option": 0,
            "explanation_en": "Speed = 72 * (5/18) = 20 m/s. Total distance in 25 sec = 20 * 25 = 500 m. Length of platform = Total distance - Train length = 500 - 240 = 260 m.",
            "explanation_te": "రైలు వేగం = 72 * (5/18) = 20 మీ/సె. 25 సెకన్లలో దూరం = 20 * 25 = 500 మీటర్లు. ప్లాట్‌ఫారమ్ పొడవు = 500 - 240 = 260 మీటర్లు."
        },
        {
            "id": 13,
            "qNumber": 13,
            "section": "Arithmetic",
            "topic": "Boats and Streams",
            "question_en": "A boat can travel 36 km downstream in 3 hours and 24 km upstream in 4 hours. What is the speed of the water current in km/h?",
            "question_te": "ఒక పడవ ప్రవాహ దిశలో 36 కిమీ దూరాన్ని 3 గంటల్లో మరియు ప్రవాహానికి ఎదురుగా 24 కిమీ దూరాన్ని 4 గంటల్లో ప్రయాణించగలదు. ప్రవాహ వేగం గంటకు ఎన్ని కిలోమీటర్లు?",
            "options_en": ["3 km/h", "2.5 km/h", "4 km/h", "2 km/h"],
            "options_te": ["గంటకు 3 కిమీ", "గంటకు 2.5 కిమీ", "గంటకు 4 కిమీ", "గంటకు 2 కిమీ"],
            "correct_option": 0,
            "explanation_en": "Downstream speed (u + v) = 36 / 3 = 12 km/h. Upstream speed (u - v) = 24 / 4 = 6 km/h. Speed of stream v = (12 - 6) / 2 = 3 km/h.",
            "explanation_te": "ప్రవాహ దిశలో వేగం = 12 కిమీ/గం. ఎదురు వేగం = 6 కిమీ/గం. ప్రవాహ వేగం = (12 - 6) / 2 = గంటకు 3 కిమీ."
        },
        {
            "id": 14,
            "qNumber": 14,
            "section": "Arithmetic",
            "topic": "Alligation and Mixtures",
            "question_en": "In what ratio must rice at ₹48 per kg be mixed with rice at ₹60 per kg so that selling the mixture at ₹62.70 per kg yields a profit of 10%?",
            "question_te": "కిలో రూ. 48 ఉన్న బియ్యాన్ని, కిలో రూ. 60 ఉన్న బియ్యంతో ఏ నిష్పత్తిలో కలిపితే ఆ మిశ్రమాన్ని కిలో రూ. 62.70 కు విక్రయించడం ద్వారా 10% లాభం పొందవచ్చు?",
            "options_en": ["1 : 3", "2 : 3", "3 : 4", "1 : 2"],
            "options_te": ["1 : 3", "2 : 3", "3 : 4", "1 : 2"],
            "correct_option": 0,
            "explanation_en": "Cost price of mixture = 62.70 / 1.10 = ₹57 per kg. Applying alligation: (60 - 57) : (57 - 48) = 3 : 9 = 1 : 3.",
            "explanation_te": "మిశ్రమం కొన్నవెల = 62.70 / 1.10 = రూ. 57/కిలో. మిశ్రమ నియమం ప్రకారం: (60 - 57) : (57 - 48) = 3 : 9 = 1 : 3."
        },
        {
            "id": 15,
            "qNumber": 15,
            "section": "Arithmetic",
            "topic": "Partnership",
            "question_en": "A, B and C enter into a partnership. A invests ₹40,000 for 12 months, B invests ₹60,000 for 8 months and C invests ₹80,000 for 6 months. If the annual profit is ₹36,000, what is B's share?",
            "question_te": "A, B మరియు C లు ఒక వ్యాపారంలో భాగస్వాములుగా చేరారు. A రూ. 40,000 ను 12 నెలలు, B రూ. 60,000 ను 8 నెలలు మరియు C రూ. 80,000 ను 6 నెలల పాటు పెట్టుబడి పెట్టారు. వార్షిక లాభం రూ. 36,000 అయితే, అందులో B వాటా ఎంత?",
            "options_en": ["₹12,000", "₹14,000", "₹10,000", "₹16,000"],
            "options_te": ["₹12,000", "₹14,000", "₹10,000", "₹16,000"],
            "correct_option": 0,
            "explanation_en": "Profit ratio = (40000*12) : (60000*8) : (80000*6) = 480000 : 480000 : 480000 = 1 : 1 : 1. Since all three have equal profit weights, B's share = 36000 / 3 = ₹12,000.",
            "explanation_te": "లాభాల నిష్పత్తి = 480000 : 480000 : 480000 = 1 : 1 : 1. ముగ్గురి వాటా సమానం కాబట్టి B వాటా = 36000 / 3 = రూ. 12,000."
        },
        {
            "id": 16,
            "qNumber": 16,
            "section": "Arithmetic",
            "topic": "Mensuration 2D - Circles & Rectangles",
            "question_en": "A wire when bent in the form of a square encloses an area of 484 cm². If the same wire is bent into a circle, what is the area enclosed by the circle (take π = 22/7)?",
            "question_te": "ఒక తీగను చతురస్రాకారంలో వంచినప్పుడు అది 484 చ.సెం.మీ వైశాల్యాన్ని ఆక్రమిస్తుంది. అదే తీగను వృత్తాకారంలో వంచితే, ఆ వృత్తం ఆక్రమించే వైశాల్యం ఎంత (π = 22/7)?",
            "options_en": ["616 cm²", "628 cm²", "594 cm²", "642 cm²"],
            "options_te": ["616 చ.సెం.మీ", "628 చ.సెం.మీ", "594 చ.సెం.మీ", "642 చ.సెం.మీ"],
            "correct_option": 0,
            "explanation_en": "Side of square a = √484 = 22 cm. Total length of wire (perimeter) = 4 * 22 = 88 cm. Circumference of circle = 2 * (22/7) * r = 88 => r = 14 cm. Area of circle = (22/7) * 14 * 14 = 616 cm².",
            "explanation_te": "చతురస్రం భుజం = √484 = 22 సెం.మీ. తీగ పొడవు (చుట్టుకొలత) = 88 సెం.మీ. వృత్త చుట్టుకొలత 2πr = 88 => వ్యాసార్థం r = 14 సెం.మీ. వృత్త వైశాల్యం = 616 చ.సెం.మీ."
        },
        {
            "id": 17,
            "qNumber": 17,
            "section": "Arithmetic",
            "topic": "Mensuration 3D - Cylinder and Spheres",
            "question_en": "A solid metallic cylinder of base radius 6 cm and height 36 cm is melted and recast into small solid spheres of radius 3 cm each. How many such spheres can be formed?",
            "question_te": "భూమి వ్యాసార్థం 6 సెం.మీ మరియు ఎత్తు 36 సెం.మీ కలిగిన ఒక లోహపు స్థూపాన్ని కరిగించి, ప్రతి ఒక్కటి 3 సెం.మీ వ్యాసార్థం గల చిన్న ఘన గోళాలుగా మార్చారు. అటువంటి ఎన్ని గోళాలను తయారు చేయవచ్చు?",
            "options_en": ["36", "48", "32", "24"],
            "options_te": ["36", "48", "32", "24"],
            "correct_option": 0,
            "explanation_en": "Volume of cylinder = π * r1^2 * h = π * 36 * 36 = 1296π. Volume of one sphere = (4/3) * π * r2^3 = (4/3) * π * 27 = 36π. Number of spheres = 1296π / 36π = 36 spheres.",
            "explanation_te": "స్థూపం ఘనపరిమాణం = π * 6^2 * 36 = 1296π. ఒక గోళం ఘనపరిమాణం = 4/3 * π * 27 = 36π. గోళాల సంఖ్య = 1296π / 36π = 36."
        },
        {
            "id": 18,
            "qNumber": 18,
            "section": "Arithmetic",
            "topic": "Permutations and Combinations",
            "question_en": "In how many distinct ways can the letters of the word 'POLICE' be arranged such that all vowels always remain together?",
            "question_te": "'POLICE' అనే పదం లోని అక్షరాలను, అచ్చులన్నీ ఎల్లప్పుడూ కలిసి ఉండేలా ఎన్ని విభిన్న రకాలుగా అమర్చవచ్చు?",
            "options_en": ["144", "120", "240", "720"],
            "options_te": ["144", "120", "240", "720"],
            "correct_option": 0,
            "explanation_en": "Word 'POLICE' has 6 letters: Vowels = O, I, E (3 letters). Consonants = P, L, C (3 letters). Treat (O, I, E) as a single block. Total units to arrange = 3 consonants + 1 block = 4 units => 4! = 24. Inside the block, 3 vowels arrange in 3! = 6 ways. Total arrangements = 24 * 6 = 144.",
            "explanation_te": "'POLICE' లో అచ్చులు: O, I, E (3), హల్లులు: P, L, C (3). అచ్చులను ఒకే యూనిట్‌గా భావిస్తే మొత్తం 4 యూనిట్లు => 4! = 24. అచ్చులు తమలో తాము 3! = 6 రకాలుగా అమరుతాయి. మొత్తం అమరికలు = 24 * 6 = 144."
        },
        {
            "id": 19,
            "qNumber": 19,
            "section": "Arithmetic",
            "topic": "Probability - Cards",
            "question_en": "Two cards are drawn at random without replacement from a standard well-shuffled pack of 52 playing cards. What is the probability that both cards drawn are Kings?",
            "question_te": "బాగా కలిపిన 52 పేక ముక్కల కట్ట నుండి తిరిగి ఉంచకుండా యాదృచ్ఛికంగా రెండు కార్డులను తీశారు. ఆ రెండు కార్డులు కూడా రాజులు (Kings) అయ్యే సంభావ్యత ఎంత?",
            "options_en": ["1 / 221", "1 / 169", "2 / 221", "1 / 26"],
            "options_te": ["1 / 221", "1 / 169", "2 / 221", "1 / 26"],
            "correct_option": 0,
            "explanation_en": "Number of Kings = 4. Probability = (4/52) * (3/51) = (1/13) * (1/17) = 1 / 221.",
            "explanation_te": "మొత్తం రాజు కార్డులు = 4. సంభావ్యత = (4/52) * (3/51) = (1/13) * (1/17) = 1 / 221."
        },
        {
            "id": 20,
            "qNumber": 20,
            "section": "Arithmetic",
            "topic": "Data Interpretation - Tabular Analysis",
            "question_en": "The total sales of a police recruitment book across 5 districts in 2024 is 45,000 copies. If Warangal district accounts for 24% and Karimnagar accounts for 18% of the sales, what is the difference in sales between these two districts?",
            "question_te": "2024లో 5 జిల్లాలలో పోలీస్ రిక్రూట్‌మెంట్ పుస్తకం మొత్తం అమ్మకాలు 45,000 కాపీలు. వరంగల్ జిల్లా వాటా 24% మరియు కరీంనగర్ వాటా 18% అయితే, ఈ రెండు జిల్లాల మధ్య అమ్మకాల వ్యత్యాసం ఎంత?",
            "options_en": ["2,700", "3,150", "2,400", "2,250"],
            "options_te": ["2,700", "3,150", "2,400", "2,250"],
            "correct_option": 0,
            "explanation_en": "Difference in percentage = 24% - 18% = 6%. Difference in copies = 6% of 45,000 = 0.06 * 45000 = 2,700.",
            "explanation_te": "శాతాల మధ్య వ్యత్యాసం = 24% - 18% = 6%. కాపీల వ్యత్యాసం = 45000 లో 6% = 2,700."
        }
    ]

print("Arithmetic module ready with 20 base high-yield questions.")
