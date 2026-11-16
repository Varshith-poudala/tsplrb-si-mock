#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updates Mock Test 1 (mock_test_full_200.json) and Mock Test 3 (mock_test_full_200_3.json)
by replacing outdated 2024 Current Affairs questions (Q103 to Q113) with fresh 2026 Current Affairs
questions extracted directly from the user's provided YouTube video:
https://youtu.be/wSUFFsHf0gc (2026 Important 800+ Current Affairs In Telugu - Telugu Share Knowledge).
"""

import json
import os

new_ca_2026 = [
    # Q103: Forex Reserves 2026
    {
        "id": 103,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - Indian Economy",
        "question_en": "In 2026, India's foreign exchange reserves crossed $700 billion, surpassing Russia to become the world's fourth-largest holder of forex reserves. Which three countries hold the top three positions globally?",
        "question_te": "2026 లో భారత విదేశీ మారక నిల్వలు (Forex Reserves) 700 బిలియన్ డాలర్లను దాటి రష్యాను అధిగమించి ప్రపంచంలో 4వ స్థానానికి చేరుకున్నాయి. ప్రపంచంలో మొదటి మూడు స్థానాల్లో ఉన్న దేశాలు ఏవి?",
        "options_en": ["China, Japan, and Switzerland", "USA, China, and Germany", "Japan, Germany, and Saudi Arabia", "China, UK, and France"],
        "options_te": ["చైనా, జపాన్, మరియు స్విట్జర్లాండ్", "అమెరికా, చైనా, మరియు జర్మనీ", "జపాన్, జర్మనీ, మరియు సౌదీ అరేబియా", "చైనా, యూకే, మరియు ఫ్రాన్స్"],
        "correct_option": 0,
        "explanation_en": "India's foreign exchange reserves rose above $700 billion in 2026, overtaking Russia to secure the 4th rank globally, behind China (1st), Japan (2nd), and Switzerland (3rd).",
        "explanation_te": "2026 లో భారత ఫారెక్స్ నిల్వలు రష్యాను వెనక్కి నెట్టి ప్రపంచంలోనే 4వ స్థానానికి చేరాయి. చైనా, జపాన్, స్విట్జర్లాండ్ మొదటి 3 స్థానాల్లో ఉన్నాయి."
    },
    # Q104: Senior Citizens Budget 2026
    {
        "id": 104,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - State Welfare Initiatives",
        "question_en": "Which Indian state became the first in the country to present a dedicated 'Senior Citizens Budget' to address elder care, pensions, and healthcare?",
        "question_te": "వృద్ధుల సంక్షేమం, పెన్షన్లు మరియు వైద్య సేవల కోసం ప్రత్యేకంగా 'సీనియర్ సిటిజెన్స్ బడ్జెట్' (Senior Citizens Budget) ను ప్రవేశపెట్టిన భారతదేశపు తొలి రాష్ట్రం ఏది?",
        "options_en": ["Kerala", "Tamil Nadu", "Karnataka", "Maharashtra"],
        "options_te": ["కేరళ", "తమిళనాడు", "కర్ణాటక", "మహారాష్ట్ర"],
        "correct_option": 0,
        "explanation_en": "Kerala became the first state in India to introduce a dedicated Senior Citizens Budget allocating targeted resources for geriatric healthcare and old-age welfare.",
        "explanation_te": "వృద్ధుల వైద్యం మరియు సంక్షేమం కోసం ప్రత్యేకంగా సీనియర్ సిటిజెన్స్ బడ్జెట్‌ను ప్రవేశపెట్టిన తొలి రాష్ట్రంగా కేరళ నిలిచింది."
    },
    # Q105: MoSPI CPI Base Year Revision
    {
        "id": 105,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - Economic Indicators",
        "question_en": "The Ministry of Statistics and Programme Implementation (MoSPI) announced the revision of the base year for the Consumer Price Index (CPI) from 2012 to which new base year?",
        "question_te": "వినియోగదారుల ధరల సూచి (CPI) ఆధార సంవత్సరాన్ని 2012 నుండి ఏ సంవత్సరానికి సవరించాలని గణాంకాల మంత్రిత్వ శాఖ (MoSPI) నిర్ణయించింది?",
        "options_en": ["2024", "2020", "2022", "2025"],
        "options_te": ["2024", "2020", "2022", "2025"],
        "correct_option": 0,
        "explanation_en": "MoSPI revised the CPI base year from 2012 to 2024 based on the latest Household Consumption Expenditure Survey to accurately reflect modern consumer expenditure.",
        "explanation_te": "సరికొత్త గృహ వినియోగ వ్యయ సర్వే ఆధారంగా కన్స్యూమర్ ప్రైస్ ఇండెక్స్ (CPI) ఆధార సంవత్సరాన్ని 2012 నుండి 2024కి మార్చారు."
    },
    # Q106: PM Modi 1st International Visit 2026
    {
        "id": 106,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - Bilateral Relations",
        "question_en": "Which Southeast Asian country did Prime Minister Narendra Modi visit on his first official bilateral overseas tour of 2026?",
        "question_te": "2026 లో ప్రధానమంత్రి నరేంద్ర మోదీ తన తొలి అధికారిక ద్వైపాక్షిక విదేశీ పర్యటనలో భాగంగా ఏ ఆగ్నేయాసియా దేశాన్ని సందర్శించారు?",
        "options_en": ["Malaysia", "Singapore", "Vietnam", "Indonesia"],
        "options_te": ["మలేషియా", "సింగపూర్", "వియత్నాం", "ఇండోనేషియా"],
        "correct_option": 0,
        "explanation_en": "Prime Minister Modi undertook his first official bilateral foreign visit of 2026 to Malaysia, upgrading diplomatic ties to an Enhanced Strategic Partnership.",
        "explanation_te": "2026 లో ప్రధాని మోదీ తన తొలి ద్వైపాక్షిక విదేశీ పర్యటనలో మలేషియాను సందర్శించి ద్వైపాక్షిక సంబంధాలను బలోపేతం చేశారు."
    },
    # Q107: 77th Republic Day 2026 Chief Guests
    {
        "id": 107,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - National Celebrations",
        "question_en": "Who were the Chief Guests at India's 77th Republic Day celebrations held in New Delhi?",
        "question_te": "న్యూఢిల్లీలో జరిగిన భారతదేశపు 77వ గణతంత్ర దినోత్సవ వేడుకలకు ముఖ్య అతిథులుగా ఎవరు విచ్చేశారు?",
        "options_en": [
            "António Costa (President of European Council) and Ursula von der Leyen (President of European Commission)",
            "Emmanuel Macron (President of France)",
            "Luiz Inácio Lula da Silva (President of Brazil)",
            "Cyril Ramaphosa (President of South Africa)"
        ],
        "options_te": [
            "ఆంటోనియో కోస్టా (యూరోపియన్ కౌన్సిల్ అధ్యక్షుడు) మరియు ఉర్సులా వాన్ డెర్ లేయెన్ (యూరోపియన్ కమిషన్ అధ్యక్షురాలు)",
            "ఇమ్మాన్యుయేల్ మాక్రాన్ (ఫ్రాన్స్ అధ్యక్షుడు)",
            "లులా డా సిల్వా (బ్రెజిల్ అధ్యక్షుడు)",
            "సిరిల్ రామఫోసా (దక్షిణాఫ్రికా అధ్యక్షుడు)"
        ],
        "correct_option": 0,
        "explanation_en": "European Council President António Costa and European Commission President Ursula von der Leyen attended India's 77th Republic Day as joint Chief Guests.",
        "explanation_te": "యూరోపియన్ కౌన్సిల్ ప్రెసిడెంట్ ఆంటోనియో కోస్టా మరియు యూరోపియన్ కమిషన్ ప్రెసిడెంట్ ఉర్సులా వాన్ డెర్ లేయెన్ 77వ గణతంత్ర వేడుకలకు సంయుక్త ముఖ్య అతిథులుగా హాజరయ్యారు."
    },
    # Q108: Asian Games 2026 Women's Trap Gold
    {
        "id": 108,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - Sports: Shooting",
        "question_en": "Who became the first Indian woman shooter to win a gold medal in the individual Women's Trap event at the 2026 Asian Games?",
        "question_te": "2026 ఆసియా క్రీడలలో మహిళల వ్యక్తిగత ట్రాప్ (Women's Trap) షూటింగ్ ఈవెంట్‌లో స్వర్ణ పతకం సాధించిన తొలి భారతీయ మహిళగా ఎవరు నిలిచారు?",
        "options_en": ["Niru Dhanda", "Manu Bhaker", "Esha Singh", "Sift Kaur Samra"],
        "options_te": ["నీరు దండా", "మను భాకర్", "ఇషా సింగ్", "సిఫ్ట్ కౌర్ సమ్రా"],
        "correct_option": 0,
        "explanation_en": "Niru Dhanda made history by winning India's first-ever gold medal in the individual Women's Trap event at the Asian Games.",
        "explanation_te": "మహిళల వ్యక్తిగత ట్రాప్ షూటింగ్‌లో నీరు దండా స్వర్ణ పతకం గెలుచుకుని ఆసియా క్రీడల్లో ఈ ఘనత సాధించిన తొలి భారత మహిళగా రికార్డు సృష్టించింది."
    },
    # Q109: Padma Awards 2026
    {
        "id": 109,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - National Honours",
        "question_en": "How many eminent personalities were approved for the conferment of Padma Awards (Padma Vibhushan, Padma Bhushan, Padma Shri) by the President of India in 2026?",
        "question_te": "2026 లో భారత రాష్ట్రపతి మొత్తం ఎంతమంది ప్రముఖులకు పద్మ పురస్కారాలను (పద్మవిభూషణ్, పద్మభూషణ్, పద్మశ్రీ) ప్రకటించారు?",
        "options_en": ["131 awardees (5 Padma Vibhushan, 17 Padma Bhushan, 109 Padma Shri)", "106 awardees", "128 awardees", "141 awardees"],
        "options_te": ["131 మంది (5 పద్మవిభూషణ్, 17 పద్మభూషణ్, 109 పద్మశ్రీ)", "106 మంది", "128 మంది", "141 మంది"],
        "correct_option": 0,
        "explanation_en": "The President approved 131 Padma Awards for 2026: 5 Padma Vibhushan, 17 Padma Bhushan, and 109 Padma Shri.",
        "explanation_te": "2026 లో మొత్తం 131 మందికి పద్మ పురస్కారాలు లభించాయి (5 పద్మవిభూషణ్, 17 పద్మభూషణ్, 109 పద్మశ్రీ)."
    },
    # Q110: Uzbekistan Highest Civilian Award 2026
    {
        "id": 110,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - International Honours",
        "question_en": "Which Central Asian nation conferred its highest state civilian honour, the 'Order of Supreme Friendship' (Oliy Darajali Do'stlik), upon Prime Minister Narendra Modi in August 2026?",
        "question_te": "2026 ఆగస్టులో ప్రధానమంత్రి నరేంద్ర మోదీకి తమ అత్యున్నత పౌర పురస్కారమైన 'ఆర్డర్ ఆఫ్ సుప్రీం ఫ్రెండ్‌షిప్' (ఓలీ దరజాలి దోస్త్లిక్) ను ప్రదానం చేసిన దేశం ఏది?",
        "options_en": ["Uzbekistan", "Kazakhstan", "Turkmenistan", "Tajikistan"],
        "options_te": ["ఉజ్బెకిస్తాన్", "కజకిస్తాన్", "తుర్క్‌మెనిస్తాన్", "తజికిస్తాన్"],
        "correct_option": 0,
        "explanation_en": "Uzbekistan honoured PM Narendra Modi with its highest decoration, 'Oliy Darajali Do'stlik', for strengthening bilateral cooperation and mutual friendship.",
        "explanation_te": "భారత్-ఉజ్బెకిస్తాన్ సంబంధాలను బలోపేతం చేసినందుకు గాను ఉజ్బెకిస్తాన్ ప్రభుత్వం ప్రధాని మోదీకి తమ అత్యున్నత పురస్కారమైన 'ఓలీ దరజాలి దోస్త్లిక్' ను ప్రదానం చేసింది."
    },
    # Q111: 72nd National Film Awards 2026
    {
        "id": 111,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - Cinema & Culture",
        "question_en": "Which movie was adjudged the Best Feature Film at the 72nd National Film Awards 2026?",
        "question_te": "72వ జాతీయ చలనచిత్ర పురస్కారాలు 2026 లో 'ఉత్తమ చలన చిత్రం' (Best Feature Film) అవార్డును గెలుచుకున్న చిత్రం ఏది?",
        "options_en": ["Article 370", "Chandu Champion", "Kalki 2898 AD", "Captain Miller"],
        "options_te": ["ఆర్టికల్ 370", "చందూ ఛాంపియన్", "కల్కి 2898 AD", "కెప్టెన్ మిల్లర్"],
        "correct_option": 0,
        "explanation_en": "'Article 370' won the Best Feature Film honour at the 72nd National Film Awards 2026.",
        "explanation_te": "72వ జాతీయ చలనచిత్ర పురస్కారాలలో 'ఆర్టికల్ 370' ఉత్తమ చలన చిత్రంగా స్వర్ణ కమలాన్ని దక్కించుకుంది."
    },
    # Q112: Saraswati Samman 2026
    {
        "id": 112,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - Literature & Awards",
        "question_en": "Who was conferred with the prestigious literary award 'Saraswati Samman 2026' instituted by the K.K. Birla Foundation?",
        "question_te": "కె.కె. బిర్లా ఫౌండేషన్ అందించే ప్రతిష్టాత్మక సాహిత్య పురస్కారం 'సరస్వతి సమ్మాన్ 2026' ఎవరికి లభించింది?",
        "options_en": ["Rajkumar Mukhopadhyay", "Prabha Varma", "Sivasankari", "Ramdarash Mishra"],
        "options_te": ["రాజ్‌కుమార్ ముఖోపాధ్యాయ్", "ప్రభా వర్మ", "శివశంకరి", "రామ్‌దరశ్ మిశ్రా"],
        "correct_option": 0,
        "explanation_en": "Eminent litterateur Rajkumar Mukhopadhyay was honoured with the Saraswati Samman 2026 for outstanding literary contributions.",
        "explanation_te": "ప్రముఖ రచయిత రాజ్‌కుమార్ ముఖోపాధ్యాయ్‌కు 2026 సరస్వతి సమ్మాన్ పురస్కారం లభించింది."
    },
    # Q113: National Lata Mangeshkar Award 2026
    {
        "id": 113,
        "section": "General Studies",
        "topic": "Current Affairs 2026 - Music & Honours",
        "question_en": "Who was selected for the prestigious National Lata Mangeshkar Award in 2026 for lifetime contributions to Indian music?",
        "question_te": "భారతీయ సంగీత రంగానికి చేసిన విశేష సేవలకు గాను 2026 లో ప్రతిష్టాత్మక 'జాతీయ లతా మంగేష్కర్ పురస్కారం' ఎవరికి దక్కింది?",
        "options_en": ["Shantanu Moitra", "Uttam Singh", "Kumar Sanu", "Anand-Milind"],
        "options_te": ["శంతను మోయిత్రా", "ఉత్తమ్ సింగ్", "కుమార్ సాను", "ఆనంద్-మిలింద్"],
        "correct_option": 0,
        "explanation_en": "Renowned music director Shantanu Moitra was conferred the National Lata Mangeshkar Award in 2026.",
        "explanation_te": "ప్రఖ్యాత సంగీత దర్శకుడు శంతను మోయిత్రాకు 2026 జాతీయ లతా మంగేష్కర్ పురస్కారం లభించింది."
    }
]

target_files = [
    'public/data/mock_test_full_200.json',
    'public/data/mock_test_full_200_3.json'
]

for file_rel in target_files:
    file_path = os.path.join(os.path.dirname(__file__), '..', file_rel)
    if not os.path.exists(file_path):
        print(f"Skipping {file_rel} (not found)")
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data['questions']
    q_map = {q['id']: q for q in questions}

    # Replace Q103 to Q113
    for update_q in new_ca_2026:
        qid = update_q['id']
        if qid in q_map:
            q_map[qid]['topic'] = update_q['topic']
            q_map[qid]['question_en'] = update_q['question_en']
            q_map[qid]['question_te'] = update_q['question_te']
            q_map[qid]['options_en'] = update_q['options_en']
            q_map[qid]['options_te'] = update_q['options_te']
            q_map[qid]['correct_option'] = update_q['correct_option']
            q_map[qid]['explanation_en'] = update_q['explanation_en']
            q_map[qid]['explanation_te'] = update_q['explanation_te']

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully updated 2026 CA in {file_rel}!")

if __name__ == '__main__':
    print("Update script ready.")
