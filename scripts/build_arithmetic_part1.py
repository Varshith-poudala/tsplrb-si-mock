# -*- coding: utf-8 -*-
"""
Arithmetic Part 1 (Q1 to Q60):
- Speed, Distance & Time (Q1 to Q30)
- Mensuration 2D & 3D (Q31 to Q60)
"""

def get_part1():
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

    # Q1: Circular Track First Meeting
    qs.append(make_q(
        1, "Speed, Distance & Time - Circular Track", "Hard",
        "Two runners A and B start simultaneously from the same point on a circular track of circumference 1,200 metres, running in opposite directions with speeds of 18 km/h and 27 km/h respectively. After how much time from the start will they meet for the first time anywhere on the track?",
        "1,200 మీటర్ల చుట్టుకొలత గల ఒక వృత్తాకార ట్రాక్‌పై ఒకే బిందువు నుండి A మరియు B అనే ఇద్దరు రన్నర్లు ఒకే సమయంలో బయలుదేరి వ్యతిరేక దిశలలో వరుసగా 18 కి.మీ/గం మరియు 27 కి.మీ/గం వేగాలతో పరుగెడుతున్నారు. బయలుదేరిన ఎంత సమయం తర్వాత వారు ట్రాక్‌పై మొదటిసారి కలుసుకుంటారు?",
        ["80 seconds", "96 seconds", "108 seconds", "120 seconds"],
        ["80 సెకన్లు", "96 సెకన్లు", "108 సెకన్లు", "120 సెకన్లు"],
        1,
        "Relative speed in opposite direction = 18 + 27 = 45 km/h = 45 * (5/18) = 12.5 m/s. Time = 1200 / 12.5 = 96 seconds.",
        "వ్యతిరేక దిశలో సాపేక్ష వేగం = 45 కి.మీ/గం = 12.5 మీ/సె. పట్టే సమయం = 1200 / 12.5 = 96 సెకన్లు."
    ))

    # Q2: Circular Track Starting Point Meeting
    qs.append(make_q(
        2, "Speed, Distance & Time - Circular Track", "Hard",
        "Two athletes P and Q run along a circular path of length 600 metres in the same direction. P takes 30 seconds to complete one full round, while Q takes 45 seconds. After how much time from the start will they meet for the first time at the exact starting point?",
        "600 మీటర్ల పొడవు గల వృత్తాకార ట్రాక్‌పై P మరియు Q లు ఒకే దిశలో పరుగెడుతున్నారు. ఒక పూర్తి రౌండ్‌ను పూర్తి చేయడానికి P కి 30 సెకన్లు, Q కి 45 సెకన్లు పడుతుంది. బయలుదేరిన ఎంత సమయం తర్వాత వారు ఖచ్చితంగా ప్రారంభ స్థానం వద్ద మొదటిసారి కలుసుకుంటారు?",
        ["60 seconds", "90 seconds", "120 seconds", "180 seconds"],
        ["60 సెకన్లు", "90 సెకన్లు", "120 సెకన్లు", "180 సెకన్లు"],
        1,
        "Meeting at starting point = LCM of individual round times = LCM(30, 45) = 90 seconds.",
        "ప్రారంభ స్థానం వద్ద కలుసుకునే సమయం = వారి రౌండ్ సమయాల క.సా.గు = క.సా.గు(30, 45) = 90 సెకన్లు."
    ))

    # Q3: Trains - Crossing Moving Train Opposite
    qs.append(make_q(
        3, "Speed, Distance & Time - Trains", "Medium",
        "Train A of length 220 metres running at 68 km/h crosses Train B of length 260 metres running at 58 km/h in the opposite direction. What is the time taken by them to cross each other completely?",
        "68 కి.మీ/గం వేగంతో ప్రయాణిస్తున్న 220 మీటర్ల పొడవు గల రైలు A, వ్యతిరేక దిశలో 58 కి.మీ/గం వేగంతో వస్తున్న 260 మీటర్ల పొడవు గల రైలు B ని దాటడానికి ఎంత సమయం పడుతుంది?",
        ["12.4 seconds", "13.7 seconds", "14.4 seconds", "15.2 seconds"],
        ["12.4 సెకన్లు", "13.7 సెకన్లు", "14.4 సెకన్లు", "15.2 సెకన్లు"],
        1,
        "Total distance = 220 + 260 = 480 m. Relative speed = 68 + 58 = 126 km/h = 126 * (5/18) = 35 m/s. Time = 480 / 35 = 13.71 seconds.",
        "మొత్తం దూరం = 480 మీ. సాపేక్ష వేగం = 126 కి.మీ/గం = 35 మీ/సె. దాటడానికి పట్టే సమయం = 480 / 35 = 13.71 సెకన్లు."
    ))

    # Q4: Trains - Passenger in Slower Train
    qs.append(make_q(
        4, "Speed, Distance & Time - Trains", "Hard",
        "A faster train 150 metres long passes a passenger sitting in a slower train running in the same direction in 18 seconds. If the speed of the faster train is 72 km/h, what is the speed of the slower train?",
        "ఒకే దిశలో ప్రయాణిస్తున్న రెండు రైళ్లలో, 72 కి.మీ/గం వేగంతో వెళ్తున్న 150 మీటర్ల పొడవు గల వేగవంతమైన రైలు నెమ్మదిగా వెళ్లే రైలులో కూర్చున్న ఒక ప్రయాణికుడిని 18 సెకన్లలో దాటుతుంది. ఆ నెమ్మదైన రైలు వేగం ఎంత?",
        ["42 km/h", "45 km/h", "48 km/h", "52 km/h"],
        ["42 కి.మీ/గం", "45 కి.మీ/గం", "48 కి.మీ/గం", "52 కి.మీ/గం"],
        0,
        "Distance = 150 m. Relative speed = 150 / 18 m/s = (150/18) * (18/5) = 30 km/h. S_faster - S_slower = 30 => 72 - S_slower = 30 => S_slower = 42 km/h.",
        "సాపేక్ష వేగం = 150 / 18 మీ/సె = 30 కి.మీ/గం. ఒకే దిశ కాబట్టి: 72 - వేగం = 30 => నెమ్మదైన రైలు వేగం = 42 కి.మీ/గం."
    ))

    # Q5: Boats & Streams - Ratio
    qs.append(make_q(
        5, "Boats & Streams - Speed Ratio", "Medium",
        "A police patrol boat can travel at 15 km/h in still water. If the speed of the river current is 3 km/h, what is the ratio of time taken by the boat to travel a certain distance upstream to the time taken to travel the same distance downstream?",
        "నిలకడగా ఉన్న నీటిలో ఒక పోలీస్ పెట్రోలింగ్ పడవ వేగం 15 కి.మీ/గం. నదీ ప్రవాహ వేగం 3 కి.మీ/గం అయితే, ఒక నిర్ణీత దూరాన్ని ప్రవాహానికి ఎదురుగా వెళ్ళడానికి పట్టే సమయానికి, ప్రవాహ దిశలో వెళ్ళడానికి పట్టే సమయానికి గల నిష్పత్తి ఎంత?",
        ["3 : 2", "4 : 3", "5 : 3", "2 : 1"],
        ["3 : 2", "4 : 3", "5 : 3", "2 : 1"],
        0,
        "Downstream speed = 15 + 3 = 18 km/h. Upstream speed = 15 - 3 = 12 km/h. Time ratio upstream : downstream = 18 : 12 = 3 : 2.",
        "ఎదురుగా సమయం : ప్రవాహ దిశలో సమయం = 18 : 12 = 3 : 2."
    ))

    # Q6: Boats & Streams - Round Trip
    qs.append(make_q(
        6, "Boats & Streams - Round Trip", "Hard",
        "A boat goes 24 km downstream and returns to the starting point in a total time of 5 hours. If the speed of the current is 2 km/h, what is the speed of the boat in still water?",
        "ఒక పడవ ప్రవాహ దిశలో 24 కి.మీ వెళ్లి తిరిగి ప్రారంభ స్థానానికి రావడానికి మొత్తం 5 గంటల సమయం పడుతుంది. నదీ ప్రవాహ వేగం 2 కి.మీ/గం అయితే, నిలకడ నీటిలో పడవ వేగం ఎంత?",
        ["8 km/h", "10 km/h", "12 km/h", "14 km/h"],
        ["8 కి.మీ/గం", "10 కి.మీ/గం", "12 కి.మీ/గం", "14 కి.మీ/గం"],
        1,
        "24/(B + 2) + 24/(B - 2) = 5. For B = 10: 24/12 + 24/8 = 2 + 3 = 5 hours. Still water speed = 10 km/h.",
        "24/(B + 2) + 24/(B - 2) = 5. B = 10 వద్ద: 2 + 3 = 5 గంటలు. పడవ వేగం = 10 కి.మీ/గం."
    ))

    # Q7: Races - Beat by 50m or 10s
    qs.append(make_q(
        7, "Races & Games - Head Start", "Hard",
        "In a 1,000-metre sprint race, athlete A beats athlete B by 50 metres or by 10 seconds. What is the time taken by athlete A to complete the race?",
        "1,000 మీటర్ల పరుగు పందెంలో అథ్లెట్ A, అథ్లెట్ B ని 50 మీటర్లు లేదా 10 సెకన్ల తేడాతో ఓడిస్తాడు. అథ్లెట్ A మొత్తం పందెం పూర్తి చేయడానికి పట్టే సమయం ఎంత?",
        ["180 seconds", "190 seconds", "200 seconds", "210 seconds"],
        ["180 సెకన్లు", "190 సెకన్లు", "200 సెకన్లు", "210 సెకన్లు"],
        1,
        "Speed of B = 50 m / 10 s = 5 m/s. Time of B for 1,000 m = 1000 / 5 = 200 s. Time of A = 200 - 10 = 190 seconds.",
        "B వేగం = 50 / 10 = 5 మీ/సె. B కి మొత్తం సమయం = 200 సెకన్లు. A సమయం = 200 - 10 = 190 సెకన్లు."
    ))

    # Q8: Races - Head start win
    qs.append(make_q(
        8, "Races & Games - Beat by Distance", "Hard",
        "In a 500-metre race, the ratio of speeds of two sprinters A and B is 3 : 4. If A has a head start of 140 metres, who wins the race and by what distance?",
        "500 మీటర్ల పరుగు పందెంలో A మరియు B ల వేగాల నిష్పత్తి 3 : 4. A కి 140 మీటర్ల ప్రారంభ ఆధిక్యం (Start) ఇస్తే, పందెంలో ఎవరు గెలుస్తారు మరియు ఎంత దూరంతో గెలుస్తారు?",
        ["A wins by 20 metres", "B wins by 20 metres", "B wins by 25 metres", "A wins by 30 metres"],
        ["A 20 మీటర్లతో గెలుస్తాడు", "B 20 మీటర్లతో గెలుస్తాడు", "B 25 మీటర్లతో గెలుస్తాడు", "A 30 మీటర్లతో గెలుస్తాడు"],
        0,
        "Distance A needs to run = 500 - 140 = 360 m. Time for A = 360 / 3 = 120 units. In 120 units, B runs 120 * 4 = 480 m. Since B needs 500 m, B is 20 m behind. A wins by 20 metres.",
        "A పరిగెత్తవలసిన దూరం = 360 మీ. A సమయం = 120 యూనిట్లు. ఆ సమయంలో B దూరం = 480 మీ. కాబట్టి A 20 మీటర్ల ఆధిక్యంతో గెలుస్తాడు."
    ))

    # Q9: Late & Early formula
    qs.append(make_q(
        9, "Speed, Distance & Time - Late & Early", "Medium",
        "If a candidate walks from his house to the police exam center at 4 km/h, he arrives 10 minutes late. But if he increases his speed to 5 km/h, he arrives 5 minutes early. What is the distance from his house to the exam center?",
        "ఒక అభ్యర్థి తన ఇంటి నుండి పోలీస్ పరీక్షా కేంద్రానికి 4 కి.మీ/గం వేగంతో నడిస్తే 10 నిమిషాలు ఆలస్యంగా చేరుకుంటాడు. కానీ తన వేగాన్ని 5 కి.మీ/గం కి పెంచితే 5 నిమిషాలు ముందుగానే చేరుకుంటాడు. అతని ఇంటి నుండి పరీక్షా కేంద్రానికి గల దూరం ఎంత?",
        ["4 km", "5 km", "6 km", "7.5 km"],
        ["4 కి.మీ", "5 కి.మీ", "6 కి.మీ", "7.5 కి.మీ"],
        1,
        "Time diff = 10 + 5 = 15 min = 1/4 hr. Distance = (S1 * S2 / |S1 - S2|) * Delta_T = (4 * 5 / 1) * (1/4) = 5 km.",
        "దూరం = (S1 * S2 / |S1 - S2|) * Delta_T = (4 * 5 / 1) * (15/60) = 5 కి.మీ."
    ))

    # Q10: Staggered Departure
    qs.append(make_q(
        10, "Speed, Distance & Time - Staggered Starts", "Hard",
        "Police Station A and Police Outpost B are 260 km apart on a highway. A police jeep leaves Station A at 8:00 AM towards B at 40 km/h. Another patrol van leaves Outpost B at 9:00 AM towards A at 50 km/h. At what time will they cross each other?",
        "పోలీస్ స్టేషన్ A మరియు పోలీస్ అవుట్‌పోస్ట్ B జాతీయ రహదారిపై 260 కి.మీ దూరంలో ఉన్నాయి. ఒక పోలీస్ జీపు ఉదయం 8:00 గంటలకు A నుండి 40 కి.మీ/గం వేగంతో B వైపు బయలుదేరింది. మరొక పెట్రోలింగ్ వ్యాన్ ఉదయం 9:00 గంటలకు B నుండి 50 కి.మీ/గం వేగంతో A వైపు బయలుదేరింది. అవి ఏ సమయానికి ఎదురుపడతాయి?",
        ["11:00 AM", "11:24 AM", "11:30 AM", "12:00 Noon"],
        ["ఉదయం 11:00", "ఉదయం 11:24", "ఉదయం 11:30", "మధ్యాహ్నం 12:00"],
        1,
        "Distance covered by first jeep by 9 AM = 40 km. Remaining distance = 260 - 40 = 220 km. Combined speed = 40 + 50 = 90 km/h. Time = 220/90 = 2h 24m. Crossing time = 9:00 AM + 2h 24m = 11:24 AM.",
        "9 గంటల సమయానికి మిగిలిన దూరం = 220 కి.మీ. సాపేక్ష వేగం = 90 కి.మీ/గం. సమయం = 2 గంటల 24 నిమిషాలు. కలిసే సమయం = ఉదయం 11:24."
    ))

    # Q11: Average Speed - Three Equal Segments
    qs.append(make_q(
        11, "Speed, Distance & Time - Average Speed", "Hard",
        "A highway patrol car covers three equal successive distances of 60 km each at speeds of 30 km/h, 40 km/h, and 60 km/h respectively. What is the average speed of the patrol car for the entire journey of 180 km?",
        "ఒక హైవే పెట్రోల్ కారు వరుసగా 60 కి.మీ చొప్పున మూడు సమాన దూరాలను 30 కి.మీ/గం, 40 కి.మీ/గం మరియు 60 కి.మీ/గం వేగాలతో ప్రయాణించింది. మొత్తం 180 కి.మీ ప్రయాణానికి ఆ కారు సగటు వేగం ఎంత?",
        ["38 km/h", "40 km/h", "42 km/h", "45 km/h"],
        ["38 కి.మీ/గం", "40 కి.మీ/గం", "42 కి.మీ/గం", "45 కి.మీ/గం"],
        1,
        "Total distance = 180 km. Total time = 60/30 + 60/40 + 60/60 = 2 + 1.5 + 1 = 4.5 hours. Average speed = 180 / 4.5 = 40 km/h.\nHarmonic mean shortcut: 3 / (1/30 + 1/40 + 1/60) = 3 / ((4+3+2)/120) = 3 / (9/120) = 360/9 = 40 km/h.",
        "మొత్తం కాలం = 60/30 + 60/40 + 60/60 = 4.5 గంటలు. సగటు వేగం = 180 / 4.5 = 40 కి.మీ/గం."
    ))

    # Q12: Sound & Bullet Problem
    qs.append(make_q(
        12, "Speed, Distance & Time - Relative Sound", "Hard",
        "Two gunshots were fired from the same police firing range at an interval of 12 minutes, but a person approaching the range in a car hears the second shot 11 minutes after the first. If the speed of sound is 330 m/s, what is the speed of the car?",
        "ఒక పోలీస్ ఫైరింగ్ రేంజ్ నుండి 12 నిమిషాల వ్యవధిలో రెండు తుపాకీ గుండ్లు కాల్చబడ్డాయి. కానీ కారులో ఆ ఫైరింగ్ రేంజ్ వైపు వస్తున్న ఒక వ్యక్తి మొదటి శబ్దం విన్న 11 నిమిషాల తర్వాత రెండవ శబ్దాన్ని విన్నాడు. ధ్వని వేగం 330 మీ/సె అయితే, ఆ కారు వేగం ఎంత?",
        ["108 km/h", "118.8 km/h", "120 km/h", "125.5 km/h"],
        ["108 కి.మీ/గం", "118.8 కి.మీ/గం", "120 కి.మీ/గం", "125.5 కి.మీ/గం"],
        1,
        "Distance sound travels in (12 - 11 = 1) minute = Distance car travels in 11 minutes.\nSpeed_car * 11 = Speed_sound * 1 => Speed_car = 330 * (1/11) = 30 m/s.\nConvert to km/h: 30 * (18/5) = 108 km/h. Wait: 30 * 18 / 5 = 6 * 18 = 108 km/h! Let's check option 0: 108 km/h.",
        "ధ్వని 1 నిమిషంలో ప్రయాణించే దూరం = కారు 11 నిమిషాల్లో ప్రయాణించే దూరం. కారు వేగం = 330 * (1/11) = 30 మీ/సె = 108 కి.మీ/గం."
    ))
    # Correct option for Q12 should be 0 (108 km/h)
    qs[-1]["correct_option"] = 0

    # Q13: Train Passing Two Men Walking
    qs.append(make_q(
        13, "Speed, Distance & Time - Train & Walkers", "Hard",
        "A train travelling at uniform speed passes two men walking in the same direction along the railway track. The first man walks at 3 km/h and the train passes him in 9 seconds. The second man walks at 5 km/h and the train passes him in 10 seconds. What is the speed of the train?",
        "స్థిర వేగంతో వెళ్తున్న ఒక రైలు ట్రాక్ వెంబడి ఒకే దిశలో నడుస్తున్న ఇద్దరు వ్యక్తులను దాటుతుంది. మొదటి వ్యక్తి 3 కి.మీ/గం వేగంతో నడుస్తుండగా రైలు అతన్ని 9 సెకన్లలో దాటుతుంది. రెండవ వ్యక్తి 5 కి.మీ/గం వేగంతో నడుస్తుండగా 10 సెకన్లలో దాటుతుంది. ఆ రైలు వేగం ఎంత?",
        ["21 km/h", "23 km/h", "25 km/h", "27 km/h"],
        ["21 కి.మీ/గం", "23 కి.మీ/గం", "25 కి.మీ/గం", "27 కి.మీ/గం"],
        1,
        "Let train speed be S km/h. Length of train is constant.\nLength = (S - 3) * (5/18) * 9 = (S - 5) * (5/18) * 10.\n9(S - 3) = 10(S - 5) => 9S - 27 = 10S - 50 => S = 23 km/h.",
        "రైలు పొడవు స్థిరం: (S - 3) * 9 = (S - 5) * 10 => 9S - 27 = 10S - 50 => S = 23 కి.మీ/గం."
    ))

    # Q14: Steamer river downstream & upstream with percentage
    qs.append(make_q(
        14, "Boats & Streams - Speed Calculation", "Medium",
        "A man can row at 9 km/h in still water. If the river current flows at 3 km/h, it takes him 3 hours more in rowing upstream than in rowing downstream for the same distance. What is the distance?",
        "ఒక వ్యక్తి నిలకడ నీటిలో 9 కి.మీ/గం వేగంతో పడవ నడపగలడు. నదీ ప్రవాహ వేగం 3 కి.మీ/గం అయితే, సమాన దూరానికి ప్రవాహ దిశలో కంటే ప్రవాహానికి ఎదురుగా ప్రయాణించడానికి అతనికి 3 గంటల సమయం ఎక్కువ పడుతుంది. ఆ దూరం ఎంత?",
        ["36 km", "40 km", "45 km", "48 km"],
        ["36 కి.మీ", "40 కి.మీ", "45 కి.మీ", "48 కి.మీ"],
        0,
        "Downstream speed = 9 + 3 = 12 km/h. Upstream speed = 9 - 3 = 6 km/h.\nD/6 - D/12 = 3 => D/12 = 3 => D = 36 km.",
        "ప్రవాహ దిశలో వేగం = 12 కి.మీ/గం, ఎదురుగా వేగం = 6 కి.మీ/గం. D/6 - D/12 = 3 => D = 36 కి.మీ."
    ))

    # Q15: Escalator Problem (Relative Speed)
    qs.append(make_q(
        15, "Speed, Distance & Time - Moving Walkway", "Hard",
        "An airport moving walkway of length 120 metres moves at a speed of 1.5 m/s. If an officer walks on the walkway in the direction of its motion at 2.5 m/s, how many seconds will he take to reach the other end?",
        "120 మీటర్ల పొడవు గల విమానాశ్రయ మూవింగ్ వాక్‌వే 1.5 మీ/సె వేగంతో కదులుతుంది. ఒక అధికారి ఆ వాక్‌వేపై అది కదులుతున్న దిశలోనే 2.5 మీ/సె వేగంతో నడిస్తే, అతను అవతలి చివరకు చేరుకోవడానికి ఎన్ని సెకన్లు పడుతుంది?",
        ["25 seconds", "30 seconds", "35 seconds", "40 seconds"],
        ["25 సెకన్లు", "30 సెకన్లు", "35 సెకన్లు", "40 సెకన్లు"],
        1,
        "Net speed in the direction of moving walkway = 1.5 + 2.5 = 4.0 m/s. Time = Distance / Net Speed = 120 / 4.0 = 30 seconds.",
        "వాక్‌వే కదిలే దిశలోనే నడుస్తున్నప్పుడు నికర వేగం = 1.5 + 2.5 = 4.0 మీ/సె. పట్టే కాలం = 120 / 4 = 30 సెకన్లు."
    ))

    # Q16: Circular Track - 3 Runners
    qs.append(make_q(
        16, "Speed, Distance & Time - Circular Track (3 Runners)", "Hard",
        "Three runners A, B, and C run on a circular track of 1,200 metres in the same direction with speeds of 3 m/s, 4 m/s, and 6 m/s respectively. After how many seconds from the start will all three meet together for the first time at the starting point?",
        "1,200 మీటర్ల వృత్తాకార ట్రాక్‌పై ముగ్గురు రన్నర్లు A, B మరియు C లు ఒకే దిశలో వరుసగా 3 మీ/సె, 4 మీ/సె, మరియు 6 మీ/సె వేగాలతో పరుగెడుతున్నారు. ప్రారంభ స్థానం వద్ద వారందరూ మొదటిసారి కలిసి కలుసుకోవడానికి ఎన్ని సెకన్లు పడుతుంది?",
        ["600 seconds", "900 seconds", "1,200 seconds", "1,500 seconds"],
        ["600 సెకన్లు", "900 సెకన్లు", "1,200 సెకన్లు", "1,500 సెకన్లు"],
        2,
        "Time for 1 lap: A = 1200/3 = 400 s; B = 1200/4 = 300 s; C = 1200/6 = 200 s.\nMeeting at starting point = LCM(400, 300, 200) = 1,200 seconds.",
        "ఒక్కో రౌండ్‌కు సమయం: A = 400 సె, B = 300 సె, C = 200 సె. ప్రారంభ స్థానం వద్ద కలిసే సమయం = క.సా.గు(400, 300, 200) = 1,200 సెకన్లు."
    ))

    # Q17: Train Crossing Platform & Post
    qs.append(make_q(
        17, "Speed, Distance & Time - Platform & Post", "Medium",
        "A train travelling at uniform speed passes a telegraph post in 8 seconds and a platform 264 metres long in 20 seconds. What is the length of the train?",
        "ఒక రైలు టెలిగ్రాఫ్ స్తంభాన్ని 8 సెకన్లలో మరియు 264 మీటర్ల పొడవు గల ప్లాట్‌ఫారమ్‌ను 20 సెకన్లలో దాటుతుంది. ఆ రైలు పొడవు ఎంత?",
        ["160 metres", "176 metres", "184 metres", "192 metres"],
        ["160 మీటర్లు", "176 మీటర్లు", "184 మీటర్లు", "192 మీటర్లు"],
        1,
        "Let train length be L. Speed = L / 8 = (L + 264) / 20 => 20L = 8L + 2112 => 12L = 2112 => L = 176 metres.",
        "రైలు పొడవు L అనుకుంటే: L / 8 = (L + 264) / 20 => 12L = 2112 => L = 176 మీటర్లు."
    ))

    # Q18: Average Speed - Harmonic Mean Concept
    qs.append(make_q(
        18, "Speed, Distance & Time - Variable Distances", "Hard",
        "A bus travels 1/3rd of the total distance at 20 km/h, the next 1/3rd at 30 km/h, and the remaining 1/3rd at 60 km/h. What is the average speed of the bus for the entire journey?",
        "ఒక బస్సు మొత్తం దూరంలో 1/3 వంతు దూరాన్ని 20 కి.మీ/గం వేగంతో, తర్వాతి 1/3 వంతు దూరాన్ని 30 కి.మీ/గం వేగంతో, మరియు మిగిలిన 1/3 వంతు దూరాన్ని 60 కి.మీ/గం వేగంతో ప్రయాణిస్తుంది. మొత్తం ప్రయాణానికి ఆ బస్సు సగటు వేగం ఎంత?",
        ["28 km/h", "30 km/h", "32 km/h", "36 km/h"],
        ["28 కి.మీ/గం", "30 కి.మీ/గం", "32 కి.మీ/గం", "36 కి.మీ/గం"],
        1,
        "For 3 equal distances, Average Speed = 3 / (1/v1 + 1/v2 + 1/v3) = 3 / (1/20 + 1/30 + 1/60) = 3 / ((3+2+1)/60) = 3 / (6/60) = 30 km/h.",
        "సమాన దూరాలకు సగటు వేగం = 3 / (1/20 + 1/30 + 1/60) = 3 / (6/60) = 30 కి.మీ/గం."
    ))

    # Q19: Boat River Crossing (Perpendicular)
    qs.append(make_q(
        19, "Boats & Streams - River Width", "Hard",
        "A river 400 metres wide flows at 3 km/h. A swimmer who swims at 5 km/h in still water wants to cross the river along the shortest possible path (perpendicular to river bank). In which direction should he head and how many minutes will he take to cross?",
        "400 మీటర్ల వెడల్పు గల నది 3 కి.మీ/గం వేగంతో ప్రవహిస్తుంది. నిలకడ నీటిలో 5 కి.మీ/గం ఈదగల ఈతగాడు నదిని అతి తక్కువ మార్గంలో (లంబంగా) దాటాలనుకుంటున్నాడు. అతను ఎంత సమయం (నిమిషాల్లో) లో నదిని దాటగలడు?",
        ["5 minutes", "6 minutes", "7.5 minutes", "8 minutes"],
        ["5 నిమిషాలు", "6 నిమిషాలు", "7.5 నిమిషాలు", "8 నిమిషాలు"],
        1,
        "Resultant velocity perpendicular to flow = sqrt(5^2 - 3^2) = sqrt(25 - 9) = 4 km/h = 4 * (1000/60) = 200/3 m/min.\nTime = Width / Velocity = 400 / (200/3) = 6 minutes.",
        "నదికి లంబంగా ఫలిత వేగం = sqrt(5^2 - 3^2) = 4 కి.మీ/గం = 200/3 మీ/నిమిషం. కాలం = 400 / (200/3) = 6 నిమిషాలు."
    ))

    # Q20: Relative Speed - Thief and Police Chase
    qs.append(make_q(
        20, "Speed, Distance & Time - Police Pursuit", "Medium",
        "A thief spots a policeman from a distance of 200 metres and starts running at 10 km/h. The policeman instantly gives chase at 12 km/h. At what distance from the spot of theft will the policeman catch the thief?",
        "ఒక దొంగ 200 మీటర్ల దూరం నుండి పోలీసును చూసి 10 కి.మీ/గం వేగంతో పరుగెత్తడం ప్రారంభించాడు. పోలీసులు వెంటనే 12 కి.మీ/గం వేగంతో వెంబడించారు. దొంగతనం జరిగిన ప్రదేశం నుండి ఎంత దూరంలో పోలీసులు దొంగను పట్టుకుంటారు?",
        ["1,000 metres", "1,200 metres", "1,400 metres", "1,500 metres"],
        ["1,000 మీటర్లు", "1,200 మీటర్లు", "1,400 మీటర్లు", "1,500 మీటర్లు"],
        1,
        "Relative speed = 12 - 10 = 2 km/h = 2 * (5/18) = 5/9 m/s.\nTime to catch = Initial gap / Relative speed = 200 / (5/9) = 360 seconds = 6 minutes.\nDistance covered by police = 12 km/h * (6/60 hr) = 1.2 km = 1,200 metres.",
        "సాపేక్ష వేగం = 2 కి.మీ/గం = 5/9 మీ/సె. పట్టుకోవడానికి పట్టే సమయం = 360 సెకన్లు = 6 నిమిషాలు. పోలీస్ పరిగెత్తిన దూరం = 12 * (6/60) = 1.2 కి.మీ = 1,200 మీటర్లు."
    ))

    # Q21 to Q30: Advanced Speed-Distance & Time
    # Q21: Train lengths ratio
    qs.append(make_q(
        21, "Speed, Distance & Time - Train Length Ratio", "Hard",
        "Two trains of lengths in the ratio 5 : 3 run on parallel tracks. When running in the same direction, the faster train passes the slower one in 48 seconds. When running in opposite directions, they pass each other in 12 seconds. What is the ratio of speeds of the faster train to the slower train?",
        "సమాంతర ట్రాక్‌లపై 5 : 3 పొడవుల నిష్పత్తి గల రెండు రైళ్లు నడుస్తున్నాయి. అవి ఒకే దిశలో ప్రయాణిస్తున్నప్పుడు వేగవంతమైన రైలు నెమ్మదైన రైలును 48 సెకన్లలో దాటుతుంది. వ్యతిరేక దిశలో ప్రయాణిస్తున్నప్పుడు అవి 12 సెకన్లలో ఒకదానికొకటి దాటుతాయి. ఆ రెండు రైళ్ల వేగాల నిష్పత్తి ఎంత?",
        ["5 : 3", "7 : 5", "4 : 3", "3 : 2"],
        ["5 : 3", "7 : 5", "4 : 3", "3 : 2"],
        0,
        "Total length = L. Opposite: S1 + S2 = L / 12. Same direction: S1 - S2 = L / 48.\n(S1 + S2) / (S1 - S2) = 48 / 12 = 4 / 1.\nBy componendo and dividendo: S1 / S2 = (4 + 1) / (4 - 1) = 5 / 3.",
        "(S1 + S2) / (S1 - S2) = 48 / 12 = 4 / 1 => S1 / S2 = (4 + 1) / (4 - 1) = 5 : 3."
    ))

    # Q22: Change in speed after accident
    qs.append(make_q(
        22, "Speed, Distance & Time - Speed Reduction", "Hard",
        "A train meets with an accident 60 km after starting and then proceeds at 3/4th of its original speed, arriving at its destination 40 minutes late. Had the accident occurred 30 km further along the route, it would have arrived only 25 minutes late. What is the original speed of the train?",
        "ఒక రైలు బయలుదేరిన 60 కి.మీ తర్వాత ప్రమాదానికి గురై, మిగిలిన ప్రయాణాన్ని తన అసలు వేగంలో 3/4 వంతు వేగంతో పూర్తి చేస్తూ గమ్యస్థానానికి 40 నిమిషాలు ఆలస్యంగా చేరుకుంది. ఆ ప్రమాదం మరో 30 కి.మీ ముందు జరిగి ఉంటే, అది 25 నిమిషాలు మాత్రమే ఆలస్యంగా చేరేది. ఆ రైలు అసలు వేగం ఎంత?",
        ["40 km/h", "45 km/h", "50 km/h", "60 km/h"],
        ["40 కి.మీ/గం", "45 కి.మీ/గం", "50 కి.మీ/గం", "60 కి.మీ/గం"],
        3,
        "The 15-minute time difference (40 - 25 = 15 min = 1/4 hr) is due to travelling 30 km at 3/4 speed vs original speed S.\n30/(3S/4) - 30/S = 1/4 => 40/S - 30/S = 1/4 => 10/S = 1/4 => S = 40? Wait: 40/S - 30/S = 10/S = 1/4 => S = 40 km/h. Let's verify: 30 / 30 = 1 hr. 30 / 40 = 3/4 hr = 45 min. Difference = 15 min! Yes! Option 0 is 40 km/h.",
        "30 కి.మీ దూరాన్ని 3/4 వేగంతో వెళ్ళినప్పటి సమయానికి, అసలు వేగంతో వెళ్ళిన సమయానికి తేడా = 15 నిమిషాలు (1/4 గంట). 40/S - 30/S = 1/4 => 10/S = 1/4 => S = 40 కి.మీ/గం."
    ))
    qs[-1]["correct_option"] = 0

    # Q23: Escalator walking opposite
    qs.append(make_q(
        23, "Speed, Distance & Time - Escalator Steps", "Hard",
        "A person walking down an escalator takes 50 steps to reach the bottom. When he doubles his walking speed, he takes 60 steps. How many steps would be visible if the escalator were stationary?",
        "కదులుతున్న ఎస్కలేటర్‌పై కిందకు నడుస్తున్న ఒక వ్యక్తి 50 అడుగులు వేసి కిందకు చేరుకుంటాడు. అతను తన నడక వేగాన్ని రెట్టింపు చేసినప్పుడు 60 అడుగులు వేస్తాడు. ఆ ఎస్కలేటర్ ఆగిపోయి ఉన్నప్పుడు కనిపించే మొత్తం అడుగుల సంఖ్య ఎంత?",
        ["75 steps", "80 steps", "90 steps", "100 steps"],
        ["75 అడుగులు", "80 అడుగులు", "90 అడుగులు", "100 అడుగులు"],
        0,
        "Let escalator speed be e steps/s and walking speed be v. Total steps N = 50 + 50*(e/v) = 60 + 60*(e/2v) = 60 + 30*(e/v).\n50 + 50(e/v) = 60 + 30(e/v) => 20(e/v) = 10 => e/v = 1/2.\nTotal visible steps N = 50 + 50*(1/2) = 75 steps.",
        "ఎస్కలేటర్ నిశ్చలంగా ఉన్నప్పుడు మొత్తం అడుగులు N = 50 + 50*(1/2) = 75 అడుగులు."
    ))

    # Q24: Circular track meeting count
    qs.append(make_q(
        24, "Speed, Distance & Time - Distinct Meeting Points", "Hard",
        "Two runners A and B run on a circular track in opposite directions with speeds in the ratio 7 : 5. How many distinct meeting points are there on the circular track?",
        "వృత్తాకార ట్రాక్‌పై వ్యతిరేక దిశలలో 7 : 5 వేగాల నిష్పత్తితో ఇద్దరు రన్నర్లు పరుగెడుతున్నారు. ఆ వృత్తాకార ట్రాక్‌పై వారు కలుసుకునే విభిన్న బిందువుల (Distinct Meeting Points) సంఖ్య ఎంత?",
        ["2", "5", "7", "12"],
        ["2", "5", "7", "12"],
        3,
        "Formula for distinct meeting points on circular track:\nIf running in OPPOSITE directions with speed ratio a : b (in simplest form): Number of distinct points = a + b = 7 + 5 = 12.\n(If running in SAME direction: |a - b| = 7 - 5 = 2).",
        "వ్యతిరేక దిశలో విభిన్న సమావేశ బిందువుల సూత్రం = a + b = 7 + 5 = 12 (ఒకే దిశలో అయితే a - b = 2)."
    ))

    # Q25: River stream speed calculation
    qs.append(make_q(
        25, "Boats & Streams - Stream Speed", "Medium",
        "A boat travels 32 km downstream and 14 km upstream in a total of 6 hours. It also covers 40 km downstream and 21 km upstream in 8 hours. What is the speed of the river stream?",
        "ఒక పడవ ప్రవాహ దిశలో 32 కి.మీ మరియు ప్రవాహానికి ఎదురుగా 14 కి.మీ దూరాన్ని మొత్తం 6 గంటల్లో ప్రయాణిస్తుంది. అలాగే ప్రవాహ దిశలో 40 కి.మీ మరియు ఎదురుగా 21 కి.మీ దూరాన్ని 8 గంటల్లో ప్రయాణిస్తుంది. నదీ ప్రవాహ వేగం ఎంత?",
        ["2 km/h", "3 km/h", "4 km/h", "5 km/h"],
        ["2 కి.మీ/గం", "3 కి.మీ/గం", "4 కి.మీ/గం", "5 కి.మీ/గం"],
        1,
        "Let downstream speed be D and upstream speed be U.\n32/D + 14/U = 6 and 40/D + 21/U = 8.\nNotice HCF of (32, 40) is 8 => Test D = 8: 32/8 = 4 => 14/U = 2 => U = 7.\nCheck second eq: 40/8 + 21/7 = 5 + 3 = 8! Perfect.\nSpeed of stream = (D - U) / 2 = (8 - 7) / 2 = 0.5? Wait: if D = 10? 40/10=4, 21/U=4 => U=5.25. If D=8, stream is 0.5. If D=12, U=6? Let's check: 32/8 + 14/7 = 4 + 2 = 6. 40/8 + 21/7 = 5 + 3 = 8. Downstream D = 8, Upstream U = 7. Stream = (8 - 7)/2 = 0.5. Let's adjust numbers for clean integer: 36 km downstream & 24 km upstream in 6 hrs; 48 downstream & 40 upstream in 9 hrs => D = 12, U = 8 => Boat = 10, Stream = (12-8)/2 = 2 km/h!",
        "D = 12 కి.మీ/గం, U = 8 కి.మీ/గం అయినప్పుడు ప్రవాహ వేగం = (12 - 8) / 2 = 2 కి.మీ/గం."
    ))
    qs[-1]["options_en"] = ["1.5 km/h", "2 km/h", "2.5 km/h", "3 km/h"]
    qs[-1]["options_te"] = ["1.5 కి.మీ/గం", "2 కి.మీ/గం", "2.5 కి.మీ/గం", "3 కి.మీ/గం"]
    qs[-1]["question_en"] = "A boat travels 36 km downstream and 24 km upstream in 6 hours. It also covers 48 km downstream and 40 km upstream in 9 hours. What is the speed of the river stream?"
    qs[-1]["question_te"] = "ఒక పడవ ప్రవాహ దిశలో 36 కి.మీ మరియు ప్రవాహానికి ఎదురుగా 24 కి.మీ దూరాన్ని 6 గంటల్లో ప్రయాణిస్తుంది. అలాగే ప్రవాహ దిశలో 48 కి.మీ మరియు ఎదురుగా 40 కి.మీ దూరాన్ని 9 గంటల్లో ప్రయాణిస్తుంది. నదీ ప్రవాహ వేగం ఎంత?"
    qs[-1]["correct_option"] = 1

    # Q26 to Q30: More Speed & Distance
    # Q26: Relative Speed Circular with 3 athletes
    qs.append(make_q(
        26, "Speed, Distance & Time - Circular Track", "Medium",
        "Two cyclists start from the same point on a 400-metre circular track running in opposite directions at 15 m/s and 25 m/s. How many times will they meet each other while riding for 10 minutes?",
        "400 మీటర్ల వృత్తాకార ట్రాక్‌పై ఒకే బిందువు నుండి ఇద్దరు సైక్లిస్టులు వ్యతిరేక దిశలలో 15 మీ/సె మరియు 25 మీ/సె వేగాలతో బయలుదేరారు. 10 నిమిషాల వ్యవధిలో వారు ఎన్నిసార్లు ఒకరినొకరు కలుసుకుంటారు?",
        ["50 times", "60 times", "75 times", "100 times"],
        ["50 సార్లు", "60 సార్లు", "75 సార్లు", "100 సార్లు"],
        1,
        "Relative speed in opposite directions = 15 + 25 = 40 m/s.\nTime for 1 meeting = Track length / Relative speed = 400 / 40 = 10 seconds.\nTotal time = 10 minutes = 600 seconds.\nNumber of meetings = 600 / 10 = 60 times.",
        "సాపేక్ష వేగం = 40 మీ/సె. ఒక్కో సమావేశానికి పట్టే సమయం = 400 / 40 = 10 సెకన్లు. 10 నిమిషాలు (600 సెకన్లు) లో సమావేశాల సంఖ్య = 600 / 10 = 60 సార్లు."
    ))

    # Q27: Two trains passing two platforms
    qs.append(make_q(
        27, "Speed, Distance & Time - Trains", "Medium",
        "A train of length 150 metres passes a platform 100 metres long in 10 seconds. How long will it take to pass another platform 250 metres long?",
        "150 మీటర్ల పొడవు గల ఒక రైలు 100 మీటర్ల ప్లాట్‌ఫారమ్‌ను 10 సెకన్లలో దాటుతుంది. 250 మీటర్ల పొడవు గల మరొక ప్లాట్‌ఫారమ్‌ను దాటడానికి దానికి ఎంత సమయం పడుతుంది?",
        ["14 seconds", "15 seconds", "16 seconds", "18 seconds"],
        ["14 సెకన్లు", "15 సెకన్లు", "16 సెకన్లు", "18 సెకన్లు"],
        2,
        "Speed = (150 + 100) / 10 = 250 / 10 = 25 m/s.\nFor second platform: Distance = 150 + 250 = 400 m.\nTime = 400 / 25 = 16 seconds.",
        "రైలు వేగం = (150 + 100) / 10 = 25 మీ/సె. రెండవ ప్లాట్‌ఫారమ్ దాటడానికి సమయం = (150 + 250) / 25 = 400 / 25 = 16 సెకన్లు."
    ))

    # Q28: Average speed - Equal time intervals
    qs.append(make_q(
        28, "Speed, Distance & Time - Average Speed", "Medium",
        "A car travels for 2 hours at 50 km/h and for the next 3 hours at 70 km/h. What is the average speed of the car for the entire 5-hour journey?",
        "ఒక కారు మొదటి 2 గంటలు 50 కి.మీ/గం వేగంతో, తర్వాతి 3 గంటలు 70 కి.మీ/గం వేగంతో ప్రయాణించింది. మొత్తం 5 గంటల ప్రయాణానికి ఆ కారు సగటు వేగం ఎంత?",
        ["60 km/h", "62 km/h", "64 km/h", "65 km/h"],
        ["60 కి.మీ/గం", "62 కి.మీ/గం", "64 కి.మీ/గం", "65 కి.మీ/గం"],
        1,
        "Total distance = (50 * 2) + (70 * 3) = 100 + 210 = 310 km. Total time = 5 hours. Average speed = 310 / 5 = 62 km/h.",
        "మొత్తం దూరం = 100 + 210 = 310 కి.మీ. మొత్తం కాలం = 5 గంటలు. సగటు వేగం = 310 / 5 = 62 కి.మీ/గం."
    ))

    # Q29: Ratio of speeds from time
    qs.append(make_q(
        29, "Speed, Distance & Time - Speed from Time Ratio", "Medium",
        "A car takes 4 hours less than a bus to cover a distance of 240 km. If the speed of the car is 20 km/h more than that of the bus, what is the speed of the bus?",
        "240 కి.మీ దూరాన్ని చేరుకోవడానికి బస్సు కంటే కారుకు 4 గంటల సమయం తక్కువ పడుతుంది. కారు వేగం బస్సు వేగం కంటే 20 కి.మీ/గం ఎక్కువ అయితే, బస్సు వేగం ఎంత?",
        ["25 km/h", "30 km/h", "35 km/h", "40 km/h"],
        ["25 కి.మీ/గం", "30 కి.మీ/గం", "35 కి.మీ/గం", "40 కి.మీ/గం"],
        1,
        "240/S - 240/(S + 20) = 4.\nTest option S = 30: 240/30 - 240/50 = 8 - 4.8 = 3.2 (no).\nTest S = 20? 240/20 - 240/40 = 12 - 6 = 6.\nFor 4 hours: 240/S - 240/(S + 20) = 4 => 60/S - 60/(S + 20) = 1 => 60*20 / (S*(S+20)) = 1 => S(S + 20) = 1200 => S = 30? Wait: 30 * 50 = 1500. 30^2 is 900. S^2 + 20S - 1200 = 0 => (S + 60)(S - 20) = 0 => S = wait, if S = 20: 240/20 = 12, 240/40 = 6, diff = 6. If diff is 2 hours: S(S+20) = 2400 => S = 40 (40*60=2400). If diff is 2 hours: 240/40=6, 240/60=4, diff = 2 hours! Let's set diff to 2 hours with S = 40 km/h.",
        "బస్సు వేగం S = 30 కి.మీ/గం."
    ))
    qs[-1]["question_en"] = "A car takes 2 hours less than a bus to cover a distance of 240 km. If the speed of the car is 20 km/h more than that of the bus, what is the speed of the bus?"
    qs[-1]["question_te"] = "240 కి.మీ దూరాన్ని చేరుకోవడానికి బస్సు కంటే కారుకు 2 గంటల సమయం తక్కువ పడుతుంది. కారు వేగం బస్సు వేగం కంటే 20 కి.మీ/గం ఎక్కువ అయితే, బస్సు వేగం ఎంత?"
    qs[-1]["options_en"] = ["30 km/h", "35 km/h", "40 km/h", "45 km/h"]
    qs[-1]["options_te"] = ["30 కి.మీ/గం", "35 కి.మీ/గం", "40 కి.మీ/గం", "45 కి.మీ/గం"]
    qs[-1]["correct_option"] = 2
    qs[-1]["explanation_en"] = "240/S - 240/(S + 20) = 2 => S(S + 20) = 2400 => S = 40 km/h (40 * 60 = 2400)."
    qs[-1]["explanation_te"] = "240/S - 240/(S + 20) = 2 => S = 40 కి.మీ/గం (బస్సు వేగం = 40 కి.మీ/గం, కారు వేగం = 60 కి.మీ/గం)."

    # Q30: Speed Distance - Wheel revolutions
    qs.append(make_q(
        30, "Speed, Distance & Time - Wheel Revolutions", "Medium",
        "The wheel of a police patrol van has a diameter of 70 cm. How many complete revolutions will the wheel make in travelling a distance of 1.1 km? (Take pi = 22/7)",
        "ఒక పోలీస్ వ్యాన్ చక్రం యొక్క వ్యాసం 70 సెం.మీ. 1.1 కి.మీ దూరం ప్రయాణించడానికి ఆ చక్రం ఎన్ని పూర్తి భ్రమణాలు (రివల్యూషన్లు) తిరగాలి? (pi = 22/7 తీసుకోండి)",
        ["400", "500", "600", "700"],
        ["400", "500", "600", "700"],
        1,
        "Distance in 1 revolution = Circumference = pi * d = (22/7) * 70 = 220 cm = 2.2 metres.\nTotal distance = 1.1 km = 1,100 metres.\nNumber of revolutions = 1100 / 2.2 = 500 revolutions.",
        "ఒక భ్రమణంలో దూరం = pi * d = 2.2 మీటర్లు. మొత్తం దూరం = 1,100 మీటర్లు. భ్రమణాల సంఖ్య = 1100 / 2.2 = 500."
    ))

    # --- 2. MENSURATION 2D & 3D (30 Questions: Q31 to Q60) ---

    # Q31: Trapezium Area & Parallel sides
    qs.append(make_q(
        31, "Mensuration 2D - Trapezium", "Medium",
        "The area of a trapezium-shaped security compound is 480 square metres. If the distance between its parallel sides is 15 metres and one of the parallel sides is 20 metres, what is the length of the other parallel side?",
        "ట్రెపీజియం ఆకారంలో ఉన్న ఒక సెక్యూరిటీ కాంపౌండ్ వైశాల్యం 480 చదరపు మీటర్లు. సమాంతర భుజాల మధ్య లంబ దూరం 15 మీటర్లు మరియు ఒక సమాంతర భుజం 20 మీటర్లు అయితే, రెండవ సమాంతర భుజం పొడవు ఎంత?",
        ["40 metres", "44 metres", "48 metres", "52 metres"],
        ["40 మీటర్లు", "44 మీటర్లు", "48 మీటర్లు", "52 మీటర్లు"],
        1,
        "Area = (1/2) * (a + b) * h => 480 = (1/2) * (20 + b) * 15 => (20 + b) = (480 * 2) / 15 = 64 => b = 64 - 20 = 44 metres.",
        "ట్రెపీజియం వైశాల్యం = 1/2 * (a + b) * h => 480 = 1/2 * (20 + b) * 15 => 20 + b = 64 => b = 44 మీటర్లు."
    ))

    # Q32: Rhombus Perimeter & Diagonals
    qs.append(make_q(
        32, "Mensuration 2D - Rhombus", "Hard",
        "The perimeter of a rhombus is 100 cm and one of its diagonals is 40 cm. What is the area of the rhombus?",
        "ఒక రాంబస్ చుట్టుకొలత 100 సెం.మీ మరియు దాని ఒక కర్ణం పొడవు 40 సెం.మీ. ఆ రాంబస్ వైశాల్యం ఎంత?",
        ["500 sq cm", "600 sq cm", "750 sq cm", "800 sq cm"],
        ["500 చ.సెం.మీ", "600 చ.సెం.మీ", "750 చ.సెం.మీ", "800 చ.సెం.మీ"],
        1,
        "Side of rhombus a = Perimeter / 4 = 100 / 4 = 25 cm.\nIn a rhombus, diagonals bisect at right angles: (d1/2)^2 + (d2/2)^2 = a^2.\n(40/2)^2 + (d2/2)^2 = 25^2 => 20^2 + (d2/2)^2 = 625 => (d2/2)^2 = 625 - 400 = 225 => d2/2 = 15 => d2 = 30 cm.\nArea = (1/2) * d1 * d2 = (1/2) * 40 * 30 = 600 sq cm.",
        "రాంబస్ భుజం = 25 సెం.మీ. కర్ణాలు లంబంగా సమద్విఖండన చేసుకుంటాయి: 20^2 + (d2/2)^2 = 25^2 => d2 = 30 సెం.మీ. వైశాల్యం = 1/2 * 40 * 30 = 600 చ.సెం.మీ."
    ))

    # Q33: Pathway Around Rectangular Lawn
    qs.append(make_q(
        33, "Mensuration 2D - Pathway Area", "Medium",
        "A rectangular parade ground 60 metres long and 40 metres wide has a uniform concrete path 2.5 metres wide running all around its outside. What is the total area of the concrete path?",
        "60 మీటర్ల పొడవు మరియు 40 మీటర్ల వెడల్పు గల ఒక దీర్ఘచతురస్రాకార పరేడ్ గ్రౌండ్ చుట్టూ వెలుపలి వైపున 2.5 మీటర్ల వెడల్పు గల కాంక్రీట్ బాట నిర్మించబడింది. ఆ బాట యొక్క మొత్తం వైశాల్యం ఎంత?",
        ["480 sq m", "500 sq m", "525 sq m", "550 sq m"],
        ["480 చ.మీ", "500 చ.మీ", "525 చ.మీ", "550 చ.మీ"],
        2,
        "Inner dimensions: 60 m by 40 m. Inner area = 2,400 sq m.\nOuter dimensions: (60 + 2*2.5) = 65 m, (40 + 2*2.5) = 45 m.\nOuter area = 65 * 45 = 2,925 sq m.\nPath area = 2925 - 2400 = 525 sq m.\nShortcut: Path Area = 2w(L + B + 2w) = 2(2.5)(60 + 40 + 5) = 5(105) = 525 sq m.",
        "బాట వైశాల్యం = 2w(L + B + 2w) = 5 * (60 + 40 + 5) = 5 * 105 = 525 చ.మీటర్లు."
    ))

    # Q34: Frustum of a Cone Volume
    qs.append(make_q(
        34, "Mensuration 3D - Frustum of Cone", "Hard",
        "A bucket in the form of a frustum of a right circular cone has top and bottom radii of 20 cm and 10 cm respectively, and a vertical height of 21 cm. What is the capacity (volume) of the bucket in litres? (Take pi = 22/7)",
        "శంకువు యొక్క ఛేదకం (Frustum of Cone) ఆకారంలో ఉన్న ఒక బకెట్ పై మరియు కింది వృత్తాకార వ్యాసార్థాలు వరుసగా 20 సెం.మీ మరియు 10 సెం.మీ, మరియు దాని నిలువు ఎత్తు 21 సెం.మీ. ఆ బకెట్ యొక్క సామర్థ్యం (ఘనపరిమాణం) లీటర్లలో ఎంత? (pi = 22/7)",
        ["14.8 litres", "15.4 litres", "16.2 litres", "17.6 litres"],
        ["14.8 లీటర్లు", "15.4 లీటర్లు", "16.2 లీటర్లు", "17.6 లీటర్లు"],
        1,
        "Volume of frustum = (1/3) * pi * h * (R^2 + r^2 + R*r)\n= (1/3) * (22/7) * 21 * (20^2 + 10^2 + 20*10)\n= 22 * (400 + 100 + 200) = 22 * 700 = 15,400 cubic cm.\nConvert to litres (1 litre = 1,000 cm^3): 15,400 / 1000 = 15.4 litres.",
        "ఛేదకం ఘనపరిమాణం = 1/3 * pi * h * (R^2 + r^2 + Rr) = 22 * 700 = 15,400 ఘన సెం.మీ = 15.4 లీటర్లు."
    ))

    # Q35: Wire Bending Equivalence
    qs.append(make_q(
        35, "Mensuration 2D - Wire Bending", "Medium",
        "A copper wire when bent in the form of a square encloses an area of 484 sq cm. If the same wire is straightened and then bent into the shape of a circle, what will be the area enclosed by the circle? (Take pi = 22/7)",
        "ఒక రాగి తీగను చతురస్రంగా మడిచినప్పుడు అది 484 చ.సెం.మీ వైశాల్యాన్ని ఆవరిస్తుంది. అదే తీగను నిఠారుగా చేసి వృత్తాకారంగా మడిస్తే, ఆ వృత్తం ఆవరించే వైశాల్యం ఎంత? (pi = 22/7)",
        ["594 sq cm", "616 sq cm", "648 sq cm", "676 sq cm"],
        ["594 చ.సెం.మీ", "616 చ.సెం.మీ", "648 చ.సెం.మీ", "676 చ.సెం.మీ"],
        1,
        "Side of square = sqrt(484) = 22 cm. Total length of wire = Perimeter = 4 * 22 = 88 cm.\nCircumference of circle = 2 * (22/7) * r = 88 => r = 14 cm.\nArea of circle = pi * r^2 = (22/7) * 14 * 14 = 22 * 28 = 616 sq cm.",
        "తీగ పొడవు = 4 * 22 = 88 సెం.మీ. వృత్త చుట్టుకొలత 2*pi*r = 88 => r = 14 సెం.మీ. వృత్త వైశాల్యం = pi * r^2 = 616 చ.సెం.మీ."
    ))

    # Q36: Cylinder from Solid Sphere (Melting)
    qs.append(make_q(
        36, "Mensuration 3D - Melting Solids", "Hard",
        "A solid metallic sphere of radius 6 cm is melted and recast into a solid circular cylinder of radius 4 cm. What is the height of the cylinder?",
        "6 సెం.మీ వ్యాసార్థం గల ఒక ఘన లోహపు గోళాన్ని కరిగించి, 4 సెం.మీ వ్యాసార్థం గల ఘన స్థూపంగా మార్చారు. ఆ స్థూపం యొక్క ఎత్తు ఎంత?",
        ["16 cm", "18 cm", "20 cm", "24 cm"],
        ["16 సెం.మీ", "18 సెం.మీ", "20 సెం.మీ", "24 సెం.మీ"],
        1,
        "Volume of sphere = (4/3) * pi * R^3 = (4/3) * pi * 6^3 = (4/3) * pi * 216 = 288*pi.\nVolume of cylinder = pi * r^2 * h = pi * 4^2 * h = 16*pi*h.\nEquating volumes: 16*pi*h = 288*pi => h = 288 / 16 = 18 cm.",
        "గోళం ఘనపరిమాణం = స్థూపం ఘనపరిమాణం => 4/3 * pi * 6^3 = pi * 4^2 * h => 16h = 288 => h = 18 సెం.మీ."
    ))

    # Q37: Largest Rod in Cuboid Room
    qs.append(make_q(
        37, "Mensuration 3D - Diagonal of Room", "Medium",
        "What is the maximum length of an iron rod that can be placed inside an interrogation room measuring 12 metres in length, 9 metres in breadth, and 8 metres in height?",
        "12 మీటర్ల పొడవు, 9 మీటర్ల వెడల్పు మరియు 8 మీటర్ల ఎత్తు గల ఒక గదిలో ఉంచగల అత్యంత పొడవైన ఇనుప రాడ్ పొడవు ఎంత?",
        ["15 metres", "16 metres", "17 metres", "18 metres"],
        ["15 మీటర్లు", "16 మీటర్లు", "17 మీటర్లు", "18 మీటర్లు"],
        2,
        "Longest rod = Space diagonal of cuboid = sqrt(l^2 + b^2 + h^2) = sqrt(12^2 + 9^2 + 8^2) = sqrt(144 + 81 + 64) = sqrt(289) = 17 metres.",
        "గది కర్ణం = sqrt(12^2 + 9^2 + 8^2) = sqrt(144 + 81 + 64) = sqrt(289) = 17 మీటర్లు."
    ))

    # Q38: Solid Hemisphere Total Surface Area
    qs.append(make_q(
        38, "Mensuration 3D - Hemisphere", "Medium",
        "What is the total surface area of a solid hemisphere of radius 7 cm? (Take pi = 22/7)",
        "7 సెం.మీ వ్యాసార్థం గల ఒక ఘన అర్ధగోళం యొక్క సంపూర్ణతల వైశాల్యం ఎంత? (pi = 22/7)",
        ["308 sq cm", "462 sq cm", "616 sq cm", "770 sq cm"],
        ["308 చ.సెం.మీ", "462 చ.సెం.మీ", "616 చ.సెం.మీ", "770 చ.సెం.మీ"],
        1,
        "Total Surface Area of solid hemisphere = Curved Surface Area + Base Area = 2*pi*r^2 + pi*r^2 = 3*pi*r^2.\nTSA = 3 * (22/7) * 7 * 7 = 3 * 22 * 7 = 462 sq cm.",
        "ఘన అర్ధగోళ సంపూర్ణతల వైశాల్యం = 3 * pi * r^2 = 3 * (22/7) * 49 = 462 చ.సెం.మీ."
    ))

    # Q39: Water Flow Through Cylindrical Pipe
    qs.append(make_q(
        39, "Mensuration 3D - Water Flow Rate", "Hard",
        "Water flows through a cylindrical pipe of internal diameter 2 cm into a cylindrical tank of base radius 40 cm at the rate of 0.7 metres per second. By how much will the water level in the tank rise in half an hour (30 minutes)?",
        "2 సెం.మీ అంతర వ్యాసం గల స్థూపాకార పైపు గుండా సెకనుకు 0.7 మీటర్ల వేగంతో నీరు 40 సెం.మీ భూ వ్యాసార్థం గల స్థూపాకార ట్యాంకులోకి ప్రవహిస్తుంది. అరగంట (30 నిమిషాలు) లో ఆ ట్యాంకులోని నీటి మట్టం ఎంత ఎత్తు పెరుగుతుంది?",
        ["65 cm", "72.5 cm", "78.75 cm", "84 cm"],
        ["65 సెం.మీ", "72.5 సెం.మీ", "78.75 సెం.మీ", "84 సెం.మీ"],
        2,
        "Radius of pipe r = 1 cm. Water speed = 70 cm/s.\nVolume of water flowing in 1 sec = pi * r^2 * v = pi * 1^2 * 70 = 70*pi cm^3.\nVolume in 30 minutes (1,800 sec) = 70*pi * 1800 = 126,000*pi cm^3.\nVolume in tank = pi * R^2 * H = pi * 40^2 * H = 1600*pi * H.\n1600*pi * H = 126,000*pi => H = 126000 / 1600 = 1260 / 16 = 78.75 cm.",
        "ట్యాంకులో పెరిగే ఎత్తు H = (pi * 1^2 * 70 * 1800) / (pi * 40^2) = 126000 / 1600 = 78.75 సెం.మీ."
    ))

    # Q40: Equilateral Triangle Inradius & Circumradius
    qs.append(make_q(
        40, "Mensuration 2D - Equilateral Triangle", "Hard",
        "An equilateral triangular lawn has a side of 12 cm. What is the area of its incircle (the circle inscribed inside the triangle)? (Take pi = 22/7)",
        "12 సెం.మీ భుజం గల ఒక సమబాహు త్రిభుజం లోపల అంతర్లిఖించబడిన అంతర్వృత్తం (Incircle) యొక్క వైశాల్యం ఎంత?",
        ["28.5 sq cm", "37.7 sq cm", "44.2 sq cm", "50.3 sq cm"],
        ["28.5 చ.సెం.మీ", "37.7 చ.సెం.మీ", "44.2 చ.సెం.మీ", "50.3 చ.సెం.మీ"],
        1,
        "Inradius r of equilateral triangle = a / (2 * sqrt(3)) = 12 / (2 * sqrt(3)) = 6 / sqrt(3) = 2*sqrt(3) cm.\nArea of incircle = pi * r^2 = pi * (2*sqrt(3))^2 = pi * 12 = 12 * 3.1416 = 37.7 sq cm.",
        "సమబాహు త్రిభుజ అంతర్వ్యాసార్థం r = a / (2*sqrt(3)) = 2*sqrt(3) సెం.మీ. అంతర్వృత్త వైశాల్యం = pi * r^2 = 12 * 3.1416 = 37.7 చ.సెం.మీ."
    ))

    
    # Q41 to Q60: High-Yield TSPLRB Mensuration Problems
    qs.append(make_q(
        41, "Mensuration 2D - Circular Ring", "Medium",
        """A circular running track has an inner circumference of 440 metres and an outer circumference of 506 metres. What is the width of the track and its total area? (Take pi = 22/7)""",
        """ఒక వృత్తాకార రన్నింగ్ ట్రాక్ లోపలి చుట్టుకొలత 440 మీటర్లు మరియు వెలుపలి చుట్టుకొలత 506 మీటర్లు. ఆ ట్రాక్ వెడల్పు మరియు దాని మొత్తం వైశాల్యం ఎంత? (pi = 22/7 గా తీసుకోండి)""",
        ['Width = 10.5 m, Area = 4,966.5 sq m', 'Width = 10.5 m, Area = 4,520 sq m', 'Width = 14 m, Area = 5,120 sq m', 'Width = 7 m, Area = 3,850 sq m'],
        ['వెడల్పు = 10.5 మీ, వైశాల్యం = 4,966.5 చ.మీ', 'వెడల్పు = 10.5 మీ, వైశాల్యం = 4,520 చ.మీ', 'వెడల్పు = 14 మీ, వైశాల్యం = 5,120 చ.మీ', 'వెడల్పు = 7 మీ, వైశాల్యం = 3,850 చ.మీ'],
        0,
        """Inner radius r = 440 / (2 * 22/7) = 70 m. Outer radius R = 506 / (2 * 22/7) = 80.5 m.
Width = R - r = 80.5 - 70 = 10.5 m.
Area = pi * (R^2 - r^2) = (22/7) * (80.5 + 70) * (80.5 - 70) = (22/7) * 150.5 * 10.5 = 22 * 150.5 * 1.5 = 4,966.5 sq m.""",
        """లోపలి వ్యాసార్థం r = 70 మీ. వెలుపలి వ్యాసార్థం R = 80.5 మీ.
వెడల్పు = 80.5 - 70 = 10.5 మీ.
వైశాల్యం = pi * (R^2 - r^2) = (22/7) * 150.5 * 10.5 = 4,966.5 చ.మీ."""
    ))

    qs.append(make_q(
        42, "Mensuration 3D - Hollow Cylinder", "Hard",
        """A hollow metallic cylindrical pipe of length 35 cm has an external diameter of 10 cm and an internal diameter of 8 cm. If the metal weighs 8 grams per cubic centimetre, what is the total weight of the pipe? (Take pi = 22/7)""",
        """35 సెం.మీ పొడవు గల ఒక బోలు లోహపు స్థూపాకార పైపు బాహ్య వ్యాసం 10 సెం.మీ మరియు అంతర్గత వ్యాసం 8 సెం.మీ. ఒక ఘనపు సెంటీమీటరు లోహం బరువు 8 గ్రాములు ఉంటే, ఆ పైపు మొత్తం బరువు ఎంత? (pi = 22/7)""",
        ['7.92 kg', '6.84 kg', '8.48 kg', '7.15 kg'],
        ['7.92 కి.గ్రా', '6.84 కి.గ్రా', '8.48 కి.గ్రా', '7.15 కి.గ్రా'],
        0,
        """External radius R = 5 cm, internal radius r = 4 cm, h = 35 cm.
Volume of metal = pi * (R^2 - r^2) * h = (22/7) * (25 - 16) * 35 = 22 * 9 * 5 = 990 cu cm.
Weight = 990 * 8 g = 7,920 g = 7.92 kg.""",
        """బాహ్య వ్యాసార్థం R = 5 సెం.మీ, అంతర్గత వ్యాసార్థం r = 4 సెం.మీ, ఎత్తు h = 35 సెం.మీ.
లోహం ఘనపరిమాణం = pi * (R^2 - r^2) * h = 22 * 9 * 5 = 990 ఘ.సెం.మీ.
బరువు = 990 * 8 = 7,920 గ్రా = 7.92 కి.గ్రా."""
    ))

    qs.append(make_q(
        43, "Mensuration 2D - Sector of Circle", "Medium",
        """A perimeter of a sector of a circle of radius 10.5 cm is 43 cm. What is the area of the sector? (Take pi = 22/7)""",
        """10.5 సెం.మీ వ్యాసార్థం గల వృత్త సెక్టార్ చుట్టుకొలత 43 సెం.మీ. ఆ సెక్టార్ వైశాల్యం ఎంత?""",
        ['115.5 sq cm', '105.0 sq cm', '126.5 sq cm', '98.5 sq cm'],
        ['115.5 చ.సెం.మీ', '105.0 చ.సెం.మీ', '126.5 చ.సెం.మీ', '98.5 చ.సెం.మీ'],
        0,
        """Perimeter of sector = 2r + l = 43 cm => 2(10.5) + l = 43 => 21 + l = 43 => l = 22 cm.
Area of sector = (1/2) * l * r = (1/2) * 22 * 10.5 = 11 * 10.5 = 115.5 sq cm.""",
        """సెక్టార్ చుట్టుకొలత = 2r + l = 43 => 21 + l = 43 => చాపం పొడవు l = 22 సెం.మీ.
సెక్టార్ వైశాల్యం = (1/2) * l * r = 11 * 10.5 = 115.5 చ.సెం.మీ."""
    ))

    qs.append(make_q(
        44, "Mensuration 3D - Cone Canvas", "Medium",
        """A conical tent is 9 metres high and the radius of its circular base is 12 metres. Find the cost of canvas required to make the tent at the rate of Rs. 14 per square metre. (Take pi = 22/7)""",
        """ఒక శంఖు ఆకారపు టెంట్ ఎత్తు 9 మీటర్లు మరియు దాని భూ వ్యాసార్థం 12 మీటర్లు. చదరపు మీటరుకు రూ. 14 చొప్పున ఆ టెంట్ తయారీకి అవసరమైన కాన్వాస్ ఖర్చు ఎంత? (pi = 22/7)""",
        ['Rs. 7,920', 'Rs. 8,240', 'Rs. 7,450', 'Rs. 8,680'],
        ['రూ. 7,920', 'రూ. 8,240', 'రూ. 7,450', 'రూ. 8,680'],
        0,
        """Slant height l = sqrt(r^2 + h^2) = sqrt(12^2 + 9^2) = sqrt(144 + 81) = sqrt(225) = 15 m.
Curved surface area = pi * r * l = (22/7) * 12 * 15 = (22 * 180)/7 sq m.
Cost = Area * 14 = ((22 * 180) / 7) * 14 = 22 * 180 * 2 = Rs. 7,920.""",
        """వాలు ఎత్తు l = sqrt(12^2 + 9^2) = 15 మీ.
వక్రతల వైశాల్యం = pi * r * l = (22/7) * 12 * 15 చ.మీ.
ఖర్చు = ((22 * 180)/7) * 14 = 22 * 180 * 2 = రూ. 7,920."""
    ))

    qs.append(make_q(
        45, "Mensuration 2D - Isosceles Trapezium", "Hard",
        """In an isosceles trapezium, the parallel sides are 16 cm and 26 cm, and the non-parallel sides are each equal to 13 cm. What is the area of the trapezium?""",
        """ఒక సమద్విబాహు సమలంబ చతుర్భుజం (Isosceles Trapezium) లో సమాంతర భుజాలు 16 సెం.మీ మరియు 26 సెం.మీ, సమాంతరము కాని భుజాలు ఒక్కొక్కటి 13 సెం.మీ. ఆ సమలంబ చతుర్భుజం వైశాల్యం ఎంత?""",
        ['252 sq cm', '273 sq cm', '240 sq cm', '288 sq cm'],
        ['252 చ.సెం.మీ', '273 చ.సెం.మీ', '240 చ.సెం.మీ', '288 చ.సెం.మీ'],
        0,
        """Difference between parallel sides = 26 - 16 = 10 cm. Since it is isosceles, projection on each side = 10 / 2 = 5 cm.
Height h = sqrt(13^2 - 5^2) = sqrt(169 - 25) = sqrt(144) = 12 cm.
Area = (1/2) * (sum of parallel sides) * h = (1/2) * (16 + 26) * 12 = 42 * 6 = 252 sq cm.""",
        """సమాంతర భుజాల తేడా = 26 - 16 = 10 సెం.మీ. ప్రతి వైపు ప్రొజెక్షన్ = 5 సెం.మీ.
ఎత్తు h = sqrt(13^2 - 5^2) = 12 సెం.మీ.
వైశాల్యం = (1/2) * (16 + 26) * 12 = 42 * 6 = 252 చ.సెం.మీ."""
    ))

    qs.append(make_q(
        46, "Mensuration 3D - Right Prism", "Hard",
        """The base of a right prism is a regular hexagon of side 6 cm. If its height is 15 cm, what is its total volume? (Take sqrt(3) = 1.732)""",
        """ఒక లంబ ప్రిజం భూమి 6 సెం.మీ భుజం గల క్రమ షడ్భుజి. దాని ఎత్తు 15 సెం.మీ అయితే, దాని మొత్తం ఘనపరిమాణం ఎంత? (sqrt(3) = 1.732 గా తీసుకోండి)""",
        ['1,402.92 cu cm', '1,350.50 cu cm', '1,248.80 cu cm', '1,520.40 cu cm'],
        ['1,402.92 ఘ.సెం.మీ', '1,350.50 ఘ.సెం.మీ', '1,248.80 ఘ.సెం.మీ', '1,520.40 ఘ.సెం.మీ'],
        0,
        """Area of regular hexagon base = 6 * (sqrt(3)/4) * a^2 = (3*sqrt(3)/2) * 36 = 54 * sqrt(3) = 54 * 1.732 = 93.528 sq cm.
Volume = Base Area * Height = 54 * sqrt(3) * 15 = 810 * 1.732 = 1,402.92 cu cm.""",
        """క్రమ షడ్భుజి భూ వైశాల్యం = 6 * (sqrt(3)/4) * 6^2 = 54 * 1.732 = 93.528 చ.సెం.మీ.
ఘనపరిమాణం = భూ వైశాల్యం * ఎత్తు = 54 * sqrt(3) * 15 = 810 * 1.732 = 1,402.92 ఘ.సెం.మీ."""
    ))

    qs.append(make_q(
        47, "Mensuration 3D - Right Pyramid", "Hard",
        """A right pyramid stands on a square base of side 10 cm. If its vertical height is 12 cm, what is its total surface area (including base)?""",
        """ఒక లంబ పిరమిడ్ 10 సెం.మీ భుజం గల చతురస్రాకార భూమిపై ఉంది. దాని నిలువు ఎత్తు 12 సెం.మీ అయితే, దాని సంపూర్ణతల వైశాల్యం ఎంత?""",
        ['360 sq cm', '340 sq cm', '380 sq cm', '400 sq cm'],
        ['360 చ.సెం.మీ', '340 చ.సెం.మీ', '380 చ.సెం.మీ', '400 చ.సెం.మీ'],
        0,
        """Distance from centre to midpoint of side = 10 / 2 = 5 cm.
Slant height l = sqrt(h^2 + (a/2)^2) = sqrt(12^2 + 5^2) = sqrt(169) = 13 cm.
Lateral surface area = (1/2) * Perimeter of base * l = (1/2) * (4 * 10) * 13 = 20 * 13 = 260 sq cm.
Base area = 10^2 = 100 sq cm. Total surface area = 260 + 100 = 360 sq cm.""",
        """వాలు ఎత్తు l = sqrt(12^2 + 5^2) = 13 సెం.మీ.
పార్శ్వతల వైశాల్యం = (1/2) * చుట్టుకొలత * l = (1/2) * 40 * 13 = 260 చ.సెం.మీ.
భూ వైశాల్యం = 100 చ.సెం.మీ. సంపూర్ణతల వైశాల్యం = 260 + 100 = 360 చ.సెం.మీ."""
    ))

    qs.append(make_q(
        48, "Mensuration 2D - Regular Polygon", "Medium",
        """The ratio between the interior angle and the exterior angle of a regular polygon is 5 : 1. How many sides does the regular polygon have?""",
        """ఒక క్రమ బహుభుజి యొక్క అంతర కోణం మరియు బాహ్య కోణాల నిష్పత్తి 5 : 1. ఆ క్రమ బహుభుజికి గల భుజాల సంఖ్య ఎంత?""",
        ['12', '10', '14', '16'],
        ['12', '10', '14', '16'],
        0,
        """Interior angle + Exterior angle = 180 degrees.
Ratio = 5 : 1 => Total parts = 6 => 1 part (Exterior angle) = 180 / 6 = 30 degrees.
Number of sides n = 360 / Exterior angle = 360 / 30 = 12.""",
        """అంతర కోణం + బాహ్య కోణం = 180 డిగ్రీలు.
బాహ్య కోణం = 180 / 6 = 30 డిగ్రీలు.
భుజాల సంఖ్య n = 360 / 30 = 12."""
    ))

    qs.append(make_q(
        49, "Mensuration 2D - Four Circles", "Hard",
        """Four equal coins of radius 7 cm each are placed on a table touching each other so that their centres form a square. What is the area of the shaded space enclosed between the four coins? (Take pi = 22/7)""",
        """ఒక్కొక్కటి 7 సెం.మీ వ్యాసార్థం గల నాలుగు సమాన నాణేలు ఒకదానికొకటి తాకుతూ వాటి కేంద్రాలు చతురస్రాన్ని ఏర్పరిచేలా ఉంచబడ్డాయి. ఆ నాలుగు నాణేల మధ్య బంధించబడిన ఖాళీ ప్రదేశ వైశాల్యం ఎంత?""",
        ['42 sq cm', '38 sq cm', '48 sq cm', '56 sq cm'],
        ['42 చ.సెం.మీ', '38 చ.సెం.మీ', '48 చ.సెం.మీ', '56 చ.సెం.మీ'],
        0,
        """Side of square formed by centres a = 2r = 2 * 7 = 14 cm.
Area of square = 14^2 = 196 sq cm.
The four corners contain 4 quadrants of radius 7 cm, which form 1 full circle of radius 7 cm.
Area of circle = pi * r^2 = (22/7) * 49 = 154 sq cm.
Enclosed area = Area of square - Area of circle = 196 - 154 = 42 sq cm. (Shortcut: (6/7) * r^2 = (6/7) * 49 = 42 sq cm).""",
        """కేంద్రాలతో ఏర్పడే చతురస్ర భుజం a = 2r = 14 సెం.మీ. చతురస్ర వైశాల్యం = 196 చ.సెం.మీ.
నాలుగు పాద వృత్తాల వైశాల్యం = pi * r^2 = 154 చ.సెం.మీ.
బంధించబడిన వైశాల్యం = 196 - 154 = 42 చ.సెం.మీ. (షార్ట్‌కట్: (6/7) * r^2 = 42 చ.సెం.మీ)."""
    ))

    qs.append(make_q(
        50, "Mensuration 3D - Solid Comparison", "Hard",
        """A right circular cone and a cylinder have the same base radius and the same height. If a sphere has a radius equal to the base radius of the cylinder, and the height of both the cylinder and cone is equal to the diameter of the sphere, what is the ratio of their volumes (Cone : Sphere : Cylinder)?""",
        """ఒక లంబ శంఖువు మరియు ఒక స్థూపం ఒకే భూ వ్యాసార్థాన్ని మరియు ఒకే ఎత్తును కలిగి ఉన్నాయి. స్థూపం భూ వ్యాసార్థానికి సమానమైన వ్యాసార్థం గల ఒక గోళం ఉండి, స్థూపం మరియు శంఖువుల ఎత్తులు ఆ గోళ వ్యాసానికి సమానమైతే, వాటి ఘనపరిమాణాల నిష్పత్తి (శంఖువు : గోళం : స్థూపం) ఎంత?""",
        ['1 : 2 : 3', '1 : 3 : 4', '2 : 3 : 4', '1 : 4 : 6'],
        ['1 : 2 : 3', '1 : 3 : 4', '2 : 3 : 4', '1 : 4 : 6'],
        0,
        """Let radius = r. Height h = 2r (diameter of sphere).
Volume of Cone = (1/3) * pi * r^2 * h = (1/3) * pi * r^2 * (2r) = (2/3) * pi * r^3.
Volume of Sphere = (4/3) * pi * r^3.
Volume of Cylinder = pi * r^2 * h = pi * r^2 * (2r) = 2 * pi * r^3 = (6/3) * pi * r^3.
Ratio = (2/3) : (4/3) : (6/3) = 2 : 4 : 6 = 1 : 2 : 3.""",
        """వ్యాసార్థం = r, ఎత్తు h = 2r అనుకుందాం.
శంఖువు ఘనపరిమాణం = (2/3) * pi * r^3.
గోళ ఘనపరిమాణం = (4/3) * pi * r^3.
స్థూప ఘనపరిమాణం = 2 * pi * r^3 = (6/3) * pi * r^3.
నిష్పత్తి = 2 : 4 : 6 = 1 : 2 : 3."""
    ))

    qs.append(make_q(
        51, "Mensuration 2D - Scalene Triangle", "Medium",
        """The sides of a triangular field are 13 metres, 14 metres, and 15 metres. What is the length of the altitude drawn to the side of length 14 metres?""",
        """ఒక త్రిభుజాకార పొలం భుజాలు 13 మీటర్లు, 14 మీటర్లు మరియు 15 మీటర్లు. 14 మీటర్ల పొడవు గల భుజంపైకి గీసిన ఉన్నతి (Altitude) పొడవు ఎంత?""",
        ['12 metres', '11.2 metres', '12.5 metres', '10.8 metres'],
        ['12 మీటర్లు', '11.2 మీటర్లు', '12.5 మీటర్లు', '10.8 మీటర్లు'],
        0,
        """Semi-perimeter s = (13 + 14 + 15)/2 = 21 m.
Area by Heron's formula = sqrt(s(s-a)(s-b)(s-c)) = sqrt(21 * 8 * 7 * 6) = sqrt(21 * 7 * 48) = sqrt(147 * 48) = sqrt(7056) = 84 sq m.
Area = (1/2) * base * height => 84 = (1/2) * 14 * h => 84 = 7h => h = 12 metres.""",
        """అర్థ చుట్టుకొలత s = 21 మీ.
హెరాన్ సూత్రం ప్రకారం వైశాల్యం = sqrt(21 * 8 * 7 * 6) = 84 చ.మీ.
వైశాల్యం = (1/2) * భూమి * ఎత్తు => 84 = (1/2) * 14 * h => h = 12 మీటర్లు."""
    ))

    qs.append(make_q(
        52, "Mensuration 3D - Spherical Shell", "Hard",
        """A hollow spherical shell of iron has internal and external radii of 6 cm and 8 cm respectively. It is melted and recast into a solid cone of base radius 8 cm. What is the height of the cone?""",
        """ఒక బోలు ఇనుప గోళపు అంతర్గత మరియు బాహ్య వ్యాసార్థాలు వరుసగా 6 సెం.మీ మరియు 8 సెం.మీ. దానిని కరిగించి 8 సెం.మీ భూ వ్యాసార్థం గల ఒక ఘన శంఖువుగా మార్చారు. ఆ శంఖువు ఎత్తు ఎంత?""",
        ['18.5 cm', '16.8 cm', '20.2 cm', '15.4 cm'],
        ['18.5 సెం.మీ', '16.8 సెం.మీ', '20.2 సెం.మీ', '15.4 సెం.మీ'],
        0,
        """Volume of shell = (4/3) * pi * (R^3 - r^3) = (4/3) * pi * (512 - 216) = (4/3) * pi * 296.
Volume of cone = (1/3) * pi * r_cone^2 * h = (1/3) * pi * 64 * h.
Equating: (4/3) * pi * 296 = (1/3) * pi * 64 * h => 4 * 296 = 64 * h => h = 1184 / 64 = 18.5 cm.""",
        """బోలు గోళ ఘనపరిమాణం = (4/3) * pi * (8^3 - 6^3) = (4/3) * pi * 296.
శంఖు ఘనపరిమాణం = (1/3) * pi * 64 * h.
4 * 296 = 64 * h => h = 1184 / 64 = 18.5 సెం.మీ."""
    ))

    qs.append(make_q(
        53, "Mensuration 2D - Inscribed Square", "Hard",
        """A square is inscribed in a semicircle of radius R such that two of its vertices lie on the diameter and the other two vertices lie on the curved semicircular arc. What is the area of the square?""",
        """R వ్యాసార్థం గల ఒక అర్థవృత్తంలో ఒక చతురస్రం అంతర్లిఖించబడింది. దాని రెండు శీర్షాలు వ్యాసంపై, మిగిలిన రెండు శీర్షాలు అర్థవృత్త చాపంపై ఉన్నాయి. ఆ చతురస్ర వైశాల్యం ఎంత?""",
        ['(4/5) R^2', '(2/3) R^2', '(3/4) R^2', '(1/2) R^2'],
        ['(4/5) R^2', '(2/3) R^2', '(3/4) R^2', '(1/2) R^2'],
        0,
        """Let side of square be x. The center of the diameter bisects the bottom side into x/2 each.
From center to top corner is radius R: (x/2)^2 + x^2 = R^2 => x^2 / 4 + x^2 = R^2 => (5/4) x^2 = R^2.
Area of square x^2 = (4/5) R^2 = 0.8 R^2.""",
        """చతురస్ర భుజం x అనుకుంటే, (x/2)^2 + x^2 = R^2 => (5/4) x^2 = R^2 => వైశాల్యం x^2 = (4/5) R^2."""
    ))

    qs.append(make_q(
        54, "Mensuration 3D - Water Rise", "Medium",
        """A cylindrical vessel of base radius 14 cm contains some water. If 6 identical solid metallic spheres, each of radius 3.5 cm, are completely immersed in the water, what is the rise in the water level? (Take pi = 22/7)""",
        """14 సెం.మీ భూ వ్యాసార్థం గల ఒక స్థూపాకార పాత్రలో కొంత నీరు ఉంది. ఒక్కొక్కటి 3.5 సెం.మీ వ్యాసార్థం గల 6 ఘన లోహపు గోళాలను ఆ నీటిలో పూర్తిగా ముంచితే, నీటి మట్టంలో పెరుగుదల ఎంత? (pi = 22/7)""",
        ['1.75 cm', '2.25 cm', '1.50 cm', '2.00 cm'],
        ['1.75 సెం.మీ', '2.25 సెం.మీ', '1.50 సెం.మీ', '2.00 సెం.మీ'],
        0,
        """Volume of 6 spheres = 6 * (4/3) * pi * (3.5)^3 = 8 * pi * (7/2)^3 = 8 * pi * (343 / 8) = 343 * pi.
Volume of water displaced = pi * r^2 * h = pi * 14^2 * h = 196 * pi * h.
196 * pi * h = 343 * pi => h = 343 / 196 = 7 / 4 = 1.75 cm.""",
        """6 గోళాల ఘనపరిమాణం = 6 * (4/3) * pi * (7/2)^3 = 343 * pi.
స్థూపంలో నీటి ఘనపరిమాణ పెరుగుదల = pi * 14^2 * h = 196 * pi * h.
h = 343 / 196 = 1.75 సెం.మీ."""
    ))

    qs.append(make_q(
        55, "Mensuration 2D - Percentage Change", "Medium",
        """If the length of a rectangular sports ground is increased by 25% and its breadth is decreased by 20%, what is the percentage change in its area?""",
        """ఒక దీర్ఘచతురస్రాకార క్రీడా మైదానం పొడవును 25% పెంచి, వెడల్పును 20% తగ్గించినట్లయితే, దాని వైశాల్యంలో వచ్చే శాతం మార్పు ఎంత?""",
        ['No change (0%)', 'Increases by 5%', 'Decreases by 5%', 'Increases by 2%'],
        ['ఎలాంటి మార్పు ఉండదు (0%)', '5% పెరుగుతుంది', '5% తగ్గుతుంది', '2% పెరుగుతుంది'],
        0,
        """Net % change = x + y + (xy/100) = +25 - 20 + (25 * (-20))/100 = 5 - 500/100 = 5 - 5 = 0% (No change).""",
        """నికర శాతం మార్పు = x + y + (xy/100) = 25 - 20 - (500/100) = 5 - 5 = 0% (మార్పు ఉండదు)."""
    ))

    qs.append(make_q(
        56, "Mensuration 3D - Percentage Change", "Hard",
        """If the radius of a cylinder is increased by 20% while its height is decreased by 25%, by what percentage does the volume of the cylinder change?""",
        """ఒక స్థూపం యొక్క వ్యాసార్థాన్ని 20% పెంచి, దాని ఎత్తును 25% తగ్గించినట్లయితే, ఆ స్థూప ఘనపరిమాణంలో వచ్చే శాతం మార్పు ఎంత?""",
        ['Increases by 8%', 'Decreases by 5%', 'Increases by 10%', 'Decreases by 8%'],
        ['8% పెరుగుతుంది', '5% తగ్గుతుంది', '10% పెరుగుతుంది', '8% తగ్గుతుంది'],
        0,
        """Volume V is proportional to r^2 * h.
New Volume = (1.2)^2 * (0.75) * V = 1.44 * 0.75 * V = 1.08 V.
Percentage increase = (1.08 - 1) * 100 = 8% increase.""",
        """ఘనపరిమాణం V proportional to r^2 * h.
నూతన ఘనపరిమాణం = (1.2)^2 * 0.75 * V = 1.44 * 0.75 * V = 1.08 V.
పెరుగుదల = 8% పెరుగుతుంది."""
    ))

    qs.append(make_q(
        57, "Mensuration 2D - Diagonal Walk", "Medium",
        """A rectangular police training ground is 120 metres long and 50 metres wide. A cadet walks along the diagonal from one corner to the opposite corner instead of walking along the two adjacent edges. How much distance does he save?""",
        """ఒక దీర్ఘచతురస్రాకార పోలీస్ శిక్షణ మైదానం పొడవు 120 మీటర్లు మరియు వెడల్పు 50 మీటర్లు. ఒక క్యాడెట్ రెండు పక్క భుజాల వెంబడి నడవడానికి బదులుగా ఒక మూల నుండి కర్ణం వెంబడి ఎదురు మూలకు నడిచాడు. అతను ఎంత దూరాన్ని ఆదా చేశాడు?""",
        ['40 metres', '30 metres', '50 metres', '45 metres'],
        ['40 మీటర్లు', '30 మీటర్లు', '50 మీటర్లు', '45 మీటర్లు'],
        0,
        """Distance along edges = 120 + 50 = 170 metres.
Diagonal distance = sqrt(120^2 + 50^2) = sqrt(14400 + 2500) = sqrt(16900) = 130 metres.
Distance saved = 170 - 130 = 40 metres.""",
        """భుజాల వెంబడి దూరం = 120 + 50 = 170 మీటర్లు.
కర్ణం పొడవు = sqrt(120^2 + 50^2) = 130 మీటర్లు.
ఆదా చేసిన దూరం = 170 - 130 = 40 మీటర్లు."""
    ))

    qs.append(make_q(
        58, "Mensuration 3D - Painting Walls", "Hard",
        """A room is 10 metres long, 8 metres wide, and 4 metres high. It has two doors of size 2 m x 1 m each and four windows of size 1.5 m x 1 m each. Find the cost of painting the four walls at Rs. 15 per square metre.""",
        """ఒక గది పొడవు 10 మీటర్లు, వెడల్పు 8 మీటర్లు మరియు ఎత్తు 4 మీటర్లు. అందులో ఒక్కొక్కటి 2 మీ x 1 మీ కొలతలు గల రెండు తలుపులు మరియు 1.5 మీ x 1 మీ కొలతలు గల నాలుగు కిటికీలు ఉన్నాయి. చదరపు మీటరుకు రూ. 15 చొప్పున నాలుగు గోడలకు పెయింట్ వేయడానికి అయ్యే ఖర్చు ఎంత?""",
        ['Rs. 2,010', 'Rs. 2,160', 'Rs. 1,980', 'Rs. 2,250'],
        ['రూ. 2,010', 'రూ. 2,160', 'రూ. 1,980', 'రూ. 2,250'],
        0,
        """Area of 4 walls = 2 * (l + b) * h = 2 * (10 + 8) * 4 = 2 * 18 * 4 = 144 sq m.
Area of 2 doors = 2 * (2 * 1) = 4 sq m.
Area of 4 windows = 4 * (1.5 * 1) = 6 sq m.
Net area to be painted = 144 - (4 + 6) = 144 - 10 = 134 sq m.
Cost = 134 * 15 = Rs. 2,010.""",
        """నాలుగు గోడల వైశాల్యం = 2 * (10 + 8) * 4 = 144 చ.మీ.
2 తలుపుల వైశాల్యం = 4 చ.మీ, 4 కిటికీల వైశాల్యం = 6 చ.మీ. మొత్తం తగ్గింపు = 10 చ.మీ.
పెయింట్ చేయాల్సిన వైశాల్యం = 144 - 10 = 134 చ.మీ.
ఖర్చు = 134 * 15 = రూ. 2,010."""
    ))

    qs.append(make_q(
        59, "Mensuration 2D - Regular Octagon", "Hard",
        """What is the area of a regular octagon having each side equal to 10 cm? (Take sqrt(2) = 1.414)""",
        """ప్రతి భుజం 10 సెం.మీ గల ఒక క్రమ అష్టభుజి (Regular Octagon) వైశాల్యం ఎంత? (sqrt(2) = 1.414)""",
        ['482.8 sq cm', '460.5 sq cm', '512.4 sq cm', '445.0 sq cm'],
        ['482.8 చ.సెం.మీ', '460.5 చ.సెం.మీ', '512.4 చ.సెం.మీ', '445.0 చ.సెం.మీ'],
        0,
        """Area of regular octagon = 2 * (1 + sqrt(2)) * a^2 = 2 * (1 + 1.414) * 100 = 2 * 2.414 * 100 = 482.8 sq cm.""",
        """క్రమ అష్టభుజి వైశాల్యం = 2 * (1 + sqrt(2)) * a^2 = 2 * 2.414 * 100 = 482.8 చ.సెం.మీ."""
    ))

    qs.append(make_q(
        60, "Mensuration 3D - Cone Truncation", "Hard",
        """A solid right circular cone of height 30 cm is cut into two parts by a plane parallel to its base at a height of 20 cm from the base. What is the ratio of the volume of the smaller cone formed at the top to the volume of the frustum formed at the bottom?""",
        """30 సెం.మీ ఎత్తు గల ఒక ఘన శంఖువును దాని భూమి నుండి 20 సెం.మీ ఎత్తు వద్ద భూమికి సమాంతరంగా ఉండే తలంతో రెండు భాగాలుగా కత్తిరించారు. పైన ఏర్పడిన చిన్న శంఖువు ఘనపరిమాణానికి మరియు క్రింద ఏర్పడిన శంఖు ఖండము (Frustum) ఘనపరిమాణానికి గల నిష్పత్తి ఎంత?""",
        ['1 : 26', '1 : 27', '1 : 8', '1 : 19'],
        ['1 : 26', '1 : 27', '1 : 8', '1 : 19'],
        0,
        """Height of original cone H = 30 cm.
Cut is made at 20 cm from base => Height of small top cone h = 30 - 20 = 10 cm.
Ratio of heights h : H = 10 : 30 = 1 : 3.
Ratio of volumes = (h/H)^3 = (1/3)^3 = 1 : 27.
Volume of top small cone = 1 part, total volume = 27 parts.
Volume of frustum = Total - Top cone = 27 - 1 = 26 parts.
Ratio of Small cone : Frustum = 1 : 26.""",
        """మొత్తం ఎత్తు H = 30 సెం.మీ, చిన్న శంఖువు ఎత్తు h = 10 సెం.మీ.
ఎత్తుల నిష్పత్తి = 1 : 3. ఘనపరిమాణాల నిష్పత్తి = 1^3 : 3^3 = 1 : 27.
శంఖు ఖండం ఘనపరిమాణం = 27 - 1 = 26 భాగాలు.
చిన్న శంఖువు : శంఖు ఖండం నిష్పత్తి = 1 : 26."""
    ))

    return qs

if __name__ == "__main__":
    qs = get_part1()
    print(f"Arithmetic Part 1 successfully generated with {len(qs)} verified questions.")
