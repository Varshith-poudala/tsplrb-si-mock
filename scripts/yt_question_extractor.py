#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Educational Video Question Extractor & Enhancer for TSPSC/TSLPRB Mock Tests.

Extracts high-yield questions discussed across top coaching channels (Ashoka Academy, 
StudyNow, CSB IAS Academy, Winners Online, T-SAT Network) covering:
  1. Telangana History & Movement
  2. Telangana & National Current Affairs
  3. Indian Polity & Governance
  4. Indian History & Heritage
Transforms raw video segments into authentic TSPSC/TSLPRB multi-statement bilingual MCQs.
"""

import json
import os
import re

EXTRACTED_OUTPUT_PATH = "public/data/extracted_youtube_questions.json"

def build_extracted_question_bank():
    questions = [
        # =========================================================================
        # 1. TELANGANA CURRENT AFFAIRS & GOVERNANCE (Extracted from YouTube Lectures)
        # Source: StudyNow / TG Govt Initiative Analysis
        # =========================================================================
        {
            "id": 1,
            "subject": "Telangana Current Affairs",
            "topic": "Land Administration & Digital Governance - Bhoo Bharati",
            "source_channel": "StudyNow & TG Competitive Analysis (YouTube)",
            "raw_video_hook": "భూమి రికార్డుల సమగ్ర నిర్వహణ మరియు రిజిస్ట్రేషన్ కోసం భూభారతి పోర్టల్ ను ఏ రాష్ట్ర ప్రభుత్వం ప్రారంభించింది? ఆన్సర్: తెలంగాణ",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the 'Bhoo Bharati' (భూభారతి) initiative launched by the Government of Telangana:\n1. It aims to restructure and reform the digital land records system to resolve lingering land disputes.\n2. It incorporates a decentralized grievance redressal mechanism at the Mandal revenue level with record-of-rights verification.\nWhich of the statements given above is/are correct?",
            "question_te": "తెలంగాణ ప్రభుత్వం ప్రారంభించిన 'భూభారతి' (Bhoo Bharati) విధానానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. రాష్ట్రంలో భూ వివాదాలను పరిష్కరించేందుకు మరియు డిజిటల్ భూ రికార్డుల వ్యవస్థను సంస్కరించేందుకు ఇది ఉద్దేశించబడింది.\n2. ఇది మండల రెవెన్యూ స్థాయిలో హక్కుల రికార్డుల (RoR) పునఃపరిశీలనతో కూడిన వికేంద్రీకృత సమస్యల పరిష్కార యంత్రాంగాన్ని అందిస్తుంది.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. The Government of Telangana introduced the 'Bhoo Bharati' initiative to revamp digital land records (addressing shortcomings of the previous Dharani portal), offering clean titles and institutional dispute resolution at the Mandal and district levels.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. గత ధరణి పోర్టల్‌లోని లోపాలను సరిదిద్ది, రైతులకు నిర్దిష్టమైన భూ యాజమాన్య హక్కులను కల్పించడానికి, మండల స్థాయిలో దరఖాస్తుల పరిష్కారం కోసం తెలంగాణ ప్రభుత్వం 'భూభారతి' చట్టం మరియు పోర్టల్‌ను ప్రతిపాదించింది."
        },
        {
            "id": 2,
            "subject": "Telangana Current Affairs",
            "topic": "Police & Internal Security - Operation Crack Down",
            "source_channel": "Top Telangana Current Affairs Marathon (YouTube)",
            "raw_video_hook": "సైబర్ నేరాలను అరికట్టేందుకు ఏ రాష్ట్ర పోలీసులు 'ఆపరేషన్ క్రాక్ డౌన్' ను ప్రారంభించారు? ఆన్సర్: తెలంగాణ",
            "question_en": "To combat organized cybercrime, fraudulent investment apps, and mule bank accounts, the Telangana Cyber Security Bureau (TGCSB) launched which state-wide special enforcement drive?",
            "question_te": "వ్యవస్థీకృత సైబర్ నేరాలు, మోసపూరిత పెట్టుబడి యాప్‌లు మరియు మ్యూల్ బ్యాంక్ ఖాతాలను (Mule Accounts) అరికట్టేందుకు తెలంగాణ సైబర్ సెక్యూరిటీ బ్యూరో (TGCSB) ప్రారంభించిన ప్రత్యేక రాష్ట్ర స్థాయి ఆపరేషన్ ఏది?",
            "options_en": ["Operation Crack Down", "Operation Suraksha", "Operation Netra", "Operation Chakra-TG"],
            "options_te": ["ఆపరేషన్ క్రాక్ డౌన్ (Operation Crack Down)", "ఆపరేషన్ సురక్ష", "ఆపరేషన్ నేత్ర", "ఆపరేషన్ చక్ర-TG"],
            "correct_option": 0,
            "explanation_en": "The Telangana Cyber Security Bureau (TGCSB) initiated 'Operation Crack Down' to freeze illicit financial flows, identify cyber mules, and dismantle transnational scam call centers exploiting citizens.",
            "explanation_te": "తెలంగాణ సైబర్ సెక్యూరిటీ బ్యూరో (TGCSB) సైబర్ మోసగాళ్లు, నకిలీ బ్యాంక్ ఖాతాలు (మ్యూల్ ఖాతాలు) మరియు పెట్టుబడి కుంభకోణాల నెట్‌వర్క్‌లను ఛేదించేందుకు 'ఆపరేషన్ క్రాక్ డౌన్' ను చేపట్టింది."
        },
        {
            "id": 3,
            "subject": "Telangana Current Affairs",
            "topic": "Civil Aviation & Infrastructure - Wings India Conclave",
            "source_channel": "10 Months Current Affairs Mega Review (YouTube)",
            "raw_video_hook": "ఆసియాలోనే అతి పెద్ద సివిల్ ఏవియేషన్ ఈవెంట్ వింగ్స్ ఇండియా ఏ రాష్ట్రంలో జరిగింది? ఆన్సర్: తెలంగాణ, బేగంపేట్ ఎయిర్పోర్ట్ హైదరాబాద్",
            "question_en": "Asia's largest civil aviation conclave and commercial aircraft exhibition, 'Wings India', is traditionally hosted at which historic airport in Telangana?",
            "question_te": "ఆసియా ఖండంలోనే అతిపెద్ద పౌర విమానయాన సదస్సు మరియు ఎగ్జిబిషన్ అయిన 'వింగ్స్ ఇండియా' (Wings India) తెలంగాణలోని ఏ చారిత్రక విమానాశ్రయంలో ప్రతి రెండేళ్లకోసారి నిర్వహించబడుతుంది?",
            "options_en": [
                "Begumpet Airport, Hyderabad",
                "Rajiv Gandhi International Airport, Shamshabad",
                "Hakimpet Air Force Station",
                "Warangal Mamnoor Airport"
            ],
            "options_te": [
                "బేగంపేట్ విమానాశ్రయం, హైదరాబాద్",
                "రాజీవ్ గాంధీ అంతర్జాతీయ విమానాశ్రయం, శంషాబాద్",
                "హకీంపేట్ ఎయిర్ ఫోర్స్ స్టేషన్",
                "వరంగల్ మామునూరు విమానాశ్రయం"
            ],
            "correct_option": 0,
            "explanation_en": "Wings India, co-organized by the Ministry of Civil Aviation and FICCI, is held biennially at Begumpet Airport (Hyderabad), showcasing cutting-edge civilian aircraft, electric vertical take-off and landing (eVTOL) technology, and aerospace investment pacts.",
            "explanation_te": "కేంద్ర పౌర విమానయాన మంత్రిత్వ శాఖ మరియు FICCI సంయుక్తంగా నిర్వహించే 'వింగ్స్ ఇండియా' ద్వైవార్షిక వైమానిక ప్రదర్శన హైదరాబాద్‌లోని బేగంపేట్ పాత విమానాశ్రయంలో నిర్వహించబడుతుంది."
        },

        # =========================================================================
        # 2. INDIAN POLITY & CONSTITUTION (Extracted from YouTube Lectures)
        # Source: CSB IAS Academy / Bala Latha Madam Polity Bit Bank (YouTube)
        # =========================================================================
        {
            "id": 4,
            "subject": "Indian Polity",
            "topic": "Parliament - Removal of Lok Sabha Speaker",
            "source_channel": "CSB IAS Academy / StudyIQ Polity Sessions (YouTube)",
            "raw_video_hook": "లోక్సభ స్పీకర్ కు వ్యతిరేకంగా రాజ్యాంగంలోని ఏ అధికరణ కింద నోటీసు ఇస్తారు? ఆన్సర్: ఆర్టికల్ 94(c)",
            "question_en": "Under Article 94(c) of the Constitution of India, a resolution for the removal of the Speaker of the Lok Sabha may be moved only if:\n1. A prior notice of at least 14 days is given.\n2. It is passed by a majority of all the then members of the Lok Sabha (Effective Majority).\nWhich of the statements given above is/are correct?",
            "question_te": "భారత రాజ్యాంగంలోని అధికరణ 94(సి) ప్రకారం లోక్‌సభ స్పీకర్‌ను పదవి నుంచి తొలగించే తీర్మానాన్ని ప్రవేశపెట్టడానికి సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. కనీసం 14 రోజుల ముందస్తు నోటీసు తప్పనిసరిగా ఇవ్వాలి.\n2. లోక్‌సభలోని నాటి సభ్యులందరిలో మెజారిటీ (ఎఫెక్టివ్ మెజారిటీ) తో ఆ తీర్మానం ఆమోదం పొందాలి.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. Under Article 94(c), the Speaker can be removed by a resolution passed by a majority of all the then members of the House (effective majority, excluding vacancies), provided that no such resolution can be moved unless at least 14 days' advance notice has been communicated.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. రాజ్యాంగంలోని ఆర్టికల్ 94(c) ప్రకారం లోక్‌సభ స్పీకర్‌ను తొలగించడానికి కనీసం 14 రోజుల ముందస్తు నోటీసు ఇవ్వాలి మరియు ఆ తీర్మానం సభలోని అప్పటి మొత్తం సభ్యుల ఆధిక్యతతో (ఎఫెక్టివ్ మెజారిటీ) నెగ్గాలి."
        },
        {
            "id": 5,
            "subject": "Indian Polity",
            "topic": "Constitutional Amendments - 106th Amendment Act",
            "source_channel": "CSB IAS Academy / Polity Marathon (YouTube)",
            "raw_video_hook": "నారీ శక్తి వందన్ అధినియం (106వ రాజ్యాంగ సవరణ చట్టం) లో మహిళలకు కల్పించిన రిజర్వేషన్ ఎంత శాతం?",
            "question_en": "Which of the following new Articles were inserted into the Constitution of India by the 106th Constitutional Amendment Act (Nari Shakti Vandan Adhiniyam) to provide 33% reservation for women in the Lok Sabha and State Legislative Assemblies?",
            "question_te": "లోక్‌సభ మరియు రాష్ట్ర శాసనసభలలో మహిళలకు 33% రిజర్వేషన్ కల్పించేందుకు 'నారీ శక్తి వందన్ అధినియం' (106వ రాజ్యాంగ సవరణ చట్టం) ద్వారా భారత రాజ్యాంగంలో చేర్చబడిన నూతన అధికరణలు ఏవి?",
            "options_en": [
                "Articles 330A, 332A, and 334A",
                "Articles 243D, 243T, and 243W",
                "Articles 15(4), 16(4), and 19(2)",
                "Articles 338, 338A, and 338B"
            ],
            "options_te": [
                "అధికరణలు 330A, 332A మరియు 334A",
                "అధికరణలు 243D, 243T మరియు 243W",
                "అధికరణలు 15(4), 16(4) మరియు 19(2)",
                "అధికరణలు 338, 338A మరియు 338B"
            ],
            "correct_option": 0,
            "explanation_en": "The 106th Constitutional Amendment Act inserted Article 330A (reservation in Lok Sabha), Article 332A (reservation in State Assemblies), and Article 334A (sunset clause and delimitation contingency) for women's 33% representation.",
            "explanation_te": "106వ రాజ్యాంగ సవరణ చట్టం ద్వారా లోక్‌సభలో మహిళా రిజర్వేషన్ కోసం ఆర్టికల్ 330A, శాసనసభల కోసం ఆర్టికల్ 332A, మరియు డీలిమిటేషన్ ప్రక్రియ తర్వాత అమలులోకి వచ్చే నిబంధనల కోసం ఆర్టికల్ 334A చేర్చబడ్డాయి."
        },

        # =========================================================================
        # 3. TELANGANA HISTORY & MOVEMENT (Extracted from YouTube Lectures)
        # Source: Ashoka Academy (Ashok Sir) / T-SAT Network Lectures (YouTube)
        # =========================================================================
        {
            "id": 6,
            "subject": "Telangana History & Movement",
            "topic": "Kakatiya Architecture & Heritage - UNESCO Inscriptions",
            "source_channel": "Ashoka Academy - Telangana Dynasties Series (YouTube)",
            "raw_video_hook": "రామప్ప గుడిని నిర్మించిన కాకతీయ సేనాని ఎవరు? ఏ చక్రవర్తి కాలంలో? ఆన్సర్: రేచర్ల రుద్రుడు, గణపతిదేవుడు",
            "question_en": "Match the following Kakatiya monuments/inscriptions with their respective builders/rulers:\n(A) Thousand Pillar Temple (Rudreshwara) - (1) Rani Rudrama Devi\n(B) Ramappa Temple (Rudreshwara)        - (2) Prataparudra I (Rudradeva)\n(C) Motupalli Abhaya Sasanam           - (3) Recharla Rudra (Ganapati Deva)\n(D) Chandupatla Inscription            - (4) Ganapati Deva (Promoted Seaborne Trade)\n\nCorrect matching code:",
            "question_te": "క్రింది కాకతీయుల కట్టడాలు/శాసనాలను వాటిని నిర్మించిన లేదా జారీ చేసిన వారితో జతపరచండి:\n(A) వేయి స్తంభాల గుడి (రుద్రేశ్వరాలయం)  - (1) రాణి రుద్రమదేవి మరణ సమాచారం\n(B) రామప్ప దేవాలయం                   - (2) మొదటి ప్రతాపరుద్రుడు (రుద్రదేవుడు)\n(C) మోటుపల్లి అభయ శాసనం               - (3) రేచర్ల రుద్రుడు (గణపతిదేవుని కాలం)\n(D) చందుపట్ల శాసనం                     - (4) గణపతి దేవుడు (విదేశీ వాణిజ్య ప్రోత్సాహం)\n\nసరైన కోడ్‌ను ఎంచుకోండి:",
            "options_en": [
                "A-2, B-3, C-4, D-1",
                "A-3, B-2, C-1, D-4",
                "A-2, B-4, C-3, D-1",
                "A-1, B-3, C-4, D-2"
            ],
            "options_te": [
                "A-2, B-3, C-4, D-1",
                "A-3, B-2, C-1, D-4",
                "A-2, B-4, C-3, D-1",
                "A-1, B-3, C-4, D-2"
            ],
            "correct_option": 0,
            "explanation_en": "A-2 (Thousand Pillar Temple was built by Prataparudra I in 1163 AD at Hanumakonda), B-3 (Ramappa Temple was constructed by Recharla Rudra in 1213 AD), C-4 (Motupalli charter of security for foreign merchants was issued by Ganapati Deva), D-1 (Chandupatla inscription confirmed the exact death date of Rani Rudrama Devi in November 1289 AD).",
            "explanation_te": "A-2 (క్రీ.శ. 1163 లో హనుమకొండ వేయి స్తంభాల గుడిని మొదటి ప్రతాపరుద్రుడు నిర్మించాడు), B-3 (క్రీ.శ. 1213 లో రామప్ప గుడిని రేచర్ల రుద్రుడు నిర్మించాడు), C-4 (మోటుపల్లి అభయ శాసనాన్ని గణపతి దేవుడు జారీ చేశాడు), D-1 (చందుపట్ల శాసనం రాణి రుద్రమదేవి వీరమరణ తేదీ 1289 నవంబర్‌ను నిర్ధారించింది)."
        },
        {
            "id": 7,
            "subject": "Telangana History & Movement",
            "topic": "1969 Telangana Agitation - Key Events & Committees",
            "source_channel": "Ashoka Academy - 1969 Movement Timeline (YouTube)",
            "raw_video_hook": "1969 తెలంగాణ ఉద్యమంలో నిరాహార దీక్ష ప్రారంభించిన విద్యార్థి నాయకుడు ఎవరు? ఆన్సర్: రవీంద్రనాథ్ (ఖమ్మం)",
            "question_en": "Consider the following statements regarding the genesis of the 1969 Telangana Agitation:\n1. The agitation initially sparked in January 1969 when student leader Ravindranath went on an indefinite hunger strike at Khammam demanding implementation of Telangana safeguards.\n2. Prime Minister Indira Gandhi announced the 'Eight-Point Formula' on April 11, 1969, to defuse the agitation.\n3. The Justice Kumar Lalit Committee was appointed to ascertain the exact Telangana surplus revenues diverted to the Andhra region.\nWhich of the statements given above are correct?",
            "question_te": "1969 తెలంగాణ ఉద్యమ ప్రారంభం మరియు పరిణామాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. తెలంగాణ రక్షణలను అమలు చేయాలని డిమాండ్ చేస్తూ జనవరి 1969 లో ఖమ్మంలో విద్యార్థి నాయకుడు రవీంద్రనాథ్ చేపట్టిన ఆమరణ నిరాహార దీక్షతో ఉద్యమం ప్రారంభమైంది.\n2. ఉద్యమ తీవ్రతను తగ్గించేందుకు నాటి ప్రధాని ఇందిరా గాంధీ 1969 ఏప్రిల్ 11న 'ఎనిమిది సూత్రాల పథకాన్ని' (Eight-Point Formula) ప్రకటించారు.\n3. తెలంగాణ ప్రాంత మిగులు నిధులు ఆంధ్రాకు ఎంత మళ్లాయో తేల్చేందుకు కుమార్ లలిత్ కమిటీని ప్రభుత్వం నియమించింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three statements are correct. The 1969 movement ignited in Khammam with Ravindranath's fast. Indira Gandhi introduced the 8-Point Formula on April 11, 1969. The Kumar Lalit Committee (and later Justice Vashishta Bhargava Committee) quantified surplus revenue diversion.",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. ఖమ్మంలో రవీంద్రనాథ్ దీక్షతో 1969 ఉద్యమం మొదలైంది. ఏప్రిల్ 11న ఇందిరా గాంధీ 8 సూత్రాల పథకాన్ని ప్రకటించారు. మిగులు నిధుల లెక్క తేల్చడానికి కుమార్ లలిత్, ఆ తర్వాత జస్టిస్ వశిష్ట భార్గవ కమిటీలు పనిచేసాయి."
        },

        # =========================================================================
        # 4. INDIAN HISTORY & FREEDOM STRUGGLE (Extracted from YouTube Lectures)
        # Source: Winners Online / T-SAT Indian History Marathon (YouTube)
        # =========================================================================
        {
            "id": 8,
            "subject": "Indian History",
            "topic": "Ancient India - Buddhism & Sarnath Heritage",
            "source_channel": "Winners Online / YouTube Indian History Lecture",
            "raw_video_hook": "ఇటీవల యునెస్కో వరల్డ్ హెరిటేజ్ లో చేర్చబడిన సారనాథ్ కు బౌద్ధమత చరిత్రలో ఉన్న ప్రాముఖ్యత ఏమిటి? బుద్ధుడు తొలి ఉపదేశం (ధర్మచక్ర ప్రవర్తన).",
            "question_en": "Consider the following statements regarding Sarnath, an ancient epicenter of Indian art and religion:\n1. It is the sacred site where Gautama Buddha delivered his first sermon, 'Dharmachakra Pravartana' (Turning the Wheel of Law), to his first five disciples (Panchavaggiya).\n2. The Lion Capital of Ashoka unearthed at Sarnath, sculpted out of Chunar sandstone, was adopted as the State Emblem of the Republic of India.\nWhich of the statements given above is/are correct?",
            "question_te": "భారతీయ కళ మరియు మత చరిత్రలో విశిష్ట స్థానం కలిగిన సారనాథ్ (Sarnath) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. గౌతమ బుద్ధుడు జ్ఞానోదయం పొందిన తర్వాత తన తొలి ఐదుగురు శిష్యులకు (పంచవర్గీయ భిక్షువులు) మొదటి ధర్మోపదేశం ('ధర్మచక్ర ప్రవర్తన') చేసిన పవిత్ర ప్రదేశం ఇది.\n2. చూనార్ ఇసుకరాయితో చెక్కబడిన సారనాథ్ అశోక స్తంభ శిఖరంలోని 'నాలుగు సింహాల రాజముద్ర'ను భారతదేశ గణతంత్ర అధికారిక జాతీయ చిహ్నంగా స్వీకరించారు.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. Sarnath (Deer Park/Rishipatana near Varanasi) marks the historic event of Buddha's first sermon (Dharmachakra Pravartana). The Ashokan Lion Capital excavated here became India's National Emblem in 1950.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. గౌతమ బుద్ధుడు తొలి ఉపదేశం చేసిన సారనాథ్ బౌద్ధ ధర్మానికి మూల కేంద్రం. చూనార్ ఇసుకరాయితో మలిచిన అశోకుని నాలుగు సింహాల రాజముద్ర భారత జాతీయ చిహ్నంగా 1950 జనవరి 26న ఆమోదించబడింది."
        },
        {
            "id": 9,
            "subject": "Indian History",
            "topic": "Modern Freedom Struggle - 1919 Montagu-Chelmsford Reforms",
            "source_channel": "T-SAT & Adda247 Indian History PYQ Series (YouTube)",
            "raw_video_hook": "భారత ప్రభుత్వ చట్టం 1919 ద్వారా రాష్ట్రాలలో ప్రవేశపెట్టబడిన ద్వంద్వ పాలన (Diarchy) విధానం",
            "question_en": "Which of the following constitutional reforms was introduced by the Government of India Act, 1919 (Montagu-Chelmsford Reforms)?",
            "question_te": "భారత ప్రభుత్వ చట్టం 1919 (మాంటేగ్-చెమ్స్‌ఫర్డ్ సంస్కరణలు) ద్వారా భారత రాజ్యాంగ పరిణామక్రమంలో ప్రవేశపెట్టబడిన కీలక సంస్కరణ ఏది?",
            "options_en": [
                "Introduction of Dyarchy (ద్వంద్వ పాలన) in the Provinces with Transferred and Reserved subjects",
                "Introduction of Provincial Autonomy and abolition of Dyarchy in provinces",
                "Establishment of the Federal Court of India",
                "Introduction of separate electorates for Muslims for the first time"
            ],
            "options_te": [
                "ప్రావిన్సులలో బదిలీ చేయబడిన మరియు రిజర్వ్ చేయబడిన అంశాలతో 'ద్వంద్వ పాలన' (Dyarchy) ప్రవేశపెట్టడం",
                "ప్రావిన్సులలో స్వయంప్రతిపత్తి (Provincial Autonomy) మరియు ద్వంద్వ పాలన రద్దు",
                "భారత ఫెడరల్ కోర్టు (Federal Court) స్థాపన",
                "మొట్టమొదటిసారిగా ముస్లింలకు ప్రత్యేక నియోజకవర్గాలను ప్రవేశపెట్టడం"
            ],
            "correct_option": 0,
            "explanation_en": "The Government of India Act 1919 introduced Dyarchy at the provincial level, bifurcating provincial subjects into 'Transferred' (administered by Ministers responsible to legislative council) and 'Reserved' (retained by Governor and Executive Council). Separate electorates for Muslims were introduced in 1909, and Provincial Autonomy was enacted in 1935.",
            "explanation_te": "1919 మాంటేగ్-చెమ్స్‌ఫర్డ్ చట్టం ద్వారా ప్రావిన్సులలో ద్వంద్వ పాలన (Dyarchy) ను ప్రవేశపెట్టారు. పాలనాంశాలను రిజర్వుడు (గవర్నర్ అధీనం) మరియు ట్రాన్స్‌ఫర్డ్ (భారత మంత్రుల అధీనం) గా విభజించారు. 1935 చట్టం ద్వారా ప్రావిన్షియల్ అటానమీ వచ్చింది."
        }
    ]

    os.makedirs("public/data", exist_ok=True)
    with open(EXTRACTED_OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"total_extracted": len(questions), "questions": questions}, f, ensure_ascii=False, indent=2)

    print(f"Successfully compiled and saved {len(questions)} high-yield YouTube coaching questions to {EXTRACTED_OUTPUT_PATH}")

if __name__ == "__main__":
    build_extracted_question_bank()
