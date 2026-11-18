import json
import re
import os

print("=== APPLYING SHENTU'S RECOMMENDATIONS TO MOCK DATA ===")

# -------------------------------------------------------------
# 1. CLEAN MOCK 5 (Strip [Advanced Calculation], etc. & Fix Q38)
# -------------------------------------------------------------
mock5_path = 'public/data/mock_test_full_200_5.json'
with open(mock5_path) as f:
    mock5_data = json.load(f)

q5 = mock5_data.get('questions', mock5_data)

pattern_en = re.compile(r'^\s*\[(Advanced Calculation|Analytical|Multi-Step Puzzle)\]\s*', re.IGNORECASE)
pattern_te = re.compile(r'^\s*\[(క్లిష్టమైన సమస్య|విశ్లేషణాత్మక|బహుళ-దశల పజిల్)\]\s*')

cleaned_en, cleaned_te = 0, 0
for q in q5:
    if 'question_en' in q and pattern_en.search(q['question_en']):
        q['question_en'] = pattern_en.sub('', q['question_en']).strip()
        cleaned_en += 1
    if 'question_te' in q and pattern_te.search(q['question_te']):
        q['question_te'] = pattern_te.sub('', q['question_te']).strip()
        cleaned_te += 1

# Replace Q38 (index 37) with Calendar Repetition 2024
q5[37] = {
    "id": 38,
    "qNumber": 38,
    "section": "Reasoning",
    "topic": "Reasoning & Mental Ability - Calendar",
    "question_en": "Which future year will have the exact same calendar as the year 2024?",
    "question_te": "2024 సంవత్సరానికి సంబంధించిన క్యాలెండర్ భవిష్యత్తులో ఏ సంవత్సరపు క్యాలెండర్‌తో సరిగ్గా సమానంగా ఉంటుంది?",
    "options_en": [
        "2030",
        "2052",
        "2048",
        "2035"
    ],
    "options_te": [
        "2030",
        "2052",
        "2048",
        "2035"
    ],
    "correct_option": 1,
    "explanation_en": "The year 2024 is a leap year. A leap year calendar repeats after 28 years (or multiples of 28 when no non-leap century year intervenes). Therefore, 2024 + 28 = 2052. The calendar for 2052 will be identical to 2024 (same starting day and 366 days).",
    "explanation_te": "2024 ఒక లీపు సంవత్సరం. లీపు సంవత్సరం క్యాలెండర్ సాధారణంగా 28 సంవత్సరాల తర్వాత పునరావృతమవుతుంది (2024 + 28 = 2052). కాబట్టి 2052 క్యాలెండర్ 2024తో పూర్తిగా సరిపోలుతుంది."
}

with open(mock5_path, 'w', encoding='utf-8') as f:
    json.dump(mock5_data, f, ensure_ascii=False, indent=2)

print(f"Mock 5 updated: Cleaned {cleaned_en} EN & {cleaned_te} TE prefixes, replaced Q38 with Calendar Repetition 2024.")


# -------------------------------------------------------------
# 2. FIX MOCK 3 (Q196 and Q200 formatting & differentiation)
# -------------------------------------------------------------
mock3_path = 'public/data/mock_test_full_200_3.json'
with open(mock3_path) as f:
    mock3_data = json.load(f)

q3 = mock3_data.get('questions', mock3_data)

q3[195]['question_en'] = """Match List-I (Scheme) with List-II (Objective):

List-I (Scheme):
a. Pradhan Mantri Kaushal Vikas Yojana (PMKVY)
b. Prime Minister's Rozgar Yojana (PMRY)
c. Deen Dayal Upadhyaya Grameen Kaushalya Yojana (DDGKY)
d. Aajeevika (National Rural Livelihoods Mission)

List-II (Objective):
i. Providing requisite skills to poor for managing their institutions
ii. Encouraging skill development for youth by providing monetary rewards
iii. Converting India's demographic surplus into a demographic dividend
iv. Providing self-employment to educated unemployed youth

Select the correct matching code:"""

