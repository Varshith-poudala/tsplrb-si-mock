import json
import os

print("Rebuilding Mock 3 to perfect 50+50+100 TSPLRB SI blueprint...")

# Load faculty curated bank
with open('public/data/faculty_curated_bank.json') as f:
    fc_qs = json.load(f).get('questions', [])

polity_fc = [q for q in fc_qs if 'polity' in q.get('subject', '').lower()]
tsm_fc = [q for q in fc_qs if 'movement' in q.get('subject', '').lower() or 'movement' in q.get('topic', '').lower() or 'telangana history' in q.get('subject', '').lower()]
gov_fc = [q for q in fc_qs if 'governance' in q.get('subject', '').lower() or 'telangana current' in q.get('subject', '').lower()]
hist_fc = [q for q in fc_qs if 'indian history' in q.get('subject', '').lower()]

# Load original Mock 3
with open('public/data/mock_test_full_200_3.json') as f:
    m3_qs = json.load(f).get('questions')

def make_q(q_num, section, topic, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
    return {
        "id": q_num,
        "qNumber": q_num,
        "section": section,
        "topic": topic,
        "question_en": q_en.strip(),
        "question_te": q_te.strip(),
        "options_en": [str(o).strip() for o in opts_en],
        "options_te": [str(o).strip() for o in opts_te],
        "correct_option": corr,
        "explanation_en": exp_en.strip(),
        "explanation_te": exp_te.strip()
    }

new_questions = []

# -------------------------------------------------------------
# PART A: ARITHMETIC (Q1 TO Q50)
# -------------------------------------------------------------
# Keep original Q1 to Q34
for i in range(34):
    q = m3_qs[i].copy()
    q['id'] = i + 1
    q['qNumber'] = i + 1
    q['section'] = 'Arithmetic'
    new_questions.append(q)

# Q35-Q41: Speed, Distance & Time (Trains, Boats, Relative Speed) - 7 questions
speed_qs = [
    (
        "A train travelling at 60 km/h crosses a platform 250 meters long in 27 seconds. What is the length of the train?",
        "60 కి.మీ/గం స్థిర వేగంతో ప్రయాణిస్తున్న ఒక రైలు 250 మీటర్ల పొడవు గల ప్లాట్‌ఫారమ్‌ను 27 సెకన్లలో దాటుతుంది. ఆ రైలు పొడవు ఎంత?",
        ["180 meters", "200 meters", "220 meters", "240 meters"],
        ["180 మీటర్లు", "200 మీటర్లు", "220 మీటర్లు", "240 మీటర్లు"],
        1,
        "Speed in m/s = 60 * (5/18) = 50/3 m/s. Distance = Speed * Time = (50/3) * 27 = 450 m. Length of train = 450 - 250 = 200 meters.",
        "వేగం = 50/3 మీ/సె. మొత్తం దూరం = (50/3) * 27 = 450 మీ. రైలు పొడవు = 450 - 250 = 200 మీటర్లు."
    ),
    (
        "Two trains of lengths 150 m and 130 m are running on parallel tracks in the same direction at 82 km/h and 64 km/h respectively. In how many seconds will the faster train completely overtake the slower train?",
        "150 మీ మరియు 130 మీ పొడవు గల రెండు రైళ్లు సమాంతర పట్టాలపై ఒకే దిశలో వరుసగా 82 కి.మీ/గం మరియు 64 కి.మీ/గం వేగాలతో వెళ్తున్నాయి. వేగవంతమైన రైలు నెమ్మదిగా వెళ్లే రైలును పూర్తిగా దాటడానికి ఎన్ని సెకన్లు పట్టును?",
        ["48 seconds", "52 seconds", "56 seconds", "60 seconds"],
        ["48 సెకన్లు", "52 సెకన్లు", "56 సెకన్లు", "60 సెకన్లు"],
        2,
        "Total distance = 150 + 130 = 280 m. Relative speed = 82 - 64 = 18 km/h = 5 m/s. Time = 280 / 5 = 56 seconds.",
        "దూరం = 280 మీ. సాపేక్ష వేగం = 18 కి.మీ/గం = 5 మీ/సె. సమయం = 280 / 5 = 56 సెకన్లు."
    ),
    (
        "A boat travels 36 km downstream in 3 hours and takes 6 hours to return the same distance upstream. What is the speed of the stream?",
        "ఒక పడవ ప్రవాహ దిశలో 36 కి.మీ దూరాన్ని 3 గంటలలో ప్రయాణించి, ప్రవాహానికి ఎదురు దిశలో అదే దూరాన్ని తిరిగి రావడానికి 6 గంటల సమయం తీసుకుంటుంది. ప్రవాహ వేగం ఎంత?",
        ["2 km/h", "3 km/h", "4 km/h", "5 km/h"],
        ["2 కి.మీ/గం", "3 కి.మీ/గం", "4 కి.మీ/గం", "5 కి.మీ/గం"],
        1,
        "Downstream speed u = 36/3 = 12 km/h. Upstream speed v = 36/6 = 6 km/h. Speed of stream y = (12 - 6)/2 = 3 km/h.",
        "ప్రవాహ దిశ వేగం = 12 కి.మీ/గం, ఎదురు వేగం = 6 కి.మీ/గం. ప్రవాహ వేగం = (12 - 6)/2 = 3 కి.మీ/గం."
    ),
    (
        "A man walks from his house to his office at 4 km/h and reaches 10 minutes late. If he walks at 5 km/h, he reaches 5 minutes early. What is the distance between his house and office?",
        "ఒక వ్యక్తి తన ఇంటి నుండి కార్యాలయానికి 4 కి.మీ/గం వేగంతో నడిచి 10 నిమిషాలు ఆలస్యంగా చేరుకుంటాడు. 5 కి.మీ/గం వేగంతో నడిస్తే 5 నిమిషాలు ముందుగా చేరుకుంటాడు. ఇంటి నుండి కార్యాలయానికి గల దూరం ఎంత?",
        ["4 km", "5 km", "6 km", "7.5 km"],
        ["4 కి.మీ", "5 కి.మీ", "6 కి.మీ", "7.5 కి.మీ"],
        1,
        "Time difference = 10 + 5 = 15 minutes = 1/4 hour. Distance D = (s1 * s2) / (s2 - s1) * Δt = (4 * 5) / (5 - 4) * (1/4) = 20 * (1/4) = 5 km.",
        "సమయాల తేడా = 15 నిమిషాలు = 1/4 గంట. దూరం = (4 * 5 / 1) * (1/4) = 5 కి.మీ."
    ),
    (
        "A car covers a distance of 450 km at a certain uniform speed. If the speed had been 15 km/h more, it would have taken 1.5 hours less. Find the original speed of the car.",
        "ఒక కారు 450 కి.మీ దూరాన్ని నిర్దిష్ట స్థిర వేగంతో ప్రయాణిస్తుంది. వేగం 15 కి.మీ/గం ఎక్కువైతే 1.5 గంటల సమయం తక్కువ పడుతుంది. కారు అసలు వేగం ఎంత?",
        ["60 km/h", "65 km/h", "75 km/h", "80 km/h"],
        ["60 కి.మీ/గం", "65 కి.మీ/గం", "75 కి.మీ/గం", "80 కి.మీ/గం"],
        0,
        "At 60 km/h, time = 450 / 60 = 7.5 hours. At 75 km/h, time = 450 / 75 = 6 hours. Difference = 7.5 - 6 = 1.5 hours. Original speed = 60 km/h.",
        "60 కి.మీ/గం వేగంతో సమయం = 7.5 గంటలు. 75 కి.మీ/గం వద్ద = 6 గంటలు. తేడా = 1.5 గంటలు. అసలు వేగం = 60 కి.మీ/గం."
    ),
    (
        "A motorboat takes 2 hours to travel 20 km upstream in a river where the current flows at 3 km/h. How much time will it take to travel the same distance downstream?",
        "3 కి.మీ/గం వేగంతో ప్రవహించే నదిలో ఒక మోటార్ బోట్ ప్రవాహానికి ఎదురుగా 20 కి.మీ ప్రయాణించడానికి 2 గంటలు పడుతుంది. అదే దూరాన్ని ప్రవాహ దిశలో ప్రయాణించడానికి ఎంత సమయం పట్టును?",
        ["1 hour 15 minutes", "1 hour 30 minutes", "1 hour 45 minutes", "2 hours"],
        ["1 గంట 15 నిమిషాలు", "1 గంట 30 నిమిషాలు", "1 గంట 45 నిమిషాలు", "2 గంటలు"],
        0,
        "Upstream speed v = 20 / 2 = 10 km/h. Speed of boat in still water = 10 + 3 = 13 km/h. Downstream speed u = 13 + 3 = 16 km/h. Time downstream = 20 / 16 = 5/4 hours = 1 hour 15 minutes.",
        "ఎదురు వేగం = 10 కి.మీ/గం. నిశ్చల నీటిలో బోట్ వేగం = 13 కి.మీ/గం. ప్రవాహ దిశ వేగం = 16 కి.మీ/గం. సమయం = 20/16 = 1 గంట 15 నిమిషాలు."
    ),
    (
        "Excluding stoppages, the speed of a bus is 54 km/h and including stoppages, it is 45 km/h. For how many minutes does the bus stop per hour?",
        "ఆగడాలు (stoppages) మినహాయిస్తే బస్సు వేగం 54 కి.మీ/గం, ఆగడాలతో కలిపితే 45 కి.మీ/గం. బస్సు గంటకు ఎన్ని నిమిషాలు ఆగుతుంది?",
        ["8 minutes", "10 minutes", "12 minutes", "15 minutes"],
        ["8 నిమిషాలు", "10 నిమిషాలు", "12 నిమిషాలు", "15 నిమిషాలు"],
        1,
        "Stoppage time = (54 - 45) / 54 * 60 = (9/54) * 60 = 10 minutes per hour.",
        "ఆగే సమయం = (54 - 45) / 54 * 60 = 10 నిమిషాలు/గంట."
    )
]

for idx, sq in enumerate(speed_qs):
    q_num = 35 + idx
    new_questions.append(make_q(q_num, 'Arithmetic', 'Speed, Distance & Time', sq[0], sq[1], sq[2], sq[3], sq[4], sq[5], sq[6]))

# Q42-Q47: Mensuration (2D & 3D) - 6 questions
mensuration_qs = [
    (
        "A rectangular grassy plot 110 m by 65 m has a gravel path 2.5 m wide all around it on the inside. What is the area of the gravel path?",
        "110 మీ x 65 మీ కొలతలు గల ఒక దీర్ఘచతురస్రాకార స్థలం లోపలి వైపు చుట్టూ 2.5 మీ వెడల్పు గల కంకర బాట కలదు. ఆ బాట వైశాల్యం ఎంత?",
        ["850 sq.m", "875 sq.m", "900 sq.m", "925 sq.m"],
        ["850 చ.మీ", "875 చ.మీ", "900 చ.మీ", "925 చ.మీ"],
        0,
        "Outer Area = 110 * 65 = 7150 sq.m. Inner Area = (110 - 5) * (65 - 5) = 105 * 60 = 6300 sq.m. Path Area = 7150 - 6300 = 850 sq.m.",
        "బాట వైశాల్యం = 7150 - 6300 = 850 చ.మీ."
    ),
    (
        "A circular copper wire of radius 28 cm is bent into the shape of a square. Find the side of the square. (Take π = 22/7)",
        "28 సెం.మీ వ్యాసార్థం గల వృత్తాకార రాగి తీగను చతురస్రాకారంలోకి మలిచారు. ఆ చతురస్రం యొక్క భుజం పొడవు ఎంత?",
        ["40 cm", "44 cm", "48 cm", "52 cm"],
        ["40 సెం.మీ", "44 సెం.మీ", "48 సెం.మీ", "52 సెం.మీ"],
        1,
        "Perimeter of square = Circumference of circle = 2 * (22/7) * 28 = 176 cm. Side = 176 / 4 = 44 cm.",
        "చతురస్ర చుట్టుకొలత = వృత్త పరిధి = 176 సెం.మీ. భుజం = 176 / 4 = 44 సెం.మీ."
    ),
    (
        "The diagonals of a rhombus are 32 cm and 24 cm respectively. Find the perimeter of the rhombus.",
        "ఒక రాంబస్ యొక్క కర్ణములు వరుసగా 32 సెం.మీ మరియు 24 సెం.మీ. ఆ రాంబస్ యొక్క చుట్టుకొలత ఎంత?",
        ["72 cm", "80 cm", "88 cm", "96 cm"],
        ["72 సెం.మీ", "80 సెం.మీ", "88 సెం.మీ", "96 సెం.మీ"],
        1,
        "Side of rhombus a = √[(32/2)^2 + (24/2)^2] = √(16^2 + 12^2) = √400 = 20 cm. Perimeter = 4 * 20 = 80 cm.",
        "భుజం = √(16^2 + 12^2) = 20 సెం.మీ. చుట్టుకొలత = 4 * 20 = 80 సెం.మీ."
    ),
    (
        "The radius of the base of a right circular cylinder is 7 cm and its height is 15 cm. Find its total surface area. (Take π = 22/7)",
        "ఒక స్థూపం భూ వ్యాసార్థం 7 సెం.మీ మరియు ఎత్తు 15 సెం.మీ. దాని సంపూర్ణతల వైశాల్యం ఎంత?",
        ["880 sq.cm", "968 sq.cm", "1024 sq.cm", "1100 sq.cm"],
        ["880 చ.సెం.మీ", "968 చ.సెం.మీ", "1024 చ.సెం.మీ", "1100 చ.సెం.మీ"],
        1,
        "Total Surface Area = 2πr(h + r) = 2 * (22/7) * 7 * (15 + 7) = 44 * 22 = 968 sq.cm.",
        "సంపూర్ణతల వైశాల్యం = 2πr(h + r) = 44 * 22 = 968 చ.సెం.మీ."
    ),
    (
        "A solid metallic sphere of radius 6 cm is melted and recast into small solid cones, each of base radius 2 cm and height 3 cm. How many such cones can be formed?",
        "6 సెం.మీ వ్యాసార్థం గల లోహపు గోళాన్ని కరిగించి, భూ వ్యాసార్థం 2 సెం.మీ మరియు ఎత్తు 3 సెం.మీ గల చిన్న శంకువులుగా తయారు చేసెను. ఎన్ని శంకువులు తయారవుతాయి?",
        ["48", "64", "72", "84"],
        ["48", "64", "72", "84"],
        2,
        "Volume of sphere = (4/3)πR^3 = 288π. Volume of cone = (1/3)πr^2h = 4π. Number = 288π / 4π = 72.",
        "గోళ ఘనపరిమాణం / శంకువు ఘనపరిమాణం = 288π / 4π = 72 శంకువులు."
    ),
    (
        "Find the length of the longest rod that can be placed inside a room of dimensions 12 m × 9 m × 8 m.",
        "12 మీ × 9 మీ × 8 మీ కొలతలు గల గదిలో ఉంచగల అత్యంత పొడవైన కర్ర పొడవు ఎంత?",
        ["15 meters", "17 meters", "19 meters", "21 meters"],
        ["15 మీటర్లు", "17 మీటర్లు", "19 మీటర్లు", "21 మీటర్లు"],
        1,
        "Diagonal of room = √(12^2 + 9^2 + 8^2) = √(144 + 81 + 64) = √289 = 17 meters.",
        "గది కర్ణం = √(144 + 81 + 64) = √289 = 17 మీటర్లు."
    )
]

for idx, mq in enumerate(mensuration_qs):
    q_num = 42 + idx
    new_questions.append(make_q(q_num, 'Arithmetic', 'Mensuration (2D & 3D)', mq[0], mq[1], mq[2], mq[3], mq[4], mq[5], mq[6]))

# Q48-Q50: Averages / Allegation (Keep original Q46-Q48)
for idx, orig_idx in enumerate([45, 46, 47]):
    q = m3_qs[orig_idx].copy()
    q_num = 48 + idx
    q['id'] = q_num
    q['qNumber'] = q_num
    q['section'] = 'Arithmetic'
    new_questions.append(q)

print(f"Part A complete: {len(new_questions)} questions.")

# -------------------------------------------------------------
# PART B: REASONING & MENTAL ABILITY (Q51 TO Q100)
# -------------------------------------------------------------
for i in range(50, 100):
    q = m3_qs[i].copy()
    q['id'] = i + 1
    q['qNumber'] = i + 1
    q['section'] = 'Reasoning'
    new_questions.append(q)

print(f"Part B complete: {len(new_questions)} questions.")

# -------------------------------------------------------------
# PART C: GENERAL STUDIES (Q101 TO Q200) - 100 BALANCED QUESTIONS
# -------------------------------------------------------------

# 1. General Science (Q101-Q114) - 14 Qs
for i in range(14):
    q = m3_qs[115 + i].copy()
    q_num = 101 + i
    q['id'] = q_num
    q['qNumber'] = q_num
    q['section'] = 'General Studies'
    new_questions.append(q)

# 2. Current Affairs & Multilateral Summits (Q115-Q130) - 16 Qs
for i in range(15):
    q = m3_qs[100 + i].copy()
    q_num = 115 + i
    q['id'] = q_num
    q['qNumber'] = q_num
    q['section'] = 'General Studies'
    new_questions.append(q)

# Add 16th CA: BRICS 2024 Kazan Summit & New Members (Shentu's specific suggestion)
new_questions.append(make_q(
    130, 'General Studies', 'Current Affairs - Multilateral Summits & International Organizations',
    """Consider the following statements regarding the 16th BRICS Summit held in Kazan, Russia:
1. It was the first summit held with the participation of five new member states: Egypt, Ethiopia, Iran, Saudi Arabia, and the UAE.
2. The theme of the summit was 'Strengthening Multilateralism for Just Global Development and Security'.
3. The New Development Bank (NDB) was formally merged into the International Monetary Fund during the summit.
Which of the statements given above is/are correct?""",
    """రష్యాలోని కజాన్‌లో జరిగిన 16వ బ్రిక్స్ (BRICS) శిఖరాగ్ర సదస్సుకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:
1. ఈజిప్ట్, ఇథియోపియా, ఇరాన్, సౌదీ అరేబియా మరియు యునైటెడ్ అరబ్ ఎమిరేట్స్ (UAE) అనే ఐదు నూతన సభ్య దేశాల భాగస్వామ్యంతో జరిగిన మొదటి సదస్సు ఇది.
2. ఈ సదస్సు ఇతివృత్తం 'న్యాయమైన ప్రపంచ అభివృద్ధి మరియు భద్రత కోసం బహుళపక్షవాదాన్ని బలోపేతం చేయడం'.
3. ఈ సదస్సులో న్యూ డెవలప్‌మెంట్ బ్యాంక్ (NDB) అధికారికంగా అంతర్జాతీయ ద్రవ్య నిధి (IMF) లో విలీనం చేయబడింది.
పై ప్రకటనలలో ఏది/వి సరైనది/వి?""",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
    0,
    "Statements 1 and 2 are correct. Statement 3 is incorrect: The New Development Bank (NDB) headquartered in Shanghai operates as an independent multilateral bank and was not merged into the IMF.",
    "ప్రకటనలు 1 మరియు 2 సరైనవి. ప్రకటన 3 తప్పు: షాంఘై ప్రధాన కేంద్రంగా గల న్యూ డెవలప్‌మెంట్ బ్యాంక్ స్వతంత్ర బహుళపక్ష బ్యాంకుగా కొనసాగుతోంది."
))

# 3. Geography of India & Telangana (Q131-Q144) - 14 Qs
for i in range(14):
    q = m3_qs[172 + i].copy()
    q_num = 131 + i
    q['id'] = q_num
    q['qNumber'] = q_num
    q['section'] = 'General Studies'
    new_questions.append(q)

# 4. Indian & Telangana Economy (Q145-Q158) - 14 Qs
economy_qs = [
    (
        """Consider the following statements regarding the Goods and Services Tax (GST) Council established under Article 279A of the Constitution of India:
1. The Union Finance Minister serves as the Chairperson of the GST Council.
2. Every decision of the Council requires a majority of not less than three-fourths (75%) of the weighted votes of the members present and voting.
3. The vote of the Central Government has a weightage of one-third (33.33%) of total votes, and the votes of all State Governments combined have a weightage of two-thirds (66.67%).
Which of the statements given above are correct?""",
        """భారత రాజ్యాంగంలోని అధికరణం 279A క్రింద ఏర్పడిన వస్తు సేవల పన్ను (GST) కౌన్సిల్ కు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:
1. కేంద్ర ఆర్థిక మంత్రి GST కౌన్సిల్ ఛైర్‌పర్సన్‌గా వ్యవహరిస్తారు.
2. కౌన్సిల్ తీసుకునే ప్రతి నిర్ణయానికి హాజరై ఓటు వేసిన సభ్యుల వెయిటెడ్ ఓట్లలో కనీసం మూడొంతుల (75%) మెజారిటీ అవసరం.
3. కేంద్ర ప్రభుత్వ ఓటుకు మూడోవంతు (1/3) వెయిటేజీ, అన్ని రాష్ట్ర ప్రభుత్వాల ఉమ్మడి ఓట్లకు మూడింట రెండొంతుల (2/3) వెయిటేజీ ఉంటుంది.
పై ప్రకటనలలో సరైనవి ఏవి?""",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct under Article 279A of the Indian Constitution.",
        "భారత రాజ్యాంగంలోని అధికరణం 279A ప్రకారం మూడు ప్రకటనలూ సరైనవి."
    ),
    (
        "Which price index is officially adopted by the Reserve Bank of India's Monetary Policy Committee (MPC) as the headline anchor for targeting inflation under the flexible inflation targeting framework?",
        "రిజర్వ్ బ్యాంక్ ఆఫ్ ఇండియా మానిటరీ పాలసీ కమిటీ (MPC) ద్రవ్యోల్బణ నియంత్రణ లక్ష్యం కోసం అధికారికంగా ఏ సూచీని ప్రధాన ఆధారంగా స్వీకరించింది?",
        ["Wholesale Price Index (WPI - All Commodities)", "Consumer Price Index (CPI - Combined)", "Index of Industrial Production (IIP)", "GDP Deflator"],
        ["టోకు ధరల సూచీ (WPI)", "వినియోగదారుల ధరల సూచీ (CPI - కంబైన్డ్)", "పారిశ్రామిక ఉత్పత్తి సూచీ (IIP)", "జీడీపీ డీఫ్లేటర్"],
        1,
        "RBI officially adopted Consumer Price Index (CPI-Combined) with base year 2012 as the headline inflation anchor with a target of 4% (+/- 2%).",
        "ఆర్బీఐ 4% (+/- 2%) ద్రవ్యోల్బణ లక్ష్యం కోసం వినియోగదారుల ధరల సూచీ (CPI - కంబైన్డ్) ని ప్రామాణికంగా స్వీకరించింది."
    ),
    (
        "What is defined as 'Primary Deficit' in the Union and State Government Budgets?",
        "కేంద్ర మరియు రాష్ట్ర ప్రభుత్వ బడ్జెట్లలో 'ప్రాథమిక లోటు' (Primary Deficit) అనగా ఏమిటి?",
        ["Fiscal Deficit minus Interest Payments", "Revenue Deficit minus Capital Grants", "Fiscal Deficit plus Disinvestment Proceeds", "Total Expenditure minus Total Revenue Receipts"],
        ["ద్రవ్య లోటు మైనస్ వడ్డీ చెల్లింపులు", "రెవెన్యూ లోటు మైనస్ మూలధన గ్రాంట్లు", "ద్రవ్య లోటు ప్లస్ పెట్టుబడుల ఉపసంహరణ", "మొత్తం వ్యయం మైనస్ మొత్తం రెవెన్యూ వసూళ్లు"],
        0,
        "Primary Deficit = Fiscal Deficit - Interest Payments. It indicates the government's borrowing requirement excluding interest liabilities on past debts.",
        "ప్రాథమిక లోటు = ద్రవ్య లోటు - వడ్డీ చెల్లింపులు. ఇది గత రుణాలపై వడ్డీలను మినహాయించి ప్రస్తుత ప్రభుత్వ రుణ అవసరాన్ని సూచిస్తుంది."
    ),
    (
        "The flagship scheme 'Rythu Bharosa' launched by the Government of Telangana provides financial investment support of what amount per acre per year to farmers?",
        "తెలంగాణ ప్రభుత్వం అమలు చేస్తున్న 'రైతు భరోసా' పథకం క్రింద రైతులకు ఎకరానికి సంవత్సరానికి ఎంత ఆర్థిక సాయం అందించబడుతుంది?",
        ["₹10,000 per acre", "₹12,000 per acre", "₹15,000 per acre", "₹18,000 per acre"],
        ["ఎకరానికి ₹10,000", "ఎకరానికి ₹12,000", "ఎకరానికి ₹15,000", "ఎకరానికి ₹18,000"],
        2,
        "Under Rythu Bharosa, the financial assistance is enhanced to ₹15,000 per acre per year (₹7,500 per crop season for Rabi and Kharif).",
        "రైతు భరోసా క్రింద సంవత్సరానికి ఎకరానికి ₹15,000 (రెండు పంటలకు ₹7,500 చొప్పున) పెట్టుబడి సాయం అందించబడుతుంది."
    ),
    (
        "Which of the following bodies replaced the 65-year-old Planning Commission of India on 1st January 2015?",
        "1 జనవరి 2015న 65 ఏళ్ల నాటి ప్రణాళికా సంఘం స్థానంలో క్రింది వాటిలో ఏ వ్యవస్థ ఏర్పాటయింది?",
        ["National Development Council (NDC)", "NITI Aayog (National Institution for Transforming India)", "Fiscal Responsibility Commission", "National Economic Development Forum"],
        ["జాతీయ అభివృద్ధి మండలి (NDC)", "నీతి ఆయోగ్ (NITI Aayog)", "ఫిస్కల్ రెస్పాన్సిబిలిటీ కమిషన్", "నేషనల్ ఎకనామిక్ ఫోరమ్"],
        1,
        "NITI Aayog was formed on January 1, 2015 via Cabinet resolution, replacing the Planning Commission.",
        "కేబినెట్ తీర్మానం ద్వారా 1 జనవరి 2015న ప్రణాళికా సంఘం స్థానంలో నీతి ఆయోగ్ ఏర్పాటయింది."
    ),
    (
        "Under the 'Gruha Jyothi' guarantee scheme launched in Telangana, how many units of free domestic electricity are provided per month to eligible poor households?",
        "తెలంగాణ ప్రభుత్వం ప్రారంభించిన 'గృహ జ్యోతి' హామీ పథకం క్రింద అర్హులైన పేద కుటుంబాలకు నెలకు ఎన్ని యూనిట్ల ఉచిత గృహ విద్యుత్ అందించబడుతుంది?",
        ["100 units", "150 units", "200 units", "250 units"],
        ["100 యూనిట్లు", "150 యూనిట్లు", "200 యూనిట్లు", "250 యూనిట్లు"],
        2,
        "Gruha Jyothi provides up to 200 units of free domestic electricity per month to eligible families.",
        "గృహ జ్యోతి పథకం క్రింద నెలకు 200 యూనిట్ల వరకు ఉచిత గృహ విద్యుత్ అందించబడుతుంది."
    ),
    (
        "The Insolvency and Bankruptcy Code (IBC) was enacted in India in 2016 primarily to:",
        "భారతదేశంలో 2016 లో ఇన్సాల్వెన్సీ అండ్ బ్యాంక్‌రప్ట్సీ కోడ్ (IBC) ను ప్రధానంగా దేని కోసం ప్రవేశపెట్టారు?",
        ["Regulate cryptocurrency markets", "Consolidate and streamline the time-bound resolution of corporate distress and NPA recovery", "Enforce direct tax assessments", "Nationalize private sector financial institutions"],
        ["క్రిప్టోకరెన్సీ మార్కెట్లను నియంత్రించుటకు", "కార్పొరేట్ సంస్థల దివాళా పరిష్కారాన్ని మరియు మొండి బకాయిల (NPA) రికవరీని వేగవంతం చేయుటకు", "ప్రత్యక్ష పన్నుల లెక్కింపునకు", "ప్రైవేట్ బ్యాంకుల జాతీయకరణకు"],
        1,
        "IBC 2016 provides a time-bound corporate insolvency resolution process (CIRP) to resolve stressed assets.",
        "మొండి బకాయిల (NPA) సత్వర పరిష్కారం మరియు దివాళా తీసిన కంపెనీల పునరుద్ధరణకు IBC 2016 ను అమలు చేశారు."
    ),
    (
        "Which premier incubator in Hyderabad, established in partnership with the Government of Telangana, is recognized as the world's largest technology incubator facility?",
        "తెలంగాణ ప్రభుత్వ భాగస్వామ్యంతో హైదరాబాద్‌లో ఏర్పాటైన ప్రపంచంలోనే అతిపెద్ద టెక్నాలజీ ఇంక్యుబేటర్ ఫెసిలిటీ ఏది?",
        ["T-Hub (Technology Hub)", "T-Works", "WE Hub", "RICH (Research and Innovation Circle of Hyderabad)"],
        ["టి-హబ్ (T-Hub)", "టి-వర్క్స్ (T-Works)", "వి-హబ్ (WE Hub)", "రిచ్ (RICH)"],
        0,
        "T-Hub Phase 2 in Madhapur/Raidurg, Hyderabad, spanning over 5.8 lakh sq.ft, is the world's largest startup innovation campus.",
        "హైదరాబాద్‌లోని టి-హబ్ ఫేజ్-2 ప్రపంచంలోనే అతిపెద్ద స్టార్టప్ ఇన్నోవేషన్ ఇంక్యుబేటర్ ప్రాంగణంగా గుర్తింపు పొందింది."
    ),
    (
        "What is the base year currently used for calculating India's official Gross Domestic Product (GDP) series?",
        "భారతదేశ అధికారిక స్థూల జాతీయోత్పత్తి (GDP) గణనలో ప్రస్తుతం ఉపయోగించే మూల సంవత్సరం (Base Year) ఏది?",
        ["2004-05", "2011-12", "2015-16", "2018-19"],
        ["2004-05", "2011-12", "2015-16", "2018-19"],
        1,
        "The Central Statistics Office (CSO/NSO) revised the base year for GDP computation from 2004-05 to 2011-12 in January 2015.",
        "భారతదేశ జీడీపీ లెక్కల మూల సంవత్సరం 2011-12."
    ),
    (
        "Under the 'Mahalakshmi Scheme' in Telangana, which zero-fare welfare entitlement is provided to all girls and women residing in the state?",
        "తెలంగాణలోని 'మహాలక్ష్మి పథకం' క్రింద రాష్ట్రంలోని మహిళలు మరియు బాలికలకు అందించబడుతున్న ఉచిత సంక్షేమ ప్రయోజనం ఏది?",
        ["Free LPG cooking cylinder refills", "Free travel in TSRTC / TGSRTC Palle Velugu and Express buses", "Free internet broadband access", "Free health insurance coverage up to ₹20 lakhs"],
        ["ఉచిత ఎల్‌పీజీ గ్యాస్ సిలిండర్లు", "TSRTC / TGSRTC పల్లె వెలుగు మరియు ఎక్స్‌ప్రెస్ బస్సులలో ఉచిత ప్రయాణం", "ఉచిత ఇంటర్నెట్ సౌకర్యం", "₹20 లక్షల ఉచిత ఆరోగ్య బీమా"],
        1,
        "Mahalakshmi scheme provides 100% free bus travel to girls, women, and transgender persons across Telangana in non-AC TGSRTC buses.",
        "మహాలక్ష్మి పథకం క్రింద రాష్ట్రవ్యాప్తంగా పల్లె వెలుగు, ఎక్స్‌ప్రెస్ బస్సుల్లో మహిళలకు ఉచిత బస్సు ప్రయాణ సదుపాయం కల్పించబడింది."
    ),
    (
        "What is the statutory threshold limit for 'Fiscal Deficit' as a percentage of GSDP recommended for states by the 15th Finance Commission under the FRBM framework?",
        "ఎఫ్ఆర్బీఎం (FRBM) చట్టం క్రింద 15వ ఆర్థిక సంఘం రాష్ట్రాల స్థూల రాష్ట్ర దేశీయోత్పత్తి (GSDP) లో ద్రవ్య లోటు పరిమితిని ఎంత శాతంగా సిఫార్సు చేసింది?",
        ["2.0% of GSDP", "2.5% of GSDP", "3.0% of GSDP (with 0.5% power sector performance linkage)", "5.0% of GSDP"],
        ["GSDP లో 2.0%", "GSDP లో 2.5%", "GSDP లో 3.0% (విద్యుత్ సంస్కరణలకు అదనంగా 0.5%)", "GSDP లో 5.0%"],
        2,
        "The standard FRBM fiscal deficit anchor for states is 3% of GSDP, with an extra 0.5% conditional on power sector reforms.",
        "రాష్ట్రాల సాధారణ ద్రవ్య లోటు పరిమితి GSDP లో 3% (విద్యుత్ సంస్కరణల అమలుతో అదనంగా 0.5%)."
    ),
    (
        "The 'Kakatiya Mega Textile Park' (KMTP), developed as one of the largest integrated textile clusters in India, is situated in which district of Telangana?",
        "భారతదేశంలోనే అతిపెద్ద ఇంటిగ్రేటెడ్ టెక్స్‌టైల్ పార్కులలో ఒకటైన 'కాకతీయ మెగా టెక్స్‌టైల్ పార్క్' తెలంగాణలోని ఏ జిల్లాలో ఏర్పాటయింది?",
        ["Karimnagar", "Warangal", "Nalgonda", "Sircilla"],
        ["కరీంనగర్", "వరంగల్", "నల్గొండ", "సిరిసిల్ల"],
        1,
        "Kakatiya Mega Textile Park is situated at Shayampet in Warangal district over 1,200 acres.",
        "కాకతీయ మెగా టెక్స్‌టైల్ పార్క్ వరంగల్ జిల్లా శ్యాంపేట వద్ద ఏర్పాటయింది."
    ),
    (
        "What does 'Standing Deposit Facility' (SDF) introduced by the Reserve Bank of India in 2022 enable the central bank to do?",
        "2022లో రిజర్వ్ బ్యాంక్ ఆఫ్ ఇండియా ప్రవేశపెట్టిన 'స్టాండింగ్ డిపాజిట్ ఫెసిలిటీ' (SDF) యొక్క ముఖ్య ఉద్దేశం ఏమిటి?",
        ["Absorb excess liquidity from banks without offering collateral securities", "Provide collateral-free long term loans to MSMEs", "Inject overnight liquidity during financial runs", "Finance state government budget deficits directly"],
        ["ఎటువంటి హామీ (సెక్యూరిటీలు) ఇవ్వకుండానే బ్యాంకుల వద్ద నుండి మిగులు నగదును స్వీకరించుట", "చిన్న పరిశ్రమలకు పూచీకత్తు లేని రుణాలు ఇచ్చుట", "మార్కెట్లోకి అదనపు నగదును విడుదల చేయుట", "రాష్ట్రాల బడ్జెట్ లోటును నేరుగా పూడ్చుట"],
        0,
        "SDF allows the RBI to absorb surplus liquidity from the commercial banking system without having to pledge government securities as collateral.",
        "బ్యాంకుల నుండి ఎటువంటి ప్రభుత్వ సెక్యూరిటీలను తనఖా పెట్టకుండా మిగులు ద్రవ్యత్వాన్ని స్వీకరించడానికి SDF ప్రవేశపెట్టబడింది."
    ),
    (
        "The flagship drinking water supply grid project 'Mission Bhagiratha' in Telangana was designed to provide treated surface water to every rural household at what quantity per capita per day?",
        "తెలంగాణలోని ప్రతి గ్రామీణ గృహానికి సురక్షిత రక్షిత తాగునీరు అందించే 'మిషన్ భగీరథ' క్రింద గ్రామీణ ప్రాంతాల్లో వ్యక్తికి రోజుకు ఎన్ని లీటర్ల నీరు అందించేలా రూపకల్పన చేశారు?",
        ["55 Litres per capita per day (LPCD)", "100 Litres per capita per day (LPCD)", "135 Litres per capita per day (LPCD)", "150 Litres per capita per day (LPCD)"],
        ["రోజుకు వ్యక్తికి 55 లీటర్లు (LPCD)", "రోజుకు వ్యక్తికి 100 లీటర్లు (LPCD)", "రోజుకు వ్యక్తికి 135 లీటర్లు (LPCD)", "రోజుకు వ్యక్తికి 150 లీటర్లు (LPCD)"],
        1,
        "Mission Bhagiratha supplies 100 LPCD in rural households, 135 LPCD in municipalities, and 150 LPCD in municipal corporations.",
        "మిషన్ భగీరథ ద్వారా గ్రామీణ ప్రాంతాల్లో రోజుకు తలసరి 100 లీటర్లు, మున్సిపాలిటీలలో 135 లీటర్లు, కార్పొరేషన్లలో 150 లీటర్ల నీరు అందించబడుతుంది."
    )
]

for idx, eq in enumerate(economy_qs):
    q_num = 145 + idx
    new_questions.append(make_q(q_num, 'General Studies', 'Indian & Telangana Economy', eq[0], eq[1], eq[2], eq[3], eq[4], eq[5], eq[6]))

# 5. Indian Polity & Governance (Q159-Q175) - 17 Qs
for idx, pq in enumerate(polity_fc[:17]):
    q_num = 159 + idx
    opts_en = pq.get('options_en', ['A', 'B', 'C', 'D'])
    opts_te = pq.get('options_te', opts_en)
    new_questions.append(make_q(
        q_num, 'General Studies', f"Indian Polity - {pq.get('topic', 'Constitutional Governance')}",
        pq.get('question_en', ''), pq.get('question_te', ''),
        opts_en, opts_te, pq.get('correct_option', 0),
        pq.get('explanation_en', ''), pq.get('explanation_te', '')
    ))

# 6. Indian History & National Movement (Q176-Q188) - 13 Qs
# Select 13 best unique Indian History questions from original Mock 3 (Q131-Q143)
for idx in range(13):
    q = m3_qs[130 + idx].copy()
    q_num = 176 + idx
    q['id'] = q_num
    q['qNumber'] = q_num
    q['section'] = 'General Studies'
    new_questions.append(q)

# 7. Telangana History & Statehood Movement (Q189-Q200) - 12 Qs
for idx, tq in enumerate(tsm_fc[:12]):
    q_num = 189 + idx
    opts_en = tq.get('options_en', ['A', 'B', 'C', 'D'])
    opts_te = tq.get('options_te', opts_en)
    new_questions.append(make_q(
        q_num, 'General Studies', f"Telangana History & Movement - {tq.get('topic', 'Statehood Movement')}",
        tq.get('question_en', ''), tq.get('question_te', ''),
        opts_en, opts_te, tq.get('correct_option', 0),
        tq.get('explanation_en', ''), tq.get('explanation_te', '')
    ))

print(f"Total new questions: {len(new_questions)}")
assert len(new_questions) == 200, f"Expected 200 questions, got {len(new_questions)}"

# Write out rebalanced Mock 3
out_path = 'public/data/mock_test_full_200_3.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({"testId": "tsplrb-si-mock-full-200-3", "questions": new_questions}, f, ensure_ascii=False, indent=2)

print("✅ Rebalanced Mock 3 saved successfully!")
