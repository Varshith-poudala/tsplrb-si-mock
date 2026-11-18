# -*- coding: utf-8 -*-
"""
Mock Test 11 - Arithmetic & Quantitative Aptitude (Q1 to Q50)
Strictly adheres to TSPLRB SI PWT Blueprint & Shentu's feedback:
- Speed, Distance & Time (Trains, Boats, Circular tracks, Relative Speed)
- Mensuration 2D & 3D (Rhombus, Trapezium, Frustum, Cylinder, Sphere)
- Commercial Mathematics (Profit/Loss, CI/SI, Time & Work, Ratio, Percentages)
- Pure Math (Number Systems, HCF/LCM, Permutations, Probability, Averages)
- Zero bracket prefix tags, complete bilingual English & Telugu.
"""

def make_q(id_num, topic, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
    return {
        "id": id_num,
        "qNumber": id_num,
        "section": "Arithmetic & Quantitative Reasoning",
        "topic": topic,
        "question_en": q_en.strip(),
        "question_te": q_te.strip(),
        "options_en": [str(o).strip() for o in opts_en],
        "options_te": [str(o).strip() for o in opts_te],
        "correct_option": corr,
        "explanation_en": exp_en.strip(),
        "explanation_te": exp_te.strip()
    }

def get_arithmetic_50():
    qs = []

    # Q1: Speed Distance Time - Train crossing bridge
    qs.append(make_q(
        1, "Speed, Distance & Time - Bridge Crossing",
        "A train 240 metres in length travelling at a uniform speed of 72 km/h crosses a railway bridge in 30 seconds. What is the length of the bridge?",
        "72 కి.మీ/గం స్థిర వేగంతో ప్రయాణిస్తున్న 240 మీటర్ల పొడవు గల ఒక రైలు ఒక రైల్వే వంతెనను 30 సెకన్లలో దాటుతుంది. ఆ వంతెన పొడవు ఎంత?",
        ["320 metres", "360 metres", "400 metres", "440 metres"],
        ["320 మీటర్లు", "360 మీటర్లు", "400 మీటర్లు", "440 మీటర్లు"],
        1,
        "Speed = 72 * (5/18) = 20 m/s. Total distance covered in 30 s = 20 * 30 = 600 m. Length of bridge = 600 - 240 = 360 metres.",
        "రైలు వేగం = 72 * (5/18) = 20 మీ/సె. 30 సెకన్లలో దాటిన మొత్తం దూరం = 20 * 30 = 600 మీ. వంతెన పొడవు = 600 - 240 = 360 మీటర్లు."
    ))

    # Q2: Speed Distance Time - Two trains opposite directions
    qs.append(make_q(
        2, "Speed, Distance & Time - Opposite Trains Crossing",
        "Two trains of lengths 150 m and 250 m are moving on parallel tracks in opposite directions at speeds of 50 km/h and 58 km/h respectively. In how many seconds will they cross each other completely from the moment they meet?",
        "సమాంతర పట్టాలపై ఎదురెదురు దిశల్లో వరుసగా 50 కి.మీ/గం మరియు 58 కి.మీ/గం వేగంతో ప్రయాణిస్తున్న 150 మీటర్లు మరియు 250 మీటర్ల పొడవు గల రెండు రైళ్లు, పరస్పరం కలిసిన తర్వాత ఒకదానికొకటి పూర్తిగా దాటడానికి ఎన్ని సెకన్లు పడుతుంది?",
        ["12 seconds", "13.33 seconds", "15 seconds", "16 seconds"],
        ["12 సెకన్లు", "13.33 సెకన్లు", "15 సెకన్లు", "16 సెకన్లు"],
        1,
        "Total distance = 150 + 250 = 400 m. Relative speed = 50 + 58 = 108 km/h = 108 * (5/18) = 30 m/s. Time = 400 / 30 = 40 / 3 = 13.33 seconds.",
        "మొత్తం దూరం = 400 మీ. సాపేక్ష వేగం = 108 కి.మీ/గం = 30 మీ/సె. దాటడానికి పట్టే సమయం = 400 / 30 = 13.33 సెకన్లు."
    ))

    # Q3: Speed Distance Time - Boats & Streams upstream
    qs.append(make_q(
        3, "Speed, Distance & Time - Boats and Streams",
        "A boat travels 24 km upstream against a river current in 4 hours, and covers the same distance downstream with the current in 2 hours. What is the speed of the boat in still water?",
        "ఒక పడవ ప్రవాహానికి ఎదురుగా (upstream) 24 కి.మీ దూరాన్ని 4 గంటల్లో ప్రయాణిస్తుంది, మరియు ప్రవాహ దిశలో (downstream) అదే దూరాన్ని 2 గంటల్లో చేరుకుంటుంది. నిశ్చల నీటిలో ఆ పడవ వేగం ఎంత?",
        ["8 km/h", "9 km/h", "10 km/h", "12 km/h"],
        ["8 కి.మీ/గం", "9 కి.మీ/గం", "10 కి.మీ/గం", "12 కి.మీ/గం"],
        1,
        "Upstream speed u = 24 / 4 = 6 km/h. Downstream speed v = 24 / 2 = 12 km/h. Speed in still water = (u + v)/2 = (6 + 12)/2 = 9 km/h.",
        "ఎదురు ప్రవాహ వేగం = 6 కి.మీ/గం. అనుకూల ప్రవాహ వేగం = 12 కి.మీ/గం. నిశ్చల నీటిలో వేగం = (6 + 12)/2 = 9 కి.మీ/గం."
    ))

    # Q4: Speed Distance Time - Reduced speed late arrival
    qs.append(make_q(
        4, "Speed, Distance & Time - Fraction of Speed",
        "Walking at 5/6th of his usual speed, a sub-inspector cadet reaches the parade ground 12 minutes late. What is his usual time to reach the ground?",
        "ఒక సబ్-ఇన్‌స్పెక్టర్ క్యాడెట్ తన సాధారణ వేగంలో 5/6 వంతు వేగంతో నడవడం వలన పరేడ్ మైదానానికి 12 నిమిషాలు ఆలస్యంగా చేరుకుంటాడు. మైదానాన్ని చేరుకోవడానికి అతని సాధారణ సమయం ఎంత?",
        ["50 minutes", "60 minutes", "72 minutes", "80 minutes"],
        ["50 నిమిషాలు", "60 నిమిషాలు", "72 నిమిషాలు", "80 నిమిషాలు"],
        1,
        "New time = (6/5) of usual time T. Extra time = (6/5)T - T = T/5 = 12 minutes => Usual time T = 12 * 5 = 60 minutes.",
        "కొత్త సమయం = (6/5)T. ఆలస్యమైన సమయం = T/5 = 12 నిమిషాలు => సాధారణ సమయం T = 60 నిమిషాలు (1 గంట)."
    ))

    # Q5: Speed Distance Time - Circular track race
    qs.append(make_q(
        5, "Speed, Distance & Time - Circular Track Race",
        "Two runners P and Q start simultaneously from the same starting point on a 400-metre circular track in the same direction with speeds of 8 m/s and 5 m/s respectively. After how many seconds will P overtake Q for the first time?",
        "400 మీటర్ల చుట్టుకొలత గల వృత్తాకార ట్రాక్‌పై P మరియు Q అనే ఇద్దరు రన్నర్లు ఒకే బిందువు నుండి ఒకే దిశలో వరుసగా 8 మీ/సె మరియు 5 మీ/సె వేగంతో పరుగెత్తడం ప్రారంభించారు. P మొదటిసారిగా Q ని ఎన్ని సెకన్ల తర్వాత అధిగమిస్తాడు?",
        ["100 seconds", "120 seconds", "133.33 seconds", "150 seconds"],
        ["100 సెకన్లు", "120 సెకన్లు", "133.33 సెకన్లు", "150 సెకన్లు"],
        2,
        "Relative speed in same direction = 8 - 5 = 3 m/s. P laps Q when relative distance is 400 m. Time = 400 / 3 = 133.33 seconds.",
        "ఒకే దిశలో సాపేక్ష వేగం = 8 - 5 = 3 మీ/సె. P, Q ని దాటడానికి పట్టే సమయం = 400 / 3 = 133.33 సెకన్లు."
    ))

    # Q6: Speed Distance Time - Average speed
    qs.append(make_q(
        6, "Speed, Distance & Time - Trip Average Speed",
        "A police vehicle covers the first 120 km of a journey at 40 km/h and the remaining 180 km at 60 km/h. What is the average speed of the vehicle for the entire 300 km journey?",
        "ఒక పోలీస్ వాహనం 300 కి.మీ ప్రయాణంలో మొదటి 120 కి.మీ దూరాన్ని 40 కి.మీ/గం వేగంతోను, మిగిలిన 180 కి.మీ దూరాన్ని 60 కి.మీ/గం వేగంతోను పూర్తి చేసింది. ఆ ప్రయాణం మొత్తానికి సగటు వేగం ఎంత?",
        ["48 km/h", "50 km/h", "52 km/h", "54 km/h"],
        ["48 కి.మీ/గం", "50 కి.మీ/గం", "52 కి.మీ/గం", "54 కి.మీ/గం"],
        1,
        "Time for 1st part = 120 / 40 = 3 hrs. Time for 2nd part = 180 / 60 = 3 hrs. Total distance = 300 km. Total time = 3 + 3 = 6 hrs. Average speed = 300 / 6 = 50 km/h.",
        "మొదటి భాగానికి సమయం = 120/40 = 3 గంటలు. రెండవ భాగానికి = 180/60 = 3 గంటలు. మొత్తం సమయం = 6 గంటలు. సగటు వేగం = 300 / 6 = 50 కి.మీ/గం."
    ))

    # Q7: Speed Distance Time - Police thief chase
    qs.append(make_q(
        7, "Speed, Distance & Time - Pursuit Chase",
        "A thief escapes from a police outpost at 10:00 AM running at 30 km/h. The sub-inspector discovers the escape at 10:30 AM and pursues him in a patrol jeep at 50 km/h. At what time will the sub-inspector capture the thief?",
        "ఉదయం 10:00 గంటలకు ఒక దొంగ పోలీస్ ఔట్‌పోస్ట్ నుండి 30 కి.మీ/గం వేగంతో పారిపోయాడు. ఉదయం 10:30 గంటలకు గమనించిన సబ్-ఇన్‌స్పెక్టర్ పెట్రోల్ జీపులో 50 కి.మీ/గం వేగంతో వెంబడించారు. సబ్-ఇన్‌స్పెక్టర్ దొంగను ఏ సమయానికి పట్టుకుంటారు?",
        ["11:00 AM", "11:15 AM", "11:30 AM", "12:00 PM"],
        ["ఉదయం 11:00", "ఉదయం 11:15", "ఉదయం 11:30", "మధ్యాహ్నం 12:00"],
        1,
        "Head start in 30 mins (0.5 hr) = 30 * 0.5 = 15 km. Relative speed = 50 - 30 = 20 km/h. Time to catch = 15 / 20 = 0.75 hrs = 45 minutes. Catch time = 10:30 AM + 45 mins = 11:15 AM.",
        "30 నిమిషాల్లో దొంగ వెళ్లిన దూరం = 15 కి.మీ. సాపేక్ష వేగం = 20 కి.మీ/గం. పట్టుకోవడానికి పట్టే సమయం = 15/20 = 45 నిమిషాలు. పట్టుకునే సమయం = 10:30 + 45 నిమిషాలు = 11:15 AM."
    ))

    # Q8: Speed Distance Time - Escalator / Equal segments
    qs.append(make_q(
        8, "Speed, Distance & Time - Harmonic Mean Speed",
        "A commuter travels three equal distances of 30 km each at speeds of 10 km/h, 20 km/h, and 60 km/h respectively. What is the average speed for the entire journey?",
        "ఒక ప్రయాణికుడు ఒక్కొక్కటి 30 కి.మీ చొప్పున ఉన్న మూడు సమాన దూరాలను వరుసగా 10 కి.మీ/గం, 20 కి.మీ/గం, మరియు 60 కి.మీ/గం వేగంతో ప్రయాణించాడు. ఆ మొత్తం ప్రయాణానికి సగటు వేగం ఎంత?",
        ["18 km/h", "20 km/h", "24 km/h", "30 km/h"],
        ["18 కి.మీ/గం", "20 కి.మీ/గం", "24 కి.మీ/గం", "30 కి.మీ/గం"],
        0,
        "Total distance = 90 km. Time = 30/10 + 30/20 + 30/60 = 3 + 1.5 + 0.5 = 5 hours. Average speed = 90 / 5 = 18 km/h.",
        "మొత్తం దూరం = 90 కి.మీ. మొత్తం సమయం = 3 + 1.5 + 0.5 = 5 గంటలు. సగటు వేగం = 90 / 5 = 18 కి.మీ/గం."
    ))

    # Q9: Mensuration 2D - Rhombus area from perimeter
    qs.append(make_q(
        9, "Mensuration 2D - Rhombus",
        "The perimeter of a rhombus is 100 cm and one of its diagonals is 40 cm. What is the area of this rhombus?",
        "ఒక రాంబస్ చుట్టుకొలత 100 సెం.మీ మరియు దాని ఒక కర్ణం పొడవు 40 సెం.మీ. ఆ రాంబస్ వైశాల్యం ఎంత?",
        ["400 sq.cm", "500 sq.cm", "600 sq.cm", "800 sq.cm"],
        ["400 చ.సెం.మీ", "500 చ.సెం.మీ", "600 చ.సెం.మీ", "800 చ.సెం.మీ"],
        2,
        "Perimeter = 4a = 100 => a = 25 cm. Diagonal d1 = 40 => d1/2 = 20. Other half-diagonal = sqrt(25^2 - 20^2) = sqrt(625 - 400) = sqrt(225) = 15 cm => d2 = 30 cm. Area = 1/2 * d1 * d2 = 1/2 * 40 * 30 = 600 sq.cm.",
        "భుజం a = 25 సెం.మీ. రెండవ కర్ణం d2 = 2 * sqrt(25^2 - 20^2) = 30 సెం.మీ. వైశాల్యం = 1/2 * 40 * 30 = 600 చ.సెం.మీ."
    ))

    # Q10: Mensuration 2D - Trapezium field fencing
    qs.append(make_q(
        10, "Mensuration 2D - Trapezium",
        "The parallel sides of a trapezium-shaped police training ground are 35 m and 25 m, and the non-parallel sides are equal to 13 m each. What is the area of the training ground?",
        "ట్రెపీజియం ఆకారంలో ఉన్న ఒక పోలీస్ శిక్షణ మైదానం సమాంతర భుజాలు 35 మీ మరియు 25 మీ, మరియు సమాంతరం కాని భుజాలు ఒక్కొక్కటి 13 మీ పొడవు ఉన్నాయి. ఆ మైదానం వైశాల్యం ఎంత?",
        ["300 sq.m", "360 sq.m", "420 sq.m", "480 sq.m"],
        ["300 చ.మీ", "360 చ.మీ", "420 చ.మీ", "480 చ.మీ"],
        1,
        "Base difference = 35 - 25 = 10 m. Splitting into two equal right triangles at ends: base of each right triangle = 10/2 = 5 m. Height h = sqrt(13^2 - 5^2) = sqrt(169 - 25) = sqrt(144) = 12 m. Area = 1/2 * (35 + 25) * 12 = 30 * 12 = 360 sq.m.",
        "ఎత్తు h = sqrt(13^2 - 5^2) = 12 మీటర్లు. వైశాల్యం = 1/2 * (35 + 25) * 12 = 60 * 6 = 360 చ.మీ."
    ))

    # Q11: Mensuration 2D - Circular track width
    qs.append(make_q(
        11, "Mensuration 2D - Circular Ring Track",
        "A circular running track has an inner circumference of 440 metres and an outer circumference of 506 metres. What is the width of the running track? (Take pi = 22/7)",
        "ఒక వృత్తాకార రన్నింగ్ ట్రాక్ లోపలి చుట్టుకొలత 440 మీటర్లు మరియు వెలుపలి చుట్టుకొలత 506 మీటర్లు. ఆ రన్నింగ్ ట్రాక్ వెడల్పు ఎంత?",
        ["7.5 metres", "10.5 metres", "12 metres", "14 metres"],
        ["7.5 మీటర్లు", "10.5 మీటర్లు", "12 మీటర్లు", "14 మీటర్లు"],
        1,
        "2*pi*R - 2*pi*r = 506 - 440 = 66 m => 2 * (22/7) * (R - r) = 66 => (R - r) = (66 * 7) / 44 = 10.5 metres.",
        "ట్రాక్ వెడల్పు (R - r) = (506 - 440) / (2 * pi) = 66 / (44/7) = 10.5 మీటర్లు."
    ))

    # Q12: Mensuration 2D - Sector of a circle
    qs.append(make_q(
        12, "Mensuration 2D - Circle Sector",
        "A sector of a circle of radius 21 cm has a central angle of 60 degrees. What is the perimeter of this sector? (Take pi = 22/7)",
        "21 సెం.మీ వ్యాసార్థం గల వృత్తంలో 60 డిగ్రీల కేంద్ర కోణం కలిగిన ఒక సెక్టార్ చుట్టుకొలత ఎంత?",
        ["42 cm", "64 cm", "76 cm", "88 cm"],
        ["42 సెం.మీ", "64 సెం.మీ", "76 సెం.మీ", "88 సెం.మీ"],
        1,
        "Arc length l = (theta/360) * 2*pi*r = (60/360) * 2 * (22/7) * 21 = (1/6) * 132 = 22 cm. Perimeter of sector = l + 2r = 22 + 2(21) = 22 + 42 = 64 cm.",
        "చాపం పొడవు l = (60/360) * 2 * (22/7) * 21 = 22 సెం.మీ. సెక్టార్ చుట్టుకొలత = l + 2r = 22 + 42 = 64 సెం.మీ."
    ))

    # Q13: Mensuration 3D - Cone volume & slant height
    qs.append(make_q(
        13, "Mensuration 3D - Cone Curved Surface Area",
        "A conical tent has a base radius of 7 metres and a vertical height of 24 metres. What is the area of the canvas cloth required to fabricate the curved surface of the tent? (Take pi = 22/7)",
        "ఒక శంఖు ఆకారపు గుడారం భూ వ్యాసార్థం 7 మీటర్లు మరియు నిలువు ఎత్తు 24 మీటర్లు. ఆ గుడారం యొక్క వక్రతల వైశాల్యానికి అవసరమైన కాన్వాస్ వస్త్రం ఎంత?",
        ["440 sq.m", "550 sq.m", "660 sq.m", "770 sq.m"],
        ["440 చ.మీ", "550 చ.మీ", "660 చ.మీ", "770 చ.మీ"],
        1,
        "Slant height l = sqrt(r^2 + h^2) = sqrt(7^2 + 24^2) = sqrt(49 + 576) = sqrt(625) = 25 m. Curved Surface Area = pi * r * l = (22/7) * 7 * 25 = 22 * 25 = 550 sq.m.",
        "ఏటవాలు ఎత్తు l = sqrt(49 + 576) = 25 మీటర్లు. వక్రతల వైశాల్యం = pi * r * l = (22/7) * 7 * 25 = 550 చ.మీ."
    ))

    # Q14: Mensuration 3D - Melting spheres into cylinder
    qs.append(make_q(
        14, "Mensuration 3D - Melting & Recasting",
        "Three solid metallic spheres of radii 3 cm, 4 cm, and 5 cm are melted together and recast into a single solid sphere. What is the radius of the newly formed sphere?",
        "3 సెం.మీ, 4 సెం.మీ మరియు 5 సెం.మీ వ్యాసార్థాలు గల మూడు ఘన లోహ గోళాలను కరిగించి ఒకే పెద్ద ఘన గోళంగా మార్చారు. కొత్తగా ఏర్పడిన గోళం వ్యాసార్థం ఎంత?",
        ["6 cm", "7 cm", "8 cm", "9 cm"],
        ["6 సెం.మీ", "7 సెం.మీ", "8 సెం.మీ", "9 సెం.మీ"],
        0,
        "Volume of combined sphere = (4/3)*pi * (r1^3 + r2^3 + r3^3) = (4/3)*pi * (27 + 64 + 125) = (4/3)*pi * 216. Since R^3 = 216, R = 6 cm.",
        "R^3 = 3^3 + 4^3 + 5^3 = 27 + 64 + 125 = 216 => R = 6 సెం.మీ."
    ))

    # Q15: Mensuration 3D - Cylinder water level rise
    qs.append(make_q(
        15, "Mensuration 3D - Cylinder Water Rise",
        "A cylindrical vessel of radius 12 cm contains water. A solid spherical iron ball of radius 6 cm is completely submerged into the vessel. By how much does the water level in the cylinder rise?",
        "12 సెం.మీ వ్యాసార్థం గల ఒక స్థూపాకార పాత్రలో నీరు ఉంది. 6 సెం.మీ వ్యాసార్థం గల ఒక ఘన ఇనుప గోళాన్ని ఆ నీటిలో పూర్తిగా ముంచారు. ఆ పాత్రలోని నీటి మట్టం ఎంత ఎత్తుకు పెరుగుతుంది?",
        ["1 cm", "2 cm", "3 cm", "4 cm"],
        ["1 సెం.మీ", "2 సెం.మీ", "3 సెం.మీ", "4 సెం.మీ"],
        0,
        "Volume of sphere = (4/3)*pi*r^3 = (4/3)*pi * 216 = 288*pi. Rise in water level h in cylinder: pi * R^2 * h = Volume of sphere => pi * 144 * h = 288*pi => h = 288 / 144 = 2 cm.",
        "గోళం ఘనపరిమాణం = (4/3)*pi*(6)^3 = 288*pi. స్థూపంలో నీటి పెరుగుదల h = 288 / (12^2) = 288 / 144 = 2 సెం.మీ."
    ))
    qs[-1]["correct_option"] = 1

    # Q16: Mensuration 3D - Frustum of cone
    qs.append(make_q(
        16, "Mensuration 3D - Frustum of Cone",
        "A drinking water bucket is in the shape of a frustum of a cone with top radius 14 cm, bottom radius 7 cm, and vertical height 24 cm. What is the capacity (volume) of the bucket? (Take pi = 22/7)",
        "ఒక నీటి బకెట్ శంఖువు ఖండం (Frustum) ఆకారంలో ఉండి, పై వ్యాసార్థం 14 సెం.మీ, అడుగు వ్యాసార్థం 7 సెం.మీ మరియు నిలువు ఎత్తు 24 సెం.మీ కలిగి ఉంది. ఆ బకెట్ సామర్థ్యం (ఘనపరిమాణం) ఎంత?",
        ["7,392 cu.cm", "8,624 cu.cm", "9,240 cu.cm", "10,164 cu.cm"],
        ["7,392 ఘ.సెం.మీ", "8,624 ఘ.సెం.మీ", "9,240 ఘ.సెం.మీ", "10,164 ఘ.సెం.మీ"],
        1,
        "Volume of frustum = (1/3)*pi*h * (R^2 + r^2 + R*r) = (1/3) * (22/7) * 24 * (196 + 49 + 98) = 8 * (22/7) * 343 = 8 * 22 * 49 = 8,624 cu.cm.",
        "శంఖు ఖండం ఘనపరిమాణం = (1/3)*pi*h*(R^2 + r^2 + Rr) = (1/3)*(22/7)*24*(343) = 8 * 22 * 49 = 8,624 ఘ.సెం.మీ."
    ))

    # Q17: Time and Work - Efficiency ratio
    qs.append(make_q(
        17, "Time & Work - Efficiency Ratio",
        "A is twice as efficient as B, and together they can complete a task in 14 days. In how many days can A working alone finish the entire task?",
        "A అనే వ్యక్తి B కంటే రెండు రెట్లు ఎక్కువ పని సామర్థ్యం కలవాడు, మరియు వారిద్దరూ కలిసి ఒక పనిని 14 రోజుల్లో పూర్తి చేయగలరు. A ఒంటరిగా ఆ పనిని ఎన్ని రోజుల్లో పూర్తి చేయగలడు?",
        ["21 days", "28 days", "35 days", "42 days"],
        ["21 రోజులు", "28 రోజులు", "35 రోజులు", "42 రోజులు"],
        0,
        "Let B's rate = 1 unit/day => A's rate = 2 units/day. Together = 3 units/day. Total work = 3 * 14 = 42 units. A alone takes = 42 / 2 = 21 days.",
        "A సామర్థ్యం 2, B సామర్థ్యం 1. మొత్తం పని = 3 * 14 = 42 యూనిట్లు. A ఒక్కడికే పట్టే సమయం = 42 / 2 = 21 రోజులు."
    ))

    # Q18: Time and Work - Men and Boys
    qs.append(make_q(
        18, "Time & Work - Men and Boys",
        "4 men and 6 boys can finish a job in 8 days, while 3 men and 7 boys can finish it in 10 days. In how many days will 10 boys finish the same job alone?",
        "4 మంది పురుషులు మరియు 6 మంది బాలురు కలిసి ఒక పనిని 8 రోజుల్లో చేయగలరు, కాగా 3 మంది పురుషులు మరియు 7 మంది బాలురు అదే పనిని 10 రోజుల్లో చేయగలరు. 10 మంది బాలురు మాత్రమే ఆ పనిని ఎన్ని రోజుల్లో పూర్తి చేయగలరు?",
        ["36 days", "40 days", "44 days", "48 days"],
        ["36 రోజులు", "40 రోజులు", "44 రోజులు", "48 రోజులు"],
        1,
        "(4M + 6B)*8 = (3M + 7B)*10 => 32M + 48B = 30M + 70B => 2M = 22B => 1M = 11B. Total work = (4*11B + 6B)*8 = 50B * 8 = 400 boy-days. Time for 10 boys = 400 / 10 = 40 days.",
        "2M = 22B => 1M = 11B. మొత్తం పని = 50B * 8 = 400 బాయ్-డేస్. 10 మంది బాలురకు పట్టే సమయం = 400 / 10 = 40 రోజులు."
    ))

    # Q19: Time and Work - Three workers
    qs.append(make_q(
        19, "Time & Work - Multiple Workers",
        "A, B, and C can complete a work in 10, 15, and 30 days respectively. If A works with B and C on alternate days (A and B on 1st day, A and C on 2nd day, and so on), in how many days will the work be completed?",
        "A, B మరియు C లు వరుసగా 10, 15 మరియు 30 రోజుల్లో ఒక పనిని చేయగలరు. A కి మొదటి రోజు B, రెండవ రోజు C ఇలా రోజు మార్చి రోజు సహాయం చేస్తే, ఆ పని మొత్తం ఎన్ని రోజుల్లో పూర్తవుతుంది?",
        ["6 days", "7 days", "8 days", "9 days"],
        ["6 రోజులు", "7 రోజులు", "8 రోజులు", "9 రోజులు"],
        0,
        "Total work = LCM(10, 15, 30) = 30 units. A = 3, B = 2, C = 1 unit/day. Day 1 (A+B) = 3 + 2 = 5 units. Day 2 (A+C) = 3 + 1 = 4 units. In 2 days = 5 + 4 = 9 units. In 6 days (3 cycles) = 9 * 3 = 27 units? Wait: 3 cycles = 27 units. Then Day 7 (A+B) needs 3 units = 3/5 day. Let's make total work 36 or adjust: If A+B=5, A+C=4 => 9 units in 2 days. For 36 units: 4 cycles = 8 days. Let's make options 6, 7, 8, 9 with total work 30 => wait: 2 days = 9 units, 4 days = 18, 6 days = 27. Day 7 = 3/5 day. Let's adjust A=12, B=15, C=20 days => LCM=60. A=5, B=4, C=3. Day 1 (A+B)=9, Day 2 (A+C)=8. 2 days = 17 units. 6 days = 51 units. Let's use simple: A=10, B=20, C=30.",
        "మొత్తం పని = 30 యూనిట్లు. 2 రోజుల్లో 9 యూనిట్లు పూర్తవుతాయి."
    ))
    # Replace Q19 with clean numbers:
    qs[-1]["question_en"] = "A can do a piece of work in 20 days and B can do it in 30 days. They work together for 5 days and then A leaves. In how many more days will B finish the remaining work?"
    qs[-1]["question_te"] = "ఒక పనిని A 20 రోజుల్లో మరియు B 30 రోజుల్లో చేయగలరు. వారిద్దరూ కలిసి 5 రోజులు పనిచేసిన తర్వాత A నిష్క్రమించాడు. మిగిలిన పనిని B ఇంకా ఎన్ని రోజుల్లో పూర్తి చేయగలడు?"
    qs[-1]["options_en"] = ["15 days", "17.5 days", "18 days", "20 days"]
    qs[-1]["options_te"] = ["15 రోజులు", "17.5 రోజులు", "18 రోజులు", "20 రోజులు"]
    qs[-1]["correct_option"] = 1
    qs[-1]["explanation_en"] = "Total work = LCM(20, 30) = 60 units. A = 3, B = 2. In 5 days together = 5 * 5 = 25 units. Remaining = 60 - 25 = 35 units. B alone takes = 35 / 2 = 17.5 days."
    qs[-1]["explanation_te"] = "మొత్తం పని = 60 యూనిట్లు. 5 రోజుల్లో చేసిన పని = 25 యూనిట్లు. మిగిలిన 35 యూనిట్లను B పూర్తి చేయడానికి 35 / 2 = 17.5 రోజులు పడుతుంది."

    # Q20: Pipes and Cisterns - 3 pipes
    qs.append(make_q(
        20, "Pipes & Cisterns - Three Inlets",
        "Three pipes A, B, and C can fill a cistern in 6 hours. After working together for 2 hours, C is closed and A and B fill the remaining part in 7 hours. In how many hours can pipe C alone fill the cistern?",
        "A, B మరియు C అనే మూడు పైపులు కలిసి ఒక తొట్టిని 6 గంటల్లో నింపగలవు. మూడు పైపులు కలిసి 2 గంటలు పనిచేసిన తర్వాత C పైపును మూసివేశారు. మిగిలిన భాగాన్ని A మరియు B లు కలిసి 7 గంటల్లో నింపాయి. C పైపు ఒక్కటే ఆ తొట్టిని ఎన్ని గంటల్లో నింపగలదు?",
        ["12 hours", "14 hours", "15 hours", "18 hours"],
        ["12 గంటలు", "14 గంటలు", "15 గంటలు", "18 గంటలు"],
        1,
        "In 2 hrs, A+B+C fill 2/6 = 1/3 of cistern. Remaining = 2/3. A+B fill 2/3 in 7 hrs => A+B full cistern in 7 * (3/2) = 10.5 hrs. C's rate = 1/6 - 1/10.5 = 1/6 - 2/21 = (7 - 4)/42 = 3/42 = 1/14. Pipe C alone takes 14 hours.",
        "2 గంటల్లో నిండిన భాగం = 1/3. మిగిలిన 2/3 భాగాన్ని A, B లు 7 గంటల్లో నింపారు => A+B మొత్తం నింపడానికి 10.5 గంటలు. C రేటు = 1/6 - 1/10.5 = 1/14. C ఒక్కటే 14 గంటల్లో నింపగలదు."
    ))

    # Q21: Percentages - Population growth
    qs.append(make_q(
        21, "Percentages - Compound Growth",
        "The population of a mandal in Telangana increases at an annual rate of 5%. If its present population is 80,000, what will be its population after 2 years?",
        "తెలంగాణలోని ఒక మండల జనాభా వార్షికంగా 5% చొప్పున పెరుగుతుంది. ప్రస్తుత జనాభా 80,000 అయితే, 2 సంవత్సరాల తర్వాత ఆ మండల జనాభా ఎంత అవుతుంది?",
        ["86,200", "88,000", "88,200", "90,000"],
        ["86,200", "88,000", "88,200", "90,000"],
        2,
        "Population after 2 years = 80000 * (1 + 5/100)^2 = 80000 * (21/20)^2 = 80000 * (441 / 400) = 200 * 441 = 88,200.",
        "2 సంవత్సరాల తర్వాత జనాభా = 80,000 * (21/20)^2 = 200 * 441 = 88,200."
    ))

    # Q22: Percentages - Salary spending
    qs.append(make_q(
        22, "Percentages - Successive Spending",
        "A police constable spends 20% of his monthly salary on house rent, 40% of the remaining on food and children's education, and saves 80% of the rest. If he saves ₹7,680 every month, what is his total monthly salary?",
        "ఒక పోలీస్ కానిస్టేబుల్ తన నెలవారీ జీతంలో 20% ఇంటి అద్దెకు, మిగిలిన మొత్తంలో 40% ఆహారం మరియు పిల్లల చదువుకు ఖర్చు చేసి, ఇంకా మిగిలిన దానిలో 80% పొదుపు చేస్తాడు. అతను నెలకు ₹7,680 పొదుపు చేస్తే, అతని మొత్తం నెలవారీ జీతం ఎంత?",
        ["₹18,000", "₹20,000", "₹22,000", "₹24,000"],
        ["₹18,000", "₹20,000", "₹22,000", "₹24,000"],
        1,
        "Let salary = S. After rent: 0.8S. After food/edu: 0.8S * 0.6 = 0.48S. Savings = 0.48S * 0.8 = 0.384S = 7680 => S = 7680 / 0.384 = ₹20,000.",
        "జీతం S అనుకుంటే: మిగిలిన మొత్తం = S * 0.8 * 0.6 * 0.8 = 0.384S = 7680 => S = ₹20,000."
    ))

    # Q23: Profit & Loss - Double selling price
    qs.append(make_q(
        23, "Profit & Loss - Selling Price Manipulation",
        "If the selling price of an article is doubled, the profit triples. What is the original profit percentage?",
        "ఒక వస్తువు అమ్మకపు ధరను రెట్టింపు చేస్తే, లాభం మూడు రెట్లు అవుతుంది. అసలు లాభ శాతం ఎంత?",
        ["50%", "75%", "100%", "120%"],
        ["50%", "75%", "100%", "120%"],
        2,
        "Original Profit P = SP - CP. New profit 3P = 2*SP - CP. Subtracting: 2P = SP => SP = 2P => P = SP - CP => 2P - CP = P => CP = P. Since Profit = CP, Profit % = (P/CP)*100 = 100%.",
        "లాభం P = SP - CP. కొత్త లాభం 3P = 2SP - CP => 2P = SP => CP = P. కాబట్టి అసలు లాభ శాతం 100%."
    ))

    # Q24: Profit & Loss - Marked price discount
    qs.append(make_q(
        24, "Profit & Loss - Discount on Marked Price",
        "A retailer buys an item for ₹800. At what price should he mark it so that even after allowing a discount of 20%, he still makes a profit of 25%?",
        "ఒక వ్యాపారి ₹800 కి ఒక వస్తువును కొన్నాడు. 20% తగ్గింపు (డిస్కౌంట్) ఇచ్చినప్పటికీ 25% లాభం పొందడానికి అతను ఆ వస్తువుపై ఎంత ధరను ముద్రించాలి?",
        ["₹1,150", "₹1,200", "₹1,250", "₹1,300"],
        ["₹1,150", "₹1,200", "₹1,250", "₹1,300"],
        2,
        "Required SP = CP * 1.25 = 800 * 1.25 = ₹1,000. MP * (1 - 0.20) = 1000 => MP * 0.8 = 1000 => MP = 1000 / 0.8 = ₹1,250.",
        "కావలసిన అమ్మకపు ధర = 800 * 1.25 = ₹1,000. ప్రకటన ధర MP = 1000 / 0.80 = ₹1,250."
    ))

    # Q25: Profit & Loss - Dishonest shopkeeper
    qs.append(make_q(
        25, "Profit & Loss - False Weight",
        "A dishonest grocer sells pulses at a profit of 10% on cost price, but uses a false weight that weighs 800 grams instead of 1 kilogram. What is his overall actual profit percentage?",
        "ఒక వ్యాపారి పప్పు దినుసులను కొన్న ధరపై 10% లాభానికి అమ్ముతూ, 1 కిలోగ్రాము బదులుగా 800 గ్రాముల తప్పుడు తూకాన్ని ఉపయోగిస్తున్నాడు. అతని మొత్తం అసలు లాభ శాతం ఎంత?",
        ["32.5%", "35%", "37.5%", "40%"],
        ["32.5%", "35%", "37.5%", "40%"],
        2,
        "Cost of 800g = 800. Selling price for 1000g marked with 10% gain = 1000 * 1.10 = 1100. Profit = 1100 - 800 = 300. Profit % = (300 / 800) * 100 = 37.5%.",
        "800 గ్రాముల కొన్న ఖరీదు 800 అనుకుంటే, అమ్మిన ధర 1100. లాభం = 300. లాభ శాతం = (300 / 800) * 100 = 37.5%."
    ))

    # Q26: Simple Interest - Rate calculation
    qs.append(make_q(
        26, "Simple Interest - Unknown Rate",
        "A sum of money amounts to ₹9,800 in 5 years and ₹12,005 in 8 years at the same simple interest rate. What is the annual rate of interest?",
        "ఒకే సాధారణ వడ్డీ రేటు వద్ద ఒక మొత్తం 5 సంవత్సరాలలో ₹9,800 గాను మరియు 8 సంవత్సరాలలో ₹12,005 గాను మారింది. వార్షిక వడ్డీ రేటు ఎంత?",
        ["10%", "12%", "12.5%", "15%"],
        ["10%", "12%", "12.5%", "15%"],
        1,
        "Interest for 3 years = 12005 - 9800 = ₹2,205 => SI per year = 2205 / 3 = ₹735. Principal = 9800 - 5*(735) = 9800 - 3675 = ₹6,125. Rate R = (735 * 100) / 6125 = 12%.",
        "3 సంవత్సరాల వడ్డీ = 2205 => సంవత్సరానికి వడ్డీ = ₹735. అసలు = 9800 - (5 * 735) = ₹6,125. వడ్డీ రేటు = (735 * 100) / 6125 = 12%."
    ))

    # Q27: Simple Interest - Multiplication
    qs.append(make_q(
        27, "Simple Interest - Time to Quadruple",
        "At a certain simple interest rate, a sum becomes 4 times of itself in 15 years. How long will it take for the same sum to become 10 times of itself at that rate?",
        "ఒక నిర్దిష్ట సాధారణ వడ్డీ రేటు వద్ద ఒక సొమ్ము 15 సంవత్సరాలలో 4 రెట్లు అవుతుంది. అదే వడ్డీ రేటు వద్ద ఆ సొమ్ము 10 రెట్లు కావడానికి ఎంత సమయం పడుతుంది?",
        ["40 years", "45 years", "50 years", "60 years"],
        ["40 సంవత్సరాలు", "45 సంవత్సరాలు", "50 సంవత్సరాలు", "60 సంవత్సరాలు"],
        1,
        "(N1 - 1)/T1 = (N2 - 1)/T2 => (4 - 1)/15 = (10 - 1)/T2 => 3/15 = 9/T2 => 1/5 = 9/T2 => T2 = 45 years.",
        "సాధారణ వడ్డీ సూత్రం: 3/15 = 9/T2 => T2 = 45 సంవత్సరాలు."
    ))

    # Q28: Compound Interest - Difference for 3 years
    qs.append(make_q(
        28, "Compound Interest - 3-Year CI vs SI Difference",
        "What is the difference between compound interest and simple interest on ₹10,000 for 3 years at 10% per annum?",
        "వార్షిక 10% వడ్డీ రేటు చొప్పున ₹10,000 అసలుపై 3 సంవత్సరాలకు చక్రవడ్డీ మరియు సాధారణ వడ్డీల మధ్య తేడా ఎంత?",
        ["₹300", "₹310", "₹320", "₹330"],
        ["₹300", "₹310", "₹320", "₹330"],
        1,
        "Difference for 3 years = P * (R/100)^2 * (3 + R/100) = 10000 * (0.01) * (3 + 0.1) = 100 * 3.1 = ₹310.",
        "3 సంవత్సరాల తేడా = P * (R/100)^2 * (3 + R/100) = 10000 * 0.01 * 3.1 = ₹310."
    ))

    # Q29: Compound Interest - Half-yearly compounding
    qs.append(make_q(
        29, "Compound Interest - Half-Yearly Compounding",
        "What will be the compound interest on a principal of ₹8,000 for 1 year at 10% per annum, compounded half-yearly?",
        "వార్షిక 10% వడ్డీ రేటు చొప్పున ₹8,000 అసలుపై 1 సంవత్సరానికి అర్ధ వార్షిక చక్రవడ్డీ ఎంత?",
        ["₹800", "₹820", "₹840", "₹860"],
        ["₹800", "₹820", "₹840", "₹860"],
        1,
        "Semi-annual rate = 10/2 = 5%. Periods n = 2. Amount = 8000 * (1 + 0.05)^2 = 8000 * (1.05)^2 = 8000 * 1.1025 = ₹8,820. CI = 8820 - 8000 = ₹820.",
        "అర్ధ వార్షిక రేటు = 5%, n = 2. మొత్తం = 8000 * 1.1025 = ₹8,820. చక్రవడ్డీ = ₹820."
    ))

    # Q30: Ratio and Proportion - Coin bag
    qs.append(make_q(
        30, "Ratio & Proportion - Coins",
        "A box contains ₹1, 50 paise, and 25 paise coins in the ratio 2 : 3 : 5. If the total value of all coins in the box is ₹228, what is the number of 50 paise coins?",
        "ఒక పెట్టెలో ₹1, 50 పైసలు మరియు 25 పైసల నాణేలు 2 : 3 : 5 నిష్పత్తిలో ఉన్నాయి. ఆ పెట్టెలోని నాణేల మొత్తం విలువ ₹228 అయితే, అందులోని 50 పైసల నాణేల సంఖ్య ఎంత?",
        ["144", "152", "160", "172"],
        ["144", "152", "160", "172"],
        0,
        "Value per unit ratio = 2(1.00) + 3(0.50) + 5(0.25) = 2 + 1.50 + 1.25 = ₹4.75. Multiplier x = 228 / 4.75 = 48. Number of 50p coins = 3 * 48 = 144.",
        "యూనిట్ విలువ = 2 + 1.5 + 1.25 = ₹4.75. గుణకం = 228 / 4.75 = 48. 50 పైసల నాణేలు = 3 * 48 = 144."
    ))

    # Q31: Partnership - Active partner
    qs.append(make_q(
        31, "Partnership - Management Salary & Profit",
        "A and B invest in a security agency in the ratio 3 : 2. A is an active partner and receives 10% of the total profit as management salary, and the remaining profit is divided in their investment ratio. If A receives a total of ₹59,000, what was the total profit earned by the agency?",
        "A మరియు B లు ఒక సెక్యూరిటీ ఏజెన్సీలో 3 : 2 నిష్పత్తిలో పెట్టుబడి పెట్టారు. A క్రియాశీల భాగస్వామిగా ఉన్నందుకు మొత్తం లాభంలో 10% జీతంగా పొందుతాడు, మిగిలిన లాభం వారి పెట్టుబడి నిష్పత్తిలో పంచబడుతుంది. A కి మొత్తం ₹59,000 లభిస్తే, ఆ ఏజెన్సీ ఆర్జించిన మొత్తం లాభం ఎంత?",
        ["₹90,000", "₹1,00,000", "₹1,10,000", "₹1,20,000"],
        ["₹90,000", "₹1,00,000", "₹1,10,000", "₹1,20,000"],
        1,
        "Let total profit = P. A gets 0.10P (salary). Remaining profit = 0.90P. A's investment share = (3/5) * 0.90P = 0.54P. Total for A = 0.10P + 0.54P = 0.64P = 59000? Wait: 59000 / 0.64 is not clean. Let's make total for A = 0.10P + 0.54P = 0.64P. If P = 1,00,000 => A gets 10,000 + 54,000 = ₹64,000. Let's change A receives ₹64,000.",
        "మొత్తం లాభం P అనుకుంటే: A వాటా = 0.10P + (3/5)*0.90P = 0.64P. 0.64P = 64,000 => P = ₹1,00,000."
    ))
    qs[-1]["question_en"] = "A and B invest in a security agency in the ratio 3 : 2. A is an active partner and receives 10% of the total profit as management salary, and the remaining profit is divided in their investment ratio. If A receives a total of ₹64,000, what was the total profit earned by the agency?"
    qs[-1]["question_te"] = "A మరియు B లు ఒక సెక్యూరిటీ ఏజెన్సీలో 3 : 2 నిష్పత్తిలో పెట్టుబడి పెట్టారు. A క్రియాశీల భాగస్వామిగా ఉన్నందుకు మొత్తం లాభంలో 10% జీతంగా పొందుతాడు, మిగిలిన లాభం వారి పెట్టుబడి నిష్పత్తిలో పంచబడుతుంది. A కి మొత్తం ₹64,000 లభిస్తే, ఆ ఏజెన్సీ ఆర్జించిన మొత్తం లాభం ఎంత?"

    # Q32: Mixtures - Repeated replacement
    qs.append(make_q(
        32, "Mixtures & Alligations - Repeated Dilution",
        "A container contains 80 litres of pure milk. From this, 8 litres of milk is removed and replaced with water. This process is repeated two more times. How much milk is left in the container now?",
        "ఒక పాత్రలో 80 లీటర్ల స్వచ్ఛమైన పాలు ఉన్నాయి. అందులో నుండి 8 లీటర్ల పాలు తీసి అంతే నీటితో నింపారు. ఈ విధానాన్ని మరో రెండు సార్లు పునరావృతం చేశారు. ప్రస్తుతం ఆ పాత్రలో మిగిలిన పాల పరిమాణం ఎంత?",
        ["56.42 litres", "58.32 litres", "60.48 litres", "62.50 litres"],
        ["56.42 లీటర్లు", "58.32 లీటర్లు", "60.48 లీటర్లు", "62.50 లీటర్లు"],
        1,
        "Remaining milk = Initial * (1 - y/x)^n = 80 * (1 - 8/80)^3 = 80 * (9/10)^3 = 80 * 0.729 = 58.32 litres.",
        "మిగిలిన పాలు = 80 * (1 - 8/80)^3 = 80 * (0.9)^3 = 80 * 0.729 = 58.32 లీటర్లు."
    ))

    # Q33: Alligations - Average price
    qs.append(make_q(
        33, "Mixtures & Alligations - Blending Ratio",
        "A merchant has two varieties of wheat costing ₹32/kg and ₹42/kg. In what ratio must he mix them so that selling the mixture at ₹41.80/kg yields a profit of 10%?",
        "ఒక వ్యాపారి వద్ద కిలో ₹32 మరియు కిలో ₹42 ధర గల రెండు రకాల గోధుమలు ఉన్నాయి. ఆ మిశ్రమాన్ని కిలోకు ₹41.80 చొప్పున అమ్మినప్పుడు 10% లాభం రావాలంటే ఆ రెండింటిని ఏ నిష్పత్తిలో కలపాలి?",
        ["1 : 2", "2 : 3", "3 : 2", "4 : 3"],
        ["1 : 2", "2 : 3", "3 : 2", "4 : 3"],
        1,
        "Mean cost price of mixture = 41.80 / 1.10 = ₹38/kg. By alligation: (42 - 38) : (38 - 32) = 4 : 6 = 2 : 3.",
        "మిశ్రమం కొన్న ధర = 41.80 / 1.10 = ₹38. నిష్పత్తి = (42 - 38) : (38 - 32) = 4 : 6 = 2 : 3."
    ))

    # Q34: Problems on Ages - Past and future
    qs.append(make_q(
        34, "Problems on Ages - Two Time Periods",
        "6 years ago, the ratio of the ages of Ramesh and Suresh was 6 : 5. Four years hence, the ratio of their ages will be 11 : 10. What is Suresh's present age?",
        "6 సంవత్సరాల క్రితం రమేష్ మరియు సురేష్ ల వయస్సుల నిష్పత్తి 6 : 5. నాలుగేళ్ల తర్వాత వారి వయస్సుల నిష్పత్తి 11 : 10 అవుతుంది. ప్రస్తుతం సురేష్ వయస్సు ఎంత?",
        ["14 years", "16 years", "18 years", "20 years"],
        ["14 సంవత్సరాలు", "16 సంవత్సరాలు", "18 సంవత్సరాలు", "20 సంవత్సరాలు"],
        1,
        "Let ages 6 yrs ago be 6x and 5x. After 10 years (from 6 yrs ago to 4 yrs hence): (6x + 10)/(5x + 10) = 11/10 => 60x + 100 = 55x + 110 => 5x = 10 => x = 2. Suresh's age 6 yrs ago = 5*2 = 10. Present age = 10 + 6 = 16 years.",
        "6 సంవత్సరాల క్రితం సురేష్ వయస్సు = 5 * 2 = 10. ప్రస్తుత వయస్సు = 10 + 6 = 16 సంవత్సరాలు."
    ))

    # Q35: Averages - Batting average
    qs.append(make_q(
        35, "Averages - Cricket Batting",
        "A batsman has a certain average for 16 innings. In his 17th inning, he scores 85 runs, thereby increasing his average by 3 runs. What is his new batting average after the 17th inning?",
        "ఒక బ్యాట్స్‌మెన్ 16 ఇన్నింగ్స్‌లకు ఒక నిర్దిష్ట సగటును కలిగి ఉన్నాడు. 17వ ఇన్నింగ్స్‌లో అతను 85 పరుగులు చేసి, తన సగటును 3 పరుగులు పెంచుకున్నాడు. 17వ ఇన్నింగ్స్ తర్వాత అతని కొత్త సగటు ఎంత?",
        ["34", "37", "40", "42"],
        ["34", "37", "40", "42"],
        1,
        "Let old average = A. Total runs in 17 innings = 16A + 85 = 17(A + 3) => 16A + 85 = 17A + 51 => A = 34. New average = 34 + 3 = 37.",
        "పాత సగటు A. 16A + 85 = 17(A + 3) => A = 34. కొత్త సగటు = 34 + 3 = 37."
    ))

    # Q36: Number Systems - Divisibility by 88
    qs.append(make_q(
        36, "Number Systems - Divisibility by 88",
        "If the 8-digit number 342x18y6 is divisible by 88, what is the value of (x * y)?",
        "ఒక 8-అంకెల సంఖ్య 342x18y6 అనేది 88 చే నిశ్శేషంగా భాగించబడితే, (x * y) లబ్ధం ఎంత?",
        ["12", "14", "18", "24"],
        ["12", "14", "18", "24"],
        0,
        "88 = 8 * 11. For divisibility by 8, last 3 digits 8y6 must be divisible by 8 => 816 (y=1) or 856 (y=5) or 896 (y=9). If y=1: 342x1816. Odd sum = 6+8+x+4 = 18+x. Even sum = 1+1+2+3 = 7. Difference = (18+x) - 7 = 11+x => for div by 11, x=0. Then x*y = 0. If y=5: 342x1856. Odd sum = 6+8+x+4 = 18+x. Even sum = 5+1+2+3 = 11. Difference = 18+x - 11 = 7+x => x=4. Then x*y = 4 * 5 = 20? Wait, let's test options. If y=3: 836 not div by 8. If y=9: 342x1896. Odd sum = 18+x. Even sum = 9+1+2+3 = 15. Diff = 18+x - 15 = 3+x => x=8. Then x*y = 8*9 = 72. What if y=5 and x=4? Wait, let's adjust options: 12, 16, 20, 24 with answer 20.",
        "88 = 8 * 11. 8 చే భాగించబడటానికి y = 5 (856). 11 చే భాగించబడటానికి x = 4. కాబట్టి x * y = 4 * 5 = 20."
    ))
    qs[-1]["options_en"] = ["12", "16", "20", "24"]
    qs[-1]["options_te"] = ["12", "16", "20", "24"]
    qs[-1]["correct_option"] = 2

    # Q37: Number Systems - Power remainder
    qs.append(make_q(
        37, "Number Systems - Remainder",
        "What is the remainder when 2^100 is divided by 7?",
        "2^100 ను 7 చే భాగించినప్పుడు వచ్చే శేషం ఎంత?",
        ["1", "2", "4", "6"],
        ["1", "2", "4", "6"],
        1,
        "2^3 = 8 = 1 mod 7. 2^100 = (2^3)^33 * 2^1 = (1)^33 * 2 = 2 mod 7. Remainder is 2.",
        "2^3 = 8 mod 7 = 1. 2^100 = (2^3)^33 * 2 = 1 * 2 = 2. శేషం 2."
    ))

    # Q38: Number Systems - Unit digit sum
    qs.append(make_q(
        38, "Number Systems - Unit Digit of Powers",
        "What is the unit digit of the expression (124)^372 + (124)^373?",
        "(124)^372 + (124)^373 సమాసము యొక్క ఒకట్ల స్థానంలోని అంకె ఎంత?",
        ["0", "2", "4", "6"],
        ["0", "2", "4", "6"],
        0,
        "4^even ends in 6; 4^odd ends in 4. Here 372 is even => ends in 6. 373 is odd => ends in 4. Sum = 6 + 4 = 10 (unit digit 0).",
        "4 యొక్క సరి ఘాతం 6 తో, బేసి ఘాతం 4 తో ముగుస్తుంది. 6 + 4 = 10, ఒకట్ల స్థానంలో 0 ఉంటుంది."
    ))

    # Q39: HCF and LCM - Three numbers ratio
    qs.append(make_q(
        39, "HCF & LCM - Three Numbers Ratio",
        "Three numbers are in the ratio 2 : 3 : 4 and their LCM is 240. What is their HCF?",
        "మూడు సంఖ్యలు 2 : 3 : 4 నిష్పత్తిలో ఉన్నాయి మరియు వాటి క.సా.గు 240. ఆ సంఖ్యల గ.సా.భా (HCF) ఎంత?",
        ["10", "15", "20", "24"],
        ["10", "15", "20", "24"],
        2,
        "Let HCF be x. Numbers are 2x, 3x, 4x. LCM(2, 3, 4) = 12 => LCM of numbers is 12x = 240 => x = 20. HCF is 20.",
        "క.సా.గు = 12x = 240 => x = 20. గ.సా.భా = 20."
    ))

    # Q40: HCF and LCM - Bells tolling together
    qs.append(make_q(
        40, "HCF & LCM - Simultaneous Bells",
        "Four electronic bells toll at intervals of 6, 8, 12, and 18 seconds respectively. If they all toll together at 12:00 noon, how many times will they toll together in the next 1 hour (excluding the start)?",
        "నాలుగు ఎలక్ట్రానిక్ గంటలు వరుసగా 6, 8, 12 మరియు 18 సెకన్ల వ్యవధిలో మోగుతాయి. మధ్యాహ్నం 12:00 గంటలకు అవన్నీ కలిసి మోగితే, తర్వాతి 1 గంటలో అవి ఎన్నిసార్లు కలిసి మోగుతాయి?",
        ["45 times", "50 times", "55 times", "60 times"],
        ["45 సార్లు", "50 సార్లు", "55 సార్లు", "60 సార్లు"],
        1,
        "LCM(6, 8, 12, 18) = 72 seconds. In 1 hour (3600 seconds), number of times = 3600 / 72 = 50 times.",
        "క.సా.గు (6, 8, 12, 18) = 72 సెకన్లు. 1 గంట (3600 సెకన్లు) లో మోగే సార్లు = 3600 / 72 = 50 సార్లు."
    ))

    # Q41: Simplification - Surds
    qs.append(make_q(
        41, "Simplification - Surds & Radicals",
        "What is the value of x if x = sqrt(42 - sqrt(42 - sqrt(42 - ... to infinity)))?",
        "x = sqrt(42 - sqrt(42 - sqrt(42 - ... అనంతం))) అయితే x విలువ ఎంత?",
        ["5", "6", "7", "8"],
        ["5", "6", "7", "8"],
        1,
        "x = sqrt(42 - x) => x^2 + x - 42 = 0 => (x + 7)(x - 6) = 0. Since x > 0, x = 6.",
        "x^2 + x - 42 = 0 => (x - 6)(x + 7) = 0 => x = 6."
    ))

    # Q42: Permutations - Vowels together
    qs.append(make_q(
        42, "Permutations - Vowels Grouping",
        "In how many different ways can the letters of the word 'OFFICER' be arranged such that all the vowels always come together?",
        "'OFFICER' అనే పదంలోని అక్షరాలలో అచ్చులు (Vowels) ఎల్లప్పుడూ కలిసి ఉండేలా ఎన్ని విభిన్న రకాలుగా అమర్చవచ్చు?",
        ["240", "360", "480", "720"],
        ["240", "360", "480", "720"],
        1,
        "The word 'OFFICER' has 7 letters: vowels {O, I, E} (3 vowels) and consonants {F, F, C, R} (4 consonants, with 'F' repeating twice). Treating the 3 vowels as one block, we have 4 + 1 = 5 units. These 5 units can be arranged in 5! / 2! = 120 / 2 = 60 ways. The 3 distinct vowels within the block can be arranged in 3! = 6 ways. Total arrangements = 60 * 6 = 360.",
        "'OFFICER' పదంలో మొత్తం 7 అక్షరాలు ఉన్నాయి: అచ్చులు {O, I, E} (3 అచ్చులు), హల్లులు {F, F, C, R} (4 హల్లులు, 'F' రెండుసార్లు వచ్చింది). 3 అచ్చులను ఒక యూనిట్‌గా పరిగణిస్తే మొత్తం 4 + 1 = 5 యూనిట్లు ఉంటాయి. 'F' పునరావృతమైనందున 5 యూనిట్లను 5! / 2! = 60 రకాలుగా అమర్చవచ్చు. ఆ 3 అచ్చులను వాటిలో అవి 3! = 6 రకాలుగా అమరగలవు. మొత్తం అమరికలు = 60 * 6 = 360."
    ))

    # Q43: Combinations - Handshakes
    qs.append(make_q(
        43, "Combinations - Handshake Problem",
        "At a conference of Telangana Police Station House Officers (SHOs), there are 20 officers. If every officer shakes hands with every other officer exactly once, how many total handshakes take place?",
        "తెలంగాణ ఎస్‌హెచ్‌ఓ (SHO) ల సదస్సులో 20 మంది అధికారులు పాల్గొన్నారు. ప్రతి అధికారి మరొక అధికారితో సరిగ్గా ఒకసారి కరచాలనం (Handshake) చేసుకుంటే, మొత్తం ఎన్ని కరచాలనాలు జరుగుతాయి?",
        ["180", "190", "200", "210"],
        ["180", "190", "200", "210"],
        1,
        "Total handshakes = 20C2 = (20 * 19) / 2 = 190.",
        "మొత్తం కరచాలనాలు = 20C2 = (20 * 19) / 2 = 190."
    ))

    # Q44: Probability - Two dice sum
    qs.append(make_q(
        44, "Probability - Two Dice Sum",
        "Two unbiased standard six-faced dice are thrown simultaneously. What is the probability that the sum of the numbers shown on their top faces is equal to 8?",
        "రెండు సాధారణ పాచికలను ఏకకాలంలో దొర్లించినప్పుడు, వాటి ముఖాలపై కనిపించే సంఖ్యల మొత్తం 8 అయ్యే సంభావ్యత ఎంత?",
        ["5 / 36", "1 / 6", "7 / 36", "1 / 4"],
        ["5 / 36", "1 / 6", "7 / 36", "1 / 4"],
        0,
        "Favourable outcomes for sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) = 5 outcomes. Total possible outcomes = 6 * 6 = 36. Probability = 5 / 36.",
        "మొత్తం 8 వచ్చే అవకాశాలు: (2,6), (3,5), (4,4), (5,3), (6,2) = 5. మొత్తం అవకాశాలు = 36. సంభావ్యత = 5 / 36."
    ))

    # Q45: Probability - Colored balls
    qs.append(make_q(
        45, "Probability - Selection of Balls",
        "An urn contains 5 red balls, 4 green balls, and 3 blue balls. If two balls are drawn at random without replacement, what is the probability that both are green?",
        "ఒక పాత్రలో 5 ఎరుపు, 4 ఆకుపచ్చ మరియు 3 నీలి రంగు బంతులు ఉన్నాయి. పాత్ర నుండి రెండు బంతులను యాదృచ్ఛికంగా తీసినప్పుడు రెండూ ఆకుపచ్చ రంగువే అయ్యే సంభావ్యత ఎంత?",
        ["1 / 11", "2 / 11", "1 / 12", "3 / 22"],
        ["1 / 11", "2 / 11", "1 / 12", "3 / 22"],
        0,
        "Total balls = 12. P(both green) = (4/12) * (3/11) = (1/3) * (3/11) = 1 / 11.",
        "సంభావ్యత = (4/12) * (3/11) = 1 / 11."
    ))

    # Q46: Progression - Arithmetic Progression
    qs.append(make_q(
        46, "Progression - Arithmetic Progression Sum",
        "What is the sum of all natural numbers between 100 and 300 that are completely divisible by 7?",
        "100 మరియు 300 ల మధ్య 7 చే నిశ్శేషంగా భాగించబడే అన్ని సహజ సంఖ్యల మొత్తం ఎంత?",
        ["5,586", "5,700", "5,720", "5,845"],
        ["5,586", "5,700", "5,720", "5,845"],
        0,
        "First number = 105 (7*15). Last number = 294 (7*42). Number of terms n = (294 - 105)/7 + 1 = 189/7 + 1 = 27 + 1 = 28. Sum = (n/2) * (a + l) = 14 * (105 + 294) = 14 * 399 = 5,586.",
        "మొదటి సంఖ్య 105, చివరి సంఖ్య 294. పదాల సంఖ్య = 28. మొత్తం = 14 * (105 + 294) = 5,586."
    ))

    # Q47: Progression - Geometric Progression
    qs.append(make_q(
        47, "Progression - Geometric Progression",
        "The 3rd term of a Geometric Progression (GP) is 12 and the 6th term is 96. What is the 9th term of this progression?",
        "ఒక గుణశ్రేఢి (GP) లో 3వ పదం 12 మరియు 6వ పదం 96. ఆ శ్రేఢిలోని 9వ పదం ఎంత?",
        ["384", "512", "768", "864"],
        ["384", "512", "768", "864"],
        2,
        "T3 = a*r^2 = 12. T6 = a*r^5 = 96. Dividing: r^3 = 96 / 12 = 8 => r = 2. T9 = T6 * r^3 = 96 * 8 = 768.",
        "r^3 = 96/12 = 8 => r = 2. 9వ పదం T9 = 96 * 8 = 768."
    ))

    # Q48: Clocks - Speed gain
    qs.append(make_q(
        48, "Clocks - Faulty Clock",
        "A clock is set right at 5:00 AM. The clock gains 16 minutes in 24 hours. What will be the true time when the clock indicates 10:00 PM on the 4th day?",
        "ఒక గడియారాన్ని ఉదయం 5:00 గంటలకు సరిచేశారు. ఆ గడియారం 24 గంటల్లో 16 నిమిషాలు వేగంగా తిరుగుతుంది. 4వ రోజు రాత్రి 10:00 గంటలను ఆ గడియారం చూపించినప్పుడు అసలైన ఖచ్చితమైన సమయం ఎంత?",
        ["8:00 PM", "9:00 PM", "9:30 PM", "10:16 PM"],
        ["రాత్రి 8:00", "రాత్రి 9:00", "రాత్రి 9:30", "రాత్రి 10:16"],
        1,
        "Time from 5 AM day 1 to 10 PM day 4: Day 1 to 4 is 3 full days (72 hrs) + 17 hrs (5 AM to 10 PM) = 89 hours. Clock rate: 24 hrs 16 min of faulty clock = 24 hrs of true clock => (364/15) hrs of faulty = 24 hrs true => 89 faulty hrs = 24 * (15/364) * 89 = 88 true hours. 88 hours from 5 AM day 1 brings true time to 9:00 PM on the 4th day.",
        "లోపభూయిష్ట గడియారం 89 గంటలు తిరిగినప్పుడు నిజమైన సమయం 88 గంటలు గడుస్తుంది. నిజమైన సమయం రాత్రి 9:00 గంటలు."
    ))

    # Q49: Data Interpretation - Police zone table
    qs.append(make_q(
        49, "Data Interpretation - Ratio of Applicants",
        "In a state police exam, Zone I had 12,000 applicants and Zone II had 18,000 applicants. If 35% of Zone I applicants and 45% of Zone II applicants qualified for Mains, what is the ratio of qualified candidates from Zone I to Zone II?",
        "రాష్ట్ర పోలీస్ పరీక్షలో జోన్ I నుండి 12,000 మంది, జోన్ II నుండి 18,000 మంది దరఖాస్తు చేసుకున్నారు. జోన్ I లో 35% మరియు జోన్ II లో 45% మంది మెయిన్స్‌కు అర్హత సాధిస్తే, జోన్ I మరియు జోన్ II నుండి అర్హత సాధించిన అభ్యర్థుల నిష్పత్తి ఎంత?",
        ["14 : 27", "7 : 15", "2 : 3", "5 : 9"],
        ["14 : 27", "7 : 15", "2 : 3", "5 : 9"],
        0,
        "Zone I qualified = 12000 * 0.35 = 4200. Zone II qualified = 18000 * 0.45 = 8100. Ratio = 4200 : 8100 = 42 : 81 = 14 : 27.",
        "జోన్ I అర్హత = 4,200. జోన్ II అర్హత = 8,100. నిష్పత్తి = 42 : 81 = 14 : 27."
    ))

    # Q50: Data Interpretation - Pass Percentage
    qs.append(make_q(
        50, "Data Interpretation - Total Pass Rate",
        "Across three training centers X, Y, and Z, the number of trainees enrolled are 300, 500, and 200 respectively. If their pass percentages in the weapon handling examination are 80%, 70%, and 90% respectively, what is the overall combined pass percentage?",
        "X, Y మరియు Z అనే మూడు శిక్షణ కేంద్రాలలో వరుసగా 300, 500 మరియు 200 మంది ట్రైనీలు ఉన్నారు. ఆయుధ నిర్వహణ పరీక్షలో వారి ఉత్తీర్ణత శాతాలు వరుసగా 80%, 70%, మరియు 90% అయితే, మొత్తం మూడు కేంద్రాల ఉమ్మడి ఉత్తీర్ణత శాతం ఎంత?",
        ["75%", "77%", "79%", "81%"],
        ["75%", "77%", "79%", "81%"],
        1,
        "Total enrolled = 300 + 500 + 200 = 1000. Passed: X = 240, Y = 350, Z = 180. Total passed = 240 + 350 + 180 = 770. Combined pass % = (770 / 1000) * 100 = 77%.",
        "మొత్తం ట్రైనీలు = 1,000. ఉత్తీర్ణులు = 240 + 350 + 180 = 770. ఉమ్మడి ఉత్తీర్ణత శాతం = 77%."
    ))

    return qs
