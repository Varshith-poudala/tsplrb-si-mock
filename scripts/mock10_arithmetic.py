# -*- coding: utf-8 -*-
"""
Mock Test 10 - Arithmetic & Quantitative Aptitude (Q1 to Q50)
Strictly adheres to TSPLRB SI PWT Blueprint & Shentu's feedback:
- Speed, Distance & Time (Trains, Boats, Circular tracks, Relative Speed)
- Mensuration 2D & 3D (Cylinder, Cone, Sphere, Rhombus, Trapezium, Field Paths)
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
    
    # Q1: Speed Distance Time - Relative speed same direction
    qs.append(make_q(
        1, "Speed, Distance & Time - Relative Speed",
        "A train 180 metres long is moving at a uniform speed of 72 km/h. How much time will it take to overtake a car 4 metres long running at 54 km/h in the same direction?",
        "180 మీటర్ల పొడవు గల రైలు 72 కి.మీ/గం స్థిర వేగంతో ప్రయాణిస్తోంది. అదే దిశలో 54 కి.మీ/గం వేగంతో ప్రయాణిస్తున్న 4 మీటర్ల పొడవు గల కారును అధిగమించడానికి ఎంత సమయం పడుతుంది?",
        ["36.8 seconds", "32.4 seconds", "40.5 seconds", "28.6 seconds"],
        ["36.8 సెకన్లు", "32.4 సెకన్లు", "40.5 సెకన్లు", "28.6 సెకన్లు"],
        0,
        "Total distance = 180 + 4 = 184 m. Relative speed = 72 - 54 = 18 km/h = 18 * (5/18) = 5 m/s. Time = Distance / Speed = 184 / 5 = 36.8 seconds.",
        "మొత్తం దూరం = 180 + 4 = 184 మీటర్లు. సాపేక్ష వేగం = 72 - 54 = 18 కి.మీ/గం = 5 మీ/సె. అవసరమైన సమయం = 184 / 5 = 36.8 సెకన్లు."
    ))

    # Q2: Speed Distance Time - Platform crossing
    qs.append(make_q(
        2, "Speed, Distance & Time - Platform Crossing",
        "A train travelling at 90 km/h crosses a 250-metre long platform in 22 seconds. What is the length of the train?",
        "90 కి.మీ/గం వేగంతో ప్రయాణిస్తున్న ఒక రైలు 250 మీటర్ల పొడవు గల ప్లాట్‌ఫామ్‌ను 22 సెకన్లలో దాటుతుంది. ఆ రైలు పొడవు ఎంత?",
        ["275 metres", "300 metres", "325 metres", "350 metres"],
        ["275 మీటర్లు", "300 మీటర్లు", "325 మీటర్లు", "350 మీటర్లు"],
        1,
        "Speed = 90 * (5/18) = 25 m/s. Total distance covered in 22 s = 25 * 22 = 550 m. Length of train = 550 - 250 = 300 metres.",
        "వేగం = 90 * (5/18) = 25 మీ/సె. 22 సెకన్లలో దాటిన మొత్తం దూరం = 25 * 22 = 550 మీ. రైలు పొడవు = 550 - 250 = 300 మీటర్లు."
    ))

    # Q3: Speed Distance Time - Opposite trains meeting
    qs.append(make_q(
        3, "Speed, Distance & Time - Opposite Trains",
        "Two trains of lengths 140 m and 160 m run on parallel tracks towards each other with speeds of 60 km/h and 48 km/h respectively. In how many seconds will they cross each other from the moment they meet?",
        "140 మీటర్లు మరియు 160 మీటర్ల పొడవు గల రెండు రైళ్లు సమాంతర పట్టాలపై ఎదురెదురుగా వరుసగా 60 కి.మీ/గం మరియు 48 కి.మీ/గం వేగంతో ప్రయాణిస్తున్నాయి. అవి కలిసిన క్షణం నుండి ఒకదానికొకటి పూర్తిగా దాటడానికి ఎన్ని సెకన్లు పడుతుంది?",
        ["10 seconds", "12 seconds", "15 seconds", "8 seconds"],
        ["10 సెకన్లు", "12 సెకన్లు", "15 సెకన్లు", "8 సెకన్లు"],
        0,
        "Total distance = 140 + 160 = 300 m. Relative speed = 60 + 48 = 108 km/h = 108 * (5/18) = 30 m/s. Time = 300 / 30 = 10 seconds.",
        "మొత్తం దూరం = 140 + 160 = 300 మీటర్లు. సాపేక్ష వేగం = 60 + 48 = 108 కి.మీ/గం = 30 మీ/సె. అవసరమైన సమయం = 300 / 30 = 10 సెకన్లు."
    ))

    # Q4: Boats & Streams
    qs.append(make_q(
        4, "Speed, Distance & Time - Boats & Streams",
        "A motorboat can travel at 15 km/h in still water. If the river flows at a speed of 3 km/h, how much total time will it take to travel 36 km downstream and return back upstream to the starting point?",
        "నిశ్చల నీటిలో ఒక మోటార్‌బోట్ వేగం 15 కి.మీ/గం. ప్రవాహ వేగం 3 కి.మీ/గం అయితే, ఆ బోటు ప్రవాహ దిశలో (downstream) 36 కి.మీ వెళ్లి తిరిగి బయలుదేరిన స్థానానికి (upstream) రావడానికి పట్టే మొత్తం సమయం ఎంత?",
        ["4.5 hours", "5 hours", "5.5 hours", "6 hours"],
        ["4.5 గంటలు", "5 గంటలు", "5.5 గంటలు", "6 గంటలు"],
        1,
        "Downstream speed = 15 + 3 = 18 km/h. Downstream time = 36 / 18 = 2 hrs. Upstream speed = 15 - 3 = 12 km/h. Upstream time = 36 / 12 = 3 hrs. Total time = 2 + 3 = 5 hours.",
        "ప్రవాహ దిశలో వేగం = 15 + 3 = 18 కి.మీ/గం (సమయం = 36/18 = 2 గంటలు). ఎదురు ప్రవాహంలో వేగం = 15 - 3 = 12 కి.మీ/గం (సమయం = 36/12 = 3 గంటలు). మొత్తం సమయం = 2 + 3 = 5 గంటలు."
    ))

    # Q5: Speed Distance Time - Late arrival formula
    qs.append(make_q(
        5, "Speed, Distance & Time - Late/Early Formula",
        "Walking at 3/4th of his normal speed, a candidate reaches the TSPLRB examination center 20 minutes late. What is his usual time to cover this journey?",
        "ఒక అభ్యర్థి తన సాధారణ వేగంలో 3/4 వంతు వేగంతో నడవడం వల్ల, TSPLRB పరీక్షా కేంద్రానికి 20 నిమిషాలు ఆలస్యంగా చేరుకుంటాడు. సాధారణ వేగంతో ఆ దూరాన్ని చేరుకోవడానికి అతనికి పట్టే సమయం ఎంత?",
        ["45 minutes", "50 minutes", "60 minutes", "80 minutes"],
        ["45 నిమిషాలు", "50 నిమిషాలు", "60 నిమిషాలు", "80 నిమిషాలు"],
        2,
        "When speed becomes 3/4, time becomes 4/3 of usual time T. Extra time = (4/3)T - T = T/3 = 20 mins => Usual time T = 60 minutes.",
        "వేగం 3/4 వంతు అయినప్పుడు, పట్టే సమయం 4/3T అవుతుంది. అదనపు సమయం = 4/3T - T = T/3 = 20 నిమిషాలు => సాధారణ సమయం T = 60 నిమిషాలు."
    ))

    # Q6: Speed Distance Time - Circular track
    qs.append(make_q(
        6, "Speed, Distance & Time - Circular Track",
        "Two runners A and B start running simultaneously from the same point on a 600-metre circular track in opposite directions with speeds of 4 m/s and 6 m/s. After how many seconds will they meet for the first time?",
        "600 మీటర్ల చుట్టుకొలత గల వృత్తాకార ట్రాక్‌పై ఒకే బిందువు వద్ద A మరియు B అనే ఇద్దరు రన్నర్లు ఒకేసారి ఎదురెదురు దిశల్లో వరుసగా 4 మీ/సె మరియు 6 మీ/సె వేగంతో పరుగెత్తడం ప్రారంభించారు. వారు మొదటిసారి ఎన్ని సెకన్ల తర్వాత కలుసుకుంటారు?",
        ["60 seconds", "75 seconds", "100 seconds", "120 seconds"],
        ["60 సెకన్లు", "75 సెకన్లు", "100 సెకన్లు", "120 సెకన్లు"],
        0,
        "Opposite directions relative speed = 4 + 6 = 10 m/s. Track length = 600 m. Time to first meeting = 600 / 10 = 60 seconds.",
        "వ్యతిరేక దిశల్లో సాపేక్ష వేగం = 4 + 6 = 10 మీ/సె. మొదటిసారి కలిసే సమయం = 600 / 10 = 60 సెకన్లు."
    ))

    # Q7: Speed Distance Time - Average speed
    qs.append(make_q(
        7, "Speed, Distance & Time - Average Speed",
        "A police patrol vehicle travels from Hyderabad to Warangal at a speed of 60 km/h and returns along the same route at 90 km/h. What is the average speed of the vehicle for the entire round trip?",
        "ఒక పోలీస్ పెట్రోలింగ్ వాహనం హైదరాబాద్ నుండి వరంగల్‌కు 60 కి.మీ/గం వేగంతో వెళ్లి, అదే మార్గంలో 90 కి.మీ/గం వేగంతో తిరిగి వచ్చింది. ఆ ప్రయాణం మొత్తానికి వాహనం యొక్క సగటు వేగం ఎంత?",
        ["72 km/h", "75 km/h", "70 km/h", "80 km/h"],
        ["72 కి.మీ/గం", "75 కి.మీ/గం", "70 కి.మీ/గం", "80 కి.మీ/గం"],
        0,
        "For equal distances, Average speed = 2*x*y / (x + y) = (2 * 60 * 90) / (60 + 90) = 10800 / 150 = 72 km/h.",
        "సమాన దూరాలకు సగటు వేగం = 2xy / (x + y) = (2 * 60 * 90) / 150 = 10800 / 150 = 72 కి.మీ/గం."
    ))

    # Q8: Speed Distance Time - Distance headstart
    qs.append(make_q(
        8, "Speed, Distance & Time - Headstart & Catch-up",
        "A thief flees on a motorcycle at 45 km/h. A police sub-inspector discovers the theft after 20 minutes and pursues him in a jeep at 60 km/h. At what distance from the crime spot will the police intercept the thief?",
        "ఒక దొంగ మోటార్ సైకిల్‌పై 45 కి.మీ/గం వేగంతో పారిపోయాడు. 20 నిమిషాల తర్వాత దొంగతనాన్ని గమనించిన పోలీస్ సబ్-ఇన్‌స్పెక్టర్ జీపులో 60 కి.మీ/గం వేగంతో వెంబడించారు. నేరం జరిగిన స్థలం నుండి ఎంత దూరంలో పోలీసులు దొంగను పట్టుకుంటారు?",
        ["45 km", "60 km", "75 km", "50 km"],
        ["45 కి.మీ", "60 కి.మీ", "75 కి.మీ", "50 కి.మీ"],
        1,
        "Head start distance in 20 mins (1/3 hr) = 45 * (1/3) = 15 km. Relative speed = 60 - 45 = 15 km/h. Time to catch = 15 / 15 = 1 hour. Distance covered by police in 1 hr = 60 * 1 = 60 km.",
        "20 నిమిషాలలో దొంగ ప్రయాణించిన దూరం = 45 * (1/3) = 15 కి.మీ. సాపేక్ష వేగం = 60 - 45 = 15 కి.మీ/గం. పట్టుకోవడానికి పట్టే సమయం = 15/15 = 1 గంట. 1 గంటలో పోలీస్ జీపు ప్రయాణించిన దూరం = 60 * 1 = 60 కి.మీ."
    ))

    # Q9: Mensuration 2D - Rhombus
    qs.append(make_q(
        9, "Mensuration 2D - Rhombus",
        "The diagonals of a rhombus are 24 cm and 10 cm respectively. What is the perimeter of this rhombus?",
        "ఒక రాంబస్ యొక్క కర్ణాలు వరుసగా 24 సెం.మీ మరియు 10 సెం.మీ. ఆ రాంబస్ యొక్క చుట్టుకొలత ఎంత?",
        ["48 cm", "52 cm", "60 cm", "68 cm"],
        ["48 సెం.మీ", "52 సెం.మీ", "60 సెం.మీ", "68 సెం.మీ"],
        1,
        "Diagonals bisect at right angles: half diagonals are 12 cm and 5 cm. Side a = sqrt(12^2 + 5^2) = sqrt(144 + 25) = 13 cm. Perimeter = 4 * 13 = 52 cm.",
        "రాంబస్ కర్ణాలు పరస్పరం లంబంగా సమద్విఖండన చేసుకుంటాయి. కర్ణాల సగాలు = 12 సెం.మీ, 5 సెం.మీ. భుజం a = sqrt(12^2 + 5^2) = 13 సెం.మీ. చుట్టుకొలత = 4 * 13 = 52 సెం.మీ."
    ))

    # Q10: Mensuration 2D - Trapezium
    qs.append(make_q(
        10, "Mensuration 2D - Trapezium",
        "The parallel sides of a trapezium are 18 cm and 26 cm, and its area is 308 sq.cm. What is the perpendicular distance (height) between the parallel sides?",
        "ఒక ట్రెపీజియం సమాంతర భుజాలు 18 సెం.మీ మరియు 26 సెం.మీ, మరియు దాని వైశాల్యం 308 చ.సెం.మీ. ఆ సమాంతర భుజాల మధ్య లంబ దూరం (ఎత్తు) ఎంత?",
        ["12 cm", "14 cm", "16 cm", "18 cm"],
        ["12 సెం.మీ", "14 సెం.మీ", "16 సెం.మీ", "18 సెం.మీ"],
        1,
        "Area = 1/2 * (a + b) * h => 308 = 1/2 * (18 + 26) * h = 22 * h => h = 308 / 22 = 14 cm.",
        "ట్రెపీజియం వైశాల్యం = 1/2 * (a + b) * h => 308 = 1/2 * (44) * h => 22h = 308 => h = 14 సెం.మీ."
    ))

    # Q11: Mensuration 2D - Uniform gravel path
    qs.append(make_q(
        11, "Mensuration 2D - Rectangular Field Path",
        "A rectangular lawn 40 metres long and 30 metres wide has a uniform gravel path 2.5 metres wide running all around the outside. What is the area of this gravel path?",
        "40 మీటర్ల పొడవు మరియు 30 మీటర్ల వెడల్పు గల ఒక దీర్ఘచతురస్రాకార పచ్చిక బయలు చుట్టూ వెలుపలి వైపు 2.5 మీటర్ల వెడల్పు గల కంకర బాట నిర్మించబడింది. ఆ బాట వైశాల్యం ఎంత?",
        ["350 sq.m", "375 sq.m", "400 sq.m", "425 sq.m"],
        ["350 చ.మీ", "375 చ.మీ", "400 చ.మీ", "425 చ.మీ"],
        1,
        "Outer length = 40 + 2(2.5) = 45 m. Outer width = 30 + 2(2.5) = 35 m. Outer area = 45 * 35 = 1575 sq.m. Inner area = 40 * 30 = 1200 sq.m. Area of path = 1575 - 1200 = 375 sq.m.",
        "బాటతో కలిపి బయటి కొలతలు: పొడవు = 45 మీ, వెడల్పు = 35 మీ. వెలుపలి వైశాల్యం = 45 * 35 = 1575 చ.మీ. లోపలి వైశాల్యం = 40 * 30 = 1200 చ.మీ. బాట వైశాల్యం = 1575 - 1200 = 375 చ.మీ."
    ))

    # Q12: Mensuration 2D - Equilateral triangle inradius
    qs.append(make_q(
        12, "Mensuration 2D - Equilateral Triangle Incircle",
        "The side of an equilateral triangle is 12 cm. What is the area of the incircle inscribed inside this equilateral triangle? (Take pi = 22/7)",
        "ఒక సమబాహు త్రిభుజం భుజం 12 సెం.మీ. ఆ సమబాహు త్రిభుజం లోపల గీయబడిన అంతర్వృత్త వైశాల్యం ఎంత?",
        ["12*pi sq.cm", "16*pi sq.cm", "9*pi sq.cm", "24*pi sq.cm"],
        ["12*pi చ.సెం.మీ", "16*pi చ.సెం.మీ", "9*pi చ.సెం.మీ", "24*pi చ.సెం.మీ"],
        0,
        "Inradius r of equilateral triangle of side a is a / (2*sqrt(3)). Here r = 12 / (2*sqrt(3)) = 6 / sqrt(3) = 2*sqrt(3) cm. Area = pi * r^2 = pi * (2*sqrt(3))^2 = pi * 12 = 12*pi sq.cm.",
        "సమబాహు త్రిభుజ అంతర్వ్యాసార్థం r = a / (2*sqrt(3)) = 12 / (2*sqrt(3)) = 2*sqrt(3) సెం.మీ. వైశాల్యం = pi * r^2 = pi * 12 = 12*pi చ.సెం.మీ."
    ))

    # Q13: Mensuration 3D - Melting cylinder into cones
    qs.append(make_q(
        13, "Mensuration 3D - Recasting Solids",
        "A solid metallic cylinder of radius 6 cm and height 15 cm is melted and recast into small solid cones, each of radius 3 cm and height 5 cm. How many such cones can be formed?",
        "6 సెం.మీ వ్యాసార్థం మరియు 15 సెం.మీ ఎత్తు గల ఒక ఘన లోహ స్తూపాన్ని కరిగించి, ఒక్కొక్కటి 3 సెం.మీ వ్యాసార్థం మరియు 5 సెం.మీ ఎత్తు గల చిన్న ఘన శంకువులుగా మార్చారు. అలా ఎన్ని శంకువులు ఏర్పడతాయి?",
        ["24", "30", "36", "45"],
        ["24", "30", "36", "45"],
        2,
        "Volume of cylinder = pi * R^2 * H = pi * 36 * 15 = 540*pi. Volume of one cone = (1/3) * pi * r^2 * h = (1/3) * pi * 9 * 5 = 15*pi. Number of cones = 540*pi / 15*pi = 36.",
        "స్తూపం ఘనపరిమాణం = pi * 36 * 15 = 540*pi. ఒక శంకువు ఘనపరిమాణం = (1/3) * pi * 9 * 5 = 15*pi. ఏర్పడే శంకువుల సంఖ్య = 540 / 15 = 36."
    ))

    # Q14: Mensuration 3D - Sphere vs circumscribed cylinder
    qs.append(make_q(
        14, "Mensuration 3D - Sphere & Cylinder Ratio",
        "What is the ratio of the volume of a sphere of radius r to the volume of a cylinder of radius r and height equal to the diameter of the sphere?",
        "r వ్యాసార్థం గల గోళం యొక్క ఘనపరిమాణానికి, r వ్యాసార్థం మరియు గోళం వ్యాసానికి సమానమైన ఎత్తు గల స్తూపం యొక్క ఘనపరిమాణానికి గల నిష్పత్తి ఎంత?",
        ["2 : 3", "3 : 4", "1 : 2", "4 : 5"],
        ["2 : 3", "3 : 4", "1 : 2", "4 : 5"],
        0,
        "Volume of sphere = (4/3)*pi*r^3. Cylinder radius = r, height h = 2r. Volume of cylinder = pi*r^2*(2r) = 2*pi*r^3. Ratio = [(4/3)*pi*r^3] / [2*pi*r^3] = 4/6 = 2:3.",
        "గోళం ఘనపరిమాణం = (4/3)*pi*r^3. స్తూపం ఎత్తు h = 2r, ఘనపరిమాణం = 2*pi*r^3. నిష్పత్తి = (4/3) / 2 = 2 : 3."
    ))

    # Q15: Mensuration 3D - Cuboid diagonal
    qs.append(make_q(
        15, "Mensuration 3D - Longest Rod in Room",
        "What is the length of the longest pole that can be placed in a room of dimensions 12 m long, 9 m wide, and 8 m high?",
        "12 మీటర్ల పొడవు, 9 మీటర్ల వెడల్పు మరియు 8 మీటర్ల ఎత్తు గల గదిలో ఉంచగల అత్యంత పొడవైన కర్ర (పోల్) పొడవు ఎంత?",
        ["15 metres", "17 metres", "18 metres", "20 metres"],
        ["15 మీటర్లు", "17 మీటర్లు", "18 మీటర్లు", "20 మీటర్లు"],
        1,
        "Longest diagonal = sqrt(l^2 + b^2 + h^2) = sqrt(12^2 + 9^2 + 8^2) = sqrt(144 + 81 + 64) = sqrt(289) = 17 metres.",
        "గది కర్ణం పొడవు = sqrt(l^2 + b^2 + h^2) = sqrt(144 + 81 + 64) = sqrt(289) = 17 మీటర్లు."
    ))

    # Q16: Mensuration 3D - Hemispherical bowl
    qs.append(make_q(
        16, "Mensuration 3D - Hemispherical Bowl",
        "A metallic hemispherical bowl has an inner diameter of 14 cm. What is its internal curved surface area? (Take pi = 22/7)",
        "ఒక లోహ అర్ధగోళాకార పాత్ర యొక్క అంతర్గత వ్యాసం 14 సెం.మీ. దాని అంతర్గత వక్రతల వైశాల్యం ఎంత?",
        ["308 sq.cm", "462 sq.cm", "616 sq.cm", "154 sq.cm"],
        ["308 చ.సెం.మీ", "462 చ.సెం.మీ", "616 చ.సెం.మీ", "154 చ.సెం.మీ"],
        0,
        "Inner radius r = 14 / 2 = 7 cm. Internal curved surface area = 2 * pi * r^2 = 2 * (22/7) * 49 = 2 * 22 * 7 = 308 sq.cm.",
        "అంతర్గత వ్యాసార్థం r = 7 సెం.మీ. వక్రతల వైశాల్యం = 2*pi*r^2 = 2 * (22/7) * 49 = 308 చ.సెం.మీ."
    ))

    # Q17: Time & Work - Leaving before completion
    qs.append(make_q(
        17, "Time & Work - Leaving Before Completion",
        "A can complete a piece of work in 18 days, while B can do it in 24 days. They began the work together, but A left 3 days before the completion of the work. In how many total days was the work completed?",
        "ఒక పనిని A 18 రోజుల్లో, B 24 రోజుల్లో చేయగలరు. వారిద్దరూ కలిసి పని ప్రారంభించారు, కానీ పని ముగియడానికి 3 రోజుల ముందు A పని నుండి నిష్క్రమించాడు. ఆ పని మొత్తం ఎన్ని రోజుల్లో పూర్తయింది?",
        ["10 days", "12 days", "14 days", "15 days"],
        ["10 రోజులు", "12 రోజులు", "14 రోజులు", "15 రోజులు"],
        1,
        "Let total work = LCM(18, 24) = 72 units. A's rate = 4 units/day, B's rate = 3 units/day. In last 3 days, only B worked = 3 * 3 = 9 units. Remaining work done together = 72 - 9 = 63 units. Days together = 63 / (4 + 3) = 63 / 7 = 9 days. Total days = 9 + 3 = 12 days.",
        "మొత్తం పని = 72 యూనిట్లు. A సామర్థ్యం = 4, B సామర్థ్యం = 3. చివరి 3 రోజులు B ఒక్కడే చేశాడు = 9 యూనిట్లు. మిగిలిన 63 యూనిట్లను ఇద్దరూ కలిసి చేశారు = 63 / 7 = 9 రోజులు. మొత్తం సమయం = 9 + 3 = 12 రోజులు."
    ))

    # Q18: Time & Work - Men vs Women
    qs.append(make_q(
        18, "Time & Work - Men and Women Equivalence",
        "If 12 men or 18 women can harvest a field in 14 days, in how many days can 8 men and 16 women harvest the same field?",
        "12 మంది పురుషులు లేదా 18 మంది స్త్రీలు ఒక పొలాన్ని 14 రోజుల్లో కోయగలరు. అదే పొలాన్ని 8 మంది పురుషులు మరియు 16 మంది స్త్రీలు కలిసి ఎన్ని రోజుల్లో కోయగలరు?",
        ["7 days", "9 days", "10 days", "12 days"],
        ["7 రోజులు", "9 రోజులు", "10 రోజులు", "12 రోజులు"],
        1,
        "12 M = 18 W => 1 M = 1.5 W. So 8 M = 8 * 1.5 = 12 W. 8 M + 16 W = 12 W + 16 W = 28 W. Using W1*D1 = W2*D2: 18 * 14 = 28 * D => D = (18 * 14) / 28 = 9 days.",
        "12 M = 18 W => 1 M = 1.5 W. 8 పురుషులు = 12 స్త్రీలు. మొత్తం స్త్రీలు = 12 + 16 = 28 మంది. D = (18 * 14) / 28 = 9 రోజులు."
    ))

    # Q19: Time & Work - Alternate days
    qs.append(make_q(
        19, "Time & Work - Alternate Days",
        "A and B working alone can complete a job in 12 days and 16 days respectively. If they work on alternate days with A starting on the first day, in how many days will the entire job be finished?",
        "A మరియు B ఒంటరిగా ఒక పనిని వరుసగా 12 రోజులు మరియు 16 రోజుల్లో పూర్తి చేయగలరు. మొదటి రోజు A ప్రారంభించి ఒకరి తర్వాత ఒకరు రోజు విడిచి రోజు పనిచేస్తే, ఆ పని మొత్తం ఎన్ని రోజుల్లో పూర్తవుతుంది?",
        ["13(1/3) days", "13(2/3) days", "13(3/4) days", "14 days"],
        ["13(1/3) రోజులు", "13(2/3) రోజులు", "13(3/4) రోజులు", "14 రోజులు"],
        2,
        "Total work = LCM(12, 16) = 48 units. A = 4 units/day, B = 3 units/day. In 2-day cycle: 4 + 3 = 7 units. In 6 cycles (12 days): 6 * 7 = 42 units. Day 13 (A works): 4 units (total 46 units). Remaining = 2 units. Day 14 (B works): 2/3 day? Wait, B rate is 3, wait, A is 48/12 = 4, B is 48/16 = 3. 42 + 4 = 46. Remaining = 2 units. B takes 2/3 day? Wait, check option: 48 units. 6 cycles = 42 units (12 days). Day 13: A does 4 units => 46 units. Remaining 2 units done by B in 2/3 day => 13(2/3)? Wait, let's check LCM(12, 15)? Wait, 48 - 42 = 6 units. Day 13: A does 4 units. Remaining = 2 units. B rate is 3. So 2/3 day => 13(2/3) days.",
        "మొత్తం పని = 48 యూనిట్లు. 2 రోజుల్లో పని = 7 యూనిట్లు. 6 చక్రాలలో (12 రోజులు) = 42 యూనిట్లు పూర్తవుతాయి. 13వ రోజు A 4 యూనిట్లు చేస్తాడు (మొత్తం 46). మిగిలిన 2 యూనిట్లను B 2/3 రోజులో పూర్తి చేస్తాడు => 13(2/3) రోజులు."
    ))

    # Q20: Pipes and Cisterns - Leak in tank
    qs.append(make_q(
        20, "Pipes & Cisterns - Filling with Leak",
        "A tap can fill an overhead water tank in 8 hours, but due to a leak at the bottom, it takes 10 hours to fill the tank. If the tank is completely full, in how many hours will the leak empty it alone?",
        "ఒక కుళాయి ఒక నీటి ట్యాంకును 8 గంటల్లో నింపగలదు, కానీ అడుగున ఉన్న లీకేజీ కారణంగా ట్యాంక్ నిండటానికి 10 గంటలు పట్టింది. ట్యాంక్ పూర్తిగా నిండి ఉన్నప్పుడు, ఆ లీకేజీ ఒక్కటే ఎన్ని గంటల్లో ట్యాంకును ఖాళీ చేస్తుంది?",
        ["32 hours", "36 hours", "40 hours", "48 hours"],
        ["32 గంటలు", "36 గంటలు", "40 గంటలు", "48 గంటలు"],
        2,
        "Tap rate = 1/8. Net rate = 1/10. Leak rate = 1/8 - 1/10 = (5 - 4)/40 = 1/40. Leak alone empties the tank in 40 hours.",
        "కుళాయి నింపే రేటు = 1/8. లీకేజీతో నిండే రేటు = 1/10. లీకేజీ ఖాళీ చేసే రేటు = 1/8 - 1/10 = 1/40. లీకేజీ ఒక్కటే 40 గంటల్లో ఖాళీ చేస్తుంది."
    ))

    # Q21: Pipes and Cisterns - Multiple pipes
    qs.append(make_q(
        21, "Pipes & Cisterns - Multiple Inlets",
        "Pipe P can fill a reservoir in 15 hours and Pipe Q can fill it in 20 hours. Both pipes are opened together, but Pipe P is closed after 6 hours. How much further time will Pipe Q take to fill the remaining reservoir?",
        "P అనే పైపు ఒక జలాశయాన్ని 15 గంటల్లో, Q అనే పైపు 20 గంటల్లో నింపగలవు. రెండు పైపులను ఒకేసారి తెరిచారు, కానీ 6 గంటల తర్వాత P పైపును మూసివేశారు. మిగిలిన భాగాన్ని నింపడానికి Q పైపునకు ఇంకా ఎంత సమయం పడుతుంది?",
        ["5 hours", "6 hours", "7 hours", "8 hours"],
        ["5 గంటలు", "6 గంటలు", "7 గంటలు", "8 గంటలు"],
        1,
        "Total capacity = LCM(15, 20) = 60 units. P = 4 units/hr, Q = 3 units/hr. In 6 hrs both fill = 6 * (4 + 3) = 42 units. Remaining = 60 - 42 = 18 units. Pipe Q fills 18 units in 18 / 3 = 6 hours.",
        "మొత్తం సామర్థ్యం = 60 యూనిట్లు. 6 గంటల్లో నిండిన నీరు = 6 * 7 = 42 యూనిట్లు. మిగిలినది = 18 యూనిట్లు. Q కి పట్టే సమయం = 18 / 3 = 6 గంటలు."
    ))

    # Q22: Percentages - Price hike & consumption
    qs.append(make_q(
        22, "Percentages - Price Hike & Consumption",
        "If the price of cooking oil increases by 25%, by what percentage must a household reduce its consumption so that the overall expenditure remains unchanged?",
        "వంటనూనె ధర 25% పెరిగితే, ఒక కుటుంబం తన వ్యయం పెరగకుండా ఉండటానికి నూనె వినియోగాన్ని ఎంత శాతం తగ్గించుకోవాలి?",
        ["18%", "20%", "22.5%", "25%"],
        ["18%", "20%", "22.5%", "25%"],
        1,
        "Reduction % = [r / (100 + r)] * 100 = [25 / 125] * 100 = (1/5) * 100 = 20%.",
        "వినియోగంలో తగ్గుదల శాతం = [r / (100 + r)] * 100 = [25 / 125] * 100 = 20%."
    ))

    # Q23: Percentages - Exam marks criteria
    qs.append(make_q(
        23, "Percentages - Examination Passing Marks",
        "In an examination, a candidate securing 35% marks fails by 20 marks, while another candidate securing 45% marks gets 30 marks more than the minimum passing marks. What are the maximum marks of the examination?",
        "ఒక పరీక్షలో 35% మార్కులు సాధించిన అభ్యర్థి 20 మార్కులతో ఫెయిల్ అయ్యాడు, కాగా 45% మార్కులు సాధించిన మరో అభ్యర్థి ఉత్తీర్ణత మార్కుల కంటే 30 మార్కులు ఎక్కువగా పొందాడు. ఆ పరీక్ష గరిష్ట మార్కులు ఎంత?",
        ["450", "500", "550", "600"],
        ["450", "500", "550", "600"],
        1,
        "Difference in % = 45% - 35% = 10%. Difference in marks = 30 - (-20) = 50 marks. 10% of Total = 50 => Total Maximum Marks = (50 / 10) * 100 = 500.",
        "శాతాల తేడా = 10%. మార్కుల తేడా = 30 + 20 = 50 మార్కులు. 10% = 50 అయితే మొత్తం మార్కులు = 500."
    ))

    # Q24: Profit & Loss - Successive discounts
    qs.append(make_q(
        24, "Profit & Loss - Successive Discounts",
        "A shopkeeper marks an article at ₹2,500 and offers two successive discounts of 20% and 10%. What is the final selling price of the article?",
        "ఒక దుకాణదారుడు ఒక వస్తువుపై ₹2,500 ప్రకటన ధరగా నిర్ణయించి, వరుసగా 20% మరియు 10% తగ్గింపులను (డిస్కౌంట్లను) ఇచ్చాడు. ఆ వస్తువు యొక్క తుది అమ్మకపు ధర ఎంత?",
        ["₹1,750", "₹1,800", "₹1,850", "₹1,900"],
        ["₹1,750", "₹1,800", "₹1,850", "₹1,900"],
        1,
        "Single equivalent discount = 20 + 10 - (20*10)/100 = 28%. Selling Price = 2500 * (1 - 0.28) = 2500 * 0.72 = ₹1,800.",
        "మొత్తం తగ్గింపు = 20 + 10 - 2 = 28%. అమ్మకపు ధర = 2500 * 72/100 = ₹1,800."
    ))

    # Q25: Profit & Loss - Same selling price gain and loss
    qs.append(make_q(
        25, "Profit & Loss - Equal Selling Price",
        "A dealer sells two police uniforms for ₹1,980 each. On one he gains 10% and on the other he loses 10%. In the overall transaction, what was his net profit or loss percentage?",
        "ఒక వ్యాపారి రెండు పోలీస్ యూనిఫామ్‌లను ఒక్కొక్కటి ₹1,980 చొప్పున అమ్మాడు. ఒకదానిపై 10% లాభం, మరొకదానిపై 10% నష్టం వచ్చింది. ఈ మొత్తం లావాదేవీలో అతనికి వచ్చిన నికర లాభం లేదా నష్టం శాతం ఎంత?",
        ["1% Profit", "1% Loss", "No profit no loss", "2% Loss"],
        ["1% లాభం", "1% నష్టం", "లాభమూ లేదు నష్టమూ లేదు", "2% నష్టం"],
        1,
        "When two articles are sold at equal SP, one at x% gain and other at x% loss, there is always a loss of (x/10)^2 % = (10/10)^2 = 1% loss.",
        "రెండు వస్తువులను సమాన ధరకు అమ్మి, ఒకదానిపై x% లాభం, మరొకదానిపై x% నష్టం వచ్చినప్పుడు ఎల్లప్పుడూ నష్టమే వస్తుంది: నష్టం % = (x/10)^2 = (1)^2 = 1% నష్టం."
    ))

    # Q26: Profit & Loss - Dishonest trader
    qs.append(make_q(
        26, "Profit & Loss - Dishonest Dealer",
        "A dishonest trader claims to sell his goods at cost price, but uses a false weight of 920 grams instead of 1 kilogram. What is his actual gain percentage?",
        "ఒక వ్యాపారి తన వస్తువులను కొన్న ధరకే అమ్ముతున్నానని చెబుతూ, 1 కిలోగ్రాము బదులుగా 920 గ్రాముల తప్పుడు తూకాన్ని ఉపయోగిస్తున్నాడు. అతని అసలు లాభ శాతం ఎంత?",
        ["8.7%", "8.25%", "9.1%", "7.5%"],
        ["8.7%", "8.25%", "9.1%", "7.5%"],
        0,
        "Gain % = [Error / (True value - Error)] * 100 = [80 / 920] * 100 = (2 / 23) * 100 = 8.695% approx 8.7%.",
        "లాభ శాతం = [లోపం / తప్పుడు తూకం] * 100 = [80 / 920] * 100 = 8.695% దాదాపు 8.7%."
    ))

    # Q27: Simple Interest - Multiplication of sum
    qs.append(make_q(
        27, "Simple Interest - Rate and Time",
        "A sum of money invested at simple interest triples itself in 8 years. In how many years will it become 7 times of itself at the same rate of interest?",
        "సాధారణ వడ్డీ వద్ద పెట్టుబడి పెట్టిన ఒక సొమ్ము 8 సంవత్సరాలలో 3 రెట్లు అవుతుంది. అదే వడ్డీ రేటు వద్ద ఆ సొమ్ము 7 రెట్లు కావడానికి ఎన్ని సంవత్సరాలు పడుతుంది?",
        ["20 years", "24 years", "28 years", "32 years"],
        ["20 సంవత్సరాలు", "24 సంవత్సరాలు", "28 సంవత్సరాలు", "32 సంవత్సరాలు"],
        1,
        "Under SI: (N1 - 1)/T1 = (N2 - 1)/T2 => (3 - 1)/8 = (7 - 1)/T2 => 2/8 = 6/T2 => 1/4 = 6/T2 => T2 = 24 years.",
        "సాధారణ వడ్డీ సూత్రం ప్రకారం: (N1 - 1)/T1 = (N2 - 1)/T2 => (3 - 1)/8 = (7 - 1)/T2 => 2/8 = 6/T2 => T2 = 24 సంవత్సరాలు."
    ))

    # Q28: Compound Interest - CI & SI difference for 2 years
    qs.append(make_q(
        28, "Compound Interest - 2 Year Difference",
        "What is the difference between the compound interest and simple interest on a principal of ₹15,000 for 2 years at an annual interest rate of 8%?",
        "వార్షిక 8% వడ్డీ రేటు చొప్పున ₹15,000 అసలుపై 2 సంవత్సరాలకు చక్రవడ్డీ మరియు సాధారణ వడ్డీల మధ్య తేడా ఎంత?",
        ["₹96", "₹104", "₹112", "₹120"],
        ["₹96", "₹104", "₹112", "₹120"],
        0,
        "Difference for 2 years = P * (R/100)^2 = 15000 * (8/100)^2 = 15000 * (64 / 10000) = 1.5 * 64 = ₹96.",
        "2 సంవత్సరాల తేడా = P * (R/100)^2 = 15000 * (64/10000) = 1.5 * 64 = ₹96."
    ))

    # Q29: Compound Interest - Compounding multiples
    qs.append(make_q(
        29, "Compound Interest - Growth Periods",
        "A sum of money placed at compound interest doubles itself in 5 years. In how many years will it amount to 8 times of itself at the same compound interest rate?",
        "చక్రవడ్డీ వద్ద జమ చేసిన ఒక మొత్తం 5 సంవత్సరాలలో రెట్టింపు అవుతుంది. అదే వడ్డీ రేటు వద్ద ఆ మొత్తం 8 రెట్లు కావడానికి ఎన్ని సంవత్సరాలు పడుతుంది?",
        ["12 years", "15 years", "20 years", "25 years"],
        ["12 సంవత్సరాలు", "15 సంవత్సరాలు", "20 సంవత్సరాలు", "25 సంవత్సరాలు"],
        1,
        "At CI: 2^1 times in 5 years => 8 times = 2^3 times in 5 * 3 = 15 years.",
        "చక్రవడ్డీలో: 5 సంవత్సరాలలో 2^1 రెట్లు అయితే, 8 రెట్లు (2^3) కావడానికి = 5 * 3 = 15 సంవత్సరాలు పడుతుంది."
    ))

    # Q30: Ratio and Proportion - Division of sum
    qs.append(make_q(
        30, "Ratio & Proportion - Division of Amount",
        "An amount of ₹4,200 is divided among A, B, and C such that A : B = 2 : 3 and B : C = 4 : 5. What is the share of B?",
        "₹4,200 మొత్తాన్ని A, B, C లకు A : B = 2 : 3 మరియు B : C = 4 : 5 అయ్యే విధంగా పంచారు. అందులో B యొక్క వాటా ఎంత?",
        ["₹1,200", "₹1,440", "₹1,560", "₹1,600"],
        ["₹1,200", "₹1,440", "₹1,560", "₹1,600"],
        1,
        "Combine ratios: A : B = 8 : 12, B : C = 12 : 15 => A : B : C = 8 : 12 : 15. Total parts = 8 + 12 + 15 = 35. B's share = (12 / 35) * 4200 = 12 * 120 = ₹1,440.",
        "సంయుక్త నిష్పత్తి A : B : C = 8 : 12 : 15. మొత్తం భాగాలు = 35. B వాటా = (12 / 35) * 4200 = ₹1,440."
    ))

    # Q31: Ratio and Proportion - Coin bag
    qs.append(make_q(
        31, "Ratio & Proportion - Coin Bag Problem",
        "A bag contains 50 paise, 25 paise, and 10 paise coins in the ratio 5 : 9 : 4, amounting to a total value of ₹206. What is the total number of coins in the bag?",
        "ఒక సంచిలో 50 పైసలు, 25 పైసలు మరియు 10 పైసల నాణేలు 5 : 9 : 4 నిష్పత్తిలో ఉన్నాయి. వాటి మొత్తం విలువ ₹206 అయితే, ఆ సంచిలోని మొత్తం నాణేల సంఖ్య ఎంత?",
        ["800", "900", "918", "945"],
        ["800", "900", "918", "945"],
        2,
        "Let coins be 5x, 9x, 4x. Total value in rupees = 5x*(0.50) + 9x*(0.25) + 4x*(0.10) = 2.5x + 2.25x + 0.40x = 5.15x = 206 => x = 206 / 5.15 = 40. Total coins = (5 + 9 + 4)*x = 18 * 40 = 720? Wait, let's recalculate 206 / 5.15 = 40. Then 18 * 40 = 720? Wait, let's change 50p, 25p, 10p coins: 5x*0.5 + 9x*0.25 + 4x*0.1 = 5.15x. If x=51: wait, 206 / 5.15 = 40. Total coins = 18 * 40 = 720. Let's fix options to include 720.",
        "నాణేల సంఖ్య = 5x, 9x, 4x. విలువ = 2.5x + 2.25x + 0.4x = 5.15x = ₹206 => x = 40. మొత్తం నాణేలు = 18 * 40 = 720."
    ))
    # Fix Q31 options
    qs[-1]["options_en"] = ["640", "720", "800", "850"]
    qs[-1]["options_te"] = ["640", "720", "800", "850"]
    qs[-1]["correct_option"] = 1

    # Q32: Partnership
    qs.append(make_q(
        32, "Partnership - Profit Sharing",
        "A and B started a business. A invested ₹45,000 for 12 months, while B invested ₹60,000 for 8 months. If the total annual profit was ₹42,000, what was B's share in the profit?",
        "A మరియు B ఒక వ్యాపారాన్ని ప్రారంభించారు. A ₹45,000 ను 12 నెలల పాటు, B ₹60,000 ను 8 నెలల పాటు పెట్టుబడిగా పెట్టారు. వార్షిక లాభం ₹42,000 అయితే, అందులో B యొక్క లాభం ఎంత?",
        ["₹18,000", "₹20,000", "₹22,000", "₹24,000"],
        ["₹18,000", "₹20,000", "₹22,000", "₹24,000"],
        1,
        "Ratio of investments * time = (45000 * 12) : (60000 * 8) = 540 : 480 = 9 : 8. Total parts = 17? Wait, 540 / 60 = 9, 480 / 60 = 8. Wait, if total profit is ₹51,000 then 9+8=17, 42000/17 is not integer. Let's make total profit ₹51,000 or ratio 9:8 with ₹51,000 profit => B gets (8/17)*51000 = 24,000. Let's adjust total profit to ₹51,000.",
        "పెట్టుబడి నిష్పత్తి = (45,000 * 12) : (60,000 * 8) = 540 : 480 = 9 : 8. B వాటా = (8/17) * 51,000 = ₹24,000."
    ))
    qs[-1]["question_en"] = "A and B started a business. A invested ₹45,000 for 12 months, while B invested ₹60,000 for 8 months. If the total annual profit was ₹51,000, what was B's share in the profit?"
    qs[-1]["question_te"] = "A మరియు B ఒక వ్యాపారాన్ని ప్రారంభించారు. A ₹45,000 ను 12 నెలల పాటు, B ₹60,000 ను 8 నెలల పాటు పెట్టుబడిగా పెట్టారు. వార్షిక లాభం ₹51,000 అయితే, అందులో B యొక్క లాభం ఎంత?"
    qs[-1]["correct_option"] = 3

    # Q33: Mixtures & Alligations - Water added
    qs.append(make_q(
        33, "Mixtures & Alligations - Adding Water",
        "A 75-litre mixture contains milk and water in the ratio 4 : 1. How many litres of water must be added to this mixture so that the ratio of milk to water becomes 3 : 1?",
        "75 లీటర్ల మిశ్రమంలో పాలు మరియు నీరు 4 : 1 నిష్పత్తిలో ఉన్నాయి. పాలు మరియు నీటి నిష్పత్తి 3 : 1 కావడానికి ఈ మిశ్రమానికి ఎన్ని లీటర్ల నీరు కలపాలి? (Wait, adding water decreases ratio: let ratio become 3:2)",
        ["10 litres", "12 litres", "15 litres", "20 litres"],
        ["10 లీటర్లు", "12 లీటర్లు", "15 లీటర్లు", "20 లీటర్లు"],
        0,
        "Milk = 75 * (4/5) = 60 L. Water = 15 L. Let water added be x. Milk / (Water + x) = 3 / 2 => 60 / (15 + x) = 3 / 2 => 120 = 45 + 3x => 3x = 75 => x = 25 L. Let's make question: ratio becomes 2:1 => 60 / (15 + x) = 2/1 => 30 = 15 + x => x = 15 litres.",
        "పాలు = 60 లీటర్లు, నీరు = 15 లీటర్లు. నిష్పత్తి 2 : 1 కావడానికి: 60 / (15 + x) = 2/1 => 15 + x = 30 => x = 15 లీటర్లు."
    ))
    qs[-1]["question_en"] = "A 75-litre mixture contains milk and water in the ratio 4 : 1. How many litres of water must be added to this mixture so that the ratio of milk to water becomes 2 : 1?"
    qs[-1]["question_te"] = "75 లీటర్ల మిశ్రమంలో పాలు మరియు నీరు 4 : 1 నిష్పత్తిలో ఉన్నాయి. పాలు మరియు నీటి నిష్పత్తి 2 : 1 కావడానికి ఈ మిశ్రమానికి ఎన్ని లీటర్ల నీరు కలపాలి?"
    qs[-1]["correct_option"] = 2

    # Q34: Alligations - Mixing two varieties
    qs.append(make_q(
        34, "Mixtures & Alligations - Mean Price",
        "In what ratio must rice at ₹48 per kg be mixed with rice at ₹66 per kg so that the resulting mixture is worth ₹54 per kg?",
        "కిలో ₹48 ధర గల బియ్యాన్ని, కిలో ₹66 ధర గల బియ్యంతో ఏ నిష్పత్తిలో కలిపితే ఏర్పడే మిశ్రమం విలువ కిలోకు ₹54 అవుతుంది?",
        ["2 : 1", "3 : 2", "1 : 2", "4 : 3"],
        ["2 : 1", "3 : 2", "1 : 2", "4 : 3"],
        0,
        "By rule of alligation: (66 - 54) / (54 - 48) = 12 / 6 = 2 : 1.",
        "మిశ్రమ సూత్రం ప్రకారం: (66 - 54) : (54 - 48) = 12 : 6 = 2 : 1."
    ))

    # Q35: Problems on Ages
    qs.append(make_q(
        35, "Problems on Ages - Ratio Method",
        "The present age ratio of a father to his son is 5 : 2. After 10 years, the ratio of their ages will become 2 : 1. What is the present age of the father?",
        "తండ్రి మరియు కొడుకుల ప్రస్తుత వయస్సుల నిష్పత్తి 5 : 2. 10 సంవత్సరాల తర్వాత వారి వయస్సుల నిష్పత్తి 2 : 1 అవుతుంది. ప్రస్తుతం తండ్రి వయస్సు ఎంత?",
        ["40 years", "45 years", "50 years", "55 years"],
        ["40 సంవత్సరాలు", "45 సంవత్సరాలు", "50 సంవత్సరాలు", "55 సంవత్సరాలు"],
        2,
        "Let present ages be 5x and 2x. (5x + 10) / (2x + 10) = 2 / 1 => 5x + 10 = 4x + 20 => x = 10. Present age of father = 5 * 10 = 50 years.",
        "ప్రస్తుత వయస్సులు 5x, 2x. (5x + 10) / (2x + 10) = 2/1 => x = 10. తండ్రి ప్రస్తుత వయస్సు = 5 * 10 = 50 సంవత్సరాలు."
    ))

    # Q36: Averages - Misread observation
    qs.append(make_q(
        36, "Averages - Correction of Errors",
        "The average of 30 observations was calculated as 52. Later, it was discovered that an observation of 78 was wrongly recorded as 48. What is the correct average of the observations?",
        "30 పరిశీలనల సగటు 52 గా లెక్కించబడింది. తరువాత, 78 అనే పరిశీలన పొరపాటున 48 గా నమోదు చేయబడిందని గుర్తించారు. ఆ పరిశీలనల యొక్క సరైన సగటు ఎంత?",
        ["53", "54", "55", "52.5"],
        ["53", "54", "55", "52.5"],
        0,
        "Difference = Correct value - Wrong value = 78 - 48 = +30. Increase in average = 30 / 30 = +1. Correct average = 52 + 1 = 53.",
        "సరైన విలువ మరియు తప్పుడు విలువల తేడా = 78 - 48 = +30. సగటులో పెరుగుదల = 30 / 30 = 1. సరైన సగటు = 52 + 1 = 53."
    ))

    # Q37: Averages - Weight replacement
    qs.append(make_q(
        37, "Averages - Replacement in Group",
        "The average weight of 16 police cadets increases by 1.25 kg when one cadet weighing 58 kg is replaced by a new recruit. What is the weight of the new recruit?",
        "58 కేజీల బరువున్న ఒక క్యాడెట్ స్థానంలో కొత్త అభ్యర్థి చేరినప్పుడు 16 మంది పోలీస్ క్యాడెట్ల సగటు బరువు 1.25 కేజీలు పెరిగింది. ఆ కొత్త అభ్యర్థి బరువు ఎంత?",
        ["74 kg", "76 kg", "78 kg", "80 kg"],
        ["74 కేజీలు", "76 కేజీలు", "78 కేజీలు", "80 కేజీలు"],
        2,
        "Total weight increase = 16 * 1.25 = 20 kg. Weight of new recruit = Replaced weight + Total increase = 58 + 20 = 78 kg.",
        "మొత్తం బరువులో పెరుగుదల = 16 * 1.25 = 20 కేజీలు. కొత్త అభ్యర్థి బరువు = 58 + 20 = 78 కేజీలు."
    ))

    # Q38: Number Systems - Remainder theorem
    qs.append(make_q(
        38, "Number Systems - Polynomial Remainder",
        "What is the remainder when (67^67 + 67) is divided by 68?",
        "(67^67 + 67) ను 68 చే భాగించినప్పుడు వచ్చే శేషం ఎంత?",
        ["1", "66", "67", "0"],
        ["1", "66", "67", "0"],
        1,
        "67 = (68 - 1). 67^67 mod 68 = (-1)^67 mod 68 = -1. (-1 + 67) mod 68 = 66 mod 68 = 66.",
        "67 mod 68 = -1. (-1)^67 = -1. (-1 + 67) = 66. కాబట్టి శేషం 66."
    ))

    # Q39: Number Systems - Unit digit
    qs.append(make_q(
        39, "Number Systems - Unit Digit",
        "What is the unit digit of the expression (2153)^167 * (827)^153?",
        "(2153)^167 * (827)^153 లబ్ధం యొక్క ఒకట్ల స్థానంలోని అంకె ఎంత?",
        ["1", "3", "7", "9"],
        ["1", "3", "7", "9"],
        2,
        "Unit digit of 3^167: 167 mod 4 = 3 => 3^3 = 27 (unit digit 7). Unit digit of 7^153: 153 mod 4 = 1 => 7^1 = 7. Product = 7 * 7 = 49 (unit digit 9? Wait: 7 * 7 = 49, unit digit 9!). Let's adjust correct option to 3 (which is 9).",
        "3^167 ఒకట్ల అంకె: 167 mod 4 = 3 => 3^3 = 27 (అంకె 7). 7^153 ఒకట్ల అంకె: 153 mod 4 = 1 => 7^1 = 7. లబ్ధం = 7 * 7 = 49 => ఒకట్ల స్థానం 9."
    ))
    qs[-1]["correct_option"] = 3

    # Q40: Number Systems - Trailing zeros
    qs.append(make_q(
        40, "Number Systems - Trailing Zeros",
        "How many trailing zeros are there at the end of the product of 125! (factorial of 125)?",
        "125! (125 యొక్క ఫ్యాక్టోరియల్) లబ్ధం చివర ఎన్ని సున్నాలు ఉంటాయి?",
        ["28", "30", "31", "35"],
        ["28", "30", "31", "35"],
        2,
        "Trailing zeros in N! = [N/5] + [N/25] + [N/125] = [125/5] + [125/25] + [125/125] = 25 + 5 + 1 = 31.",
        "సున్నాల సంఖ్య = [125/5] + [125/25] + [125/125] = 25 + 5 + 1 = 31."
    ))

    # Q41: Number Systems - Divisibility by 72
    qs.append(make_q(
        41, "Number Systems - Divisibility Rules",
        "If a 9-digit number 785x3678y is completely divisible by 72, what is the value of (x + y)? (Given x and y are single-digit integers)",
        "ఒక 9-అంకెల సంఖ్య 785x3678y అనేది 72 చే నిశ్శేషంగా భాగించబడితే, (x + y) విలువ ఎంత?",
        ["8", "10", "12", "14"],
        ["8", "10", "12", "14"],
        0,
        "72 = 8 * 9. For divisibility by 8, last 3 digits 78y must be divisible by 8 => 784 is divisible by 8 (784 = 8 * 98) => y = 4. For divisibility by 9: sum of digits = 7+8+5+x+3+6+7+8+4 = 48 + x. For 48 + x to be divisible by 9, x = 6. So x + y = 6 + 4 = 10? Wait: 48 + 6 = 54. So x = 6, y = 4 => x + y = 10. Correct option is 1 (value 10).",
        "72 = 8 * 9. 8 చే భాగించబడటానికి: 78y లో y = 4 (784 = 8*98). 9 చే భాగించబడటానికి: అంకెల మొత్తం = 48 + x => x = 6 (54 divisible by 9). x + y = 6 + 4 = 10."
    ))
    qs[-1]["correct_option"] = 1

    # Q42: Number Systems - Recurring decimal
    qs.append(make_q(
        42, "Number Systems - Recurring Decimals",
        "Express the recurring decimal 0.3727272... (with 72 recurring) in the form of a vulgar fraction p/q in its lowest terms.",
        "0.3727272... (72 ఆవర్తనం) అనే ఆవర్తన దశాంశాన్ని కనిష్ట రూపంలో p/q భిన్నంగా మార్చండి.",
        ["41 / 110", "37 / 99", "123 / 330", "43 / 110"],
        ["41 / 110", "37 / 99", "123 / 330", "43 / 110"],
        0,
        "0.3(72) = (372 - 3) / 990 = 369 / 990. Divide numerator and denominator by 9: 369/9 = 41, 990/9 = 110. Fraction = 41 / 110.",
        "0.3(72) = (372 - 3) / 990 = 369 / 990 = 41 / 110."
    ))

    # Q43: HCF and LCM - Product and HCF
    qs.append(make_q(
        43, "HCF & LCM - Possible Pairs",
        "The product of two natural numbers is 2,160 and their HCF is 12. How many pairs of such numbers are possible?",
        "రెండు సహజ సంఖ్యల లబ్ధం 2,160 మరియు వాటి గ.సా.భా (HCF) 12. అటువంటి సంఖ్యల జతలు ఎన్ని సాధ్యమవుతాయి?",
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        1,
        "Let numbers be 12a and 12b (where a, b are co-prime). Product = 12a * 12b = 144ab = 2160 => ab = 2160 / 144 = 15. Co-prime pairs (a, b) multiplying to 15 are (1, 15) and (3, 5). So exactly 2 pairs are possible.",
        "సంఖ్యలు 12a, 12b (a, b లు సాపేక్ష ప్రధాన సంఖ్యలు). 144*a*b = 2160 => a*b = 15. సాధ్యమయ్యే జతలు: (1, 15) మరియు (3, 5). మొత్తం 2 జతలు."
    ))

    # Q44: HCF and LCM - Smallest number with remainder
    qs.append(make_q(
        44, "HCF & LCM - Smallest Number with Remainder",
        "What is the smallest number which when divided by 12, 16, 18, and 24 leaves a remainder of 7 in each case?",
        "12, 16, 18 మరియు 24 లచే భాగించినప్పుడు ప్రతి సందర్భంలోనూ 7 శేషాన్ని ఇచ్చే అతి చిన్న సంఖ్య ఏది?",
        ["137", "144", "151", "167"],
        ["137", "144", "151", "167"],
        2,
        "LCM(12, 16, 18, 24) = 144. Required number = LCM + remainder = 144 + 7 = 151.",
        "క.సా.గు (12, 16, 18, 24) = 144. కావలసిన సంఖ్య = 144 + 7 = 151."
    ))

    # Q45: Simplification - Infinite radical
    qs.append(make_q(
        45, "Simplification - Infinite Radicals",
        "What is the evaluated value of x = sqrt(20 + sqrt(20 + sqrt(20 + ...))) to infinity?",
        "x = sqrt(20 + sqrt(20 + sqrt(20 + ...))) అనంతం వరకు విస్తరించిన సమాసము యొక్క విలువ ఎంత?",
        ["4", "5", "6", "10"],
        ["4", "5", "6", "10"],
        1,
        "x = sqrt(20 + x) => x^2 - x - 20 = 0 => (x - 5)(x + 4) = 0. Since x > 0, x = 5.",
        "x^2 - x - 20 = 0 => (x - 5)(x + 4) = 0 => x = 5."
    ))

    # Q46: Permutations - Letter arrangement
    qs.append(make_q(
        46, "Permutations - Word Letters Arrangement",
        "In how many distinct ways can the letters of the word 'TELANGANA' be arranged?",
        "'TELANGANA' అనే పదంలోని అక్షరాలను ఎన్ని విభిన్న రకాలుగా అమర్చవచ్చు?",
        ["15,120", "30,240", "45,360", "60,480"],
        ["15,120", "30,240", "45,360", "60,480"],
        1,
        "Total letters = 9 (T:1, E:1, L:1, A:3, N:2, G:1). Total distinct arrangements = 9! / (3! * 2!) = 362,880 / (6 * 2) = 362,880 / 12 = 30,240.",
        "మొత్తం అక్షరాలు = 9. A మూడుసార్లు, N రెండుసార్లు ఉన్నాయి. విభిన్న అమరికలు = 9! / (3! * 2!) = 362,880 / 12 = 30,240."
    ))

    # Q47: Combinations - Committee formation
    qs.append(make_q(
        47, "Combinations - Committee Selection",
        "In how many ways can a selection committee of 5 members be chosen from 6 male sub-inspectors and 4 female sub-inspectors such that it contains at least 3 male sub-inspectors?",
        "6 మంది పురుష సబ్-ఇన్‌స్పెక్టర్లు మరియు 4 మంది మహిళా సబ్-ఇన్‌స్పెక్టర్ల నుండి కనీసం 3 మంది పురుషులు ఉండేలా 5 మంది సభ్యుల ఎంపిక కమిటీని ఎన్ని రకాలుగా ఎన్నుకోవచ్చు?",
        ["162", "186", "210", "246"],
        ["162", "186", "210", "246"],
        1,
        "Possibilities: (3M, 2W) + (4M, 1W) + (5M, 0W) = (6C3 * 4C2) + (6C4 * 4C1) + (6C5 * 4C0) = (20 * 6) + (15 * 4) + (6 * 1) = 120 + 60 + 6 = 186.",
        "సాధ్యమయ్యే ఎంపికలు: (6C3 * 4C2) + (6C4 * 4C1) + (6C5 * 4C0) = (20 * 6) + (15 * 4) + (6 * 1) = 120 + 60 + 6 = 186."
    ))

    # Q48: Probability - Cards without replacement
    qs.append(make_q(
        48, "Probability - Cards Without Replacement",
        "Two cards are drawn at random one after another without replacement from a well-shuffled standard pack of 52 playing cards. What is the probability that both cards are Kings?",
        "బాగా కలపబడిన 52 పేక ముక్కల ప్యాక్ నుండి ఒకదాని తర్వాత ఒకటిగా తిరిగి ఉంచకుండా యాదృచ్ఛికంగా రెండు కార్డులను తీశారు. ఆ రెండు కార్డులు కూడా కింగ్స్ (Kings) అయ్యే సంభావ్యత ఎంత?",
        ["1 / 221", "1 / 169", "2 / 221", "4 / 663"],
        ["1 / 221", "1 / 169", "2 / 221", "4 / 663"],
        0,
        "P(both Kings) = (4/52) * (3/51) = (1/13) * (1/17) = 1 / 221.",
        "సంభావ్యత = (4/52) * (3/51) = (1/13) * (1/17) = 1 / 221."
    ))

    # Q49: Data Interpretation - Police recruitment
    qs.append(make_q(
        49, "Data Interpretation - Tabular Analysis",
        "In a district recruitment drive, 4,800 candidates appeared. If 65% of the candidates qualified in the preliminary physical measurements test (PMT) and 40% of the PMT-qualified candidates cleared the 1600-metre running event, how many candidates successfully cleared the running event?",
        "ఒక జిల్లా రిక్రూట్‌మెంట్‌లో 4,800 మంది అభ్యర్థులు హాజరయ్యారు. వారిలో 65% మంది శారీరక కొలతల పరీక్షలో (PMT) అర్హత సాధించారు మరియు PMT అర్హత సాధించిన వారిలో 40% మంది 1600 మీటర్ల రన్నింగ్ ఈవెంట్‌ను పూర్తి చేశారు. రన్నింగ్ ఈవెంట్‌ను విజయవంతంగా పూర్తి చేసిన అభ్యర్థుల సంఖ్య ఎంత?",
        ["1,184", "1,248", "1,312", "1,420"],
        ["1,184", "1,248", "1,312", "1,420"],
        1,
        "PMT qualified = 4800 * 0.65 = 3120. Running cleared = 3120 * 0.40 = 1248.",
        "PMT అర్హత = 4800 * 0.65 = 3120. రన్నింగ్ క్లియర్ చేసిన వారు = 3120 * 0.40 = 1248."
    ))

    # Q50: Data Interpretation - Percentage comparison
    qs.append(make_q(
        50, "Data Interpretation - Percentage Distribution",
        "In a police training academy batch of 600 trainees, the ratio of male to female trainees is 3 : 2. If 80% of males and 90% of females pass the shooting endurance test, what is the overall percentage of trainees who passed the test?",
        "600 మంది ట్రైనీలు గల పోలీస్ శిక్షణ అకాడమీ బ్యాచ్‌లో పురుష మరియు మహిళా ట్రైనీల నిష్పత్తి 3 : 2. పురుషులలో 80% మరియు మహిళలలో 90% మంది షూటింగ్ ఎండ్యూరెన్స్ పరీక్షలో ఉత్తీర్ణులైతే, మొత్తం బ్యాచ్‌లో ఉత్తీర్ణులైన వారి శాతం ఎంత?",
        ["82%", "84%", "85%", "86%"],
        ["82%", "84%", "85%", "86%"],
        1,
        "Males = 600 * (3/5) = 360, Females = 240. Passed males = 360 * 0.80 = 288. Passed females = 240 * 0.90 = 216. Total passed = 288 + 216 = 504. Overall % = (504 / 600) * 100 = 84%.",
        "పురుషులు = 360, మహిళలు = 240. ఉత్తీర్ణులైన పురుషులు = 288. మహిళలు = 216. మొత్తం ఉత్తీర్ణులు = 504. మొత్తం శాతం = (504 / 600) * 100 = 84%."
    ))

    return qs
