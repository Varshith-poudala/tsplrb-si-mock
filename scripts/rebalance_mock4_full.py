import json
import os

print("Rebuilding Mock 4 to perfect 50+50+100 TSPLRB SI blueprint...")

# Load faculty curated bank
with open('public/data/faculty_curated_bank.json') as f:
    fc_qs = json.load(f).get('questions', [])

# Load original Mock 4
with open('public/data/mock_test_full_200_4.json') as f:
    m4_qs = json.load(f).get('questions')

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
# PART A: ARITHMETIC (Q1 TO Q50) - 50 QUESTIONS
# -------------------------------------------------------------
# Retain first 40 arithmetic questions from Mock 4
for i in range(40):
    q = m4_qs[i].copy()
    q['id'] = i + 1
    q['qNumber'] = i + 1
    q['section'] = 'Arithmetic'
    new_questions.append(q)

# Q41-Q46: Mensuration (2D & 3D) - 6 authentic questions
mensuration_qs = [
    (
        "The perimeter of a right-angled triangle is 60 cm and its hypotenuse is 25 cm. Find the area of the triangle.",
        "ఒక లంబకోణ త్రిభుజం యొక్క చుట్టుకొలత 60 సెం.మీ మరియు దాని కర్ణం 25 సెం.మీ. ఆ త్రిభుజం వైశాల్యం ఎంత?",
        ["120 sq.cm", "150 sq.cm", "180 sq.cm", "200 sq.cm"],
        ["120 చ.సెం.మీ", "150 చ.సెం.మీ", "180 చ.సెం.మీ", "200 చ.సెం.మీ"],
        1,
        "Let perpendicular sides be a and b. a + b + 25 = 60 => a + b = 35. Also a^2 + b^2 = 25^2 = 625. (a + b)^2 = a^2 + b^2 + 2ab => 35^2 = 625 + 2ab => 1225 - 625 = 2ab => 600 = 2ab => Area = (1/2)ab = 600 / 4 = 150 sq.cm.",
        "a + b = 35. a^2 + b^2 = 625. 2ab = 1225 - 625 = 600. వైశాల్యం = ab / 2 = 150 చ.సెం.మీ."
    ),
    (
        "The parallel sides of a trapezium are 20 cm and 12 cm, and the distance between them is 10 cm. Find the area of the trapezium.",
        "ఒక ట్రెపీజియం సమాంతర భుజాలు 20 సెం.మీ మరియు 12 సెం.మీ, మరియు వాటి మధ్య లంబ దూరం 10 సెం.మీ. ఆ ట్రెపీజియం వైశాల్యం ఎంత?",
        ["140 sq.cm", "160 sq.cm", "180 sq.cm", "200 sq.cm"],
        ["140 చ.సెం.మీ", "160 చ.సెం.మీ", "180 చ.సెం.మీ", "200 చ.సెం.మీ"],
        1,
        "Area of trapezium = (1/2) * (sum of parallel sides) * height = (1/2) * (20 + 12) * 10 = (1/2) * 32 * 10 = 160 sq.cm.",
        "ట్రెపీజియం వైశాల్యం = 1/2 * (a + b) * h = 1/2 * 32 * 10 = 160 చ.సెం.మీ."
    ),
    (
        "A cone of radius 7 cm and height 24 cm has a curved surface area of what value? (Take π = 22/7)",
        "7 సెం.మీ భూ వ్యాసార్థం మరియు 24 సెం.మీ ఎత్తు గల శంకువు యొక్క ప్రక్కతల వైశాల్యం ఎంత?",
        ["500 sq.cm", "550 sq.cm", "600 sq.cm", "650 sq.cm"],
        ["500 చ.సెం.మీ", "550 చ.సెం.మీ", "600 చ.సెం.మీ", "650 చ.సెం.మీ"],
        1,
        "Slant height l = √(r^2 + h^2) = √(49 + 576) = √625 = 25 cm. Curved Surface Area = πrl = (22/7) * 7 * 25 = 22 * 25 = 550 sq.cm.",
        "ఏటవాలు ఎత్తు l = √(7^2 + 24^2) = 25 సెం.మీ. ప్రక్కతల వైశాల్యం = πrl = (22/7) * 7 * 25 = 550 చ.సెం.మీ."
    ),
    (
        "The dimensions of a rectangular solid box are in the ratio 3 : 2 : 1 and its total surface area is 352 sq.cm. Find the volume of the box.",
        "ఒక దీర్ఘఘనం యొక్క కొలతలు 3 : 2 : 1 నిష్పత్తిలో ఉన్నాయి మరియు దాని సంపూర్ణతల వైశాల్యం 352 చ.సెం.మీ. ఆ దీర్ఘఘనం ఘనపరిమాణం ఎంత?",
        ["384 cu.cm", "432 cu.cm", "480 cu.cm", "512 cu.cm"],
        ["384 ఘ.సెం.మీ", "432 ఘ.సెం.మీ", "480 ఘ.సెం.మీ", "512 ఘ.సెం.మీ"],
        0,
        "Let sides be 3x, 2x, 1x. TSA = 2(lb + bh + hl) = 2(6x^2 + 2x^2 + 3x^2) = 22x^2 = 352 => x^2 = 16 => x = 4. Dimensions are 12, 8, 4. Volume = 12 * 8 * 4 = 384 cu.cm.",
        "సంపూర్ణతల వైశాల్యం = 22x^2 = 352. x = 4. కొలతలు 12, 8, 4. ఘనపరిమాణం = 12 * 8 * 4 = 384 ఘ.సెం.మీ."
    ),
    (
        "If the radius of a sphere is increased by 50%, by what percentage does its surface area increase?",
        "ఒక గోళం యొక్క వ్యాసార్థాన్ని 50% పెంచినచో, దాని ఉపరితల వైశాల్యం ఎంత శాతం పెరుగుతుంది?",
        ["100%", "125%", "150%", "225%"],
        ["100%", "125%", "150%", "225%"],
        1,
        "Surface area is proportional to r^2. New area = (1.5)^2 = 2.25 times original area. Increase = (2.25 - 1) * 100 = 125%.",
        "వైశాల్యం r^2 కు అనులోమానుపాతంలో ఉండును. నూతన వైశాల్యం = (1.5)^2 = 2.25. పెరుగుదల శాతం = 125%."
    ),
    (
        "A copper sphere of diameter 18 cm is drawn into a wire of diameter 4 mm. Find the length of the wire in meters.",
        "18 సెం.మీ వ్యాసం గల రాగి గోళాన్ని 4 మి.మీ వ్యాసం గల తీగగా మార్చినచో, ఆ తీగ పొడవు మీటర్లలో ఎంత?",
        ["243 meters", "256 meters", "270 meters", "285 meters"],
        ["243 మీటర్లు", "256 మీటర్లు", "270 మీటర్లు", "285 మీటర్లు"],
        0,
        "Volume of sphere = (4/3)π(9^3) = 972π cu.cm. Radius of wire = 2 mm = 0.2 cm. Volume of wire (cylinder) = π * (0.2)^2 * h = 0.04π * h. 0.04π * h = 972π => h = 972 / 0.04 = 24,300 cm = 243 meters.",
        "తీగ ఘనపరిమాణం = గోళ ఘనపరిమాణం. 0.04 * h = 972. h = 24,300 సెం.మీ = 243 మీటర్లు."
    )
]

for idx, mq in enumerate(mensuration_qs):
    q_num = 41 + idx
    new_questions.append(make_q(q_num, 'Arithmetic', 'Mensuration (2D & 3D)', mq[0], mq[1], mq[2], mq[3], mq[4], mq[5], mq[6]))

# Q47-Q50: Retain original Q47-Q50
for i in range(46, 50):
    q = m4_qs[i].copy()
    q['id'] = i + 1
    q['qNumber'] = i + 1
    q['section'] = 'Arithmetic'
    new_questions.append(q)

print(f"Part A complete: {len(new_questions)} questions.")

# -------------------------------------------------------------
# PART B: REASONING & MENTAL ABILITY (Q51 TO Q100)
# -------------------------------------------------------------
for i in range(50, 100):
    q = m4_qs[i].copy()
    q['id'] = i + 1
    q['qNumber'] = i + 1
    q['section'] = 'Reasoning'
    new_questions.append(q)

print(f"Part B complete: {len(new_questions)} questions.")

# -------------------------------------------------------------
# PART C: GENERAL STUDIES (Q101 TO Q200) - 100 BALANCED QUESTIONS
# -------------------------------------------------------------