q3[195]['question_te'] = """జాబితా-I (పథకం) ను జాబితా-II (లక్ష్యం) తో జతపరచండి:

జాబితా-I (పథకం):
a. ప్రధానమంత్రి కౌశల్ వికాస్ యోజన (PMKVY)
b. ప్రధానమంత్రి రోజ్‌గార్ యోజన (PMRY)
c. దీన్ దయాళ్ ఉపాధ్యాయ గ్రామీణ్ కౌశల్య యోజన (DDGKY)
d. ఆజీవిక (NRLM)

జాబితా-II (లక్ష్యం):
i. పేదవారికి వారి సంస్థల నిర్వహణకు అవసరమైన నైపుణ్యాలను కల్పించుట
ii. నగదు ప్రోత్సాహకాలు కల్పించుట ద్వారా యువతలో నైపుణ్యాభివృద్ధిని ప్రోత్సహించుట
iii. భారతదేశ జనాభా మిగులును డెమోగ్రాఫిక్ డివిడెండ్‌గా మార్చుట
iv. చదువుకున్న నిరుద్యోగ యువతకు స్వయం ఉపాధి కల్పన

సరైన కోడ్‌ను ఎంచుకోండి:"""

q3[199]['question_en'] = """Match List-I (Economic Policy / Reform) with List-II (Primary Aim):

List-I (Economic Policy / Reform):
a. Insolvency and Bankruptcy Code (IBC)
b. Public Sector Bank Recapitalization Package
c. Demonetisation and GST Implementation
d. Mission Indradhanush for PSBs

List-II (Primary Aim):
i. Assisting corporates to clean balance sheets and resolve non-performing assets (NPAs)
ii. Strengthening capital adequacy ratios and balance sheets of Public Sector Banks
iii. Expanding formalization and increasing the number of registered tax filers
iv. Multi-pronged governance and performance revitalization of public sector banks

Select the correct matching code:"""

q3[199]['question_te'] = """జాబితా-I (ఆర్థిక సంస్కరణ) ను జాబితా-II (ప్రాథమిక లక్ష్యం) తో జతపరచండి:

జాబితా-I (ఆర్థిక విధానం):
a. భారతీయ నూతన దివాళా కోడ్ (IBC)
b. ప్రభుత్వ రంగ బ్యాంకుల రీ-క్యాపిటలైజేషన్ ప్యాకేజీ
c. డీమానిటైజేషన్ మరియు GST అమలు
d. మిషన్ ఇంద్రధనుష్

జాబితా-II (లక్ష్యం):
i. కార్పొరేట్ సంస్థల ఆస్తి-అప్పుల పట్టికల ప్రక్షాళన మరియు మొండి బకాయిల పరిష్కారం
ii. ప్రభుత్వ రంగ బ్యాంకుల మూలధన సమృద్ధిని, ఆస్తి-అప్పుల పట్టికను బలోపేతం చేయడం
iii. వ్యవస్థీకృత ఆర్థిక వృద్ధి మరియు పన్ను చెల్లింపుదారుల సంఖ్యలో గణనీయమైన పెరుగుదల
iv. ప్రభుత్వ రంగ బ్యాంకుల సమగ్ర నిర్వహణ మరియు పాలన సంస్కరణలు

సరైన సమాధానం ఎంపిక చేయండి:"""

with open(mock3_path, 'w', encoding='utf-8') as f:
    json.dump(mock3_data, f, ensure_ascii=False, indent=2)

print("Mock 3 updated: Q196 & Q200 completely distinct and cleanly formatted.")


# -------------------------------------------------------------
# 3. UPDATE MOCK 6 (Add Calendar Repetition 2017 at Q75)
# -------------------------------------------------------------
mock6_path = 'public/data/mock_test_full_200_6.json'
with open(mock6_path) as f:
    mock6_data = json.load(f)

q6 = mock6_data.get('questions', mock6_data)
q6[74] = {
    "id": 75,
    "qNumber": 75,
    "section": "Reasoning",
    "topic": "Reasoning & Mental Ability - Calendar",
    "question_en": "Which year will have the exact same calendar as the year 2017?",
    "question_te": "2017 సంవత్సరపు క్యాలెండర్‌తో సరిగ్గా సమానమైన క్యాలెండర్ క్రింది ఏ సంవత్సరంలో వస్తుంది?",
    "options_en": [
        "2022",
        "2023",
        "2028",
        "2025"
    ],
    "options_te": [
        "2022",
        "2023",
        "2028",
        "2025"
    ],
    "correct_option": 1,
    "explanation_en": "2017 is an ordinary year that immediately follows a leap year (2016 + 1). An ordinary year of the form (Leap Year + 1) repeats its calendar after 6 years: 2017 + 6 = 2023. Total odd days between 2017 and 2023 = 1+1+1+2+1+1 = 7 odd days = 0 odd days.",
    "explanation_te": "2017 అనేది లీపు సంవత్సరం (2016) తర్వాత వచ్చే సాధారణ సంవత్సరం (లీపు + 1). (లీపు + 1) సంవత్సరం క్యాలెండర్ 6 సంవత్సరాల తర్వాత పునరావృతమవుతుంది: 2017 + 6 = 2023. ఈ కాలంలో అదనపు రోజుల మొత్తం 7 (7/7 = 0 శేషం)."
}

