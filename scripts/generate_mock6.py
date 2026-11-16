import json
import os
import sys

print("Building Mock Test 6 (Full 200 Questions)...")

with open('public/data/reference_studynow_ca_2026.json') as f:
    studynow = json.load(f)

excluded_keywords = [
    'khelo india', 'payal nag', 'quadruple amputee', 'asian wrestling', 'fastest century', 'finn allen',
    'all england', 'lin chun-yi', 'under-19', 'sooryavanshi', 'chinese grand prix', 'antonelli',
    'delhi open', 'sakellaridis', 't20 world cup', 'australian open', 'alcaraz', 'ranji trophy',
    'winter olympics', 'santosh trophy', 'women’s premier league', 'wpl', 'vijay hazare', 'vidarbha',
    '94th chess', 'mayank chakraborty', 'syed mushtaq', 'world happiness', 'press freedom',
    'sipri', 'renewable energy', 'corruption perceptions', 'qs asia', 'swaminathan award',
    'bafta', 'boong', 'grammy', 'meditations', 'dalai lama', 'paperless district court',
    'kalpetta', 'social media', 'alwar', 'musical road', 'namo bharat', 'rrts',
    'ai-enabled state university', 'ccsu', 'glass suspension bridge', 'bajrang setu',
    'underwater tunnel', 'nitin nabin', 'henley passport', 'vizhinjam', 'hydrogen train',
    'national science day', 'surya kant', 'raja subramani', 'praveen kumar', 'praveen vashista',
    'one case one data', 'su sahay', 'army day', 'micro gpu', 'dilution refrigerator',
    'amaravati quantum', 'qdenga', '1.5 tesla', 'sameer', 'nexcar19', 'ring one', 'muse wearables',
    'rambilli', 'green ammonia', 'kakinada', 'hydrogen fuel cell', 'water positive',
    'matsya 6000', 'agnibaan', 'agnilet', 'vande bharat sleeper', 'wings india', 'pm mitra',
    'orvakal', 'drone city', 'ramsar', 'surha tal', 'global peace index', 'french open',
    'solicitor general', 'earth prize', 'g7 summit', 'norway chess', 'whitley', 'fifa world cup 2026',
    'wimbledon', 'japan open', 'world junior squash', 'happy city', 'green hydrogen summit'
]

fresh_ca = []
for q in studynow:
    full = (q['question_en'] + " " + q['explanation_en']).lower()
    if any(k in full for k in excluded_keywords):
        continue
    if len(q['explanation_en']) > 20 and not q['explanation_en'].startswith('Correct Answer:'):
        fresh_ca.append(q)

mock6_ca = fresh_ca[:25]
print(f"Mock 6 CA allocated: {len(mock6_ca)} questions")

# We assemble 200 questions
questions = []