# 1. General Science & Everyday Technology (Q101-Q114) - 14 Qs
science_qs = [
    (
        "Which law of physics explains the working principle of hydraulic brakes used in automobiles?",
        "ఆటోమొబైల్స్‌లో ఉపయోగించే హైడ్రాలిక్ బ్రేక్‌ల పనితీరు సూత్రాన్ని వివరించే భౌతికశాస్త్ర నియమం ఏది?",
        ["Bernoulli's Principle", "Pascal's Law", "Archimedes' Principle", "Hooke's Law"],
        ["బెర్నౌలీ సూత్రం", "పాస్కల్ నియమం", "ఆర్కిమెడిస్ సూత్రం", "హుక్స్ నియమం"],
        1,
        "Pascal's law states that pressure exerted anywhere in a confined incompressible fluid is transmitted equally in all directions, which is the basis of hydraulic lifts and brakes.",
        "నిర్బంధిత ద్రవంపై కలుగజేసిన పీడనం అన్ని దిశలలో సమానంగా ప్రసరిస్తుందని తెలిపే పాస్కల్ నియమం ఆధారంగా హైడ్రాలిక్ బ్రేకులు పనిచేస్తాయి."
    ),
    (
        "Why does a diamond sparkle brilliantly when light enters it?",
        "వజ్రం లోపలికి కాంతి ప్రవేశించినప్పుడు అది మిరుమిట్లు గొలిపేలా ప్రకాశించడానికి కారణం ఏమిటి?",
        ["Total Internal Reflection due to very small critical angle", "Refraction with zero dispersion", "Scattering of light by carbon atoms", "Complete absorption of infrared rays"],
        ["తక్కువ సందిగ్ధ కోణం వల్ల జరిగే సంపూర్ణాంతర పరావర్తనం", "విక్షేపణం లేని వక్రీభవనం", "కార్బన్ పరమాణువుల కాంతి పరిక్షేపణం", "పరారుణ కిరణాల పూర్తి శోషణం"],
        0,
        "Diamond has a very high refractive index (2.42) and small critical angle (~24.4°). Light entering suffers multiple total internal reflections before emerging.",
        "వజ్రం వక్రీభవన గుణకం (2.42) ఎక్కువ మరియు సందిగ్ధ కోణం (24.4°) తక్కువ కావడం వలన సంపూర్ణాంతర పరావర్తనం చెంది ప్రకాశిస్తుంది."
    ),
    (
        "Which gas is evolved when baking soda (sodium hydrogen carbonate) reacts with an acid or is heated during baking?",
        "బేకింగ్ సోడా (సోడియం హైడ్రోజన్ కార్బోనేట్) ఆమ్లంతో చర్య జరిపినప్పుడు లేదా వేడి చేసినప్పుడు వెలువడే వాయువు ఏది?",
        ["Oxygen (O2)", "Carbon dioxide (CO2)", "Hydrogen (H2)", "Nitrogen dioxide (NO2)"],
        ["ఆక్సిజన్ (O2)", "కార్బన్ డయాక్సైడ్ (CO2)", "హైడ్రోజన్ (H2)", "నైట్రోజన్ డయాక్సైడ్ (NO2)"],
        1,
        "2 NaHCO3 -> Na2CO3 + H2O + CO2. The released carbon dioxide gas causes cakes and dough to rise and become spongy.",
        "బేకింగ్ సోడాను వేడి చేసినప్పుడు విడుదలయ్యే కార్బన్ డయాక్సైడ్ (CO2) వాయువు వల్ల కేకులు, పిండి పదార్థాలు పొంగి మృదువుగా మారతాయి."
    ),
    (
        "Which metal is the best conductor of electricity at standard room temperature?",
        "గది ఉష్ణోగ్రత వద్ద అత్యధిక విద్యుత్ వాహకతను ప్రదర్శించే లోహం ఏది?",
        ["Copper (Cu)", "Silver (Ag)", "Gold (Au)", "Aluminium (Al)"],
        ["రాగి (Cu)", "వెండి (Ag)", "బంగారం (Au)", "అల్యూమినియం (Al)"],
        1,
        "Silver (Ag) has the highest electrical conductivity and thermal conductivity among all metals, followed by copper.",
        "లోహాలన్నింటిలో వెండి అత్యధిక విద్యుత్ మరియు ఉష్ణ వాహకతను కలిగి ఉంటుంది, దీని తర్వాత రాగి ఉంటుంది."
    ),
    (
        "Which chemical compound is commonly known as 'Plaster of Paris'?",
        "రసాయన శాస్త్రంలో దేనిని 'ప్లాస్టర్ ఆఫ్ ప్యారిస్' అని పిలుస్తారు?",
        ["Calcium sulphate dihydrate (CaSO4 · 2H2O)", "Calcium sulphate hemihydrate (CaSO4 · 1/2 H2O)", "Calcium carbonate (CaCO3)", "Magnesium sulphate heptahydrate (MgSO4 · 7H2O)"],
        ["కాల్షియం సల్ఫేట్ డైహైడ్రేట్", "కాల్షియం సల్ఫేట్ హెమీహైడ్రేట్ (CaSO4 · 1/2 H2O)", "కాల్షియం కార్బోనేట్", "మెగ్నీషియం సల్ఫేట్ హెప్టాహైడ్రేట్"],
        1,
        "Plaster of Paris is calcium sulphate hemihydrate (CaSO4 · 1/2 H2O), produced by heating gypsum (CaSO4 · 2H2O) to 373 K.",
        "జిప్సంను 373 K వద్ద వేడి చేసినప్పుడు ఏర్పడే కాల్షియం సల్ఫేట్ హెమీహైడ్రేట్ ను ప్లాస్టర్ ఆఫ్ ప్యారిస్ అంటారు."
    ),
    (
        "Which organelle in a plant cell contains green chlorophyll pigments responsible for capturing light energy during photosynthesis?",
        "మొక్కల కణాలలో కిరణజన్య సంయోగక్రియకు అవసరమైన కాంతి శక్తిని గ్రహించే క్లోరోఫిల్ వర్ణద్రవ్యాన్ని కలిగి ఉండే కణాంగం ఏది?",
        ["Mitochondria", "Chloroplast", "Golgi apparatus", "Ribosome"],
        ["మైటోకాండ్రియా", "హరితరేణువు (క్లోరోప్లాస్ట్)", "గాల్జీ సంక్లిష్టం", "రైబోజోమ్"],
        1,
        "Chloroplasts are double-membrane organelles containing thylakoids and chlorophyll where photosynthesis takes place.",
        "కిరణజన్య సంయోగక్రియ హరితరేణువులలోని థైలకాయిడ్ పొరలలో క్లోరోఫిల్ సమక్షంలో జరుగుతుంది."
    ),
    (
        "Deficiency of which vitamin causes the bleeding gums and delayed wound healing condition known as 'Scurvy'?",
        "ఏ విటమిన్ లోపం వలన చిగుళ్ళ నుండి రక్తం కారడం, గాయాలు మానకపోవడం వంటి లక్షణాలు గల 'స్కర్వీ' వ్యాధి వస్తుంది?",
        ["Vitamin A (Retinol)", "Vitamin B1 (Thiamine)", "Vitamin C (Ascorbic Acid)", "Vitamin D (Calciferol)"],
        ["విటమిన్ A", "విటమిన్ B1", "విటమిన్ C (ఆస్కార్బిక్ ఆమ్లం)", "విటమిన్ D"],
        2,
        "Scurvy is caused by deficiency of Vitamin C (Ascorbic Acid), which is essential for collagen synthesis.",
        "కొల్లాజెన్ సంశ్లేషణకు అవసరమైన విటమిన్ C (ఆస్కార్బిక్ ఆమ్లం) లోపం వల్ల స్కర్వీ వ్యాధి కలుగుతుంది."
    ),
    (
        "Which endocrine gland located at the base of the brain is often designated as the 'Master Gland' of the human body?",
        "మెదడు అడుగుభాగంలో ఉండి, ఇతర అనేక వినాళ గ్రంథుల పనితీరును నియంత్రించడం వల్ల 'మాస్టర్ గ్లాండ్' (ప్రధాన గ్రంథి) అని పిలువబడే గ్రంథి ఏది?",
        ["Thyroid gland", "Pituitary gland", "Adrenal gland", "Pancreas"],
        ["థైరాయిడ్ గ్రంథి", "పీయూష గ్రంథి (పిట్యూటరీ)", "అధివృక్క గ్రంథి (అడ్రినల్)", "క్లోమం"],
        1,
        "The pituitary gland secretes tropic hormones that regulate thyroid, adrenals, and gonads, earning the title Master Gland.",
        "పీయూష గ్రంథి విడుదల చేసే హార్మోన్లు ఇతర గ్రంథుల స్రావాలను నియంత్రిస్తాయి కాబట్టి దీనిని ప్రధాన గ్రంథి అంటారు."
    ),
    (
        "Which instrument is used in automobiles to measure and display the instantaneous travel speed of the vehicle?",
        "మోటారు వాహనాలలో వాహనం యొక్క తక్షణ వేగాన్ని కొలవడానికి మరియు ప్రదర్శించడానికి ఉపయోగించే పరికరం ఏది?",
        ["Odometer", "Speedometer", "Tachometer", "Anemometer"],
        ["ఓడోమీటర్", "స్పీడోమీటర్", "టాకోమీటర్", "అనెమోమీటర్"],
        1,
        "Speedometer measures instantaneous speed in km/h. Odometer records cumulative distance travelled.",
        "స్పీడోమీటర్ తక్షణ వేగాన్ని కొలుస్తుంది. ఓడోమీటర్ ప్రయాణించిన మొత్తం దూరాన్ని రికార్డు చేస్తుంది."
    ),
    (
        "What type of mirror is utilized as the driver's side rearview mirror in motor vehicles to provide a wider field of view?",
        "మోటారు వాహనాలలో డ్రైవర్‌కు విశాలమైన వెనుక దృశ్యాన్ని అందించడానికి ఉపయోగించే దర్పణం ఏది?",
        ["Concave mirror", "Convex mirror", "Plane mirror", "Cylindrical mirror"],
        ["పుటాకార దర్పణం", "కుంభాకార దర్పణం (Convex mirror)", "సమతల దర్పణం", "స్థూపాకార దర్పణం"],
        1,
        "Convex mirrors always produce erect and diminished virtual images, providing a much wider field of view for motorists.",
        "కుంభాకార దర్పణాలు ఎల్లప్పుడూ నిటారైన, చిన్నదైన మిథ్యా ప్రతిబింబాలను ఏర్పరచి విస్తృత దృశ్యాన్ని అందిస్తాయి."
    ),
    (
        "Which indigenous multi-barrel rocket launcher system was developed by the Defence Research and Development Organisation (DRDO)?",
        "భారత రక్షణ పరిశోధన మరియు అభివృద్ధి సంస్థ (DRDO) చే అభివృద్ధి చేయబడిన స్వదేశీ మల్టీ-బారెల్ రాకెట్ లాంచర్ వ్యవస్థ ఏది?",
        ["Pinaka", "Dhanush", "BrahMos", "Akash"],
        ["పినాక (Pinaka)", "ధనుష్", "బ్రహ్మోస్", "ఆకాశ్"],
        0,
        "Pinaka is a multi-barrel rocket launcher (MBRL) system developed by DRDO for the Indian Army.",
        "పినాక అనేది భారత సైన్యం కోసం DRDO రూపొందించిన అత్యాధునిక మల్టీ-బారెల్ రాకెట్ లాంచర్ వ్యవస్థ."
    ),
    (
        "India's premier solar observatory space mission placed at the Sun-Earth Lagrange Point 1 (L1) was launched under which mission name by ISRO?",
        "సూర్యుడిని నిరంతరం పరిశీలించడానికి ఇస్రో (ISRO) భూమి-సూర్యుని లగ్రాంజ్ పాయింట్-1 (L1) వద్ద ప్రవేశపెట్టిన భారతదేశ తొలి సౌర అబ్జర్వేటరీ మిషన్ ఏది?",
        ["Aditya-L1", "Surya-1", "Chandrayaan-3", "XPoSat"],
        ["ఆదిత్య-L1 (Aditya-L1)", "సూర్య-1", "చంద్రయాన్-3", "ఎక్స్‌పోశాట్ (XPoSat)"],
        0,
        "Aditya-L1 was successfully placed into a halo orbit around L1 to study coronal heating and solar flares.",
        "సూర్యుని కరోనా, సౌర తుఫానులను అధ్యయనం చేయడానికి ఇస్రో ఆదిత్య-L1 ఉపగ్రహాన్ని ప్రయోగించింది."
    ),
    (
        "Which vector transmits the pathogen responsible for Malaria in humans?",
        "మానవులలో మలేరియా వ్యాధిని కలిగించే ప్లాస్మోడియం పరాన్నజీవిని వ్యాప్తి చేసే వాహకం ఏది?",
        ["Female Anopheles mosquito", "Female Aedes aegypti mosquito", "Female Culex mosquito", "Tsetse fly"],
        ["ఆడ అనాఫిలిస్ దోమ", "ఆడ ఈడిస్ ఈజిప్టి దోమ", "ఆడ క్యూలెక్స్ దోమ", "ట్సేట్సే ఈగ"],
        0,
        "Female Anopheles mosquito transmits the protozoan parasite Plasmodium vivax / falciparum causing malaria.",
        "మలేరియా ప్లాస్మోడియం అనే ప్రోటోజోవన్ వల్ల కలుగుతుంది మరియు ఇది ఆడ అనాఫిలిస్ దోమ ద్వారా వ్యాపిస్తుంది."
    ),
    (
        "Which radioactive isotope is widely utilized in clinical medicine for the diagnosis and therapeutic treatment of thyroid gland disorders?",
        "వైద్యరంగంలో థైరాయిడ్ గ్రంథి వ్యాధుల నిర్ధారణ మరియు చికిత్సలో విస్తృతంగా ఉపయోగించే రేడియోధార్మిక ఐసోటోప్ ఏది?",
        ["Cobalt-60", "Iodine-131", "Carbon-14", "Sodium-24"],
        ["కోబాల్ట్-60", "అయోడిన్-131 (Iodine-131)", "కార్బన్-14", "సోడియం-24"],
        1,
        "Iodine-131 is used in medicine to diagnose and treat hyperthyroidism and thyroid cancer.",
        "థైరాయిడ్ గ్రంథి లోపాలు మరియు క్యాన్సర్ చికిత్సలో రేడియోధార్మిక అయోడిన్-131 ను ఉపయోగిస్తారు."
    )
]

for idx, sq in enumerate(science_qs):
    q_num = 101 + idx
    new_questions.append(make_q(q_num, 'General Studies', 'General Science & Everyday Technology', sq[0], sq[1], sq[2], sq[3], sq[4], sq[5], sq[6]))

