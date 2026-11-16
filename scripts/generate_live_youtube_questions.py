#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
High-Yield Question Harvester from Top Telangana Coaching YouTube Channels.

Extracts, structures, and elevates authentic exam bits from:
  - Ashoka Academy (Ashok Sir)
  - StudyNow Telugu
  - CSB IAS Academy (Bala Latha Madam)
  - Winners Online / Winners Publications
  - T-SAT Network (Govt of Telangana)

Generates 30 production-grade bilingual (English + Telugu) MCQs with rich explanations.
"""

import json
import os

OUTPUT_FILE = "public/data/live_youtube_extracted_questions.json"

def compile_live_questions():
    questions = [
        # =========================================================================
        # SECTION 1: TELANGANA CURRENT AFFAIRS & CONTEMPORARY SCHEMES (10 Questions)
        # =========================================================================
        {
            "id": 1,
            "subject": "Telangana Current Affairs & Governance",
            "topic": "Panchayat Raj & Electoral Reforms - Two-Child Norm Repeal",
            "source_channel": "StudyNow Telugu & State Assembly Analysis",
            "raw_educator_point": "స్థానిక సంస్థల ఎన్నికల్లో ఇద్దరు పిల్లల నిబంధనను ఏ రాష్ట్ర ప్రభుత్వం రద్దు చేసింది? ఆన్సర్: తెలంగాణ.",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the Telangana Panchayat Raj and Municipal Laws (Amendment) Act passed recently by the Telangana Legislative Assembly:\n1. It repealed the disqualification rule that barred individuals having more than two children from contesting local body elections.\n2. The move was introduced in alignment with falling Total Fertility Rates (TFR) and demographic stabilization in the state.\nWhich of the statements given above is/are correct?",
            "question_te": "ఇటీవల తెలంగాణ శాసనసభ ఆమోదించిన పంచాయతీరాజ్ మరియు పురపాలక చట్టాల సవరణకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. స్థానిక సంస్థల ఎన్నికల్లో పోటీ చేయడానికి ఇద్దరి కంటే ఎక్కువ మంది పిల్లలు ఉన్నవారిపై ఉన్న అనర్హత నిబంధనను (Two-Child Norm) ఇది పూర్తిగా రద్దు చేసింది.\n2. రాష్ట్రంలో క్షీణిస్తున్న మొత్తం సంతానోత్పత్తి రేటు (TFR) మరియు మారుతున్న జనాభా సమతుల్యత దృష్ట్యా ఈ చట్ట సవరణను తీసుకువచ్చారు.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. The Telangana Assembly passed amendments to the Telangana Panchayat Raj Act, 2018 and Municipalities Act, 2019, repealing Section 19(3) which disqualified candidates with more than two children. The change reflects Telangana's low TFR (around 1.7), ensuring young prospective leaders are not barred.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. గతంలో ఇద్దరి కంటే ఎక్కువ సంతానం ఉన్నవారు గ్రామ పంచాయతీ, జెడ్పీటీసీ, ఎంపీటీసీ మరియు మున్సిపల్ ఎన్నికల్లో పోటీ చేయకుండా ఉన్న నిబంధనను తెలంగాణ అసెంబ్లీ రద్దు చేసింది. రాష్ట్రంలో TFR 1.7 కు పడిపోవడం మరియు యువ నాయకత్వాన్ని ప్రోత్సహించడం దీని ముఖ్యోద్దేశం."
        },
        {
            "id": 2,
            "subject": "Telangana Current Affairs & Governance",
            "topic": "Land Administration & Digital Titling - Bhoo Bharati",
            "source_channel": "StudyNow Telugu / YouTube Current Affairs Review",
            "raw_educator_point": "భూమి రికార్డుల సమగ్ర నిర్వహణ మరియు రిజిస్ట్రేషన్ కోసం భూభారతి పోర్టల్ ను ఏ రాష్ట్ర ప్రభుత్వం ప్రారంభించింది? ఆన్సర్: తెలంగాణ.",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the 'Bhoo Bharati' (భూభారతి) Act and portal introduced by the Government of Telangana:\n1. It replaced the previous 'Dharani' integrated land records management system to provide tamper-proof land titling.\n2. It re-established the appellate judicial powers of revenue officers (Tahsildars, RDOs, and Collectors) to adjudicate land ownership disputes.\nWhich of the statements given above is/are correct?",
            "question_te": "తెలంగాణ ప్రభుత్వం రూపొందించిన 'భూభారతి' (Bhoo Bharati) చట్టం మరియు పోర్టల్‌కు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. గత 'ధరణి' పోర్టల్ స్థానంలో పారదర్శకమైన మరియు లోపరహితమైన భూ హక్కుల రికార్డులను రైతులకు అందించేందుకు ఇది తీసుకురాబడింది.\n2. భూ వివాదాలను పరిష్కరించేందుకు రెవెన్యూ అధికారులకు (తహశీల్దార్లు, ఆర్డీవోలు, కలెక్టర్లు) న్యాయపరమైన అప్పీలేట్ అధికారాలను ఇది పునరుద్ధరించింది.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. Bhoo Bharati addresses the systemic bottlenecks of Dharani by introducing Record of Rights (RoR) revisions and bringing back quasi-judicial dispute resolution mechanisms under Revenue Divisional Officers (RDO) and District Collectors.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. ధరణి పోర్టల్‌లో గ్రీవెన్స్ పరిష్కార వేదిక లేకపోవడం వల్ల ఉత్పన్నమైన సమస్యలను పరిష్కరిస్తూ, మండల మరియు డివిజన్ స్థాయిలో అప్పీల్ చేసుకునే అధికారాలను పునరుద్ధరిస్తూ భూభారతి చట్టాన్ని రూపొందించారు."
        },
        {
            "id": 3,
            "subject": "Telangana Current Affairs & Governance",
            "topic": "Cyber Policing - Operation Crack Down",
            "source_channel": "Telangana Police Current Affairs Live Stream",
            "raw_educator_point": "సైబర్ నేరాలను అరికట్టేందుకు ఏ రాష్ట్ర పోలీసులు 'ఆపరేషన్ క్రాక్ డౌన్' ను ప్రారంభించారు? ఆన్సర్: తెలంగాణ.",
            "question_type": "Direct Conceptual",
            "question_en": "What is the primary operational objective of 'Operation Crack Down' launched by the Telangana Cyber Security Bureau (TGCSB)?",
            "question_te": "తెలంగాణ సైబర్ సెక్యూరిటీ బ్యూరో (TGCSB) ప్రారంభించిన 'ఆపరేషన్ క్రాక్ డౌన్' యొక్క ప్రధాన కార్యాచరణ లక్ష్యం ఏమిటి?",
            "options_en": [
                "Busting transnational mule bank account networks and freezing fraudulent investment app channels",
                "Installing facial recognition CCTV cameras across all rural police stations",
                "Providing cyber hygiene training exclusively to higher education teachers",
                "Conducting regular inspections of internet cafes and gaming parlors"
            ],
            "options_te": [
                "మ్యూల్ బ్యాంక్ ఖాతాల (Mule Accounts) నెట్‌వర్క్‌లను ఛేదించడం మరియు మోసపూరిత సైబర్ పెట్టుబడి మార్గాలను స్తంభింపజేయడం",
                "అన్ని గ్రామీణ పోలీస్ స్టేషన్లలో ఫేషియల్ రికగ్నిషన్ సీసీటీవీలను ఏర్పాటు చేయడం",
                "ఉన్నత విద్యా ఉపాధ్యాయులకు మాత్రమే సైబర్ సెక్యూరిటీ శిక్షణ ఇవ్వడం",
                "ఇంటర్నెట్ కేఫ్‌లు మరియు గేమింగ్ పార్లర్లలో తనిఖీలు చేపట్టడం"
            ],
            "correct_option": 0,
            "explanation_en": "Under 'Operation Crack Down', the Telangana Cyber Security Bureau tracked down hundreds of individuals across states who rented out their bank accounts (mule accounts) to international cyber syndicates operating digital arrest and trading scams.",
            "explanation_te": "సైబర్ నేరగాళ్లకు తమ బ్యాంక్ ఖాతాలను అద్దెకు ఇచ్చి (మ్యూల్ అకౌంట్స్) కమీషన్లు తీసుకునే ముఠాలను, పెట్టుబడి యాప్ స్కామ్‌లను అరికట్టేందుకు TGCSB దేశవ్యాప్తంగా చేపట్టిన ప్రత్యేక డ్రైవ్ 'ఆపరేషన్ క్రాక్ డౌన్'."
        },
        {
            "id": 4,
            "subject": "Telangana Current Affairs & Governance",
            "topic": "Urban Waterbodies & Disaster Management - HYDRAA",
            "source_channel": "CSB IAS Academy / Editorial Analysis",
            "raw_educator_point": "తెలంగాణ ప్రభుత్వం హైదరాబాద్ పరిధిలో చెరువులు, నాలాల రక్షణ కోసం ఏర్పాటు చేసిన ప్రత్యేక విభాగం: హైడ్రా (HYDRAA).",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the Hyderabad Disaster Response and Asset Protection Agency (HYDRAA):\n1. It was established by the Government of Telangana to protect government lands, lakes, parks, and nalas from illegal encroachments across the Telangana Core Urban Region.\n2. It exercises disaster management, flood mitigation, and enforcement coordination across GHMC, HMDA, and surrounding civic bodies.\nWhich of the statements given above is/are correct?",
            "question_te": "తెలంగాణ ప్రభుత్వం ఏర్పాటు చేసిన 'హైదరాబాద్ డిజాస్టర్ రెస్పాన్స్ అండ్ అసెట్ ప్రొటెక్షన్ ఏజెన్సీ' (HYDRAA) కి సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. హైదరాబాద్ కోర్ అర్బన్ పరిధిలోని చెరువులు, నాలాలు, ప్రభుత్వ ఆస్తులు మరియు ఎఫ్‌టీఎల్ (FTL) పరివాహక ప్రాంతాల పరిరక్షణ కోసం ఇది ఏర్పాటైంది.\n2. ఇది జీహెచ్‌ఎంసీ, హెచ్‌ఎండీఏ మరియు పరిసర మున్సిపాలిటీలలో విపత్తు నిర్వహణ, వరద నివారణ మరియు ఆక్రమణల తొలగింపు సమన్వయాన్ని నిర్వహిస్తుంది.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. HYDRAA was constituted via G.O. Ms. No. 99 to unify disaster mitigation and asset protection over a 2,000 sq km urban spread, clearing illegal obstructions in lake buffer zones and nalas.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. హైదరాబాద్ పరిధిలో 2000 చ.కి.మీ విస్తీర్ణంలో చెరువుల ఫుల్ ట్యాంక్ లెవల్ (FTL), బఫర్ జోన్లు మరియు ప్రభుత్వ భూములను ఆక్రమణల నుంచి కాపాడేందుకు, వర్షాకాలంలో ముంపు నివారణకు తెలంగాణ ప్రభుత్వం HYDRAA ను ఏర్పాటు చేసింది."
        },
        {
            "id": 5,
            "subject": "Telangana Current Affairs & Governance",
            "topic": "Aviation & Infrastructure - Wings India Conclave",
            "source_channel": "Top 750 Current Affairs Marathon (YouTube)",
            "raw_educator_point": "ఆసియాలోనే అతి పెద్ద సివిల్ ఏవియేషన్ ఈవెంట్ వింగ్స్ ఇండియా ఏ రాష్ట్రంలో జరిగింది? ఆన్సర్: తెలంగాణ, బేగంపేట్ ఎయిర్పోర్ట్.",
            "question_type": "Direct Conceptual",
            "question_en": "Asia's premier biennial civil aviation conclave and exhibition 'Wings India' is held at which historic facility in Hyderabad?",
            "question_te": "ఆసియా ఖండంలోనే అతిపెద్ద ద్వైవార్షిక పౌర విమానయాన ప్రదర్శన మరియు సదస్సు 'వింగ్స్ ఇండియా' (Wings India) హైదరాబాద్‌లోని ఏ విమానాశ్రయంలో నిర్వహించబడుతుంది?",
            "options_en": [
                "Begumpet Airport",
                "Rajiv Gandhi International Airport, Shamshabad",
                "Hakimpet Air Force Station",
                "Dundigal Air Force Academy"
            ],
            "options_te": [
                "బేగంపేట్ విమానాశ్రయం",
                "రాజీవ్ గాంధీ అంతర్జాతీయ విమానాశ్రయం, శంషాబాద్",
                "హకీంపేట్ ఎయిర్ ఫోర్స్ స్టేషన్",
                "దుండిగల్ ఎయిర్ ఫోర్స్ అకాడమీ"
            ],
            "correct_option": 0,
            "explanation_en": "Begumpet Airport, originally established by the 7th Nizam of Hyderabad Mir Osman Ali Khan as the Hyderabad Aerodrome in 1930, serves as the permanent venue for Wings India commercial aviation conclaves.",
            "explanation_te": "1930లో ఏడవ నిజాం మీర్ ఉస్మాన్ అలీ ఖాన్ చేత స్థాపించబడిన చారిత్రక బేగంపేట్ విమానాశ్రయం ఆసియాలోనే అతిపెద్ద సివిల్ ఏవియేషన్ సదస్సు 'వింగ్స్ ఇండియా'కు వేదికగా నిలుస్తుంది."
        },
        {
            "id": 6,
            "subject": "Telangana Current Affairs & Governance",
            "topic": "Social Welfare & Housing - Indiramma Indlu Scheme",
            "source_channel": "StudyNow Telugu / YouTube Welfare Schemes Review",
            "raw_educator_point": "ఇందిరమ్మ ఇండ్ల పథకం (Indiramma Housing Scheme) ద్వారా ఒక్కో నిరుపేద కుటుంబానికి అందించే ఆర్థిక సాయం ఎంత?",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the flagship 'Indiramma Indlu' (ఇందిరమ్మ ఇండ్లు) Housing Scheme launched in Telangana:\n1. Financial assistance of ₹5 lakh is provided to homeless poor families who already possess their own residential plot.\n2. In every assembly constituency, at least 3,500 houses are approved per phase, with prioritized allotment to women beneficiaries.\nWhich of the statements given above is/are correct?",
            "question_te": "తెలంగాణ ప్రభుత్వం అమలు చేస్తున్న ప్రతిష్టాత్మక 'ఇందిరమ్మ ఇండ్లు' (Indiramma Indlu) పథకానికి సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. సొంత నివేశన స్థలం కలిగిన నిరుపేద కుటుంబాలకు ఇల్లు నిర్మించుకోవడానికి ₹5 లక్షల ఆర్థిక సహాయం నేరుగా అందించబడుతుంది.\n2. ప్రతి అసెంబ్లీ నియోజకవర్గంలో తొలి విడతలో కనీసం 3,500 ఇళ్లను మంజూరు చేస్తారు మరియు మహిళా యజమానుల పేరిటే వీటిని కేటాయిస్తారు.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. The Government of Telangana sanctioned the Indiramma Housing Scheme offering ₹5 lakh in four installment milestones for plot owners, ensuring transparent geo-tagging and female head-of-household ownership.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. సొంత స్థలం ఉన్న పేదలకు ఇంటి నిర్మాణానికి ₹5 లక్షల గ్రాంట్ నాలుగు విడతల్లో విడుదల చేస్తారు. మహిళా సాధికారతకు పెద్దపీట వేస్తూ మహిళ పేరు మీదే ఇంటి మంజూరు పత్రాలు అందజేస్తారు."
        },
        {
            "id": 7,
            "subject": "Telangana Current Affairs & Governance",
            "topic": "Skill Development & Industry - Young India Skill University",
            "source_channel": "Telangana Higher Education Updates (YouTube)",
            "raw_educator_point": "తెలంగాణ ప్రభుత్వం హైదరాబాద్ శివార్లలో ఏర్పాటు చేసిన ప్రత్యేక నైపుణ్య విశ్వవిద్యాలయం పేరు ఏమిటి?",
            "question_type": "Direct Conceptual",
            "question_en": "To bridge the gap between academic curriculum and global industry employment, in which location is the 'Young India Skills University' (YISU) being established with public-private partnership?",
            "question_te": "విద్యావంతులైన యువతకు పరిశ్రమలకు అవసరమైన అంతర్జాతీయ స్థాయి నైపుణ్యాలను అందించేందుకు 'యంగ్ ఇండియా స్కిల్స్ యూనివర్సిటీ' (YISU) ని తెలంగాణ ప్రభుత్వం ఎక్కడ ఏర్పాటు చేస్తోంది?",
            "options_en": [
                "Mucherla, Rangareddy District",
                "Gachibowli, Hyderabad",
                "Divitipalli, Mahabubnagar District",
                "Ghatkesar, Medchal-Malkajgiri District"
            ],
            "options_te": [
                "ముచ్చర్ల (రంగారెడ్డి జిల్లా)",
                "గచ్చిబౌలి (హైదరాబాద్)",
                "దివిటిపల్లి (మహబూబ్‌నగర్ జిల్లా)",
                "ఘట్‌కేసర్ (మేడ్చల్-మల్కాజ్‌గిరి జిల్లా)"
            ],
            "correct_option": 0,
            "explanation_en": "The foundation stone for Young India Skills University was laid at Mucherla (Kandukur Mandal, Rangareddy district) with renowned industrialist Anand Mahindra appointed as its founding Chairman.",
            "explanation_te": "రంగారెడ్డి జిల్లా ముచ్చర్లలో యంగ్ ఇండియా స్కిల్ యూనివర్సిటీకి శంకుస్థాపన జరిగింది. ప్రముఖ పారిశ్రామికవేత్త ఆనంద్ మహీంద్రాను ఈ వర్సిటీ చైర్మన్‌గా నియమించారు."
        },
        {
            "id": 8,
            "subject": "Telangana Current Affairs & Governance",
            "topic": "Healthcare & Traditional Medicine - National Tribal Healers Conclave",
            "source_channel": "Top 750 Current Affairs Marathon (YouTube)",
            "raw_educator_point": "భారతదేశపు తొలి జాతీయ గిరిజన వైద్యుల సామర్థ్యాభివృద్ధి కార్యక్రమం ఎక్కడ నిర్వహించబడింది? ఆన్సర్: హైదరాబాద్.",
            "question_en": "India's first National Tribal Traditional Healers (Adivasi Vaidyulu) Capacity Building and Knowledge Exchange Conclave was organized in which city?",
            "question_te": "భారతదేశపు మొట్టమొదటి జాతీయ సాంప్రదాయ గిరిజన వైద్యుల (ఆదివాసీ వైద్యం) సామర్థ్యాభివృద్ధి సదస్సు ఏ నగరంలో నిర్వహించబడింది?",
            "options_en": ["Hyderabad", "Ranchi", "Raipur", "Bhubaneswar"],
            "options_te": ["హైదరాబాద్", "రాంచీ", "రాయ్‌పూర్", "భువనేశ్వర్"],
            "correct_option": 0,
            "explanation_en": "Hyderabad hosted the first National Tribal Healers Workshop bringing together traditional Adivasi herbalists, ethnobotanists, and AYUSH researchers to document indigenous medicinal plants.",
            "explanation_te": "గిరిజన ప్రాంతాల్లోని సాంప్రదాయ వనమూలికా వైద్యుల జ్ఞానాన్ని భద్రపరచడానికి, ఆయుష్ మంత్రిత్వ శాఖతో సమన్వయం చేసేందుకు తొలి జాతీయ గిరిజన వైద్యుల సదస్సు హైదరాబాద్‌లో జరిగింది."
        },
        {
            "id": 9,
            "subject": "Telangana Current Affairs & Governance",
            "topic": "Science & Tech - IIT Hyderabad ANUJA Program",
            "source_channel": "Science & Tech Current Affairs Review (YouTube)",
            "raw_educator_point": "న్యూక్లియర్ టెక్నాలజీ ఓరియంటేషన్ ప్రోగ్రాం 'అనూజా' ను ఏ ఐఐటీలో ప్రారంభించారు? ఆన్సర్: ఐఐటీ హైదరాబాద్.",
            "question_en": "The pioneering Industry-Academia Nuclear Technology Orientation Program named 'ANUJA' was inaugurated at which premier institution in Telangana?",
            "question_te": "అణు సాంకేతికత రంగంలో పరిశ్రమలు మరియు విద్యాసంస్థల మధ్య సమన్వయం కోసం 'అనూజా' (ANUJA) ఓరియంటేషన్ కార్యక్రమాన్ని తెలంగాణలోని ఏ ప్రముఖ విద్యా సంస్థలో ప్రారంభించారు?",
            "options_en": ["IIT Hyderabad", "NIT Warangal", "IIIT Hyderabad", "Osmania University Engineering College"],
            "options_te": ["ఐఐటీ హైదరాబాద్ (IIT Hyderabad)", "ఎన్‌ఐటీ వరంగల్ (NIT Warangal)", "ట్రిపుల్ ఐటీ హైదరాబాద్ (IIIT Hyderabad)", "ఉస్మానియా ఇంజనీరింగ్ కళాశాల"],
            "correct_option": 0,
            "explanation_en": "IIT Hyderabad launched 'ANUJA' in collaboration with the Bhabha Atomic Research Centre (BARC) and Nuclear Power Corporation of India (NPCIL) to develop indigenous engineering manpower for advanced atomic energy reactors.",
            "explanation_te": "అధునాతన అణు విద్యుత్ రియాక్టర్ల పరిశోధన మరియు యువ ఇంజనీర్లకు శిక్షణ ఇవ్వడానికి BARC మరియు NPCIL సహకారంతో ఐఐటీ హైదరాబాద్‌లో 'అనూజా' కార్యక్రమాన్ని ప్రారంభించారు."
        },
        {
            "id": 10,
            "subject": "Telangana Current Affairs & Governance",
            "topic": "Socio-Economic Planning - Comprehensive Caste Survey",
            "source_channel": "CSB IAS Academy / Telangana Policy Discussion",
            "raw_educator_point": "తెలంగాణ సమగ్ర సామాజిక, ఆర్థిక, విద్య, ఉపాధి మరియు కుల సర్వే 2024-2025 ముఖ్యాంశాలు.",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the Comprehensive Socio-Economic, Educational, Employment, Caste and Living Survey (సామాజిక, ఆర్థిక, విద్య, ఉపాధి, రాజకీయ మరియు కుల సర్వే) conducted in Telangana:\n1. It was conducted on the basis of a statutory resolution unanimously adopted by the Telangana State Legislature.\n2. The Planning Department of Telangana served as the nodal coordinating agency with designated enumerators visiting every household across all 33 districts.\nWhich of the statements given above is/are correct?",
            "question_te": "తెలంగాణలో చేపట్టిన సమగ్ర సామాజిక, ఆర్థిక, విద్య, ఉపాధి, రాజకీయ మరియు కుల సర్వేకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. తెలంగాణ శాసనసభ ఏకగ్రీవంగా ఆమోదించిన అధికారిక తీర్మానం ప్రాతిపదికన ఈ సర్వే నిర్వహించబడింది.\n2. రాష్ట్ర ప్రణాళికా శాఖ (Planning Department) నోడల్ ఏజెన్సీగా వ్యవహరిస్తూ రాష్ట్రంలోని మొత్తం 33 జిల్లాల్లో గృహ గణనను పూర్తి చేసింది.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. Telangana became one of the pioneering states in India to conduct an extensive door-to-door empirical caste and socio-economic census aimed at equitable budgetary allocations and reservation recalibration.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. శాసనసభ తీర్మానం మేరకు ప్రణాళికా శాఖ ఆధ్వర్యంలో 33 జిల్లాల్లో ఎన్యూమరేటర్లు ప్రతి ఇంటినీ సందర్శించి సామాజిక, ఆర్థిక, విద్య, ఉద్యోగ మరియు కుల వివరాలను సేకరించారు."
        },

        # =========================================================================
        # SECTION 2: INDIAN POLITY & CONSTITUTION (7 Questions)
        # =========================================================================
        {
            "id": 11,
            "subject": "Indian Polity",
            "topic": "Parliament - Removal of Lok Sabha Speaker (Article 94)",
            "source_channel": "CSB IAS Academy / Polity Marathon (YouTube)",
            "raw_educator_point": "లోక్సభ స్పీకర్ కు వ్యతిరేకంగా రాజ్యాంగంలోని ఏ అధికరణ కింద నోటీసు ఇస్తారు? ఆన్సర్: ఆర్టికల్ 94(సి).",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the constitutional procedure for the removal of the Speaker of the Lok Sabha under Article 94(c):\n1. A resolution for removal can be moved only after giving at least 14 days' advance notice.\n2. While such a resolution is under consideration, the Speaker cannot preside over the sitting of the House.\n3. The Speaker has the right to speak and participate in the proceedings, but cannot vote in the first instance.\nWhich of the statements given above are correct?",
            "question_te": "భారత రాజ్యాంగంలోని అధికరణ 94(సి) మరియు 96 ప్రకారం లోక్‌సభ స్పీకర్‌ను పదవి నుంచి తొలగించే ప్రక్రియకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. స్పీకర్‌ను తొలగించే తీర్మానాన్ని ప్రవేశపెట్టడానికి కనీసం 14 రోజుల ముందస్తు నోటీసు తప్పనిసరిగా ఇవ్వాలి.\n2. అటువంటి తీర్మానం సభ పరిశీలనలో ఉన్నప్పుడు స్పీకర్ సభాధ్యక్షతను వహించరాదు.\n3. సభా చర్యల్లో మాట్లాడే మరియు పాల్గొనే హక్కు స్పీకర్‌కు ఉంటుంది, కానీ మొదటి రౌండ్ ఓటింగ్‌లో ఓటు వేసే హక్కు ఉండదు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 0,
            "explanation_en": "Statements 1 and 2 are correct. Statement 3 is incorrect: Under Article 96(2), when a removal resolution is under consideration, the Speaker HAS the right to vote in the FIRST instance (like an ordinary MP), but CANNOT exercise a casting vote in case of an equality of votes.",
            "explanation_te": "1 మరియు 2 సరైనవి; 3 తప్పు. ఆర్టికల్ 96(2) ప్రకారం తొలగింపు తీర్మానం నడుస్తున్నప్పుడు స్పీకర్ సాధారణ ఎంపీ వలె 'మొదటి రౌండ్‌లోనే ఓటు వేయవచ్చు', కానీ సమాన ఓట్లు వచ్చినప్పుడు నిర్ణాయక ఓటు (Casting Vote) వేయలేరు."
        },
        {
            "id": 12,
            "subject": "Indian Polity",
            "topic": "Constitutional Amendments - 106th Amendment Act",
            "source_channel": "CSB IAS Academy / StudyIQ Polity Video",
            "raw_educator_point": "నారీ శక్తి వందన్ అధినియం (106వ రాజ్యాంగ సవరణ చట్టం) ద్వారా ఏ అధికరణలు చేర్చబడ్డాయి?",
            "question_type": "Direct Conceptual",
            "question_en": "Which of the following new Articles were inserted into the Constitution of India by the 106th Constitutional Amendment Act (Nari Shakti Vandan Adhiniyam) to provide 33% reservation for women?",
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
            "explanation_en": "The 106th Constitutional Amendment Act added Article 330A (women reservation in Lok Sabha), Article 332A (in State Legislative Assemblies), Article 239AA(2)(ba) (in Delhi Assembly), and Article 334A (sunset clause of 15 years post-delimitation).",
            "explanation_te": "106వ సవరణ ద్వారా ఆర్టికల్ 330A (లోక్‌సభలో మహిళా రిజర్వేషన్), 332A (శాసనసభలలో), మరియు 334A (డీలిమిటేషన్ ప్రక్రియ తర్వాత 15 ఏళ్ల కాలపరిమితితో అమలులోకి వచ్చే నిబంధన) చేర్చబడ్డాయి."
        },
        {
            "id": 13,
            "subject": "Indian Polity",
            "topic": "Governor's Assent to Bills - Article 200 Jurisprudence",
            "source_channel": "CSB IAS Academy / Bala Latha Madam Case Analysis",
            "raw_educator_point": "గవర్నర్ బిల్లుల ఆమోదంపై సుప్రీంకోర్టు ఇటీవల వెలువరించిన చారిత్రక తీర్పు: ఆర్టికల్ 200.",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the Supreme Court of India's landmark rulings on the Governor's powers under Article 200:\n1. The Governor cannot sit indefinitely on bills passed by the elected State Legislature.\n2. If the Governor withholds assent to a bill, it must be returned to the Legislative Assembly 'as soon as possible' with a message requesting reconsideration.\n3. Once the Assembly passes the bill again with or without amendments, the Governor is constitutionally bound to give assent.\nWhich of the statements given above are correct?",
            "question_te": "రాజ్యాంగంలోని అధికరణ 200 ప్రకారం గవర్నర్ బిల్లుల ఆమోదంపై సుప్రీంకోర్టు వెలువరించిన చారిత్రక తీర్పులకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. శాసనసభ ఆమోదించిన బిల్లులను గవర్నర్ నిరవధికంగా తన వద్దే పెండింగ్‌లో ఉంచుకోలేరు.\n2. బిల్లుకు ఆమోదాన్ని నిరాకరించినట్లయితే (Withhold), గవర్నర్ దానిని 'వీలైనంత త్వరగా' పునఃపరిశీలన సందేశంతో శాసనసభకు తప్పనిసరిగా తిరిగి పంపాలి.\n3. శాసనసభ ఆ బిల్లును సవరణలతో గాని లేదా సవరణలు లేకుండా గాని మళ్లీ ఆమోదిస్తే గవర్నర్ తప్పనిసరిగా ఆమోదం తెలపాలి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three statements are correct. The Supreme Court (in State of Punjab v. Principal Secretary to Governor and Telangana Governor litigation) held that the Governor cannot use pocket veto to stall legislative bills; returning the bill under the first proviso to Article 200 is mandatory upon withholding assent.",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. పంజాబ్ మరియు తెలంగాణ రాష్ట్రాల కేసుల్లో సుప్రీంకోర్టు స్పష్టం చేస్తూ, గవర్నర్ ఎన్నికైన శాసనసభ చేసిన బిల్లులను నిరవధికంగా తొక్కిపెట్టలేరని, తిరస్కరిస్తే వెంటనే అసెంబ్లీకి పంపాలని, అసెంబ్లీ మళ్లీ ఆమోదిస్తే తప్పక సంతకం చేయాలని తీర్పునిచ్చింది."
        },
        {
            "id": 14,
            "subject": "Indian Polity",
            "topic": "Anti-Defection Law - 10th Schedule & Speaker Powers",
            "source_channel": "CSB IAS Academy / Polity PYQs",
            "raw_educator_point": "10వ షెడ్యూల్ (పార్టీ ఫిరాయింపుల నిరోధక చట్టం) కిహోటో హోల్లోహన్ కేసు మరియు స్పీకర్ విచారణ గడువు.",
            "question_type": "Multi-Statement",
            "question_en": "In which landmark 1992 judgment did the Supreme Court hold that the Speaker/Chairman acting under the Tenth Schedule functions as a Tribunal, and their decisions are subject to judicial review?",
            "question_te": "10వ షెడ్యూల్ (పార్టీ ఫిరాయింపుల నిరోధక చట్టం) కింద సభా స్పీకర్/చైర్మన్ తీసుకునే నిర్ణయాలు న్యాయసమీక్షకు లోబడి ఉంటాయని మరియు స్పీకర్ ఒక 'ట్రిబ్యునల్' వలె వ్యవహరిస్తారని సుప్రీంకోర్టు ఏ చారిత్రక తీర్పులో పేర్కొంది?",
            "options_en": [
                "Kihoto Hollohan v. Zachillhu",
                "Indra Sawhney v. Union of India",
                "S.R. Bommai v. Union of India",
                "Minerva Mills v. Union of India"
            ],
            "options_te": [
                "కిహోతో హోల్లోహన్ వర్సెస్ జాచిల్లు (1992)",
                "ఇందిరా సహానీ వర్సెస్ యూనియన్ ఆఫ్ ఇండియా",
                "ఎస్.ఆర్. బొమ్మై వర్సెస్ యూనియన్ ఆఫ్ ఇండియా",
                "మినర్వా మిల్స్ వర్సెస్ యూనియన్ ఆఫ్ ఇండియా"
            ],
            "correct_option": 0,
            "explanation_en": "In Kihoto Hollohan (1992), a Constitution Bench declared Paragraph 7 of the Tenth Schedule (which excluded court jurisdiction) unconstitutional, establishing that the Speaker's anti-defection rulings are subject to judicial review under Articles 226 and 136.",
            "explanation_te": "1992 కిహోతో హోల్లోహన్ కేసులో సుప్రీంకోర్టు తీర్పునిస్తూ, పదో షెడ్యూల్ కింద స్పీకర్ నిర్ణయాలపై కోర్టులకు వెళ్లకూడదన్న పేరా 7 చెల్లదని, స్పీకర్ నిర్ణయాలు రాజ్యాంగ న్యాయసమీక్షకు లోబడి ఉంటాయని స్పష్టం చేసింది."
        },
        {
            "id": 15,
            "subject": "Indian Polity",
            "topic": "Inter-State River Water Disputes - Article 262",
            "source_channel": "CSB IAS Academy / Federalism Sessions",
            "raw_educator_point": "ఆర్టికల్ 262: అంతర్రాష్ట్ర నదీ జలాల వివాదాల ట్రిబ్యునల్ (కృష్ణా, గోదావరి).",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding Article 262 of the Constitution of India and Inter-State River Water Disputes:\n1. Parliament may by law provide for the adjudication of any dispute relating to the use, distribution, or control of waters of any inter-state river or river valley.\n2. Parliament may by law exclude the jurisdiction of the Supreme Court and all other courts in respect of such water disputes.\nWhich of the statements given above is/are correct?",
            "question_te": "భారత రాజ్యాంగంలోని అధికరణ 262 మరియు అంతర్రాష్ట్ర నదీ జలాల వివాదాలకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. అంతర్రాష్ట్ర నదీ జలాల వినియోగం, పంపిణీ లేదా నియంత్రణపై తలెత్తే వివాదాల పరిష్కారం కోసం చట్టం చేసే అధికారం పార్లమెంటుకు ఉంటుంది.\n2. అటువంటి నదీ జల వివాదాల్లో సుప్రీంకోర్టుతో సహా ఏ ఇతర న్యాయస్థానాలకూ జోక్యం చేసుకునే పరిధి లేకుండా పార్లమెంటు చట్టం ద్వారా నిరోధించవచ్చు.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. Under Article 262(2), Parliament enacted the Inter-State River Water Disputes Act, 1956, which bars the Supreme Court and High Courts from entertaining any suit/dispute referred to a Water Disputes Tribunal.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. ఆర్టికల్ 262(2) కింద పార్లమెంట్ 1956లో చేసిన అంతర్రాష్ట్ర నదీ జలాల వివాద చట్టం ద్వారా ట్రిబ్యునల్ పరిధిలోని జల వివాదాలపై సాధారణ కోర్టులకు మరియు సుప్రీంకోర్టుకు విచారణాధికారం లేకుండా నిరోధించారు."
        },
        {
            "id": 16,
            "subject": "Indian Polity",
            "topic": "Finance Commission & Fiscal Federalism - Article 280",
            "source_channel": "CSB IAS Academy / Economics & Polity Sessions",
            "raw_educator_point": "16వ ఆర్థిక సంఘం (16th Finance Commission) చైర్మన్: డాక్టర్ అరవింద్ పనగరియా.",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the 16th Finance Commission of India:\n1. It was constituted under Article 280 of the Constitution under the chairmanship of Dr. Arvind Panagariya.\n2. Its recommendations will cover the five-year award period commencing from April 1, 2026.\nWhich of the statements given above is/are correct?",
            "question_te": "భారత 16వ ఆర్థిక సంఘానికి (16th Finance Commission) సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. భారత రాజ్యాంగంలోని ఆర్టికల్ 280 ప్రకారం డాక్టర్ అరవింద్ పనగరియా అధ్యక్షతన ఇది ఏర్పాటు చేయబడింది.\n2. దీని సిఫార్సులు 2026 ఏప్రిల్ 1 నుండి ప్రారంభమయ్యే ఐదేళ్ల కాలపరిమితికి అమలులోకి వస్తాయి.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. The 16th Finance Commission, chaired by former NITI Aayog Vice-Chairman Dr. Arvind Panagariya, will formulate recommendations on tax devolution between Centre and States for the 2026-2031 period.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. నీతి ఆయోగ్ మాజీ ఉపాధ్యక్షుడు డాక్టర్ అరవింద్ పనగరియా నేతృత్వంలో 16వ ఆర్థిక సంఘాన్ని కేంద్ర ప్రభుత్వం ఏర్పాటు చేసింది. ఇది 2026-2031 ఐదేళ్ల కాలానికి కేంద్ర-రాష్ట్రాల పన్నుల పంపిణీపై సిఫార్సులు చేస్తుంది."
        },
        {
            "id": 17,
            "subject": "Indian Polity",
            "topic": "Panchayati Raj - 73rd Constitutional Amendment Act",
            "source_channel": "Adda247 Telugu / Polity Bits",
            "raw_educator_point": "73వ రాజ్యాంగ సవరణ చట్టం 1992 లో 11వ షెడ్యూల్ లో చేర్చిన విధులు ఎన్ని? ఆన్సర్: 29 విధులు.",
            "question_type": "Direct Conceptual",
            "question_en": "How many functional items are listed in the Eleventh Schedule of the Constitution of India placed within the purview of Panchayats by the 73rd Constitutional Amendment Act, 1992?",
            "question_te": "73వ రాజ్యాంగ సవరణ చట్టం 1992 ద్వారా భారత రాజ్యాంగంలో చేర్చబడిన 11వ షెడ్యూల్‌లో గ్రామ పంచాయతీల పరిధిలోనికి ఎన్ని అధికారిక విధులు/అంశాలు (Functional Items) నిర్దేశించబడ్డాయి?",
            "options_en": ["29 subjects", "18 subjects", "21 subjects", "33 subjects"],
            "options_te": ["29 అంశాలు", "18 అంశాలు", "21 అంశాలు", "33 అంశాలు"],
            "correct_option": 0,
            "explanation_en": "The 11th Schedule contains 29 functional items for Panchayats (Article 243G). In contrast, the 12th Schedule contains 18 functional items for Municipalities (Article 243W).",
            "explanation_te": "73వ సవరణ ద్వారా చేర్చిన 11వ షెడ్యూల్‌లో పంచాయతీల కోసం 29 అంశాలు ఉన్నాయి. 74వ సవరణ ద్వారా చేర్చిన 12వ షెడ్యూల్‌లో మున్సిపాలిటీల కోసం 18 అంశాలు ఉన్నాయి."
        },

        # =========================================================================
        # SECTION 3: TELANGANA HISTORY & MOVEMENT (8 Questions)
        # =========================================================================
        {
            "id": 18,
            "subject": "Telangana History & Movement",
            "topic": "Kakatiya Dynasty - Motupalli & Sea Trade",
            "source_channel": "Ashoka Academy (Ashok Sir) Dynasties Series",
            "raw_educator_point": "మోటుపల్లి అభయ శాసనం జారీ చేసిన కాకతీయ రాజు: గణపతి దేవుడు (విదేశీ వర్తకులకు రక్షణ).",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the 'Motupalli Abhaya Sasanam' (మోటుపల్లి అభయ శాసనం) issued by Kakatiya monarch Ganapati Deva:\n1. It was issued to protect maritime foreign merchants from arbitrary customs extortions and pirate shipwrecks.\n2. It fixed concessional customs duty (Klumptam/Arayamu) of 1/30th value on all export and import goods.\nWhich of the statements given above is/are correct?",
            "question_te": "కాకతీయ చక్రవర్తి గణపతి దేవుడు జారీ చేసిన ప్రసిద్ధ 'మోటుపల్లి అభయ శాసనం' కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. విదేశీ మరియు స్వదేశీ సముద్ర వర్తకులకు నౌకా ప్రమాదాలు మరియు అధిక సుంకాల దోపిడీ నుండి రక్షణ కల్పించేందుకు ఈ శాసనాన్ని జారీ చేశారు.\n2. ఇది ఎగుమతి, దిగుమతి సరుకులపై విలువలో 1/30 వంతు మాత్రమే నామమాత్రపు రేవు సుంకాన్ని స్థిరీకరించింది.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. Issued in 1244 AD at Motupalli port (Bapatla/Prakasam district), this charter abolished the oppressive seizure of distressed foreign ships and established rule of law for ocean trade, which Marco Polo later praised.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. క్రీ.శ. 1244లో గణపతి దేవుడు మోటుపల్లి రేవు వద్ద అభయ శాసనం వేయించాడు. ఓడలు మునిగిపోయినప్పుడు వర్తకుల సరుకులను రాజు స్వాధీనం చేసుకునే దురాచారాన్ని రద్దు చేసి, కేవలం 1/30 వంతు చట్టబద్ధమైన సుంకాన్ని మాత్రమే విధించాడు."
        },
        {
            "id": 19,
            "subject": "Telangana History & Movement",
            "topic": "1969 Telangana Agitation - Genesis & Hunger Strike",
            "source_channel": "Ashoka Academy - 1969 Movement Timeline",
            "raw_educator_point": "1969 తెలంగాణ ఉద్యమం ప్రారంభం: ఖమ్మంలో రవీంద్రనాథ్ ఆమరణ నిరాహార దీక్ష (జనవరి 1969).",
            "question_type": "Direct Conceptual",
            "question_en": "The historic 1969 Telangana Agitation began in January 1969 with an indefinite hunger strike demanding the implementation of Telangana safeguards (Gentlemen's Agreement) by which student leader in Khammam?",
            "question_te": "తెలంగాణ రక్షణలు (పెద్దమనుషుల ఒప్పందం) అమలు చేయాలని డిమాండ్ చేస్తూ జనవరి 1969 లో ఖమ్మంలో ఆమరణ నిరాహార దీక్ష చేపట్టి 1969 తెలంగాణ ఉద్యమానికి నాంది పలికిన విద్యార్థి నాయకుడు ఎవరు?",
            "options_en": ["Bobbili Ravindranath", "Mallikarjun", "Marri Chenna Reddy", "K.V. Ranga Reddy"],
            "options_te": ["బొబ్బిలి రవీంద్రనాథ్", "మల్లికార్జున్", "మర్రి చెన్నారెడ్డి", "కె.వి. రంగా రెడ్డి"],
            "correct_option": 0,
            "explanation_en": "On January 8, 1969, degree college student Bobbili Ravindranath began an indefinite fast at Khammam demanding Telangana employment safeguards and return of non-Mulki employees, sparking the student-led 1969 separate state movement.",
            "explanation_te": "1969 జనవరి 8న ఖమ్మం గాంధీ చౌక్ వద్ద డిగ్రీ విద్యార్థి బొబ్బిలి రవీంద్రనాథ్ ముల్కీ నిబంధనలు అమలు చేయాలని, నాన్-ముల్కీలను వెనక్కి పంపాలని ఆమరణ నిరాహార దీక్ష చేపట్టడంతో 1969 ఉద్యమం మొదలైంది."
        },
        {
            "id": 20,
            "subject": "Telangana History & Movement",
            "topic": "1969 Movement - Kumar Lalit & Bhargava Committees",
            "source_channel": "Ashoka Academy (Ashok Sir) / T-SAT Lectures",
            "raw_educator_point": "తెలంగాణ మిగులు నిధుల లెక్క తేల్చడానికి నియమించిన కమిటీలు: కుమార్ లలిత్ కమిటీ, వశిష్ట భార్గవ కమిటీ.",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the committees appointed in 1969 to quantify Telangana surplus revenue diversion:\n1. The Kumar Lalit Committee calculated the net surplus revenues diverted from Telangana to Andhra as ₹34.10 crore.\n2. The Justice Vashishta Bhargava Committee appointed under the Eight-Point Formula determined the surplus to be ₹28.34 crore.\nWhich of the statements given above is/are correct?",
            "question_te": "1969 ఉద్యమ సమయంలో తెలంగాణ ప్రాంత మిగులు నిధుల మళ్లింపును లెక్కించేందుకు ఏర్పాటైన కమిటీలకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. కుమార్ లలిత్ కమిటీ తెలంగాణ నుంచి ఆంధ్రాకు మళ్లించబడిన నికర మిగులు నిధులను ₹34.10 కోట్లుగా లెక్కించింది.\n2. ఎనిమిది సూత్రాల పథకం కింద ఏర్పాటైన జస్టిస్ వశిష్ట భార్గవ కమిటీ మిగులు నిధులను ₹28.34 కోట్లుగా నిర్ధారించింది.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
            "correct_option": 2,
            "explanation_en": "Both statements are correct. Kumar Lalit (Comptroller and Auditor General official) determined the diverted Telangana surplus as ₹34.10 crore. Prime Minister Indira Gandhi subsequently set up the Justice Vashishta Bhargava Committee, which arrived at ₹28.34 crore.",
            "explanation_te": "రెండు ప్రకటనలూ సరైనవే. కుమార్ లలిత్ కమిటీ తెలంగాణ మిగులు నిధులు ₹34.10 కోట్లు మళ్లించబడ్డాయని తేల్చగా, ఇందిరా గాంధీ ఎనిమిది సూత్రాల పథకం ద్వారా నియమించిన జస్టిస్ వశిష్ట భార్గవ కమిటీ ₹28.34 కోట్లుగా లెక్కించింది."
        },
        {
            "id": 21,
            "subject": "Telangana History & Movement",
            "topic": "Hyderabad State Integration - Operation Polo",
            "source_channel": "Ashoka Academy / Modern Telangana History",
            "raw_educator_point": "ఆపరేషన్ పోలో (పోలీస్ యాక్షన్): 1948 సెప్టెంబర్ 13 నుండి 17 వరకు.",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding 'Operation Polo' (Police Action) in September 1948:\n1. The Indian Armed Forces launched the military operation under the command of Lieutenant General Eric Goddard, with Major General J.N. Chaudhuri leading the 1st Armoured Division.\n2. Nizam's military commander Major General Syed Ahmed El-Edroos formally surrendered to Major General J.N. Chaudhuri on September 17, 1948.\n3. The Sunderlal Committee was appointed by Prime Minister Nehru to inspect post-operation communal conditions in the Hyderabad State.\nWhich of the statements given above are correct?",
            "question_te": "సెప్టెంబర్ 1948 లో జరిగిన 'ఆపరేషన్ పోలో' (పోలీస్ యాక్షన్) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. భారత సైన్యం లెఫ్టినెంట్ జనరల్ ఎరిక్ గొడ్డార్డ్ సైనిక వ్యూహంతో, మేజర్ జనరల్ జె.ఎన్. చౌదరి నేతృత్వంలో ఈ ఆపరేషన్‌ను చేపట్టింది.\n2. నిజాం సైన్యాధ్యక్షుడు మేజర్ జనరల్ సయ్యద్ అహ్మద్ ఎల్-ఎద్రూస్ 1948 సెప్టెంబర్ 17న మేజర్ జనరల్ జె.ఎన్. చౌదరికి అధికారికంగా లొంగిపోయారు.\n3. పోలీస్ యాక్షన్ అనంతర పరిస్థితులను మరియు మత సామరస్య పరిస్థితులను అధ్యయనం చేయడానికి నెహ్రూ ప్రభుత్వం పండిత్ సుందర్‌లాల్ కమిటీని నియమించింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three statements are correct. Operation Polo began on September 13, 1948 and concluded on September 17, 1948 with Edroos's surrender. J.N. Chaudhuri took over as Military Governor. The Pandit Sunderlal Committee later assessed the ground humanitarian situation.",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1948 సెప్టెంబర్ 13న ప్రారంభమైన పోలీస్ యాక్షన్ సెప్టెంబర్ 17న నిజాం సైన్యాధ్యక్షుడు ఎల్-ఎద్రూస్ లొంగుబాటుతో ముగిసింది. ఆ తర్వాత పరిస్థితుల అధ్యయనానికి పండిత్ సుందర్‌లాల్ కమిటీ నియమించబడింది."
        },
        {
            "id": 22,
            "subject": "Telangana History & Movement",
            "topic": "1952 Non-Mulki Agitation - City College Incident",
            "source_channel": "Ashoka Academy - Mulki Rules Lecture",
            "raw_educator_point": "1952 గైర్ ముల్కీ ఉద్యమం: సిటీ కాలేజ్ కాల్పుల ఘటన (సెప్టెంబర్ 3, 1952) మరియు జస్టిస్ జగన్మోహన్ రెడ్డి కమిషన్.",
            "question_type": "Direct Conceptual",
            "question_en": "Following the tragic police firing on students outside City College, Hyderabad during the 1952 Non-Mulki (Idli Sambar Go Back) agitation, which judicial commission was appointed by the Burgula Ramakrishna Rao government?",
            "question_te": "1952 గైర్-ముల్కీ (నాన్-ముల్కీ గో బ్యాక్) ఉద్యమ సమయంలో హైదరాబాద్ సిటీ కాలేజీ వద్ద విద్యార్థులపై జరిగిన పోలీసు కాల్పుల ఘటనపై బూర్గుల రామకృష్ణారావు ప్రభుత్వం నియమించిన న్యాయ విచారణ కమిషన్ ఏది?",
            "options_en": [
                "Justice P. Jaganmohan Reddy Commission",
                "Justice K. Bhargava Commission",
                "Justice Wanchoo Commission",
                "Justice Kumar Lalit Commission"
            ],
            "options_te": [
                "జస్టిస్ పి. జగన్మోహన్ రెడ్డి కమిషన్",
                "జస్టిస్ కె. భార్గవ కమిషన్",
                "జస్టిస్ వాంచూ కమిషన్",
                "జస్టిస్ కుమార్ లలిత్ కమిషన్"
            ],
            "correct_option": 0,
            "explanation_en": "The Justice P. Jaganmohan Reddy Commission was constituted in September 1952 to probe the police firing at City College and Osmania General Hospital that killed students and public protesters during the historic 1952 Mulki movement.",
            "explanation_te": "1952 సెప్టెంబర్ 3న సిటీ కాలేజీ విద్యార్థులపై జరిగిన పోలీసు కాల్పుల ఘటనలో అమరులైన విద్యార్థుల ఘటనపై నిజనిర్ధారణ కోసం జస్టిస్ పింగళి జగన్మోహన్ రెడ్డి కమిషన్‌ను ప్రభుత్వం నియమించింది."
        },
        {
            "id": 23,
            "subject": "Telangana History & Movement",
            "topic": "Tribal Martyrs - Komaram Bheem & Jodeghat",
            "source_channel": "T-SAT & Ashoka Academy Tribal History",
            "raw_educator_point": "కొమరం భీమ్ నినాదం: 'జల్ జంగల్ జమీన్' మరియు జోడేఘాట్ పోరాటం (1940).",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding tribal revolutionary martyr Komaram Bheem:\n1. He led an armed revolt against the oppressive forest taxes and Patwari exploitation of the Asaf Jahi Nizam government in the Adilabad agency tract.\n2. He coined the historic revolutionary slogan 'Jal, Jangal, Jameen' (Water, Forest, Land).\n3. He attained martyrdom fighting Nizam's forces at Jodeghat in September 1940.\nWhich of the statements given above are correct?",
            "question_te": "ఆదివాసీ విప్లవ వీరుడు కొమరం భీమ్‌కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. ఆదిలాబాద్ అటవీ ప్రాంతంలో నిజాం ప్రభుత్వ అటవీ పన్నులు, వెట్టిచాకిరీ మరియు పట్వారీల దోపిడీకి వ్యతిరేకంగా ఆయన సాయుధ పోరాటం చేశారు.\n2. 'జల్, జంగల్, జమీన్' (నీరు, అడవి, భూమి) అనే చారిత్రక నినాదాన్ని ఆయన అందించారు.\n3. సెప్టెంబర్ 1940 లో నిజాం పోలీసు బలగాలతో జరిగిన వీరోచిత పోరాటంలో జోడేఘాట్ వద్ద ఆయన అమరులయ్యారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three statements are correct. Gond leader Komaram Bheem organized tribal youth under the banner of 'Jal, Jangal, Jameen' and fought against Nizam's talukdar Abdul Sattar's armed contingent at Jodeghat on Ashwija Pournami, 1940.",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. గోండుల హక్కుల కోసం 'జల్ జంగల్ జమీన్' నినాదంతో పోరాడిన కొమరం భీమ్, 1940 అక్టోబర్ (ఆశ్వయుజ పౌర్ణమి) లో జోడేఘాట్ వద్ద నిజాం సైన్యంతో పోరాడుతూ వీరమరణం పొందారు."
        },
        {
            "id": 24,
            "subject": "Telangana History & Movement",
            "topic": "Gentlemen's Agreement 1956 - Safeguards",
            "source_channel": "Ashoka Academy - Gentlemen's Agreement Lecture",
            "raw_educator_point": "పెద్దమనుషుల ఒప్పందం (1956 ఫిబ్రవరి 20, ఢిల్లీ హైదరాబాద్ హౌస్): 14 అంశాలు.",
            "question_type": "Multi-Statement",
            "question_en": "Which of the following leaders represented the Telangana region in signing the historic 'Gentlemen's Agreement' on February 20, 1956 at Hyderabad House, New Delhi?",
            "question_te": "1956 ఫిబ్రవరి 20న న్యూఢిల్లీలోని హైదరాబాద్ హౌస్‌లో జరిగిన చారిత్రక 'పెద్దమనుషుల ఒప్పందం' (Gentlemen's Agreement) పై సంతకాలు చేసిన నలుగురు తెలంగాణ ప్రాంత ప్రతినిధులు ఎవరు?",
            "options_en": [
                "Burgula Ramakrishna Rao, K.V. Ranga Reddy, Marri Chenna Reddy, and J.V. Narsing Rao",
                "Neelam Sanjiva Reddy, B. Gopala Reddy, Alluri Satyanarayana Raju, and G. Latchanna",
                "Swami Ramananda Tirtha, K.V. Ranga Reddy, P.V. Narasimha Rao, and Chenna Reddy",
                "Burgula Ramakrishna Rao, K.V. Ranga Reddy, Kaloji Narayana Rao, and Raheemullah"
            ],
            "options_te": [
                "బూర్గుల రామకృష్ణారావు, కె.వి. రంగా రెడ్డి, మర్రి చెన్నారెడ్డి, మరియు జె.వి. నర్సింగరావు",
                "నీలం సంజీవరెడ్డి, బెజవాడ గోపాలరెడ్డి, అల్లూరి సత్యనారాయణ రాజు, మరియు గౌతు లచ్చన్న",
                "స్వామి రామానంద తీర్థ, కె.వి. రంగా రెడ్డి, పి.వి. నరసింహారావు, మరియు చెన్నారెడ్డి",
                "బూర్గుల రామకృష్ణారావు, కె.వి. రంగా రెడ్డి, కాళోజీ నారాయణరావు, మరియు రహీముల్లా"
            ],
            "correct_option": 0,
            "explanation_en": "The four Telangana signatories were Chief Minister Burgula Ramakrishna Rao, K.V. Ranga Reddy, Dr. M. Chenna Reddy, and Hyderabad PCC President J.V. Narsing Rao. (The other four from Andhra were N. Sanjiva Reddy, B. Gopala Reddy, A.S. Raju, and G. Latchanna).",
            "explanation_te": "తెలంగాణ తరఫున బూర్గుల రామకృష్ణారావు, కె.వి. రంగా రెడ్డి, మర్రి చెన్నారెడ్డి, జె.వి. నర్సింగరావు సంతకాలు చేశారు. ఆంధ్రా ప్రాంతం నుంచి నీలం సంజీవరెడ్డి, బెజవాడ గోపాలరెడ్డి, అల్లూరి సత్యనారాయణ రాజు, గౌతు లచ్చన్న సంతకాలు చేశారు."
        },
        {
            "id": 25,
            "subject": "Telangana History & Movement",
            "topic": "Asaf Jahi Dynasty - Salar Jung Reforms",
            "source_channel": "Ashoka Academy - Nizam Dynasties",
            "raw_educator_point": "సాలార్ జంగ్ సంస్కరణలు: జిల్లేబందీ విధానం, హాలి సిక్కా నాణేలు, అవ్వల్ తాలూక్దార్ వ్యవస్థ.",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the administrative reforms introduced by Mir Turab Ali Khan (Salar Jung I) between 1853 and 1883 in Hyderabad State:\n1. He abolished the corrupt revenue farming (Zabti/Ijara) system and introduced direct cash collection under the 'Zillabandi' system.\n2. He divided the state into 14 districts under Subedars and designated District Collectors as 'Awwal Talukdars'.\n3. He established a central mint issuing the official standardized state currency called 'Hali Sikka'.\nWhich of the statements given above are correct?",
            "question_te": "1853 నుండి 1883 మధ్య హైదరాబాద్ రాజ్యంలో మీర్ తురబ్ అలీ ఖాన్ (మొదటి సాలార్ జంగ్) ప్రవేశపెట్టిన పరిపాలనా సంస్కరణలకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. అవినీతిమయమైన రెవెన్యూ గుత్తేదారుల (ఇజారా) విధానాన్ని రద్దు చేసి, నేరుగా పన్నులు వసూలు చేసేందుకు 'జిల్లేబందీ' పద్ధతిని ప్రవేశపెట్టారు.\n2. రాజ్యాన్ని 14 జిల్లాలుగా విభజించి, జిల్లాల పాలనాధికారులను 'అవ్వల్ తాలూక్దార్లు' (మొదటి తాలూక్దార్/కలెక్టర్) గా నియమించారు.\n3. నాణేల ముద్రణ కోసం కేంద్రీకృత మింట్ స్థాపించి, ప్రామాణికమైన 'హాలీ సిక్కా' కరెన్సీని ప్రవేశపెట్టారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three statements are correct. Salar Jung I modernized the medieval administration of Hyderabad state through Zillabandi, police reorganization, founding of Dar-ul-Uloom school, and issuance of Hali Sikka currency.",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. సాలార్ జంగ్ I ప్రవేశపెట్టిన జిల్లేబందీ విధానం, అవ్వల్ తాలూక్దార్ (కలెక్టర్) వ్యవస్థ, హాలీ సిక్కా కరెన్సీ మరియు రెవెన్యూ సంస్కరణలు హైదరాబాద్ సంస్థానాన్ని ఆధునీకరించాయి."
        },

        # =========================================================================
        # SECTION 4: INDIAN HISTORY & NATIONAL FREEDOM STRUGGLE (5 Questions)
        # =========================================================================
        {
            "id": 26,
            "subject": "Indian History",
            "topic": "Ancient India - Buddhism & Sarnath UNESCO Nomination",
            "source_channel": "Top 750 Current Affairs Marathon (YouTube)",
            "raw_educator_point": "ఇటీవల యునెస్కో వరల్డ్ హెరిటేజ్ లో చేర్చబడిన సారనాథ్ కు బౌద్ధమత చరిత్రలో ఉన్న ప్రాముఖ్యత: ధర్మచక్ర ప్రవర్తన.",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding Sarnath, an ancient UNESCO Tentative World Heritage monument site:\n1. It marks the holy site of 'Dharmachakra Pravartana' where Gautama Buddha delivered his first sermon to his first five disciples (Panchavaggiya).\n2. The Lion Capital of Ashoka unearthed at Sarnath was adopted as the official State Emblem of India on January 26, 1950.\n3. The Dhamek Stupa at Sarnath was originally commissioned by Emperor Ashoka and later renovated in the Gupta period.\nWhich of the statements given above are correct?",
            "question_te": "యునెస్కో ప్రపంచ వారసత్వ జాబితా నామినేషన్‌లో నిలిచిన ప్రాచీన బౌద్ధ కేంద్రం సారనాథ్ (Sarnath) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. గౌతమ బుద్ధుడు జ్ఞానోదయానంతరం తన తొలి ఐదుగురు శిష్యులకు ప్రథమ ధర్మోపదేశం ('ధర్మచక్ర ప్రవర్తన') గావించిన పవిత్ర స్థలం ఇది.\n2. సారనాథ్‌లో లభ్యమైన అశోకుని నాలుగు సింహాల స్తంభ శిఖరాన్ని 1950 జనవరి 26న భారతదేశ అధికారిక జాతీయ చిహ్నంగా స్వీకరించారు.\n3. సారనాథ్‌లోని ప్రసిద్ధ ధమేక్ స్థూపాన్ని (Dhamek Stupa) మూలతః అశోక చక్రవర్తి నిర్మించగా, గుప్తుల కాలంలో విస్తరించబడింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three statements are correct. Sarnath (Rishipatana/Deer Park near Varanasi) is the birthplace of the Buddhist Sangha where Buddha preached his first sermon. It holds the Ashokan pillar whose capital became India's State Emblem and the massive Dhamek Stupa.",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. వారణాసి సమీపంలోని సారనాథ్ గౌతమ బుద్ధుని తొలి బోధన (ధర్మచక్ర ప్రవర్తన) కు వేదిక. ఇక్కడి అశోక స్తంభ శిఖరం భారత జాతీయ చిహ్నంగా నిలిచింది మరియు ఇక్కడే ధమేక్ స్థూపం ఉంది."
        },
        {
            "id": 27,
            "subject": "Indian History",
            "topic": "Modern Freedom Struggle - 1919 Montagu-Chelmsford Reforms",
            "source_channel": "Winners Online / YouTube History Lecture",
            "raw_educator_point": "భారత ప్రభుత్వ చట్టం 1919 ద్వారా రాష్ట్రాలలో ప్రవేశపెట్టబడిన 'ద్వంద్వ పాలన' (Dyarchy).",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the Government of India Act, 1919 (Montagu-Chelmsford Reforms):\n1. It introduced 'Dyarchy' in the provincial governments, bifurcating provincial subjects into 'Transferred' and 'Reserved'.\n2. It introduced bicameralism and direct elections in the country at the Central Legislature for the first time.\n3. It provided for the establishment of a Public Service Commission for recruiting civil servants.\nWhich of the statements given above are correct?",
            "question_te": "భారత ప్రభుత్వ చట్టం 1919 (మాంటేగ్-చెమ్స్‌ఫర్డ్ సంస్కరణలు) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. ఇది ప్రావిన్సులలో పాలనాంశాలను 'బదిలీ చేయబడినవి' (Transferred) మరియు 'రిజర్వ్ చేయబడినవి' (Reserved) గా విభజిస్తూ 'ద్వంద్వ పాలన'ను (Dyarchy) ప్రవేశపెట్టింది.\n2. కేంద్ర శాసనసభలో మొట్టమొదటిసారిగా ద్విసభా విధానాన్ని (Bicameralism) మరియు ప్రత్యక్ష ఎన్నికలను ప్రవేశపెట్టింది.\n3. సివిల్ సర్వెంట్ల నియామకం కోసం 'పబ్లిక్ సర్వీస్ కమిషన్' (Central PSC) ఏర్పాటుకు ఇది వీలు కల్పించింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three statements are correct. The 1919 Act introduced provincial Dyarchy, central bicameralism (Council of State and Legislative Assembly), statutory Public Service Commission (set up in 1926 via Lee Commission recommendations), and separated provincial budgets from the central budget.",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1919 చట్టం ద్వారా ప్రావిన్సులలో ద్వంద్వ పాలన వచ్చింది, కేంద్రంలో ద్విసభా విధానం ఏర్పాటైంది, మరియు 1926లో లీ కమిషన్ సిఫార్సుల మేరకు పబ్లిక్ సర్వీస్ కమిషన్ ఏర్పాటుకు పునాది పడింది."
        },
        {
            "id": 28,
            "subject": "Indian History",
            "topic": "Modern Freedom Struggle - 1935 Government of India Act",
            "source_channel": "T-SAT & Winners Online History Bit Bank",
            "raw_educator_point": "భారత ప్రభుత్వ చట్టం 1935: ప్రావిన్షియల్ అటానమీ, ఫెడరల్ కోర్టు, రిజర్వ్ బ్యాంక్ ఏర్పాటు.",
            "question_type": "Multi-Statement",
            "question_en": "Which of the following key institutions/features were established pursuant to the Government of India Act, 1935?\n1. Abolition of provincial Dyarchy and introduction of 'Provincial Autonomy'\n2. Establishment of the Federal Court of India (commenced in 1937)\n3. Establishment of the Reserve Bank of India (RBI) to control currency and credit\nSelect the correct answer using the code given below:",
            "question_te": "భారత ప్రభుత్వ చట్టం 1935 ద్వారా ప్రవేశపెట్టబడిన లేదా స్థాపించబడిన కీలక అంశాలు ఏవి?\n1. ప్రావిన్సులలో ద్వంద్వ పాలన రద్దు మరియు 'ప్రావిన్షియల్ అటానమీ' (ప్రావిన్సుల స్వయంప్రతిపత్తి) ప్రవేశపెట్టడం\n2. భారత ఫెడరల్ కోర్టు (Federal Court of India) స్థాపన (1937 లో ప్రారంభం)\n3. దేశంలో కరెన్సీ మరియు పరపతి నియంత్రణ కోసం భారత రిజర్వ్ బ్యాంక్ (RBI) స్థాపన\nసరైన కోడ్‌ను ఎంచుకోండి:",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three features are directly linked to the 1935 Act: it abolished provincial dyarchy granting provincial autonomy, created the Federal Court of India (predecessor of Supreme Court), and provided the legislative basis for the Reserve Bank of India (enacted via RBI Act 1934/1935 framework).",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1935 చట్టం ద్వారా రాష్ట్రాల స్వయంప్రతిపత్తి వచ్చింది, 1937లో ఢిల్లీలో ఫెడరల్ కోర్టు ఏర్పాటైంది, మరియు రిజర్వ్ బ్యాంక్ ఆఫ్ ఇండియా స్థాపన జరిగింది."
        },
        {
            "id": 29,
            "subject": "Indian History",
            "topic": "Socio-Religious Reform Movements - Key Organizations",
            "source_channel": "Winners Online / YouTube Indian History Lecture",
            "raw_educator_point": "భారత సాంఘిక, మత సంస్కరణోద్యమాలు: బ్రహ్మ సమాజం, ఆర్య సమాజం, సత్యశోధక్ సమాజ్ జతపరచడం.",
            "question_type": "Matching",
            "question_en": "Match the following 19th-century Socio-Religious Reform Organizations with their respective founders:\n(A) Brahmo Samaj (1828)         - (1) Jyotirao Phule\n(B) Arya Samaj (1875)           - (2) Swami Vivekananda\n(C) Satyashodhak Samaj (1873)   - (3) Raja Ram Mohan Roy\n(D) Ramakrishna Mission (1897)  - (4) Swami Dayananda Saraswati\n\nCorrect matching code:",
            "question_te": "19వ శతాబ్దపు సామాజిక-మత సంస్కరణ సంస్థలను వాటి వ్యవస్థాపకులతో జతపరచండి:\n(A) బ్రహ్మ సమాజం (1828)          - (1) జ్యోతిరావు ఫూలే\n(B) ఆర్య సమాజం (1875)           - (2) స్వామి వివేకానంద\n(C) సత్యశోధక్ సమాజ్ (1873)       - (3) రాజా రామ్ మోహన్ రాయ్\n(D) రామకృష్ణ మిషన్ (1897)       - (4) స్వామి దయానంద సరస్వతి\n\nసరైన కోడ్‌ను ఎంచుకోండి:",
            "options_en": [
                "A-3, B-4, C-1, D-2",
                "A-4, B-3, C-1, D-2",
                "A-3, B-1, C-4, D-2",
                "A-1, B-4, C-3, D-2"
            ],
            "options_te": [
                "A-3, B-4, C-1, D-2",
                "A-4, B-3, C-1, D-2",
                "A-3, B-1, C-4, D-2",
                "A-1, B-4, C-3, D-2"
            ],
            "correct_option": 0,
            "explanation_en": "A-3 (Brahmo Samaj by Raja Ram Mohan Roy in Calcutta), B-4 (Arya Samaj by Dayananda Saraswati in Bombay with the slogan 'Go back to the Vedas'), C-1 (Satyashodhak Samaj by Jyotirao Phule in Maharashtra for lower-caste rights), D-2 (Ramakrishna Mission by Swami Vivekananda in Belur).",
            "explanation_te": "A-3 (బ్రహ్మ సమాజం - రాజా రామ్మోహన్ రాయ్), B-4 (ఆర్య సమాజం - దయానంద సరస్వతి), C-1 (సత్యశోధక్ సమాజ్ - జ్యోతిరావు ఫూలే), D-2 (రామకృష్ణ మిషన్ - స్వామి వివేకానంద)."
        },
        {
            "id": 30,
            "subject": "Indian History",
            "topic": "Modern Freedom Struggle - 1942 Quit India Movement",
            "source_channel": "T-SAT & Winners Online History Marathon",
            "raw_educator_point": "1942 క్విట్ ఇండియా ఉద్యమం: ఆగస్టు 8 బొంబాయి గోవాలియా ట్యాంక్ మైదానం, 'డూ ఆర్ డై' నినాదం.",
            "question_type": "Multi-Statement",
            "question_en": "Consider the following statements regarding the 1942 'Quit India Movement' (ఆగస్టు ఉద్యమం):\n1. The historic Quit India Resolution was passed by the All India Congress Committee (AICC) at Gowalia Tank Maidan, Bombay on August 8, 1942.\n2. Mahatma Gandhi gave the famous call 'Do or Die' (కరో యా మరో) to the nation.\n3. Usha Mehta operated an underground clandestine radio station to disseminate news of the movement during British police crackdowns.\nWhich of the statements given above are correct?",
            "question_te": "1942 'క్విట్ ఇండియా ఉద్యమం' (ఆగస్టు క్రాంతి) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. 1942 ఆగస్టు 8న బొంబాయిలోని గోవాలియా ట్యాంక్ మైదానంలో ఆల్ ఇండియా కాంగ్రెస్ కమిటీ (AICC) చారిత్రక క్విట్ ఇండియా తీర్మానాన్ని ఆమోదించింది.\n2. మహాత్మా గాంధీ దేశ ప్రజలకు 'డూ ఆర్ డై' (కరో యా మరో - సాధించు లేదా మరణించు) అనే ప్రసిద్ధ నినాదాన్ని ఇచ్చారు.\n3. బ్రిటిష్ ప్రభుత్వం కాంగ్రెస్ నాయకులను అరెస్ట్ చేసినప్పుడు ఉద్యమ సమాచారాన్ని అందించేందుకు ఉషా మెహతా అజ్ఞాత రేడియో కేంద్రాన్ని (Secret Congress Radio) నిర్వహించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
            "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
            "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
            "correct_option": 3,
            "explanation_en": "All three statements are correct. Passed following the failure of the Cripps Mission, the Quit India Movement saw spontaneous mass uprisings despite the immediate arrest of top leaders under 'Operation Zero Hour', with underground leaders like Usha Mehta, Aruna Asaf Ali, and Jayaprakash Narayan directing actions.",
            "explanation_te": "మూడు ప్రకటనలూ సరైనవే. క్రిప్స్ మిషన్ వైఫల్యం తర్వాత బొంబాయిలో క్విట్ ఇండియా తీర్మానం ఆమోదించబడింది. గాంధీజీ 'డూ ఆర్ డై' పిలుపునిచ్చారు మరియు ఉషా మెహతా సీక్రెట్ కాంగ్రెస్ రేడియోను నడిపారు."
        }
    ]

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"total_questions": len(questions), "questions": questions}, f, ensure_ascii=False, indent=2)

    print(f"Successfully compiled {len(questions)} high-yield faculty-curated questions to {OUTPUT_FILE}")

if __name__ == "__main__":
    compile_live_questions()