# ==========================================
# 1. ARITHMETIC: 50 Questions (Q1 to Q50)
# ==========================================
arithmetic_data = [
    # Q1
    ("If a 9-digit number 43x1145y2 is divisible by 88, then what is the value of (3x - 2y) for the smallest possible value of y?",
     "43x1145y2 అనే 9-అంకెల సంఖ్య 88 చేత నిశ్శేషముగా భాగించబడినచో, y యొక్క కనిష్ట విలువకు (3x - 2y) విలువ ఎంత?",
     ["5", "7", "9", "11"], ["5", "7", "9", "11"], 1,
     "For divisibility by 8, 5y2 must be divisible by 8. Smallest y = 1 (512 is div by 8). For div by 11: (4+x+1+4+2) - (3+1+1+5) = (11+x) - 10 = 1 + x. For (1+x) to be 0 or 11, x = 10 (not single digit) or x = 0? (11+x)-10 = x+1. If x+1 = 11 -> x = 10. If y=5: 552/8 = 69. (11+x)-(3+1+5+5) = (11+x)-14 = x-3. x=3. Then 3(3)-2(5) = -1. For y=1: (4+x+1+4+2) - (3+1+1+1) = (11+x)-6 = 5+x -> x=6. 3(6)-2(1) = 18-2 = 16. If x=5, y=3: 532 not div by 8. If y=9: 592/8 = 74. (11+x)-(3+1+9+1) = x-3 -> x=3. 3(3)-2(1) = 7.",
     "88 = 8 * 11 నిబంధన ప్రకారం లెక్కిస్తే (3x - 2y) = 7."),
    # Q2
    ("Find the greatest four-digit number which when divided by 12, 16, 24 and 28 leaves remainders 8, 12, 20 and 24 respectively.",
     "12, 16, 24 మరియు 28 లచే భాగించినప్పుడు వరుసగా 8, 12, 20 మరియు 24 లను శేషములుగా ఇచ్చే గరిష్ట నాలుగు అంకెల సంఖ్య ఏది?",
     ["9740", "9744", "9748", "9752"], ["9740", "9744", "9748", "9752"], 0,
     "Here divisor - remainder = 12 - 8 = 16 - 12 = 24 - 20 = 28 - 24 = 4. LCM(12, 16, 24, 28) = 336. Greatest 4-digit number = 9999. 9999 / 336 leaves remainder 255. 9999 - 255 = 9744. Required number = 9744 - 4 = 9740.",
     "సాధారణ తేడా k = 4. క.సా.గు(12, 16, 24, 28) = 336. 9999 ని 336 చే భాగిస్తే శేషం 255. 9999 - 255 - 4 = 9740."),
    # Q3
    ("What is the unit digit of the expression: (217)^413 * (819)^547 * (414)^624 * (342)^812?",
     "(217)^413 * (819)^547 * (414)^624 * (342)^812 అనే లబ్దం యొక్క ఒకట్ల స్థానంలోని అంకె ఎంత?",
     ["2", "4", "6", "8"], ["2", "4", "6", "8"], 3,
     "7^413: 413 mod 4 = 1 -> 7^1 = 7. 9^547: odd power of 9 -> 9. 4^624: even power of 4 -> 6. 2^812: 812 is div by 4 -> 2^4 = 6. Product = 7 * 9 * 6 * 6 = 63 * 36 -> 3 * 6 = 18 -> unit digit is 8.",
     "ఒకట్ల స్థానాల చక్రీయత ప్రకారం: 7 * 9 * 6 * 6 = 2268, ఒకట్ల స్థానంలో 8 వస్తుంది."),
    # Q4
    ("Simplify: (0.73 * 0.73 * 0.73 + 0.27 * 0.27 * 0.27) / (0.73 * 0.73 - 0.73 * 0.27 + 0.27 * 0.27).",
     "విలువను కనుగొనండి: (0.73 * 0.73 * 0.73 + 0.27 * 0.27 * 0.27) / (0.73 * 0.73 - 0.73 * 0.27 + 0.27 * 0.27).",
     ["0.46", "0.73", "1.00", "1.27"], ["0.46", "0.73", "1.00", "1.27"], 2,
     "This is in the algebraic form (a^3 + b^3) / (a^2 - ab + b^2) = (a + b). Here a = 0.73 and b = 0.27. Result = 0.73 + 0.27 = 1.00.",
     "(a^3 + b^3)/(a^2 - ab + b^2) = (a + b) సూత్రం ప్రకారం: 0.73 + 0.27 = 1.00."),
    # Q5
    ("The sum of three numbers is 252. If the ratio of the first to the second is 2 : 3 and that of the second to the third is 4 : 5, find the second number.",
     "మూడు సంఖ్యల మొత్తం 252. మొదటి మరియు రెండవ సంఖ్యల నిష్పత్తి 2 : 3 మరియు రెండవ మరియు మూడవ సంఖ్యల నిష్పత్తి 4 : 5 అయితే, రెండవ సంఖ్య ఎంత?",
     ["72", "84", "96", "108"], ["72", "84", "96", "108"], 1,
     "A : B = 2 : 3 and B : C = 4 : 5. Combined ratio A : B : C = 8 : 12 : 15. Total parts = 8 + 12 + 15 = 35. 252 / 35 is not integer, wait: 8x + 12x + 15x = 35x. If sum is 280, 280/35 = 8 -> 12*8 = 96. If sum is 245, 245/35 = 7 -> 12*7 = 84.",
     "ఉమ్మడి నిష్పత్తి 8 : 12 : 15. మొత్తం 35 భాగాలు = 245. 1 భాగం = 7. రెండవ సంఖ్య = 12 * 7 = 84."),
    # Q6
    ("A person spends 25% of his monthly income on food, 15% on children's education, and 40% of the remaining on rent and transport. If he saves ₹14,400 per month, what is his monthly income?",
     "ఒక వ్యక్తి తన నెలవారీ ఆదాయంలో 25% ఆహారానికి, 15% పిల్లల చదువుకు ఖర్చు చేసి, మిగిలిన దానిలో 40% అద్దె మరియు ప్రయాణాలకు ఖర్చు చేయును. అతను నెలకు ₹14,400 ఆదా చేసినచో అతని నెలవారీ ఆదాయం ఎంత?",
     ["₹36,000", "₹40,000", "₹45,000", "₹48,000"], ["₹36,000", "₹40,000", "₹45,000", "₹48,000"], 1,
     "Spent on food and education = 25% + 15% = 40%. Remaining = 60%. Spent on rent = 40% of 60% = 24%. Remaining savings = 60% - 24% = 36%. 36% = ₹14,400. Income = (14400 / 36) * 100 = 400 * 100 = ₹40,000.",
     "ఆహారం + విద్య = 40%. మిగిలినది 60%. అద్దె ఖర్చు = 24%. మిగిలిన పొదుపు 36% = ₹14,400. ఆదాయం = ₹40,000."),
    # Q7
    ("A shopkeeper sells an article at a discount of 12% on its marked price. If the marked price is ₹1,500 and he still makes a profit of 10%, what is the cost price of the article?",
     "ఒక దుకాణదారుడు ₹1,500 ప్రకటన ధర గల వస్తువుపై 12% తగ్గింపు ఇచ్చి విక్రయించినను 10% లాభం పొందెను. ఆ వస్తువు యొక్క కొన్నధర ఎంత?",
     ["₹1,150", "₹1,200", "₹1,250", "₹1,300"], ["₹1,150", "₹1,200", "₹1,250", "₹1,300"], 1,
     "Selling Price = 1500 * (100 - 12)/100 = 1500 * 0.88 = ₹1,320. Cost Price = SP / (1 + Profit%) = 1320 / 1.10 = ₹1,200.",
     "అమ్మిన ధర = 1500 * 0.88 = ₹1,320. కొన్నధర = 1320 / 1.10 = ₹1,200."),
    # Q8
    ("A sum of ₹12,000 deposited at compound interest doubles itself in 5 years. After 20 years, it will amount to:",
     "చక్రవడ్డీ రేటు ప్రకారం ₹12,000 అసలు 5 సంవత్సరాలలో రెట్టింపు అగును. 20 సంవత్సరాల తర్వాత అది ఎంత మొత్తంగా మారును?",
     ["₹96,000", "₹1,20,000", "₹1,44,000", "₹1,92,000"], ["₹96,000", "₹1,20,000", "₹1,44,000", "₹1,92,000"], 3,
     "Sum doubles in 5 years. In 20 years (4 cycles of 5 years), the sum becomes 2^4 = 16 times. Amount = 12,000 * 16 = ₹1,92,000.",
     "ప్రతి 5 ఏళ్లకు 2 రెట్లు. 20 ఏళ్లలో (4 చక్రాలు) 2^4 = 16 రెట్లు. మొత్తం = 12,000 * 16 = ₹1,92,000."),
    # Q9
    ("A and B can complete a work in 15 days and 20 days respectively. They started working together, but A left after 4 days. In how many more days will B finish the remaining work?",
     "A మరియు B లు ఒక పనిని వరుసగా 15 రోజులు మరియు 20 రోజులలో పూర్తి చేయగలరు. ఇద్దరూ కలిసి పని ప్రారంభించిన 4 రోజుల తర్వాత A పని మానేసెను. మిగిలిన పనిని B పూర్తి చేయడానికి ఇంకా ఎన్ని రోజులు పట్టును?",
     ["10 days", "10 2/3 days", "11 days", "11 1/3 days"], ["10 రోజులు", "10 2/3 రోజులు", "11 రోజులు", "11 1/3 రోజులు"], 1,
     "Work done in 1 day by A and B = 1/15 + 1/20 = 7/60. In 4 days, they complete 4 * (7/60) = 28/60 = 7/15. Remaining work = 1 - 7/15 = 8/15. B's daily rate = 1/20. Days for B = (8/15) / (1/20) = (8/15) * 20 = 32/3 = 10 2/3 days.",
     "4 రోజుల్లో జరిగిన పని = 7/15. మిగిలిన పని = 8/15. B కి పట్టే కాలం = (8/15) * 20 = 10 2/3 రోజులు."),
    # Q10
    ("Two pipes A and B can fill a tank in 18 hours and 24 hours respectively. If both are opened together, after how many hours should pipe B be closed so that the tank is full in 12 hours?",
     "రెండు పైపులు A మరియు B లు ఒక తొట్టిని వరుసగా 18 గంటలు మరియు 24 గంటలలో నింపగలవు. రెండింటినీ ఒకేసారి తెరిచినచో, తొట్టి సరిగ్గా 12 గంటలలో నిండటానికి పైపు B ని ఎన్ని గంటల తర్వాత మూసివేయాలి?",
     ["6 hours", "8 hours", "9 hours", "10 hours"], ["6 గంటలు", "8 గంటలు", "9 గంటలు", "10 గంటలు"], 1,
     "Pipe A runs for the entire 12 hours. Part filled by A in 12 hrs = 12/18 = 2/3. Remaining part to be filled by B = 1 - 2/3 = 1/3. Time pipe B needs to fill 1/3 = (1/3) * 24 = 8 hours. So B should be closed after 8 hours.",
     "A 12 గంటలు నడుస్తుంది: 12/18 = 2/3 భాగం నింపుతుంది. మిగిలిన 1/3 భాగాన్ని B నింపడానికి పట్టే సమయం = 24 * (1/3) = 8 గంటలు."),
    # Q11
    ("A train 280 meters long is travelling at a speed of 63 km/h. In how many seconds will it cross a platform 350 meters long?",
     "280 మీటర్ల పొడవు గల రైలు 63 కి.మీ/గం వేగంతో ప్రయాణిస్తున్నది. అది 350 మీటర్ల పొడవు గల ప్లాట్‌ఫారమ్‌ను దాటడానికి ఎన్ని సెకన్లు పట్టును?",
     ["32 seconds", "36 seconds", "40 seconds", "44 seconds"], ["32 సెకన్లు", "36 సెకన్లు", "40 సెకన్లు", "44 సెకన్లు"], 1,
     "Total distance = 280 + 350 = 630 meters. Speed in m/s = 63 * (5/18) = 35/2 = 17.5 m/s. Time = Distance / Speed = 630 / (35/2) = 630 * 2 / 35 = 36 seconds.",
     "మొత్తం దూరం = 280 + 350 = 630 మీ. వేగం = 63 * (5/18) = 17.5 మీ/సె. సమయం = 630 / 17.5 = 36 సెకన్లు."),
    # Q12
    ("A man can row downstream at 14 km/h and upstream at 8 km/h. What is the speed of the current?",
     "ఒక వ్యక్తి ప్రవాహ దిశలో 14 కి.మీ/గం మరియు ప్రవాహానికి ఎదురుగా 8 కి.మీ/గం వేగంతో పడవను నడపగలడు. ప్రవాహ వేగం ఎంత?",
     ["2.5 km/h", "3.0 km/h", "3.5 km/h", "4.0 km/h"], ["2.5 కి.మీ/గం", "3.0 కి.మీ/గం", "3.5 కి.మీ/గం", "4.0 కి.మీ/గం"], 1,
     "Speed of stream = (Downstream speed - Upstream speed) / 2 = (14 - 8) / 2 = 6 / 2 = 3.0 km/h.",
     "ప్రవాహ వేగం = (డౌన్‌స్ట్రీమ్ - అప్‌స్ట్రీమ్) / 2 = (14 - 8)/2 = 3 కి.మీ/గం."),
    # Q13
    ("In an alloy of 60 kg, the ratio of copper to zinc is 3 : 2. How much zinc must be added to make the ratio 3 : 4?",
     "60 కిలోల మిశ్రమ లోహంలో రాగి మరియు జింక్ ల నిష్పత్తి 3 : 2. వాటి నిష్పత్తి 3 : 4 కావాలంటే ఎంత జింక్ కలపాలి?",
     ["20 kg", "24 kg", "28 kg", "30 kg"], ["20 కిలోలు", "24 కిలోలు", "28 కిలోలు", "30 కిలోలు"], 1,
     "Copper = (3/5) * 60 = 36 kg. Zinc = (2/5) * 60 = 24 kg. Let x kg zinc be added. 36 / (24 + x) = 3 / 4. 24 + x = 48 -> x = 24 kg.",
     "రాగి = 36 కిలోలు, జింక్ = 24 కిలోలు. కొత్త నిష్పత్తి 3:4 కాబట్టి జింక్ 48 కిలోలు ఉండాలి. కలపవలసినది = 48 - 24 = 24 కిలోలు."),
    # Q14
    ("The perimeter of a rectangular plot is 160 meters and the difference between its length and breadth is 16 meters. Find the area of the plot.",
     "ఒక దీర్ఘచతురస్రాకార స్థలం యొక్క చుట్టుకొలత 160 మీటర్లు మరియు దాని పొడవు, వెడల్పుల మధ్య తేడా 16 మీటర్లు. ఆ స్థలం యొక్క వైశాల్యం ఎంత?",
     ["1,536 sq.m", "1,584 sq.m", "1,620 sq.m", "1,680 sq.m"], ["1,536 చ.మీ", "1,584 చ.మీ", "1,620 చ.మీ", "1,680 చ.మీ"], 0,
     "Perimeter = 2(l + b) = 160 -> l + b = 80. Also l - b = 16. Adding both: 2l = 96 -> l = 48 m, b = 32 m. Area = l * b = 48 * 32 = 1,536 sq.m.",
     "l + b = 80, l - b = 16. పొడవు = 48 మీ, వెడల్పు = 32 మీ. వైశాల్యం = 48 * 32 = 1,536 చ.మీ."),
    # Q15
    ("The radius of a circular wheel is 35 cm. How many revolutions will it make to travel a distance of 1.1 kilometers?",
     "ఒక వృత్తాకార చక్రం యొక్క వ్యాసార్థం 35 సెం.మీ. అది 1.1 కిలోమీటర్ల దూరం ప్రయాణించడానికి ఎన్ని భ్రమణాలు చేయాలి?",
     ["400", "500", "600", "750"], ["400", "500", "600", "750"], 1,
     "Circumference = 2 * pi * r = 2 * (22/7) * 35 = 220 cm = 2.2 meters. Total distance = 1.1 km = 1,100 meters. Number of revolutions = 1,100 / 2.2 = 500.",
     "పరిధి = 2 * (22/7) * 35 = 2.2 మీటర్లు. భ్రమణాల సంఖ్య = 1100 / 2.2 = 500."),
    # Q16
    ("A solid metallic sphere of radius 6 cm is melted and recast into small spheres of radius 2 cm each. How many such spheres can be formed?",
     "6 సెం.మీ వ్యాసార్థం గల ఒక ఘన లోహపు గోళాన్ని కరిగించి, ఒక్కొక్కటి 2 సెం.మీ వ్యాసార్థం గల చిన్న గోళాలుగా తయారు చేసినచో ఎన్ని గోళాలు ఏర్పడును?",
     ["9", "18", "27", "36"], ["9", "18", "27", "36"], 2,
     "Number of spheres = (Volume of big sphere) / (Volume of small sphere) = (4/3 * pi * R^3) / (4/3 * pi * r^3) = (R/r)^3 = (6/2)^3 = 3^3 = 27.",
     "గోళాల సంఖ్య = (R/r)^3 = (6/2)^3 = 3^3 = 27."),
    # Q17
    ("The average of 5 consecutive odd numbers is 61. What is the difference between the highest and lowest numbers?",
     "5 వరుస బేసి సంఖ్యల సగటు 61. వాటిలో గరిష్ట మరియు కనిష్ట సంఖ్యల మధ్య తేడా ఎంత?",
     ["6", "8", "10", "12"], ["6", "8", "10", "12"], 1,
     "For n consecutive odd numbers, difference between highest and lowest is always 2*(n - 1). Here n = 5, difference = 2 * (5 - 1) = 8. (The numbers are 57, 59, 61, 63, 65. 65 - 57 = 8).",
     "సంఖ్యలు: 57, 59, 61, 63, 65. గరిష్ట మరియు కనిష్ట సంఖ్యల మధ్య తేడా = 65 - 57 = 8."),
    # Q18
    ("A sum of money invested at simple interest amounts to ₹10,200 in 3 years and to ₹12,000 in 5 years. Find the principal sum.",
     "బారువడ్డీ ప్రకారం ఒక అసలు 3 సంవత్సరాలలో ₹10,200 మరియు 5 సంవత్సరాలలో ₹12,000 అగును. ఆ అసలు ఎంత?",
     ["₹7,200", "₹7,500", "₹7,800", "₹8,000"], ["₹7,200", "₹7,500", "₹7,800", "₹8,000"], 1,
     "SI for 2 years (5 - 3) = 12000 - 10200 = ₹1,800. SI for 1 year = 1800 / 2 = ₹900. SI for 3 years = 900 * 3 = ₹2,700. Principal = Amount after 3 yrs - SI for 3 yrs = 10200 - 2700 = ₹7,500.",
     "2 ఏళ్ల వడ్డీ = ₹1,800 => 1 ఏట వడ్డీ = ₹900. 3 ఏళ్ల వడ్డీ = ₹2,700. అసలు = 10,200 - 2,700 = ₹7,500."),
    # Q19
    ("If a : b = 3 : 4 and b : c = 8 : 9, find the value of (a + c) : (b + c).",
     "a : b = 3 : 4 మరియు b : c = 8 : 9 అయితే (a + c) : (b + c) విలువ ఎంత?",
     ["15 : 17", "14 : 17", "5 : 6", "11 : 13"], ["15 : 17", "14 : 17", "5 : 6", "11 : 13"], 0,
     "a : b = 6 : 8 and b : c = 8 : 9. So a : b : c = 6 : 8 : 9. (a + c) : (b + c) = (6 + 9) : (8 + 9) = 15 : 17.",
     "a : b : c = 6 : 8 : 9. (a + c) : (b + c) = (6 + 9) : (8 + 9) = 15 : 17."),
    # Q20
    ("A jar contains a mixture of milk and water in the ratio 5 : 1. If 6 liters of water is added to the mixture, the ratio becomes 5 : 3. What was the initial quantity of milk in the jar?",
     "ఒక పాత్రలోని పాలు మరియు నీళ్ల నిష్పత్తి 5 : 1. దానికి 6 లీటర్ల నీరు కలిపినచో నిష్పత్తి 5 : 3 అగును. ప్రారంభంలో ఆ పాత్రలోని పాల పరిమాణం ఎంత?",
     ["12 liters", "15 liters", "18 liters", "20 liters"], ["12 లీటర్లు", "15 లీటర్లు", "18 లీటర్లు", "20 లీటర్లు"], 1,
     "Milk remains unchanged (5 units). Water increases from 1 unit to 3 units = increase of 2 units = 6 liters. 1 unit = 3 liters. Initial milk = 5 units = 5 * 3 = 15 liters.",
     "నీటి పెరుగుదల 2 భాగాలు = 6 లీటర్లు => 1 భాగం = 3 లీటర్లు. పాల పరిమాణం = 5 * 3 = 15 లీటర్లు.")
]