# 2. Current Affairs & Contemporary Issues (Q115-Q130) - 16 Qs
ca_qs = [
    (
        """Consider the following statements regarding the 24th Meeting of the Council of Heads of State of the Shanghai Cooperation Organisation (SCO) held in 2024:
1. The summit was hosted in Astana under the presidency of Kazakhstan.
2. Belarus was formally admitted as the 10th full member state of the SCO during this summit.
3. The official motto was 'Strengthening Multilateral Dialogue — Striving for Sustainable Peace and Prosperity'.
Which of the statements given above is/are correct?""",
        """2024 లో జరిగిన షాంఘై సహకార సంస్థ (SCO) శిఖరాగ్ర సదస్సుకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:
1. ఈ సదస్సు కజకిస్తాన్ అధ్యక్షతన అస్తానా నగరంలో జరిగింది.
2. ఈ సదస్సులోనే బెలారస్ దేశం SCO లో 10వ పూర్తి స్థాయి సభ్య దేశంగా చేరింది.
3. ఈ సదస్సు నినాదం 'బహుళపక్ష సంభాషణను బలోపేతం చేయడం — స్థిరమైన శాంతి మరియు శ్రేయస్సు కోసం కృషి చేయడం'.
పై ప్రకటనలలో ఏది/వి సరైనది/వి?""",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct regarding the 2024 SCO summit in Astana, Kazakhstan, where Belarus became the 10th member.",
        "అస్తానాలో జరిగిన 2024 SCO సదస్సుకు సంబంధించి మూడు ప్రకటనలూ సరైనవి (బెలారస్ 10వ సభ్య దేశంగా చేరింది)."
    ),
    (
        "Who was awarded the highest civilian honour of India, the Bharat Ratna, posthumously in 2024 for his lifelong championship of farmers' rights?",
        "రైతుల హక్కుల కోసం జీవితాంతం పోరాడినందుకు గాను 2024 లో మరణానంతరం భారత రత్న పురస్కారంతో గౌరవించబడిన మాజీ ప్రధానమంత్రి ఎవరు?",
        ["Chaudhary Charan Singh", "P.V. Narasimha Rao", "M.S. Swaminathan", "Karpoori Thakur"],
        ["చౌదరి చరణ్ సింగ్", "పి.వి. నరసింహారావు", "ఎం.ఎస్. స్వామినాథన్", "కర్పూరి ఠాకూర్"],
        0,
        "Chaudhary Charan Singh, former Prime Minister and champion of agricultural peasants, was conferred the Bharat Ratna in 2024.",
        "రైతు బాంధవుడు, మాజీ ప్రధాని చౌదరి చరణ్ సింగ్ కు 2024లో భారత రత్న పురస్కారం ప్రకటించబడింది."
    ),
    (
        "Which country assumed the G20 Presidency for the year 2024 following India's successful New Delhi G20 Summit?",
        "భారతదేశం 2023 న్యూఢిల్లీ సదస్సు విజయవంతంగా ముగిసిన అనంతరం 2024 లో G20 అధ్యక్ష బాధ్యతలను ఏ దేశం చేపట్టింది?",
        ["South Africa", "Brazil", "Indonesia", "Saudi Arabia"],
        ["దక్షిణాఫ్రికా", "బ్రెజిల్ (Brazil)", "ఇండోనేషియా", "సౌదీ అరేబియా"],
        1,
        "Brazil held the G20 presidency in 2024, hosting the leaders' summit in Rio de Janeiro with the theme 'Building a Just World and a Sustainable Planet'.",
        "2024 లో బ్రెజిల్ G20 అధ్యక్ష బాధ్యతలు చేపట్టి రియో డి జనీరోలో సదస్సును నిర్వహించింది."
    ),
    (
        "The Chief Election Commissioner and other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023 provides for a Selection Committee comprising whom?",
        "ప్రధాన ఎన్నికల కమిషనర్ మరియు ఇతర ఎన్నికల కమిషనర్ల నియామక చట్టం, 2023 ప్రకారం ఎన్నికల కమిషనర్లను ఎంపిక చేసే సెలక్షన్ కమిటీలో సభ్యులు ఎవరు?",
        ["Prime Minister, Chief Justice of India, and Leader of Opposition in Lok Sabha", "Prime Minister, a Union Cabinet Minister nominated by PM, and Leader of Opposition in Lok Sabha", "President of India, Vice President, and Lok Sabha Speaker", "Chief Justice of India, Union Law Minister, and Attorney General of India"],
        ["ప్రధానమంత్రి, భారత ప్రధాన న్యాయమూర్తి (CJI), లోక్‌సభలో ప్రతిపక్ష నాయకుడు", "ప్రధానమంత్రి, ప్రధానిచే నామినేట్ చేయబడిన కేంద్ర కేబినెట్ మంత్రి, లోక్‌సభలో ప్రతిపక్ష నాయకుడు", "భారత రాష్ట్రపతి, ఉపరాష్ట్రపతి, లోక్‌సభ స్పీకర్", "భారత ప్రధాన న్యాయమూర్తి, కేంద్ర న్యాయశాఖ మంత్రి, అటార్నీ జనరల్"],
        1,
        "Under the 2023 Act, the Selection Committee consists of the PM (Chairperson), a Union Cabinet Minister, and the Leader of Opposition / single largest opposition party in Lok Sabha.",
        "2023 చట్టం ప్రకారం ఎంపిక కమిటీలో ప్రధాని (ఛైర్మన్), ఒక కేంద్ర కేబినెట్ మంత్రి, మరియు లోక్‌సభలోని ప్రతిపక్ష నేత ఉంటారు."
    ),
    (
        "India achieved its best-ever Paralympic performance at the Paris 2024 Paralympic Games by winning how many total medals?",
        "పారిస్ 2024 పారాలింపిక్స్ క్రీడలలో భారతదేశం తన అత్యుత్తమ ప్రదర్శన కనబరుస్తూ మొత్తం ఎన్ని పతకాలను గెలుచుకుంది?",
        ["19 medals", "24 medals", "29 medals", "32 medals"],
        ["19 పతకాలు", "24 పతకాలు", "29 పతకాలు", "32 పతకాలు"],
        2,
        "India won a record 29 medals (7 Gold, 9 Silver, 13 Bronze) finishing 18th in the medal tally at the Paris 2024 Paralympics.",
        "పారిస్ 2024 పారాలింపిక్స్‌లో భారతదేశం రికార్డు స్థాయిలో 29 పతకాలు (7 స్వర్ణాలు, 9 రజతాలు, 13 కాంస్యాలు) సాధించింది."
    ),
    (
        "Which Indian shooter made history by winning two Olympic bronze medals at a single edition of the Olympic Games (Paris 2024)?",
        "ఒకే ఒలింపిక్ క్రీడలలో (పారిస్ 2024) రెండు కాంస్య పతకాలు గెలుచుకుని చరిత్ర సృష్టించిన భారతీయ షూటర్ ఎవరు?",
        ["Manu Bhaker", "Sarabjot Singh", "Swapnil Kusale", "Avani Lekhara"],
        ["మను భాకర్ (Manu Bhaker)", "సరబ్‌జోత్ సింగ్", "స్వప్నిల్ కుసాలే", "అవని లేఖరా"],
        0,
        "Manu Bhaker won bronze in women's 10m air pistol and another bronze with Sarabjot Singh in mixed team 10m air pistol.",
        "మను భాకర్ 10 మీటర్ల ఎయిర్ పిస్టల్ వ్యక్తిగత మరియు మిశ్రమ విభాగాలలో రెండు కాంస్య పతకాలు సాధించారు."
    ),
    (
        "Who was sworn in as the 51st Chief Justice of India (CJI) in November 2024 succeeding Justice D.Y. Chandrachud?",
        "జస్టిస్ డి.వై. చంద్రచూడ్ పదవీ విరమణ అనంతరం నవంబర్ 2024 లో భారతదేశ 51వ ప్రధాన న్యాయమూర్తిగా (CJI) ప్రమాణ స్వీకారం చేసినది ఎవరు?",
        ["Justice Sanjiv Khanna", "Justice B.R. Gavai", "Justice Surya Kant", "Justice Vikram Nath"],
        ["జస్టిస్ సంజీవ్ ఖన్నా", "జస్టిస్ బి.ఆర్. గవాయ్", "జస్టిస్ సూర్యకాంత్", "జస్టిస్ విక్రమ్ నాథ్"],
        0,
        "Justice Sanjiv Khanna took oath as the 51st Chief Justice of India on 11 November 2024.",
        "11 నవంబర్ 2024న జస్టిస్ సంజీవ్ ఖన్నా భారత 51వ ప్రధాన న్యాయమూర్తిగా బాధ్యతలు చేపట్టారు."
    ),
    (
        "The High Court of Telangana made historic news by establishing the state's first fully paperless e-Court bench in which location?",
        "తెలంగాణ హైకోర్టు రాష్ట్రంలోనే మొట్టమొదటి పూర్తి స్థాయి పేపర్‌లెస్ డిజిటల్ కోర్టు బెంచ్‌ను ఎక్కడ ప్రారంభించింది?",
        ["Hyderabad", "Warangal", "Nizamabad", "Khammam"],
        ["హైదరాబాద్", "వరంగల్", "నిజామాబాద్", "ఖమ్మం"],
        0,
        "Telangana High Court inaugurated its first paperless virtual bench in Hyderabad to accelerate digitized justice delivery.",
        "తెలంగాణ హైకోర్టు హైదరాబాద్ ప్రాంగణంలో తొలి పేపర్‌లెస్ డిజిటల్ కోర్టును ప్రారంభించింది."
    ),
    (
        "Which country became the first nation in the world to pass a nationwide legislation prohibiting social media access for children under 16 years of age?",
        "16 సంవత్సరాల కంటే తక్కువ వయస్సు ఉన్న పిల్లలకు సోషల్ మీడియాను పూర్తిగా నిషేధిస్తూ దేశవ్యాప్త చట్టాన్ని ఆమోదించిన ప్రపంచంలోనే మొదటి దేశం ఏది?",
        ["Australia", "United Kingdom", "France", "Canada"],
        ["ఆస్ట్రేలియా (Australia)", "యునైటెడ్ కింగ్‌డమ్", "ఫ్రాన్స్", "కెనడా"],
        0,
        "In late 2024, Australia enacted historic legislation banning social media platforms for minors under 16 years of age.",
        "ఆస్ట్రేలియా ప్రభుత్వం 16 ఏళ్ల లోపు పిల్లలకు సోషల్ మీడియా ఖాతాలను నిషేధిస్తూ చట్టం చేసింది."
    ),
    (
        "The indigenously built Nuclear-Powered Ballistic Missile Submarine (SSBN) commissioned into the Indian Navy at Visakhapatnam in August 2024 is named:",
        "ఆగస్టు 2024 లో విశాఖపట్నంలో భారత నౌకాదళంలోకి ప్రవేశపెట్టబడిన రెండవ స్వదేశీ అణుశక్తి ఆధారిత బాలిస్టిక్ క్షిపణి జలాంతర్గామి (SSBN) ఏది?",
        ["INS Arihant", "INS Arighaat", "INS Kalvari", "INS Vikrant"],
        ["ఐఎన్ఎస్ అరిహంత్", "ఐఎన్ఎస్ అరిఘాత్ (INS Arighaat)", "ఐఎన్ఎస్ కల్వరి", "ఐఎన్ఎస్ విక్రాంత్"],
        1,
        "INS Arighaat (SSBN S3) was commissioned into the Indian Navy at Visakhapatnam, strengthening India's nuclear triad deterrence.",
        "భారత అణ్వాయుధ త్రయంను బలోపేతం చేస్తూ రెండవ అణు జలాంతర్గామి INS అరిఘాత్ నౌకాదళంలో చేరింది."
    ),
    (
        "The 'Operation Crack Down' initiative launched by the Government of Telangana was instituted primarily to eliminate:",
        "తెలంగాణ ప్రభుత్వం చేపట్టిన 'ఆపరేషన్ క్రాక్ డౌన్' ప్రధానంగా దేని నిర్మూలనకు ఉద్దేశించబడింది?",
        ["Spurious and adulterated agricultural seeds, fertilizers, and fake pesticides", "Unregistered commercial real estate layouts", "Illegal liquor sales during festive periods", "Unlicensed money lending institutions"],
        ["నకిలీ విత్తనాలు, కల్తీ ఎరువులు మరియు నకిలీ పురుగుమందులు", "రిజిస్ట్రేషన్ లేని రియల్ ఎస్టేట్ లేఅవుట్లు", "పండుగల సమయాలలో అక్రమ మద్యం అమ్మకాలు", "లైసెన్స్ లేని ప్రైవేట్ వడ్డీ వ్యాపారం"],
        0,
        "Operation Crack Down targets manufacturers, distributors, and dealers of spurious seeds and adulterated agro-chemicals to protect farmers.",
        "రైతులను కాపాడేందుకు నకిలీ విత్తనాలు, ఎరువుల తయారీదారులపై తెలంగాణ ప్రభుత్వం 'ఆపరేషన్ క్రాక్ డౌన్' చేపట్టింది."
    ),
    (
        "Asia's largest biennial civil aviation conclave and flying display 'Wings India 2024' was hosted at which venue in Telangana?",
        "ఆసియాలోనే అతిపెద్ద ద్వైవార్షిక పౌర విమానయాన ప్రదర్శన 'వింగ్స్ ఇండియా 2024' తెలంగాణలోని ఏ వేదికపై జరిగింది?",
        ["Rajiv Gandhi International Airport, Shamshabad", "Begumpet Airport, Hyderabad", "Hakimpet Air Force Station", "Dundigal Air Force Academy"],
        ["రాజీవ్ గాంధీ అంతర్జాతీయ విమానాశ్రయం, శంషాబాద్", "బేగంపేట విమానాశ్రయం, హైదరాబాద్", "హకీంపేట ఎయిర్ ఫోర్స్ స్టేషన్", "దుండిగల్ ఎయిర్ ఫోర్స్ అకాడమీ"],
        1,
        "Wings India 2024 was organized by the Ministry of Civil Aviation and FICCI at Begumpet Airport, Hyderabad.",
        "బేగంపేట విమానాశ్రయంలో వింగ్స్ ఇండియా 2024 పౌర విమానయాన ప్రదర్శన జరిగింది."
    ),
    (
        "The 'Indiramma Indlu' housing scheme in Telangana sanctions financial assistance of what amount to poor families owning a plot for building a house?",
        "తెలంగాణ ప్రభుత్వం అమలు చేస్తున్న 'ఇందిరమ్మ ఇండ్లు' పథకం క్రింద సొంత స్థలం ఉన్న పేద కుటుంబానికి ఇల్లు నిర్మించుకోవడానికి ఎంత ఆర్థిక సాయం మంజూరు చేస్తారు?",
        ["₹3,00,000", "₹4,00,000", "₹5,00,000", "₹6,00,000"],
        ["₹3,00,000", "₹4,00,000", "₹5,00,000", "₹6,00,000"],
        2,
        "Under Indiramma Indlu scheme, eligible homeless poor owning a plot are provided ₹5 lakh financial assistance in four phases.",
        "ఇందిరమ్మ ఇండ్ల పథకం క్రింద సొంత స్థలం ఉన్న పేదలకు ఇళ్ల నిర్మాణానికి ₹5 లక్షల ఆర్థిక సాయం అందించబడుతుంది."
    ),
    (
        "The 'Young India Skills University' (YISU), established in public-private partnership by the Telangana Government, is located at:",
        "తెలంగాణ ప్రభుత్వం ప్రభుత్వ-ప్రైవేట్ భాగస్వామ్యంతో ఏర్పాటు చేసిన 'యంగ్ ఇండియా స్కిల్స్ యూనివర్సిటీ' ఎక్కడ ఏర్పాటయింది?",
        ["Kandukur, Ranga Reddy district (Mucherla Future City)", "Warangal Urban", "Karimnagar", "Gajwel, Siddipet"],
        ["కందుకూరు, రంగారెడ్డి జిల్లా (ముచ్చర్ల ఫ్యూచర్ సిటీ)", "వరంగల్ అర్బన్", "కరీంనగర్", "గజ్వేల్, సిద్దిపేట"],
        0,
        "Young India Skills University was established at Mucherla in Kandukur mandal of Ranga Reddy district in the Future City.",
        "రంగారెడ్డి జిల్లా కందుకూరు మండలం ముచ్చర్ల ఫ్యూచర్ సిటీలో యంగ్ ఇండియా స్కిల్స్ యూనివర్సిటీ ఏర్పాటయింది."
    ),
    (
        "India's first National Tribal Traditional Healers (Adivasi Vaidyulu) Conclave was inaugurated in which district of Telangana in 2024?",
        "2024 లో భారతదేశపు మొట్టమొదటి జాతీయ గిరిజన సాంప్రదాయ వైద్యుల సమ్మేళనం తెలంగాణలోని ఏ జిల్లాలో ప్రారంభించబడింది?",
        ["Bhadradri Kothagudem", "Mulugu", "Adilabad", "Asifabad Kumuram Bheem"],
        ["భద్రాద్రి కొత్తగూడెం", "ములుగు", "ఆదిలాబాద్", "ఆసిఫాబాద్ కొమురం భీమ్"],
        0,
        "The National Tribal Traditional Healers Conclave was held at Bhadrachalam in Bhadradri Kothagudem district.",
        "భద్రాద్రి కొత్తగూడెం జిల్లా భద్రాచలంలో జాతీయ గిరిజన సాంప్రదాయ వైద్యుల సదస్సు జరిగింది."
    ),
    (
        "Which autonomous authority was constituted by the Government of Telangana under G.O. Ms. No. 99 for disaster management and protection of water bodies in ORR limits?",
        "హైదరాబాద్ ఓఆర్ఆర్ (ORR) పరిధిలోని చెరువులు, ప్రభుత్వ స్థలాల పరిరక్షణ మరియు విపత్తు నిర్వహణ కోసం తెలంగాణ ప్రభుత్వం జీవో 99 ద్వారా ఏర్పాటు చేసిన స్వతంత్ర సంస్థ ఏది?",
        ["HYDRAA (Hyderabad Disaster Response and Assets Monitoring and Protection Authority)", "HMDA Task Force", "GHMC Disaster Cell", "WALMTARI"],
        ["హైడ్రా (HYDRAA)", "హెచ్ఎండిఏ టాస్క్ ఫోర్స్", "జిహెచ్ఎంసి డిజాస్టర్ సెల్", "వాల్మటారి"],
        0,
        "HYDRAA was constituted under the chairmanship of the Chief Minister / Chief Secretary to safeguard lakes and manage disasters in the 2,050 sq.km HMDA area.",
        "హైదరాబాద్ మెట్రోపాలిటన్ పరిధిలోని జలాశయాల పరిరక్షణకు తెలంగాణ ప్రభుత్వం 'హైడ్రా' (HYDRAA) ను ఏర్పాటు చేసింది."
    )
]

for idx, cq in enumerate(ca_qs):
    q_num = 115 + idx
    new_questions.append(make_q(q_num, 'General Studies', 'Current Affairs & Contemporary Issues', cq[0], cq[1], cq[2], cq[3], cq[4], cq[5], cq[6]))

