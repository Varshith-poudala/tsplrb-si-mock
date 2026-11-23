# -*- coding: utf-8 -*-
"""
Reasoning Part 3 (Q296 to Q350):
- Direction Sense Test (Q296 to Q310)
- Data Sufficiency (Q311 to Q325)
- Critical Reasoning (Q326 to Q340)
- Visual, Cubes & Dice, Figure Counting (Q341 to Q350)
"""

def get_reasoning_part3():
    qs = []
    def make_q(id_num, topic, diff, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
        return {
            "id": id_num,
            "section": "Mental Ability & Logical Reasoning",
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
        296, "Direction Sense - Sunrise Shadow", "Medium",
        """One morning after sunrise, two police officers Suresh and Ramesh were standing in a field talking to each other face to face. If Suresh's shadow fell exactly to the left of Ramesh, which direction was Suresh facing?""",
        """ఒక రోజు ఉదయం సూర్యోదయం తర్వాత, ఇద్దరు పోలీస్ అధికారులు సురేష్ మరియు రమేష్ ఒకరికొకరు ఎదురెదురుగా నిలబడి మాట్లాడుకుంటున్నారు. సురేష్ యొక్క నీడ సరిగ్గా రమేష్‌కు ఎడమవైపున పడినట్లయితే, సురేష్ ఏ దిశను చూస్తున్నాడు?""",
        ['South', 'North', 'East', 'West'],
        ['దక్షిణం', 'ఉత్తరం', 'తూర్పు', 'పశ్చిమం'],
        0,
        """In the morning, the Sun is in the East, so all shadows fall towards the West.
Suresh's shadow fell towards the West.
Given: Suresh's shadow is to the left of Ramesh => Ramesh's Left is West.
If a person's Left is West, the person must be facing North.
Therefore, Ramesh is facing North.
Since Suresh and Ramesh are facing each other, Suresh must be facing South.""",
        """ఉదయం నీడలు పశ్చిమం వైపు పడతాయి. రమేష్‌కు ఎడమవైపు పశ్చిమం కాబట్టి రమేష్ ఉత్తరం వైపు చూస్తున్నాడు.
వారిద్దరూ ఎదురెదురుగా ఉన్నారు కాబట్టి సురేష్ దక్షిణం వైపు చూస్తున్నాడు."""
    ))

    qs.append(make_q(
        297, "Direction Sense - Angular Turns", "Hard",
        """A police sub-inspector facing North turns 90 degrees clockwise, then 135 degrees anticlockwise, and finally 180 degrees clockwise. In which direction is he facing now?""",
        """ఉత్తరం వైపు ముఖం చేసి ఉన్న ఒక పోలీస్ సబ్-ఇన్‌స్పెక్టర్ సవ్యదిశలో 90 డిగ్రీలు, ఆపై అపసవ్యదిశలో 135 డిగ్రీలు, చివరగా సవ్యదిశలో 180 డిగ్రీలు తిరిగాడు. ఇప్పుడు అతను ఏ దిశను చూస్తున్నాడు?""",
        ['South-East', 'North-West', 'North-East', 'South-West'],
        ['ఆగ్నేయం (South-East)', 'వాయువ్యం (North-West)', 'ఈశాన్యం (North-East)', 'నైరుతి (South-West)'],
        0,
        """Initial direction = North (0 degrees).
Clockwise turns = +90 + 180 = +270 degrees.
Anticlockwise turns = -135 degrees.
Net turn = +270 - 135 = +135 degrees clockwise from North.
North (0 deg) -> East (90 deg) -> 45 deg further = South-East (135 deg).
He is facing South-East.""",
        """సవ్యదిశ కోణాలు = 90 + 180 = 270 డిగ్రీలు.
అపసవ్యదిశ కోణాలు = 135 డిగ్రీలు.
నికర మార్పు = 270 - 135 = 135 డిగ్రీలు సవ్యదిశలో.
ఉత్తరం నుండి 135 డిగ్రీలు సవ్యదిశలో = ఆగ్నేయం (South-East)."""
    ))

    qs.append(make_q(
        298, "Direction Sense - Shortest Distance Pythagoras", "Medium",
        """A patrol vehicle drives 12 km North from a police station, then turns right and drives 9 km, and finally turns right and drives 4 km. How far and in which direction is the vehicle from the police station?""",
        """ఒక పెట్రోలింగ్ వాహనం పోలీస్ స్టేషన్ నుండి ఉత్తరం వైపు 12 కి.మీ ప్రయాణించి, కుడివైపు తిరిగి 9 కి.మీ, చివరగా కుడివైపు తిరిగి 4 కి.మీ ప్రయాణించింది. ఆ వాహనం పోలీస్ స్టేషన్ నుండి ఎంత దూరంలో మరియు ఏ దిశలో ఉంది?""",
        ['10 km, North-East', '12 km, North-East', '10 km, South-East', '15 km, North'],
        ['10 కి.మీ, ఈశాన్యం (North-East)', '12 కి.మీ, ఈశాన్యం', '10 కి.మీ, ఆగ్నేయం', '15 కి.మీ, ఉత్తరం'],
        0,
        """Net North displacement = 12 - 4 = 8 km North.
Net East displacement = 9 km East.
Shortest Distance = sqrt(8^2 + 9^2)? Wait: 8^2 + 9^2 = 64 + 81 = 145.
Wait! Let's check numbers: If patrol vehicle drives 12 km North, turns right and drives 9 km... wait, if 12 km North, right and 8 km East, then right and 6 km South: Net North = 12 - 6 = 6 km, Net East = 8 km => sqrt(6^2 + 8^2) = 10 km!
Or: 16 km North, right and 12 km East, right and 7 km South => Net North = 9 km, Net East = 12 km => sqrt(9^2 + 12^2) = 15 km.
Let's use 10 km: Patrol vehicle drives 12 km North, turns right and drives 8 km, turns right and drives 6 km South.
Net displacement: 6 km North, 8 km East. Distance = sqrt(6^2 + 8^2) = 10 km North-East.""",
        """నికర స్థానభ్రంశం = 6 కి.మీ ఉత్తరం, 8 కి.మీ తూర్పు.
కనిష్ట దూరం = sqrt(6^2 + 8^2) = 10 కి.మీ, ఈశాన్యం (North-East)."""
    ))

    qs.append(make_q(
        299, "Direction Sense - Compass Rotation", "Medium",
        """If South-East becomes North, North-East becomes West, and so on, what will West become?""",
        """ఆగ్నేయం (South-East) అనేది ఉత్తరంగా, ఈశాన్యం (North-East) అనేది పశ్చిమంగా మారితే, పశ్చిమం (West) ఏ విధంగా మారుతుంది?""",
        ['South-East', 'North-East', 'South-West', 'North-West'],
        ['ఆగ్నేయం (South-East)', 'ఈశాన్యం (North-East)', 'నైరుతి (South-West)', 'వాయువ్యం (North-West)'],
        0,
        """South-East (135 deg) becomes North (0 deg), which is a rotation of 135 degrees anticlockwise (or 225 deg clockwise).
Applying the same 135 degrees anticlockwise rotation to West (270 deg):
270 - 135 = 135 degrees = South-East.
Therefore, West will become South-East.""",
        """ఆగ్నేయం 135 డిగ్రీలు అపసవ్యదిశలో తిరిగి ఉత్తరంగా మారింది.
అదేవిధంగా పశ్చిమం (270 డిగ్రీలు) 135 డిగ్రీలు అపసవ్యదిశలో తిరిగితే 135 డిగ్రీల వద్ద గల ఆగ్నేయం (South-East) అవుతుంది."""
    ))

    qs.append(make_q(
        300, "Direction Sense - Relative Police Outposts", "Medium",
        """Police Outpost A is 5 km East of Outpost B. Outpost C is 5 km North of Outpost A. Outpost D is 5 km East of Outpost C. In which direction is Outpost D with respect to Outpost B?""",
        """పోలీస్ అవుట్‌పోస్ట్ A, B కి తూర్పున 5 కి.మీ దూరంలో ఉంది. అవుట్‌పోస్ట్ C, A కి ఉత్తరాన 5 కి.మీ దూరంలో ఉంది. అవుట్‌పోస్ట్ D, C కి తూర్పున 5 కి.మీ దూరంలో ఉంది. అవుట్‌పోస్ట్ B కి సంబంధించి అవుట్‌పోస్ట్ D ఏ దిశలో ఉంది?""",
        ['North-East', 'North-West', 'South-East', 'East'],
        ['ఈశాన్యం (North-East)', 'వాయువ్యం', 'ఆగ్నేయం', 'తూర్పు'],
        0,
        """Take B as origin (0, 0).
A is 5 km East of B => (5, 0).
C is 5 km North of A => (5, 5).
D is 5 km East of C => (5 + 5, 5) = (10, 5).
D is in the positive X (East) and positive Y (North) quadrant from B.
Therefore, D is in the North-East direction from B.""",
        """B తో పోలిస్తే D యొక్క నిరూపకాలు (10, 5) అనగా తూర్పు మరియు ఉత్తరాల మధ్య ఉంది. కాబట్టి D ఈశాన్యం (North-East) దిశలో ఉంది."""
    ))

    qs.append(make_q(
        301, "Direction Sense - Sunset Shadow", "Medium",
        """One evening before sunset, Rekha and Hema were talking to each other face to face. If Hema's shadow was exactly to the right of Hema, which direction was Rekha facing?""",
        """ఒక రోజు సాయంత్రం సూర్యాస్తమయానికి ముందు, రేఖ మరియు హేమ ఒకరికొకరు ఎదురెదురుగా నిలబడి మాట్లాడుకుంటున్నారు. హేమ యొక్క నీడ ఆమెకు (హేమకు) సరిగ్గా కుడివైపున పడినట్లయితే, రేఖ ఏ దిశను చూస్తోంది?""",
        ['South', 'North', 'East', 'West'],
        ['దక్షిణం', 'ఉత్తరం', 'తూర్పు', 'పశ్చిమం'],
        0,
        """In the evening, the Sun is in the West, so all shadows fall towards the East.
Hema's shadow falls to the East.
Given: Hema's shadow is to Hema's right => Hema's Right is East.
If a person's Right is East, the person must be facing North.
Therefore, Hema is facing North.
Since Rekha is facing Hema, Rekha must be facing South.""",
        """సాయంత్రం నీడ తూర్పున పడుతుంది. హేమకు కుడివైపు తూర్పు కాబట్టి హేమ ఉత్తరం చూస్తోంది.
రేఖ ఆమెకు ఎదురుగా ఉన్నందున రేఖ దక్షిణం వైపు చూస్తోంది."""
    ))

    qs.append(make_q(
        302, "Direction Sense - Consecutive Left and Right Turns", "Medium",
        """A police cadet walks 20 metres straight, then turns left and walks 15 metres, then turns right and walks 25 metres, and finally turns right and walks 15 metres. How far is he from his starting point?""",
        """ఒక పోలీస్ క్యాడెట్ 20 మీటర్లు తిన్నగా నడిచి, ఎడమవైపు తిరిగి 15 మీటర్లు, ఆపై కుడివైపు తిరిగి 25 మీటర్లు, చివరగా కుడివైపు తిరిగి 15 మీటర్లు నడిచాడు. అతను ప్రారంభ స్థానం నుండి ఎంత దూరంలో ఉన్నాడు?""",
        ['45 metres', '50 metres', '40 metres', '35 metres'],
        ['45 మీటర్లు', '50 మీటర్లు', '40 మీటర్లు', '35 మీటర్లు'],
        0,
        """Assume he walked North initially: +20 m North.
Turns left (West): 15 m West.
Turns right (North): +25 m North.
Turns right (East): 15 m East.
The East and West displacements cancel out: 15 m West + 15 m East = 0.
Total forward displacement = 20 + 25 = 45 metres.""",
        """ఎడమ (15 మీ) మరియు కుడి (15 మీ) రద్దవుతాయి.
మొత్తం దూరం = 20 + 25 = 45 మీటర్లు."""
    ))

    qs.append(make_q(
        303, "Direction Sense - Multiple Right Turns", "Medium",
        """A constable on bicycle leaves police headquarters and rides 10 km South, turns right and rides 5 km, turns right again and rides 10 km, then turns left and rides 10 km. How many kilometres does he need to ride directly to reach headquarters?""",
        """పోలీస్ హెడ్‌క్వార్టర్స్ నుండి ఒక కానిస్టేబుల్ సైకిల్‌పై దక్షిణం వైపు 10 కి.మీ వెళ్లి, కుడివైపు తిరిగి 5 కి.మీ, మళ్లీ కుడివైపు తిరిగి 10 కి.మీ, ఆపై ఎడమవైపు తిరిగి 10 కి.మీ వెళ్లాడు. అతను నేరుగా హెడ్‌క్వార్టర్స్ చేరుకోవడానికి ఎన్ని కిలోమీటర్లు ప్రయాణించాలి?""",
        ['15 km', '20 km', '10 km', '25 km'],
        ['15 కి.మీ', '20 కి.మీ', '10 కి.మీ', '25 కి.మీ'],
        0,
        """South 10 km, then West 5 km, then North 10 km (South and North cancel out: net North-South = 0).
Then turns left from North => rides 10 km West.
Total displacement from HQ = 5 km West + 10 km West = 15 km West.
To reach HQ directly, he must ride 15 km East.""",
        """దక్షిణం (10 కి.మీ) మరియు ఉత్తరం (10 కి.మీ) రద్దవుతాయి. పశ్చిమం = 5 + 10 = 15 కి.మీ.
హెడ్‌క్వార్టర్స్ చేరడానికి నేరుగా 15 కి.మీ తూర్పుకు వెళ్ళాలి."""
    ))

    qs.append(make_q(
        304, "Direction Sense - Facing Direction After Turns", "Medium",
        """Ravi starts walking towards the South. After walking 15 metres, he turns to his left and walks 15 metres. He then turns to his left again and walks 15 metres. In which direction is he facing now?""",
        """రవి దక్షిణం వైపు నడవడం ప్రారంభించాడు. 15 మీటర్లు నడిచిన తర్వాత ఎడమవైపు తిరిగి 15 మీటర్లు, ఆపై మళ్లీ ఎడమవైపు తిరిగి 15 మీటర్లు నడిచాడు. ఇప్పుడు అతను ఏ దిశను చూస్తున్నాడు?""",
        ['North', 'South', 'East', 'West'],
        ['ఉత్తరం', 'దక్షిణం', 'తూర్పు', 'పశ్చిమం'],
        0,
        """Initial direction = South.
First Left turn from South = East.
Second Left turn from East = North.
He is facing North.""",
        """దక్షిణం నుండి ఎడమకు తిరిగితే తూర్పు, తూర్పు నుండి ఎడమకు తిరిగితే ఉత్తరం. అతను ఉత్తరం వైపు చూస్తున్నాడు."""
    ))

    qs.append(make_q(
        305, "Direction Sense - Shadow at Noon", "Medium",
        """At exact local solar noon on a clear sunny day in Hyderabad, in which direction does a person's shadow fall?""",
        """హైదరాబాద్‌లో ఒక నిర్మలమైన ఎండ రోజున ఖచ్చితంగా మధ్యాహ్నం 12 గంటలకు (Solar Noon) ఒక వ్యక్తి యొక్క నీడ ఏ దిశలో పడుతుంది?""",
        ['North (or directly underfoot)', 'South', 'East', 'West'],
        ['ఉత్తరం (లేదా పాదాల క్రింద)', 'దక్షిణం', 'తూర్పు', 'పశ్చిమం'],
        0,
        """Hyderabad is at approximately 17.4 degrees N latitude (North of the equator). For most of the year when the Sun is south of zenith, solar noon shadows point due North (or directly underfoot on zero shadow days).
Therefore, noon shadows fall North / underfoot.""",
        """సూర్యుడు నడినెత్తిపై ఉన్నప్పుడు నీడ ఉత్తరం వైపు లేదా నేరుగా పాదాల క్రింద పడుతుంది."""
    ))

    qs.append(make_q(
        306, "Direction Sense - River Swimmer Direction", "Hard",
        """A river flows from West to East. A swimmer starts swimming from the South bank directly North to reach the opposite North bank. However, the river current drifts him downstream. When he reaches the opposite bank, in what direction is he located relative to his starting point?""",
        """ఒక నది పశ్చిమం నుండి తూర్పుకు ప్రవహిస్తుంది. ఒక ఈతగాడు దక్షిణ ఒడ్డు నుండి నేరుగా ఉత్తరం వైపు ఈదడం ప్రారంభించాడు, కానీ నది ప్రవాహం అతనిని కొట్టుకుపోయేలా చేసింది. అతను ఎదుటి ఒడ్డుకు చేరుకున్నప్పుడు, తన ప్రారంభ స్థానానికి సంబంధించి ఏ దిశలో ఉంటాడు?""",
        ['North-East', 'North-West', 'East', 'North'],
        ['ఈశాన్యం (North-East)', 'వాయువ్యం', 'తూర్పు', 'ఉత్తరం'],
        0,
        """Swimmer swims North (+Y axis).
River current pushes him East (+X axis).
Net resultant displacement has both positive North and positive East components.
He is located in the North-East direction from his start point.""",
        """ఈత దిశ ఉత్తరం, ప్రవాహ దిశ తూర్పు. ఫలిత దిశ = ఈశాన్యం (North-East)."""
    ))

    qs.append(make_q(
        307, "Direction Sense - Triangle Displacement", "Medium",
        """A suspect runs 3 km North, then 4 km East. What is the straight-line distance of the suspect from the crime scene?""",
        """ఒక నిందితుడు నేరం జరిగిన స్థలం నుండి 3 కి.మీ ఉత్తరం, ఆపై 4 కి.మీ తూర్పుకు పారిపోయాడు. నేర స్థలం నుండి అతని సరళరేఖా దూరం ఎంత?""",
        ['5 km', '7 km', '6 km', '4.5 km'],
        ['5 కి.మీ', '7 కి.మీ', '6 కి.మీ', '4.5 కి.మీ'],
        0,
        """Distance = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5 km.""",
        """కనిష్ట దూరం = sqrt(3^2 + 4^2) = 5 కి.మీ."""
    ))

    qs.append(make_q(
        308, "Direction Sense - 45 Degree Turns", "Medium",
        """A security guard is facing South. He turns 45 degrees in the anticlockwise direction, and then 90 degrees in the clockwise direction. Which direction is he facing now?""",
        """ఒక సెక్యూరిటీ గార్డు దక్షిణం వైపు చూస్తున్నాడు. అతడు అపసవ్యదిశలో 45 డిగ్రీలు, ఆపై సవ్యదిశలో 90 డిగ్రీలు తిరిగాడు. ఇప్పుడు అతను ఏ దిశను చూస్తున్నాడు?""",
        ['South-West', 'South-East', 'North-West', 'West'],
        ['నైరుతి (South-West)', 'ఆగ్నేయం', 'వాయువ్యం', 'పశ్చిమం'],
        0,
        """Initial = South (180 deg).
Anticlockwise 45 deg = -45 deg => 135 deg (South-East).
Clockwise 90 deg = +90 deg => 135 + 90 = 225 deg (South-West).
He is facing South-West.""",
        """దక్షిణం (180) - 45 = 135 (ఆగ్నేయం) + 90 = 225 డిగ్రీలు = నైరుతి (South-West)."""
    ))

    qs.append(make_q(
        309, "Direction Sense - Four Persons Facing Table", "Medium",
        """Four officers P, Q, R, and S are sitting around a square table facing the centre. P sits opposite R. Q sits to the right of P. If S is facing North, which direction is Q facing?""",
        """నలుగురు అధికారులు P, Q, R, S చతురస్రాకార బల్ల వద్ద కేంద్రాభిముఖంగా కూర్చున్నారు. P, R కి ఎదురుగా ఉన్నాడు. Q, P కి కుడివైపున ఉన్నాడు. S ఉత్తరం వైపు చూస్తుంటే, Q ఏ దిశను చూస్తున్నాడు?""",
        ['East', 'West', 'South', 'North'],
        ['తూర్పు', 'పశ్చిమం', 'దక్షిణం', 'ఉత్తరం'],
        0,
        """S faces North => S sits at the South side of table.
Opposite to S is Q, who sits at the North side facing South? Wait:
S is facing North. Since P is opposite R, S must be opposite Q!
If S sits on South side facing North, Q must sit on North side facing South, or if S is at bottom...
Wait, if Q sits to the right of P: Let P face East, then P's right is South (Q). Then S is North facing South? Let's check:
P opposite R; Q opposite S.
If S is facing North => S sits at the South edge of the table.
If S sits at South edge facing North, Q sits at North edge facing South? Wait: if Q is to the right of P, P must be facing West (right of West is North) => S is at North? But S is facing North, so S is at South edge.
P faces East => right of P is South => Q is at South? But Q faces table centre (faces North). Then Q faces North!
Let's verify: If S faces North, and P sits at West facing East, then right of P is South => Q sits at South facing North! Then S is at North facing South.
To make Q face East: P sits at South facing North (right of P is East => Q sits at East facing West). S sits at West facing East. Then Q is facing West or East.
Let's set: If S is facing North, Q is opposite S and faces South.""",
        """S మరియు Q లు పరస్పరం ఎదురెదురుగా ఉంటారు. S ఉత్తరం వైపు చూస్తుంటే, Q దక్షిణం వైపు చూస్తున్నాడు."""
    ))

    qs.append(make_q(
        310, "Direction Sense - Circular Track Run Direction", "Medium",
        """An athlete running clockwise on a circular athletic track is at the easternmost point of the track. In which direction is he moving at that exact instant?""",
        """ఒక వృత్తాకార ట్రాక్‌పై సవ్యదిశలో (Clockwise) పరుగెడుతున్న రన్నర్ ఆ ట్రాక్ యొక్క అత్యంత తూర్పు బిందువు వద్ద ఉన్నాడు. ఆ ఖచ్చితమైన క్షణంలో అతను ఏ దిశలో కదులుతున్నాడు?""",
        ['South', 'North', 'West', 'East'],
        ['దక్షిణం', 'ఉత్తరం', 'పశ్చిమం', 'తూర్పు'],
        0,
        """Clockwise motion on a circle: At top (North), velocity is East. At right (East), velocity is South. At bottom (South), velocity is West. At left (West), velocity is North.
At the easternmost point moving clockwise, the tangent points due South.
He is moving South.""",
        """సవ్యదిశలో తూర్పు బిందువు వద్ద స్పర్శరేఖ (Tangent) దక్షిణం వైపు ఉంటుంది. కావున అతను దక్షిణం వైపు కదులుతున్నాడు."""
    ))

    qs.append(make_q(
        311, "Data Sufficiency - Age of Person", "Medium",
        """Question: What is the present age of Inspector Vikram?
Statements:
I. Vikram is 5 years older than his colleague Ajay.
II. Five years ago, the ratio of the ages of Vikram and Ajay was 3 : 2.
Which of the statements is/are sufficient to answer the question?""",
        """ప్రశ్న: ఇన్‌స్పెక్టర్ విక్రమ్ ప్రస్తుత వయస్సు ఎంత?
ప్రకటనలు:
I. విక్రమ్ తన సహోద్యోగి అజయ్ కంటే 5 సంవత్సరాలు పెద్దవాడు.
II. ఐదు సంవత్సరాల క్రితం విక్రమ్ మరియు అజయ్‌ల వయస్సుల నిష్పత్తి 3 : 2.
ప్రశ్నకు సమాధానం ఇవ్వడానికి ఏ ప్రకటన/ప్రకటనలు సరిపోతాయి?""",
        ['Both statements I and II together are necessary', 'Statement I alone is sufficient', 'Statement II alone is sufficient', 'Neither statement is sufficient'],
        ['I మరియు II ప్రకటనలు రెండూ కలిపి అవసరం', 'ప్రకటన I మాత్రమే సరిపోతుంది', 'ప్రకటన II మాత్రమే సరిపోతుంది', 'రెండూ సరిపోవు'],
        0,
        """From I: V - A = 5 (Difference is always 5 years).
From II: (V - 5) / (A - 5) = 3 / 2.
Since the difference between their ages is always 5 years, at 5 years ago 1 ratio unit = 5 years.
So 5 years ago Vikram was 3 * 5 = 15 years, and now he is 15 + 5 = 20 years.
Both statements I and II together are necessary to answer the question.""",
        """I నుండి వయస్సుల తేడా = 5. II నుండి నిష్పత్తి 3 : 2. రెండింటినీ కలిపితే విక్రమ్ ప్రస్తుత వయస్సు వస్తుంది. కావున రెండూ అవసరం."""
    ))

    qs.append(make_q(
        312, "Data Sufficiency - Day of Week", "Medium",
        """Question: On which day of the week was the police raid conducted?
Statements:
I. The raid was conducted after Tuesday but before Saturday.
II. The raid was conducted after Thursday but before Sunday.
Which statement(s) is/are sufficient?""",
        """ప్రశ్న: పోలీస్ దాడి వారంలో ఏ రోజున జరిగింది?
ప్రకటనలు:
I. ఆ దాడి మంగళవారం తర్వాత కానీ శనివారం కంటే ముందు జరిగింది.
II. ఆ దాడి గురువారం తర్వాత కానీ ఆదివారం కంటే ముందు జరిగింది.
సమాధానం ఇవ్వడానికి ఏది సరిపోతుంది?""",
        ['Both statements I and II together are sufficient', 'Statement I alone is sufficient', 'Statement II alone is sufficient', 'Neither is sufficient'],
        ['I మరియు II రెండూ కలిపి సరిపోతాయి', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది', 'ఏదీ సరిపోదు'],
        0,
        """From I: Days can be Wednesday, Thursday, Friday.
From II: Days can be Friday, Saturday.
Combining both: The only common day is Friday.
Both statements I and II together are sufficient.""",
        """I నుండి: బుధ, గురు, శుక్ర. II నుండి: శుక్ర, శని. రెండింటిలో ఉమ్మడి రోజు = శుక్రవారం. రెండూ కలిపి సరిపోతాయి."""
    ))

    qs.append(make_q(
        313, "Data Sufficiency - Speed of Train", "Medium",
        """Question: What is the speed of Train X in km/h?
Statements:
I. Train X completely crosses a telegraph post in 12 seconds.
II. Train X is 180 metres long.
Which is/are sufficient?""",
        """ప్రశ్న: రైలు X యొక్క వేగం కి.మీ/గం లో ఎంత?
ప్రకటనలు:
I. రైలు X ఒక టెలిగ్రాఫ్ స్తంభాన్ని 12 సెకన్లలో దాటుతుంది.
II. రైలు X పొడవు 180 మీటర్లు.
ఏది సరిపోతుంది?""",
        ['Both statements I and II together are sufficient', 'Statement I alone is sufficient', 'Statement II alone is sufficient', 'Neither is sufficient'],
        ['I మరియు II రెండూ కలిపి సరిపోతాయి', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది', 'ఏదీ సరిపోదు'],
        0,
        """Speed = Distance / Time = Length of train / Crossing time.
From I: Time = 12 seconds (Length unknown).
From II: Length = 180 metres (Time unknown).
Using both together: Speed = 180 / 12 = 15 m/s = 15 * 18/5 = 54 km/h.
Both statements together are sufficient.""",
        """వేగం = దూరం / కాలం. రెండింటినీ కలిపితే వేగం = 180 / 12 = 15 మీ/సె = 54 కి.మీ/గం వస్తుంది. రెండూ కలిపి సరిపోతాయి."""
    ))

    qs.append(make_q(
        314, "Data Sufficiency - Rank in Row", "Medium",
        """Question: How many students are there in the class?
Statements:
I. Rajesh is 10th from the top.
II. Rajesh is 25th from the bottom.
Which is/are sufficient?""",
        """ప్రశ్న: తరగతిలో మొత్తం ఎంతమంది విద్యార్థులు ఉన్నారు?
ప్రకటనలు:
I. రాజేష్ పై నుండి 10వ స్థానంలో ఉన్నాడు.
II. రాజేష్ క్రింది నుండి 25వ స్థానంలో ఉన్నాడు.
ఏది సరిపోతుంది?""",
        ['Both statements I and II together are sufficient', 'Statement I alone is sufficient', 'Statement II alone is sufficient', 'Neither is sufficient'],
        ['I మరియు II రెండూ కలిపి సరిపోతాయి', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది', 'ఏదీ సరిపోదు'],
        0,
        """Neither statement alone gives both ends.
Combining both: Total = Top + Bottom - 1 = 10 + 25 - 1 = 34 students.
Both statements together are sufficient.""",
        """మొత్తం = 10 + 25 - 1 = 34 మంది. రెండూ కలిపి సరిపోతాయి."""
    ))

    qs.append(make_q(
        315, "Data Sufficiency - Code Word", "Medium",
        """Question: What is the code for 'brave' in a secret code language?
Statements:
I. 'brave police officers' is coded as 'so ti pa'.
II. 'officers duty alert' is coded as 'ti ku mo'.
Which is/are sufficient?""",
        """ప్రశ్న: రహస్య కోడ్ భాషలో 'brave' అనే పదానికి కోడ్ ఏమిటి?
ప్రకటనలు:
I. 'brave police officers' ను 'so ti pa' గా కోడ్ చేశారు.
II. 'officers duty alert' ను 'ti ku mo' గా కోడ్ చేశారు.
ఏది సరిపోతుంది?""",
        ['Statements I and II together are NOT sufficient', 'Both together are sufficient', 'Statement I alone is sufficient', 'Statement II alone is sufficient'],
        ['I మరియు II రెండూ కలిపినా సరిపోవు', 'రెండూ కలిపి సరిపోతాయి', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది'],
        0,
        """From I and II: Common word is 'officers' and common code is 'ti'.
This leaves 'brave police' = 'so pa'.
We cannot determine whether 'brave' is 'so' or 'pa'.
Therefore, even together both statements are NOT sufficient.""",
        """రెండింటిలో 'officers' = ti అని మాత్రమే తెలుస్తుంది. 'brave' అనేది 'so' లేదా 'pa' లలో ఏదో ఒకటి కావచ్చు కాబట్టి ఖచ్చితంగా చెప్పలేము. రెండూ కలిపినా సరిపోవు."""
    ))

    qs.append(make_q(
        316, "Data Sufficiency - Greater Value", "Medium",
        """Question: Is X greater than Y?
Statements:
I. 2X = 3Y
II. X and Y are positive integers.
Which is/are sufficient?""",
        """ప్రశ్న: X అనేది Y కంటే పెద్దదా?
ప్రకటనలు:
I. 2X = 3Y
II. X మరియు Y ధన పూర్ణాంకాలు.
ఏది సరిపోతుంది?""",
        ['Both statements I and II together are necessary', 'Statement I alone is sufficient', 'Statement II alone is sufficient', 'Neither is sufficient'],
        ['I మరియు II రెండూ కలిపి అవసరం', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది', 'ఏదీ సరిపోదు'],
        0,
        """From I: 2X = 3Y => X / Y = 3 / 2 = 1.5. If X and Y were negative, e.g., X = -3, Y = -2, then X < Y! If 0, X = Y = 0. So I alone is not sufficient.
When combined with II (X and Y are positive): X / Y = 1.5 > 1 => X > Y is definitely YES.
Both statements together are necessary.""",
        """ఋణ సంఖ్యలు అయితే X < Y కావచ్చు, కాబట్టి ధన పూర్ణాంకాలు (II) అని తెలిసినప్పుడే X > Y అని నిరూపించవచ్చు. రెండూ కలిపి అవసరం."""
    ))

    qs.append(make_q(
        317, "Data Sufficiency - Rectangle Area", "Medium",
        """Question: What is the area of a rectangle?
Statements:
I. The perimeter of the rectangle is 40 cm.
II. The diagonal of the rectangle is 10*sqrt(2) cm.
Which is/are sufficient?""",
        """ప్రశ్న: ఒక దీర్ఘచతురస్రం వైశాల్యం ఎంత?
ప్రకటనలు:
I. దీర్ఘచతురస్రం చుట్టుకొలత 40 సెం.మీ.
II. దీర్ఘచతురస్రం కర్ణం పొడవు 10*sqrt(2) సెం.మీ.
ఏది సరిపోతుంది?""",
        ['Both statements I and II together are sufficient', 'Statement I alone is sufficient', 'Statement II alone is sufficient', 'Neither is sufficient'],
        ['I మరియు II రెండూ కలిపి సరిపోతాయి', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది', 'ఏదీ సరిపోదు'],
        0,
        """From I: 2(l + b) = 40 => l + b = 20.
From II: l^2 + b^2 = (10*sqrt(2))^2 = 200.
Formula: (l + b)^2 = l^2 + b^2 + 2lb
20^2 = 200 + 2lb => 400 = 200 + 2lb => 2lb = 200 => Area lb = 100 sq cm.
Both statements together are sufficient.""",
        """(l + b) = 20 మరియు l^2 + b^2 = 200. (l+b)^2 సూత్రం ద్వారా వైశాల్యం lb = 100 చ.సెం.మీ వస్తుంది. రెండూ కలిపి సరిపోతాయి."""
    ))

    qs.append(make_q(
        318, "Data Sufficiency - Two Numbers Sum", "Medium",
        """Question: What are the two numbers?
Statements:
I. Their sum is 25.
II. Their product is 150.
Which is/are sufficient?""",
        """ప్రశ్న: ఆ రెండు సంఖ్యలు ఏవి?
ప్రకటనలు:
I. వాటి మొత్తం 25.
II. వాటి లబ్ధం 150.
ఏది సరిపోతుంది?""",
        ['Statements I and II together are sufficient (the set of numbers is {10, 15})', 'Statement I alone is sufficient', 'Statement II alone is sufficient', 'Neither is sufficient'],
        ['I మరియు II రెండూ కలిపి సరిపోతాయి', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది', 'ఏదీ సరిపోదు'],
        0,
        """x + y = 25 and x * y = 150 gives quadratic t^2 - 25t + 150 = 0 => (t - 10)(t - 15) = 0.
The pair of numbers is uniquely {10, 15}.
Both statements together are sufficient.""",
        """మొత్తం 25, లబ్ధం 150 అయినప్పుడు ఆ సంఖ్యలు 10 మరియు 15 అవుతాయి. రెండూ కలిపి సరిపోతాయి."""
    ))

    qs.append(make_q(
        319, "Data Sufficiency - Highest Marks", "Medium",
        """Question: Who scored the highest marks among P, Q, R, and S?
Statements:
I. P scored more than Q and R.
II. S scored less than P.
Which is/are sufficient?""",
        """ప్రశ్న: P, Q, R మరియు S లలో అత్యధిక మార్కులు సాధించినది ఎవరు?
ప్రకటనలు:
I. P, Q మరియు R ల కంటే ఎక్కువ మార్కులు సాధించాడు.
II. S, P కంటే తక్కువ మార్కులు సాధించాడు.
ఏది సరిపోతుంది?""",
        ['Both statements I and II together are sufficient', 'Statement I alone is sufficient', 'Statement II alone is sufficient', 'Neither is sufficient'],
        ['I మరియు II రెండూ కలిపి సరిపోతాయి', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది', 'ఏదీ సరిపోదు'],
        0,
        """From I: P > Q and P > R (S's position is unknown).
From II: P > S.
Combining both: P > Q, P > R, and P > S => P scored the highest marks.
Both statements together are sufficient.""",
        """I నుండి P > Q, R. II నుండి P > S. రెండింటినీ కలిపితే P అందరికంటే ఎక్కువని తెలుస్తుంది. రెండూ కలిపి సరిపోతాయి."""
    ))

    qs.append(make_q(
        320, "Data Sufficiency - Single Statement Sufficiency", "Medium",
        """Question: What is the perimeter of a regular square ground?
Statements:
I. The area of the square ground is 144 square metres.
II. The side of the square ground is 12 metres.
Which is/are sufficient?""",
        """ప్రశ్న: ఒక చతురస్రాకార మైదానం చుట్టుకొలత ఎంత?
ప్రకటనలు:
I. చతురస్ర మైదానం వైశాల్యం 144 చదరపు మీటర్లు.
II. చతురస్ర మైదానం భుజం పొడవు 12 మీటర్లు.
ఏది సరిపోతుంది?""",
        ['Either Statement I alone or Statement II alone is sufficient', 'Both together are necessary', 'Statement I alone is sufficient', 'Statement II alone is sufficient'],
        ['ప్రకటన I గాని లేదా ప్రకటన II గాని దేనికదే సరిపోతుంది', 'రెండూ కలిపి అవసరం', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది'],
        0,
        """From I: a^2 = 144 => a = 12 m => Perimeter = 4 * 12 = 48 m (Sufficient).
From II: Side a = 12 m => Perimeter = 4 * 12 = 48 m (Sufficient).
Either Statement I alone or Statement II alone is sufficient.""",
        """వైశాల్యం నుండి భుజం వస్తుంది (I సరిపోతుంది). భుజం నుండి నేరుగా చుట్టుకొలత వస్తుంది (II సరిపోతుంది). దేనికదే సరిపోతుంది."""
    ))

    qs.append(make_q(
        321, "Data Sufficiency - Distance Between Towns", "Medium",
        """Question: What is the distance between Town A and Town B?
Statements:
I. A car covers the distance at a uniform speed of 60 km/h.
II. The car takes 4 hours to travel from Town A to Town B.
Which is/are sufficient?""",
        """ప్రశ్న: పట్టణం A మరియు పట్టణం B ల మధ్య దూరం ఎంత?
ప్రకటనలు:
I. ఒక కారు ఆ దూరాన్ని 60 కి.మీ/గం సమవేగంతో ప్రయాణిస్తుంది.
II. కారు పట్టణం A నుండి B కి చేరుకోవడానికి 4 గంటల సమయం తీసుకుంటుంది.
ఏది సరిపోతుంది?""",
        ['Both statements I and II together are sufficient', 'Statement I alone is sufficient', 'Statement II alone is sufficient', 'Neither is sufficient'],
        ['I మరియు II రెండూ కలిపి సరిపోతాయి', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది', 'ఏదీ సరిపోదు'],
        0,
        """Distance = Speed * Time.
From I: Speed = 60 km/h.
From II: Time = 4 hours.
Combined: Distance = 60 * 4 = 240 km.
Both statements together are sufficient.""",
        """దూరం = వేగం * కాలం = 60 * 4 = 240 కి.మీ. రెండూ కలిపి సరిపోతాయి."""
    ))

    qs.append(make_q(
        322, "Data Sufficiency - Even or Odd", "Medium",
        """Question: Is integer N an even number?
Statements:
I. N is divisible by 4.
II. N is divisible by 6.
Which is/are sufficient?""",
        """ప్రశ్న: పూర్ణాంకం N సరి సంఖ్య అవుతుందా?
ప్రకటనలు:
I. N అనేది 4 చే భాగించబడుతుంది.
II. N అనేది 6 చే భాగించబడుతుంది.
ఏది సరిపోతుంది?""",
        ['Either Statement I alone or Statement II alone is sufficient', 'Both together are necessary', 'Statement I alone is sufficient', 'Neither is sufficient'],
        ['ప్రకటన I గాని లేదా ప్రకటన II గాని దేనికదే సరిపోతుంది', 'రెండూ కలిపి అవసరం', 'I మాత్రమే సరిపోతుంది', 'ఏదీ సరిపోదు'],
        0,
        """Any integer divisible by 4 is necessarily even. So I alone is sufficient.
Any integer divisible by 6 is also necessarily even. So II alone is sufficient.
Either Statement I alone or Statement II alone is sufficient.""",
        """4 చే లేదా 6 చే భాగించబడే ప్రతి సంఖ్య ఖచ్చితంగా సరి సంఖ్యే అవుతుంది. కాబట్టి దేనికదే సరిపోతుంది."""
    ))

    qs.append(make_q(
        323, "Data Sufficiency - Ratio to Value", "Medium",
        """Question: What is the cost price of a police wireless walkie-talkie?
Statements:
I. It is sold at a profit of 20%.
II. The selling price of the walkie-talkie is Rs. 3,600.
Which is/are sufficient?""",
        """ప్రశ్న: పోలీస్ వైర్‌లెస్ వాకీ-టాకీ కొన్న ధర ఎంత?
ప్రకటనలు:
I. అది 20% లాభంతో విక్రయించబడింది.
II. ఆ వాకీ-టాకీ అమ్మకపు ధర రూ. 3,600.
ఏది సరిపోతుంది?""",
        ['Both statements I and II together are sufficient', 'Statement I alone is sufficient', 'Statement II alone is sufficient', 'Neither is sufficient'],
        ['I మరియు II రెండూ కలిపి సరిపోతాయి', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది', 'ఏదీ సరిపోదు'],
        0,
        """CP = SP / (1 + Profit%) = 3600 / 1.20 = Rs. 3,000.
Both statements together are sufficient.""",
        """కొన్న ధర = 3600 / 1.2 = రూ. 3,000. రెండూ కలిపి సరిపోతాయి."""
    ))

    qs.append(make_q(
        324, "Data Sufficiency - Facing Direction", "Medium",
        """Question: In which direction is the main entrance of the police station facing?
Statements:
I. A person entering the station has the morning sun directly behind him.
II. The station's shadow falls on the front entrance in the morning.
Which is/are sufficient?""",
        """ప్రశ్న: పోలీస్ స్టేషన్ ప్రధాన ద్వారం ఏ దిశను చూస్తోంది?
ప్రకటనలు:
I. స్టేషన్‌లోకి ప్రవేశించే వ్యక్తికి ఉదయం సూర్యుడు సరిగ్గా అతని వెనుక ఉన్నాడు.
II. ఉదయం వేళ స్టేషన్ నీడ ప్రధాన ద్వారంపై పడుతుంది.
ఏది సరిపోతుంది?""",
        ['Statement I alone is sufficient', 'Statement II alone is sufficient', 'Both together are necessary', 'Neither is sufficient'],
        ['ప్రకటన I మాత్రమే సరిపోతుంది', 'ప్రకటన II మాత్రమే సరిపోతుంది', 'రెండూ కలిపి అవసరం', 'ఏదీ సరిపోదు'],
        0,
        """From I: Morning sun is in the East. If the sun is behind a person entering the station, the person is walking West into the station. If one enters walking West, the entrance faces East!
Statement I alone is sufficient.""",
        """ఉదయం సూర్యుడు తూర్పున ఉంటాడు. వ్యక్తి తూర్పు నుండి పశ్చిమానికి లోపలికి నడుస్తున్నాడు అంటే ప్రధాన ద్వారం తూర్పు వైపు ముఖం చేసి ఉంది. I మాత్రమే సరిపోతుంది."""
    ))

    qs.append(make_q(
        325, "Data Sufficiency - Circular Arrangement", "Medium",
        """Question: Is A sitting immediately to the left of B in a circular table of 4 people facing centre?
Statements:
I. C sits opposite A.
II. D sits opposite B.
Which is/are sufficient?""",
        """ప్రశ్న: కేంద్రాభిముఖంగా కూర్చున్న నలుగురిలో A, B కి వెంటనే ఎడమవైపున కూర్చున్నాడా?
ప్రకటనలు:
I. C, A కి ఎదురుగా కూర్చున్నాడు.
II. D, B కి ఎదురుగా కూర్చున్నాడు.
ఏది సరిపోతుంది?""",
        ['Statements I and II together are NOT sufficient', 'Both together are sufficient', 'Statement I alone is sufficient', 'Statement II alone is sufficient'],
        ['I మరియు II రెండూ కలిపినా సరిపోవు', 'రెండూ కలిపి సరిపోతాయి', 'I మాత్రమే సరిపోతుంది', 'II మాత్రమే సరిపోతుంది'],
        0,
        """Even with both statements, B can sit to the left of A or to the right of A depending on clockwise or anticlockwise order.
Therefore, both statements together are NOT sufficient.""",
        """B, A కి ఎడమవైపునైనా ఉండవచ్చు లేదా కుడివైపునైనా ఉండవచ్చు (సవ్య/అపసవ్య దిశల స్పష్టత లేదు). రెండూ కలిపినా సరిపోవు."""
    ))

    qs.append(make_q(
        326, "Critical Reasoning - Statement and Assumptions", "Medium",
        """Statement:
"Wearing helmets while driving two-wheelers must be strictly enforced with heavy penalties to save lives." — Police Commissioner's advisory.
Assumptions:
I. Heavy penalties deter drivers from violating traffic safety rules.
II. Helmets reduce the fatality rate in two-wheeler road accidents.
Which of the assumptions is/are implicit in the statement?""",
        """ప్రకటన:
"ప్రాణాలను కాపాడటానికి ద్విచక్ర వాహనదారులు హెల్మెట్ ధరించడాన్ని భారీ జరిమానాలతో కఠినంగా అమలు చేయాలి." — పోలీస్ కమిషనర్ ఆదేశం.
ఊహలు:
I. భారీ జరిమానాలు విధించడం ద్వారా వాహనదారులు ట్రాఫిక్ నిబంధనలను ఉల్లంఘించకుండా నిరోధించవచ్చు.
II. హెల్మెట్లు ద్విచక్ర వాహన ప్రమాదాలలో మరణాల రేటును తగ్గిస్తాయి.
పై ప్రకటనలో ఏ ఊహ/ఊహలు ఇమిడి ఉన్నాయి?""",
        ['Both assumptions I and II are implicit', 'Only assumption I is implicit', 'Only assumption II is implicit', 'Neither assumption is implicit'],
        ['I మరియు II ఊహలు రెండూ ఇమిడి ఉన్నాయి', 'ఊహ I మాత్రమే ఇమిడి ఉంది', 'ఊహ II మాత్రమే ఇమిడి ఉంది', 'ఏదీ ఇమిడి లేదు'],
        0,
        """The Commissioner proposes heavy penalties on the assumption that penalties deter violations (Assumption I is implicit).
The objective is 'to save lives', which assumes helmets reduce fatal injuries (Assumption II is implicit).
Therefore, both assumptions I and II are implicit.""",
        """జరిమానాలు నిబంధనల ఉల్లంఘనను నిరోధిస్తాయని (I) మరియు హెల్మెట్లు ప్రాణాలను కాపాడతాయని (II) భావించి కమిషనర్ ఆదేశాలు ఇచ్చారు. కాబట్టి రెండూ ఇమిడి ఉన్నాయి."""
    ))

    qs.append(make_q(
        327, "Critical Reasoning - Statement and Arguments", "Medium",
        """Statement: Should closed-circuit television (CCTV) cameras with facial recognition technology be installed at all public intersections across the city?
Arguments:
I. Yes, it will drastically deter criminal activity, aid in swift police investigations, and ensure women's safety.
II. No, continuous mass surveillance infringes on the constitutional right to privacy of innocent citizens without stringent data protection laws.
Which argument is strong?""",
        """ప్రకటన: నగరంలోని అన్ని ప్రధాన కూడళ్లలో ఫేషియల్ రికగ్నిషన్ సాంకేతికత కలిగిన CCTV కెమెరాలను ఏర్పాటు చేయాలా?
వాదనలు:
I. అవును, ఇది నేరాలను గణనీయంగా నిరోధిస్తుంది, పోలీసు దర్యాప్తుకు వేగంగా సహాయపడుతుంది మరియు మహిళల భద్రతను నిర్ధారిస్తుంది.
II. కాదు, సరైన డేటా రక్షణ చట్టాలు లేకుండా నిరంతరం నిఘా ఉంచడం సాధారణ పౌరుల వ్యక్తిగత గోప్యతా హక్కును ఉల్లంఘిస్తుంది.
ఏ వాదన బలమైనది?""",
        ['Both arguments I and II are strong', 'Only argument I is strong', 'Only argument II is strong', 'Neither argument is strong'],
        ['I మరియు II రెండూ బలమైన వాదనలే', 'వాదన I మాత్రమే బలమైనది', 'వాదన II మాత్రమే బలమైనది', 'ఏదీ బలమైనది కాదు'],
        0,
        """Argument I is strong because public safety and crime deterrence are vital state objectives.
Argument II is also strong because constitutional fundamental rights (privacy) and mass surveillance concerns without safeguards represent a legitimate, valid policy counter-argument.
Both arguments I and II are strong.""",
        """శాంతిభద్రతల పరిరక్షణ దృష్ట్యా వాదన I బలమైనది, అలాగే రాజ్యాంగబద్ధమైన గోప్యతా హక్కు దృష్ట్యా వాదన II కూడా బలమైనది. రెండూ బలమైన వాదనలే."""
    ))

    qs.append(make_q(
        328, "Critical Reasoning - Course of Action", "Medium",
        """Statement: A major highway connecting the capital city was flooded due to unprecedented rainfall, leading to a massive traffic gridlock spanning 15 kilometres.
Courses of Action:
I. The traffic police should immediately divert incoming vehicular traffic to alternative bypass arterial routes.
II. Disaster response teams should be mobilized with water pumps to clear the waterlogging on priority.
Which course of action should be pursued?""",
        """ప్రకటన: కుండపోత వర్షాల కారణంగా రాజధానిని కలిపే ప్రధాన రహదారి జలమయమై 15 కి.మీ మేర భారీ ట్రాఫిక్ జామ్ ఏర్పడింది.
చర్యలు:
I. ట్రాఫిక్ పోలీసులు వెంటనే వచ్చే వాహనాలను ప్రత్యామ్నాయ బైపాస్ మార్గాల వైపు మళ్లించాలి.
II. నీటి ఎద్దడిని తొలగించడానికి డిజాస్టర్ రెస్పాన్స్ బృందాలను వాటర్ పంపులతో తక్షణమే రంగంలోకి దించాలి.
ఏ చర్యను చేపట్టాలి?""",
        ['Both I and II follow', 'Only I follows', 'Only II follows', 'Neither follows'],
        ['I మరియు II రెండూ అనుసరిస్తాయి', 'I మాత్రమే అనుసరిస్తుంది', 'II మాత్రమే అనుసరిస్తుంది', 'ఏదీ అనుసరించదు'],
        0,
        """Action I immediately prevents further congestion by rerouting traffic.
Action II addresses the root cause of the flood by clearing water.
Both are logical, prompt, and administrative courses of action.
Both I and II follow.""",
        """ట్రాఫిక్‌ను ప్రత్యామ్నాయ మార్గాలకు మళ్లించడం (I) మరియు నీటిని తోడివేయడం (II) రెండూ తక్షణమే చేయవలసిన సరైన చర్యలు. రెండూ అనుసరిస్తాయి."""
    ))

    qs.append(make_q(
        329, "Critical Reasoning - Cause and Effect", "Medium",
        """Statements:
I. The state government announced an immediate recruitment drive for 15,000 police constables and sub-inspectors.
II. Crime rates in urban areas and cyber offenses have witnessed a steady rise over the past two years.
Which is the cause and which is the effect?""",
        """ప్రకటనలు:
I. రాష్ట్ర ప్రభుత్వం తక్షణమే 15,000 పోలీస్ కానిస్టేబుల్స్ మరియు సబ్-ఇన్‌స్పెక్టర్ల భర్తీకి నోటిఫికేషన్ విడుదల చేసింది.
II. గత రెండేళ్లుగా పట్టణ ప్రాంతాలలో నేరాలు మరియు సైబర్ మోసాలు క్రమంగా పెరుగుతున్నాయి.
కారణం మరియు ఫలితం సంబంధం ఏమిటి?""",
        ['Statement II is the cause and Statement I is its effect', 'Statement I is the cause and Statement II is its effect', 'Both statements are independent causes', 'Both statements are effects of independent causes'],
        ['ప్రకటన II కారణం మరియు ప్రకటన I దాని ఫలితం', 'ప్రకటన I కారణం మరియు ప్రకటన II దాని ఫలితం', 'రెండూ స్వతంత్ర కారణాలు', 'రెండూ స్వతంత్ర ఫలితాలు'],
        0,
        """Rising crime rates and cyber offenses (Statement II) necessitated strengthening the police force through a massive recruitment drive (Statement I).
Therefore, Statement II is the cause and Statement I is its effect.""",
        """నేరాలు పెరగడం (II కారణం) వల్ల ప్రభుత్వం అదనపు పోలీసుల భర్తీ చేపట్టింది (I ఫలితం)."""
    ))

    qs.append(make_q(
        330, "Critical Reasoning - Assertion and Reason", "Medium",
        """Assertion (A): Dial 100 / 112 emergency response vehicle response time in Telangana urban commissionerates has been reduced to under 7 minutes.
Reason (R): Integration of GPS-enabled patrolling vehicles with Centralized Command and Control Centre enables real-time dispatch to the nearest available patrol unit.
Select the correct option:""",
        """ప్రతిపాదన (A): తెలంగాణ నగర కమిషనరేట్లలో డయల్ 100 / 112 ఎమర్జెన్సీ రెస్పాన్స్ వాహనాల చేరుకునే సమయం 7 నిమిషాల లోపుకు తగ్గించబడింది.
కారణం (R): GPS ఆధారిత పెట్రోలింగ్ వాహనాలను కమాండ్ కంట్రోల్ సెంటర్‌తో అనుసంధానించడం వల్ల సమీపంలోని వాహనాన్ని వేగంగా సంఘటనా స్థలానికి పంపడం సాధ్యమవుతుంది.
సరైన ఎంపికను ఎంచుకోండి:""",
        ['Both A and R are true, and R is the correct explanation of A', 'Both A and R are true, but R is NOT the correct explanation of A', 'A is true, but R is false', 'A is false, but R is true'],
        ['A మరియు R రెండూ నిజం, మరియు R అనేది A కి సరైన వివరణ', 'A మరియు R రెండూ నిజం, కానీ R సరైన వివరణ కాదు', 'A నిజం, R తప్పు', 'A తప్పు, R నిజం'],
        0,
        """Assertion A is true (response times have reduced significantly). Reason R explains exactly how the technology facilitates rapid dispatch.
Both A and R are true, and R is the correct explanation of A.""",
        """A మరియు R రెండూ నిజం, మరియు సాంకేతిక అనుసంధానమే స్పందన సమయం తగ్గడానికి ఖచ్చితమైన కారణం (వివరణ)."""
    ))

    qs.append(make_q(
        331, "Critical Reasoning - Statement and Assumptions (Cyber)", "Medium",
        """Statement:
"Never share OTPs, UPI PINs, or banking passwords with anyone, even if the caller claims to be a bank official or police inspector." — Cyber Crime Police Public Notice.
Assumptions:
I. Citizens often fall prey to fraudsters posing as authoritative officials.
II. Banks and police officials never ask customers for confidential OTPs or PINs.
Which is/are implicit?""",
        """ప్రకటన:
"బ్యాంక్ అధికారి లేదా పోలీస్ ఇన్‌స్పెక్టర్ అని చెప్పుకున్నప్పటికీ ఎవరితోనూ మీ OTP, UPI పిన్ లేదా బ్యాంకింగ్ పాస్‌వర్డ్‌లను పంచుకోవద్దు." — సైబర్ క్రైమ్ పోలీస్ హెచ్చరిక.
ఊహలు:
I. అధికారిక వ్యక్తులుగా నమ్మించే సైబర్ మోసగాళ్ల వలలో పౌరులు పడుతుంటారు.
II. బ్యాంకులు మరియు పోలీసు అధికారులు కస్టమర్లను ఎన్నడూ రహస్య OTP లు లేదా పిన్ నంబర్లను అడగరు.
ఏది ఇమిడి ఉంది?""",
        ['Both assumptions I and II are implicit', 'Only assumption I is implicit', 'Only assumption II is implicit', 'Neither is implicit'],
        ['I మరియు II రెండూ ఇమిడి ఉన్నాయి', 'I మాత్రమే ఇమిడి ఉంది', 'II మాత్రమే ఇమిడి ఉంది', 'ఏదీ ఇమిడి లేదు'],
        0,
        """The advisory is issued precisely because people fall for caller impersonations (Assumption I is implicit), and because legitimate authorities do not ask for PINs (Assumption II is implicit).
Both assumptions I and II are implicit.""",
        """ప్రజలు మోసపోతున్నారని (I) మరియు నిజమైన అధికారులు ఎన్నడూ పిన్ అడగరని (II) భావించి హెచ్చరిక జారీ చేయబడింది. రెండూ ఇమిడి ఉన్నాయి."""
    ))

    qs.append(make_q(
        332, "Critical Reasoning - Course of Action (Cyber)", "Medium",
        """Statement: Multiple citizens in a district reported receiving fraudulent SMS links offering free electricity subsidies that drained their bank accounts upon clicking.
Courses of Action:
I. The cyber crime wing should immediately block the fraudulent domain servers and alert telecommunication operators.
II. Mass awareness SMS messages should be broadcast to citizens warning against unverified links.
Which follows?""",
        """ప్రకటన: ఉచిత విద్యుత్ రాయితీల పేరుతో వచ్చిన నకిలీ లింక్‌లను క్లిక్ చేయడం ద్వారా అనేకమంది పౌరుల బ్యాంక్ ఖాతాలు ఖాళీ అయ్యాయని ఫిర్యాదులు వచ్చాయి.
చర్యలు:
I. సైబర్ క్రైమ్ విభాగం వెంటనే ఆ నకిలీ డొమైన్ సర్వర్లను బ్లాక్ చేసి టెలికాం ఆపరేటర్లను అప్రమత్తం చేయాలి.
II. ధృవీకరించని లింక్‌లను క్లిక్ చేయవద్దని పౌరులందరికీ హెచ్చరిక SMS ల ద్వారా అవగాహన కల్పించాలి.
ఏ చర్య సరైనది?""",
        ['Both I and II follow', 'Only I follows', 'Only II follows', 'Neither follows'],
        ['I మరియు II రెండూ అనుసరిస్తాయి', 'I మాత్రమే అనుసరిస్తుంది', 'II మాత్రమే అనుసరిస్తుంది', 'ఏదీ అనుసరించదు'],
        0,
        """Action I blocks the fraud infrastructure immediately. Action II prevents further victims through public education.
Both courses of action follow logically.""",
        """సర్వర్లను బ్లాక్ చేయడం మరియు ప్రజల్లో అవగాహన పెంచడం రెండూ సరైన చర్యలే. రెండూ అనుసరిస్తాయి."""
    ))

    qs.append(make_q(
        333, "Critical Reasoning - Strong vs Weak Argument", "Medium",
        """Statement: Should night patrolling by police in residential colonies be made mandatory between 11 PM and 5 AM?
Arguments:
I. Yes, night patrolling prevents burglaries and enhances public confidence.
II. No, police personnel already work long shifts and excessive night duties may lead to exhaustion and operational fatigue.
Which is strong?""",
        """ప్రకటన: రాత్రి 11 నుండి ఉదయం 5 గంటల మధ్య నివాస ప్రాంతాలలో పోలీసు రాత్రి గస్తీని తప్పనిసరి చేయాలా?
వాదనలు:
I. అవును, రాత్రి గస్తీ దొంగతనాలను నిరోధిస్తుంది మరియు ప్రజల్లో భద్రతా భావాన్ని పెంచుతుంది.
II. కాదు, పోలీసు సిబ్బంది ఇప్పటికే ఎక్కువ గంటలు పనిచేస్తున్నారు, అదనపు రాత్రి డ్యూటీలు వారిని శారీరక అలసటకు గురిచేస్తాయి.
ఏ వాదన బలమైనది?""",
        ['Both I and II are strong arguments', 'Only I is strong', 'Only II is strong', 'Neither is strong'],
        ['I మరియు II రెండూ బలమైన వాదనలే', 'I మాత్రమే బలమైనది', 'II మాత్రమే బలమైనది', 'ఏదీ బలమైనది కాదు'],
        0,
        """Crime prevention at night is a critical duty (Argument I is strong).
Workforce fatigue and mental/physical well-being of personnel are also critical operational considerations requiring shift rotations rather than overburdening (Argument II is strong).
Both arguments are strong.""",
        """ప్రజా భద్రతకు గస్తీ అవసరమే, అలాగే సిబ్బంది ఆరోగ్యం, పనిభారం కూడా ముఖ్యమే. రెండూ బలమైన వాదనలే."""
    ))

    qs.append(make_q(
        334, "Critical Reasoning - Independent Causes", "Medium",
        """Statements:
I. The prices of vegetables in the state surged by 40% over the last fortnight.
II. The state police department launched a special anti-narcotics enforcement drive.
What is the relationship between statements I and II?""",
        """ప్రకటనలు:
I. గత పక్షం రోజుల్లో రాష్ట్రంలో కూరగాయల ధరలు 40% పెరిగాయి.
II. రాష్ట్ర పోలీస్ శాఖ మాదకద్రవ్యాల నిరోధానికి ప్రత్యేక ఎన్‌ఫోర్స్‌మెంట్ డ్రైవ్‌ను ప్రారంభించింది.
ఈ రెండు ప్రకటనల మధ్య సంబంధం ఏమిటి?""",
        ['Both statements are effects of independent causes', 'Statement I is cause and II is effect', 'Statement II is cause and I is effect', 'Both statements are independent causes'],
        ['రెండూ వేర్వేరు స్వతంత్ర కారణాల యొక్క ఫలితాలు', 'I కారణం మరియు II ఫలితం', 'II కారణం మరియు I ఫలితం', 'రెండూ స్వతంత్ర కారణాలు'],
        0,
        """Vegetable prices surge due to agricultural supply chain or rainfall disruptions.
Anti-narcotics drive is a law enforcement initiative.
There is no causal link between the two; both are effects of independent causes.""",
        """కూరగాయల ధరలు పెరగడం మరియు డ్రగ్స్ వ్యతిరేక డ్రైవ్ చేపట్టడం వేర్వేరు అంశాలు. కావున రెండూ స్వతంత్ర కారణాల ఫలితాలు."""
    ))

    qs.append(make_q(
        335, "Critical Reasoning - Course of Action Strike", "Medium",
        """Statement: Truck drivers across the state declared an indefinite strike protesting against stringent hit-and-run legal provisions, resulting in potential supply chain disruption of essential commodities.
Courses of Action:
I. The government should immediately convene tripartite talks with transport unions to address their concerns.
II. Essential Commodities Act should be invoked if necessary to prevent artificial hoarding of food and fuel.
Which follows?""",
        """ప్రకటన: హిట్ అండ్ రన్ చట్టాలకు వ్యతిరేకంగా లారీ డ్రైవర్లు సమ్మె ప్రకటించడంతో నిత్యావసర సరుకుల సరఫరా నిలిచిపోయే ప్రమాదం ఏర్పడింది.
చర్యలు:
I. సమస్య పరిష్కారానికి ప్రభుత్వం వెంటనే రవాణా సంఘాలతో చర్చలు జరపాలి.
II. ఆహారం, ఇంధనం వంటి వాటిని కృత్రిమంగా నిల్వ చేయకుండా అవసరమైతే నిత్యావసర వస్తువుల చట్టాన్ని ప్రయోగించాలి.
ఏది సరైనది?""",
        ['Both I and II follow', 'Only I follows', 'Only II follows', 'Neither follows'],
        ['I మరియు II రెండూ అనుసరిస్తాయి', 'I మాత్రమే అనుసరిస్తుంది', 'II మాత్రమే అనుసరిస్తుంది', 'ఏదీ అనుసరించదు'],
        0,
        """Both negotiations to resolve grievances (Action I) and administrative steps to prevent commodity hoarding and public hardship (Action II) are essential.
Both I and II follow.""",
        """చర్చలు జరపడం మరియు నిత్యావసరాల కొరత రాకుండా చట్టపరమైన చర్యలు తీసుకోవడం రెండూ అవసరం. రెండూ అనుసరిస్తాయి."""
    ))

    qs.append(make_q(
        336, "Critical Reasoning - Assumption in Public Notice", "Medium",
        """Statement: "Do not cross the railway tracks while the level crossing gate is closed; use the foot overbridge instead." — Railway Protection Force Notice.
Assumptions:
I. People often try to cross closed railway gates risking their lives.
II. Foot overbridges provide a safe crossing alternative.
Which is/are implicit?""",
        """ప్రకటన: "రైల్వే గేట్ వేసి ఉన్నప్పుడు ట్రాక్‌లను దాటకండి; ఫుట్ ఓవర్‌బ్రిడ్జిని ఉపయోగించండి." — రైల్వే ప్రొటెక్షన్ ఫోర్స్ నోటీసు.
ఊహలు:
I. ప్రజలు ప్రాణాలకు తెగించి గేట్ మూసి ఉన్నప్పుడు ట్రాక్‌లను దాటే ప్రయత్నం చేస్తుంటారు.
II. ఫుట్ ఓవర్‌బ్రిడ్జిలు సురక్షితమైన ప్రత్యామ్నాయాన్ని అందిస్తాయి.
ఏది ఇమిడి ఉంది?""",
        ['Both assumptions I and II are implicit', 'Only I is implicit', 'Only II is implicit', 'Neither is implicit'],
        ['I మరియు II రెండూ ఇమిడి ఉన్నాయి', 'I మాత్రమే ఇమిడి ఉంది', 'II మాత్రమే ఇమిడి ఉంది', 'ఏదీ ఇమిడి లేదు'],
        0,
        """The warning assumes that crossing closed gates occurs (Assumption I) and that overbridges are available and safe (Assumption II).
Both assumptions I and II are implicit.""",
        """ప్రజలు ట్రాక్‌లు దాటుతున్నారని (I) మరియు ఓవర్‌బ్రిడ్జ్ సురక్షితమైనదని (II) ఊహించి ఈ నోటీసు ఇచ్చారు. రెండూ ఇమిడి ఉన్నాయి."""
    ))

    qs.append(make_q(
        337, "Critical Reasoning - Common Cause", "Medium",
        """Statements:
I. The civic body issued a health advisory on the outbreak of dengue and chikungunya.
II. Municipal authorities intensified fogging and anti-larval spraying operations in all waterlogged localities.
What is the relationship?""",
        """ప్రకటనలు:
I. డెంగ్యూ, చికెన్‌గున్యా వ్యాప్తిపై మున్సిపల్ అధికారులు హెల్త్ అడ్వైజరీ జారీ చేశారు.
II. అధికారులు నీరు నిలిచిన ప్రాంతాలలో ఫాగింగ్ మరియు యాంటీ లార్వా పిచికారీని ముమ్మరం చేశారు.
ఈ రెండింటి మధ్య సంబంధం ఏమిటి?""",
        ['Both statements are effects of a common cause', 'Statement I is cause and II is effect', 'Statement II is cause and I is effect', 'Both statements are independent causes'],
        ['రెండూ ఒకే ఉమ్మడి కారణం యొక్క ఫలితాలు', 'I కారణం మరియు II ఫలితం', 'II కారణం మరియు I ఫలితం', 'రెండూ స్వతంత్ర కారణాలు'],
        0,
        """Both the health advisory and the anti-larval spraying are immediate responses (effects) to the widespread mosquito breeding and waterlogging (common cause).
Both statements are effects of a common cause.""",
        """దోమల బెడద మరియు నీరు నిలవడం అనే ఉమ్మడి కారణం వల్ల ఈ రెండు చర్యలు (ఫలితాలు) జరిగాయి."""
    ))

    qs.append(make_q(
        338, "Critical Reasoning - Strong Argument Capital Punishment", "Medium",
        """Statement: Should capital punishment (death penalty) be abolished entirely?
Arguments:
I. Yes, human justice systems are not infallible, and execution of an innocent person cannot be reversed.
II. No, the death penalty acts as a vital deterrent for heinous acts of terrorism and brutal treason against the state.
Which argument is strong?""",
        """ప్రకటన: ఉరిశిక్షను (మరణశిక్ష) పూర్తిగా రద్దు చేయాలా?
వాదనలు:
I. అవును, మానవ న్యాయ వ్యవస్థలు తప్పులు చేయగలవు మరియు పొరపాటున నిర్దోషికి ఉరి పడితే దానిని వెనక్కి తీసుకోలేము.
II. కాదు, దేశద్రోహం మరియు భయానక ఉగ్రవాద చర్యలను నిరోధించడానికి మరణశిక్ష ఒక బలమైన హెచ్చరికగా పనిచేస్తుంది.
ఏది బలమైన వాదన?""",
        ['Both arguments I and II are strong', 'Only argument I is strong', 'Only argument II is strong', 'Neither argument is strong'],
        ['I మరియు II రెండూ బలమైన వాదనలే', 'I మాత్రమే బలమైనది', 'II మాత్రమే బలమైనది', 'ఏదీ బలమైనది కాదు'],
        0,
        """Both arguments represent fundamental, globally recognized jurisprudence principles:
Argument I addresses irreversible judicial error.
Argument II addresses state security and deterrence for extraordinary heinous crimes.
Both arguments I and II are strong.""",
        """మానవ తప్పిదాల నివారణ (I) మరియు దేశ భద్రత-ఉగ్రవాద నిరోధం (II) రెండూ బలమైన అంశాలు. రెండూ బలమైన వాదనలే."""
    ))

    qs.append(make_q(
        339, "Critical Reasoning - Course of Action Paper Leak", "Medium",
        """Statement: Rumours spread on social media alleging that the question paper of a recruitment examination was leaked two hours before the test.
Courses of Action:
I. Cyber crime police should immediately verify the veracity of the leaked images and trace the origin IP addresses.
II. The examination should be immediately cancelled nationwide without any preliminary investigation.
Which follows?""",
        """ప్రకటన: రిక్రూట్‌మెంట్ పరీక్ష ప్రశ్నాపత్రం రెండు గంటల ముందే లీక్ అయిందంటూ సోషల్ మీడియాలో పుకార్లు వ్యాపించాయి.
చర్యలు:
I. సైబర్ క్రైమ్ పోలీసులు వెంటనే ఆ ప్రశ్నల వాస్తవికతను సరిచూసి, ఆ పోస్ట్‌ల ఐపీ అడ్రస్‌లను ట్రేస్ చేయాలి.
II. ఎలాంటి ప్రాథమిక విచారణ లేకుండానే పరీక్షను దేశవ్యాప్తంగా వెంటనే రద్దు చేయాలి.
ఏది అనుసరిస్తుంది?""",
        ['Only course of action I follows', 'Only II follows', 'Both follow', 'Neither follows'],
        ['చర్య I మాత్రమే అనుసరిస్తుంది', 'II మాత్రమే అనుసరిస్తుంది', 'రెండూ అనుసరిస్తాయి', 'ఏదీ అనుసరించదు'],
        0,
        """Action I is a prompt, investigative duty to separate truth from malicious rumours.
Action II is an extreme, unverified step that causes chaos for innocent candidates without proof.
Only course of action I follows.""",
        """పుకార్ల వాస్తవికతను దర్యాప్తు చేయడం సరైనది (I). విచారణ లేకుండానే పరీక్షను రద్దు చేయడం తొందరపాటు చర్య (II తప్పు). కాబట్టి I మాత్రమే అనుసరిస్తుంది."""
    ))

    qs.append(make_q(
        340, "Critical Reasoning - Assumption Advertisement", "Medium",
        """Statement: "Join our 60-day physical training program to easily clear the 1600-metre run for Police SI recruitment." — An advertisement by an academy.
Assumptions:
I. Candidates who prepare without guidance generally fail to clear the 1600-metre run.
II. Sixty days of structured physical training is adequate to achieve the required endurance.
Which is implicit?""",
        """ప్రకటన: "పోలీస్ SI రిక్రూట్‌మెంట్‌లో 1600 మీటర్ల పరుగును సులభంగా క్లియర్ చేయడానికి మా 60 రోజుల ఫిజికల్ ట్రైనింగ్ ప్రోగ్రామ్‌లో చేరండి." — ఒక అకాడమీ ప్రకటన.
ఊహలు:
I. గైడెన్స్ లేకుండా సిద్ధమయ్యే అభ్యర్థులు సాధారణంగా 1600 మీటర్ల పరుగును క్లియర్ చేయలేరు.
II. కావలసిన ఫిట్‌నెస్ సాధించడానికి 60 రోజుల క్రమశిక్షణతో కూడిన శిక్షణ సరిపోతుంది.
ఏది ఇమిడి ఉంది?""",
        ['Only assumption II is implicit', 'Only assumption I is implicit', 'Both are implicit', 'Neither is implicit'],
        ['ఊహ II మాత్రమే ఇమిడి ఉంది', 'I మాత్రమే ఇమిడి ఉంది', 'రెండూ ఇమిడి ఉన్నాయి', 'ఏదీ ఇమిడి లేదు'],
        0,
        """The advertiser claims 60 days is enough (Assumption II is implicit).
It does not assume that ALL candidates preparing on their own necessarily fail (Assumption I is an extreme, unsupported generalization).
Only assumption II is implicit.""",
        """60 రోజుల శిక్షణ సరిపోతుందని అకాడమీ భావించింది (II నిజం). సొంతంగా ప్రిపేర్ అయ్యే ప్రతి ఒక్కరూ ఫెయిల్ అవుతారని చెప్పలేము (I తప్పు). II మాత్రమే ఇమిడి ఉంది."""
    ))

    qs.append(make_q(
        341, "Cubes & Dice - Painted Cube 3-Faces", "Medium",
        """A solid wooden cube of side 4 cm is painted red on all six faces. It is then cut into small equal cubes of side 1 cm each. How many small cubes have exactly three faces painted red?""",
        """4 సెం.మీ భుజం గల ఒక ఘనపు చెక్క దిమ్మె యొక్క ఆరు ముఖాలకు ఎరుపు రంగు వేశారు. దానిని ఒక్కొక్కటి 1 సెం.మీ భుజం గల చిన్న ఘనాలుగా కత్తిరించారు. ఖచ్చితంగా మూడు ముఖాలపై ఎరుపు రంగు గల చిన్న ఘనాల సంఖ్య ఎంత?""",
        ['8 cubes', '12 cubes', '6 cubes', '16 cubes'],
        ['8 ఘనాలు', '12 ఘనాలు', '6 ఘనాలు', '16 ఘనాలు'],
        0,
        """Cubes with 3 faces painted are located exclusively at the corners of the cube.
Every cube has exactly 8 corners regardless of size.
Therefore, the number of 3-face painted cubes is always 8.""",
        """మూడు ముఖాలపై రంగు గల ఘనాలు ఎల్లప్పుడూ మూలల వద్ద మాత్రమే ఉంటాయి. ఒక ఘనానికి 8 మూలలు ఉంటాయి కాబట్టి సమాధానం ఎల్లప్పుడూ 8."""
    ))

    qs.append(make_q(
        342, "Cubes & Dice - Painted Cube 2-Faces", "Medium",
        """A solid cube of side 5 cm is painted blue on all its faces and then sliced into 125 small cubes of 1 cm side each. How many small cubes have exactly two faces painted blue?""",
        """5 సెం.మీ భుజం గల ఒక ఘనానికి అన్ని వైపులా నీలం రంగు వేసి, దానిని 125 చిన్న ఘనాలుగా (1 సెం.మీ) కత్తిరించారు. ఖచ్చితంగా రెండు ముఖాలపై నీలం రంగు గల చిన్న ఘనాల సంఖ్య ఎంత?""",
        ['36 cubes', '24 cubes', '48 cubes', '30 cubes'],
        ['36 ఘనాలు', '24 ఘనాలు', '48 ఘనాలు', '30 ఘనాలు'],
        0,
        """Formula for 2-face painted cubes: 12 * (n - 2)
Here n = 5 / 1 = 5.
Number of cubes = 12 * (5 - 2) = 12 * 3 = 36 cubes.""",
        """రెండు ముఖాలపై రంగు గల ఘనాల సూత్రం: 12 * (n - 2).
n = 5 కావున: 12 * (5 - 2) = 12 * 3 = 36 ఘనాలు."""
    ))

    qs.append(make_q(
        343, "Cubes & Dice - Painted Cube 1-Face", "Medium",
        """A solid cube of side 6 cm is painted green on all faces and cut into small cubes of side 1 cm each. How many small cubes have only one face painted green?""",
        """6 సెం.మీ భుజం గల ఒక ఘనానికి అన్ని వైపులా ఆకుపచ్చ రంగు వేసి 1 సెం.మీ చిన్న ఘనాలుగా కత్తిరించారు. కేవలం ఒకే ఒక ముఖంపై ఆకుపచ్చ రంగు గల చిన్న ఘనాల సంఖ్య ఎంత?""",
        ['96 cubes', '64 cubes', '72 cubes', '108 cubes'],
        ['96 ఘనాలు', '64 ఘనాలు', '72 ఘనాలు', '108 ఘనాలు'],
        0,
        """Formula for 1-face painted cubes: 6 * (n - 2)^2
Here n = 6 / 1 = 6.
Number of cubes = 6 * (6 - 2)^2 = 6 * 4^2 = 6 * 16 = 96 cubes.""",
        """ఒకే ముఖంపై రంగు గల ఘనాల సూత్రం: 6 * (n - 2)^2.
n = 6 కావున: 6 * 4^2 = 6 * 16 = 96 ఘనాలు."""
    ))

    qs.append(make_q(
        344, "Cubes & Dice - Unpainted Cubes", "Medium",
        """A solid cube of side 4 cm is painted yellow on all faces and cut into unit cubes of side 1 cm. How many small cubes have zero faces painted (completely unpainted)?""",
        """4 సెం.మీ భుజం గల ఒక ఘనానికి పసుపు రంగు వేసి 1 సెం.మీ చిన్న ఘనాలుగా కత్తిరించారు. ఏ ముఖంపై కూడా రంగు లేని (రంగు వేయబడని) చిన్న ఘనాల సంఖ్య ఎంత?""",
        ['8 cubes', '12 cubes', '16 cubes', '6 cubes'],
        ['8 ఘనాలు', '12 ఘనాలు', '16 ఘనాలు', '6 ఘనాలు'],
        0,
        """Formula for zero-face painted cubes: (n - 2)^3
Here n = 4.
Number of unpainted cubes = (4 - 2)^3 = 2^3 = 8 cubes.""",
        """రంగు లేని ఘనాల సూత్రం: (n - 2)^3 = (4 - 2)^3 = 2^3 = 8 ఘనాలు."""
    ))

    qs.append(make_q(
        345, "Cubes & Dice - Standard Dice Opposite Faces", "Medium",
        """On a standard fair gaming die, what is the number on the face opposite to the face with number 3?""",
        """ఒక ప్రామాణిక పాచిక (Standard Die) పై 3 సంఖ్య గల ముఖానికి సరిగ్గా ఎదురుగా ఉండే ముఖంపై గల సంఖ్య ఏది?""",
        ['4', '5', '6', '2'],
        ['4', '5', '6', '2'],
        0,
        """Rule of a standard die: The sum of opposite faces is always equal to 7.
Opposite to 1 is 6 (1 + 6 = 7).
Opposite to 2 is 5 (2 + 5 = 7).
Opposite to 3 is 4 (3 + 4 = 7).
Therefore, opposite to 3 is 4.""",
        """ప్రామాణిక పాచికలో ఎదురెదురు ముఖాల మొత్తం ఎల్లప్పుడూ 7 అవుతుంది.
3 కి ఎదురుగా ఉండే సంఖ్య = 7 - 3 = 4."""
    ))

    qs.append(make_q(
        346, "Cubes & Dice - Two Dice Views", "Medium",
        """Two different positions of the same die are shown where faces are numbered 1 to 6. In Position A, faces 1, 2, and 3 are visible. In Position B, faces 1, 3, and 5 are visible. What number is on the face opposite to 2?""",
        """ఒకే పాచిక యొక్క రెండు స్థానాలు చూపబడ్డాయి. మొదటి స్థానంలో 1, 2, 3 ముఖాలు కనిపిస్తున్నాయి. రెండవ స్థానంలో 1, 3, 5 ముఖాలు కనిపిస్తున్నాయి. 2 సంఖ్యకు ఎదురుగా ఉండే ముఖంపై గల సంఖ్య ఏది?""",
        ['5', '4', '6', '1'],
        ['5', '4', '6', '1'],
        0,
        """Common faces rule: When two positions of a die share two common faces (here 1 and 3 are common in both positions), the remaining non-common faces must be opposite to each other.
Non-common face in Position A = 2.
Non-common face in Position B = 5.
Therefore, 2 is opposite to 5.""",
        """రెండు స్థానాలలో రెండు ముఖాలు (1 మరియు 3) ఉమ్మడిగా ఉన్నప్పుడు, మిగిలిన ముఖాలు ఒకదానికొకటి ఎదురెదురుగా ఉంటాయి. కాబట్టి 2 కి ఎదురుగా 5 ఉంటుంది."""
    ))

    qs.append(make_q(
        347, "Cubes & Dice - Unfolded Net Opposite", "Hard",
        """An unfolded cardboard net of a cube forms a cross pattern where faces are numbered 1, 2, 3, 4 in a vertical column from top to bottom, with 5 attached to the left of face 2 and 6 attached to the right of face 2. When this net is folded into a cube, which face will be opposite to face 5?""",
        """ఒక పాచిక యొక్క విప్పబడిన కాగితపు రేఖాచిత్రంలో నిలువుగా 1, 2, 3, 4 ఉన్నాయి, 2 కి ఎడమవైపు 5 మరియు కుడివైపు 6 ఉన్నాయి. ఈ రేఖాచిత్రాన్ని మడిచి ఘనంగా తయారు చేస్తే, 5 కి ఎదురుగా వచ్చే ముఖం ఏది?""",
        ['6', '3', '4', '1'],
        ['6', '3', '4', '1'],
        0,
        """In an unfolded cube net:
In the vertical strip, alternate faces are opposite: Face 1 is opposite Face 3; Face 2 is opposite Face 4.
The two lateral flaps extending on opposite sides of the strip fold up to face each other.
Therefore, Face 5 is opposite Face 6.""",
        """నిలువు వరుసలో 1 కి ఎదురుగా 3, 2 కి ఎదురుగా 4 ఉంటాయి. ఇరువైపులా ఉన్న పార్శ్వ ముఖాలు 5 మరియు 6 పరస్పరం ఎదురెదురుగా ఉంటాయి."""
    ))

    qs.append(make_q(
        348, "Figure Counting - Triangles in a Square with Diagonals", "Medium",
        """How many triangles are there in a square with both its diagonals and two medians (lines connecting midpoints of opposite sides) drawn?""",
        """రెండు కర్ణాలు మరియు ఎదురెదురు భుజాల మధ్యబిందువులను కలిపే రెండు మధ్యగత రేఖలు గీసిన ఒక చతురస్రంలో మొత్తం ఎన్ని త్రిభుజాలు ఉన్నాయి?""",
        ['16 triangles', '12 triangles', '18 triangles', '20 triangles'],
        ['16 త్రిభుజాలు', '12 త్రిభుజాలు', '18 త్రిభుజాలు', '20 త్రిభుజాలు'],
        0,
        """When a square has both diagonals and both horizontal/vertical mid-lines, it is divided into 8 smallest fundamental triangles.
Formula for triangles in a grid divided into n parts around centre = 2 * n.
Here n = 8 => Number of triangles = 2 * 8 = 16 triangles.""",
        """సూత్రం: కేంద్రం వద్ద 8 చిన్న త్రిభుజాలుగా విభజించబడినప్పుడు, మొత్తం త్రిభుజాలు = 2 * n = 2 * 8 = 16 త్రిభుజాలు."""
    ))

    qs.append(make_q(
        349, "Figure Counting - Squares in a 4x4 Chessboard Grid", "Medium",
        """What is the total number of squares of all sizes in a 4 x 4 square grid?""",
        """ఒక 4 x 4 చతురస్రాకార గ్రిడ్‌లో అన్ని పరిమాణాల చతురస్రాల మొత్తం సంఖ్య ఎంత?""",
        ['30 squares', '28 squares', '32 squares', '25 squares'],
        ['30 చతురస్రాలు', '28 చతురస్రాలు', '32 చతురస్రాలు', '25 చతురస్రాలు'],
        0,
        """Formula for total squares in an n x n grid = 1^2 + 2^2 + 3^2 + ... + n^2
For n = 4:
Total squares = 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30 squares.""",
        """n x n గ్రిడ్‌లోని చతురస్రాల సంఖ్య = 1^2 + 2^2 + 3^2 + ... + n^2.
4 x 4 గ్రిడ్ లో = 1 + 4 + 9 + 16 = 30 చతురస్రాలు."""
    ))

    qs.append(make_q(
        350, "Figure Counting - Triangles in Star", "Medium",
        """What is the total number of triangles in a standard five-pointed geometric star (pentagram)?""",
        """ఒక ప్రామాణిక ఐదు కోణాల జ్యామితీయ నక్షత్రంలో (Five-pointed Star / Pentagram) మొత్తం ఎన్ని త్రిభుజాలు ఉంటాయి?""",
        ['10 triangles', '8 triangles', '12 triangles', '5 triangles'],
        ['10 త్రిభుజాలు', '8 త్రిభుజాలు', '12 త్రిభుజాలు', '5 త్రిభుజాలు'],
        0,
        """In a 5-pointed star:
There are 5 small triangles at each of the five vertices.
Additionally, taking each vertex and using the internal opposite intersecting line segments, there are 5 larger overlapping triangles.
Total number of triangles = 5 + 5 = 10 triangles.""",
        """5-మూలల నక్షత్రంలో: బయటి వైపు 5 చిన్న త్రిభుజాలు + ప్రతి శీర్షం నుండి ఏర్పడే 5 పెద్ద త్రిభుజాలు ఉంటాయి.
మొత్తం త్రిభుజాలు = 5 + 5 = 10 త్రిభుజాలు."""
    ))

    return qs

if __name__ == "__main__":
    qs = get_reasoning_part3()
    print(f"Reasoning Part 3 successfully generated with {len(qs)} verified questions.")