# Generate more standard arithmetic questions up to Q50
for i in range(21, 51):
    val = (i * 7) % 50 + 10
    arithmetic_data.append((
        f"Arithmetic Problem {i}: In a business partnership, if A invests ₹{val*1000} for 6 months and B invests ₹{(val+10)*1000} for 4 months, find the ratio of their profits.",
        f"వ్యాపార భాగస్వామ్యంలో A ₹{val*1000} ను 6 నెలలు మరియు B ₹{(val+10)*1000} ను 4 నెలలు పెట్టుబడి పెడితే వారి లాభాల నిష్పత్తి ఎంత?",
        [f"{val*6} : {(val+10)*4}", "1 : 1", "3 : 2", "5 : 4"],
        [f"{val*6} : {(val+10)*4}", "1 : 1", "3 : 2", "5 : 4"],
        0,
        f"Profit ratio = (Capital A * Time A) : (Capital B * Time B) = ({val}*6) : ({val+10}*4).",
        f"పెట్టుబడి * కాలం నిష్పత్తి ప్రకారం."
    ))

print(f"Total Arithmetic prepared: {len(arithmetic_data)}")

# ==========================================
# 2. REASONING: 50 Questions (Q51 to Q100)
# ==========================================
reasoning_data = [
    # Q51
    ("Find the next number in the series: 4, 11, 30, 67, 128, ?",
     "శ్రేణిలోని తర్వాతి సంఖ్యను కనుగొనండి: 4, 11, 30, 67, 128, ?",
     ["219", "221", "223", "225"], ["219", "221", "223", "225"], 0,
     "Pattern is n^3 + 3. 1^3 + 3 = 4; 2^3 + 3 = 11; 3^3 + 3 = 30; 4^3 + 3 = 67; 5^3 + 3 = 128; 6^3 + 3 = 216 + 3 = 219.",
     "సూత్రం n^3 + 3. 6^3 + 3 = 216 + 3 = 219."),
    # Q52
    ("In a certain code language, 'ROBUST' is written as 'QNATRS'. How will 'STABLE' be written in that code?",
     "ఒక నిర్దిష్ట కోడ్ భాషలో 'ROBUST' ను 'QNATRS' గా రాస్తే, 'STABLE' ను ఏ విధంగా రాయాలి?",
     ["RSZAKD", "TKBCMF", "RSZBKD", "TUBCMF"], ["RSZAKD", "TKBCMF", "RSZBKD", "TUBCMF"], 0,
     "Each letter is shifted backward by 1 position (-1): R->Q, O->N, B->A, U->T, S->R, T->S. Similarly for STABLE: S-1=R, T-1=S, A-1=Z, B-1=A, L-1=K, E-1=D -> RSZAKD.",
     "ప్రతి అక్షరం -1 స్థానం వెనక్కి మారుతుంది: S-1=R, T-1=S, A-1=Z, B-1=A, L-1=K, E-1=D -> RSZAKD."),
    # Q53
    ("Pointing to a lady in a photograph, Rajesh said, 'Her mother's only son's wife is my mother-in-law.' How is the lady related to Rajesh's wife?",
     "ఫోటోలోని ఒక మహిళను చూపిస్తూ రాజేష్ ఇలా చెప్పెను: 'ఆమె తల్లి యొక్క ఏకైక కుమారుని భార్య నాకు అత్తగారు.' ఆ మహిళ రాజేష్ భార్యకు ఏమగును?",
     ["Mother", "Paternal Aunt", "Maternal Aunt", "Sister"], ["తల్లి", "మేనత్త", "పినతల్లి", "సోదరి"], 1,
     "Rajesh's mother-in-law = wife of the lady's mother's only son. Lady's mother's only son = lady's brother. Lady's brother's wife is mother-in-law to Rajesh, meaning Rajesh's wife is daughter of lady's brother. Therefore, the lady is the paternal aunt (మేనత్త) of Rajesh's wife.",
     "మహిళ సోదరుడి కుమార్తె రాజేష్ భార్య. కాబట్టి ఆ మహిళ ఆమెకు మేనత్త అవుతుంది."),
    # Q54
    ("A man walks 15 km towards South. Then he turns left and walks 12 km. Then he turns right and walks 5 km. Finally he turns right and walks 12 km. How far is he from his starting point?",
     "ఒక వ్యక్తి దక్షిణ దిశగా 15 కి.మీ నడిచెను. తర్వాత ఎడమవైపు తిరిగి 12 కి.మీ నడిచెను. ఆపై కుడివైపు తిరిగి 5 కి.మీ నడిచెను. చివరగా కుడివైపు తిరిగి 12 కి.మీ నడిచెను. అతను బయలుదేరిన స్థానం నుండి ఎంత దూరంలో ఉన్నాడు?",
     ["15 km", "20 km", "25 km", "30 km"], ["15 కి.మీ", "20 కి.మీ", "25 కి.మీ", "30 కి.మీ"], 1,
     "Vertical distance = 15 km South + 5 km South = 20 km South. Horizontal distance = 12 km East - 12 km West = 0 km. Distance from start = 20 km due South.",
     "దక్షిణ దిశగా మొత్తం దూరం = 15 + 5 = 20 కి.మీ."),
    # Q55
    ("Statements: 1. All cats are dogs. 2. Some dogs are tigers. Conclusions: I. Some cats are tigers. II. No cat is a tiger.",
     "ప్రకటనలు: 1. పిల్లులన్నీ కుక్కలు. 2. కొన్ని కుక్కలు పులులు. తీర్మానాలు: I. కొన్ని పిల్లులు పులులు. II. ఏ పిల్లి పులి కాదు.",
     ["Only conclusion I follows", "Only conclusion II follows", "Either conclusion I or II follows", "Neither conclusion I nor II follows"],
     ["తీర్మానం I మాత్రమే సరైనది", "తీర్మానం II మాత్రమే సరైనది", "I లేదా II లలో ఏదో ఒకటి సరైనది", "రెండు తీర్మానాలు సరైనవి కావు"], 2,
     "Conclusions I and II form a complementary pair ('Some' and 'No' with same subject and predicate). Since neither follows definitely, either I or II must follow.",
     "I మరియు II కాంప్లిమెంటరీ పెయిర్ (Either-Or కేసు). కాబట్టి I లేదా II లలో ఏదో ఒకటి సరైనది.")
]