# 3. Geography of India & Telangana (Q131-Q144) - 14 Qs
geography_qs = [
    (
        "Which pass in the Greater Himalayas connects the Kashmir Valley with Leh in the Union Territory of Ladakh?",
        "గ్రేటర్ హిమాలయాలలో ఉన్న ఏ కనుమ కాశ్మీర్ లోయను లడఖ్ కేంద్రపాలిత ప్రాంతంలోని లేహ్‌తో కలుపుతుంది?",
        ["Banihal Pass", "Zoji La Pass", "Rohtang Pass", "Nathu La Pass"],
        ["బనిహాల్ కనుమ", "జోజి లా కనుమ", "రోహ్‌తాంగ్ కనుమ", "నాథు లా కనుమ"],
        1,
        "Zoji La Pass at 3,528 m elevation on National Highway 1 connects Srinagar/Kashmir with Kargil and Leh.",
        "శ్రీనగర్ ను లడఖ్‌లోని లేహ్‌తో కలిపే ముఖ్యమైన హిమాలయ కనుమ జోజి లా."
    ),
    (
        "Which of the following is the largest peninsular river system in India, also known as the 'Dakshin Ganga'?",
        "భారతదేశంలో 'దక్షిణ గంగ' గా ప్రసిద్ధి చెందిన అతిపెద్ద ద్వీపకల్ప నదీ వ్యవస్థ ఏది?",
        ["Krishna River", "Godavari River", "Cauvery River", "Narmada River"],
        ["కృష్ణా నది", "గోదావరి నది", "కావేరి నది", "నర్మదా నది"],
        1,
        "Godavari River (length 1,465 km), originating at Trimbakeshwar in Maharashtra, is the largest peninsular river.",
        "మహారాష్ట్రలోని త్రయంబకేశ్వర్ వద్ద జన్మించే గోదావరి నది (1,465 కి.మీ) ద్వీపకల్ప భారతదేశంలో అతిపెద్ద నది."
    ),
    (
        "The black cotton soils (Regur soils) of the Deccan Plateau in India are most suited for the cultivation of which commercial crop?",
        "దక్కన్ పీఠభూమిలోని నల్లరేగడి నేలలు (రెగూర్ నేలలు) క్రింది ఏ వాణిజ్య పంట సాగుకు అత్యంత అనుకూలమైనవి?",
        ["Jute", "Cotton", "Tea", "Rubber"],
        ["జనపనార", "పత్తి (Cotton)", "టీ", "రబ్బరు"],
        1,
        "Regur soils derived from basaltic lava are clayey, highly moisture-retentive, and ideal for cotton cultivation.",
        "లావా శిలల వల్ల ఏర్పడిన నల్లరేగడి నేలలు తేమను నిల్వ ఉంచే గుణాన్ని కలిగి ఉండి పత్తి పంటకు అత్యంత అనుకూలం."
    ),
    (
        "Which of the following tiger reserves in Telangana is located across the Nallamala forest range?",
        "తెలంగాణలో నల్లమల అటవీ ప్రాంతంలో విస్తరించి ఉన్న ప్రముఖ పులుల సంరక్షణ కేంద్రం (టైగర్ రిజర్వ్) ఏది?",
        ["Kawal Tiger Reserve", "Amrabad Tiger Reserve", "Pakhal Wildlife Sanctuary", "Eturnagaram Sanctuary"],
        ["కవ్వాల్ టైగర్ రిజర్వ్", "అమ్రాబాద్ టైగర్ రిజర్వ్", "పాకాల అభయారణ్యం", "ఏటూరునాగారం అభయారణ్యం"],
        1,
        "Amrabad Tiger Reserve covers the southern Nallamala forests across Nagarkurnool and Nalgonda districts.",
        "నాగర్‌కర్నూల్ మరియు నల్గొండ జిల్లాల్లోని నల్లమల అటవీ ప్రాంతంలో అమ్రాబాద్ టైగర్ రిజర్వ్ విస్తరించి ఉంది."
    ),
    (
        "Singareni Collieries Company Limited (SCCL) extracts coal primarily from which geological rift valley in Telangana?",
        "సింగరేణి బొగ్గు గనుల సంస్థ (SCCL) తెలంగాణలోని ఏ నదీ లోయ పరివాహక ప్రాంతం నుండి బొగ్గును వెలికితీస్తుంది?",
        ["Krishna Valley", "Pranahita-Godavari Valley", "Bhima Valley", "Musi Valley"],
        ["కృష్ణా లోయ", "ప్రాణహిత-గోదావరి లోయ", "భీమా లోయ", "మూసీ లోయ"],
        1,
        "The Gondwana coal deposits of Telangana are located along the Pranahita-Godavari rift basin stretching across Adilabad, Mancherial, Peddapalli, Bhupalpally, and Kothagudem.",
        "తెలంగాణలోని గోండ్వానా బొగ్గు నిల్వలు ప్రాణహిత-గోదావరి లోయ పరివాహక ప్రాంతంలో విస్తరించి ఉన్నాయి."
    ),
    (
        "At which location does the Godavari river enter the state of Telangana from Maharashtra?",
        "గోదావరి నది మహారాష్ట్ర నుండి తెలంగాణ రాష్ట్రంలోకి ఏ ప్రాంతం వద్ద ప్రవేశిస్తుంది?",
        ["Basara (Nirmal district)", "Kandakurthi (Nizamabad district)", "Kaleshwaram (Bhupalpally district)", "Dharmapuri (Jagtial district)"],
        ["బాసర (నిర్మల్ జిల్లా)", "కందకుర్తి (నిజామాబాద్ జిల్లా)", "కాళేశ్వరం (భూపాలపల్లి జిల్లా)", "ధర్మపురి (జగిత్యాల జిల్లా)"],
        1,
        "Godavari enters Telangana at Kandakurthi in Renjal mandal of Nizamabad district, forming a Triveni Sangam with Manjeera and Haridra.",
        "గోదావరి నది నిజామాబాద్ జిల్లా కందకుర్తి వద్ద తెలంగాణలోకి ప్రవేశిస్తుంది (గోదావరి, మంజీర, హరిద్ర త్రివేణి సంగమం)."
    ),
    (
        "Which major tributary of the Krishna river flows through the historic capital city of Hyderabad?",
        "కృష్ణా నది యొక్క ఏ ముఖ్యమైన ఉపనది చారిత్రక రాజధాని నగరమైన హైదరాబాద్ గుండా ప్రవహిస్తుంది?",
        ["Dindi", "Musi", "Paleru", "Munneru"],
        ["దిండి", "మూసీ నది", "పాలేరు", "మున్నేరు"],
        1,
        "River Musi originates in the Ananthagiri Hills of Vikarabad district and flows through Hyderabad before joining River Krishna at Vadapally.",
        "వికారాబాద్ జిల్లా అనంతగిరి కొండల్లో పుట్టే మూసీ నది హైదరాబాద్ నగరం గుండా ప్రవహించి వాడపల్లి వద్ద కృష్ణాలో కలుస్తుంది."
    ),
    (
        "What is the total number of administrative revenue districts in the State of Telangana?",
        "తెలంగాణ రాష్ట్రంలో గల మొత్తం పరిపాలనా రెవెన్యూ జిల్లాల సంఖ్య ఎంత?",
        ["31 districts", "33 districts", "35 districts", "36 districts"],
        ["31 జిల్లాలు", "33 జిల్లాలు", "35 జిల్లాలు", "36 జిల్లాలు"],
        1,
        "Following the reorganization of districts in 2016 and 2019 (creation of Mulugu and Narayanpet), Telangana has 33 districts.",
        "ములుగు మరియు నారాయణపేట ఏర్పాటుతో తెలంగాణలోని మొత్తం జిల్లాల సంఖ్య 33 కు చేరింది."
    ),
    (
        "The highest peak in the South Peninsular India, Anamudi (2,695 m), is situated in which mountain range?",
        "దక్షిణ భారతదేశంలోనే అత్యంత ఎత్తైన శిఖరమైన అనైముడి (2,695 మీ) ఏ కొండలలో ఉంది?",
        ["Nilgiri Hills", "Anaimalai Hills", "Cardamom Hills", "Javadi Hills"],
        ["నీలగిరి కొండలు", "ఆనైమలై కొండలు (Anaimalai Hills)", "ఏలకుల కొండలు (కార్డమం)", "జవాది కొండలు"],
        1,
        "Anamudi (2,695 m) in Kerala is located in the Anaimalai Hills of the Western Ghats.",
        "పశ్చిమ కనుమలలోని ఆనైమలై కొండలలో దక్షిణ భారతదేశంలోకెల్లా ఎత్తైన అనైముడి శిఖరం ఉంది."
    ),
    (
        "Which multi-stage lift irrigation project on the Godavari river in Telangana features the world's longest underground irrigation tunnel?",
        "తెలంగాణలోని గోదావరి నదిపై నిర్మించబడిన ఏ ఎత్తిపోతల పథకం ప్రపంచంలోనే అత్యంత పొడవైన భూగర్భ నీటిపారుదల సొరంగాన్ని కలిగి ఉంది?",
        ["Kaleshwaram Lift Irrigation Project (KLIP)", "Devadula Lift Irrigation Project", "Palamuru-Rangareddy Lift Irrigation Project", "Sitarama Lift Irrigation Project"],
        ["కాళేశ్వరం ఎత్తిపోతల పథకం (KLIP)", "దేవాదుల ఎత్తిపోతల పథకం", "పాలమూరు-రంగారెడ్డి ఎత్తిపోతల పథకం", "సీతారామ ఎత్తిపోతల పథకం"],
        0,
        "Kaleshwaram Project includes underground surge pools and a 203 km tunnel network including the 21 km Package 8 tunnel.",
        "గోదావరి నదిపై నిర్మించిన కాళేశ్వరం ఎత్తిపోతల ప్రాజెక్టులో భారీ భూగర్భ సొరంగాలు మరియు పంపింగ్ కేంద్రాలు ఉన్నాయి."
    ),
    (
        "The 'Pakhal Lake' (పాకాల సరస్సు), an engineering marvel of medieval irrigation, was constructed during the reign of which Kakatiya monarch?",
        "మధ్యయుగ నీటిపారుదల అద్భుతమైన 'పాకాల సరస్సు' ఏ కాకతీయ చక్రవర్తి పాలనా కాలంలో నిర్మించబడింది?",
        ["Ganapati Deva", "Rudrama Devi", "Prataparudra II", "Prola II"],
        ["గణపతి దేవుడు", "రుద్రమదేవి", "రెండవ ప్రతాపరుద్రుడు", "రెండవ ప్రోలరాజు"],
        0,
        "Pakhal Lake was built in 1213 AD by Jagadala Mummadi, a minister of Kakatiya King Ganapati Deva in Warangal district.",
        "కాకతీయ గణపతి దేవుని మంత్రి జగదల ముమ్మడి క్రీ.శ. 1213 లో పాకాల సరస్సును నిర్మించారు."
    ),
    (
        "Which wind system is primarily responsible for bringing rainfall to the Coromandel coast of Tamil Nadu during October–December?",
        "అక్టోబర్-డిసెంబర్ శీతాకాలంలో తమిళనాడులోని కోరమాండల్ తీరానికి అధిక వర్షపాతాన్ని తెచ్చే పవనాలు ఏవి?",
        ["South-West Monsoon", "North-East Retreating Monsoon", "Western Disturbances", "South-Easterly Trade Winds"],
        ["నైరుతి రుతుపవనాలు", "ఈశాన్య (తిరోగమన) రుతుపవనాలు", "పశ్చిమ అలజడులు", "ఆగ్నేయ వ్యాపార పవనాలు"],
        1,
        "The North-East retreating monsoon picks up moisture from the Bay of Bengal and causes heavy rainfall along Tamil Nadu coast.",
        "బంగాళాఖాతం మీదుగా తేమను గ్రహించి కోరమాండల్ తీరంలో భారీ వర్షాన్ని కురిపించేవి ఈశాన్య తిరోగమన రుతుపవనాలు."
    ),
    (
        "Telangana state does not share land boundaries with which of the following states?",
        "తెలంగాణ రాష్ట్రం క్రింది ఏ రాష్ట్రంతో సరిహద్దును పంచుకోదు?",
        ["Maharashtra", "Karnataka", "Odisha", "Chhattisgarh"],
        ["మహారాష్ట్ర", "కర్ణాటక", "ఒడిశా (Odisha)", "ఛత్తీస్‌గఢ్"],
        2,
        "Telangana shares borders with Maharashtra (north), Karnataka (west), AP (south and east), and Chhattisgarh (northeast). It has no border with Odisha.",
        "తెలంగాణ మహారాష్ట్ర, కర్ణాటక, ఆంధ్రప్రదేశ్, ఛత్తీస్‌గఢ్‌లతో సరిహద్దు కలిగి ఉంది; ఒడిశాతో నేరుగా సరిహద్దు లేదు."
    ),
    (
        "The historic 'Ramappa Lake' was constructed adjacent to the UNESCO World Heritage Ramappa Temple during which century?",
        "యునెస్కో ప్రపంచ వారసత్వ సంపద రామప్ప దేవాలయం సమీపంలో గల చారిత్రక 'రామప్ప సరస్సు' ఏ శతాబ్దంలో నిర్మించబడింది?",
        ["11th Century AD", "13th Century AD", "15th Century AD", "17th Century AD"],
        ["క్రీ.శ. 11వ శతాబ్దం", "క్రీ.శ. 13వ శతాబ్దం (1213 AD)", "క్రీ.శ. 15వ శతాబ్దం", "క్రీ.శ. 17వ శతాబ్దం"],
        1,
        "Ramappa Lake was constructed under Kakatiya ruler Ganapati Deva around 1213 AD (13th Century).",
        "రామప్ప చెరువు క్రీ.శ. 1213 లో (13వ శతాబ్దం) కాకతీయుల కాలంలో నిర్మించబడింది."
    )
]

for idx, gq in enumerate(geography_qs):
    q_num = 131 + idx
    new_questions.append(make_q(q_num, 'General Studies', 'Geography of India & Telangana', gq[0], gq[1], gq[2], gq[3], gq[4], gq[5], gq[6]))

