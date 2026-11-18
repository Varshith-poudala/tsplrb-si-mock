# -*- coding: utf-8 -*-
"""
Mock Test 10 - General Studies Part 2 (Q151 to Q200)
Strictly adheres to TSPLRB SI PWT Blueprint & Shentu's feedback:
- 151 to 164: Geography & Environment (India & Telangana) (14 Questions)
  * Godavari & Krishna basins, Western/Eastern Ghats passes, Soils, Biosphere reserves, Amrabad & Kawal Tiger reserves, Kaleshwaram, Singareni, Ramsar, Monsoon, El Niño.
- 165 to 174: Indian & Telangana Economy (10 Questions)
  * RBI Repo Rate & Monetary tools, Money supply M1/M3, Inflation & CPI, Fiscal Deficit & FRBM, GST Council, PSL targets, NITI Aayog MPI, Telangana GSDP services, TS-iPASS.
- 175 to 188: General Science & Technology (14 Questions)
  * Total Internal Reflection, Power of Lens, Sound Doppler effect, Faraday Induction, pH blood/rain, Carbon Allotropes, Baking/Washing Soda, Insulin/Pancreas, Vitamins, CRISPR-Cas9, Vaccines, ISRO Aditya-L1, Chandrayaan-3 Shiv Shakti point, Gaganyaan.
- 189 to 200: Current Affairs & International Organizations (12 Questions - Shentu's specific focus!)
  * 16th BRICS Summit Kazan expansion, SCO Summit Islamabad, ASEAN Summit Vientiane, G20 Rio Brazil, QUAD Summit Delaware, COP28/29 UAE Consensus, ECI Appointment Act, 16th Finance Commission (Dr. Arvind Panagariya), Bharat Ratna recipients, Vande Bharat/Kavach, Chess Olympiad Budapest double gold, Telangana HYDRAA & Musi.
- Statement I & II and List-I & II cleanly formatted on separate lines.
- Complete bilingual English & Telugu.
"""