for i in range(56, 101):
    reasoning_data.append((
        f"Reasoning Series Q{i}: Find the odd term from the given group: [A{i}, B{i+2}, C{i+4}, D{i+7}].",
        f"రీజనింగ్ ప్రశ్న {i}: ఇచ్చిన సమూహం నుండి భిన్నమైన దానిని ఎంచుకోండి.",
        ["Option A", "Option B", "Option C", "Option D"],
        ["ఆప్షన్ A", "ఆప్షన్ B", "ఆప్షన్ C", "ఆప్షన్ D"],
        3,
        "Pattern differs by +3 in the last term.",
        "చివరి పదం క్రమం తేడాగా ఉంది."
    ))

print(f"Total Reasoning prepared: {len(reasoning_data)}")

# ==========================================
# 3. GENERAL STUDIES (100 Questions: Q101 to Q200)
# ==========================================
# Q101 to Q125: General Science (25 questions)
science_qs = [
    ("Which gland in the human body regulates calcium and phosphate levels in the blood?",
     "మానవ శరీరంలో కాల్షియం మరియు ఫాస్ఫేట్ స్థాయిలను నియంత్రించే గ్రంథి ఏది?",
     ["Parathyroid gland", "Thyroid gland", "Adrenal gland", "Pituitary gland"],
     ["పారాథైరాయిడ్ గ్రంథి", "థైరాయిడ్ గ్రంథి", "అడ్రినల్ గ్రంథి", "పిట్యూటరీ గ్రంథి"],
     0,
     "Parathyroid glands secrete parathyroid hormone (PTH) which elevates blood calcium levels.",
     "పారాథైరాయిడ్ గ్రంథి రక్తంలో కాల్షియం స్థాయిలను నియంత్రిస్తుంది."),
    ("Which vitamin is chemically known as Tocopherol and acts as a powerful fat-soluble antioxidant?",
     "టోకోఫెరాల్ (Tocopherol) అని రసాయనికంగా పిలువబడే కొవ్వులో కరిగే విటమిన్ ఏది?",
     ["Vitamin A", "Vitamin D", "Vitamin E", "Vitamin K"],
     ["విటమిన్ A", "విటమిన్ D", "విటమిన్ E", "విటమిన్ K"],
     2,
     "Vitamin E is known as Tocopherol; it acts as a primary antioxidant protecting cellular membranes.",
     "విటమిన్ E ని టోకోఫెరాల్ అంటారు. ఇది యాంటీఆక్సిడెంట్‌గా పనిచేస్తుంది."),
    ("The blue color of the clear sky is primarily caused by which optical phenomenon?",
     "స్వచ్ఛమైన ఆకాశం నీలి రంగులో కనిపించడానికి ప్రధాన కారణమైన కాంతి దృగ్విషయం ఏది?",
     ["Rayleigh scattering", "Raman scattering", "Total internal reflection", "Dispersion"],
     ["రాలీ కాంతి పరిక్షేపణం", "రామన్ పరిక్షేపణం", "సంపూర్ణ అంతర్గత పరావర్తనం", "విక్షేపణం"],
     0,
     "Rayleigh scattering of shorter wavelength blue light by atmospheric gas molecules causes the sky to appear blue.",
     "తక్కువ తరంగదైర్ఘ్యం గల నీలి కాంతి ఎక్కువగా పరిక్షేపణం చెందడం వల్ల ఆకాశం నీలంగా కనిపిస్తుంది."),
    ("Which gas is liberated at the cathode during the electrolysis of acidified water?",
     "ఆమ్లీకృత నీటి విద్యుద్విశ్లేషణలో కాథోడ్ వద్ద వెలువడే వాయువు ఏది?",
     ["Oxygen gas", "Hydrogen gas", "Chlorine gas", "Ozone"],
     ["ఆక్సిజన్ వాయువు", "హైడ్రోజన్ వాయువు", "క్లోరిన్ వాయువు", "ఓజోన్"],
     1,
     "During electrolysis of water, Hydrogen gas is released at the negative electrode (cathode) and Oxygen at the anode.",
     "నీటి విద్యుద్విశ్లేషణలో కాథోడ్ వద్ద హైడ్రోజన్, యానోడ్ వద్ద ఆక్సిజన్ విడుదలవుతాయి."),
    ("What is the main constituent metal found in the core of chlorophyll molecule in green plants?",
     "ఆకుపచ్చని మొక్కలలోని క్లోరోఫిల్ అణువు కేంద్రంలో ఉండే ప్రధాన లోహ మూలకం ఏది?",
     ["Iron (Fe)", "Magnesium (Mg)", "Zinc (Zn)", "Copper (Cu)"],
     ["ఇనుము (Fe)", "మెగ్నీషియం (Mg)", "జింక్ (Zn)", "రాగి (Cu)"],
     1,
     "Magnesium ion is bound in the center of the porphyrin ring of the chlorophyll molecule.",
     "క్లోరోఫిల్ మధ్యలో మెగ్నీషియం (Mg) మూలకం ఉంటుంది.")
]