# 4. Indian & Telangana Economy (Q145-Q158) - 14 Qs
economy_qs_m4 = [
    (
        "What is 'Gross State Domestic Product' (GSDP)?",
        "స్థూల రాష్ట్ర దేశీయోత్పత్తి (GSDP) అనగా ఏమిటి?",
        ["Total monetary value of all final goods and services produced within the boundaries of a state in a financial year", "Total revenue collected by the state commercial taxes department", "Net state income after subtracting all central transfers", "Per capita income of all rural workers in the state"],
        ["ఒక ఆర్థిక సంవత్సరంలో రాష్ట్ర భౌగోళిక సరిహద్దుల లోపల ఉత్పత్తి చేయబడిన అన్ని అంతిమ వస్తువులు మరియు సేవల మొత్తం ద్రవ్య విలువ", "రాష్ట్ర వాణిజ్య పన్నుల శాఖ వసూలు చేసిన మొత్తం పన్ను", "కేంద్ర గ్రాంట్లను మినహాయించిన నికర రాష్ట్ర ఆదాయం", "రాష్ట్రంలోని గ్రామీణ శ్రామికుల సగటు తలసరి ఆదాయం"],
        0,
        "GSDP represents the total market value of all final goods and services produced within a state's geographic borders during a financial year.",
        "ఒక నిర్దిష్ట ఆర్థిక సంవత్సరంలో రాష్ట్ర భౌగోళిక సరిహద్దుల్లో ఉత్పత్తి అయిన అన్ని అంతిమ వస్తు సేవల మార్కెట్ విలువను GSDP అంటారు."
    ),
    (
        "Which regulatory authority enforces the Food Safety and Standards Act in India?",
        "భారతదేశంలో ఆహార భద్రత మరియు ప్రమాణాల చట్టాన్ని అమలు చేసే అత్యున్నత నియంత్రణ సంస్థ ఏది?",
        ["FSSAI (Food Safety and Standards Authority of India)", "BIS (Bureau of Indian Standards)", "FCI (Food Corporation of India)", "APEDA"],
        ["ఎఫ్ఎస్ఎస్ఏఐ (FSSAI)", "బిఐఎస్ (BIS)", "ఎఫ్సిఐ (FCI)", "అపెడా (APEDA)"],
        0,
        "FSSAI is the statutory authority under the Ministry of Health and Family Welfare regulating food manufacture, storage, and sales.",
        "భారతదేశంలో ఆహార నాణ్యతా ప్రమాణాలు, భద్రతను పర్యవేక్షించే చట్టబద్ధ సంస్థ FSSAI."
    ),
    (
        "Under the FRBM Act, what is the target ratio of Fiscal Deficit to GDP mandated for the Central Government?",
        "ఎఫ్ఆర్బీఎం (FRBM) చట్టం ప్రకారం కేంద్ర ప్రభుత్వం సాధించాల్సిన ద్రవ్య లోటు-జీడీపీ నిష్పత్తి లక్ష్యం ఎంత?",
        ["2.0% of GDP", "3.0% of GDP", "4.5% of GDP", "5.0% of GDP"],
        ["జీడీపీ లో 2.0%", "జీడీపీ లో 3.0%", "జీడీపీ లో 4.5%", "జీడీపీ లో 5.0%"],
        1,
        "The statutory FRBM benchmark anchor is 3% of GDP for the Central Government fiscal deficit.",
        "కేంద్ర ప్రభుత్వ ద్రవ్య లోటును జీడీపీలో 3% కి పరిమితం చేయాలని FRBM చట్టం నిర్దేశించింది."
    ),
    (
        "The TS-iPASS Act enacted by the Telangana legislature is renowned across India for:",
        "తెలంగాణ శాసనసభ ఆమోదించిన 'టిఎస్-ఐపాస్' (TS-iPASS) చట్టం దేశవ్యాప్తంగా దేనికి ప్రసిద్ధి చెందింది?",
        ["Time-bound statutory right to clearance for setting up industrial enterprises within 15 to 30 days", "Free commercial land allotments to multinational software corporations", "Complete exemption of all industries from labour inspection laws", "Government takeover of sick small scale industrial units"],
        ["పారిశ్రామిక అనుమతులను 15 నుండి 30 రోజులలో పొందే చట్టబద్ధ హక్కును కల్పించుట", "బహుళజాతి కంపెనీలకు ఉచితంగా భూమిని కేటాయించుట", "పరిశ్రమలకు కార్మిక చట్టాల నుండి పూర్తి మినహాయింపునిచ్చుట", "నష్టాల్లో ఉన్న చిన్న పరిశ్రమలను ప్రభుత్వమే స్వాధీనం చేసుకొనుట"],
        0,
        "TS-iPASS provides right to industrial clearances within 15 to 30 days, with self-certification and deemed approval provisions.",
        "పరిశ్రమల స్థాపనకు అవసరమైన అన్ని అనుమతులను 15 నుండి 30 రోజులలోగా పొందే చట్టబద్ధ హక్కును TS-iPASS కల్పించింది."
    ),
    (
        "Which organization computes and releases the official Periodic Labour Force Survey (PLFS) data in India?",
        "భారతదేశంలో అధికారిక ఆవర్తన శ్రామిక శక్తి సర్వే (PLFS) నివేదికలను విడుదల చేసే సంస్థ ఏది?",
        ["National Statistical Office (NSO / MoSPI)", "Labour Bureau, Shimla", "NITI Aayog", "Employees' Provident Fund Organisation (EPFO)"],
        ["నేషనల్ స్టాటిస్టికల్ ఆఫీస్ (NSO)", "లేబర్ బ్యూరో, సిమ్లా", "నీతి ఆయోగ్", "ఈపీఎఫ్ఓ (EPFO)"],
        0,
        "The National Statistical Office (NSO) under the Ministry of Statistics and Programme Implementation (MoSPI) conducts the PLFS.",
        "భారత గణాంక మరియు కార్యక్రమ అమలు మంత్రిత్వ శాఖకు చెందిన నేషనల్ స్టాటిస్టికల్ ఆఫీస్ (NSO) శ్రామిక సర్వేలను నిర్వహిస్తుంది."
    ),
    (
        "What does 'Monetary Policy Stance: Withdrawal of Accommodation' indicate?",
        "ఆర్బీఐ ద్రవ్య విధానంలో 'విత్‌డ్రాయల్ ఆఫ్ అకామడేషన్' (Withdrawal of Accommodation) వైఖరి దేనిని సూచిస్తుంది?",
        ["Gradual reduction of surplus money supply from the economy to combat inflationary pressures", "Immediate devaluation of the Indian Rupee against the US Dollar", "Expansion of unhedged foreign borrowings", "Subsidizing commercial bank home loans"],
        ["ద్రవ్యోల్బణాన్ని అదుపు చేయడానికి మార్కెట్‌లోని అదనపు ద్రవ్య సరఫరాను క్రమంగా తగ్గించడం", "డాలర్‌తో రూపాయి మారకం విలువను తగ్గించడం", "విదేశీ రుణాలను అపరిమితంగా పెంచడం", "బ్యాంకు గృహ రుణాలపై వడ్డీ రాయితీనివ్వడం"],
        0,
        "Withdrawal of accommodation means tightening policy and reining in liquidity to bring inflation back to target.",
        "ద్రవ్యోల్బణ ఒత్తిళ్లను నిరోధించడానికి మార్కెట్ నుండి ద్రవ్యత్వాన్ని తగ్గించే కఠిన ద్రవ్య విధానాన్ని ఇది సూచిస్తుంది."
    ),
    (
        "Which crop is the single largest cultivated crop in Telangana during both Kharif and Rabi seasons?",
        "తెలంగాణలో ఖరీఫ్ మరియు రబీ రెండు సీజన్లలోనూ అత్యధిక విస్తీర్ణంలో సాగయ్యే ప్రధాన పంట ఏది?",
        ["Cotton", "Paddy (Rice)", "Maize", "Red Gram (Pigeon Pea)"],
        ["పత్తి", "వరి (Paddy)", "మొక్కజొన్న", "కందులు"],
        1,
        "Paddy covers the largest gross cropped area in Telangana, with the state emerging as a leading contributor of rice to the central pool.",
        "తెలంగాణలో విస్తారమైన సాగునీటి వనరుల లభ్యత వల్ల వరి అత్యధిక విస్తీర్ణంలో సాగవుతున్న ప్రధాన పంట."
    ),
    (
        "Under the Reserve Bank of India's regulations, what is 'Cash Reserve Ratio' (CRR)?",
        "రిజర్వ్ బ్యాంక్ ఆఫ్ ఇండియా నిబంధనల ప్రకారం 'నగదు నిల్వల నిష్పత్తి' (CRR) అనగా ఏమిటి?",
        ["Share of Net Demand and Time Liabilities (NDTL) that commercial banks must maintain with the RBI as cash balances", "Percentage of gold reserves banks must hold in their own vaults", "Percentage of bank assets invested in government securities", "Minimum capital adequacy ratio required under Basel III norms"],
        ["వాణిజ్య బ్యాంకులు తమ డిపాజిట్లలో (NDTL) నగదు రూపంలో ఆర్బీఐ వద్ద తప్పనిసరిగా ఉంచాల్సిన శాతం", "బ్యాంకులు తమ లాకర్లలో భద్రపరచాల్సిన బంగారు నిల్వల శాతం", "ప్రభుత్వ బాండ్లలో బ్యాంకులు చేయాల్సిన కనీస పెట్టుబడి", "బాసెల్ నిబంధనల క్రింద అవసరమైన మూలధన నిష్పత్తి"],
        0,
        "CRR is the percentage of a bank's total deposits (NDTL) that it is mandated to park with the RBI in cash with no interest.",
        "బ్యాంకులు తమ మొత్తం డిపాజిట్లలో నిర్ణీత శాతాన్ని రిజర్వ్ బ్యాంకు వద్ద నగదు రూపంలో నిల్వ ఉంచడాన్ని CRR అంటారు."
    ),
    (
        "Which public sector bank was formed by the historic merger of Andhra Bank and Corporation Bank in 2020?",
        "2020 లో ఆంధ్ర బ్యాంక్ మరియు కార్పొరేషన్ బ్యాంకులు విలీనం కావడం ద్వారా ఏర్పడిన ప్రభుత్వ రంగ బ్యాంకు ఏది?",
        ["Canara Bank", "Union Bank of India", "Indian Bank", "Punjab National Bank"],
        ["కెనరా బ్యాంక్", "యూనియన్ బ్యాంక్ ఆఫ్ ఇండియా", "ఇండియన్ బ్యాంక్", "పంజాబ్ నేషనల్ బ్యాంక్"],
        1,
        "Andhra Bank and Corporation Bank were merged into Union Bank of India on April 1, 2020.",
        "ఆంధ్ర బ్యాంక్ మరియు కార్పొరేషన్ బ్యాంకులు యూనియన్ బ్యాంక్ ఆఫ్ ఇండియాలో విలీనమయ్యాయి."
    ),
    (
        "What is the maximum loan waiver amount per farmer sanctioned under the Government of Telangana's 2024 Crop Loan Waiver Scheme?",
        "తెలంగాణ ప్రభుత్వం 2024 లో అమలు చేసిన రైతు రుణమాఫీ పథకం క్రింద ఒక్కో రైతు కుటుంబానికి గరిష్టంగా ఎంత మొత్తం రుణమాఫీ చేశారు?",
        ["₹1,00,000", "₹1,50,000", "₹2,00,000", "₹2,50,000"],
        ["₹1,00,000", "₹1,50,000", "₹2,00,000", "₹2,50,000"],
        2,
        "The Telangana Government fulfilled its core guarantee by waiving crop loans up to ₹2,00,000 per farming household in three phases.",
        "తెలంగాణ ప్రభుత్వం రైతులకు ఒక్కొక్కరికి గరిష్టంగా ₹2 లక్షల వరకు పంట రుణాలను మాఫీ చేసింది."
    ),
    (
        "Which index published by the United Nations Development Programme (UNDP) measures deprivations across Health, Education, and Standard of Living?",
        "ఐక్యరాజ్యసమితి అభివృద్ధి కార్యక్రమం (UNDP) ఆరోగ్యం, విద్య, జీవన ప్రమాణం అనే మూడు రంగాలలో పేదరికాన్ని కొలవడానికి ప్రచురించే సూచిక ఏది?",
        ["Human Development Index (HDI)", "Multidimensional Poverty Index (MPI)", "Gender Inequality Index (GII)", "Global Hunger Index (GHI)"],
        ["మానవాభివృద్ధి సూచిక (HDI)", "బహుమితీయ పేదరిక సూచిక (MPI)", "లింగ అసమానతల సూచిక", "గ్లోబల్ హంగర్ ఇండెక్స్"],
        1,
        "Global MPI uses 10 indicators across health, education, and living standards to quantify non-income poverty deprivations.",
        "ఆరోగ్యం, విద్య, జీవన ప్రమాణాలు అనే రంగాలలో ప్రజలు ఎదుర్కొనే లేమిని బహుమితీయ పేదరిక సూచిక (MPI) లెక్కిస్తుంది."
    ),
    (
        "Which autonomous institution promotes and finances rural development and microcredit in India?",
        "భారతదేశంలో గ్రామీణాభివృద్ధి, వ్యవసాయం మరియు సూక్ష్మ రుణాలకు ఆర్థిక సహాయం అందించే అత్యున్నత అభివృద్ధి బ్యాంకు ఏది?",
        ["SIDBI", "NABARD (National Bank for Agriculture and Rural Development)", "EXIM Bank", "NHB"],
        ["సిడ్బి (SIDBI)", "నాబార్డ్ (NABARD)", "ఎగ్జిమ్ బ్యాంక్", "నేషనల్ హౌసింగ్ బ్యాంక్"],
        1,
        "NABARD was established in 1982 under the B. Sivaraman Committee recommendations to finance agriculture and rural infrastructure.",
        "శివరామన్ కమిటీ సిఫార్సుల మేరకు 1982 లో వ్యవసాయ, గ్రామీణాభివృద్ధికి నిధులందించడానికి నాబార్డ్ ఏర్పాటయింది."
    ),
    (
        "Under the Goods and Services Tax (GST) regime, which items remain outside the levy of GST and continue under state excises?",
        "వస్తు సేవల పన్ను (GST) పరిధి నుండి మినహాయించబడి, ఇప్పటికీ రాష్ట్ర ఎక్సైజ్ మరియు వ్యాట్ పరిధిలోనే ఉన్న వస్తువులు ఏవి?",
        ["Alcohol for human consumption and five petroleum products", "Pharmaceutical formulations and medical devices", "Automobiles and auto spare components", "Cotton and synthetic textile garments"],
        ["మానవ వినియోగానికి ఉద్దేశించిన మద్యం మరియు 5 పెట్రోలియం ఉత్పత్తులు", "ఔషధాలు మరియు వైద్య పరికరాలు", "మోటారు వాహనాలు మరియు విడిభాగాలు", "వస్త్రాలు మరియు గార్మెంట్స్"],
        0,
        "Alcohol for human consumption is constitutionally outside GST (under state excise). Crude oil, diesel, petrol, ATF, and natural gas are temporarily outside GST.",
        "మానవ వినియోగ మద్యం మరియు 5 రకాల పెట్రోలియం ఉత్పత్తులు జీఎస్టీ పరిధి బయట ఉండి రాష్ట్రాల పన్నుల పరిధిలోనే ఉన్నాయి."
    ),
    (
        "Which flagship enterprise support program was launched in Telangana to empower Dalit and tribal entrepreneurs through enhanced investment subsidies?",
        "తెలంగాణలో దళిత మరియు గిరిజన పారిశ్రామికవేత్తలను ప్రోత్సహించడానికి ప్రత్యేక రాయితీలతో ప్రారంభించిన పథకం ఏది?",
        ["T-PRIDE (Telangana Program for Rapid Incubation of Dalit Entrepreneurs)", "T-IDEA", "Dalit Bandhu", "WE Hub"],
        ["టి-ప్రైడ్ (T-PRIDE)", "టి-ఐడియా (T-IDEA)", "దళిత బంధు", "వి-హబ్"],
        0,
        "T-PRIDE provides special incentives, power tariff rebates, and capital investment subsidies to SC/ST entrepreneurs.",
        "దళిత, గిరిజన పారిశ్రామికవేత్తలకు పెట్టుబడి రాయితీలు, విద్యుత్ రాయితీలు అందించడానికి T-PRIDE పథకం అమలు చేయబడింది."
    )
]

for idx, eq in enumerate(economy_qs_m4):
    q_num = 145 + idx
    new_questions.append(make_q(q_num, 'General Studies', 'Indian & Telangana Economy', eq[0], eq[1], eq[2], eq[3], eq[4], eq[5], eq[6]))

