# -*- coding: utf-8 -*-
"""
Arithmetic Part 2 (Q61 to Q120):
- Time & Work (Q61 to Q80)
- Pipes & Cisterns (Q81 to Q95)
- Profit, Loss & Discount (Q96 to Q110)
- Simple & Compound Interest (Q111 to Q120)
"""

def get_part2():
    qs = []
    def make_q(id_num, topic, diff, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
        return {
            "id": id_num,
            "section": "Arithmetic & Quantitative Reasoning",
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

    qs.append(make_q(
        61, "Time & Work - Alternate Days", "Medium",
        """A can complete a piece of work in 12 days and B can complete it in 18 days. If they work on alternate days with A starting on the first day, in how many days will the entire work be completed?""",
        """A ఒక పనిని 12 రోజుల్లో, B అదే పనిని 18 రోజుల్లో పూర్తి చేయగలరు. మొదటి రోజు A తో ప్రారంభించి, వారు రోజు మార్చి రోజు పనిచేస్తే, ఆ పని మొత్తం ఎన్ని రోజుల్లో పూర్తవుతుంది?""",
        ['14 1/3 days', '14 1/2 days', '15 days', '13 2/3 days'],
        ['14 1/3 రోజులు', '14 1/2 రోజులు', '15 రోజులు', '13 2/3 రోజులు'],
        0,
        """Total work = LCM(12, 18) = 36 units. Efficiency of A = 3 units/day, B = 2 units/day.
Work in 2 days (1 cycle) = 3 + 2 = 5 units.
In 7 cycles (14 days), work completed = 7 * 5 = 35 units.
Remaining work = 36 - 35 = 1 unit.
On day 15, A works: time taken = 1/3 day.
Total time = 14 + 1/3 = 14 1/3 days.""",
        """మొత్తం పని = LCM(12, 18) = 36 యూనిట్లు. A సామర్థ్యం = 3, B సామర్థ్యం = 2.
2 రోజులలో (1 సైకిల్) పని = 5 యూనిట్లు.
7 సైకిల్స్ (14 రోజులు) లో = 35 యూనిట్లు.
మిగిలిన పని = 1 యూనిట్. 15వ రోజు A కు పట్టే కాలం = 1/3 రోజు.
మొత్తం సమయం = 14 1/3 రోజులు."""
    ))

    qs.append(make_q(
        62, "Time & Work - Leaving Before Completion", "Hard",
        """A, B, and C can complete a task in 10, 15, and 30 days respectively. All three started the work together, but A left 2 days before the scheduled completion and B left 3 days before completion. For how many days did the work actually continue?""",
        """A, B మరియు C లు ఒక పనిని వరుసగా 10, 15 మరియు 30 రోజుల్లో చేయగలరు. ముగ్గురూ కలిసి పని ప్రారంభించారు, కానీ పని పూర్తి కావడానికి 2 రోజుల ముందు A, 3 రోజుల ముందు B విడిచిపెట్టారు. ఆ పని మొత్తం ఎన్ని రోజులు కొనసాగింది?""",
        ['7 days', '8 days', '6 days', '9 days'],
        ['7 రోజులు', '8 రోజులు', '6 రోజులు', '9 రోజులు'],
        0,
        """Total work = LCM(10, 15, 30) = 30 units.
Efficiency: A = 3, B = 2, C = 1 (Total = 6 units/day).
Shortcut: Add work left undone: Total effective work = 30 + (2 days * 3 for A) + (3 days * 2 for B) = 30 + 6 + 6 = 42 units.
Total days = 42 / 6 = 7 days.""",
        """మొత్తం పని = 30 యూనిట్లు. సామర్థ్యాలు: A = 3, B = 2, C = 1 (మొత్తం = 6 యూనిట్లు/రోజు).
షార్ట్‌కట్: ముందుగా వెళ్లిపోయిన వారి పనిని మొత్తం పనికి కలపండి: 30 + (2*3) + (3*2) = 42 యూనిట్లు.
మొత్తం రోజులు = 42 / 6 = 7 రోజులు."""
    ))

    qs.append(make_q(
        63, "Time & Work - Efficiency Ratio", "Medium",
        """A is 40% more efficient than B, and B takes 35 days to finish a construction work alone. In how many days can A and B working together finish the same work?""",
        """A అనే వ్యక్తి B కంటే 40% ఎక్కువ సమర్థుడు. B ఒంటరిగా ఆ పనిని 35 రోజుల్లో పూర్తి చేయగలడు. వారిద్దరూ కలిసి పనిచేస్తే అదే పనిని ఎన్ని రోజుల్లో పూర్తి చేయగలరు?""",
        ['14 7/12 days', '15 days', '16 2/3 days', '14 days'],
        ['14 7/12 రోజులు', '15 రోజులు', '16 2/3 రోజులు', '14 రోజులు'],
        0,
        """Ratio of efficiencies A : B = 140 : 100 = 7 : 5.
Total work = Efficiency of B * Days = 5 * 35 = 175 units.
Combined efficiency of A + B = 7 + 5 = 12 units/day.
Days required together = 175 / 12 = 14 7/12 days.""",
        """A మరియు B ల సామర్థ్యాల నిష్పత్తి = 7 : 5.
మొత్తం పని = 5 * 35 = 175 యూనిట్లు.
ఉమ్మడి సామర్థ్యం = 7 + 5 = 12 యూనిట్లు/రోజు.
పట్టే రోజులు = 175 / 12 = 14 7/12 రోజులు."""
    ))

    qs.append(make_q(
        64, "Time & Work - Men, Women & Children", "Hard",
        """1 man or 2 women or 3 boys can finish a piece of work in 44 days. In how many days will 1 man, 1 woman, and 1 boy working together finish the same work?""",
        """1 పురుషుడు లేదా 2 స్త్రీలు లేదా 3 బాలురు ఒక పనిని 44 రోజుల్లో చేయగలరు. 1 పురుషుడు, 1 స్త్రీ మరియు 1 బాలుడు కలిసి అదే పనిని ఎన్ని రోజుల్లో పూర్తి చేయగలరు?""",
        ['24 days', '22 days', '26 days', '28 days'],
        ['24 రోజులు', '22 రోజులు', '26 రోజులు', '28 రోజులు'],
        0,
        """Shortcut Formula: Days = D / (m2/m1 + w2/w1 + b2/b1)
Here D = 44, m1=1, w1=2, b1=3; m2=1, w2=1, b2=1.
Days = 44 / (1/1 + 1/2 + 1/3) = 44 / ((6 + 3 + 2)/6) = 44 / (11/6) = (44 * 6) / 11 = 4 * 6 = 24 days.""",
        """షార్ట్‌కట్ సూత్రం: Days = D / (m2/m1 + w2/w1 + b2/b1).
రోజులు = 44 / (1/1 + 1/2 + 1/3) = 44 / (11/6) = (44 * 6) / 11 = 24 రోజులు."""
    ))

    qs.append(make_q(
        65, "Time & Work - Wages Distribution", "Medium",
        """A and B undertook to do a piece of work for Rs. 4,800. A alone could do it in 6 days and B alone in 8 days. With the assistance of a boy, they finished it in 3 days. What is the boy's share of the money?""",
        """A మరియు B లు ఒక పనిని రూ. 4,800 లకు ఒప్పందం చేసుకున్నారు. A ఒంటరిగా 6 రోజుల్లో, B ఒంటరిగా 8 రోజుల్లో చేయగలరు. ఒక బాలుడి సహాయంతో వారు ఆ పనిని 3 రోజుల్లో ముగించారు. బాలుడికి వచ్చే వాటా ఎంత?""",
        ['Rs. 600', 'Rs. 800', 'Rs. 750', 'Rs. 500'],
        ['రూ. 600', 'రూ. 800', 'రూ. 750', 'రూ. 500'],
        0,
        """Total work = LCM(6, 8, 3) = 24 units. Efficiency of (A+B+Boy) = 24/3 = 8 units/day.
Efficiency of A = 24/6 = 4 units/day; Efficiency of B = 24/8 = 3 units/day.
Boy's efficiency = 8 - (4 + 3) = 1 unit/day.
Boy's share = (1/8) * 4800 = Rs. 600.""",
        """మొత్తం పని = 24 యూనిట్లు. ఉమ్మడి సామర్థ్యం = 8 యూనిట్లు/రోజు.
A సామర్థ్యం = 4, B సామర్థ్యం = 3.
బాలుడి సామర్థ్యం = 8 - 7 = 1 యూనిట్/రోజు.
బాలుడి వాటా = (1/8) * 4800 = రూ. 600."""
    ))

    qs.append(make_q(
        66, "Time & Work - Negative Work", "Hard",
        """A builder can build a perimeter security wall in 10 days, while a demolition machine can completely demolish it in 15 days. If they work on alternate days with the builder working on day 1, on which day will the wall be completely built?""",
        """ఒక తాపీ మేస్త్రీ భద్రతా గోడను 10 రోజుల్లో నిర్మించగలడు, కాగా కూల్చివేత యంత్రం దానిని 15 రోజుల్లో నేలమట్టం చేయగలదు. మొదటి రోజు మేస్త్రీతో ప్రారంభించి వారు రోజు మార్చి రోజు పనిచేస్తే, గోడ నిర్మాణం ఎన్నవ రోజున పూర్తవుతుంది?""",
        ['55th day', '54th day', '57th day', '60th day'],
        ['55వ రోజు', '54వ రోజు', '57వ రోజు', '60వ రోజు'],
        0,
        """Total work = LCM(10, 15) = 30 units. Builder = +3 units/day, Demolisher = -2 units/day.
Net work in 2 days (1 cycle) = 3 - 2 = 1 unit.
Since builder finishes 3 units on odd days, work before the final day must reach 30 - 3 = 27 units.
Time to reach 27 units = 27 cycles * 2 = 54 days.
On the 55th day, the builder adds 3 units: 27 + 3 = 30 units (wall complete!).""",
        """మొత్తం పని = 30 యూనిట్లు. మేస్త్రీ = +3, కూల్చివేత = -2. 2 రోజులకు నికర పని = 1 యూనిట్.
చివరి రోజు మేస్త్రీ 3 యూనిట్లు పూర్తి చేస్తాడు కాబట్టి, 27 యూనిట్లు చేరడానికి 27 * 2 = 54 రోజులు పడుతుంది.
55వ రోజున మేస్త్రీ 3 యూనిట్లు నిర్మించడంతో గోడ పూర్తవుతుంది. సమాధానం: 55వ రోజు."""
    ))

    qs.append(make_q(
        67, "Time & Work - Contractor & Extra Men", "Hard",
        """A contractor undertook to complete a road project in 120 days and deployed 100 men. After 45 days, he found that only 1/4th of the total work was completed. How many additional men must he employ to finish the project strictly on time?""",
        """ఒక కాంట్రాక్టర్ 120 రోజుల్లో ఒక రోడ్డు ప్రాజెక్టును పూర్తి చేయడానికి ఒప్పందం చేసుకుని 100 మంది వ్యక్తులను నియమించాడు. 45 రోజుల తర్వాత కేవలం 1/4 వంతు పని మాత్రమే పూర్తయిందని గుర్తించాడు. ప్రాజెక్టును నిర్దేశిత సమయంలో పూర్తి చేయడానికి అతను అదనంగా ఎంతమంది వ్యక్తులను నియమించాలి?""",
        ['80 additional men', '75 additional men', '90 additional men', '60 additional men'],
        ['80 మంది అదనపు వ్యక్తులు', '75 మంది అదనపు వ్యక్తులు', '90 మంది అదనపు వ్యక్తులు', '60 మంది అదనపు వ్యక్తులు'],
        0,
        """Formula: (M1 * D1) / W1 = (M2 * D2) / W2
M1 = 100, D1 = 45, W1 = 1/4.
Remaining work W2 = 3/4. Remaining days D2 = 120 - 45 = 75 days.
(100 * 45) / (1/4) = (M2 * 75) / (3/4) => (100 * 45) = (M2 * 75) / 3 => 4500 = M2 * 25 => M2 = 180 men.
Additional men required = 180 - 100 = 80 men.""",
        """సూత్రం: (M1 * D1) / W1 = (M2 * D2) / W2.
(100 * 45) / 1 = (M2 * 75) / 3 => 4500 = M2 * 25 => M2 = 180 మంది.
అదనంగా కావలసిన వ్యక్తులు = 180 - 100 = 80 మంది."""
    ))

    qs.append(make_q(
        68, "Time & Work - Partial Periods", "Hard",
        """A and B together can complete a work in 12 days, while B and C together can complete it in 16 days. A worked on it for 5 days, B worked on it for 7 days, and C completed the remaining work in 13 days. In how many days can C alone complete the entire work?""",
        """A మరియు B కలిసి ఒక పనిని 12 రోజుల్లో, B మరియు C కలిసి 16 రోజుల్లో చేయగలరు. ఆ పనిపై A 5 రోజులు, B 7 రోజులు పనిచేసిన తర్వాత మిగిలిన పనిని C ఒంటరిగా 13 రోజుల్లో పూర్తి చేశాడు. C ఒక్కడే మొత్తం పనిని ఎన్ని రోజుల్లో పూర్తి చేయగలడు?""",
        ['24 days', '20 days', '28 days', '32 days'],
        ['24 రోజులు', '20 రోజులు', '28 రోజులు', '32 రోజులు'],
        0,
        """Total work = LCM(12, 16) = 48 units.
Efficiency of (A+B) = 4 units/day; Efficiency of (B+C) = 3 units/day.
Group work: 5*(A+B) + 2*(B+C) + 11*C = 48 units.
5*(4) + 2*(3) + 11*C = 48 => 20 + 6 + 11*C = 48 => 11*C = 22 => C = 2 units/day.
Time for C alone = 48 / 2 = 24 days.""",
        """మొత్తం పని = 48 యూనిట్లు. (A+B) = 4, (B+C) = 3.
పని విభజన: 5(A+B) + 2(B+C) + 11C = 48 => 20 + 6 + 11C = 48 => 11C = 22 => C = 2 యూనిట్లు/రోజు.
C ఒక్కడే మొత్తం పనిని చేసే రోజులు = 48 / 2 = 24 రోజులు."""
    ))

    qs.append(make_q(
        69, "Time & Work - Combined Time Formula", "Medium",
        """A alone takes 4 days more than the time taken by (A + B) together to finish a task. B alone takes 9 days more than the time taken by (A + B) together. In how many days can A and B together finish the task?""",
        """A ఒంటరిగా ఒక పనిని పూర్తి చేయడానికి (A + B) కలిసి పట్టే సమయం కంటే 4 రోజులు ఎక్కువ పడుతుంది. B ఒంటరిగా పూర్తి చేయడానికి (A + B) కంటే 9 రోజులు ఎక్కువ పడుతుంది. A మరియు B కలిసి ఆ పనిని ఎన్ని రోజుల్లో పూర్తి చేయగలరు?""",
        ['6 days', '8 days', '7 days', '5 days'],
        ['6 రోజులు', '8 రోజులు', '7 రోజులు', '5 రోజులు'],
        0,
        """Standard Shortcut: If A takes (T + a) days and B takes (T + b) days, then combined time T = sqrt(a * b).
Here a = 4 days, b = 9 days.
T = sqrt(4 * 9) = sqrt(36) = 6 days.""",
        """షార్ట్‌కట్ సూత్రం: T = sqrt(a * b).
T = sqrt(4 * 9) = sqrt(36) = 6 రోజులు."""
    ))

    qs.append(make_q(
        70, "Time & Work - Men Joining Mid-way", "Medium",
        """12 men can complete a work in 18 days. 6 days after they started working, 4 more men joined them. In how many days will the remaining work be completed?""",
        """12 మంది వ్యక్తులు ఒక పనిని 18 రోజుల్లో పూర్తి చేయగలరు. వారు పని ప్రారంభించిన 6 రోజుల తర్వాత మరో 4 గురు వ్యక్తులు వారితో చేరారు. మిగిలిన పని ఎన్ని రోజుల్లో పూర్తవుతుంది?""",
        ['9 days', '8 days', '10 days', '7.5 days'],
        ['9 రోజులు', '8 రోజులు', '10 రోజులు', '7.5 రోజులు'],
        0,
        """Remaining work for 12 men = 18 - 6 = 12 days of work.
Total man-days remaining = 12 * 12 = 144 man-days.
New total men = 12 + 4 = 16 men.
Days to finish remaining work = 144 / 16 = 9 days.""",
        """12 మందికి మిగిలిన పని = 18 - 6 = 12 రోజుల పని = 12 * 12 = 144 మ్యాన్-డేస్.
కొత్త వ్యక్తుల సంఖ్య = 12 + 4 = 16 మంది.
మిగిలిన పనికి పట్టే రోజులు = 144 / 16 = 9 రోజులు."""
    ))

    qs.append(make_q(
        71, "Time & Work - Person Leaves After Start", "Medium",
        """A can complete a task in 20 days and B in 25 days. They start the task together, but B leaves after 5 days. How many more days will A take to complete the remaining task alone?""",
        """A ఒక పనిని 20 రోజుల్లో, B 25 రోజుల్లో చేయగలరు. ఇద్దరూ కలిసి పనిని ప్రారంభించారు, కానీ 5 రోజుల తర్వాత B విడిచిపెట్టాడు. మిగిలిన పనిని ఒంటరిగా పూర్తి చేయడానికి A కి ఇంకా ఎన్ని రోజులు పడుతుంది?""",
        ['11 days', '12 days', '10 days', '13 days'],
        ['11 రోజులు', '12 రోజులు', '10 రోజులు', '13 రోజులు'],
        0,
        """Total work = LCM(20, 25) = 100 units. Efficiency: A = 5, B = 4.
Work done together in 5 days = 5 * (5 + 4) = 5 * 9 = 45 units.
Remaining work = 100 - 45 = 55 units.
Days taken by A alone to finish remaining = 55 / 5 = 11 days.""",
        """మొత్తం పని = 100 యూనిట్లు. సామర్థ్యాలు: A = 5, B = 4.
5 రోజుల్లో కలిసి చేసిన పని = 5 * 9 = 45 యూనిట్లు.
మిగిలిన పని = 55 యూనిట్లు.
A కి మిగిలిన పని చేయడానికి పట్టే రోజులు = 55 / 5 = 11 రోజులు."""
    ))

    qs.append(make_q(
        72, "Time & Work - Efficiency Change", "Hard",
        """P can complete a job in 24 days. After working alone for 6 days, his efficiency doubles due to advanced equipment. In how many total days was the entire job completed?""",
        """P ఒక పనిని 24 రోజుల్లో చేయగలడు. 6 రోజులు ఒంటరిగా పనిచేసిన తర్వాత, ఆధునిక పరికరాల వల్ల అతని పని సామర్థ్యం రెట్టింపు అయింది. ఆ పని మొత్తం ఎన్ని రోజుల్లో పూర్తయింది?""",
        ['15 days', '14 days', '16 days', '18 days'],
        ['15 రోజులు', '14 రోజులు', '16 రోజులు', '18 రోజులు'],
        0,
        """Total work = 24 units (efficiency = 1 unit/day).
In first 6 days, work done = 6 units. Remaining work = 24 - 6 = 18 units.
New efficiency = 2 units/day.
Time for remaining work = 18 / 2 = 9 days.
Total days = 6 + 9 = 15 days.""",
        """మొత్తం పని = 24 యూనిట్లు (రోజుకు 1 యూనిట్).
మొదటి 6 రోజుల్లో పని = 6 యూనిట్లు. మిగిలిన పని = 18 యూనిట్లు.
రెట్టింపు సామర్థ్యం = రోజుకు 2 యూనిట్లు. మిగిలిన పనికి పట్టే రోజులు = 18 / 2 = 9 రోజులు.
మొత్తం సమయం = 6 + 9 = 15 రోజులు."""
    ))

    qs.append(make_q(
        73, "Time & Work - Men and Boys Equations", "Hard",
        """8 men and 12 boys can finish a piece of work in 10 days, while 6 men and 8 boys can finish it in 14 days. In how many days can 1 man alone finish the work?""",
        """8 మంది పురుషులు మరియు 12 మంది బాలురు ఒక పనిని 10 రోజుల్లో చేయగలరు, 6 మంది పురుషులు మరియు 8 మంది బాలురు దానిని 14 రోజుల్లో చేయగలరు. 1 పురుషుడు ఒక్కడే ఆ పనిని ఎన్ని రోజుల్లో పూర్తి చేయగలడు?""",
        ['140 days', '120 days', '160 days', '100 days'],
        ['140 రోజులు', '120 రోజులు', '160 రోజులు', '100 రోజులు'],
        0,
        """(8M + 12B) * 10 = (6M + 8B) * 14 => 80M + 120B = 84M + 112B => 4M = 8B => 1M = 2B.
Substitute in first case: 8M + 12*(0.5M) = 8M + 6M = 14M can finish in 10 days.
Total work = 14 * 10 = 140 man-days.
Time taken by 1 man alone = 140 / 1 = 140 days.""",
        """80M + 120B = 84M + 112B => 4M = 8B => 1M = 2B.
మొదటి గ్రూప్: 8M + 6M = 14 మంది పురుషులు 10 రోజుల్లో చేస్తారు.
మొత్తం పని = 14 * 10 = 140 మ్యాన్-డేస్.
ఒక్క పురుషుడు చేసే రోజులు = 140 రోజులు."""
    ))

    qs.append(make_q(
        74, "Time & Work - Three Person Ratio", "Hard",
        """A is twice as fast as B, and B is thrice as fast as C. If working together all three can complete a project in 30 days, in how many days can A alone complete the project?""",
        """A అనే వ్యక్తి B కంటే రెండు రెట్లు వేగంగా, B అనే వ్యక్తి C కంటే మూడు రెట్లు వేగంగా పనిచేస్తారు. ముగ్గురూ కలిసి ఆ ప్రాజెక్టును 30 రోజుల్లో పూర్తి చేయగలిగితే, A ఒక్కడే దానిని ఎన్ని రోజుల్లో పూర్తి చేయగలడు?""",
        ['50 days', '45 days', '60 days', '40 days'],
        ['50 రోజులు', '45 రోజులు', '60 రోజులు', '40 రోజులు'],
        0,
        """Let C's efficiency = 1 unit/day.
Then B = 3 units/day, and A = 2 * 3 = 6 units/day.
Combined efficiency = 6 + 3 + 1 = 10 units/day.
Total work = 10 * 30 = 300 units.
Days taken by A alone = 300 / 6 = 50 days.""",
        """C సామర్థ్యం = 1 అనుకుంటే, B = 3, A = 6.
ముగ్గురి ఉమ్మడి సామర్థ్యం = 6 + 3 + 1 = 10 యూనిట్లు/రోజు.
మొత్తం పని = 10 * 30 = 300 యూనిట్లు.
A ఒక్కడికి పట్టే రోజులు = 300 / 6 = 50 రోజులు."""
    ))

    qs.append(make_q(
        75, "Time & Work - Alternating Assistance", "Hard",
        """A, B, and C can do a job in 20, 30, and 60 days respectively. In how many days can A do the job if he is assisted by B and C on every third day?""",
        """A, B మరియు C లు ఒక పనిని వరుసగా 20, 30 మరియు 60 రోజుల్లో చేయగలరు. ప్రతి మూడవ రోజున B మరియు C ల సహాయం పొందుతూ A ఆ పనిని ఎన్ని రోజుల్లో పూర్తి చేయగలడు?""",
        ['15 days', '16 days', '12 days', '18 days'],
        ['15 రోజులు', '16 రోజులు', '12 రోజులు', '18 రోజులు'],
        0,
        """Total work = LCM(20, 30, 60) = 60 units. Efficiency: A = 3, B = 2, C = 1.
Day 1: A works = 3 units.
Day 2: A works = 3 units.
Day 3: (A + B + C) works = 3 + 2 + 1 = 6 units.
Work in 3 days (1 cycle) = 3 + 3 + 6 = 12 units.
Number of cycles to complete 60 units = 60 / 12 = 5 cycles.
Total days = 5 cycles * 3 days = 15 days.""",
        """మొత్తం పని = 60 యూనిట్లు. సామర్థ్యాలు: A = 3, B = 2, C = 1.
3 రోజుల (1 సైకిల్) లో పూర్తయ్యే పని = 3 + 3 + 6 = 12 యూనిట్లు.
60 యూనిట్లకు పట్టే సైకిల్స్ = 60 / 12 = 5 సైకిల్స్.
మొత్తం రోజులు = 5 * 3 = 15 రోజులు."""
    ))

    qs.append(make_q(
        76, "Time & Work - MDH Formula", "Medium",
        """15 men working 8 hours a day can complete 2/3 of a work in 20 days. How many men working 6 hours a day are required to complete the remaining work in 10 days?""",
        """రోజుకు 8 గంటలు పనిచేస్తూ 15 మంది వ్యక్తులు 20 రోజుల్లో 2/3 వంతు పనిని పూర్తి చేయగలరు. రోజుకు 6 గంటలు పనిచేస్తూ మిగిలిన పనిని 10 రోజుల్లో పూర్తి చేయడానికి ఎంతమంది వ్యక్తులు అవసరం?""",
        ['20 men', '18 men', '24 men', '16 men'],
        ['20 మంది వ్యక్తులు', '18 మంది వ్యక్తులు', '24 మంది వ్యక్తులు', '16 మంది వ్యక్తులు'],
        0,
        """MDH Formula: (M1 * D1 * H1) / W1 = (M2 * D2 * H2) / W2
(15 * 20 * 8) / (2/3) = (M2 * 10 * 6) / (1/3)
(2400) / 2 = (60 * M2) / 1 => 1200 = 60 * M2 => M2 = 20 men.""",
        """సూత్రం: (M1 * D1 * H1) / W1 = (M2 * D2 * H2) / W2.
(15 * 20 * 8) / 2 = (M2 * 10 * 6) / 1 => 1200 = 60 * M2 => M2 = 20 మంది."""
    ))

    qs.append(make_q(
        77, "Time & Work - New Partner Assists", "Hard",
        """A and B can do a work in 15 days and 10 days respectively. They worked together for 2 days, after which B left. A was then joined by C, and together they finished the remaining work in 4 days. In how many days can C alone complete the entire work?""",
        """A మరియు B ఒక పనిని వరుసగా 15 రోజులు మరియు 10 రోజుల్లో చేయగలరు. వారు 2 రోజులు కలిసి పనిచేసిన తర్వాత B వెళ్లిపోయాడు. అప్పుడు A తో C జతకట్టగా, వారు మిగిలిన పనిని 4 రోజుల్లో పూర్తి చేశారు. C ఒక్కడే మొత్తం పనిని ఎన్ని రోజుల్లో పూర్తి చేయగలడు?""",
        ['10 days', '12 days', '15 days', '18 days'],
        ['10 రోజులు', '12 రోజులు', '15 రోజులు', '18 రోజులు'],
        0,
        """Total work = LCM(15, 10) = 30 units. Efficiency: A = 2, B = 3 units/day.
Work in first 2 days by (A + B) = 2 * (2 + 3) = 10 units.
Remaining work = 30 - 10 = 20 units.
A and C finished 20 units in 4 days => Combined efficiency (A + C) = 20 / 4 = 5 units/day.
Since A's efficiency = 2, C's efficiency = 5 - 2 = 3 units/day.
Time for C alone = 30 / 3 = 10 days.""",
        """మొత్తం పని = 30 యూనిట్లు. A = 2, B = 3. మొదటి 2 రోజుల్లో పని = 10 యూనిట్లు.
మిగిలిన పని = 20 యూనిట్లు. 4 రోజుల్లో (A+C) సామర్థ్యం = 20/4 = 5. C సామర్థ్యం = 5 - 2 = 3.
C ఒక్కడికే పట్టే రోజులు = 30 / 3 = 10 రోజులు."""
    ))

    qs.append(make_q(
        78, "Time & Work - Police Mess Provisions", "Medium",
        """A police training academy has food provisions for 500 recruits for 27 days. After 3 days, a reinforcement of 300 additional recruits arrives at the academy. For how many more days will the remaining provisions last?""",
        """ఒక పోలీస్ ట్రైనింగ్ అకాడమీలో 500 మంది రిక్రూట్‌లకు 27 రోజులకు సరిపడా ఆహార నిల్వలు ఉన్నాయి. 3 రోజుల తర్వాత మరో 300 మంది అదనపు రిక్రూట్‌లు అకాడమీకి వచ్చారు. మిగిలిన ఆహారం ఇంకా ఎన్ని రోజులు వస్తుంది?""",
        ['15 days', '16 days', '14 days', '18 days'],
        ['15 రోజులు', '16 రోజులు', '14 రోజులు', '18 రోజులు'],
        0,
        """After 3 days, remaining food is sufficient for 500 men for (27 - 3) = 24 days.
Total recruit-days of food left = 500 * 24 = 12,000.
New total recruits = 500 + 300 = 800 recruits.
Days food will last = 12,000 / 800 = 15 days.""",
        """3 రోజుల తర్వాత, 500 మందికి మిగిలిన ఆహారం 24 రోజులకు సరిపోతుంది.
మొత్తం నిల్వ = 500 * 24 = 12,000 మ్యాన్-డేస్.
నూతన రిక్రూట్‌ల సంఖ్య = 800 మంది.
మిగిలిన ఆహారం వచ్చే రోజులు = 12,000 / 800 = 15 రోజులు."""
    ))

    qs.append(make_q(
        79, "Time & Work - Wages Proportion", "Medium",
        """A can do a work in 12 days and B can do it in 15 days. With the help of C, they complete the entire work in 4 days. If the total payment for the work is Rs. 1,800, what is C's share of the payment?""",
        """A ఒక పనిని 12 రోజుల్లో, B 15 రోజుల్లో చేయగలరు. C సహాయంతో వారు మొత్తం పనిని 4 రోజుల్లో పూర్తి చేశారు. ఆ పనికి మొత్తం చెల్లింపు రూ. 1,800 అయితే, అందులో C వాటా ఎంత?""",
        ['Rs. 720', 'Rs. 600', 'Rs. 480', 'Rs. 800'],
        ['రూ. 720', 'రూ. 600', 'రూ. 480', 'రూ. 800'],
        0,
        """Total work = LCM(12, 15, 4) = 60 units. Total efficiency = 60 / 4 = 15 units/day.
Efficiency of A = 60 / 12 = 5 units/day; Efficiency of B = 60 / 15 = 4 units/day.
Efficiency of C = 15 - (5 + 4) = 6 units/day.
Wages are shared in ratio of efficiency = 5 : 4 : 6 (Total = 15 parts).
C's share = (6 / 15) * 1800 = 6 * 120 = Rs. 720.""",
        """మొత్తం పని = 60 యూనిట్లు. ఉమ్మడి సామర్థ్యం = 15 యూనిట్లు/రోజు.
A = 5, B = 4, C = 15 - 9 = 6 యూనిట్లు/రోజు.
వాటాల నిష్పత్తి = 5 : 4 : 6 (మొత్తం 15 భాగాలు).
C వాటా = (6 / 15) * 1800 = రూ. 720."""
    ))

    qs.append(make_q(
        80, "Time & Work - Production Rate", "Medium",
        """If 5 automatic bullet-casing machines produce 500 casings in 5 minutes, how many minutes will 10 identical machines take to produce 1,000 casings?""",
        """5 ఆటోమేటిక్ బుల్లెట్ కేసింగ్ యంత్రాలు 5 నిమిషాల్లో 500 కేసింగ్‌లను తయారు చేస్తే, 10 అవే రకమైన యంత్రాలు 1,000 కేసింగ్‌లను తయారు చేయడానికి ఎన్ని నిమిషాలు పడుతుంది?""",
        ['5 minutes', '10 minutes', '2.5 minutes', '8 minutes'],
        ['5 నిమిషాలు', '10 నిమిషాలు', '2.5 నిమిషాలు', '8 నిమిషాలు'],
        0,
        """Formula: (M1 * T1) / W1 = (M2 * T2) / W2
(5 * 5) / 500 = (10 * T2) / 1000 => 25 / 500 = (10 * T2) / 1000 => 1 / 20 = T2 / 100 => T2 = 100 / 20 = 5 minutes.""",
        """సూత్రం: (M1 * T1) / W1 = (M2 * T2) / W2.
(5 * 5) / 500 = (10 * T2) / 1000 => 1/20 = T2/100 => T2 = 5 నిమిషాలు."""
    ))

    qs.append(make_q(
        81, "Pipes & Cisterns - Bottom Leak", "Medium",
        """An inlet pipe can fill a water tank in 8 hours. Due to a leak in the bottom of the tank, it now takes 10 hours to fill the tank completely. If the tank is completely full, in how many hours will the leak alone empty the tank?""",
        """ఒక ఇన్లెట్ పైపు ఒక నీటి తొట్టిని 8 గంటల్లో నింపగలదు. తొట్టి అడుగున ఒక లీక్ ఉండటం వల్ల, అది పూర్తిగా నిండటానికి 10 గంటలు పడుతుంది. తొట్టి పూర్తిగా నిండి ఉన్నప్పుడు, ఆ లీక్ ఒక్కటే తొట్టిని ఎన్ని గంటల్లో ఖాళీ చేస్తుంది?""",
        ['40 hours', '36 hours', '48 hours', '32 hours'],
        ['40 గంటలు', '36 గంటలు', '48 గంటలు', '32 గంటలు'],
        0,
        """Capacity = LCM(8, 10) = 40 units. Inlet rate = 40 / 8 = 5 units/hr.
Net rate with leak = 40 / 10 = 4 units/hr.
Leak rate = 5 - 4 = 1 unit/hr.
Time for leak alone to empty full tank = 40 / 1 = 40 hours.""",
        """సామర్థ్యం = 40 యూనిట్లు. ఇన్లెట్ వేగం = 5 యూనిట్లు/గం.
లీక్‌తో నికర వేగం = 4 యూనిట్లు/గం. లీక్ వేగం = 5 - 4 = 1 యూనిట్/గం.
లీక్ ఖాళీ చేయడానికి పట్టే కాలం = 40 / 1 = 40 గంటలు."""
    ))

    qs.append(make_q(
        82, "Pipes & Cisterns - Alternate Hours", "Hard",
        """Pipe A can fill a tank in 6 hours and Pipe B can fill it in 8 hours. Both pipes are opened alternately for 1 hour each, starting with Pipe A. In how many hours will the tank be completely filled?""",
        """పైప్ A ఒక తొట్టిని 6 గంటల్లో, పైప్ B 8 గంటల్లో నింపగలవు. పైప్ A తో ప్రారంభించి, రెండు పైపులను గంట మార్చి గంట తెరిచినట్లయితే, ఆ తొట్టి ఎన్ని గంటల్లో పూర్తిగా నిండుతుంది?""",
        ['6 hours 45 minutes', '7 hours', '6 hours 30 minutes', '7 hours 15 minutes'],
        ['6 గంటల 45 నిమిషాలు', '7 గంటలు', '6 గంటల 30 నిమిషాలు', '7 గంటల 15 నిమిషాలు'],
        0,
        """Total capacity = LCM(6, 8) = 24 units. Efficiency: A = 4, B = 3 units/hr.
Work in 2 hours (1 cycle) = 4 + 3 = 7 units.
In 3 cycles (6 hours), work done = 3 * 7 = 21 units.
Remaining work = 24 - 21 = 3 units.
On the 7th hour, Pipe A works: time taken = 3 / 4 hour = 45 minutes.
Total time = 6 hours + 45 minutes = 6 hours 45 minutes.""",
        """మొత్తం సామర్థ్యం = 24 యూనిట్లు. A = 4, B = 3 యూనిట్లు/గం.
2 గంటల్లో నిండేది = 7 యూనిట్లు. 3 సైకిల్స్ (6 గంటలు) లో = 21 యూనిట్లు.
మిగిలినది = 3 యూనిట్లు. 7వ గంటన పైప్ A కి పట్టే కాలం = 3/4 గంట = 45 నిమిషాలు.
మొత్తం సమయం = 6 గంటల 45 నిమిషాలు."""
    ))

    qs.append(make_q(
        83, "Pipes & Cisterns - Inlets and Outlet", "Medium",
        """Two pipes A and B can fill a cistern in 12 hours and 15 hours respectively, while an emptying pipe C can empty the full cistern in 20 hours. If all three pipes are opened together in an empty cistern, in how many hours will it be filled?""",
        """రెండు పైపులు A మరియు B లు ఒక తొట్టిని వరుసగా 12 గంటలు మరియు 15 గంటల్లో నింపగలవు, కాగా ఖాళీ చేసే పైప్ C నిండిన తొట్టిని 20 గంటల్లో ఖాళీ చేయగలదు. ఖాళీ తొట్టిలో మూడు పైపులను ఒకేసారి తెరిస్తే, అది ఎన్ని గంటల్లో నిండుతుంది?""",
        ['10 hours', '12 hours', '8 hours', '14 hours'],
        ['10 గంటలు', '12 గంటలు', '8 గంటలు', '14 గంటలు'],
        0,
        """Capacity = LCM(12, 15, 20) = 60 units.
A = +5 units/hr, B = +4 units/hr, C = -3 units/hr.
Net filling rate = 5 + 4 - 3 = 6 units/hr.
Time to fill = 60 / 6 = 10 hours.""",
        """మొత్తం సామర్థ్యం = 60 యూనిట్లు. A = +5, B = +4, C = -3 యూనిట్లు/గం.
నికర నింపే వేగం = 5 + 4 - 3 = 6 యూనిట్లు/గం.
పట్టే కాలం = 60 / 6 = 10 గంటలు."""
    ))

    qs.append(make_q(
        84, "Pipes & Cisterns - Flow Proportional to Diameter Squared", "Hard",
        """Three pipes of diameters 1 cm, 2 cm, and 3 cm are connected to a reservoir. The rate of water flow through each pipe is proportional to the square of its diameter. The largest pipe alone can fill the reservoir in 28 minutes. In how many minutes will all three pipes together fill the reservoir?""",
        """1 సెం.మీ, 2 సెం.మీ మరియు 3 సెం.మీ వ్యాసాలు గల మూడు పైపులు ఒక రిజర్వాయర్‌కు కలపబడ్డాయి. ప్రతి పైపు ద్వారా నీటి ప్రవాహం దాని వ్యాసం యొక్క వర్గానికి అనులోమానుపాతంలో ఉంటుంది. అతిపెద్ద పైపు ఒక్కటే రిజర్వాయర్‌ను 28 నిమిషాల్లో నింపగలదు. మూడు పైపులు కలిసి ఆ రిజర్వాయర్‌ను ఎన్ని నిమిషాల్లో నింపుతాయి?""",
        ['18 minutes', '20 minutes', '16 minutes', '21 minutes'],
        ['18 నిమిషాలు', '20 నిమిషాలు', '16 నిమిషాలు', '21 నిమిషాలు'],
        0,
        """Flow rate is proportional to d^2: Rate ratio = 1^2 : 2^2 : 3^2 = 1 : 4 : 9.
Largest pipe rate = 9 units/min. Time taken = 28 minutes.
Total reservoir volume = 9 * 28 = 252 units.
Combined flow rate of all 3 pipes = 1 + 4 + 9 = 14 units/min.
Time taken together = 252 / 14 = 18 minutes.""",
        """ప్రవాహ వేగం వ్యాసం వర్గానికి అనులోమానుపాతం: 1^2 : 2^2 : 3^2 = 1 : 4 : 9.
పెద్ద పైపు వేగం = 9 యూనిట్లు/నిమి. ఘనపరిమాణం = 9 * 28 = 252 యూనిట్లు.
మూడు పైపుల ఉమ్మడి వేగం = 1 + 4 + 9 = 14 యూనిట్లు/నిమి.
కలిసి పట్టే కాలం = 252 / 14 = 18 నిమిషాలు."""
    ))

    qs.append(make_q(
        85, "Pipes & Cisterns - Pipe Closed Mid-Way", "Medium",
        """Pipe A can fill a tank in 24 minutes and Pipe B can fill it in 32 minutes. Both pipes are opened together. After how many minutes should Pipe B be closed so that the tank is completely full in 18 minutes?""",
        """పైప్ A ఒక తొట్టిని 24 నిమిషాల్లో, పైప్ B 32 నిమిషాల్లో నింపగలవు. రెండు పైపులను ఒకేసారి తెరిచారు. తొట్టి సరిగ్గా 18 నిమిషాల్లో నిండాలంటే, ఎన్ని నిమిషాల తర్వాత పైప్ B ని మూసివేయాలి?""",
        ['8 minutes', '9 minutes', '6 minutes', '10 minutes'],
        ['8 నిమిషాలు', '9 నిమిషాలు', '6 నిమిషాలు', '10 నిమిషాలు'],
        0,
        """Capacity = LCM(24, 32) = 96 units. A = 4 units/min, B = 3 units/min.
Pipe A is kept open for the entire 18 minutes: Work done by A = 18 * 4 = 72 units.
Remaining work done by B = 96 - 72 = 24 units.
Time Pipe B was open = 24 / 3 = 8 minutes.""",
        """సామర్థ్యం = 96 యూనిట్లు. A = 4, B = 3 యూనిట్లు/నిమి.
పైప్ A మొత్తం 18 నిమిషాలు పనిచేస్తుంది: A చేసిన పని = 18 * 4 = 72 యూనిట్లు.
B చేయాల్సిన మిగిలిన పని = 96 - 72 = 24 యూనిట్లు.
B పనిచేసిన సమయం = 24 / 3 = 8 నిమిషాలు."""
    ))

    qs.append(make_q(
        86, "Pipes & Cisterns - Tank Capacity Calculation", "Hard",
        """A leak at the bottom of a cistern can empty the entire cistern in 8 hours. An inlet pipe is turned on which admits water at the rate of 6 litres per minute. When both the inlet and leak are active, the cistern is emptied in 12 hours. What is the capacity of the cistern?""",
        """ఒక తొట్టి అడుగున ఉన్న లీక్ పూర్తి తొట్టిని 8 గంటల్లో ఖాళీ చేయగలదు. నిమిషానికి 6 లీటర్ల నీటిని నింపే ఒక ఇన్లెట్ పైపును తెరిచారు. ఇన్లెట్ మరియు లీక్ రెండూ పనిచేస్తున్నప్పుడు, నిండిన తొట్టి 12 గంటల్లో ఖాళీ అవుతుంది. ఆ తొట్టి యొక్క సామర్థ్యం ఎంత?""",
        ['8,640 litres', '7,200 litres', '9,600 litres', '8,120 litres'],
        ['8,640 లీటర్లు', '7,200 లీటర్లు', '9,600 లీటర్లు', '8,120 లీటర్లు'],
        0,
        """Leak emptying rate = 1/8 tank/hour. Net emptying rate = 1/12 tank/hour.
Inlet filling rate = (1/8) - (1/12) = (3 - 2)/24 = 1/24 tank/hour.
This means the inlet alone can fill the tank in 24 hours.
Inlet flow rate = 6 litres/min = 6 * 60 = 360 litres/hour.
Capacity of tank = 24 hours * 360 litres/hour = 8,640 litres.""",
        """లీక్ వేగం = 1/8, నికర ఖాళీ వేగం = 1/12.
ఇన్లెట్ నింపే వేగం = 1/8 - 1/12 = 1/24 తొట్టి/గంట.
అంటే ఇన్లెట్ 24 గంటల్లో తొట్టిని నింపగలదు.
ఇన్లెట్ ప్రవాహం = 6 లీ/నిమి = 360 లీ/గంట.
తొట్టి సామర్థ్యం = 24 * 360 = 8,640 లీటర్లు."""
    ))

    qs.append(make_q(
        87, "Pipes & Cisterns - Waste Pipe Flow", "Hard",
        """Two pipes A and B can fill a cistern in 10 hours and 12 hours respectively. A waste pipe can empty water at 80 gallons per hour. When all three pipes are opened together, the empty cistern is filled in 20 hours. What is the capacity of the cistern?""",
        """రెండు పైపులు A మరియు B ఒక తొట్టిని వరుసగా 10 గంటలు మరియు 12 గంటల్లో నింపగలవు. ఒక వ్యర్థపు పైపు గంటకు 80 గ్యాలన్ల నీటిని ఖాళీ చేయగలదు. మూడు పైపులను ఒకేసారి తెరిస్తే ఖాళీ తొట్టి 20 గంటల్లో నిండుతుంది. ఆ తొట్టి సామర్థ్యం ఎంత?""",
        ['600 gallons', '720 gallons', '800 gallons', '540 gallons'],
        ['600 గ్యాలన్లు', '720 గ్యాలన్లు', '800 గ్యాలన్లు', '540 గ్యాలన్లు'],
        0,
        """Rate of waste pipe C: (1/10) + (1/12) - (1/C) = (1/20)
1/C = (1/10 + 1/12 - 1/20) = (6 + 5 - 3) / 60 = 8 / 60 = 2 / 15 tank/hour.
Time for waste pipe to empty full tank = 15 / 2 = 7.5 hours.
Capacity = 7.5 hours * 80 gallons/hour = 600 gallons.""",
        """వ్యర్థపు పైప్ C వేగం = 1/10 + 1/12 - 1/20 = 8/60 = 2/15 తొట్టి/గంట.
పూర్తి తొట్టిని ఖాళీ చేయడానికి పట్టే కాలం = 7.5 గంటలు.
సామర్థ్యం = 7.5 * 80 = 600 గ్యాలన్లు."""
    ))

    qs.append(make_q(
        88, "Pipes & Cisterns - Identical Taps Opened", "Medium",
        """A single tap can fill a tank in 6 hours. After half the tank is filled, 3 more identical taps are opened. What is the total time taken to fill the tank completely?""",
        """ఒక కుళాయి ఒక తొట్టిని 6 గంటల్లో నింపగలదు. తొట్టి సగం నిండిన తర్వాత, అదే సామర్థ్యం గల మరో 3 కుళాయిలను తెరిచారు. ఆ తొట్టి పూర్తిగా నిండటానికి పట్టే మొత్తం సమయం ఎంత?""",
        ['3 hours 45 minutes', '4 hours', '3 hours 30 minutes', '4 hours 15 minutes'],
        ['3 గంటల 45 నిమిషాలు', '4 గంటలు', '3 గంటల 30 నిమిషాలు', '4 గంటల 15 నిమిషాలు'],
        0,
        """Time to fill first half by 1 tap = 6 / 2 = 3 hours.
Remaining half = 3 hours of single tap work.
Now total taps = 1 + 3 = 4 taps.
Time to fill remaining half with 4 taps = 3 / 4 hours = 45 minutes.
Total time = 3 hours + 45 minutes = 3 hours 45 minutes.""",
        """మొదటి సగం నిండటానికి పట్టే సమయం = 3 గంటలు.
మిగిలిన సగానికి 4 కుళాయిలు కలవు: పట్టే కాలం = 3/4 గంట = 45 నిమిషాలు.
మొత్తం సమయం = 3 గంటల 45 నిమిషాలు."""
    ))

    qs.append(make_q(
        89, "Pipes & Cisterns - Inlet Closed Early", "Medium",
        """Pipes A and B can fill a tank in 20 minutes and 30 minutes respectively. Both pipes are opened together, but after 5 minutes, Pipe A is turned off. In how many additional minutes will Pipe B alone fill the rest of the tank?""",
        """పైపులు A మరియు B ఒక తొట్టిని వరుసగా 20 నిమిషాలు మరియు 30 నిమిషాల్లో నింపగలవు. రెండు పైపులను ఒకేసారి తెరిచారు, కానీ 5 నిమిషాల తర్వాత పైప్ A ని మూసివేశారు. మిగిలిన తొట్టిని నింపడానికి పైప్ B కి ఇంకా ఎన్ని అదనపు నిమిషాలు పడుతుంది?""",
        ['17.5 minutes', '15 minutes', '20 minutes', '18 minutes'],
        ['17.5 నిమిషాలు', '15 నిమిషాలు', '20 నిమిషాలు', '18 నిమిషాలు'],
        0,
        """Capacity = LCM(20, 30) = 60 units. A = 3 units/min, B = 2 units/min.
Work in first 5 minutes = 5 * (3 + 2) = 25 units.
Remaining work = 60 - 25 = 35 units.
Time taken by B alone = 35 / 2 = 17.5 minutes.""",
        """సామర్థ్యం = 60 యూనిట్లు. A = 3, B = 2 యూనిట్లు/నిమి.
మొదటి 5 నిమిషాల్లో నిండినది = 5 * 5 = 25 యూనిట్లు.
మిగిలినది = 35 యూనిట్లు. B కి పట్టే అదనపు సమయం = 35 / 2 = 17.5 నిమిషాలు."""
    ))

    qs.append(make_q(
        90, "Pipes & Cisterns - Sequential Pipe Closure", "Hard",
        """Pipe A and Pipe B can fill a cistern in 15 hours and 20 hours respectively, while Pipe C empties it in 25 hours. All three pipes are opened together, but Pipe C is closed after 10 hours. What is the total time taken to fill the cistern?""",
        """పైప్ A మరియు B లు ఒక తొట్టిని వరుసగా 15 గంటలు మరియు 20 గంటల్లో నింపగలవు, పైప్ C దానిని 25 గంటల్లో ఖాళీ చేయగలదు. మూడు పైపులను ఒకేసారి తెరిచారు, కానీ 10 గంటల తర్వాత పైప్ C ని మూసివేశారు. ఆ తొట్టి నిండటానికి పట్టిన మొత్తం సమయం ఎంత?""",
        ['12 hours', '14 hours', '11.5 hours', '13 hours'],
        ['12 గంటలు', '14 గంటలు', '11.5 గంటలు', '13 గంటలు'],
        0,
        """Capacity = LCM(15, 20, 25) = 300 units. A = 20, B = 15, C = -12 units/hr.
In first 10 hours with all three open: Work = 10 * (20 + 15 - 12) = 10 * 23 = 230 units.
Remaining work = 300 - 230 = 70 units.
Now only A and B work: Combined rate = 20 + 15 = 35 units/hr.
Time for remaining work = 70 / 35 = 2 hours.
Total time = 10 + 2 = 12 hours.""",
        """సామర్థ్యం = 300 యూనిట్లు. A = 20, B = 15, C = -12 యూనిట్లు/గం.
మొదటి 10 గంటల్లో నిండినది = 10 * 23 = 230 యూనిట్లు.
మిగిలిన పని = 70 యూనిట్లు. A మరియు B ల వేగం = 35 యూనిట్లు/గం.
మిగిలిన దానికి పట్టే కాలం = 70 / 35 = 2 గంటలు. మొత్తం కాలం = 10 + 2 = 12 గంటలు."""
    ))

    qs.append(make_q(
        91, "Pipes & Cisterns - Relative Speed Difference", "Medium",
        """Two pipes together can fill a reservoir in 6 hours. One pipe fills the reservoir 5 hours faster than the other. How many hours does the faster pipe alone take to fill the reservoir?""",
        """రెండు పైపులు కలిసి ఒక రిజర్వాయర్‌ను 6 గంటల్లో నింపగలవు. ఒక పైపు మరొకదాని కంటే 5 గంటలు వేగంగా నింపగలదు. వేగవంతమైన పైపు ఒక్కటే రిజర్వాయర్‌ను ఎన్ని గంటల్లో నింపగలదు?""",
        ['10 hours', '12 hours', '8 hours', '15 hours'],
        ['10 గంటలు', '12 గంటలు', '8 గంటలు', '15 గంటలు'],
        0,
        """Let faster pipe take t hours; slower pipe takes (t + 5) hours.
1/t + 1/(t + 5) = 1/6 => (2t + 5) / (t^2 + 5t) = 1/6 => 12t + 30 = t^2 + 5t => t^2 - 7t - 30 = 0.
(t - 10)(t + 3) = 0 => t = 10 hours.""",
        """వేగవంతమైన పైపు t గంటలు అనుకుంటే, 1/t + 1/(t+5) = 1/6.
t^2 - 7t - 30 = 0 => t = 10 గంటలు."""
    ))

    qs.append(make_q(
        92, "Pipes & Cisterns - Staggered Opening & Emptying", "Hard",
        """Pipes A and B can fill a cistern in 15 hours and 12 hours respectively, while pipe C can empty it in 4 hours. The pipes are opened in order at 8:00 AM, 9:00 AM, and 11:00 AM respectively. At what time will the cistern be completely empty?""",
        """పైపులు A మరియు B ఒక తొట్టిని వరుసగా 15 గంటలు మరియు 12 గంటల్లో నింపగలవు, పైప్ C దానిని 4 గంటల్లో ఖాళీ చేయగలదు. ఉదయం 8:00 గంటలకు A, 9:00 గంటలకు B, 11:00 గంటలకు C క్రమంగా తెరవబడ్డాయి. తొట్టి ఏ సమయానికి పూర్తిగా ఖాళీ అవుతుంది?""",
        ['2:40 PM', '2:20 PM', '3:00 PM', '1:50 PM'],
        ['మధ్యాహ్నం 2:40', 'మధ్యాహ్నం 2:20', 'మధ్యాహ్నం 3:00', 'మధ్యాహ్నం 1:50'],
        0,
        """Capacity = LCM(15, 12, 4) = 60 units. Rates: A = +4, B = +5, C = -15 units/hr.
By 11:00 AM:
Pipe A ran for 3 hrs (8 AM to 11 AM) = 3 * 4 = 12 units.
Pipe B ran for 2 hrs (9 AM to 11 AM) = 2 * 5 = 10 units.
Total filled by 11:00 AM = 12 + 10 = 22 units.
After 11:00 AM, all 3 pipes are open: Net rate = 4 + 5 - 15 = -6 units/hr (net emptying).
Time to empty the 22 units = 22 / 6 = 3 2/3 hours = 3 hours 40 minutes.
Time = 11:00 AM + 3 hours 40 minutes = 2:40 PM.""",
        """సామర్థ్యం = 60 యూనిట్లు. A = +4, B = +5, C = -15.
ఉదయం 11:00 గంటల వరకు నిండిన నీరు = (3 * 4) + (2 * 5) = 22 యూనిట్లు.
11:00 తర్వాత నికర వేగం = 4 + 5 - 15 = -6 యూనిట్లు/గం (ఖాళీ అవుతుంది).
ఖాళీ కావడానికి పట్టే కాలం = 22 / 6 = 3 గంటల 40 నిమిషాలు.
సమయం = 11:00 AM + 3 గం 40 నిమి = మధ్యాహ్నం 2:40."""
    ))

    qs.append(make_q(
        93, "Pipes & Cisterns - Pumps and Work Formula", "Medium",
        """12 identical pumps working 7 hours a day can lift 2,800 tonnes of water in 20 days. How many days will 14 identical pumps working 6 hours a day take to lift 2,520 tonnes of water?""",
        """రోజుకు 7 గంటలు పనిచేస్తూ 12 పంపులు 20 రోజుల్లో 2,800 టన్నుల నీటిని తోడగలవు. రోజుకు 6 గంటలు పనిచేస్తూ 14 పంపులు 2,520 టన్నుల నీటిని తోడటానికి ఎన్ని రోజులు పడుతుంది?""",
        ['18 days', '16 days', '20 days', '15 days'],
        ['18 రోజులు', '16 రోజులు', '20 రోజులు', '15 రోజులు'],
        0,
        """Formula: (P1 * D1 * H1) / W1 = (P2 * D2 * H2) / W2
(12 * 20 * 7) / 2800 = (14 * D2 * 6) / 2520
1680 / 2800 = (84 * D2) / 2520 => 0.6 = (84 * D2) / 2520 => 84 * D2 = 1512 => D2 = 18 days.""",
        """సూత్రం: (P1 * D1 * H1) / W1 = (P2 * D2 * H2) / W2.
(12 * 20 * 7) / 2800 = (14 * D2 * 6) / 2520 => 0.6 = 84*D2 / 2520 => D2 = 18 రోజులు."""
    ))

    qs.append(make_q(
        94, "Pipes & Cisterns - Bucket Capacity Transfer", "Medium",
        """A water tank is completely filled by 12 buckets of water when each bucket holds 13.5 litres. How many buckets will be needed to fill the same tank if the capacity of each bucket is 9 litres?""",
        """ఒక్కొక్కటి 13.5 లీటర్ల సామర్థ్యం గల 12 బకెట్ల నీటితో ఒక తొట్టి పూర్తిగా నిండుతుంది. ప్రతి బకెట్ సామర్థ్యం 9 లీటర్లు అయితే, అదే తొట్టిని నింపడానికి ఎన్ని బకెట్లు అవసరం?""",
        ['18 buckets', '16 buckets', '20 buckets', '15 buckets'],
        ['18 బకెట్లు', '16 బకెట్లు', '20 బకెట్లు', '15 బకెట్లు'],
        0,
        """Total capacity of the tank = 12 * 13.5 = 162 litres.
Number of 9-litre buckets required = 162 / 9 = 18 buckets.""",
        """తొట్టి మొత్తం సామర్థ్యం = 12 * 13.5 = 162 లీటర్లు.
కావలసిన 9 లీటర్ల బకెట్ల సంఖ్య = 162 / 9 = 18 బకెట్లు."""
    ))

    qs.append(make_q(
        95, "Pipes & Cisterns - Speed Multiple", "Medium",
        """Pipe A fills a tank 3 times faster than Pipe B. If together they can fill the tank in 36 minutes, how many minutes will the slower Pipe B alone take to fill the tank?""",
        """పైప్ A ఒక తొట్టిని పైప్ B కంటే 3 రెట్లు వేగంగా నింపగలదు. రెండు పైపులు కలిసి ఆ తొట్టిని 36 నిమిషాల్లో నింపగలిగితే, నెమ్మదిగా ఉండే పైప్ B ఒక్కటే ఆ తొట్టిని ఎన్ని నిమిషాల్లో నింపగలదు?""",
        ['144 minutes', '108 minutes', '120 minutes', '160 minutes'],
        ['144 నిమిషాలు', '108 నిమిషాలు', '120 నిమిషాలు', '160 నిమిషాలు'],
        0,
        """Ratio of rates A : B = 3 : 1. Combined rate = 3 + 1 = 4 units/min.
Total tank capacity = 4 * 36 = 144 units.
Time taken by Pipe B alone = 144 / 1 = 144 minutes.""",
        """సామర్థ్యాల నిష్పత్తి A : B = 3 : 1. ఉమ్మడి వేగం = 4 యూనిట్లు/నిమి.
మొత్తం సామర్థ్యం = 4 * 36 = 144 యూనిట్లు.
పైప్ B కి పట్టే కాలం = 144 / 1 = 144 నిమిషాలు."""
    ))

    qs.append(make_q(
        96, "Profit, Loss & Discount - Dishonest Dealer Weight", "Medium",
        """A dishonest trader professes to sell his goods at cost price, but uses a false weight of 900 grams for a 1 kg weight. What is his actual profit percentage?""",
        """ఒక వ్యాపారి తన వస్తువులను కొన్న ధరకే విక్రయిస్తున్నట్లు నటిస్తూ, 1 కి.గ్రా తూకానికి బదులుగా 900 గ్రాముల తప్పుడు తూకాన్ని ఉపయోగిస్తున్నాడు. అతని వాస్తవ లాభ శాతం ఎంత?""",
        ['11 1/9%', '10%', '12 1/2%', '9 1/11%'],
        ['11 1/9%', '10%', '12 1/2%', '9 1/11%'],
        0,
        """Profit % = [Error / (True Value - Error)] * 100
Profit % = [100 / (1000 - 100)] * 100 = (100 / 900) * 100 = 100 / 9 = 11 1/9%.""",
        """లాభ శాతం = [లోపం / తప్పుడు తూకం] * 100 = (100 / 900) * 100 = 11 1/9%."""
    ))

    qs.append(make_q(
        97, "Profit, Loss & Discount - Markup, Discount & False Weight", "Hard",
        """A merchant marks his goods 20% above the cost price and allows a discount of 10% on the marked price. In addition, he cheats the customer by using a false weight of 900 grams instead of 1 kg. What is his overall profit percentage?""",
        """ఒక వ్యాపారి తన వస్తువులను కొన్న ధర కంటే 20% అధికంగా ప్రకటించి, ప్రకటిత ధరపై 10% తగ్గింపును ఇస్తాడు. అదనంగా, 1 కి.గ్రా కు బదులుగా 900 గ్రాముల తప్పుడు తూకాన్ని ఉపయోగిస్తాడు. అతని మొత్తం లాభ శాతం ఎంత?""",
        ['20%', '22%', '18%', '25%'],
        ['20%', '22%', '18%', '25%'],
        0,
        """Let CP of 1,000 g = Rs. 1,000.
Trader sells 900 g, so his actual CP = Rs. 900.
Marked price for 1,000 g = Rs. 1,200. With 10% discount, selling price SP = 1200 * 0.90 = Rs. 1,080.
Customer pays Rs. 1,080 for goods costing the trader Rs. 900.
Profit = 1080 - 900 = Rs. 180.
Profit % = (180 / 900) * 100 = 20%.""",
        """1,000 గ్రాముల కొన్న ధర = రూ. 1,000 అనుకుందాం.
అతను ఇచ్చే 900 గ్రాముల అసలు ధర = రూ. 900.
ప్రకటిత ధర = రూ. 1,200; 10% తగ్గింపు తర్వాత అమ్మకపు ధర = రూ. 1,080.
లాభం = 1080 - 900 = రూ. 180.
లాభ శాతం = (180 / 900) * 100 = 20%."""
    ))

    qs.append(make_q(
        98, "Profit, Loss & Discount - Same SP Profit and Loss", "Medium",
        """Two police patrol motorcycles were sold for Rs. 99,000 each. On one motorcycle, the dealer gained 10%, while on the other, he incurred a loss of 10%. What was his overall profit or loss percentage and net rupee change?""",
        """రెండు పోలీస్ పెట్రోలింగ్ మోటార్‌సైకిళ్లను ఒక్కొక్కటి రూ. 99,000 చొప్పున విక్రయించారు. ఒకదానిపై 10% లాభం, మరొకదానిపై 10% నష్టం వచ్చింది. మొత్తం లావాదేవీలో లాభ/నష్ట శాతం మరియు నికర నష్టం ఎంత?""",
        ['1% Loss, Net Loss = Rs. 2,000', 'No Profit No Loss, Rs. 0', '1% Profit, Net Gain = Rs. 2,000', '2% Loss, Net Loss = Rs. 4,000'],
        ['1% నష్టం, నికర నష్టం = రూ. 2,000', 'లాభమూ లేదు నష్టమూ లేదు, రూ. 0', '1% లాభం, నికర లాభం = రూ. 2,000', '2% నష్టం, నికర నష్టం = రూ. 4,000'],
        0,
        """When SP is same for both articles with x% gain and x% loss:
Overall Loss % = (x / 10)^2 = (10 / 10)^2 = 1% loss.
Total SP = 2 * 99,000 = Rs. 198,000.
Total CP = 198,000 / (1 - 0.01) = 198,000 / 0.99 = Rs. 200,000.
Net Loss in Rupees = 200,000 - 198,000 = Rs. 2,000.""",
        """అమ్మకపు ధర సమానమై x% లాభం, x% నష్టం వచ్చినప్పుడు:
మొత్తం నష్ట శాతం = (x/10)^2 = 1% నష్టం.
మొత్తం అమ్మకపు ధర = రూ. 1,98,000. కొన్న ధర = రూ. 2,00,000.
రూపాయలలో నష్టం = రూ. 2,000."""
    ))

    qs.append(make_q(
        99, "Profit, Loss & Discount - Three Successive Discounts", "Medium",
        """What single discount is equivalent to three successive discounts of 20%, 15%, and 10%?""",
        """20%, 15% మరియు 10% ల మూడు వరుస తగ్గింపులకు సమానమైన ఒకే తగ్గింపు (Single Discount) ఎంత?""",
        ['38.8%', '45.0%', '36.5%', '40.2%'],
        ['38.8%', '45.0%', '36.5%', '40.2%'],
        0,
        """Net multiplier = (1 - 0.20) * (1 - 0.15) * (1 - 0.10) = 0.80 * 0.85 * 0.90
0.80 * 0.85 = 0.68; 0.68 * 0.90 = 0.612.
Equivalent Single Discount = (1 - 0.612) * 100 = 38.8%.""",
        """నికర గుణకం = 0.80 * 0.85 * 0.90 = 0.612.
సమానమైన ఒకే తగ్గింపు = (1 - 0.612) * 100 = 38.8%."""
    ))

    qs.append(make_q(
        100, "Profit, Loss & Discount - Markup and Discount Profit", "Medium",
        """A trader marks his goods 40% above the cost price and allows a discount of 25% on the marked price. What is his net profit percentage?""",
        """ఒక వ్యాపారి తన వస్తువులపై కొన్న ధర కంటే 40% అధికంగా ధరను ప్రకటించి, ఆ ప్రకటిత ధరపై 25% తగ్గింపును ఇచ్చాడు. అతని నికర లాభ శాతం ఎంత?""",
        ['5%', '15%', '10%', '8%'],
        ['5%', '15%', '10%', '8%'],
        0,
        """Let CP = 100. MP = 140.
SP = 140 * (1 - 0.25) = 140 * 0.75 = 105.
Profit % = 105 - 100 = 5%.""",
        """కొన్న ధర CP = 100 అనుకుంటే, ప్రకటిత ధర MP = 140.
అమ్మకపు ధర SP = 140 * 0.75 = 105.
లాభ శాతం = 105 - 100 = 5%."""
    ))

    qs.append(make_q(
        101, "Profit, Loss & Discount - SP of Articles Gain", "Medium",
        """By selling 33 metres of uniform cloth, a merchant gains the selling price of 11 metres of cloth. What is his gain percentage?""",
        """33 మీటర్ల యూనిఫాం వస్త్రాన్ని విక్రయించడం ద్వారా, ఒక వ్యాపారి 11 మీటర్ల వస్త్రం యొక్క అమ్మకపు ధరకు సమానమైన లాభాన్ని పొందాడు. అతని లాభ శాతం ఎంత?""",
        ['50%', '33 1/3%', '25%', '40%'],
        ['50%', '33 1/3%', '25%', '40%'],
        0,
        """Gain = SP of 11 m = SP of 33 m - CP of 33 m
=> CP of 33 m = SP of 22 m => SP / CP = 33 / 22 = 3 / 2.
Gain % = [(3 - 2) / 2] * 100 = 1/2 * 100 = 50%.""",
        """లాభం = 11 మీటర్ల SP = 33 మీటర్ల SP - 33 మీటర్ల CP.
33 CP = 22 SP => SP / CP = 3 / 2.
లాభ శాతం = (1/2) * 100 = 50%."""
    ))

    qs.append(make_q(
        102, "Profit, Loss & Discount - CP of X = SP of Y", "Medium",
        """If the cost price of 16 articles is equal to the selling price of 12 articles, what is the profit percentage earned?""",
        """16 వస్తువుల కొన్న ధర 12 వస్తువుల అమ్మకపు ధరకు సమానమైతే, లభించిన లాభ శాతం ఎంత?""",
        ['33 1/3%', '25%', '30%', '20%'],
        ['33 1/3%', '25%', '30%', '20%'],
        0,
        """16 * CP = 12 * SP => SP / CP = 16 / 12 = 4 / 3.
Profit % = [(SP - CP) / CP] * 100 = [(4 - 3) / 3] * 100 = 100 / 3 = 33 1/3%.""",
        """16 CP = 12 SP => SP / CP = 4 / 3.
లాభ శాతం = (1/3) * 100 = 33 1/3%."""
    ))

    qs.append(make_q(
        103, "Profit, Loss & Discount - Buy X Get Y Free", "Medium",
        """A police departmental store offers a special promotional scheme: "Buy 4 Get 1 Free". What is the effective discount percentage offered to the customer?""",
        """ఒక పోలీస్ డిపార్ట్‌మెంటల్ స్టోర్ "4 కొనండి 1 ఉచితంగా పొందండి" (Buy 4 Get 1 Free) అనే ఆఫర్‌ను ప్రకటించింది. కస్టమర్‌కు లభించే ప్రభావవంతమైన తగ్గింపు (Effective Discount) శాతం ఎంత?""",
        ['20%', '25%', '16 2/3%', '22.5%'],
        ['20%', '25%', '16 2/3%', '22.5%'],
        0,
        """Discount % = [Free Articles / Total Articles Received] * 100
Total articles received = 4 + 1 = 5.
Effective Discount % = (1 / 5) * 100 = 20%.""",
        """తగ్గింపు శాతం = [ఉచిత వస్తువులు / మొత్తం పొందిన వస్తువులు] * 100.
మొత్తం వస్తువులు = 4 + 1 = 5.
తగ్గింపు శాతం = (1 / 5) * 100 = 20%."""
    ))

    qs.append(make_q(
        104, "Profit, Loss & Discount - Faulty Meter Scale", "Medium",
        """A cloth merchant uses a measuring meter rod of length 90 cm while selling cloth, claiming to sell the cloth at cost price. What is his percentage profit?""",
        """ఒక వస్త్ర వ్యాపారి కొన్న ధరకే బట్టను అమ్ముతున్నానని చెబుతూ, మీటరుకు బదులుగా 90 సెం.మీ కొలత గల స్కేలును ఉపయోగిస్తున్నాడు. అతని లాభ శాతం ఎంత?""",
        ['11 1/9%', '10%', '12 1/2%', '9 1/11%'],
        ['11 1/9%', '10%', '12 1/2%', '9 1/11%'],
        0,
        """Actual goods delivered = 90 cm; Claimed goods charged for = 100 cm.
Error = 10 cm.
Profit % = (10 / 90) * 100 = 100 / 9 = 11 1/9%.""",
        """లాభ శాతం = (లోపం / వాస్తవ కొలత) * 100 = (10 / 90) * 100 = 11 1/9%."""
    ))

    qs.append(make_q(
        105, "Profit, Loss & Discount - Fraction of SP", "Hard",
        """By selling an article at 2/3 of its original selling price, a trader incurs a loss of 10%. What would be the profit percentage if the article were sold at its original selling price?""",
        """ఒక వస్తువును దాని అసలు అమ్మకపు ధరలో 2/3 వంతు ధరకు విక్రయించడం వల్ల ఒక వ్యాపారికి 10% నష్టం వాటిల్లింది. ఆ వస్తువును దాని అసలు అమ్మకపు ధరకే విక్రయిస్తే వచ్చే లాభ శాతం ఎంత?""",
        ['35%', '30%', '25%', '40%'],
        ['35%', '30%', '25%', '40%'],
        0,
        """Let CP = 100. Selling at 2/3 of SP gives 10% loss => (2/3) * SP = 90
=> Original SP = 90 * (3 / 2) = 135.
When sold at original SP (135), Profit % = 135 - 100 = 35%.""",
        """కొన్న ధర = 100 అనుకుంటే, (2/3) * SP = 90 => అసలు SP = 135.
అసలు ధరకు విక్రయిస్తే లాభ శాతం = 135 - 100 = 35%."""
    ))

    qs.append(make_q(
        106, "Profit, Loss & Discount - Finding Marked Price", "Medium",
        """A trader wants to earn a 20% profit on an article after allowing a discount of 10% on the marked price. If the cost price of the article is Rs. 450, what should be its marked price?""",
        """ఒక వ్యాపారి ప్రకటిత ధరపై 10% తగ్గింపు ఇచ్చిన తర్వాత కూడా 20% లాభం పొందాలనుకుంటున్నాడు. ఆ వస్తువు కొన్న ధర రూ. 450 అయితే, దాని ప్రకటిత ధర ఎంత ఉండాలి?""",
        ['Rs. 600', 'Rs. 580', 'Rs. 620', 'Rs. 550'],
        ['రూ. 600', 'రూ. 580', 'రూ. 620', 'రూ. 550'],
        0,
        """Required SP = CP * 1.20 = 450 * 1.20 = Rs. 540.
Discount = 10% => SP = 0.90 * MP
0.90 * MP = 540 => MP = 540 / 0.90 = Rs. 600.""",
        """కావలసిన అమ్మకపు ధర SP = 450 * 1.20 = రూ. 540.
0.90 * MP = 540 => ప్రకటిత ధర MP = రూ. 600."""
    ))

    qs.append(make_q(
        107, "Profit, Loss & Discount - Two Articles SP Given", "Hard",
        """A merchant sells two items for Rs. 1,200 each. On the first item, he makes a profit of 20%, and on the second item, he incurs a loss of 25%. What is his overall loss percentage on the entire transaction?""",
        """ఒక వ్యాపారి రెండు వస్తువులను ఒక్కొక్కటి రూ. 1,200 చొప్పున విక్రయిస్తాడు. మొదటి వస్తువుపై 20% లాభం, రెండవ వస్తువుపై 25% నష్టం వచ్చింది. మొత్తం లావాదేవీపై అతని నికర నష్ట శాతం ఎంత?""",
        ['7 9/13% Loss', '8% Loss', '6 2/3% Loss', '5 5/13% Loss'],
        ['7 9/13% నష్టం', '8% నష్టం', '6 2/3% నష్టం', '5 5/13% నష్టం'],
        0,
        """CP of first item = 1,200 / 1.20 = Rs. 1,000.
CP of second item = 1,200 / 0.75 = Rs. 1,600.
Total CP = 1,000 + 1,600 = Rs. 2,600.
Total SP = 2 * 1,200 = Rs. 2,400.
Total Loss = 2,600 - 2,400 = Rs. 200.
Loss % = (200 / 2,600) * 100 = 20 / 2.6 = 100 / 13 = 7 9/13% Loss.""",
        """మొదటి వస్తువు CP = రూ. 1,000; రెండవ వస్తువు CP = రూ. 1,600.
మొత్తం CP = రూ. 2,600. మొత్తం SP = రూ. 2,400.
మొత్తం నష్టం = రూ. 200. నష్ట శాతం = (200 / 2600) * 100 = 100 / 13 = 7 9/13% నష్టం."""
    ))

    qs.append(make_q(
        108, "Profit, Loss & Discount - Water in Milk Ratio", "Medium",
        """A milk vendor purchases pure milk at Rs. 24 per litre. He adds water to it and sells the resulting mixture at the same cost price of Rs. 24 per litre, thereby earning a profit of 25%. What is the ratio of water to pure milk in the mixture?""",
        """ఒక పాల వ్యాపారి లీటరుకు రూ. 24 చొప్పున స్వచ్ఛమైన పాలను కొంటాడు. అతడు అందులో నీటిని కలిపి, ఆ మిశ్రమాన్ని కూడా లీటరుకు రూ. 24 కే అమ్ముతూ 25% లాభం పొందుతాడు. ఆ మిశ్రమంలో నీరు మరియు స్వచ్ఛమైన పాల నిష్పత్తి ఎంత?""",
        ['1 : 4', '1 : 5', '1 : 3', '2 : 5'],
        ['1 : 4', '1 : 5', '1 : 3', '2 : 5'],
        0,
        """When mixture is sold at the cost price of pure liquid:
Profit % = (Quantity of free water / Quantity of pure milk) * 100
25 = (W / M) * 100 => W / M = 25 / 100 = 1 / 4 => Ratio = 1 : 4.""",
        """కొన్న ధరకే విక్రయించినప్పుడు: లాభ శాతం = (నీరు / పాలు) * 100.
25 = (W / M) * 100 => W / M = 1 / 4. నిష్పత్తి = 1 : 4."""
    ))

    qs.append(make_q(
        109, "Profit, Loss & Discount - Second Discount Percentage", "Hard",
        """The marked price of an electronic tablet is Rs. 1,600. After allowing two successive discounts, a customer pays Rs. 1,224. If the first discount is 10%, what is the percentage of the second discount?""",
        """ఒక ఎలక్ట్రానిక్ టాబ్లెట్ ప్రకటిత ధర రూ. 1,600. రెండు వరుస తగ్గింపుల తర్వాత ఒక కస్టమర్ రూ. 1,224 చెల్లించాడు. మొదటి తగ్గింపు 10% అయితే, రెండవ తగ్గింపు శాతం ఎంత?""",
        ['15%', '12%', '18%', '14%'],
        ['15%', '12%', '18%', '14%'],
        0,
        """Price after first discount (10%) = 1,600 * (1 - 0.10) = Rs. 1,440.
Final selling price = Rs. 1,224.
Second discount amount = 1,440 - 1,224 = Rs. 216.
Second discount % = (216 / 1,440) * 100 = 15%.""",
        """మొదటి తగ్గింపు (10%) తర్వాత ధర = 1,600 * 0.90 = రూ. 1,440.
రెండవ తగ్గింపు మొత్తం = 1,440 - 1,224 = రూ. 216.
రెండవ తగ్గింపు శాతం = (216 / 1440) * 100 = 15%."""
    ))

    qs.append(make_q(
        110, "Profit, Loss & Discount - Chain of Intermediaries", "Hard",
        """A manufacturer sells an equipment to a wholesaler at 10% profit. The wholesaler sells it to a retailer at 15% profit, and the retailer sells it to the end consumer at 25% profit. If the consumer pays Rs. 1,265, what was the original manufacturing cost?""",
        """ఒక తయారీదారు ఒక పరికరాన్ని హోల్‌సేలర్‌కు 10% లాభానికి అమ్ముతాడు. హోల్‌సేలర్ దానిని రిటైలర్‌కు 15% లాభానికి, రిటైలర్ వినియోగదారునికి 25% లాభానికి విక్రయిస్తారు. వినియోగదారుడు రూ. 1,265 చెల్లించినట్లయితే, అసలు తయారీ ఖర్చు ఎంత?""",
        ['Rs. 800', 'Rs. 750', 'Rs. 850', 'Rs. 900'],
        ['రూ. 800', 'రూ. 750', 'రూ. 850', 'రూ. 900'],
        0,
        """Let manufacturing cost be C.
C * 1.10 * 1.15 * 1.25 = 1,265
C * (11/10) * (23/20) * (5/4) = 1,265 => C * (1,265 / 800) = 1,265 => C = Rs. 800.""",
        """తయారీ ఖర్చు C అనుకుంటే: C * (11/10) * (23/20) * (5/4) = 1,265.
C * (1265 / 800) = 1265 => C = రూ. 800."""
    ))

    qs.append(make_q(
        111, "Simple & Compound Interest - 2-Year Difference", "Medium",
        """What is the difference between compound interest and simple interest on a principal of Rs. 15,000 for 2 years at an interest rate of 8% per annum?""",
        """రూ. 15,000 అసలుపై సంవత్సరానికి 8% వడ్డీ రేటు చొప్పున 2 సంవత్సరాలకు అయ్యే చక్రవడ్డీ మరియు బారువడ్డీల మధ్య తేడా ఎంత?""",
        ['Rs. 96', 'Rs. 90', 'Rs. 104', 'Rs. 88'],
        ['రూ. 96', 'రూ. 90', 'రూ. 104', 'రూ. 88'],
        0,
        """Formula for 2-year difference: CI - SI = P * (R / 100)^2
Difference = 15,000 * (8 / 100)^2 = 15,000 * (64 / 10,000) = 1.5 * 64 = Rs. 96.""",
        """2 సంవత్సరాల తేడా సూత్రం: CI - SI = P * (R / 100)^2.
తేడా = 15,000 * (64 / 10,000) = రూ. 96."""
    ))

    qs.append(make_q(
        112, "Simple & Compound Interest - 3-Year Difference", "Hard",
        """The difference between compound interest and simple interest on a sum of Rs. 10,000 for 3 years at 10% per annum is:""",
        """రూ. 10,000 అసలుపై 10% వార్షిక వడ్డీ రేటుతో 3 సంవత్సరాలకు అయ్యే చక్రవడ్డీ మరియు బారువడ్డీల మధ్య వ్యత్యాసం ఎంత?""",
        ['Rs. 310', 'Rs. 300', 'Rs. 325', 'Rs. 280'],
        ['రూ. 310', 'రూ. 300', 'రూ. 325', 'రూ. 280'],
        0,
        """Formula for 3-year difference: CI - SI = P * (R / 100)^2 * [3 + (R / 100)]
Difference = 10,000 * (10 / 100)^2 * [3 + 0.10] = 10,000 * (1 / 100) * 3.1 = 100 * 3.1 = Rs. 310.""",
        """3 సంవత్సరాల తేడా సూత్రం: CI - SI = P * (R / 100)^2 * [3 + (R / 100)].
తేడా = 10,000 * 0.01 * 3.1 = రూ. 310."""
    ))

    qs.append(make_q(
        113, "Simple & Compound Interest - Consecutive Amounts", "Medium",
        """A sum of money invested at compound interest amounts to Rs. 4,840 in 2 years and to Rs. 5,324 in 3 years. What is the annual rate of interest?""",
        """చక్రవడ్డీ రేటుతో పెట్టుబడి పెట్టిన ఒక మొత్తం 2 సంవత్సరాలలో రూ. 4,840 మరియు 3 సంవత్సరాలలో రూ. 5,324 అవుతుంది. వార్షిక వడ్డీ రేటు ఎంత?""",
        ['10%', '12%', '8%', '9%'],
        ['10%', '12%', '8%', '9%'],
        0,
        """Interest for the 3rd year = Amount(3 yrs) - Amount(2 yrs) = 5,324 - 4,840 = Rs. 484.
Rate R = (Interest / Principal for that year) * 100 = (484 / 4,840) * 100 = 10% per annum.""",
        """3వ సంవత్సరపు వడ్డీ = 5,324 - 4,840 = రూ. 484.
వడ్డీ రేటు R = (484 / 4,840) * 100 = 10%."""
    ))

    qs.append(make_q(
        114, "Simple & Compound Interest - Doubling Formula", "Medium",
        """A sum of money invested at compound interest doubles itself in 5 years. In how many years will it become 8 times its original value at the same interest rate?""",
        """చక్రవడ్డీ వద్ద ఒక మొత్తం 5 సంవత్సరాలలో రెట్టింపు అవుతుంది. అదే వడ్డీ రేటుతో అది 8 రెట్లు కావడానికి ఎన్ని సంవత్సరాలు పడుతుంది?""",
        ['15 years', '20 years', '25 years', '12 years'],
        ['15 సంవత్సరాలు', '20 సంవత్సరాలు', '25 సంవత్సరాలు', '12 సంవత్సరాలు'],
        0,
        """At CI, if a sum becomes 2^1 times in 5 years, it becomes 2^n times in (n * 5) years.
Here 8 = 2^3 => n = 3.
Time required = 3 * 5 = 15 years.""",
        """చక్రవడ్డీ వద్ద: 2^1 రెట్లు కావడానికి 5 సంవత్సరాలు పడితే, 8 రెట్లు (2^3) కావడానికి = 3 * 5 = 15 సంవత్సరాలు పడుతుంది."""
    ))

    qs.append(make_q(
        115, "Simple & Compound Interest - Half-Yearly Compounding", "Medium",
        """What is the compound interest on a principal of Rs. 8,000 for 1 year at 10% per annum, compounded half-yearly?""",
        """రూ. 8,000 అసలుపై 10% వార్షిక వడ్డీ రేటు చొప్పున అర్థ సంవత్సరానికి ఒకసారి చక్రవడ్డీ లెక్కించినప్పుడు 1 సంవత్సరానికి అయ్యే చక్రవడ్డీ ఎంత?""",
        ['Rs. 820', 'Rs. 800', 'Rs. 840', 'Rs. 810'],
        ['రూ. 820', 'రూ. 800', 'రూ. 840', 'రూ. 810'],
        0,
        """Half-yearly rate r = 10% / 2 = 5%. Periods n = 1 * 2 = 2.
Amount = 8,000 * (1 + 0.05)^2 = 8,000 * 1.1025 = Rs. 8,820.
Compound Interest = 8,820 - 8,000 = Rs. 820.""",
        """అర్థ సంవత్సర వడ్డీ రేటు = 5%, n = 2.
మొత్తం = 8,000 * (1.05)^2 = రూ. 8,820.
చక్రవడ్డీ = 8,820 - 8,000 = రూ. 820."""
    ))

    qs.append(make_q(
        116, "Simple & Compound Interest - Doubling at SI", "Medium",
        """At what rate percent per annum will a sum of money double itself in 8 years under simple interest?""",
        """బారువడ్డీ ప్రకారం ఒక మొత్తం 8 సంవత్సరాలలో రెట్టింపు కావడానికి వార్షిక వడ్డీ రేటు ఎంత ఉండాలి?""",
        ['12.5% per annum', '10% per annum', '12% per annum', '15% per annum'],
        ['సంవత్సరానికి 12.5%', 'సంవత్సరానికి 10%', 'సంవత్సరానికి 12%', 'సంవత్సరానికి 15%'],
        0,
        """When sum doubles, SI = P.
SI = (P * R * T) / 100 => P = (P * R * 8) / 100 => 8R = 100 => R = 12.5% per annum.""",
        """మొత్తం రెట్టింపు అయినప్పుడు SI = P.
8R = 100 => R = 12.5%."""
    ))

    qs.append(make_q(
        117, "Simple & Compound Interest - Equal Annual Installments", "Hard",
        """A loan of Rs. 2,100 is borrowed at 10% compound interest per annum, to be paid back in two equal annual installments. What is the value of each installment?""",
        """రూ. 2,100 రుణాన్ని వార్షికంగా 10% చక్రవడ్డీతో రెండు సమాన వార్షిక వాయిదాలలో తిరిగి చెల్లించాలి. ప్రతి వాయిదా మొత్తం ఎంత?""",
        ['Rs. 1,210', 'Rs. 1,155', 'Rs. 1,200', 'Rs. 1,250'],
        ['రూ. 1,210', 'రూ. 1,155', 'రూ. 1,200', 'రూ. 1,250'],
        0,
        """Let each installment be X.
Present Value formula: P = X / (1 + R/100) + X / (1 + R/100)^2
2,100 = X / 1.10 + X / 1.21 = (1.1X + X) / 1.21 = 2.1X / 1.21
=> X = (2,100 * 1.21) / 2.1 = 1,000 * 1.21 = Rs. 1,210.""",
        """ప్రతి వాయిదా X అనుకుంటే: P = X / 1.10 + X / 1.21.
2100 = 2.1X / 1.21 => X = 1000 * 1.21 = రూ. 1,210."""
    ))

    qs.append(make_q(
        118, "Simple & Compound Interest - SI to CI Conversion", "Hard",
        """The simple interest on a certain sum of money for 3 years at 4% per annum is Rs. 600. What will be the compound interest on the same sum for 2 years at the same annual interest rate?""",
        """ఒక నిర్దిష్ట మొత్తంపై సంవత్సరానికి 4% చొప్పున 3 సంవత్సరాలకు అయ్యే బారువడ్డీ రూ. 600. అదే మొత్తంపై అదే వడ్డీ రేటుతో 2 సంవత్సరాలకు అయ్యే చక్రవడ్డీ ఎంత?""",
        ['Rs. 408', 'Rs. 400', 'Rs. 416', 'Rs. 420'],
        ['రూ. 408', 'రూ. 400', 'రూ. 416', 'రూ. 420'],
        0,
        """Principal P = (SI * 100) / (R * T) = (600 * 100) / (4 * 3) = 60,000 / 12 = Rs. 5,000.
CI for 2 years on Rs. 5,000 at 4% = P * [(1 + R/100)^2 - 1]
CI = 5,000 * [(1.04)^2 - 1] = 5,000 * [1.0816 - 1] = 5,000 * 0.0816 = Rs. 408.""",
        """అసలు P = (600 * 100) / 12 = రూ. 5,000.
4% చొప్పున 2 సంవత్సరాలకు చక్రవడ్డీ = 5,000 * [(1.04)^2 - 1] = 5,000 * 0.0816 = రూ. 408."""
    ))

    qs.append(make_q(
        119, "Simple & Compound Interest - Principal from Amounts", "Medium",
        """A sum of money lent out at simple interest amounts to Rs. 756 in 2 years and to Rs. 873 in 3.5 years. What is the original principal sum and the rate of interest per annum?""",
        """బారువడ్డీకి ఇచ్చిన ఒక మొత్తం 2 సంవత్సరాలలో రూ. 756 మరియు 3.5 సంవత్సరాలలో రూ. 873 అవుతుంది. అసలు మరియు వార్షిక వడ్డీ రేటు ఎంత?""",
        ['Principal = Rs. 600, Rate = 13%', 'Principal = Rs. 620, Rate = 12%', 'Principal = Rs. 580, Rate = 14%', 'Principal = Rs. 600, Rate = 12%'],
        ['అసలు = రూ. 600, వడ్డీ రేటు = 13%', 'అసలు = రూ. 620, వడ్డీ రేటు = 12%', 'అసలు = రూ. 580, వడ్డీ రేటు = 14%', 'అసలు = రూ. 600, వడ్డీ రేటు = 12%'],
        0,
        """Interest for (3.5 - 2) = 1.5 years = 873 - 756 = Rs. 117.
Interest per year = 117 / 1.5 = Rs. 78.
Interest for 2 years = 78 * 2 = Rs. 156.
Principal P = 756 - 156 = Rs. 600.
Rate R = (78 / 600) * 100 = 13% per annum.""",
        """1.5 సంవత్సరాల వడ్డీ = 873 - 756 = రూ. 117.
సంవత్సరానికి వడ్డీ = 117 / 1.5 = రూ. 78.
2 సంవత్సరాల వడ్డీ = రూ. 156. అసలు = 756 - 156 = రూ. 600.
వడ్డీ రేటు = (78 / 600) * 100 = 13%."""
    ))

    qs.append(make_q(
        120, "Simple & Compound Interest - Quarterly Compounding", "Hard",
        """What is the compound interest on a principal of Rs. 16,000 for 9 months at 20% per annum, compounded quarterly?""",
        """రూ. 16,000 అసలుపై 20% వార్షిక వడ్డీ రేటుతో ప్రతి త్రైమాసికానికి (Quarterly) చక్రవడ్డీ లెక్కించినప్పుడు 9 నెలలకు అయ్యే చక్రవడ్డీ ఎంత?""",
        ['Rs. 2,522', 'Rs. 2,400', 'Rs. 2,610', 'Rs. 2,480'],
        ['రూ. 2,522', 'రూ. 2,400', 'రూ. 2,610', 'రూ. 2,480'],
        0,
        """Quarterly rate r = 20% / 4 = 5%. Time = 9 months = 3 quarters (n = 3).
Amount = 16,000 * (1 + 0.05)^3 = 16,000 * (1.05)^3 = 16,000 * 1.157625 = Rs. 18,522.
Compound Interest = 18,522 - 16,000 = Rs. 2,522.""",
        """త్రైమాసిక వడ్డీ రేటు = 5%, n = 3 త్రైమాసికాలు.
మొత్తం = 16,000 * (1.05)^3 = రూ. 18,522.
చక్రవడ్డీ = 18,522 - 16,000 = రూ. 2,522."""
    ))

    return qs

if __name__ == "__main__":
    qs = get_part2()
    print(f"Arithmetic Part 2 successfully generated with {len(qs)} verified questions.")