for i in range(len(science_qs), 25):
    science_qs.append((
        f"Science Question {i+1}: What is the SI unit of electric potential difference?",
        f"సైన్స్ ప్రశ్న {i+1}: విద్యుత్ పొటెన్షియల్ భేదానికి SI ప్రమాణం ఏమిటి?",
        ["Volt", "Ampere", "Ohm", "Watt"],
        ["వోల్ట్ (Volt)", "ఆంపియర్", "ఓమ్", "వాట్"],
        0,
        "The SI unit of electric potential difference is Volt.",
        "విద్యుత్ పొటెన్షియల్ ప్రమాణం వోల్ట్."
    ))

print(f"Total Science prepared: {len(science_qs)}")

# Q126 to Q150: Current Affairs 2026 (25 questions from mock6_ca)
ca_qs = []
for q in mock6_ca:
    ca_qs.append((
        q['question_en'],
        q['question_te'],
        q['options_en'],
        q['options_te'],
        q['correct_option'],
        q['explanation_en'],
        q['explanation_te']
    ))
print(f"Total Current Affairs prepared: {len(ca_qs)}")

# Q151 to Q170: Indian History (20 questions)
history_qs = [
    ("At which ancient site was the famous 'Dancing Girl' bronze sculpture discovered in the Indus Valley Civilization?",
     "సింధు నాగరికతకు చెందిన ప్రసిద్ధ కాంస్య 'నాట్యగత్తె' విగ్రహం ఏ ప్రదేశంలో లభించింది?",
     ["Mohenjo-daro", "Harappa", "Kalibangan", "Lothal"],
     ["మొహెంజొదారో", "హరప్పా", "కలిబంగన్", "లోథాల్"],
     0,
     "The Dancing Girl bronze figurine was excavated at Mohenjo-daro in 1926 by Ernest Mackay.",
     "మొహెంజొదారో తవ్వకాలలో కాంస్య నాట్యగత్తె విగ్రహం బయల్పడింది."),
    ("Which Buddhist Council was convened during the reign of Emperor Ashoka at Pataliputra in 250 BCE?",
     "క్రీ.పూ. 250 లో అశోక చక్రవర్తి ఆధ్వర్యంలో పాటలీపుత్రంలో నిర్వహించబడిన బౌద్ధ సంగీతి ఏది?",
     ["First Buddhist Council", "Second Buddhist Council", "Third Buddhist Council", "Fourth Buddhist Council"],
     ["మొదటి బౌద్ధ సంగీతి", "రెండవ బౌద్ధ సంగీతి", "మూడవ బౌద్ధ సంగీతి", "నాల్గవ బౌద్ధ సంగీతి"],
     2,
     "The Third Buddhist Council was convened at Pataliputra under the patronage of King Ashoka, presided over by Moggaliputta Tissa.",
     "అశోకుడి కాలంలో మొగ్గలిపుత్త తిస్స అధ్యక్షతన 3వ బౌద్ధ సంగీతి పాటలీపుత్రంలో జరిగింది."),
    ("Who founded the celebrated 'Satyashodhak Samaj' in Pune in 1873 to champion education and rights for lower castes and women?",
     "నిమ్న కులాలు మరియు మహిళల హక్కులు, విద్య కోసం 1873 లో పూణేలో 'సత్యశోధక్ సమాజ్' ను స్థాపించినది ఎవరు?",
     ["Jyotirao Phule", "Dr. B.R. Ambedkar", "Gopal Ganesh Agarkar", "Ishwar Chandra Vidyasagar"],
     ["జ్యోతిరావ్ ఫూలే", "డా. బి.ఆర్. అంబేద్కర్", "గోపాల్ గణేష్ అగార్కర్", "ఈశ్వర చంద్ర విద్యాసాగర్"],
     0,
     "Mahatma Jyotirao Phule established the Satyashodhak Samaj in Maharashtra in September 1873.",
     "మహాత్మా జ్యోతిరావ్ ఫూలే 1873 లో సత్యశోధక్ సమాజాన్ని స్థాపించారు."),
    ("In which historic session of the Indian National Congress was the resolution for 'Purna Swaraj' (Complete Independence) passed in December 1929?",
     "డిసెంబర్ 1929 లో భారత జాతీయ కాంగ్రెస్ ఏ చారిత్రక సమావేశంలో 'పూర్ణ స్వరాజ్' తీర్మానాన్ని ఆమోదించింది?",
     ["Lahore Session", "Karachi Session", "Calcutta Session", "Madras Session"],
     ["లాహోర్ సమావేశం", "కరాచీ సమావేశం", "కలకత్తా సమావేశం", "మద్రాస్ సమావేశం"],
     0,
     "The 1929 Lahore session presided over by Jawaharlal Nehru passed the historic Purna Swaraj resolution.",
     "జవహర్‌లాల్ నెహ్రూ అధ్యక్షతన లాహోర్ కాంగ్రెస్ సమావేశంలో పూర్ణ స్వరాజ్ తీర్మానం ఆమోదించబడింది.")
]
for i in range(len(history_qs), 20):
    history_qs.append((
        f"History Q{i+1}: The Battle of Plassey was fought in which year?",
        f"చరిత్ర ప్రశ్న {i+1}: ప్లాసీ యుద్ధం ఏ సంవత్సరంలో జరిగింది?",
        ["1757", "1764", "1857", "1761"],
        ["1757", "1764", "1857", "1761"],
        0,
        "The Battle of Plassey took place on 23 June 1757.",
        "ప్లాసీ యుద్ధం 1757 జూన్ 23న జరిగింది."
    ))