# 5. Indian Polity & Constitutional Governance (Q159-Q175) - 17 Qs
polity_qs_m4 = [
    (
        "The words 'SOCIALIST, SECULAR, and INTEGRITY' were added to the Preamble of the Indian Constitution by which Constitutional Amendment Act?",
        "భారత రాజ్యాంగ పీఠికకు 'సామ్యవాద, లౌకిక, సమగ్రత' అనే పదాలను ఏ రాజ్యాంగ సవరణ చట్టం ద్వారా చేర్చారు?",
        ["42nd Constitutional Amendment Act, 1976", "44th Constitutional Amendment Act, 1978", "52nd Constitutional Amendment Act, 1985", "86th Constitutional Amendment Act, 2002"],
        ["42వ రాజ్యాంగ సవరణ చట్టం, 1976", "44వ రాజ్యాంగ సవరణ చట్టం, 1978", "52వ రాజ్యాంగ సవరణ చట్టం, 1985", "86వ రాజ్యాంగ సవరణ చట్టం, 2002"],
        0,
        "The 42nd Amendment Act of 1976 amended the Preamble, inserting 'Socialist', 'Secular', and 'Integrity'.",
        "1976 లోని 42వ రాజ్యాంగ సవరణ ద్వారా పీఠికలో సామ్యవాద, లౌకిక మరియు సమగ్రత అనే పదాలను చేర్చారు."
    ),
    (
        "Under Article 32 of the Indian Constitution, which prerogative writ is issued by the Supreme Court to command an authority to perform its mandatory statutory duty?",
        "భారత రాజ్యాంగంలోని అధికరణం 32 ప్రకారం, ఒక ప్రభుత్వ అధికారి తన చట్టబద్ధ కర్తవ్యాన్ని నిర్వహించేలా ఆదేశించడానికి న్యాయస్థానం జారీ చేసే రిట్ ఏది?",
        ["Habeas Corpus", "Mandamus", "Certiorari", "Quo-Warranto"],
        ["హెబియస్ కార్పస్", "మాండమస్ (Mandamus)", "సెర్షియోరరీ", "కో-వారంటో"],
        1,
        "Mandamus ('We Command') is issued to compel a public official or body to perform a public duty that they have refused to execute.",
        "మాండమస్ అనగా 'మేము ఆజ్ఞాపిస్తున్నాము'. ప్రభుత్వ అధికారులు లేదా సంస్థలు తమ చట్టబద్ధ బాధ్యతను నిర్వర్తించనప్పుడు న్యాయస్థానం ఈ రిట్ జారీ చేస్తుంది."
    ),
    (
        "Which Article of the Constitution of India provides for the establishment and jurisdiction of the Election Commission of India (ECI)?",
        "భారత రాజ్యాంగంలో కేంద్ర ఎన్నికల సంఘం (ECI) ఏర్పాటు మరియు అధికారాలను తెలిపే అధికరణం ఏది?",
        ["Article 280", "Article 324", "Article 356", "Article 370"],
        ["అధికరణం 280", "అధికరణం 324", "అధికరణం 356", "అధికరణం 370"],
        1,
        "Article 324 vests the superintendence, direction, and control of elections to Parliament and State Legislatures in the Election Commission.",
        "అధికరణం 324 భారతదేశంలో పార్లమెంటు, రాష్ట్ర శాసనసభల ఎన్నికల నిర్వహణ, పర్యవేక్షణ అధికారాలను ఎన్నికల సంఘానికి కల్పిస్తుంది."
    ),
    (
        "Who among the following has the final authority to decide whether a bill introduced in Parliament is a 'Money Bill' or not under Article 110?",
        "భారత రాజ్యాంగంలోని అధికరణం 110 ప్రకారం పార్లమెంటులో ప్రవేశపెట్టిన బిల్లు 'ద్రవ్య బిల్లు' అవునా కాదా అని ధృవీకరించే అంతిమ అధికారం ఎవరికి ఉంది?",
        ["President of India", "Speaker of the Lok Sabha", "Chairman of the Rajya Sabha", "Union Finance Minister"],
        ["భారత రాష్ట్రపతి", "లోక్‌సభ స్పీకర్", "రాజ్యసభ ఛైర్మన్", "కేంద్ర ఆర్థిక మంత్రి"],
        1,
        "Under Article 110(3), the decision of the Speaker of the Lok Sabha on whether a bill is a Money Bill is final.",
        "అధికరణం 110(3) ప్రకారం ఒక బిల్లు ద్రవ్య బిల్లా కాదా అని నిర్ణయించే అంతిమ అధికారం లోక్‌సభ స్పీకర్‌కు మాత్రమే ఉంది."
    ),
    (
        "The Directive Principles of State Policy (DPSP) enshrined in Part IV of the Indian Constitution were borrowed from the constitution of which nation?",
        "భారత రాజ్యాంగంలోని 4వ భాగంలో గల ఆదేశిక సూత్రాలు (DPSP) ఏ దేశ రాజ్యాంగం నుండి గ్రహించబడ్డాయి?",
        ["United States of America", "Ireland (Irish Constitution)", "United Kingdom", "Australia"],
        ["అమెరికా", "ఐర్లాండ్ రాజ్యాంగం", "బ్రిటన్", "ఆస్ట్రేలియా"],
        1,
        "The framers borrowed the Directive Principles of State Policy from the 1937 Irish Constitution.",
        "భారత రాజ్యాంగ నిర్మాతలు ఆదేశిక సూత్రాలను ఐర్లాండ్ రాజ్యాంగం నుండి స్వీకరించారు."
    ),
    (
        "Under which Article of the Constitution can the President of India promulgate an Ordinance when both Houses of Parliament are not in session?",
        "పార్లమెంటు సమావేశాలు జరగనప్పుడు అత్యవసర పరిస్థితులలో ఆర్డినెన్స్ జారీ చేసే అధికారాన్ని రాష్ట్రపతికి రాజ్యాంగంలోని ఏ అధికరణం కల్పిస్తుంది?",
        ["Article 72", "Article 123", "Article 143", "Article 213"],
        ["అధికరణం 72", "అధికరణం 123", "అధికరణం 143", "అధికరణం 213"],
        1,
        "Article 123 empowers the President to promulgate ordinances during recess of Parliament. Article 213 provides similar powers to Governors.",
        "రాష్ట్రపతికి ఆర్డినెన్స్ జారీ చేసే అధికారాన్ని అధికరణం 123 కల్పిస్తుంది (గవర్నర్‌కు అధికరణం 213)."
    ),
    (
        "The Anti-Defection Law was introduced into the Constitution of India via which Constitutional Amendment Act?",
        "పార్టీ ఫిరాయింపుల నిరోధక చట్టాన్ని భారత రాజ్యాంగంలోకి ఏ రాజ్యాంగ సవరణ చట్టం ద్వారా ప్రవేశపెట్టారు?",
        ["44th Amendment Act, 1978", "52nd Amendment Act, 1985", "61st Amendment Act, 1988", "91st Amendment Act, 2003"],
        ["44వ రాజ్యాంగ సవరణ చట్టం, 1978", "52వ రాజ్యాంగ సవరణ చట్టం, 1985", "61వ రాజ్యాంగ సవరణ చట్టం, 1988", "91వ రాజ్యాంగ సవరణ చట్టం, 2003"],
        1,
        "The 52nd Amendment Act of 1985 added the Tenth Schedule (Anti-Defection Law) to the Constitution.",
        "1985 లోని 52వ రాజ్యాంగ సవరణ చట్టం ద్వారా 10వ షెడ్యూల్ రూపంలో పార్టీ ఫిరాయింపుల నిరోధక చట్టాన్ని చేర్చారు."
    ),
    (
        "How many functional items are placed within the purview of Panchayati Raj Institutions under the Eleventh Schedule added by the 73rd Amendment?",
        "73వ రాజ్యాంగ సవరణ చట్టం ద్వారా చేర్చబడిన 11వ షెడ్యూల్‌లో పంచాయతీరాజ్ సంస్థలకు ఎన్ని విధులు/అంశాలు కేటాయించబడ్డాయి?",
        ["18 items", "21 items", "29 items", "33 items"],
        ["18 అంశాలు", "21 అంశాలు", "29 అంశాలు (29 items)", "33 అంశాలు"],
        2,
        "The Eleventh Schedule contains 29 functional items for Panchayats. (The Twelfth Schedule has 18 items for Municipalities).",
        "11వ షెడ్యూల్ లో పంచాయతీలకు 29 అధికారాలు/విధులు కేటాయించబడ్డాయి (12వ షెడ్యూల్ మున్సిపాలిటీలకు 18 అంశాలు)."
    ),
    (
        "The Comptroller and Auditor General of India (CAG) submits his audit reports relating to the accounts of the Union to whom under Article 151?",
        "భారత కంప్ట్రోలర్ అండ్ ఆడిటర్ జనరల్ (CAG) కేంద్ర ప్రభుత్వ ఖాతాల ఆడిట్ నివేదికలను అధికరణం 151 ప్రకారం ఎవరికి సమర్పిస్తారు?",
        ["Prime Minister of India", "President of India", "Speaker of Lok Sabha", "Public Accounts Committee Chairman"],
        ["భారత ప్రధానమంత్రి", "భారత రాష్ట్రపతి", "లోక్‌సభ స్పీకర్", "పబ్లిక్ అకౌంట్స్ కమిటీ ఛైర్మన్"],
        1,
        "Under Article 151(1), the CAG submits reports relating to Union accounts to the President, who causes them to be laid before each House of Parliament.",
        "అధికరణం 151(1) ప్రకారం కాగ్ తన కేంద్ర ఆడిట్ నివేదికలను రాష్ట్రపతికి సమర్పిస్తారు, రాష్ట్రపతి వాటిని పార్లమెంటు ఉభయ సభల ముందుంచుతారు."
    ),
    (
        "Under Article 200 of the Constitution, which of the following actions can a State Governor take on a bill passed by the State Legislature?",
        "భారత రాజ్యాంగంలోని అధికరణం 200 క్రింద రాష్ట్ర శాసనసభ ఆమోదించిన బిల్లుపై గవర్నర్ క్రింది ఏ చర్య తీసుకోవచ్చును?",
        ["Give assent to the bill", "Withhold assent to the bill", "Reserve the bill for the consideration of the President", "All of the above"],
        ["బిల్లుకు ఆమోదం తెలపడం", "బిల్లును నిలిపివేయడం (Withhold assent)", "రాష్ట్రపతి పరిశీలన కోసం బిల్లును రిజర్వ్ చేయడం", "పైవన్నీ సరైనవే"],
        3,
        "Article 200 gives the Governor options: assent, withhold assent, return for reconsideration (non-money bill), or reserve for the President.",
        "అధికరణం 200 ప్రకారం గవర్నర్ బిల్లును ఆమోదించవచ్చు, నిలిపివేయవచ్చు లేదా రాష్ట్రపతి పరిశీలనకు పంపవచ్చు."
    ),
    (
        "Which landmark Supreme Court judgment in 1973 established the 'Basic Structure Doctrine' of the Indian Constitution?",
        "భారత రాజ్యాంగం యొక్క 'ప్రాథమిక స్వరూప సిద్ధాంతాన్ని' (Basic Structure Doctrine) ప్రతిపాదించిన 1973 నాటి సుప్రీంకోర్టు చారిత్రక తీర్పు ఏది?",
        ["Golaknath v. State of Punjab", "Kesavananda Bharati v. State of Kerala", "Minerva Mills v. Union of India", "Maneka Gandhi v. Union of India"],
        ["గోలక్‌నాథ్ వర్సెస్ పంజాబ్ రాష్ట్రం", "కేశవానంద భారతి వర్సెస్ కేరళ రాష్ట్రం", "మినర్వా మిల్స్ వర్సెస్ యూనియన్ ఆఫ్ ఇండియా", "మేనకా గాంధీ వర్సెస్ యూనియన్ ఆఫ్ ఇండియా"],
        1,
        "In Kesavananda Bharati (1973), a 13-judge bench ruled that Parliament cannot alter the basic structure of the Constitution under Article 368.",
        "1973 నాటి కేశవానంద భారతి కేసులో 13 మంది న్యాయమూర్తుల ధర్మాసనం రాజ్యాంగ ప్రాథమిక నిర్మాణాన్ని పార్లమెంటు మార్చలేదని తీర్పునిచ్చింది."
    ),
    (
        "Who acts as the ex-officio Chairman of the Council of States (Rajya Sabha) under Article 89 of the Constitution?",
        "రాజ్యాంగంలోని అధికరణం 89 ప్రకారం రాజ్యసభకు ఎక్స్-అఫీషియో ఛైర్మన్‌గా వ్యవహరించేది ఎవరు?",
        ["President of India", "Vice-President of India", "Prime Minister of India", "Deputy Chairman of Rajya Sabha"],
        ["భారత రాష్ట్రపతి", "భారత ఉపరాష్ట్రపతి", "భారత ప్రధానమంత్రి", "రాజ్యసభ డిప్యూటీ ఛైర్మన్"],
        1,
        "Article 89(1) specifies that the Vice-President of India is ex-officio Chairman of the Rajya Sabha.",
        "అధికరణం 89(1) ప్రకారం భారత ఉపరాష్ట్రపతి రాజ్యసభకు పదవీరీత్యా (ఎక్స్-అఫీషియో) ఛైర్మన్‌గా వ్యవహరిస్తారు."
    ),
    (
        "Which Article of the Constitution guarantees the 'Protection of life and personal liberty' to every person?",
        "ప్రతి వ్యక్తికి 'జీవించే హక్కు మరియు వ్యక్తిగత స్వేచ్ఛ'ను హామీ ఇచ్చే ప్రాథమిక హక్కు అధికరణం ఏది?",
        ["Article 14", "Article 19", "Article 21", "Article 25"],
        ["అధికరణం 14", "అధికరణం 19", "అధికరణం 21", "అధికరణం 25"],
        2,
        "Article 21 states that no person shall be deprived of his life or personal liberty except according to procedure established by law.",
        "చట్టం ద్వారా నిర్దేశించిన పద్ధతిలో తప్ప ఏ వ్యక్తి యొక్క ప్రాణాన్ని లేదా వ్యక్తిగత స్వేచ్ఛను హరించరాదని అధికరణం 21 తెలుపుతుంది."
    ),
    (
        "The Sixteenth Finance Commission of India was constituted under the chairmanship of:",
        "భారతదేశ 16వ ఆర్థిక సంఘం ఎవరి అధ్యక్షతన ఏర్పాటు చేయబడింది?",
        ["Dr. Y.V. Reddy", "N.K. Singh", "Dr. Arvind Panagariya", "Dr. C. Rangarajan"],
        ["డాక్టర్ వై.వి. రెడ్డి", "ఎన్.కె. సింగ్", "డాక్టర్ అరవింద్ పనగరియా", "డాక్టర్ సి. రంగరాజన్"],
        2,
        "Dr. Arvind Panagariya, former Vice Chairman of NITI Aayog, was appointed Chairman of the 16th Finance Commission in December 2023.",
        "నీతి ఆయోగ్ మాజీ ఉపాధ్యక్షుడు డాక్టర్ అరవింద్ పనగరియా అధ్యక్షతన 16వ ఆర్థిక సంఘం ఏర్పాటయింది."
    ),
    (
        "Which Constitutional Amendment Act lowered the voting age of Indian citizens from 21 years to 18 years?",
        "భారతీయ పౌరుల ఓటు హక్కు వయోపరిమితిని 21 సంవత్సరాల నుండి 18 సంవత్సరాలకు తగ్గించిన రాజ్యాంగ సవరణ చట్టం ఏది?",
        ["42nd Amendment Act", "61st Amendment Act, 1988", "73rd Amendment Act", "86th Amendment Act"],
        ["42వ సవరణ చట్టం", "61వ రాజ్యాంగ సవరణ చట్టం, 1988", "73వ సవరణ చట్టం", "86వ సవరణ చట్టం"],
        1,
        "The 61st Constitutional Amendment Act, 1988 amended Article 326, reducing voting age from 21 to 18 years.",
        "1988 లోని 61వ రాజ్యాంగ సవరణ ద్వారా ఓటు హక్కు వయస్సును 21 నుండి 18 ఏళ్లకు తగ్గించారు."
    ),
    (
        "National Emergency under Article 352 of the Indian Constitution can be proclaimed by the President only on the basis of written advice from:",
        "అధికరణం 352 క్రింద జాతీయ అత్యవసర పరిస్థితిని రాష్ట్రపతి ఎవరి లిఖితపూర్వక సిఫార్సు ఆధారంగా మాత్రమే విధించవచ్చును?",
        ["Prime Minister alone", "Union Cabinet (Council of Ministers headed by PM)", "Chief Justice of India", "Parliamentary Standing Committee"],
        ["ప్రధానమంత్రి ఒక్కరి సిఫార్సుపై", "కేంద్ర కేబినెట్ లిఖితపూర్వక సిఫార్సు (Union Cabinet)", "సుప్రీంకోర్టు ప్రధాన న్యాయమూర్తి", "పార్లమెంటరీ కమిటీ"],
        1,
        "The 44th Amendment Act, 1978 introduced the safeguard that the President can proclaim Article 352 only upon written recommendation of the Union Cabinet.",
        "44వ రాజ్యాంగ సవరణ ప్రకారం కేంద్ర కేబినెట్ లిఖితపూర్వక సలహా ఇస్తేనే రాష్ట్రపతి జాతీయ అత్యవసర పరిస్థితిని విధించగలరు."
    ),
    (
        "Under which Schedule of the Constitution of India are the recognized official languages of India enumerated?",
        "భారత రాజ్యాంగంలోని ఏ షెడ్యూల్‌లో అధికారికంగా గుర్తించబడిన 22 భాషలు పొందుపరచబడ్డాయి?",
        ["Seventh Schedule", "Eighth Schedule", "Ninth Schedule", "Tenth Schedule"],
        ["ఏడవ షెడ్యూల్", "ఎనిమిదవ షెడ్యూల్ (Eighth Schedule)", "తొమ్మిదవ షెడ్యూల్", "పదవ షెడ్యూల్"],
        1,
        "The Eighth Schedule lists the 22 constitutionally recognized languages of India.",
        "భారత రాజ్యాంగంలోని 8వ షెడ్యూల్ లో 22 అధికారిక భాషలు గుర్తించబడ్డాయి."
    )
]