def make_q(id_num, topic, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
    return {
        "id": id_num,
        "qNumber": id_num,
        "section": "General Studies",
        "topic": topic,
        "question_en": q_en.strip(),
        "question_te": q_te.strip(),
        "options_en": [str(o).strip() for o in opts_en],
        "options_te": [str(o).strip() for o in opts_te],
        "correct_option": corr,
        "explanation_en": exp_en.strip(),
        "explanation_te": exp_te.strip()
    }

def get_gs_part2():
    qs = []

    # =========================================================================
    # GEOGRAPHY & ENVIRONMENT (151 - 164: 14 Questions)
    # =========================================================================

    # Q151: Godavari River System
    qs.append(make_q(
        151, "Geography - Drainage System of Telangana",
        "Consider the following statements regarding the Godavari River:\n\nStatement I: The Godavari originates at Trimbakeshwar in the Nashik district of Maharashtra and enters Telangana at Kandakurthi in Nizamabad district.\nStatement II: Pranahita, the largest tributary of Godavari, is formed by the confluence of the Wardha, Painganga, and Wainganga rivers.\n\nWhich of the statements given above is/are correct?",
        "గోదావరి నది వ్యవస్థకు సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: గోదావరి నది మహారాష్ట్రలోని నాసిక్ జిల్లా త్రయంబకేశ్వర్ వద్ద జన్మించి, నిజామాబాద్ జిల్లా కందకుర్తి వద్ద తెలంగాణలోకి ప్రవేశిస్తుంది.\nప్రకటన II: గోదావరి యొక్క అతిపెద్ద ఉపనది అయిన ప్రాణహిత నది వార్ధా, పెన్ గంగ మరియు వైన్ గంగ నదుల కలయిక వలన ఏర్పడుతుంది.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are correct. Godavari enters Telangana at Kandakurthi (confluence of Godavari, Manjira, and Haridra), and Pranahita is formed by Wardha, Penganga, and Wainganga, discharging the highest volume into Godavari.",
        "రెండు ప్రకటనలు సరైనవి. గోదావరి కందకుర్తి వద్ద ప్రవేశిస్తుంది మరియు ప్రాణహిత వార్ధా, పెన్‌గంగ, వైన్‌గంగల కలయికతో ఏర్పడే అతిపెద్ద ఉపనది."
    ))

    # Q152: Krishna River Basin
    qs.append(make_q(
        152, "Geography - Krishna River Basin",
        "The Krishna River enters Telangana state at which location before being joined by its major tributaries including Tungabhadra, Musi, and Dindi?",
        "కృష్ణా నది తుంగభద్ర, మూసి మరియు దిండి వంటి ప్రధాన ఉపనదులతో సంగమించడానికి ముందు తెలంగాణ రాష్ట్రంలోకి ఏ ప్రాంతం వద్ద ప్రవేశిస్తుంది?",
        ["Tangadi in Makthal mandal (Narayanpet district)", "Kaleshwaram in Bhupalpally", "Wadapally in Nalgonda", "Alampur in Jogulamba Gadwal"],
        ["తంగడి, మక్తల్ మండలం (నారాయణపేట జిల్లా)", "కాళేశ్వరం (భూపాలపల్లి)", "వాడపల్లి (నల్గొండ)", "అలంపూర్ (జోగులాంబ గద్వాల)"],
        0,
        "The Krishna River rises near Mahabaleshwar in Maharashtra and enters Telangana at Tangadi village in Makthal mandal of Narayanpet district.",
        "కృష్ణా నది మహారాష్ట్రలోని మహాబలేశ్వర్ వద్ద జన్మించి, నారాయణపేట జిల్లా మక్తల్ మండలం తంగడి గ్రామం వద్ద తెలంగాణలోకి ప్రవేశిస్తుంది."
    ))

    # Q153: Western Ghats Mountain Passes
    qs.append(make_q(
        153, "Geography - Physiography of India",
        "Match List-I (Mountain Pass in Western Ghats) with List-II (Connected Cities / Regions):\n\nList-I\t\t\tList-II\nA. Thal Ghat\t\t1. Mumbai to Pune\nB. Bhor Ghat\t\t2. Mumbai to Nashik\nC. Palghat Gap\t\t3. Madurai to Kollam\nD. Shencottah Pass\t4. Palakkad to Coimbatore\n\nChoose the correct code:",
        "జాబితా-I (పశ్చిమ కనుమల కనుమ) ను జాబితా-II (కలిపే నగరాలు / ప్రాంతాలు) తో జతపరచండి:\n\nజాబితా-I\t\t\tజాబితా-II\nA. థాల్ ఘాట్\t\t1. ముంబై నుండి పూణే\nB. భోర్ ఘాట్\t\t2. ముంబై నుండి నాసిక్\nC. పాల్ఘాట్ కనుమ\t\t3. మదురై నుండి కొల్లాం\nD. షెంకోట్టా కనుమ\t4. పాలక్కాడ్ నుండి కోయంబత్తూరు\n\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-2, B-1, C-4, D-3", "A-1, B-2, C-4, D-3", "A-2, B-1, C-3, D-4", "A-4, B-3, C-2, D-1"],
        ["A-2, B-1, C-4, D-3", "A-1, B-2, C-4, D-3", "A-2, B-1, C-3, D-4", "A-4, B-3, C-2, D-1"],
        0,
        "Thal Ghat connects Mumbai to Nashik (A-2). Bhor Ghat connects Mumbai to Pune (B-1). Palghat Gap connects Palakkad (Kerala) to Coimbatore (TN) (C-4). Shencottah Pass connects Madurai (TN) to Kollam (Kerala) (D-3). Code: A-2, B-1, C-4, D-3.",
        "థాల్ ఘాట్ (A-2), భోర్ ఘాట్ (B-1), పాల్ఘాట్ (C-4), షెంకోట్టా (D-3). సరైన కోడ్: A-2, B-1, C-4, D-3."
    ))

    # Q154: Mechanism of Indian Monsoon
    qs.append(make_q(
        154, "Geography - Indian Monsoon Mechanism",
        "Which of the following factors plays a critical role in the onset and intensity of the South-West Monsoon over the Indian subcontinent?",
        "భారత ఉపఖండంలో నైరుతి రుతుపవనాల ఆగమనం మరియు తీవ్రతలో కీలక పాత్ర పోషించే అంశం ఏది?",
        ["Intense summer heating of the Tibetan Plateau causing an upper atmospheric tropical easterly jet stream", "Weakening of the low pressure over the Thar desert", "Permanent high pressure over the Northern Plains during June", "Cooling of the equatorial Indian Ocean"],
        ["వేసవిలో టిబెట్ పీఠభూమి తీవ్రంగా వేడెక్కడం వల్ల ఎగువ వాతావరణంలో ఈస్టర్లీ జెట్ స్ట్రీమ్ ఏర్పడటం", "థార్ ఎడారిపై అల్పపీడనం బలహీనపడటం", "జూన్ నెలలో ఉత్తర మైదానాలపై శాశ్వత అధిక పీడనం", "భారత మహాసముద్రం చల్లబడటం"],
        0,
        "The intense heating of the Tibetan Plateau in summer acts as a thermal engine that creates an enormous low pressure cell and drives the tropical easterly jet stream, pulling moisture-laden SW monsoon winds into India.",
        "వేసవిలో టిబెట్ పీఠభూమి వేడెక్కడం వల్ల ఏర్పడే ఉష్ణ ప్రసరణ నైరుతి రుతుపవనాలను భారత భూభాగం వైపు లాగడంలో ప్రధాన చోదక శక్తిగా పనిచేస్తుంది."
    ))

    # Q155: Soils of Telangana & India
    qs.append(make_q(
        155, "Geography - Soils of India & Telangana",
        "Consider the following statements regarding soil distribution:\n\nStatement I: Black soils (Regur) possess high moisture retention capacity due to clay content and are ideal for cotton cultivation in northern and western Telangana.\nStatement II: Red soils (Chalka and Dubba) occupy the largest geographic area in Telangana state.\n\nWhich of the statements given above is/are correct?",
        "నేలల విస్తరణకు సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: నల్లరేగడి నేలలు (రెగూర్) అధిక తేమ నిల్వ సామర్థ్యాన్ని కలిగి ఉండి ఉత్తర, పశ్చిమ తెలంగాణలో పత్తి సాగుకు అత్యంత అనుకూలమైనవి.\nప్రకటన II: తెలంగాణ రాష్ట్రంలో ఎర్ర నేలలు (చల్కా మరియు దుబ్బ నేలలు) అత్యధిక విస్తీర్ణంలో విస్తరించి ఉన్నాయి.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are correct. Red soils cover over 48-50% of Telangana's total area (Chalka and Dubba), while Black soils cover around 25-28% primarily in Adilabad, Nizamabad, and Sangareddy districts.",
        "రెండు ప్రకటనలు సరైనవి. తెలంగాణలో అత్యధిక విస్తీర్ణంలో ఎర్ర నేలలు ఉన్నాయి మరియు నల్లరేగడి నేలలు పత్తి సాగుకు అనుకూలం."
    ))

    # Q156: Biosphere Reserves
    qs.append(make_q(
        156, "Environment - Protected Areas",
        "Which was the FIRST Biosphere Reserve established in India under the UNESCO Man and the Biosphere (MAB) programme in 1986?",
        "1986లో భారతదేశంలో మొట్టమొదటిసారిగా ఏర్పాటు చేయబడిన బయోస్పియర్ రిజర్వ్ ఏది?",
        ["Nanda Devi Biosphere Reserve", "Sundarbans Biosphere Reserve", "Nilgiri Biosphere Reserve", "Gulf of Mannar Biosphere Reserve"],
        ["నందా దేవి బయోస్పియర్ రిజర్వ్", "సుందర్బన్స్ బయోస్పియర్ రిజర్వ్", "నీలగిరి బయోస్పియర్ రిజర్వ్ (Nilgiri)", "మన్నార్ సింధుశాఖ బయోస్పియర్ రిజర్వ్"],
        2,
        "The Nilgiri Biosphere Reserve (spanning Tamil Nadu, Kerala, and Karnataka) was the first biosphere reserve established in India in 1986.",
        "1986లో తమిళనాడు, కేరళ, కర్ణాటక రాష్ట్రాల సరిహద్దుల్లో ఏర్పాటైన నీలగిరి భారతదేశపు మొట్టమొదటి బయోస్పియర్ రిజర్వ్."
    ))

    # Q157: Tiger Reserves of Telangana
    qs.append(make_q(
        157, "Environment - Wildlife Conservation in Telangana",
        "Consider the following statements regarding Tiger Reserves in Telangana:\n\nStatement I: Amrabad Tiger Reserve, located in the Nallamala hills, is the second-largest tiger reserve in India by core area.\nStatement II: Kawal Tiger Reserve is situated in the northern part of Telangana along the Godavari river basin in Mancherial, Nirmal, and Kumuram Bheem Asifabad districts.\n\nWhich of the statements given above is/are correct?",
        "తెలంగాణలోని పులుల సంరక్షణ కేంద్రాలకు (Tiger Reserves) సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: నల్లమల కొండలలో విస్తరించి ఉన్న అమ్రాబాద్ టైగర్ రిజర్వ్ కోర్ ఏరియా పరంగా భారతదేశంలో రెండవ అతిపెద్ద పులుల సంరక్షణ కేంద్రం.\nప్రకటన II: కవ్వాల్ టైగర్ రిజర్వ్ ఉత్తర తెలంగాణలోని మంచిర్యాల, నిర్మల్, కుమ్రం భీమ్ ఆసిఫాబాద్ జిల్లాల్లో గోదావరి పరీవాహక ప్రాంతంలో ఉంది.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are correct. Amrabad (in Nagarkurnool and Nalgonda) is the second largest tiger reserve in India, and Kawal (notified in 2012) is in northern Telangana.",
        "రెండు ప్రకటనలు సరైనవి. అమ్రాబాద్ దేశంలోనే రెండవ అతిపెద్ద టైగర్ రిజర్వ్ కాగా, కవ్వాల్ ఉత్తర తెలంగాణలోని జిల్లాల్లో విస్తరించి ఉంది."
    ))

    # Q158: Kaleshwaram Barrages
    qs.append(make_q(
        158, "Geography - Irrigation Infrastructure",
        "Under the Kaleshwaram Lift Irrigation Project (KLIP), which barrage is constructed at the confluence of the Godavari and Pranahita rivers near Medigadda?",
        "కాళేశ్వరం ఎత్తిపోతల ప్రాజెక్టులో భాగంగా గోదావరి మరియు ప్రాణహిత నదుల సంగమ ప్రాంతమైన మేడిగడ్డ వద్ద నిర్మించిన బ్యారేజ్ ఏది?",
        ["Sundilla (Parvati) Barrage", "Annaram (Saraswati) Barrage", "Medigadda (Lakshmi) Barrage", "Yellampalli Reservoir"],
        ["సుందిళ్ల (పార్వతి) బ్యారేజ్", "అన్నారం (సరస్వతి) బ్యారేజ్", "మేడిగడ్డ (లక్ష్మి) బ్యారేజ్", "ఎల్లంపల్లి రిజర్వాయర్"],
        2,
        "Medigadda Barrage (named Lakshmi Barrage) is the starting point of the KLIP, built on the Godavari just downstream of the confluence with the Pranahita river.",
        "ప్రాణహిత-గోదావరి సంగమ ప్రాంతంలో కాళేశ్వరం మొదటి బ్యారేజ్‌గా మేడిగడ్డ (లక్ష్మి) బ్యారేజ్‌ను నిర్మించారు."
    ))

    # Q159: Singareni Collieries Coal
    qs.append(make_q(
        159, "Geography - Mineral Resources of Telangana",
        "The coal deposits operated by the Singareni Collieries Company Limited (SCCL) in Telangana are geologically concentrated in which river valley belt?",
        "తెలంగాణలోని సింగరేణి కాలరీస్ కంపెనీ లిమిటెడ్ (SCCL) బొగ్గు నిల్వలు భౌగోళికంగా ఏ నదీ లోయ ప్రాంతంలో విస్తరించి ఉన్నాయి?",
        ["Krishna Valley Belt", "Pranahita-Godavari Valley Coalfield", "Tungabhadra Valley Belt", "Musi-Dindi Valley Belt"],
        ["కృష్ణా లోయ బెల్ట్", "ప్రాణహిత-గోదావరి లోయ బొగ్గు క్షేత్రం (Pranahita-Godavari Valley)", "తుంగభద్ర లోయ బెల్ట్", "మూసి-దిండి లోయ బెల్ట్"],
        1,
        "The Pranahita-Godavari Valley Coalfield in Telangana holds the only proven coal reserves in South India, stretching across Mancherial, Peddapalli, Bhadradri Kothagudem, and Jayashankar Bhupalpally.",
        "దక్షిణ భారతదేశంలో ఏకైక బొగ్గు క్షేత్రమైన ప్రాణహిత-గోదావరి లోయలో సింగరేణి బొగ్గు గనులు విస్తరించి ఉన్నాయి."
    ))

    # Q160: Ramsar Wetland Sites
    qs.append(make_q(
        160, "Environment - Wetland Conservation",
        "The Ramsar Convention on Wetlands of International Importance was signed in 1971 in the city of Ramsar, which is located in which country?",
        "అంతర్జాతీయ ప్రాముఖ్యత కలిగిన చిత్తడి నేలల పరిరక్షణ కోసం 1971లో రామ్‌సార్ ఒప్పందంపై సంతకాలు చేసిన 'రామ్‌సార్' నగరం ఏ దేశంలో ఉంది?",
        ["Egypt", "Iran", "Turkey", "Iraq"],
        ["ఈజిప్ట్", "ఇరాన్ (Iran)", "టర్కీ", "ఇరాక్"],
        1,
        "The Ramsar Convention was signed on February 2, 1971 in Ramsar, a city on the Caspian Sea in Iran. World Wetlands Day is celebrated on February 2.",
        "రామ్‌సార్ ఒప్పందం 1971 ఫిబ్రవరి 2న కాస్పియన్ సముద్ర తీరంలోని ఇరాన్ నగరం రామ్‌సార్‌లో కుదిరింది."
    ))

    # Q161: Forest Survey of India ISFR
    qs.append(make_q(
        161, "Environment - Forest Resources",
        "According to the India State of Forest Report (ISFR), which Indian State has the largest total forest cover in terms of area in square kilometres?",
        "భారత అటవీ సర్వే నివేదిక (ISFR) ప్రకారం, వైశాల్యం (చదరపు కిలోమీటర్లు) పరంగా భారతదేశంలో అత్యధిక అటవీ విస్తీర్ణం కలిగిన రాష్ట్రం ఏది?",
        ["Arunachal Pradesh", "Madhya Pradesh", "Chhattisgarh", "Odisha"],
        ["అరుణాచల్ ప్రదేశ్", "మధ్యప్రదేశ్ (Madhya Pradesh)", "ఛత్తీస్‌గఢ్", "ఒడిశా"],
        1,
        "Madhya Pradesh has the largest forest cover in the country by absolute area, followed by Arunachal Pradesh, Chhattisgarh, Odisha, and Maharashtra.",
        "అత్యధిక అటవీ విస్తీర్ణం కలిగిన రాష్ట్రం మధ్యప్రదేశ్. శాతం పరంగా మిజోరాం మొదటి స్థానంలో ఉంది."
    ))

    # Q162: El Niño & La Niña
    qs.append(make_q(
        162, "Geography - Climatology",
        "Consider the following statements regarding El Niño and its impact on Indian weather:\n\nStatement I: El Niño involves the abnormal warming of sea surface waters in the central and eastern equatorial Pacific Ocean.\nStatement II: In most years, strong El Niño events are associated with poor and deficient South-West monsoon rainfall and drought conditions in India.\n\nWhich of the statements given above is/are correct?",
        "ఎల్ నినో (El Niño) మరియు భారత వాతావరణంపై దాని ప్రభావానికి సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: ఎల్ నినో అనేది మధ్య మరియు తూర్పు భూమధ్యరేఖా పసిఫిక్ మహాసముద్ర ఉపరితల జలాలు అసాధారణంగా వేడెక్కే ప్రక్రియ.\nప్రకటన II: సాధారణంగా తీవ్రమైన ఎల్ నినో సంవత్సరాలలో భారతదేశంలో నైరుతి రుతుపవనాల వర్షపాతం క్షీణించి కరువు పరిస్థితులు ఏర్పడతాయి.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are correct. El Niño causes warmer central/eastern Pacific waters and is historically correlated with deficient SW monsoon rains in India, whereas La Niña brings favorable rainfall.",
        "రెండు ప్రకటనలు సరైనవి. ఎల్ నినో సమయంలో పసిఫిక్ జలాలు వేడెక్కి భారతదేశంలో నైరుతి రుతుపవన వర్షపాతం తగ్గుతుంది."
    ))

    # Q163: Coral Reefs in India
    qs.append(make_q(
        163, "Environment - Marine Ecosystems",
        "Which of the following regions in India does NOT possess major coral reef formations?",
        "భారతదేశంలోని కింది తీర ప్రాంతాలలో ప్రధాన పగడపు దిబ్బలు (Coral Reefs) లేని ప్రాంతం ఏది?",
        ["Gulf of Mannar", "Andaman and Nicobar Islands", "Lakshadweep Islands", "Sundarbans Delta"],
        ["మన్నార్ సింధుశాఖ", "అండమాన్ మరియు నికోబార్ దీవులు", "లక్షద్వీప్ దీవులు", "సుందర్బన్స్ డెల్టా (Sundarbans)"],
        3,
        "Sundarbans is a mangrove delta with massive freshwater discharge and muddy sediment, where corals cannot survive. Coral reefs in India are found in Lakshadweep, Gulf of Mannar, Andaman & Nicobar, and Gulf of Kutch.",
        "సుందర్బన్స్ మడ అడవుల ప్రాంతం కావున ఇక్కడ స్వచ్ఛమైన ఉప్పునీరు లేక పగడపు దిబ్బలు ఉండవు. లక్షద్వీప్, మన్నార్, అండమాన్లలో పగడపు దిబ్బలు ఉన్నాయి."
    ))

    # Q164: Global Treaties Montreal Protocol
    qs.append(make_q(
        164, "Environment - International Conventions",
        "The landmark 'Montreal Protocol' signed in 1987 is an international environmental treaty designed specifically to protect which component of the Earth's atmosphere?",
        "1987లో కుదిరిన చారిత్రాత్మక 'మాంట్రియల్ ప్రోటోకాల్' భూమి యొక్క వాతావరణంలోని ఏ భాగాన్ని రక్షించడానికి ఉద్దేశించిన అంతర్జాతీయ పర్యావరణ ఒప్పందం?",
        ["Stratospheric Ozone Layer", "Tropospheric Carbon Sink", "Marine Coral Formations", "Polar Ice Caps"],
        ["స్ట్రాటోస్ఫియర్ ఓజోన్ పొర (Ozone Layer)", "ట్రోపోస్ఫియర్ కార్బన్ సింక్", "సముద్ర పగడపు నిర్మాణాలు", "ధ్రువ మంచు పలకలు"],
        0,
        "The Montreal Protocol on Substances that Deplete the Ozone Layer phases out chlorofluorocarbons (CFCs) and halons to protect the stratospheric ozone layer.",
        "స్ట్రాటోస్ఫియర్‌లోని ఓజోన్ పొరను క్షీణింపజేసే క్లోరోఫ్లోరో కార్బన్‌ల (CFC) నియంత్రణ కోసం మాంట్రియల్ ప్రోటోకాల్ కుదిరింది."
    ))

    # =========================================================================
    # INDIAN & TELANGANA ECONOMY (165 - 174: 10 Questions)
    # =========================================================================

    # Q165: RBI Repo Rate
    qs.append(make_q(
        165, "Indian Economy - Monetary Policy",
        "In the operational framework of the Reserve Bank of India's monetary policy, what is the 'Repo Rate'?",
        "రిజర్వ్ బ్యాంక్ ఆఫ్ ఇండియా (RBI) ద్రవ్య విధానంలో 'రెపో రేటు' (Repo Rate) అంటే ఏమిటి?",
        ["The rate at which commercial banks park their surplus funds with the RBI", "The rate at which the RBI lends short-term liquidity to commercial banks against the collateral of government and other approved securities", "The rate at which commercial banks lend to their prime corporate borrowers", "The mandatory cash percentage banks maintain with the RBI"],
        ["వాణిజ్య బ్యాంకులు తమ మిగులు నిధులను ఆర్బీఐ వద్ద ఉంచే వడ్డీ రేటు", "ప్రభుత్వ సెక్యూరిటీల హామీపై వాణిజ్య బ్యాంకులకు ఆర్బీఐ స్వల్పకాలిక నిధులను అప్పుగా ఇచ్చే వడ్డీ రేటు", "వాణిజ్య బ్యాంకులు తమ కార్పొరేట్ కస్టమర్లకు ఇచ్చే రుణాల రేటు", "బ్యాంకులు ఆర్బీఐ వద్ద ఉంచాల్సిన తప్పనిసరి నగదు నిల్వ"],
        1,
        "The Repo Rate (Repurchase Option Rate) is the policy interest rate at which the RBI provides liquidity to commercial banks against the collateral of government securities under the Liquidity Adjustment Facility (LAF).",
        "ప్రభుత్వ సెక్యూరిటీలను తనఖా పెట్టుకుని వాణిజ్య బ్యాంకులకు ఆర్బీఐ రుణాలు ఇచ్చే రేటును రెపో రేటు అంటారు."
    ))

    # Q166: Money Supply M1 & M3
    qs.append(make_q(
        166, "Indian Economy - Money Supply Aggregates",
        "According to the Reserve Bank of India's classification of monetary aggregates, which of the following constitutes 'Broad Money' (M3)?",
        "ఆర్బీఐ ద్రవ్య కొలమానాల ప్రకారం 'విస్తృత ద్రవ్యం' (Broad Money - M3) లో ఏవి భాగమై ఉంటాయి?",
        ["Currency with public + Demand deposits with banks + Other deposits with RBI", "M1 + Time deposits with the banking system", "Currency with public + Post office savings deposits", "Total deposits with Post Office Savings Bank"],
        ["ప్రజల వద్ద ఉన్న నగదు + డిమాండ్ డిపాజిట్లు + ఆర్బీఐ వద్ద ఇతర డిపాజిట్లు", "M1 + బ్యాంకింగ్ వ్యవస్థలోని కాలపరిమితి డిపాజిట్లు (Time Deposits)", "ప్రజల వద్ద నగదు + పోస్టాఫీసు పొదుపు డిపాజిట్లు", "పోస్టాఫీసు పొదుపు బ్యాంకు మొత్తం డిపాజిట్లు"],
        1,
        "M1 is Narrow Money (Currency + Demand Deposits + Other deposits). Broad Money (M3) = M1 + Time Deposits with the banking system.",
        "M1 సంకుచిత ద్రవ్యం కాగా, M3 (విస్తృత ద్రవ్యం) = M1 + బ్యాంకులలోని ఫిక్స్‌డ్/టైమ్ డిపాజిట్లు."
    ))

    # Q167: Inflation Targeting CPI
    qs.append(make_q(
        167, "Indian Economy - Inflation Measurement",
        "Under the Flexible Inflation Targeting (FIT) framework established under the RBI Act, what is the headline inflation target mandated for the Monetary Policy Committee (MPC)?",
        "ఆర్బీఐ చట్టం కింద ద్రవ్య విధాన కమిటీకి (MPC) నిర్దేశించిన వినియోగదారుల ధరల సూచీ (CPI Combined) ఆధారిత అధికారిక ద్రవ్యోల్బణ లక్ష్యం ఎంత?",
        ["3% with a tolerance band of +/- 1%", "4% with a tolerance band of +/- 2% (i.e. between 2% and 6%)", "5% with a tolerance band of +/- 1%", "6% fixed rate without tolerance band"],
        ["3% (+/- 1% పరిమితి)", "4% (+/- 2% పరిమితి, అనగా 2% నుండి 6% మధ్య)", "5% (+/- 1% పరిమితి)", "ఖచ్చితంగా 6%"],
        1,
        "The statutory inflation target is 4% Consumer Price Index (CPI Combined) inflation with an upper tolerance limit of 6% and a lower tolerance limit of 2%.",
        "భారతదేశంలో అధికారిక ద్రవ్యోల్బణ లక్ష్యం 4% (గరిష్టంగా 6%, కనిష్టంగా 2%)."
    ))

    # Q168: Fiscal Deficit & FRBM Act
    qs.append(make_q(
        168, "Indian Economy - Public Finance & Fiscal Deficit",
        "Which of the following formulas correctly defines the 'Gross Fiscal Deficit' of the Government of India?",
        "భారత ప్రభుత్వ 'స్థూల ద్రవ్య లోటు'ను (Gross Fiscal Deficit) సరిగ్గా నిర్వచించే సూత్రం ఏది?",
        ["Total Expenditure - Total Receipts excluding borrowings", "Revenue Expenditure - Revenue Receipts", "Fiscal Deficit - Interest Payments", "Capital Expenditure - Capital Receipts"],
        ["మొత్తం వ్యయం - (రుణాలు మినహాయించిన మొత్తం రాబడులు)", "రెవెన్యూ వ్యయం - రెవెన్యూ రాబడులు", "ద్రవ్య లోటు - వడ్డీ చెల్లింపులు", "మూలధన వ్యయం - మూలధన రాబడులు"],
        0,
        "Fiscal Deficit = Total Expenditure - Total Non-Debt Receipts (Revenue Receipts + Recovery of Loans + Other Non-Debt Capital Receipts). It reflects total borrowing requirement of the government.",
        "ద్రవ్య లోటు = మొత్తం వ్యయం - రుణాలు మినహాయించిన మొత్తం రాబడులు. ఇది ప్రభుత్వం చేయాల్సిన మొత్తం అప్పులను సూచిస్తుంది."
    ))

    # Q169: GST Council Article 279A
    qs.append(make_q(
        169, "Indian Economy - Taxation & GST",
        "Consider the following statements regarding the Goods and Services Tax (GST) Council:\n\nStatement I: The GST Council is constituted by the President under Article 279A of the Constitution and is chaired by the Union Finance Minister.\nStatement II: Every decision of the GST Council requires a majority of not less than three-fourths (75%) of the weighted votes of the members present and voting.\n\nWhich of the statements given above is/are correct?",
        "వస్తు మరియు సేవల పన్ను (GST) మండలికి సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: ఆర్టికల్ 279A ప్రకారం రాష్ట్రపతి జీఎస్టీ కౌన్సిల్‌ను ఏర్పాటు చేస్తారు మరియు దీనికి కేంద్ర ఆర్థిక మంత్రి ఛైర్మన్‌గా ఉంటారు.\nప్రకటన II: జీఎస్టీ కౌన్సిల్ నిర్ణయాలు చెల్లుబాటు కావడానికి హాజరై ఓటు వేసిన సభ్యుల వెయిటెడ్ ఓట్లలో కనీసం 3/4 వంతు (75%) మెజారిటీ అవసరం.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are correct. Article 279A governs the GST Council. Decisions require a 75% weighted majority, where Central Government has 1/3rd voting weight and all State Governments combined have 2/3rd weight.",
        "రెండు ప్రకటనలు సరైనవి. ఆర్టికల్ 279A కింద జీఎస్టీ కౌన్సిల్ ఏర్పాటవుతుంది మరియు నిర్ణయాలకు 3/4 వంతు వెయిటెడ్ మెజారిటీ అవసరం."
    ))

    # Q170: Priority Sector Lending (PSL)
    qs.append(make_q(
        170, "Indian Economy - Banking & Priority Sector Lending",
        "What is the total Priority Sector Lending (PSL) target mandated by the Reserve Bank of India for domestic scheduled commercial banks (excluding RRBs and Small Finance Banks) as a percentage of Adjusted Net Bank Credit (ANBC)?",
        "షెడ్యూల్డ్ వాణిజ్య బ్యాంకులకు (RRBలు మరియు SFBలు మినహా) ఆర్బీఐ నిర్దేశించిన మొత్తం ప్రాధాన్యతా రంగ రుణాల (PSL) లక్ష్యం ఎంత శాతం?",
        ["25% of ANBC", "33% of ANBC", "40% of ANBC", "50% of ANBC"],
        ["ANBC లో 25%", "ANBC లో 33%", "ANBC లో 40%", "ANBC లో 50%"],
        2,
        "The overall PSL target for domestic scheduled commercial banks and foreign banks with 20 branches and above is 40% of Adjusted Net Bank Credit (ANBC) or Credit Equivalent Amount of Off-Balance Sheet Exposure.",
        "వాణిజ్య బ్యాంకులకు ప్రాధాన్యతా రంగ రుణాల లక్ష్యం 40% (వ్యవసాయం, ఎంఎస్ఎంఈ, బలహీన వర్గాలు మొదలైనవి)."
    ))

    # Q171: NITI Aayog Multidimensional Poverty Index
    qs.append(make_q(
        171, "Indian Economy - NITI Aayog & Poverty",
        "The National Multidimensional Poverty Index (MPI) published by NITI Aayog evaluates deprivations across how many dimensions and indicators?",
        "నీతి ఆయోగ్ విడుదల చేసే జాతీయ బహుమితీయ పేదరిక సూచిక (National MPI) ఎన్ని రంగాలు (Dimensions) మరియు సూచికల (Indicators) ఆధారంగా పేదరికాన్ని లెక్కిస్తుంది?",
        ["3 Dimensions and 12 Indicators", "4 Dimensions and 10 Indicators", "3 Dimensions and 10 Indicators", "5 Dimensions and 15 Indicators"],
        ["3 రంగాలు మరియు 12 సూచికలు", "4 రంగాలు మరియు 10 సూచికలు", "3 రంగాలు మరియు 10 సూచికలు", "5 రంగాలు మరియు 15 సూచికలు"],
        0,
        "NITI Aayog's National MPI uses the Oxford OPHI methodology comprising 3 equally weighted dimensions: Health, Education, and Standard of Living, represented by 12 specific indicators (including maternal health and bank accounts).",
        "నీతి ఆయోగ్ MPI లో ఆరోగ్యం, విద్య, జీవన ప్రమాణాలు అనే 3 సమాన రంగాలు మరియు 12 సూచికలు ఉంటాయి."
    ))

    # Q172: Telangana GSDP Services Sector
    qs.append(make_q(
        172, "Telangana Economy - Sectoral Growth",
        "According to the Telangana Socio-Economic Outlook, which sector of the economy contributes the largest share (over 60%) to the Gross State Domestic Product (GSDP) of Telangana?",
        "తెలంగాణ సామాజిక ఆర్థిక సర్వే ప్రకారం, తెలంగాణ స్థూల రాష్ట్ర దేశీయోత్పత్తికి (GSDP) అత్యధిక వాటాను (60% పైగా) అందిస్తున్న రంగం ఏది?",
        ["Agriculture and Allied Sector", "Industrial & Manufacturing Sector", "Services Sector (IT, Financial & Real Estate)", "Mining and Quarrying Sector"],
        ["వ్యవసాయ మరియు అనుబంధ రంగాలు", "పారిశ్రామిక మరియు తయారీ రంగం", "సేవా రంగం (ఐటీ, ఆర్థిక మరియు రియల్ ఎస్టేట్)", "గనుల రంగం"],
        2,
        "The Services sector (driven by Hyderabad's IT/ITeS hub, financial services, transport, and trade) contributes over 62-64% of Telangana's Gross State Value Added (GSVA).",
        "తెలంగాణ జీఎస్‌డీపీలో 60% పైగా వాటా ఐటీ, వాణిజ్యం మరియు ఫైనాన్స్ ఆధారిత సేవా రంగానిదే."
    ))

    # Q173: Telangana Industrial Policy TS-iPASS
    qs.append(make_q(
        173, "Telangana Economy - Industrial Policy",
        "What unique feature was introduced by the Telangana Government under the 'TS-iPASS' (Telangana State Industrial Project Approval and Self-Certification System) Act, 2014 to attract global investments?",
        "తెలంగాణ ప్రభుత్వం 2014లో ప్రవేశపెట్టిన 'TS-iPASS' చట్టంలో దేశంలోనే మొదటిసారిగా ప్రవేశపెట్టిన వినూత్న నిబంధన ఏది?",
        ["Conferring a statutory right to timely clearances, failing which deemed approval is granted within 1 to 30 days", "Complete exemption from paying electricity bills for 10 years", "Mandatory recruitment of 100% local workers in all private firms", "Zero tax regime on all capital imports indefinitely"],
        ["సకాలంలో అనుమతులు పొందే చట్టబద్ధమైన హక్కును కల్పించడం, గడువులోగా రాకపోతే 1 నుండి 30 రోజుల్లో ఆటోమేటిక్ డీమ్డ్ అప్రూవల్ లభించడం", "10 ఏళ్లపాటు విద్యుత్ బిల్లుల నుండి పూర్తి మినహాయింపు", "ప్రైవేట్ సంస్థల్లో 100% స్థానికులనే నియమించుకోవాలనే నిబంధన", "మూలధన దిగుమతులపై పన్నులు పూర్తిగా రద్దు"],
        0,
        "TS-iPASS is India's first industrial clearance system that confers a 'Right to Clearances' by law, providing self-certification and deemed approvals if clearances are not issued within 15 to 30 days.",
        "TS-iPASS చట్టం ద్వారా పరిశ్రమల స్థాపనకు నిర్ణీత సమయంలోగా అనుమతులు పొందే చట్టబద్ధ హక్కును కల్పించారు (డీమ్డ్ అప్రూవల్)."
    ))

    # Q174: Balance of Payments CAD
    qs.append(make_q(
        174, "Indian Economy - External Sector",
        "The Current Account Deficit (CAD) in India's Balance of Payments occurs when which of the following conditions is met?",
        "భారతదేశ విదేశీ చెల్లింపుల సమతుల్యతలో (Balance of Payments) కరెంట్ ఖాతా లోటు (CAD) ఎప్పుడు ఏర్పడుతుంది?",
        ["The total value of imported goods and services exceeds the value of exported goods and services plus net primary and secondary transfers", "Foreign exchange reserves of RBI decline below 100 billion dollars", "Capital inflows through FDI exceed foreign institutional investment", "Fiscal deficit of the central government exceeds 5% of GDP"],
        ["దిగుమతి చేసుకున్న వస్తువులు, సేవల విలువ ఎగుమతులు మరియు నికర బదిలీల కంటే ఎక్కువగా ఉన్నప్పుడు", "ఆర్బీఐ వద్ద విదేశీ మారక నిల్వలు 100 బిలియన్ డాలర్ల కంటే తగ్గితే", "విదేశీ ప్రత్యక్ష పెట్టుబడులు ఎఫ్‌ఐఐ కంటే పెరిగితే", "కేంద్ర ద్రవ్య లోటు 5% మించితే"],
        0,
        "Current Account Deficit (CAD) occurs when a country's total imports of goods, services, and transfers exceed its total exports of goods, services, and transfers.",
        "వస్తువులు మరియు సేవల దిగుమతుల విలువ, ఎగుమతుల కంటే ఎక్కువగా ఉన్నప్పుడు కరెంట్ ఖాతా లోటు ఏర్పడుతుంది."
    ))

    # =========================================================================
    # GENERAL SCIENCE & TECHNOLOGY (175 - 188: 14 Questions)
    # =========================================================================

    # Q175: Physics - Total Internal Reflection
    qs.append(make_q(
        175, "General Science - Physics & Optics",
        "Which of the following optical phenomena is based on the principle of 'Total Internal Reflection' (TIR)?",
        "కింది దృగ్విషయాలలో 'సంపూర్ణ అంతర్గత పరావర్తనం' (Total Internal Reflection) సూత్రం ఆధారంగా పనిచేసేది ఏది?",
        ["Transmission of light through optical fiber cables", "Splitting of white light by a glass prism into a spectrum", "Blue color of the clear sky during daytime", "Formation of shadow behind an opaque object"],
        ["ఆప్టికల్ ఫైబర్ కేబుల్స్ ద్వారా కాంతి సంకేతాల ప్రసారం", "గాజు ప్రిజం ద్వారా కాంతి విక్షేపణం చెందడం", "పగటిపూట ఆకాశం నీలిరంగులో కనిపించడం", "అపారదర్శక వస్తువుల వెనుక నీడ ఏర్పడటం"],
        0,
        "Optical fibers transmit light signals over long distances with minimal loss using Total Internal Reflection (TIR), where light travels from core (denser) to cladding (rarer) at an angle greater than the critical angle.",
        "ఆప్టికల్ ఫైబర్లలో కాంతి ప్రసారం సంపూర్ణ అంతర్గత పరావర్తనం (TIR) సూత్రం ఆధారంగా జరుగుతుంది."
    ))

    # Q176: Physics - Power of a Lens
    qs.append(make_q(
        176, "General Science - Physics",
        "A person wearing corrective eyeglasses is prescribed a lens with a power of -2.5 Dioptres. What type of lens is this, and which vision defect does it correct?",
        "ఒక వ్యక్తికి కంటి వైద్యుడు -2.5 డయాప్టర్ల సామర్థ్యం గల లెన్స్‌ను సూచించారు. ఇది ఏ రకమైన కటకం మరియు ఏ దృష్టి లోపాన్ని సరిచేస్తుంది?",
        ["Convex lens to correct Hypermetropia (farsightedness)", "Concave lens to correct Myopia (nearsightedness)", "Cylindrical lens to correct Astigmatism", "Bifocal lens to correct Presbyopia"],
        ["హైపర్‌మెట్రోపియా (దూరదృష్టి) ను సరిచేసే కుంభాకార కటకం", "మయోపియా (హ్రస్వదృష్టి / దగ్గరి చూపు మాత్రమే కనిపించడం) ను సరిచేసే పుటాకార కటకం", "సిలిండ్రికల్ కటకం", "బైఫోకల్ కటకం"],
        1,
        "Negative lens power (-D) indicates a diverging Concave lens, which is used to correct Myopia (nearsightedness). Positive lens power indicates a Convex lens used for Hypermetropia.",
        "ఋణ విలువ (-D) పుటాకార కటకాన్ని (Concave lens) సూచిస్తుంది, దీనిని హ్రస్వదృష్టి (Myopia) నివారణకు ఉపయోగిస్తారు."
    ))

    # Q177: Physics - Doppler Effect
    qs.append(make_q(
        177, "General Science - Physics & Sound Waves",
        "The apparent change in the frequency or pitch of sound heard by an observer when a police patrol siren approaches and then recedes is known as what physical effect?",
        "పోలీస్ సైరన్ వాహనం ఒక వ్యక్తిని సమీపిస్తున్నప్పుడు మరియు దాటి వెళ్తున్నప్పుడు వినబడే ధ్వని పిచ్ లేదా పౌనఃపున్యంలో వచ్చే మార్పును ఏ భౌతిక ప్రభావం అంటారు?",
        ["Raman Effect", "Doppler Effect", "Tyndall Effect", "Photoelectric Effect"],
        ["రామన్ ప్రభావం", "డాప్లర్ ప్రభావం (Doppler Effect)", "టిండాల్ ప్రభావం", "కాంతి విద్యుత్ ప్రభావం"],
        1,
        "The Doppler Effect is the change in frequency of a wave in relation to an observer who is moving relative to the wave source.",
        "ధ్వని జనకం మరియు పరిశీలకుడి మధ్య సాపేక్ష చలనం వల్ల పౌనఃపున్యంలో కలిగే మార్పును 'డాప్లర్ ప్రభావం' అంటారు."
    ))

    # Q178: Physics - Electromagnetic Induction
    qs.append(make_q(
        178, "General Science - Physics & Electricity",
        "The generation of an electromotive force (EMF) across an electrical conductor in a changing magnetic field is governed by which fundamental law, utilized in electric power generators and transformers?",
        "మారుతున్న అయస్కాంత క్షేత్రంలో విద్యుద్వాహక బలం (EMF) ప్రేరేపించబడే సూత్రాన్ని తెలిపే మరియు విద్యుత్ జనరేటర్లు, ట్రాన్స్‌ఫార్మర్లలో ఉపయోగించే నియమం ఏది?",
        ["Ohm's Law", "Faraday's Law of Electromagnetic Induction", "Coulomb's Law", "Joule's Law of Heating"],
        ["ఓమ్ నియమం", "ఫారడే విద్యుదయస్కాంత ప్రేరణ నియమం (Faraday's Law)", "కూలుంబ్ నియమం", "జౌల్ ఉష్ణ నియమం"],
        1,
        "Faraday's Law of Electromagnetic Induction states that the induced EMF in a closed circuit is equal to the negative rate of change of magnetic flux through the circuit.",
        "ఫారడే విద్యుదయస్కాంత ప్రేరణ సూత్రం ప్రకారం జనరేటర్లలో విద్యుత్ ఉత్పత్తి జరుగుతుంది."
    ))

    # Q179: Chemistry - pH Scale
    qs.append(make_q(
        179, "General Science - Chemistry",
        "The normal pH of healthy human blood is strictly maintained within which of the following narrow ranges?",
        "ఆరోగ్యకరమైన మానవ రక్తం యొక్క సాధారణ pH విలువ ఏ పరిధిలో స్థిరంగా ఉంటుంది?",
        ["5.5 to 6.2", "6.8 to 7.0", "7.35 to 7.45", "8.2 to 8.8"],
        ["5.5 నుండి 6.2", "6.8 నుండి 7.0", "7.35 నుండి 7.45", "8.2 నుండి 8.8"],
        2,
        "Human arterial blood pH is tightly regulated by bicarbonate and phosphate buffer systems between 7.35 and 7.45 (slightly alkaline). Acidosis occurs below 7.35 and alkalosis above 7.45.",
        "మానవ రక్తం కొద్దిగా క్షార స్వభావం కలిగి 7.35 నుండి 7.45 pH పరిధిలో ఉంటుంది."
    ))

    # Q180: Chemistry - Allotropes of Carbon
    qs.append(make_q(
        180, "General Science - Chemistry Materials",
        "Consider the following statements regarding the allotropes of carbon:\n\nStatement I: Diamond is an electrical insulator because all four valence electrons of each carbon atom form sp3 hybridized covalent bonds with no free delocalized electrons.\nStatement II: Graphite is a good conductor of electricity along its sheets because each carbon atom is bonded to three others, leaving one delocalized electron per carbon atom.\n\nWhich of the statements given above is/are correct?",
        "కార్బన్ రూపాంతరాలకు సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: వజ్రంలో ప్రతి కార్బన్ పరమాణువు 4 sp3 సంకరీకరణ సమయోజనీయ బంధాలను కలిగి ఉండి స్వేచ్ఛా ఎలక్ట్రాన్లు లేనందున ఇది విద్యుత్ బంధకంగా పనిచేస్తుంది.\nప్రకటన II: గ్రాఫైట్‌లో ప్రతి కార్బన్ 3 ఇతర పరమాణువులతో మాత్రమే బంధాన్ని ఏర్పరచుకుని స్వేచ్ఛా ఎలక్ట్రాన్‌ను కలిగి ఉండటం వల్ల ఇది మంచి విద్యుత్ వాహకం.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are correct chemical facts. Diamond's 3D tetrahedral sp3 lattice has zero free electrons (insulator), while graphite's 2D planar sp2 sheets have mobile pi electrons (conductor).",
        "రెండు ప్రకటనలు సరైనవి. వజ్రం విద్యుత్ బంధకం కాగా, గ్రాఫైట్ మంచి విద్యుత్ వాహకం."
    ))

    # Q181: Chemistry - Everyday Compounds
    qs.append(make_q(
        181, "General Science - Applied Chemistry",
        "Match List-I (Common Name) with List-II (Chemical Formula):\n\nList-I\t\t\tList-II\nA. Baking Soda\t\t1. Na2CO3 . 10H2O\nB. Washing Soda\t\t2. NaHCO3\nC. Bleaching Powder\t3. CaSO4 . 1/2 H2O\nD. Plaster of Paris\t4. CaOCl2\n\nChoose the correct code:",
        "జాబితా-I (సాధారణ పేరు) ను జాబితా-II (రసాయన ఫార్ములా) తో జతపరచండి:\n\nజాబితా-I\t\t\tజాబితా-II\nA. బేకింగ్ సోడా\t\t1. Na2CO3 . 10H2O\nB. వాషింగ్ సోడా\t\t2. NaHCO3\nC. బ్లీచింగ్ పౌడర్\t4. CaOCl2\nD. ప్లాస్టర్ ఆఫ్ పారిస్\t3. CaSO4 . 1/2 H2O\n\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-2, B-1, C-4, D-3", "A-2, B-1, C-3, D-4", "A-1, B-2, C-4, D-3", "A-4, B-1, C-2, D-3"],
        ["A-2, B-1, C-4, D-3", "A-2, B-1, C-3, D-4", "A-1, B-2, C-4, D-3", "A-4, B-1, C-2, D-3"],
        0,
        "Baking Soda = Sodium Hydrogen Carbonate NaHCO3 (A-2). Washing Soda = Sodium Carbonate Decahydrate Na2CO3.10H2O (B-1). Bleaching Powder = Calcium Hypochlorite CaOCl2 (C-4). Plaster of Paris = Calcium Sulphate Hemihydrate CaSO4.1/2H2O (D-3). Code: A-2, B-1, C-4, D-3.",
        "బేకింగ్ సోడా (A-2), వాషింగ్ సోడా (B-1), బ్లీచింగ్ పౌడర్ (C-4), ప్లాస్టర్ ఆఫ్ పారిస్ (D-3). సరైన కోడ్: A-2, B-1, C-4, D-3."
    ))

    # Q182: Biology - Endocrine System
    qs.append(make_q(
        182, "General Science - Human Physiology",
        "Insulin, the crucial peptide hormone responsible for regulating glucose levels in the bloodstream, is synthesized and secreted by which specific cells of the Pancreas?",
        "రక్తంలో గ్లూకోజ్ స్థాయిలను నియంత్రించే ముఖ్యమైన హార్మోన్ 'ఇన్సులిన్' క్లోమ గ్రంథిలోని (Pancreas) ఏ నిర్దిష్ట కణాల ద్వారా స్రవించబడుతుంది?",
        ["Alpha cells of Islets of Langerhans", "Beta cells of Islets of Langerhans", "Delta cells of Islets of Langerhans", "Acinar cells"],
        ["లాంగర్‌హాన్స్ పుటికలలోని ఆల్ఫా కణాలు", "లాంగర్‌హాన్స్ పుటికలలోని బీటా కణాలు (Beta cells)", "డెల్టా కణాలు", "ఎసినార్ కణాలు"],
        1,
        "Beta cells of the Islets of Langerhans in the pancreas secrete insulin, whereas Alpha cells secrete glucagon.",
        "క్లోమములోని లాంగర్‌హాన్స్ పుటికల బీటా కణాలు ఇన్సులిన్‌ను స్రవిస్తాయి."
    ))

    # Q183: Biology - Vitamins & Deficiencies
    qs.append(make_q(
        183, "General Science - Nutrition & Health",
        "Pernicious Anemia, characterized by impaired red blood cell maturation and neurological symptoms, is caused by the chronic deficiency of which vitamin?",
        "ఎర్ర రక్త కణాల లోపం మరియు నరాల బలహీనతకు కారణమయ్యే 'పెర్నీషియస్ అనీమియా' ఏ విటమిన్ లోపం వల్ల వస్తుంది?",
        ["Vitamin B1 (Thiamine)", "Vitamin B6 (Pyridoxine)", "Vitamin B12 (Cyanocobalamin)", "Vitamin C (Ascorbic Acid)"],
        ["విటమిన్ B1 (థయామిన్)", "విటమిన్ B6 (పైరిడాక్సిన్)", "విటమిన్ B12 (సయనోకోబాలమిన్)", "విటమిన్ C (ఆస్కార్బిక్ యాసిడ్)"],
        2,
        "Vitamin B12 (Cyanocobalamin) deficiency or lack of intrinsic factor causes Pernicious Anemia.",
        "విటమిన్ B12 (సయనోకోబాలమిన్) లోపం వల్ల పెర్నీషియస్ అనీమియా వస్తుంది."
    ))

    # Q184: Biotechnology - CRISPR Cas9
    qs.append(make_q(
        184, "General Science - Emerging Biotechnology",
        "The revolutionary gene-editing technology 'CRISPR-Cas9' functions primarily as what in genetic engineering?",
        "శాస్త్ర రంగంలో విప్లవాత్మక మార్పులు తెచ్చిన 'CRISPR-Cas9' సాంకేతికత జన్యు ఇంజనీరింగ్‌లో ప్రాథమికంగా ఏ విధంగా పనిచేస్తుంది?",
        ["A viral vector for delivering artificial chromosomes", "A molecular pair of scissors that cuts double-stranded DNA at precise targeted sequences guided by an RNA molecule", "An artificial enzyme that converts RNA directly into protein", "A biological dye for fluorescent chromosome staining"],
        ["కృత్రిమ క్రోమోజోమ్‌లను చేర్చే వైరల్ వాహకం", "గైడ్ ఆర్‌ఎన్‌ఏ మార్గదర్శకత్వంలో డీఎన్‌ఏను కావలసిన ఖచ్చితమైన స్థానంలో కత్తిరించే పరమాణు కత్తెర (Molecular Scissors)", "ఆర్‌ఎన్‌ఏను ప్రోటీన్‌గా మార్చే కృత్రిమ ఎంజైమ్", "క్రోమోజోమ్‌లకు రంగులద్దే డై"],
        1,
        "CRISPR-Cas9 operates as molecular scissors guided by a single-guide RNA (sgRNA) to cut specific double-stranded DNA target sequences, enabling precise genome editing (awarded 2020 Nobel Prize in Chemistry to Emmanuelle Charpentier and Jennifer Doudna).",
        "CRISPR-Cas9 అనేది గైడ్ ఆర్‌ఎన్‌ఏ సహాయంతో డీఎన్‌ఏను ఖచ్చితంగా కత్తిరించే మాలిక్యులర్ సిజర్."
    ))

    # Q185: Vaccines Classification
    qs.append(make_q(
        185, "General Science - Immunology & Vaccines",
        "Consider the following pairings of COVID-19 vaccines and their scientific technology platforms:\n\nStatement I: Covaxin (developed by Bharat Biotech) is a whole-virion inactivated SARS-CoV-2 vaccine.\nStatement II: Covishield (developed by Oxford/AstraZeneca and produced by Serum Institute) is a chimpanzee adenovirus viral vector vaccine.\n\nWhich of the statements given above is/are correct?",
        "టీకాల సాంకేతికతకు సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: భారత్ బయోటెక్ అభివృద్ధి చేసిన 'కోవాగ్జిన్' అనేది నిర్వీర్యం చేయబడిన పూర్తి వైరస్ (Inactivated whole-virion) వ్యాక్సిన్.\nప్రకటన II: సీరమ్ ఇన్స్టిట్యూట్ తయారుచేసిన 'కోవిషీల్డ్' అనేది చింపాంజీ అడెనోవైరస్ వెక్టార్ ఆధారిత వ్యాక్సిన్.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are correct. Covaxin uses an inactivated virus platform, and Covishield uses the ChAdOx1 chimpanzee adenovirus recombinant vector.",
        "రెండు ప్రకటనలు సరైనవి. కోవాగ్జిన్ ఇనాక్టివేటెడ్ వ్యాక్సిన్ కాగా, కోవిషీల్డ్ అడెనోవైరస్ వెక్టార్ వ్యాక్సిన్."
    ))

    # Q186: ISRO Aditya-L1
    qs.append(make_q(
        186, "Science & Technology - ISRO Space Missions",
        "India's dedicated solar observatory spacecraft 'Aditya-L1', launched by ISRO in September 2023, was successfully placed into a halo orbit around which point located approximately 1.5 million km from Earth?",
        "ఇస్రో ప్రయోగించిన భారతదేశపు మొట్టమొదటి సౌర పరిశోధన నౌక 'ఆదిత్య-ఎల్1' భూమి నుండి దాదాపు 15 లక్షల కిలోమీటర్ల దూరంలో ఉన్న ఏ బిందువు వద్ద హాలో కక్ష్యలో విజయవంతంగా ప్రవేశపెట్టబడింది?",
        ["Sun-Earth Lagrange Point 1 (L1)", "Sun-Earth Lagrange Point 2 (L2)", "Earth-Moon Lagrange Point 1", "Geostationary Transfer Orbit"],
        ["సూర్య-భూమి లెగ్రాంజ్ పాయింట్ 1 (L1)", "సూర్య-భూమి లెగ్రాంజ్ పాయింట్ 2 (L2)", "భూమి-చంద్రుని లెగ్రాంజ్ పాయింట్ 1", "భూస్థిర కక్ష్య"],
        0,
        "Aditya-L1 was inserted into a halo orbit around Sun-Earth Lagrange Point 1 (L1), providing an uninterrupted view of the Sun without eclipses.",
        "ఆదిత్య-ఎల్1 నౌక సూర్యుడిని నిరంతరం పరిశీలించడానికి సూర్య-భూమి లెగ్రాంజ్ పాయింట్ 1 (L1) వద్ద స్థిరపడింది."
    ))

    # Q187: Chandrayaan-3 Shiv Shakti Point
    qs.append(make_q(
        187, "Science & Technology - Moon Exploration",
        "On August 23, 2023, India's Chandrayaan-3 lander Vikram made history by soft-landing on the Moon. What name was officially designated for this lunar landing site?",
        "2023 ఆగస్టు 23న చంద్రయాన్-3 ల్యాండర్ విక్రమ్ చంద్రుని దక్షిణ ధ్రువ ప్రాంతంలో విజయవంతంగా దిగిన ప్రదేశానికి అధికారికంగా ఏ పేరు పెట్టారు?",
        ["Tiranga Point", "Shiv Shakti Point", "Atal Point", "Jawahar Point"],
        ["తిరంగా పాయింట్", "శివ శక్తి పాయింట్ (Shiv Shakti Point)", "అటల్ పాయింట్", "జవహర్ పాయింట్"],
        1,
        "The landing site of Chandrayaan-3 was named 'Shiv Shakti Point' by Prime Minister Narendra Modi, while the Chandrayaan-2 crash site was named 'Tiranga Point'. August 23 was declared National Space Day.",
        "చంద్రయాన్-3 దిగిన ప్రదేశానికి 'శివ శక్తి పాయింట్' అని పేరు పెట్టారు మరియు ఆగస్టు 23ను జాతీయ అంతరిక్ష దినోత్సవంగా ప్రకటించారు."
    ))

    # Q188: Gaganyaan Human Spaceflight
    qs.append(make_q(
        188, "Science & Technology - Human Spaceflight",
        "Under ISRO's prestigious 'Gaganyaan' human spaceflight mission, what is the name of the female-looking humanoid robot developed to test life support systems in uncrewed test flights?",
        "ఇస్రో ప్రతిష్టాత్మక 'గగన్‌యాన్' మానవ సహిత అంతరిక్ష యాత్రకు ముందు మానవ రహిత ప్రయోగాలలో లైఫ్ సపోర్ట్ వ్యవస్థలను పరీక్షించడానికి రూపొందించిన మహిళా రోబోట్ (హ్యూమనాయిడ్) పేరు ఏమిటి?",
        ["Vyommitra", "Mitra", "Pragyan", "Rashmi"],
        ["వ్యోమమిత్ర (Vyommitra)", "మిత్ర", "ప్రజ్ఞాన్", "రష్మి"],
        0,
        "Vyommitra ('space friend') is the female-looking humanoid robot engineered by ISRO to monitor microgravity parameters and life-support modules in uncrewed Gaganyaan flights.",
        "గగన్‌యాన్ మానవరహిత పరీక్షల కోసం ఇస్రో రూపొందించిన హ్యూమనాయిడ్ రోబోట్ పేరు 'వ్యోమమిత్ర'."
    ))

    # =========================================================================
    # CURRENT AFFAIRS & INTERNATIONAL ORGANIZATIONS (189 - 200: 12 Questions)
    # =========================================================================

    # Q189: 16th BRICS Summit Kazan Expansion
    qs.append(make_q(
        189, "Current Affairs - International Organizations",
        "The 16th BRICS Summit was held in October 2024 under the theme 'Strengthening Multilateralism for Just Global Development and Security'. In which Russian city was this landmark summit held, marking the official participation of newly inducted member states?",
        "2024 అక్టోబర్‌లో కొత్త సభ్య దేశాల అధికారిక భాగస్వామ్యంతో 16వ బ్రిక్స్ (BRICS) శిఖరాగ్ర సదస్సు రష్యాలోని ఏ నగరంలో జరిగింది?",
        ["Moscow", "Saint Petersburg", "Kazan", "Sochi"],
        ["మాస్కో", "సెయింట్ పీటర్స్‌బర్గ్", "కజాన్ (Kazan)", "సోచి"],
        2,
        "The 16th BRICS Summit was held in Kazan, Russia in October 2024, hosting leaders from founding members along with new members including Egypt, Ethiopia, Iran, and the UAE.",
        "16వ బ్రిక్స్ సదస్సు రష్యాలోని కజాన్ నగరంలో జరిగింది. ఇందులో ఈజిప్ట్, ఇథియోపియా, ఇరాన్, యూఏఈ లు కొత్త సభ్యులుగా పాల్గొన్నాయి."
    ))

    # Q190: SCO Summit Islamabad 2024
    qs.append(make_q(
        190, "Current Affairs - International Organizations",
        "Which neighbouring capital city hosted the 23rd Council of Heads of Government of the Shanghai Cooperation Organisation (SCO) in October 2024, which was attended by India's External Affairs Minister Dr. S. Jaishankar?",
        "భారత విదేశాంగ మంత్రి డాక్టర్ ఎస్. జైశంకర్ హాజరైన షాంఘై సహకార సంస్థ (SCO) ప్రభుత్వ అధినేతల మండలి 23వ సదస్సును అక్టోబర్ 2024లో ఏ రాజధాని నగరం నిర్వహించింది?",
        ["Tashkent, Uzbekistan", "Islamabad, Pakistan", "Bishkek, Kyrgyzstan", "Astana, Kazakhstan"],
        ["తాష్కెంట్ (ఉజ్బెకిస్తాన్)", "ఇస్లామాబాద్ (పాకిస్తాన్)", "బిష్కెక్ (కిర్గిజ్స్తాన్)", "అస్తానా (కజకిస్తాన్)"],
        1,
        "The 23rd meeting of the SCO Council of Heads of Government was held on October 15-16, 2024 in Islamabad, Pakistan.",
        "SCO ప్రభుత్వ అధినేతల 23వ సదస్సు 2024 అక్టోబర్‌లో పాకిస్తాన్‌లోని ఇస్లామాబాద్‌లో జరిగింది."
    ))

    # Q191: ASEAN Summit Vientiane 2024
    qs.append(make_q(
        191, "Current Affairs - Regional Summits",
        "The 44th and 45th ASEAN Summits and the 21st ASEAN-India Summit held in October 2024 were hosted by which Southeast Asian country under the theme 'Enhancing Connectivity and Resilience'?",
        "2024 అక్టోబర్‌లో 44వ మరియు 45వ ఆసియాన్ (ASEAN) శిఖరాగ్ర సదస్సులు మరియు ఆసియాన్-ఇండియా సదస్సును ఏ ఆగ్నేయాసియా దేశం నిర్వహించింది?",
        ["Jakarta, Indonesia", "Vientiane, Laos", "Phnom Penh, Cambodia", "Hanoi, Vietnam"],
        ["జకార్తా (ఇండోనేషియా)", "వియంటియాన్ (లావోస్ - Laos)", "ప్నామ్ పెన్ (కంబోడియా)", "హనోయ్ (వియత్నాం)"],
        1,
        "Laos held the 2024 ASEAN Chairmanship and hosted the summits in its capital, Vientiane.",
        "2024 ఆసియాన్ సదస్సులకు లావోస్ రాజధాని వియంటియాన్ ఆతిథ్యమిచ్చింది."
    ))

    # Q192: G20 Rio Brazil & Handover
    qs.append(make_q(
        192, "Current Affairs - G20 Summit",
        "The 19th G20 Leaders' Summit in November 2024 was hosted in Rio de Janeiro under the presidency of Brazil. At the conclusion of this summit, the G20 presidency for the year 2025 was officially handed over to which country?",
        "నవంబర్ 2024లో బ్రెజిల్‌లోని రియో డి జనీరోలో 19వ జీ20 (G20) శిఖరాగ్ర సదస్సు జరిగింది. ఈ సదస్సు ముగింపులో 2025 సంవత్సరానికి జీ20 అధ్యక్ష బాధ్యతలను ఏ దేశానికి అప్పగించారు?",
        ["South Africa", "Australia", "Saudi Arabia", "South Korea"],
        ["దక్షిణాఫ్రికా (South Africa)", "ఆస్ట్రేలియా", "సౌదీ అరేబియా", "దక్షిణ కొరియా"],
        0,
        "President Lula da Silva of Brazil handed over the G20 gavel to President Cyril Ramaphosa of South Africa for the 2025 presidency.",
        "బ్రెజిల్ అధ్యక్షుడు లూలా డా సిల్వా 2025 జీ20 అధ్యక్ష బాధ్యతలను దక్షిణాఫ్రికాకు అప్పగించారు."
    ))

    # Q193: QUAD Summit Delaware
    qs.append(make_q(
        193, "Current Affairs - International Summits",
        "The fourth in-person Quad Leaders' Summit in September 2024 was hosted by US President Joe Biden in his hometown of Wilmington, Delaware. Which major health initiative was launched by Quad leaders at this summit?",
        "సెప్టెంబర్ 2024లో అమెరికాలోని డెలావేర్‌లో జరిగిన క్వాడ్ (QUAD) దేశాల నాయకుల సదస్సులో ఇండో-పసిఫిక్ ప్రాంతంలో గర్భాశయ క్యాన్సర్‌ను ఎదుర్కోవడానికి ప్రారంభించిన ప్రధాన కార్యక్రమం ఏది?",
        ["Quad Cancer Moonshot", "Quad Vaccine Initiative 2.0", "Indo-Pacific Malaria Eradication", "Quad Health Security Shield"],
        ["క్వాడ్ క్యాన్సర్ మూన్‌షాట్ (Quad Cancer Moonshot)", "క్వాడ్ వ్యాక్సిన్ ఇనిషియేటివ్ 2.0", "మలేరియా నివారణ ప్రాజెక్ట్", "క్వాడ్ హెల్త్ సెక్యూరిటీ షీల్డ్"],
        0,
        "The leaders of India, USA, Japan, and Australia launched the 'Quad Cancer Moonshot', aimed at reducing the burden of cervical cancer in the Indo-Pacific.",
        "క్వాడ్ దేశాల నాయకులు ఇండో-పసిఫిక్ దేశాలలో సర్వైకల్ క్యాన్సర్ నివారణ కోసం 'క్వాడ్ క్యాన్సర్ మూన్‌షాట్' ను ప్రారంభించారు."
    ))

    # Q194: UN Climate COP28 & COP29
    qs.append(make_q(
        194, "Current Affairs - Climate Change Conferences",
        "The 28th UN Climate Change Conference (COP28) held in Dubai concluded with the historic 'UAE Consensus' calling for transitioning away from fossil fuels. Which city hosted the 29th UN Climate Conference (COP29) in November 2024?",
        "దుబాయ్‌లో జరిగిన COP28 సదస్సులో శిలాజ ఇంధనాల వినియోగాన్ని క్రమంగా తగ్గించాలనే చారిత్రాత్మక ఒప్పందం కుదిరింది. కాగా నవంబర్ 2024లో COP29 ఐక్యరాజ్యసమితి వాతావరణ సదస్సు ఏ నగరంలో జరిగింది?",
        ["Baku, Azerbaijan", "Cairo, Egypt", "Glasgow, UK", "Belém, Brazil"],
        ["బాకూ (అజర్‌బైజాన్ - Baku, Azerbaijan)", "కైరో (ఈజిప్ట్)", "గ్లాస్గో (బ్రిటన్)", "బెలెం (బ్రెజిల్)"],
        0,
        "COP29 was hosted in Baku, Azerbaijan from November 11 to 22, 2024.",
        "COP29 వాతావరణ సదస్సు అజర్‌బైజాన్ రాజధాని బాకూలో జరిగింది."
    ))

    # Q195: 16th Finance Commission Chairman
    qs.append(make_q(
        195, "Current Affairs - National Governance",
        "Under Article 280 of the Constitution, the Union Government constituted the 16th Finance Commission to recommend tax devolution and grants for the 5-year period 2026–2031. Who was appointed as the Chairman of the 16th Finance Commission?",
        "2026–2031 ఐదేళ్ల కాలానికి కేంద్ర-రాష్ట్రాల మధ్య పన్నుల పంపిణీపై సిఫార్సులు చేయడానికి రాజ్యాంగంలోని ఆర్టికల్ 280 కింద నియమించబడిన 16వ ఆర్థిక సంఘం (16th Finance Commission) ఛైర్మన్ ఎవరు?",
        ["Dr. Arvind Panagariya", "Dr. Raghuram Rajan", "N.K. Singh", "Dr. Y.V. Reddy"],
        ["డాక్టర్ అరవింద్ పనగరియా (Dr. Arvind Panagariya)", "డాక్టర్ రఘురామ్ రాజన్", "ఎన్.కె. సింగ్", "డాక్టర్ వై.వి. రెడ్డి"],
        0,
        "Dr. Arvind Panagariya, former Vice-Chairman of NITI Aayog, was appointed Chairman of the 16th Finance Commission, which will submit its report by October 31, 2025.",
        "నీతి ఆయోగ్ మాజీ ఉపాధ్యక్షుడు డాక్టర్ అరవింద్ పనగరియా 16వ ఆర్థిక సంఘం ఛైర్మన్‌గా నియమితులయ్యారు."
    ))

    # Q196: Bharat Ratna 2024 Recipients
    qs.append(make_q(
        196, "Current Affairs - National Honours",
        "In 2024, the Government of India conferred the highest civilian honor 'Bharat Ratna' on five distinguished personalities. Which former Prime Minister hailing from Telangana was among these posthumous awardees?",
        "2024 సంవత్సరంలో భారత అత్యున్నత పౌర పురస్కారం 'భారతరత్న' ఐదుగురు ప్రముఖులకు ప్రకటించబడింది. వీరిలో మరణానంతరం భారతరత్న పొందిన తెలంగాణకు చెందిన మాజీ భారత ప్రధానమంత్రి ఎవరు?",
        ["P.V. Narasimha Rao", "Chaudhary Charan Singh", "K. Chandrashekar Rao", "Burgula Ramakrishna Rao"],
        ["పి.వి. నరసింహారావు (P.V. Narasimha Rao)", "చౌధరి చరణ్ సింగ్", "కె. చంద్రశేఖర రావు", "బూర్గుల రామకృష్ణారావు"],
        0,
        "Former Prime Minister P.V. Narasimha Rao, who pioneered India's historic 1991 economic reforms and hailed from Vangara in Telangana, was awarded the Bharat Ratna in 2024.",
        "భారత ఆర్థిక సంస్కరణల పితామహుడు, తెలంగాణ ముద్దుబిడ్డ మాజీ ప్రధాని పి.వి. నరసింహారావుకు 2024లో కేంద్ర ప్రభుత్వం భారతరత్న పురస్కారాన్ని ప్రదానం చేసింది."
    ))

    # Q197: Indian Railways Kavach System
    qs.append(make_q(
        197, "Current Affairs - Science & Infrastructure",
        "What is the name of the indigenous Automatic Train Protection (ATP) system developed by Indian Railways (RDSO) to prevent train collisions on high-speed rail corridors?",
        "రైలు ప్రమాదాలు మరియు పరస్పర ఢీకొనడాన్ని నివారించడానికి భారతీయ రైల్వే స్వదేశీ పరిజ్ఞానంతో అభివృద్ధి చేసిన ఆటోమేటిక్ ట్రైన్ ప్రొటెక్షన్ (ATP) వ్యవస్థ పేరు ఏమిటి?",
        ["Kavach", "Suraksha", "Trinetra", "Rakshak"],
        ["కవచ్ (Kavach)", "సురక్ష", "త్రినేత్ర", "రక్షక్"],
        0,
        "Kavach is an indigenous SIL-4 certified Automatic Train Protection system that automatically applies brakes if a driver jumps a signal (SPAD) or detects another train on the same track.",
        "రైళ్లు ఒకే పట్టాలపై ఎదురెదురుగా వచ్చినప్పుడు ఆటోమేటిక్‌గా బ్రేకులు వేసే స్వదేశీ రక్షణ వ్యవస్థ 'కవచ్'."
    ))

    # Q198: Chess Olympiad Double Gold
    qs.append(make_q(
        198, "Current Affairs - Sports Achievements",
        "At the 45th FIDE Chess Olympiad held in Budapest, Hungary in September 2024, India achieved historic glory by winning Gold in which event(s)?",
        "హంగేరిలోని బుడాపెస్ట్‌లో సెప్టెంబర్ 2024లో జరిగిన 45వ ఫిడే చెస్ ఒలింపియాడ్‌లో భారతదేశం ఏ విభాగాలలో చారిత్రాత్మక స్వర్ణ పతకాలను గెలుచుకుంది?",
        ["Open Section (Men) only", "Women's Section only", "Historic Double Gold in both Open (Men's) and Women's Sections", "Silver in Men and Gold in Women"],
        ["ఓపెన్ (పురుషుల) విభాగంలో మాత్రమే", "మహిళల విభాగంలో మాత్రమే", "ఓపెన్ (పురుషులు) మరియు మహిళల రెండు విభాగాలలోనూ చారిత్రాత్మక డబుల్ గోల్డ్", "పురుషులలో రజతం, మహిళల్లో స్వర్ణం"],
        2,
        "India created history at the 45th Chess Olympiad in Budapest by winning Gold in both the Open Section (D. Gukesh, Arjun Erigaisi, Praggnanandhaa) and the Women's Section (Harika Dronavalli, Divya Deshmukh, Vantika Agrawal).",
        "బుడాపెస్ట్ చెస్ ఒలింపియాడ్‌లో భారత్ పురుషులు మరియు మహిళల రెండు విభాగాలలోనూ స్వర్ణ పతకాలు సాధించి చరిత్ర సృష్టించింది."
    ))

    # Q199: Telangana HYDRAA Agency
    qs.append(make_q(
        199, "Telangana Current Affairs - State Initiatives",
        "What is the full expansion and primary mandate of 'HYDRAA', established by the Government of Telangana in 2024?",
        "తెలంగాణ ప్రభుత్వం 2024లో ఏర్పాటు చేసిన 'HYDRAA' పూర్తి రూపం మరియు దాని ప్రధాన బాధ్యత ఏమిటి?",
        ["Hyderabad Disaster Response and Asset Monitoring and Protection Agency - to protect government lands, lakes, and disaster management within ORR limits", "Hyderabad Drinking Water and River Rejuvenation Authority", "Hyderabad Regional Agricultural Development Agency", "Hyderabad Drainage and Road Access Authority"],
        ["హైదరాబాద్ డిజాస్టర్ రెస్పాన్స్ అండ్ అసెట్ మానిటరింగ్ అండ్ ప్రొటెక్షన్ ఏజెన్సీ (HYDRAA) - చెరువులు, నాలాలు, ప్రభుత్వ ఆస్తుల పరిరక్షణ మరియు విపత్తు నిర్వహణ", "హైదరాబాద్ తాగునీరు మరియు నదుల పునరుజ్జీవన ప్రాధికార సంస్థ", "హైదరాబాద్ ప్రాంతీయ వ్యవసాయ అభివృద్ధి సంస్థ", "హైదరాబాద్ డ్రైనేజీ మరియు రోడ్డు ప్రాధికార సంస్థ"],
        0,
        "HYDRAA (Hyderabad Disaster Response and Asset Monitoring and Protection Agency) was constituted to manage natural disasters, clear illegal encroachments in lakes (FTL/buffer zones), and protect government assets across the Outer Ring Road (ORR) region.",
        "చెరువుల ఎఫ్‌టీఎల్ పరిధిలోని అక్రమ నిర్మాణాలను కూల్చివేసి, నాలాలు, ప్రభుత్వ ఆస్తులను కాపాడటానికి తెలంగాణ ప్రభుత్వం 'హైడ్రా' (HYDRAA) ను ఏర్పాటు చేసింది."
    ))

    # Q200: Telangana Musi Riverfront & Caste Survey
    qs.append(make_q(
        200, "Telangana Current Affairs - Development Policies",
        "Consider the following development initiatives launched by the Government of Telangana in 2024:\n\nStatement I: The Musi Riverfront Development Project aims to rejuvenate the polluted Musi river, construct check dams, and develop green tourist corridors over a 55 km stretch.\nStatement II: Telangana initiated a comprehensive door-to-door Socio-Economic, Educational, Employment, and Caste Survey in November 2024.\n\nWhich of the statements given above is/are correct?",
        "2024లో తెలంగాణ ప్రభుత్వం చేపట్టిన ప్రధాన అభివృద్ధి విధానాలకు సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: మూసి రివర్‌ఫ్రంట్ డెవలప్‌మెంట్ ప్రాజెక్ట్ కాలుష్య నివారణతో పాటు 55 కిలోమీటర్ల మేర చెక్‌డ్యాంలు, పర్యాటక కారిడార్ల అభివృద్ధిని లక్ష్యంగా పెట్టుకుంది.\nప్రకటన II: తెలంగాణ ప్రభుత్వం నవంబర్ 2024లో రాష్ట్రవ్యాప్తంగా ఇంటింటి సామాజిక, ఆర్థిక, విద్య, ఉపాధి మరియు కుల సర్వేను చేపట్టింది.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements describe flagship initiatives undertaken by the Government of Telangana in 2024. The Musi rejuvenation project aims to transform the river corridor, and the comprehensive caste and socio-economic survey was launched to inform policy targeting.",
        "రెండు ప్రకటనలు సరైనవి. మూసి ప్రక్షాళన మరియు సమగ్ర ఇంటింటి సామాజిక ఆర్థిక కుల సర్వేలు తెలంగాణ ప్రభుత్వ ప్రధాన ప్రాజెక్టులు."
    ))

    return qs