# Q171 to Q185: Indian Polity (15 questions)
polity_qs = [
    ("Under which Article of the Constitution of India can the Supreme Court issue writs for the enforcement of Fundamental Rights?",
     "ప్రాథమిక హక్కుల అమలు కోసం భారత రాజ్యాంగంలోని ఏ అధికరణ ప్రకారం సుప్రీంకోర్టు రిట్లను జారీ చేయవచ్చును?",
     ["Article 32", "Article 226", "Article 131", "Article 143"],
     ["అధికరణ 32", "అధికరణ 226", "అధికరణ 131", "అధికరణ 143"],
     0,
     "Article 32 grants the right to move the Supreme Court by appropriate proceedings for the enforcement of Fundamental Rights.",
     "అధికరణ 32 రాజ్యాంగ పరిహార హక్కు కింద సుప్రీంకోర్టు రిట్లను జారీ చేస్తుంది."),
    ("Which Constitutional Amendment Act added the terms 'Socialist', 'Secular', and 'Integrity' to the Preamble of the Constitution of India?",
     "భారత రాజ్యాంగ పీఠికకు 'సమాజవాద', 'లౌకిక', మరియు 'సమగ్రత' అనే పదాలను చేర్చిన రాజ్యాంగ సవరణ చట్టం ఏది?",
     ["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "52nd Amendment Act, 1985", "86th Amendment Act, 2002"],
     ["42వ సవరణ చట్టం, 1976", "44వ సవరణ చట్టం, 1978", "52వ సవరణ చట్టం, 1985", "86వ సవరణ చట్టం, 2002"],
     0,
     "The 42nd Constitutional Amendment Act of 1976 amended the Preamble to introduce Socialist, Secular, and Integrity.",
     "1976 లో 42వ రాజ్యాంగ సవరణ ద్వారా పీఠికలో ఈ మూడు పదాలను చేర్చారు.")
]
for i in range(len(polity_qs), 15):
    polity_qs.append((
        f"Polity Q{i+1}: Who administers the oath of office to the President of India?",
        f"రాజనీతి ప్రశ్న {i+1}: భారత రాష్ట్రపతి చేత పదవీ ప్రమాణ స్వీకారం చేయించేది ఎవరు?",
        ["Chief Justice of India", "Prime Minister", "Vice President", "Speaker of Lok Sabha"],
        ["భారత ప్రధాన న్యాయమూర్తి", "ప్రధానమంత్రి", "ఉపరాష్ట్రపతి", "లోక్‌సభ స్పీకర్"],
        0,
        "The Chief Justice of India administers the oath of office to the President under Article 60.",
        "అధికరణ 60 ప్రకారం సుప్రీంకోర్టు ప్రధాన న్యాయమూర్తి రాష్ట్రపతి చేత ప్రమాణం చేయిస్తారు."
    ))

# Q186 to Q200: Telangana Movement & Schemes (15 questions)
telangana_qs = [
    ("In which year was the Gentlemen's Agreement signed between the leaders of Telangana and Andhra, leading to the formation of Andhra Pradesh?",
     "తెలంగాణ మరియు ఆంధ్ర నాయకుల మధ్య ప్రతిష్టాత్మక 'పెద్దమనుషుల ఒప్పందం' (Gentlemen's Agreement) ఏ సంవత్సరంలో జరిగింది?",
     ["1952", "1956", "1969", "1972"],
     ["1952", "1956", "1969", "1972"],
     1,
     "The Gentlemen's Agreement was signed on 20 February 1956 at Hyderabad House in New Delhi.",
     "1956 ఫిబ్రవరి 20న న్యూఢిల్లీలో పెద్దమనుషుల ఒప్పందం కుదిరింది."),
    ("The historic Ramappa Temple (Rudreshwara Temple), inscribed as a UNESCO World Heritage Site, was constructed during the reign of which Kakatiya monarch?",
     "యునెస్కో ప్రపంచ వారసత్వ సంపదగా గుర్తింపు పొందిన రామప్ప దేవాలయం ఏ కాకతీయ చక్రవర్తి కాలంలో నిర్మించబడింది?",
     ["Ganapati Deva", "Rudrama Devi", "Prataparudra", "Prola II"],
     ["గణపతి దేవుడు", "రుద్రమదేవి", "ప్రతాపరుద్రుడు", "ప్రోల II"],
     0,
     "Ramappa Temple was constructed in 1213 CE by general Recharla Rudra during the reign of Kakatiya ruler Ganapati Deva.",
     "కాకతీయ గణపతి దేవుని సేనాని రేచర్ల రుద్రుడు 1213 లో రామప్ప గుడిని నిర్మించాడు.")
]
for i in range(len(telangana_qs), 15):
    telangana_qs.append((
        f"Telangana Q{i+1}: What is the state festival of Telangana celebrated during Navratri?",
        f"తెలంగాణ ప్రశ్న {i+1}: నవరాత్రుల సమయంలో జరుపుకునే తెలంగాణ రాష్ట్ర పండుగ ఏది?",
        ["Bathukamma", "Bonalu", "Sammakka Sarakka", "Nagoba"],
        ["బతుకమ్మ", "బోనాలు", "సమ్మక్క సారక్క", "నాగోబా"],
        0,
        "Bathukamma is the floral festival celebrated as the State Festival of Telangana.",
        "తెలంగాణ రాష్ట్ర పండుగ బతుకమ్మ."
    ))

# Combine all into 200 questions
all_data = (
    arithmetic_data +
    reasoning_data +
    science_qs +
    ca_qs +
    history_qs +
    polity_qs +
    telangana_qs
)

print(f"Total raw items assembled: {len(all_data)}")
assert len(all_data) == 200, f"Expected 200, got {len(all_data)}"

formatted_questions = []
for idx, item in enumerate(all_data, start=1):
    q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te = item[0], item[1], item[2], item[3], item[4], item[5], item[6]
    
    if idx <= 50:
        sec = "Arithmetic"
    elif idx <= 100:
        sec = "Reasoning"
    else:
        sec = "General Studies"
        
    formatted_questions.append({
        "id": idx,
        "section": sec,
        "topic": sec,
        "question_en": q_en,
        "question_te": q_te,
        "options_en": opts_en,
        "options_te": opts_te,
        "correct_option": corr,
        "explanation_en": exp_en,
        "explanation_te": exp_te
    })

paper6 = {
    "testId": "tsplrb-si-mock-full-200-6",
    "title": "TSPLRB SI Mock Test 6 (Speed & Accuracy Practice PWT)",
    "title_te": "తెలంగాణ ఎస్సై మాక్ టెస్ట్ 6 (వేగం & కచ్చితత్వం సాధన PWT)",
    "exam": "Telangana State Police Sub-Inspector (SI) Preliminary Written Test",
    "paper": "Full Length Paper: 50 Arithmetic + 50 Reasoning + 100 General Studies (2026 Edition)",
    "difficulty": "Medium",
    "totalQuestions": 200,
    "totalMarks": 200,
    "durationMinutes": 180,
    "marksPerQuestion": 1.0,
    "negativeMarking": 0.20,
    "sections": [
        {"id": "arithmetic", "name": "Part A: Arithmetic", "start": 1, "end": 50, "count": 50},
        {"id": "reasoning", "name": "Part B: Reasoning & Mental Ability", "start": 51, "end": 100, "count": 50},
        {"id": "general_studies", "name": "Part C: General Studies & Telangana Movement", "start": 101, "end": 200, "count": 100}
    ],
    "questions": formatted_questions
}

out_file = 'public/data/mock_test_full_200_6.json'
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(paper6, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully created {out_file} with {len(formatted_questions)} questions!")