for idx, pq in enumerate(polity_qs_m4):
    q_num = 159 + idx
    new_questions.append(make_q(q_num, 'General Studies', 'Indian Polity & Constitutional Governance', pq[0], pq[1], pq[2], pq[3], pq[4], pq[5], pq[6]))

# 6. Indian History & National Movement (Q176-Q188) - 13 Qs
history_qs = [
    (
        "The Great Bath, one of the most famous public structures of the Indus Valley Civilization, was discovered at which site?",
        "సింధు నాగరికతకు చెందిన ప్రసిద్ధ 'మహా స్నానవాటిక' (The Great Bath) ఏ నగరంలో కనుగొనబడింది?",
        ["Harappa", "Mohenjo-daro", "Lothal", "Kalibangan"],
        ["హరప్పా", "మొహెంజొదారో (Mohenjo-daro)", "లోథాల్", "కాలిబంగన్"],
        1,
        "The Great Bath was unearthed at Mohenjo-daro in Sindh (now Pakistan) by archaeological excavations.",
        "సింధు లోయ నాగరికతలోని ప్రసిద్ధ మహా స్నానవాటిక మొహెంజొదారో నగరంలో బయల్పడింది."
    ),
    (
        "The historic Kalinga War that brought about a profound spiritual transformation in Emperor Ashoka took place in which year?",
        "అశోక చక్రవర్తిలో తీవ్ర పరివర్తన తెచ్చి బౌద్ధమతాన్ని స్వీకరించేలా చేసిన చారిత్రక కళింగ యుద్ధం ఎప్పుడు జరిగింది?",
        ["326 BC", "261 BC", "232 BC", "185 BC"],
        ["క్రీ.పూ. 326", "క్రీ.పూ. 261 (261 BC)", "క్రీ.పూ. 232", "క్రీ.పూ. 185"],
        1,
        "The Kalinga War took place in 261 BC (8th year of Ashoka's coronation), recorded in Rock Edict XIII.",
        "అశోకుడి 13వ శిలా శాసనం ప్రకారం కళింగ యుద్ధం క్రీ.పూ. 261 లో జరిగింది."
    ),
    (
        "Which ruler of the Gupta dynasty assumed the proud imperial title of 'Vikramaditya'?",
        "గుప్త వంశానికి చెందిన ఏ చక్రవర్తి 'విక్రమాదిత్య' అనే బిరుదును ధరించెను?",
        ["Chandragupta I", "Samudragupta", "Chandragupta II", "Kumaragupta"],
        ["మొదటి చంద్రగుప్తుడు", "సముద్రగుప్తుడు", "రెండవ చంద్రగుప్తుడు (Chandragupta II)", "కుమారగుప్తుడు"],
        2,
        "Chandragupta II defeated the Western Kshatrapas (Sakas) and assumed the title Vikramaditya.",
        "శకులను ఓడించిన అనంతరం రెండవ చంద్రగుప్తుడు 'విక్రమాదిత్య' బిరుదును స్వీకరించాడు."
    ),
    (
        "Which Sultan of the Delhi Sultanate introduced the famous Market Control and Price Regulation System in India?",
        "ఢిల్లీ సుల్తానేట్ పాలకులలో సైన్యం సౌలభ్యం కోసం ప్రసిద్ధ మార్కెట్ సంస్కరణలు, నిత్యావసరాల ధరల నియంత్రణ విధానాన్ని ప్రవేశపెట్టినది ఎవరు?",
        ["Iltutmish", "Balban", "Alauddin Khilji", "Muhammad bin Tughlaq"],
        ["ఇల్తుత్‌మిష్", "బాల్బన్", "అల్లావుద్దీన్ ఖిల్జీ (Alauddin Khilji)", "మహ్మద్ బిన్ తుగ్లక్"],
        2,
        "Alauddin Khilji instituted strict market control regulations (Shahna-i-Mandi) in Delhi.",
        "అల్లావుద్దీన్ ఖిల్జీ నిత్యావసర వస్తువుల ధరలను స్థిరీకరిస్తూ మార్కెట్ నియంత్రణ విధానాన్ని అమలు చేశాడు."
    ),
    (
        "The Mughal Emperor Akbar promulgated a syncretic socio-religious ethical path in 1582 known as:",
        "మొఘల్ చక్రవర్తి అక్బర్ 1582 లో సర్వమత సారాంశంతో ప్రవేశపెట్టిన నూతన విశ్వాసం/విధానం ఏది?",
        ["Din-i-Ilahi (Tauhid-i-Ilahi)", "Sulah-i-Kul", "Ibadat Khana", "Jharokha Darshan"],
        ["దీన్-ఇ-ఇలాహీ (Din-i-Ilahi)", "సుల్హ్-ఇ-కుల్", "ఇబాదత్ ఖానా", "ఝరోఖా దర్శన్"],
        0,
        "Din-i-Ilahi was an ethical monotheistic code promulgated by Akbar advocating universal peace and tolerance.",
        "సర్వ మతాలలోని ఉన్నత విలువలతో అక్బర్ దీన్-ఇ-ఇలాహీ అనే జీవన విధానాన్ని స్థాపించాడు."
    ),
    (
        "At which historic cantonment did the 1857 Revolt erupt on 10th May 1857?",
        "10 మే 1857 న భారతదేశ ప్రథమ స్వాతంత్ర్య సంగ్రామం (1857 తిరుగుబాటు) ఏ సైనిక స్థావరం వద్ద ప్రారంభమైంది?",
        ["Barrackpore", "Meerut", "Delhi", "Kanpur"],
        ["బారక్‌పూర్", "మీరట్ (Meerut)", "ఢిల్లీ", "కాన్పూర్"],
        1,
        "The general uprising of the 1857 Revolt erupted at Meerut cantonment on May 10, 1857.",
        "10 మే 1857 న మీరట్ సైనిక స్థావరంలో సిపాయిలు తిరుగుబాటు జెండా ఎగురవేశారు."
    ),
    (
        "Who founded the 'Arya Samaj' in Bombay in 1875 with the inspiring clarion call 'Go Back to the Vedas'?",
        "'వేదాలకు తరలిపొండి' అనే నినాదంతో 1875 లో బొంబాయిలో 'ఆర్య సమాజం' ను స్థాపించిన సంఘ సంస్కర్త ఎవరు?",
        ["Raja Ram Mohan Roy", "Swami Dayananda Saraswati", "Swami Vivekananda", "Ishwar Chandra Vidyasagar"],
        ["రాజా రామ్మోహన్ రాయ్", "స్వామి దయానంద సరస్వతి", "స్వామి వివేకానంద", "ఈశ్వరచంద్ర విద్యాసాగర్"],
        1,
        "Swami Dayananda Saraswati founded the Arya Samaj in 1875 and authored 'Satyarth Prakash'.",
        "1875 లో స్వామి దయానంద సరస్వతి ఆర్య సమాజాన్ని స్థాపించి వేదాల పునరుద్ధరణకు పిలుపునిచ్చారు."
    ),
    (
        "The partition of Bengal executed by Lord Curzon took effect on which date in 1905, observed across Bengal as a day of national mourning?",
        "లార్డ్ కర్జన్ అమలు చేసిన బెంగాల్ విభజన 1905 లో ఏ రోజున అమల్లోకి వచ్చింది (ఆ రోజును రక్షాబంధన్, సంతాప దినంగా పాటించారు)?",
        ["15th August 1905", "16th October 1905", "7th November 1905", "31st December 1905"],
        ["15 ఆగస్టు 1905", "16 అక్టోబర్ 1905", "7 నవంబర్ 1905", "31 డిసెంబర్ 1905"],
        1,
        "The partition of Bengal took effect on 16 October 1905, sparking the nationwide Swadeshi and Vande Mataram Movement.",
        "బెంగాల్ విభజన 16 అక్టోబర్ 1905 నుండి అమల్లోకి వచ్చింది, ఇది స్వదేశీ ఉద్యమానికి దారితీసింది."
    ),
    (
        "The Non-Cooperation Movement was abruptly suspended by Mahatma Gandhi in February 1922 following which violent tragedy?",
        "ఫిబ్రవరి 1922 లో జరిగిన ఏ హింసాత్మక సంఘటన కారణంగా మహాత్మా గాంధీ సహాయ నిరాకరణ ఉద్యమాన్ని అకస్మాత్తుగా నిలిపివేశారు?",
        ["Jallianwala Bagh Massacre", "Chauri Chaura Incident", "Kakori Train Action", "Rowlatt Act Satyagraha"],
        ["జలియన్ వాలాబాగ్ దురంతం", "చౌరీ చౌరా సంఘటన (Chauri Chaura)", "కాకోరి రైలు దోపిడీ", "రౌలత్ సత్యాగ్రహం"],
        1,
        "The Chauri Chaura incident in Gorakhpur (UP) where 22 policemen were burnt in a police station led Gandhi to withdraw the movement on 12 Feb 1922.",
        "ఉత్తరప్రదేశ్‌లోని చౌరీ చౌరా వద్ద జరిగిన హింసాత్మక ఘటనతో గాంధీజీ సహాయ నిరాకరణ ఉద్యమాన్ని విరమించారు."
    ),
    (
        "Mahatma Gandhi began his historic 24-day Salt March (Dandi March) on 12th March 1930 from which ashram?",
        "మహాత్మా గాంధీ 12 మార్చి 1930న తన చారిత్రక 24 రోజుల ఉప్పు సత్యాగ్రహాన్ని (దండి యాత్ర) ఏ ఆశ్రమం నుండి ప్రారంభించారు?",
        ["Wardha Ashram", "Sabarmati Ashram (Ahmedabad)", "Phoenix Settlement", "Sevagram"],
        ["వార్ధా ఆశ్రమం", "సబర్మతి ఆశ్రమం (అహ్మదాబాద్)", "ఫీనిక్స్ సెటిల్‌మెంట్", "సేవాగ్రామ్"],
        1,
        "Gandhiji began the 240-mile Dandi March from Sabarmati Ashram to Dandi with 78 volunteers, breaking the salt law on 6 April 1930.",
        "గాంధీజీ 78 మంది అనుచరులతో సబర్మతి ఆశ్రమం నుండి దండి వరకు పాదయాత్ర చేసి శాసనోల్లంఘన ఉద్యమాన్ని ప్రారంభించారు."
    ),
    (
        "The historic 'Quit India' Resolution was adopted by the All India Congress Committee (AICC) on 8th August 1942 at which session?",
        "8 ఆగస్టు 1942 న చారిత్రక 'క్విట్ ఇండియా' తీర్మానాన్ని అఖిల భారత కాంగ్రెస్ కమిటీ (AICC) ఏ సమావేశంలో ఆమోదించింది?",
        ["Lahore Session", "Gowalia Tank Maidan (Bombay)", "Tripuri Session", "Ramgarh Session"],
        ["లాహోర్ సమావేశం", "గోవాలియా ట్యాంక్ మైదానం (బొంబాయి)", "త్రిపురి సమావేశం", "రామ్‌గఢ్ సమావేశం"],
        1,
        "AICC met at Gowalia Tank Maidan (August Kranti Maidan) in Bombay where Gandhi gave the historic call 'Do or Die'.",
        "బొంబాయిలోని గోవాలియా ట్యాంక్ మైదానంలో జరిగిన కాంగ్రెస్ సమావేశంలో గాంధీజీ 'డూ ఆర్ డై' నినాదమిచ్చారు."
    ),
    (
        "Who founded the 'Forward Bloc' political party in 1939 after resigning from the presidency of the Indian National Congress?",
        "1939 లో కాంగ్రెస్ అధ్యక్ష పదవికి రాజీనామా చేసిన తర్వాత 'ఫార్వర్డ్ బ్లాక్' (Forward Bloc) పార్టీని స్థాపించిన జాతీయ నాయకుడు ఎవరు?",
        ["Subhas Chandra Bose", "Jawaharlal Nehru", "Acharya Narendra Deva", "Jayaprakash Narayan"],
        ["సుభాష్ చంద్రబోస్", "జవహర్‌లాల్ నెహ్రూ", "ఆచార్య నరేంద్ర దేవ్", "జయప్రకాష్ నారాయణ్"],
        0,
        "Netaji Subhas Chandra Bose resigned from the INC presidency after the Tripuri crisis and formed the Forward Bloc in May 1939.",
        "త్రిపురి సంక్షోభం అనంతరం కాంగ్రెస్ కు రాజీనామా చేసి నేతాజీ సుభాష్ చంద్రబోస్ 'ఫార్వర్డ్ బ్లాక్' ను స్థాపించారు."
    ),
    (
        "Who was the Governor-General of India at the time of India's independence in August 1947?",
        "ఆగస్టు 1947 లో భారతదేశానికి స్వాతంత్ర్యం వచ్చిన సమయంలో భారత గవర్నర్ జనరల్‌గా వ్యవహరించినది ఎవరు?",
        ["Lord Wavell", "Lord Mountbatten", "C. Rajagopalachari", "Lord Linlithgow"],
        ["లార్డ్ వేవెల్", "లార్డ్ మౌంట్‌బాటెన్ (Lord Mountbatten)", "సి. రాజగోపాలాచారి", "లార్డ్ లిన్‌లిత్‌గో"],
        1,
        "Lord Mountbatten was the last British Viceroy and served as the first Governor-General of independent India until June 1948.",
        "స్వాతంత్ర్య సమయానికి లార్డ్ మౌంట్‌బాటెన్ గవర్నర్ జనరల్‌గా ఉన్నారు (తర్వాత చక్రవర్తుల రాజగోపాలాచారి బాధ్యతలు చేపట్టారు)."
    )
]

