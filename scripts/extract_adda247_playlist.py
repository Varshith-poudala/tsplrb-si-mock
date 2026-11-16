#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extraction and Enhancement of Questions from Adda247 Telugu (Suryadeep Sir)
Playlist: https://www.youtube.com/playlist?list=PLNOSFzLA9zoqz0kdVMRbRNt7ROUS688W1
Video: IAUqxNsGV1Y (13 November Current Affairs 2026 | Daily Current Affairs for APPSC/TGPSC/UPSC)
"""

import json
import os

OUTPUT_FILE = "public/data/extracted_adda247_suryadeep_questions.json"

def extract_playlist_questions():
    questions = [
        # 1. 51st Chief Justice of India Appointment (Judiciary & Polity)
        {
            "id": 101,
            "subject": "Indian Polity & Constitutional Governance",
            "topic": "Supreme Court - Appointment of the 51st Chief Justice of India",
            "source_playlist": "https://www.youtube.com/playlist?list=PLNOSFzLA9zoqz0kdVMRbRNt7ROUS688W1",
            "source_video": "https://www.youtube.com/watch?v=IAUqxNsGV1Y",
            "educator": "Suryadeep Sir (Adda247 Telugu)",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the appointment and constitutional tenure of the Chief Justice of India (CJI):\n1. Under Article 124(2) of the Constitution, the Chief Justice of India is appointed by the President by warrant under his hand and seal.\n2. By convention, the outgoing CJI recommends the name of the senior-most puisne judge of the Supreme Court considered fit to hold the office.\n3. A judge of the Supreme Court holds office until attaining the age of 65 years.\nWhich of the statements given above are correct?",
            "question_te": "భారత ప్రధాన న్యాయమూర్తి (CJI) నియామకం మరియు రాజ్యాంగబద్ధమైన పదవీకాలానికి సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. భారత రాజ్యాంగంలోని ఆర్టికల్ 124(2) ప్రకారం భారత ప్రధాన న్యాయమూర్తిని రాష్ట్రపతి తన సంతకం మరియు రాజముద్రతో కూడిన వారెంట్ ద్వారా నియమిస్తారు.\n2. ఆనవాయితీ ప్రకారం పదవీ విరమణ చేస్తున్న ప్రస్తుత సీజేఐ, సుప్రీంకోర్టులోని అత్యంత సీనియర్ న్యాయమూర్తి పేరును కేంద్ర న్యాయశాఖకు సిఫార్సు చేస్తారు.\n3. సుప్రీంకోర్టు న్యాయమూర్తి 65 సంవత్సరాల వయస్సు పూర్తయ్యే వరకు పదవిలో కొనసాగుతారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three statements are correct. Justice Sanjiv Khanna was appointed as the 51st Chief Justice of India succeeding Justice D.Y. Chandrachud. Article 124(2) mandates presidential appointment based on the Memorandum of Procedure (MoP), and Supreme Court judges retire at 65 years.",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. జస్టిస్ డి.వై. చంద్రచూడ్ పదవీ విరమణ అనంతరం జస్టిస్ సంజీవ్ ఖన్నా భారతదేశ 51వ ప్రధాన న్యాయమూర్తిగా ప్రమాణ స్వీకారం చేశారు. ఆర్టికల్ 124(2) ప్రకారం రాష్ట్రపతి వీరిని నియమిస్తారు మరియు సుప్రీంకోర్టు న్యాయమూర్తుల పదవీ విరమణ వయస్సు 65 ఏళ్లు."
        },
        # 2. DRDO Long-Range Land Attack Cruise Missile (LRLACM)
        {
            "id": 102,
            "subject": "National Security & Defence Technology",
            "topic": "DRDO Missile Systems - Long-Range Land Attack Cruise Missile (LRLACM)",
            "source_playlist": "https://www.youtube.com/playlist?list=PLNOSFzLA9zoqz0kdVMRbRNt7ROUS688W1",
            "source_video": "https://www.youtube.com/watch?v=IAUqxNsGV1Y",
            "educator": "Suryadeep Sir (Adda247 Telugu)",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the Long-Range Land Attack Cruise Missile (LRLACM) successfully flight-tested by DRDO from the Integrated Test Range (ITR), Chandipur, Odisha:\n1. It is designed to be launched from ground-based mobile articulated launchers as well as frontline naval warships.\n2. It features terrain-hugging, low-altitude subsonic cruising with active waypoint navigation to evade radar interception.\n3. It possesses a strike range of approximately 1,000 kilometers.\nWhich of the statements given above are correct?",
            "question_te": "ఒడిశాలోని చాందీపూర్ ఇంటిగ్రేటెడ్ టెస్ట్ రేంజ్ (ITR) నుండి డీఆర్‌డీవో (DRDO) విజయవంతంగా ప్రయోగించిన 'లాంగ్ రేంజ్ ల్యాండ్ అటాక్ క్రూయిజ్ మిస్సైల్' (LRLACM) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. దీనిని భూతల మొబైల్ లాంచర్లతో పాటు భారత నౌకాదళ యుద్ధ నౌకల నుండి కూడా ప్రయోగించేలా రూపొందించారు.\n2. రాడార్లకు చిక్కకుండా ఉండేందుకు ఇది భూమికి అతి సమీపంలో (Terrain-Hugging) లో-ఆల్టిట్యూడ్ సబ్‌సోనిక్ వేగంతో లక్ష్యాన్ని చేరుకోగలదు.\n3. ఈ క్రూయిజ్ క్షిపణి సుమారు 1,000 కిలోమీటర్ల సుదూర లక్ష్యాలను ఛేదించగల సామర్థ్యాన్ని కలిగి ఉంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three statements are correct. Developed by Aeronautical Development Establishment (ADE), Bengaluru in partnership with Indian defense industries, LRLACM completed successful all-altitude navigation, proving India's indigenous long-range cruise missile capabilities.",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. బెంగళూరులోని ADE ఆధ్వర్యంలో దేశీయంగా అభివృద్ధి చేసిన LRLACM 1000 కి.మీ దూరంలోని లక్ష్యాలను అత్యంత కచ్చితత్వంతో ఛేదించగలదు. ఇది భూమిపై మరియు యుద్ధనౌకల నుండి పనిచేస్తుంది."
        },
        # 3. ISRO-ESA Proba-3 Solar Mission
        {
            "id": 103,
            "subject": "Science & Space Technology",
            "topic": "ISRO International Collaborations - Proba-3 Mission",
            "source_playlist": "https://www.youtube.com/playlist?list=PLNOSFzLA9zoqz0kdVMRbRNt7ROUS688W1",
            "source_video": "https://www.youtube.com/watch?v=IAUqxNsGV1Y",
            "educator": "Suryadeep Sir (Adda247 Telugu)",
            "question_type": "Direct Conceptual",
            "question_en": "The European Space Agency's (ESA) revolutionary 'Proba-3' high-precision formation-flying mission, designed to create an artificial solar eclipse in space to study the Sun's faint corona, is launched aboard which ISRO launch vehicle?",
            "question_te": "సూర్యుని కరోనాను అధ్యయనం చేసేందుకు అంతరిక్షంలో కృత్రిమ సూర్యగ్రహణాన్ని సృష్టించే యూరోపియన్ స్పేస్ ఏజెన్సీ (ESA) ప్రతిష్టాత్మక 'ప్రోబా-3' (Proba-3) మిషన్‌ను ఇస్రో ఏ ప్రయోగ నౌక ద్వారా అంతరిక్షంలోకి ప్రయోగించింది?",
            "options_en": [
                "PSLV-XL (Polar Satellite Launch Vehicle)",
                "LVM3 (Launch Vehicle Mark-3)",
                "SSLV (Small Satellite Launch Vehicle)",
                "GSLV Mk II"
            ],
            "options_te": [
                "పీఎస్ఎల్వీ-ఎక్స్ఎల్ (PSLV-XL)",
                "ఎల్వీఎం-3 (LVM3)",
                "ఎస్ఎస్ఎల్వీ (SSLV)",
                "జీఎస్ఎల్వీ మార్క్ II (GSLV Mk II)"
            ],
            "correct_option": 0,
            "explanation_en": "NewSpace India Limited (NSIL) and ISRO were contracted to launch ESA's dual-satellite Proba-3 mission into a highly elliptical orbit using India's reliable PSLV-XL launch vehicle from Satish Dhawan Space Centre, Sriharikota.",
            "explanation_te": "శ్రీహరికోటలోని సతీష్ ధావన్ స్పేస్ సెంటర్ నుండి ఇస్రోకు చెందిన నమ్మకమైన PSLV-XL రాకెట్ ద్వారా యూరోపియన్ స్పేస్ ఏజెన్సీకి చెందిన ప్రొబా-3 శాటిలైట్లను కక్ష్యలోకి ప్రయోగించారు."
        },
        # 4. Telangana Caste Survey Judicial Ruling
        {
            "id": 104,
            "subject": "Telangana Governance & Public Policy",
            "topic": "Telangana Caste Survey - High Court Constitutional Validation",
            "source_playlist": "https://www.youtube.com/playlist?list=PLNOSFzLA9zoqz0kdVMRbRNt7ROUS688W1",
            "source_video": "https://www.youtube.com/watch?v=IAUqxNsGV1Y",
            "educator": "Suryadeep Sir (Adda247 Telugu)",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the Telangana High Court's ruling on the state's Comprehensive Socio-Economic, Educational, Employment and Caste Survey (సామాజిక, ఆర్థిక, విద్య, ఉద్యోగ మరియు కుల సర్వే):\n1. The High Court affirmed that the state government is legally competent to collect empirical socio-economic and demographic data to identify backwardness under Article 162.\n2. The Court emphasized that participation is voluntary and personal household data cannot be published without anonymization or used for criminal profiling.\nWhich of the statements given above is/are correct?",
            "question_te": "తెలంగాణలో నిర్వహిస్తున్న సమగ్ర సామాజిక, ఆర్థిక, విద్య, ఉపాధి మరియు కుల సర్వేపై తెలంగాణ హైకోర్టు వెలువరించిన ఉత్తర్వులకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. రాజ్యాంగంలోని అధికరణ 162 పరిధిలో సామాజిక వెనుకబాటుతనాన్ని గుర్తించి సంక్షేమ పథకాలను అందించేందుకు అనుభవపూర్వక డేటాను (Empirical Data) సేకరించే అధికారం రాష్ట్ర ప్రభుత్వానికి ఉందని హైకోర్టు స్పష్టం చేసింది.\n2. సర్వేలో పాల్గొనడం స్వచ్ఛందమని, పౌరుల వ్యక్తిగత వివరాలను బహిర్గతం చేయకుండా సమాచార గోప్యతను కాపాడాలని న్యాయస్థానం స్పష్టం చేసింది.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. The Telangana High Court declined to stay the caste survey, holding that gathering ground-level data to refine affirmative action policies and welfare delivery does not violate the constitutional right to privacy if adequate data security safeguards are maintained.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. వెనుకబడిన వర్గాల అభ్యున్నతి కోసం ప్రభుత్వానికి గణాంకాలు సేకరించే హక్కు ఉందని, అయితే సేకరించిన డాటాను దుర్వినియోగం చేయకుండా వ్యక్తిగత గోప్యతను కాపాడాలని హైకోర్టు ఆదేశించింది."
        },
        # 5. COP29 Climate Finance Goal (NCQG)
        {
            "id": 105,
            "subject": "Environment, Ecology & International Treaties",
            "topic": "UNFCCC COP29 Summit - New Collective Quantified Goal (NCQG)",
            "source_playlist": "https://www.youtube.com/playlist?list=PLNOSFzLA9zoqz0kdVMRbRNt7ROUS688W1",
            "source_video": "https://www.youtube.com/watch?v=IAUqxNsGV1Y",
            "educator": "Suryadeep Sir (Adda247 Telugu)",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the 29th UN Climate Change Conference (COP29) held at Baku, Azerbaijan:\n1. It was dubbed the 'Finance COP' with the primary agenda of establishing the New Collective Quantified Goal (NCQG) on climate finance.\n2. The NCQG is designed to succeed the previous pledge by developed nations to mobilize $100 billion per year for developing countries.\nWhich of the statements given above is/are correct?",
            "question_te": "అజర్‌బైజాన్‌లోని బాకు నగరంలో జరిగిన ఐక్యరాజ్యసమితి 29వ వాతావరణ సదస్సు (COP29) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. వాతావరణ మార్పుల నివారణ కోసం నూతన నిధుల లక్ష్యమైన 'న్యూ కలెక్టివ్ క్వాంటిఫైడ్ గోల్' (NCQG) ను రూపొందించడమే ప్రధాన అజెండా కావడంతో దీనిని 'ఫైనాన్స్ కాప్' (Finance COP) గా పిలిచారు.\n2. గతంలో అభివృద్ధి చెందిన దేశాలు పేద మరియు అభివృద్ధి చెందుతున్న దేశాలకు ఏడాదికి అందించడానికి అంగీకరించిన $100 బిలియన్ల వార్షిక నిధి స్థానంలో ఈ NCQG అమల్లోకి వస్తుంది.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. COP29 in Baku centered around negotiating the quantum, contributors, and delivery structure of NCQG, intended to deliver hundreds of billions in grants and concessional loans to replace the outdated $100 billion benchmark set in 2009.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. బాకు COP29 సదస్సులో పేద దేశాల్లో గ్రీన్ ఎనర్జీ, పర్యావరణ పరిరక్షణ కోసం లక్షల కోట్ల నిధులను సమకూర్చే నూతన లక్ష్యాన్ని (NCQG) నిర్ణయించడం ప్రధాన చర్చనీయాంశంగా నిలిచింది."
        },
        # 6. Musi Riverfront Rejuvenation Project (MRDP)
        {
            "id": 106,
            "subject": "Telangana State Geography & Urban Infrastructure",
            "topic": "Urban Ecology - Musi Riverfront Development Project",
            "source_playlist": "https://www.youtube.com/playlist?list=PLNOSFzLA9zoqz0kdVMRbRNt7ROUS688W1",
            "source_video": "https://www.youtube.com/watch?v=IAUqxNsGV1Y",
            "educator": "Suryadeep Sir (Adda247 Telugu)",
            "question_type": "Direct Conceptual",
            "question_en": "Under the flagship Musi Riverfront Development Project (MRDP) undertaken by the Government of Telangana, across how many kilometers of the river stretch in the Hyderabad metropolitan region is ecological rejuvenation, sewerage diversion, and riverfront beautification planned in Phase-1?",
            "question_te": "తెలంగాణ ప్రభుత్వం ప్రతిష్టాత్మకంగా చేపట్టిన 'మూసీ రివర్‌ఫ్రంట్ డెవలప్‌మెంట్ ప్రాజెక్ట్' (MRDP) కింద హైదరాబాద్ మహానగర పరిధిలో ఎన్ని కిలోమీటర్ల మేర నది ప్రక్షాళన, మురుగునీటి మళ్లింపు మరియు సుందరీకరణ పనులను మొదటి దశలో చేపట్టాలని నిర్ణయించారు?",
            "options_en": [
                "55 kilometers (from Osmansagar/Himayatsagar junctions to Outer Ring Road East)",
                "25 kilometers (from Puranapul to Chaderghat)",
                "105 kilometers (up to Nalgonda district border)",
                "40 kilometers (from Golconda to Nagole)"
            ],
            "options_te": [
                "55 కిలోమీటర్లు (ఉస్మాన్‌సాగర్/హిమాయత్‌సాగర్ సంగమం నుండి ఔటర్ రింగ్ రోడ్ తూర్పు వరకు)",
                "25 కిలోమీటర్లు (పురానాపూల్ నుండి చాదర్‌ఘాట్ వరకు)",
                "105 కిలోమీటర్లు (నల్గొండ జిల్లా సరిహద్దు వరకు)",
                "40 కిలోమీటర్లు (గోల్కొండ నుండి నాగోల్ వరకు)"
            ],
            "correct_option": 0,
            "explanation_en": "The Musi Riverfront Development encompasses a 55 km urban stretch connecting Gandipet to Gowrelli (ORR East), focusing on 100% sewage treatment, ecological walkways, heritage tourism hubs around Charminar/High Court, and economic commercial zones.",
            "explanation_te": "మూసీ నది పరివాహక ప్రాంతంలోని 55 కి.మీ మేర నదిని ప్రక్షాళన చేసి, లండన్‌లోని థేమ్స్ నది తరహాలో పర్యాటక, ఆర్థిక కేంద్రంగా అభివృద్ధి చేయాలని తెలంగాణ ప్రభుత్వం MRDP ప్రాజెక్టును చేపట్టింది."
        }
    ]

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"total_questions": len(questions), "source": "Adda247 Telugu (Suryadeep Sir)", "questions": questions}, f, ensure_ascii=False, indent=2)

    print(f"Successfully compiled {len(questions)} high-yield Adda247 playlist questions to {OUTPUT_FILE}")

if __name__ == "__main__":
    extract_playlist_questions()