with open(mock6_path, 'w', encoding='utf-8') as f:
    json.dump(mock6_data, f, ensure_ascii=False, indent=2)

print("Mock 6 updated: Added Calendar Repetition 2017 at Q75.")


# -------------------------------------------------------------
# 4. UPDATE MOCK 8 (Add Calendar Repetition 2019 at Q76)
# -------------------------------------------------------------
mock8_path = 'public/data/mock_test_full_200_8.json'
with open(mock8_path) as f:
    mock8_data = json.load(f)

q8 = mock8_data.get('questions', mock8_data)
q8[75] = {
    "id": 76,
    "qNumber": 76,
    "section": "Reasoning",
    "topic": "Reasoning & Mental Ability - Calendar",
    "question_en": "Which year will have the exact same calendar as the year 2019?",
    "question_te": "2019 సంవత్సరపు క్యాలెండర్‌తో సరిగ్గా సరిపోలే క్యాలెండర్ క్రింది ఏ సంవత్సరంలో వస్తుంది?",
    "options_en": [
        "2028",
        "2030",
        "2031",
        "2025"
    ],
    "options_te": [
        "2028",
        "2030",
        "2031",
        "2025"
    ],
    "correct_option": 1,
    "explanation_en": "2019 is an ordinary year of the form (Leap Year + 3), since 2016 was a leap year. Years of the form (Leap Year + 2 or 3) repeat their calendar after 11 years: 2019 + 11 = 2030. Cumulative odd days from 2019 to 2030 = 1+2+1+1+1+2+1+1+1+2+1 = 14 odd days = 0 remainder mod 7.",
    "explanation_te": "2019 అనేది లీపు సంవత్సరం (2016) తర్వాత 3వ సాధారణ సంవత్సరం (లీపు + 3). ఇటువంటి సంవత్సరాల క్యాలెండర్ 11 సంవత్సరాల తర్వాత పునరావృతమవుతుంది: 2019 + 11 = 2030. ఈ మధ్య కాలంలో అదనపు రోజుల మొత్తం 14 (14/7 = 0 శేషం)."
}

with open(mock8_path, 'w', encoding='utf-8') as f:
    json.dump(mock8_data, f, ensure_ascii=False, indent=2)

print("Mock 8 updated: Added Calendar Repetition 2019 at Q76.")


# -------------------------------------------------------------
# 5. UPDATE MOCK 9 (Add Calendar Repetition 2025 at Q75)
# -------------------------------------------------------------
mock9_path = 'public/data/mock_test_full_200_9.json'
with open(mock9_path) as f:
    mock9_data = json.load(f)

q9 = mock9_data.get('questions', mock9_data)
q9[74] = {
    "id": 75,
    "qNumber": 75,
    "section": "Reasoning",
    "topic": "Reasoning & Mental Ability - Calendar",
    "question_en": "The calendar for the year 2025 will be identical to which of the following future years?",
    "question_te": "2025 సంవత్సరపు క్యాలెండర్ క్రింది ఏ భవిష్యత్ సంవత్సర క్యాలెండర్‌తో ఖచ్చితంగా ఒకే విధంగా ఉంటుంది?",
    "options_en": [
        "2030",
        "2031",
        "2036",
        "2032"
    ],
    "options_te": [
        "2030",
        "2031",
        "2036",
        "2032"
    ],
    "correct_option": 1,
    "explanation_en": "2025 is (Leap Year + 1), since 2024 is a leap year. Any ordinary year that falls immediately after a leap year repeats after 6 years: 2025 + 6 = 2031. Both years start on Wednesday and have 365 days.",
    "explanation_te": "2025 అనేది లీపు సంవత్సరం (2024) తర్వాత వచ్చే సంవత్సరం (లీపు + 1). లీపు సంవత్సరం తర్వాత వెంటనే వచ్చే సాధారణ సంవత్సరం క్యాలెండర్ 6 సంవత్సరాల తర్వాత పునరావృతమవుతుంది: 2025 + 6 = 2031."
}

with open(mock9_path, 'w', encoding='utf-8') as f:
    json.dump(mock9_data, f, ensure_ascii=False, indent=2)

print("Mock 9 updated: Added Calendar Repetition 2025 at Q75.")

print("=== ALL MOCK FILES UPDATED SUCCESSFULLY ===")