for idx, hq in enumerate(history_qs):
    q_num = 176 + idx
    new_questions.append(make_q(q_num, 'General Studies', 'Indian History & National Movement', hq[0], hq[1], hq[2], hq[3], hq[4], hq[5], hq[6]))

# 7. Telangana History, Culture & State Formation (Q189-Q200) - 12 Qs
tsm_qs_m4 = [
    (
        "Which renowned Prakrit poetic anthology consisting of 700 verses was composed by the 17th Satavahana monarch, King Hala?",
        "17వ శాతవాహన చక్రవర్తి హాలుడు ప్రాకృత భాషలో రచించిన 700 శృంగార పద్యాల ప్రసిద్ధ సంకలనం ఏది?",
        ["Brihatkatha", "Gatha Saptasati (గాథా సప్తశతి)", "Kavyamimamsa", "Lilavati Parinayam"],
        ["బృహత్కథ", "గాథా సప్తశతి", "కావ్యమీమాంస", "లీలావతి పరిణయం"],
        1,
        "King Hala of the Satavahana dynasty composed the romantic anthology Gatha Saptasati in Maharashtri Prakrit.",
        "శాతవాహన రాజు హాలుడు ప్రాకృత భాషలో 'గాథా సప్తశతి' గ్రంథాన్ని సంకలనం చేశాడు."
    ),
    (
        "The heroic Kakatiya queen Rani Rudrama Devi successfully repulsed the invasion of which Yadava (Seuna) ruler at Devagiri?",
        "కాకతీయ వీర వనిత రాణి రుద్రమదేవి ఏ యాదవ (సేవుణ) రాజు యొక్క దండయాత్రను తిప్పికొట్టి ఓడించింది?",
        ["Mahadeva", "Singhana", "Ramachandra", "Bhillama V"],
        ["మహాదేవుడు (Mahadeva)", "సింఘణ", "రామచంద్రుడు", "ఐదవ భిల్లముడు"],
        0,
        "Rudrama Devi defeated Yadava King Mahadeva of Devagiri who besieged Warangal, forcing him to pay a huge indemnity.",
        "రుద్రమదేవి దేవగిరి యాదవ రాజైన మహాదేవుడిని ఓడించి కాకతీయ రాజ్యాన్ని రక్షించింది."
    ),
    (
        "The iconic monument 'Charminar' in Hyderabad was built in 1591 by which Sultan of the Qutb Shahi dynasty to commemorate the eradication of plague?",
        "1591 లో ప్లేగు వ్యాధి నిర్మూలనకు చిహ్నంగా హైదరాబాద్‌లోని చారిత్రక 'చార్మినార్' ను నిర్మించిన కుతుబ్‌షాహీ సుల్తాన్ ఎవరు?",
        ["Sultan Quli Qutb-ul-Mulk", "Ibrahim Qutb Shah", "Muhammad Quli Qutb Shah", "Abdullah Qutb Shah"],
        ["సుల్తాన్ కులీ కుతుబ్-ఉల్-ముల్క్", "ఇబ్రహీం కుతుబ్ షా", "మహమ్మద్ కులీ కుతుబ్ షా", "అబ్దుల్లా కుతుబ్ షా"],
        2,
        "Muhammad Quli Qutb Shah, the 5th Sultan and founder of Hyderabad city, constructed the Charminar in 1591.",
        "హైదరాబాద్ నగర నిర్మాత అయిన మహమ్మద్ కులీ కుతుబ్ షా 1591 లో చార్మినార్ ను నిర్మించాడు."
    ),
    (
        "Who was the Prime Minister (Diwan) of Hyderabad State who initiated far-reaching administrative and revenue reforms between 1853 and 1883?",
        "1853 నుండి 1883 మధ్య హైదరాబాద్ రాజ్యంలో సుపరిపాలన, రెవెన్యూ సంస్కరణలను ప్రవేశపెట్టిన ప్రసిద్ధ ప్రధాని (దివాన్) ఎవరు?",
        ["Salar Jung I (Mir Turab Ali Khan)", "Salar Jung II", "Maharaja Kishen Pershad", "Mir Alam"],
        ["మొదటి సాలార్ జంగ్ (మీర్ తురబ్ అలీ ఖాన్)", "రెండవ సాలార్ జంగ్", "మహారాజా కిషన్ ప్రసాద్", "మీర్ ఆలం"],
        0,
        "Nawab Mir Turab Ali Khan (Salar Jung I) modernized the Nizam's administration, introducing Zilabandi system and railways.",
        "హైదరాబాద్ రాజ్యాన్ని ఆధునీకరించి జిలాబందీ రెవెన్యూ వ్యవస్థను తెచ్చిన దీవాన్ మొదటి సాలార్ జంగ్."
    ),
    (
        "The unique floral festival 'Bathukamma', celebrated with devotion during the Navaratri period, represents which cultural aspect of Telangana?",
        "తెలంగాణ సాంస్కృతిక అస్తిత్వానికి ప్రతీకగా నవరాత్రుల సమయంలో ఘనంగా నిర్వహించే పూల పండుగ 'బతుకమ్మ' ప్రధానంగా దేనికి సంబంధించినది?",
        ["Celebration of nature and seasonal wild medicinal flowers worshiping Goddess Gauri", "Harvesting of wheat crops in winter", "Worship of warfare weapons and horses", "Commemoration of the Kakatiya dynastic victory"],
        ["ప్రకృతిని ఆరాధిస్తూ ఔషధ గుణాలున్న అడవి పూలతో గౌరీ దేవిని పూజించే పండుగ", "శీతాకాలపు గోధుమ పంట కోత సంబరం", "ఆయుధాలు మరియు గుర్రాల పూజ", "కాకతీయుల సైనిక విజయ సంబరం"],
        0,
        "Bathukamma is the state floral festival where women arrange wild seasonal flowers in concentric tiers worshiping Gouramma.",
        "తెలంగాణ మహిళలు తంగేడు, గునుగు వంటి ఔషధ పూలతో గోపురాకారంలో బతుకమ్మలను పేర్చి గౌరమ్మను కొలుస్తారు."
    ),
    (
        "The historic Indian military police action codenamed 'Operation Polo' that integrated Hyderabad State into the Indian Union took place in which month and year?",
        "హైదరాబాద్ రాష్ట్రాన్ని భారత యూనియన్‌లో విలీనం చేసిన 'ఆపరేషన్ పోలో' సైనిక చర్య ఏ నెల మరియు సంవత్సరంలో జరిగింది?",
        ["August 1947", "September 1948", "January 1950", "November 1956"],
        ["ఆగస్టు 1947", "సెప్టెంబర్ 1948 (September 1948)", "జనవరి 1950", "నవంబర్ 1956"],
        1,
        "Operation Polo commenced on 13 September 1948 and ended with the surrender of the Nizam's forces on 17 September 1948.",
        "13 నుండి 17 సెప్టెంబర్ 1948 వరకు జరిగిన ఆపరేషన్ పోలో పోలీస్ చర్య ద్వారా హైదరాబాద్ రాష్ట్రం భారత్‌లో విలీనమైంది."
    ),
    (
        "The 1952 Non-Mulki Agitation in Hyderabad flared up following the tragic police firing on protesting students outside which institution on 3rd September 1952?",
        "హైదరాబాద్‌లో స్థానికేతరుల నియామకాలకు వ్యతిరేకంగా జరిగిన 1952 నాన్-ముల్కీ ఉద్యమం 3 సెప్టెంబర్ 1952 న ఏ విద్యాసంస్థ ఎదుట జరిగిన పోలీసు కాల్పుల వల్ల తీవ్రరూపం దాల్చింది?",
        ["Osmania University Arts College", "City College, Hyderabad", "Nizam College", "Chaderghat High School"],
        ["ఉస్మానియా విశ్వవిద్యాలయం", "సిటీ కాలేజ్, హైదరాబాద్ (City College)", "నిజాం కాలేజ్", "చాదర్‌ఘాట్ హైస్కూల్"],
        1,
        "The City College police firing on 3-4 September 1952 claimed several student lives, intensifying the 'Non-Mulki Go Back' agitation.",
        "3 సెప్టెంబర్ 1952న సిటీ కాలేజీ వద్ద విద్యార్థులపై జరిగిన పోలీసు కాల్పుల్లో అమరులైన విద్యార్థుల ఘటనతో ముల్కీ ఉద్యమం తీవ్రమైంది."
    ),
    (
        "Which committee was appointed by the Union Government under Fazal Ali in December 1953 to examine the reorganization of states on linguistic lines?",
        "భాషా ప్రాతిపదికన రాష్ట్రాల పునర్వ్యవస్థీకరణను పరిశీలించడానికి డిసెంబర్ 1953 లో కేంద్ర ప్రభుత్వం ఫజల్ అలీ అధ్యక్షతన నియమించిన కమిషన్ ఏది?",
        ["Dhar Commission", "JVP Committee", "States Reorganisation Commission (SRC)", "Wanchoo Committee"],
        ["ధార్ కమిషన్", "జెవిపి కమిటీ", "రాష్ట్రాల పునర్వ్యవస్థీకరణ కమిషన్ (SRC)", "వాంచూ కమిటీ"],
        2,
        "The States Reorganisation Commission (SRC) headed by Justice Fazal Ali with H.N. Kunzru and K.M. Panikkar recommended keeping Telangana as a separate Hyderabad state initially.",
        "ఫజల్ అలీ కమిషన్ (SRC) తెలంగాణ ప్రాంతాన్ని ప్రత్యేక హైదరాబాద్ రాష్ట్రంగానే కొనసాగించాలని సిఫార్సు చేసింది."
    ),
    (
        "Where was the historic 'Gentlemen's Agreement' signed on 20th February 1956 outlining safeguards for Telangana before the merger with Andhra?",
        "ఆంధ్రతో తెలంగాణ విలీనానికి ముందు తెలంగాణ ప్రాంత రక్షణల కోసం 20 ఫిబ్రవరి 1956 న చారిత్రక 'పెద్దమనుషుల ఒప్పందం' ఎక్కడ జరిగింది?",
        ["Hyderabad (Nizam Club)", "New Delhi (Hyderabad House)", "Kurnool", "Vijayawada"],
        ["హైదరాబాద్", "న్యూఢిల్లీ (హైదరాబాద్ హౌస్)", "కర్నూలు", "విజయవాడ"],
        1,
        "The Gentlemen's Agreement was signed on 20 February 1956 at Hyderabad House in New Delhi by 4 Telangana and 4 Andhra leaders.",
        "న్యూఢిల్లీలోని హైదరాబాద్ హౌస్‌లో 4గురు తెలంగాణ మరియు 4గురు ఆంధ్ర నాయకుల మధ్య పెద్దమనుషుల ఒప్పందం కుదిరింది."
    ),
    (
        "Who started the historic indefinite hunger strike on 8th January 1969 in Palvancha (Khammam district) that sparked the 1969 Separate Telangana Agitation?",
        "8 జనవరి 1969న ఖమ్మం జిల్లా పాల్వంచలో ప్రత్యేక తెలంగాణ రక్షణల అమలు కోసం ఆమరణ నిరాహార దీక్ష చేపట్టి 1969 తెలంగాణ ఉద్యమాన్ని ప్రారంభించినది ఎవరు?",
        ["Ravindranath (రవీంద్రనాథ్)", "Marri Chenna Reddy", "Prof. Jayashankar", "Konda Laxman Bapuji"],
        ["అన్నబత్తుల రవీంద్రనాథ్", "మర్రి చెన్నారెడ్డి", "ప్రొఫెసర్ జయశంకర్", "కొండా లక్ష్మణ్ బాపూజీ"],
        0,
        "Annabathula Ravindranath, an engineering student at Palvancha, began an indefinite hunger strike on 8 Jan 1969 for implementation of Telangana safeguards.",
        "పాల్వంచలో విద్యార్థి అన్నబత్తుల రవీంద్రనాథ్ 8 జనవరి 1969న ఆమరణ నిరాహార దీక్ష ప్రారంభించి 1969 ఉద్యమానికి శ్రీకారం చుట్టారు."
    ),
    (
        "The historic 'Million March' organized by the Telangana Joint Action Committee (TJAC) on Tank Bund, Hyderabad took place on which date?",
        "తెలంగాణ జేఏసీ ఆధ్వర్యంలో హైదరాబాద్ ట్యాంక్ బండ్ పై నిర్వహించిన చారిత్రక 'మిలియన్ మార్చ్' ఏ తేదీన జరిగింది?",
        ["9th December 2009", "10th March 2011", "30th September 2012", "2nd June 2014"],
        ["9 డిసెంబర్ 2009", "10 మార్చి 2011 (10 March 2011)", "30 సెప్టెంబర్ 2012", "2 జూన్ 2014"],
        1,
        "The historic Million March inspired by Egypt's Tahrir square was held on Tank Bund on 10 March 2011 despite massive police clampdowns.",
        "తెలంగాణ ఆకాంక్షను చాటుతూ 10 మార్చి 2011న ట్యాంక్ బండ్‌పై చారిత్రక మిలియన్ మార్చ్ విజయవంతంగా జరిగింది."
    ),
    (
        "On which historic 'Appointed Day' did the State of Telangana officially come into constitutional existence as the 29th State of India?",
        "ఏ చారిత్రక 'నియమిత దినం' (Appointed Day) నాడు తెలంగాణ రాష్ట్రం భారతదేశపు 29వ రాష్ట్రంగా అధికారికంగా ఆవిర్భవించింది?",
        ["20th February 2014", "1st March 2014", "2nd June 2014", "15th August 2014"],
        ["20 ఫిబ్రవరి 2014", "1 మార్చి 2014", "2 జూన్ 2014 (2 June 2014)", "15 ఆగస్టు 2014"],
        2,
        "Under Section 2(a) of the Andhra Pradesh Reorganisation Act, 2014, June 2, 2014 was notified as the Appointed Day of Telangana State.",
        "ఆంధ్రప్రదేశ్ పునర్వ్యవస్థీకరణ చట్టం, 2014 ప్రకారం 2 జూన్ 2014న తెలంగాణ రాష్ట్రం అధికారికంగా ఏర్పాటయింది."
    )
]

for idx, tq in enumerate(tsm_qs_m4):
    q_num = 189 + idx
    new_questions.append(make_q(q_num, 'General Studies', 'Telangana History & Movement', tq[0], tq[1], tq[2], tq[3], tq[4], tq[5], tq[6]))

print(f"Total new questions in Mock 4: {len(new_questions)}")
assert len(new_questions) == 200, f"Expected 200 questions, got {len(new_questions)}"

# Save rebalanced Mock 4
out_path = 'public/data/mock_test_full_200_4.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({"testId": "tsplrb-si-mock-full-200-4", "questions": new_questions}, f, ensure_ascii=False, indent=2)

print("✅ Rebalanced Mock 4 saved successfully!")
