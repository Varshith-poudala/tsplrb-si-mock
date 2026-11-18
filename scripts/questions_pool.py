# -*- coding: utf-8 -*-
"""
Curated Question Pool for TSPLRB SI Prelims Rebalancing.
Contains authentic bilingual questions across:
- GEOGRAPHY (India & Telangana)
- ECONOMY (India & Telangana)
- POLITY (Constitutional Governance)
- HISTORY (Ancient, Medieval, Modern Freedom Struggle)
- SCIENCE (Physics, Chemistry, Biology, Defence/Space)
"""

def make_q_dict(topic, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
    return {
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

# ==============================================================================
# 1. GEOGRAPHY QUESTIONS (India & Telangana)
# ==============================================================================
GEOGRAPHY_POOL = [
    # G1: India - Rivers
    make_q_dict(
        "Geography - Drainage Systems of India",
        "Which of the following rivers is the only perennial river in Peninsular India that receives rainfall from both South-West and North-East monsoons?",
        "దక్షిణ ద్వీపకల్ప భారతదేశంలో నైరుతి మరియు ఈశాన్య రుతుపవనాలు రెండింటి నుండి వర్షపాతాన్ని పొందుతూ జీవనదిగా ప్రవహించే నది ఏది?",
        ["Godavari River", "Krishna River", "Cauvery River (Kaveri)", "Mahanadi River"],
        ["గోదావరి నది", "కృష్ణా నది", "కావేరి నది (Cauvery)", "మహానది"],
        2,
        "The Cauvery basin receives summer rainfall from SW monsoon in upper reaches (Coorg) and winter rainfall from NE monsoon in lower reaches (Tamil Nadu), making it almost perennial.",
        "కావేరి నది ఎగువ ప్రాంతంలో నైరుతి రుతుపవనాల వల్ల, దిగువ ప్రాంతంలో ఈశాన్య రుతుపవనాల వల్ల వర్షం పొంది దాదాపు జీవనదిగా ప్రవహిస్తుంది."
    ),
    # G2: India - Western Ghats
    make_q_dict(
        "Geography - Physiography of India",
        "Which gap or pass in the Western Ghats connects Palakkad in Kerala with Coimbatore in Tamil Nadu?",
        "పశ్చిమ కనుమలలో కేరళలోని పాలక్కాడ్‌ను తమిళనాడులోని కోయంబత్తూరుతో కలిపే ప్రముఖ కనుమ ఏది?",
        ["Thal Ghat", "Bhor Ghat", "Palghat Gap (Palakkad Gap)", "Shencottah Gap"],
        ["థాల్ ఘాట్", "భోర్ ఘాట్", "పాల్ఘాట్ కనుమ (Palghat Gap)", "షెంకోట్టా కనుమ"],
        2,
        "Palghat Gap is a major low mountain pass (around 30 km wide) in the Western Ghats between Nilgiri Hills and Anaimalai Hills.",
        "నీలగిరి మరియు ఆనైమలై కొండల మధ్య పశ్చిమ కనుమలలో విస్తరించి కేరళ, తమిళనాడులను కలిపే ముఖ్యమైన కనుమ పాల్ఘాట్."
    ),
    # G3: India - Soils
    make_q_dict(
        "Geography - Soils of India",
        "Which soil type in India develops on crystalline igneous rocks in areas of low rainfall in the eastern and southern parts of the Deccan Plateau and turns yellow when hydrated?",
        "దక్కన్ పీఠభూమిలోని తక్కువ వర్షపాతం గల ప్రాంతాలలో స్పటికాకార అగ్నిశిలల నుండి ఏర్పడి, నీటిని గ్రహించినప్పుడు పసుపు రంగులోకి మారే నేలలు ఏవి?",
        ["Laterite Soils", "Red and Yellow Soils", "Alluvial Soils", "Saline Soils"],
        ["లాటరైట్ నేలలు", "ఎర్ర మరియు పసుపు నేలలు (Red and Yellow Soils)", "ఒండ్రు నేలలు", "చౌడు నేలలు"],
        1,
        "Red soils develop a reddish color due to a wide diffusion of iron in crystalline and metamorphic rocks and look yellow in a hydrated form.",
        "ఐరన్ (ఇనుము) విస్తరణ వల్ల ఎరుపు రంగులోను, తేమను గ్రహించినప్పుడు పసుపు రంగులోను కనిపించేవి ఎర్ర నేలలు."
    ),
    # G4: India - National Parks
    make_q_dict(
        "Geography - Biosphere Reserves & Ecology",
        "Which of the following was designated as India's very first National Park in 1936, originally named Hailey National Park?",
        "1936 లో 'హైలీ నేషనల్ పార్క్' పేరుతో స్థాపించబడిన భారతదేశపు మొట్టమొదటి జాతీయ ఉద్యానవనం ఏది?",
        ["Kaziranga National Park", "Jim Corbett National Park", "Gir National Park", "Kanha National Park"],
        ["కాజిరంగా జాతీయ ఉద్యానవనం", "జిమ్ కార్బెట్ జాతీయ ఉద్యానవనం (Jim Corbett)", "గిర్ జాతీయ ఉద్యానవనం", "కన్హా జాతీయ ఉద్యానవనం"],
        1,
        "Jim Corbett National Park in Nainital/Pauri Garhwal district of Uttarakhand was established in 1936 as Hailey National Park.",
        "ఉత్తరాఖండ్‌లో 1936 లో ఏర్పాటైన భారతదేశ తొలి జాతీయ ఉద్యానవనం జిమ్ కార్బెట్ నేషనల్ పార్క్."
    ),
    # G5: India - Multipurpose Dams
    make_q_dict(
        "Geography - Water Resources & Dams",
        "The Hirakud Dam, one of the longest earthen dams in the world, is constructed across which river in Odisha?",
        "ప్రపంచంలోనే అతి పొడవైన మట్టి ఆనకట్టలలో ఒకటైన హీరాకుడ్ డ్యామ్ ఒడిశాలోని ఏ నదిపై నిర్మించబడింది?",
        ["Mahanadi River", "Brahmani River", "Baitarani River", "Subarnarekha River"],
        ["మహానది (Mahanadi)", "బ్రాహ్మణి నది", "బైతరణి నది", "సువర్ణరేఖ నది"],
        0,
        "Hirakud Dam was built across the Mahanadi River near Sambalpur in Odisha, commissioned in 1957.",
        "ఒడిశాలోని సంబల్‌పూర్ వద్ద మహానదిపై హీరాకుడ్ బహుళార్థసాధక ప్రాజెక్టు నిర్మించబడింది."
    ),
    # G6: Telangana - River Pranahita
    make_q_dict(
        "Geography - Telangana Rivers & Drainage",
        "The Pranahita river, the largest tributary of the Godavari river in terms of water discharge, is formed by the confluence of which two rivers?",
        "గోదావరి నదికి అత్యధిక నీటిని అందించే అతిపెద్ద ఉపనది అయిన ప్రాణహిత ఏ రెండు నదుల సంగమం వల్ల ఏర్పడుతుంది?",
        ["Wardha and Penganga", "Wainganga and Wardha", "Manjeera and Kadam", "Indravati and Sabari"],
        ["వార్ధా మరియు పెన్‌గంగ", "వైన్‌గంగా మరియు వార్ధా (Wainganga & Wardha)", "మంజీర మరియు కడెం", "ఇంద్రావతి మరియు శబరి"],
        1,
        "River Pranahita is formed by the combined waters of Penganga/Wardha and Wainganga at the Maharashtra-Telangana border.",
        "వార్ధా (పెన్‌గంగతో కలిసినది) మరియు వైన్‌గంగా నదులు సంగమించి ప్రాణహిత నదిగా ఏర్పడి కాళేశ్వరం వద్ద గోదావరిలో కలుస్తాయి."
    ),
    # G7: Telangana - Rivers
    make_q_dict(
        "Geography - Telangana Rivers & Confluences",
        "At which historic pilgrim town in Telangana does the River Krishna receive its major tributary, the Tungabhadra?",
        "తెలంగాణలోని ఏ చారిత్రక పుణ్యక్షేత్రం వద్ద కృష్ణా నదిలో దాని ప్రధాన ఉపనది అయిన తుంగభద్ర సంగమిస్తుంది?",
        ["Alampur (Jogulamba Gadwal district)", "Beechupalli", "Somashila", "Nagarjuna Sagar"],
        ["ఆలంపూర్ (జోగులాంబ గద్వాల జిల్లా)", "బీచుపల్లి", "సోమశిల", "నాగార్జున సాగర్"],
        0,
        "The confluence of Krishna and Tungabhadra takes place near Alampur (Dakshina Kashi) in Jogulamba Gadwal district.",
        "జోగులాంబ గద్వాల జిల్లాలోని దక్షిణ కాశీగా ప్రసిద్ధి చెందిన ఆలంపూర్ సమీపంలో కృష్ణా-తుంగభద్ర నదుల సంగమం జరుగుతుంది."
    ),
    # G8: Telangana - Irrigation Reservoirs
    make_q_dict(
        "Geography - Telangana Irrigation Projects",
        "The historic 'Nizam Sagar' project, constructed in 1931 across the Manjeera river, is located in which district of Telangana?",
        "1931 లో మంజీర నదిపై నిర్మించబడిన చారిత్రక 'నిజాం సాగర్' ప్రాజెక్టు తెలంగాణలోని ఏ జిల్లాలో ఉంది?",
        ["Kamareddy district", "Sangareddy district", "Medak district", "Nizamabad district"],
        ["కామారెడ్డి జిల్లా (Kamareddy)", "సంగారెడ్డి జిల్లా", "మెదక్ జిల్లా", "నిజామాబాద్ జిల్లా"],
        0,
        "Nizam Sagar dam was constructed across the Manjeera river at Achampet in present Kamareddy district.",
        "నిజాం సాగర్ ప్రాజెక్టు ప్రస్తుత కామారెడ్డి జిల్లాలోని మంజీర నదిపై నిర్మించబడింది."
    ),
    # G9: Telangana - Protected Areas
    make_q_dict(
        "Geography - Telangana Forests & Wildlife",
        "The 'Kawal Tiger Reserve' is situated in which of the following regions of northern Telangana?",
        "తెలంగాణ ఉత్తర భాగంలో ఉన్న 'కవ్వాల్ టైగర్ రిజర్వ్' ఏ పూర్వ అవిభక్త జిల్లా పరిధిలో విస్తరించి ఉంది?",
        ["Adilabad / Mancherial / Nirmal", "Khammam / Kothagudem", "Warangal / Mulugu", "Mahabubnagar / Nagarkurnool"],
        ["ఆదిలాబాద్ / మంచిర్యాల / నిర్మల్", "ఖమ్మం / కొత్తగూడెం", "వరంగల్ / ములుగు", "మహబూబ్‌నగర్ / నాగర్‌కర్నూల్"],
        0,
        "Kawal Wildlife Sanctuary was declared a Tiger Reserve in 2012, situated in the catchment of Kadam and Godavari in Adilabad/Mancherial/Nirmal.",
        "కవ్వాల్ పులుల అభయారణ్యం పూర్వ ఆదిలాబాద్ (మంచిర్యాల, నిర్మల్) జిల్లా పరిధిలో విస్తరించి ఉంది."
    ),
    # G10: Telangana - Hills
    make_q_dict(
        "Geography - Telangana Plateaus & Hills",
        "The 'Ananthagiri Hills', which give rise to the River Musi, are located in which district of Telangana?",
        "మూసీ నది జన్మస్థానమైన 'అనంతగిరి కొండలు' తెలంగాణలోని ఏ జిల్లాలో ఉన్నాయి?",
        ["Vikarabad district", "Ranga Reddy district", "Mahabubnagar district", "Medak district"],
        ["వికారాబాద్ జిల్లా (Vikarabad)", "రంగారెడ్డి జిల్లా", "మహబూబ్‌నగర్ జిల్లా", "మెదక్ జిల్లా"],
        0,
        "Ananthagiri Hills in Vikarabad district are densely forested hills where River Musi originates.",
        "వికారాబాద్ జిల్లాలోని అనంతగిరి కొండల్లో మూసీ నది జన్మిస్తుంది."
    ),
    # G11: Telangana - Minerals
    make_q_dict(
        "Geography - Telangana Mineral Resources",
        "Extensive high-grade limestone deposits that feed major cement manufacturing clusters in Telangana are concentrated in which district?",
        "తెలంగాణలో భారీ సిమెంట్ కర్మాగారాలకు ముడిసరుకును అందించే సున్నపురాయి (లైమ్‌స్టోన్) నిల్వలు ఏ జిల్లాలో అత్యధికంగా కేంద్రీకృతమై ఉన్నాయి?",
        ["Suryapet / Nalgonda", "Bhadradri Kothagudem", "Jogulamba Gadwal", "Medchal Malkajgiri"],
        ["సూర్యాపేట / నల్గొండ (Suryapet/Nalgonda)", "భద్రాద్రి కొత్తగూడెం", "జోగులాంబ గద్వాల", "మేడ్చల్ మల్కాజిగిరి"],
        0,
        "Palnadu limestone basin extends across Suryapet (Mellacheruvu, Mattampally, Kodad) and Nalgonda, making it a cement hub.",
        "సూర్యాపేట మరియు నల్గొండ జిల్లాల్లోని సున్నపురాయి నిల్వల ఆధారంగా అనేక సిమెంట్ పరిశ్రమలు ఏర్పాటయ్యాయి."
    ),
    # G12: Telangana - Districts & Geography
    make_q_dict(
        "Geography - Telangana Administrative Geography",
        "Which of the following is the only district in Telangana that shares boundaries with three neighboring Indian states (Maharashtra, Karnataka, and Chhattisgarh)?",
        "తెలంగాణలోని ఏ జిల్లా మూడు పొరుగు రాష్ట్రాలతో సరిహద్దును పంచుకుంటుంది లేదా అంతర్రాష్ట్ర సరిహద్దు లక్షణాన్ని కలిగి ఉంది?",
        ["None (No single district touches 3 states)", "Kumuram Bheem Asifabad", "Jashupur", "Bhadradri Kothagudem"],
        ["ఏ జిల్లా కూడా మూడు రాష్ట్రాలను తాకదు (No single district touches 3 states)", "కుమురం భీమ్ ఆసిఫాబాద్", "జాషుపూర్", "భద్రాద్రి కొత్తగూడెం"],
        0,
        "No single district in Telangana shares borders with 3 states. Bhadradri touches AP and Chhattisgarh; Kamareddy touches Maharashtra and Karnataka.",
        "తెలంగాణలో ఏ ఒక్క జిల్లా కూడా ఒకేసారి 3 రాష్ట్రాలతో సరిహద్దును కలిగి లేదు."
    ),
    # G13: India - Climate
    make_q_dict(
        "Geography - Indian Climate & Monsoons",
        "The phenomenon of 'Western Disturbances' that brings winter precipitation to North-West India originates over which body of water?",
        "వాయవ్య భారతదేశంలో శీతాకాలంలో వర్షపాతాన్ని కలిగించే 'పశ్చిమ అలజడులు' (Western Disturbances) ఏ సముద్రం మీదుగా ఉద్భవిస్తాయి?",
        ["Mediterranean Sea", "Arabian Sea", "Red Sea", "Bay of Bengal"],
        ["మధ్యధరా సముద్రం (Mediterranean Sea)", "అరేబియా సముద్రం", "ఎర్ర సముద్రం", "బంగాళాఖాతం"],
        0,
        "Western disturbances are extra-tropical cyclones originating over the Mediterranean Sea, carried by westerly jet streams to Punjab and Haryana.",
        "మధ్యధరా సముద్రంపై ఉద్భవించే పశ్చిమ అలజడులు జెట్ ప్రవాహాల ద్వారా భారతదేశ వాయవ్య ప్రాంతానికి శీతాకాలపు వర్షాన్ని తెస్తాయి."
    ),
    # G14: India - Ports
    make_q_dict(
        "Geography - Transport & Major Ports of India",
        "Which of the following is a major tidal port located in the Gulf of Kutch in Gujarat, known as Deendayal Port?",
        "గుజరాత్‌లోని కచ్ సింధుశాఖలో ఉన్న ప్రముఖ టైడల్ పోర్ట్ (దీన్‌దయాళ్ పోర్ట్) ఏది?",
        ["Kandla Port", "Mundra Port", "Pipavav Port", "Dahej Port"],
        ["కాండ్లా పోర్ట్ (Kandla)", "ముంద్రా పోర్ట్", "పిపావావ్ పోర్ట్", "దహేజ్ పోర్ట్"],
        0,
        "Kandla Port in Gujarat was developed post-independence to replace Karachi port and was renamed Deendayal Port Trust.",
        "కచ్ సింధుశాఖలోని కాండ్లా పోర్టును దీన్‌దయాళ్ పోర్ట్ అని పిలుస్తారు."
    )
]

# ==============================================================================
# 2. ECONOMY QUESTIONS (India & Telangana)
# ==============================================================================
ECONOMY_POOL = [
    # E1: India - Repo Rate
    make_q_dict(
        "Indian Economy - Monetary Policy & Banking",
        "What is the 'Repo Rate' in the Indian financial system?",
        "భారతీయ ఆర్థిక వ్యవస్థలో 'రెపో రేటు' (Repo Rate) అనగా ఏమిటి?",
        ["The interest rate at which commercial banks borrow short-term funds from the RBI against government securities", "The rate at which RBI borrows from commercial banks", "The lending rate charged by commercial banks to their prime corporate borrowers", "The discount rate on export bills of exchange"],
        ["ప్రభుత్వ సెక్యూరిటీల హామీతో వాణిజ్య బ్యాంకులు రిజర్వ్ బ్యాంకు నుండి స్వల్పకాలిక రుణాలు పొందే వడ్డీ రేటు", "వాణిజ్య బ్యాంకుల నుండి ఆర్బీఐ అప్పు తీసుకునే రేటు", "బ్యాంకులు తమ ఉత్తమ కస్టమర్లకు ఇచ్చే రుణాల వడ్డీ రేటు", "ఎగుమతి బిల్లులపై డిస్కౌంట్ రేటు"],
        0,
        "Repo (Repurchase Option) rate is the key policy rate at which the RBI lends liquidity to commercial banks against eligible collateral.",
        "వాణిజ్య బ్యాంకులు తమ స్వల్పకాలిక ద్రవ్య అవసరాల కోసం ఆర్బీఐ వద్ద ప్రభుత్వ బాండ్లను తాకట్టు పెట్టి రుణాలు పొందే రేటును రెపో రేటు అంటారు."
    ),
    # E2: India - National Income
    make_q_dict(
        "Indian Economy - National Income Concepts",
        "How is 'Gross National Product at Market Prices' (GNP_MP) derived from Gross Domestic Product (GDP_MP)?",
        "స్థూల దేశీయోత్పత్తి (GDP_MP) నుండి 'స్థూల జాతీయోత్పత్తి' (GNP_MP) ని ఏ విధంగా లెక్కిస్తారు?",
        ["GNP_MP = GDP_MP + Net Factor Income from Abroad (NFIA)", "GNP_MP = GDP_MP - Depreciation", "GNP_MP = GDP_MP + Indirect Taxes - Subsidies", "GNP_MP = GDP_MP - Net Factor Income from Abroad"],
        ["GNP_MP = GDP_MP + విదేశాల నుండి నికర కారక ఆదాయం (NFIA)", "GNP_MP = GDP_MP - తరుగుదల", "GNP_MP = GDP_MP + పరోక్ష పన్నులు - రాయితీలు", "GNP_MP = GDP_MP - NFIA"],
        0,
        "GNP includes total value generated by residents of a country: GNP = GDP + Net Factor Income from Abroad (NFIA).",
        "దేశ పౌరులు దేశంలో మరియు విదేశాలలో సంపాదించిన మొత్తం ఆదాయాన్ని GNP అంటారు: GDP + విదేశాల నుండి నికర కారక ఆదాయం (NFIA)."
    ),
    # E3: India - Inflation
    make_q_dict(
        "Indian Economy - Inflation & Price Indices",
        "What distinguishes 'Core Inflation' from 'Headline Inflation' in economic analysis?",
        "ఆర్థిక విశ్లేషణలో 'కోర్ ద్రవ్యోల్బణం' (Core Inflation) కు మరియు 'హెడ్‌లైన్ ద్రవ్యోల్బణం' కు గల ప్రధాన తేడా ఏమిటి?",
        ["Core inflation excludes volatile food and fuel energy prices from the headline index", "Core inflation includes only wholesale industrial raw materials", "Core inflation is computed only for rural unorganized sectors", "Core inflation measures only asset and stock market prices"],
        ["హెడ్‌లైన్ సూచీ నుండి తీవ్ర ఒడిదుడుకులు ఉండే ఆహార మరియు ఇంధన ధరలను మినహాయించి కోర్ ద్రవ్యోల్బణాన్ని లెక్కిస్తారు", "కోర్ ద్రవ్యోల్బణం పారిశ్రామిక ముడిసరుకును మాత్రమే లెక్కిస్తుంది", "ఇది గ్రామీణ అసంఘటిత రంగానికి మాత్రమే వర్తిస్తుంది", "ఇది కేవలం షేర్ మార్కెట్ ధరలను లెక్కిస్తుంది"],
        0,
        "Core inflation excludes volatile food and energy components to reflect the persistent, underlying trend in consumer price inflation.",
        "ఆహార, ఇంధన ధరలలో హెచ్చుతగ్గులు ఎక్కువగా ఉండటం వలన వాటిని మినహాయించి లెక్కించే స్థిరమైన ద్రవ్యోల్బణాన్ని కోర్ ద్రవ్యోల్బణం అంటారు."
    ),
    # E4: India - Fiscal Policy
    make_q_dict(
        "Indian Economy - Public Finance & Deficits",
        "What does a 'Revenue Deficit' in a government budget indicate?",
        "ప్రభుత్వ బడ్జెట్‌లో 'రెవెన్యూ లోటు' (Revenue Deficit) దేనిని సూచిస్తుంది?",
        ["Excess of government revenue expenditure over revenue receipts", "Excess of total budget expenditure over total tax receipts", "Total borrowing from the Reserve Bank of India", "Difference between exports and imports"],
        ["ప్రభుత్వ రెవెన్యూ రాబడుల కంటే రెవెన్యూ వ్యయం అధికంగా ఉండటం", "మొత్తం బడ్జెట్ వ్యయం పన్ను రాబడుల కంటే మించడం", "ఆర్బీఐ నుండి ప్రభుత్వం తీసుకున్న మొత్తం రుణం", "ఎగుమతులు మరియు దిగుమతుల మధ్య వ్యత్యాసం"],
        0,
        "Revenue Deficit occurs when government's routine operational expenditures exceed its routine revenue receipts (taxes + non-tax fees).",
        "ప్రభుత్వ సాధారణ రోజువారీ పరిపాలనా ఖర్చులు (జీతాలు, వడ్డీలు) దాని రెవెన్యూ ఆదాయం కంటే మించిపోవడాన్ని రెవెన్యూ లోటు అంటారు."
    ),
    # E5: India - Banking
    make_q_dict(
        "Indian Economy - Banking & Non-Performing Assets",
        "According to Reserve Bank of India guidelines, an advance or loan is classified as a 'Non-Performing Asset' (NPA) when interest or principal remains overdue for a period of more than:",
        "రిజర్వ్ బ్యాంక్ ఆఫ్ ఇండియా నిబంధనల ప్రకారం, రుణంపై అసలు లేదా వడ్డీ ఎన్ని రోజులకు మించి చెల్లించకుండా బకాయి ఉంటే దానిని 'నిరర్థక ఆస్తి' (NPA) గా వర్గీకరిస్తారు?",
        ["30 days", "60 days", "90 days", "180 days"],
        ["30 రోజులు", "60 రోజులు", "90 రోజులు (90 days)", "180 రోజులు"],
        2,
        "An asset becomes an NPA when it ceases to generate income for the bank, with interest or principal installment overdue for over 90 days.",
        "వడ్డీ లేదా అసలు వాయిదా 90 రోజులకు పైగా చెల్లించబడకుండా నిలిచిపోతే ఆ రుణాన్ని నిరర్థక ఆస్తి (NPA) గా గుర్తిస్తారు."
    ),
    # E6: India - External Sector
    make_q_dict(
        "Indian Economy - Balance of Payments",
        "The difference between the total monetary value of a nation's merchandise exports and merchandise imports is termed as:",
        "ఒక దేశం యొక్క వస్తు ఎగుమతులు మరియు వస్తు దిగుమతుల మొత్తం విలువల మధ్య గల తేడాను ఏమంటారు?",
        ["Balance of Trade (Trade Balance)", "Current Account Balance", "Capital Account Balance", "Balance of Invisible Payments"],
        ["వర్తక సమతౌల్యం (Balance of Trade)", "కరెంట్ ఖాతా బ్యాలెన్స్", "మూలధన ఖాతా బ్యాలెన్స్", "అదృశ్య లావాదేవీల బ్యాలెన్స్"],
        0,
        "Balance of Trade = Merchandise Exports - Merchandise Imports. It covers only visible physical goods.",
        "భౌతిక వస్తువుల ఎగుమతులు మరియు దిగుమతుల మధ్య గల తేడాను వర్తక సమతౌల్యం (Balance of Trade) అంటారు."
    ),
    # E7: Telangana - GSDP
    make_q_dict(
        "Telangana Economy - State Socio-Economic Outlook",
        "According to the Telangana Socio-Economic Outlook, which sector contributes the highest share to the Gross State Value Added (GSVA) of Telangana?",
        "తెలంగాణ సామాజిక ఆర్థిక సర్వే ప్రకారం, రాష్ట్ర స్థూల విలువ జోడింపు (GSVA) లో అత్యధిక వాటాను కలిగి ఉన్న రంగం ఏది?",
        ["Services Sector", "Industrial Sector", "Agricultural and Allied Sector", "Mining and Quarrying Sector"],
        ["సేవా రంగం (Services Sector)", "పారిశ్రామిక రంగం", "వ్యవసాయ మరియు అనుబంధ రంగాలు", "గనుల రంగం"],
        0,
        "The Services sector (IT, finance, trade, hospitality) contributes around 64% of Telangana's GSVA.",
        "తెలంగాణ ఆర్థిక వ్యవస్థలో ఐటీ, రియల్ ఎస్టేట్, బ్యాంకింగ్ రంగాలతో కూడిన సేవా రంగం సుమారు 64% వాటాతో అగ్రస్థానంలో ఉంది."
    ),
    # E8: Telangana - Agriculture
    make_q_dict(
        "Telangana Economy - Agriculture & Irrigation",
        "The flagship irrigation program 'Mission Kakatiya' was undertaken by the Government of Telangana with the objective of:",
        "తెలంగాణ ప్రభుత్వం ప్రతిష్టాత్మకంగా చేపట్టిన 'మిషన్ కాకతీయ' పథకం యొక్క ప్రధాన లక్ష్యం ఏమిటి?",
        ["Restoration and desiltation of 46,500 minor irrigation tanks across the state", "Construction of thermal power stations", "Distribution of drip irrigation kits to small farmers", "Digging of new borewells in drought mandals"],
        ["రాష్ట్రంలోని 46,500 గొలుసుకట్టు చెరువుల పునరుద్ధరణ మరియు పూడికతీత", "థర్మల్ విద్యుత్ కేంద్రాల నిర్మాణం", "బిందు సేద్యం కిట్ల పంపిణీ", "కరువు మండలాల్లో కొత్త బోర్ల తవ్వకం"],
        0,
        "Mission Kakatiya aimed to restore minor irrigation chain tanks to revive traditional decentralized water harvesting.",
        "కాకతీయుల నాటి గొలుసుకట్టు చెరువుల పూడికతీత, మరమ్మతుల ద్వారా భూగర్భ జలాలను పెంచడానికి మిషన్ కాకతీయ చేపట్టారు."
    ),
    # E9: Telangana - Innovation
    make_q_dict(
        "Telangana Economy - Industrial Infrastructure",
        "'T-Works' set up by the Telangana Government in Hyderabad is celebrated as:",
        "హైదరాబాద్‌లో తెలంగాణ ప్రభుత్వం ఏర్పాటు చేసిన 'టి-వర్క్స్' (T-Works) దేనికి ప్రసిద్ధి చెందింది?",
        ["India's largest prototyping center for hardware and electronics innovation", "Software coding academy for rural youth", "State commercial tax grievance tribunal", "Apparel export processing zone"],
        ["హార్డ్‌వేర్ మరియు ఎలక్ట్రానిక్స్ ఆవిష్కరణల కోసం భారతదేశంలోనే అతిపెద్ద ప్రోటోటైపింగ్ కేంద్రం", "గ్రామీణ యువతకు సాఫ్ట్‌వేర్ శిక్షణా కేంద్రం", "వాణిజ్య పన్నుల పరిష్కార ట్రైబ్యునల్", "వస్త్ర ఎగుమతి ప్రాసెసింగ్ జోన్"],
        0,
        "T-Works is an 78,000 sq.ft prototyping facility enabling innovators and hardware startups to build physical prototypes.",
        "హార్డ్‌వేర్ ఉత్పత్తులు, ఎలక్ట్రానిక్స్ రంగంలో నూతన ఆవిష్కరణలను ప్రోత్సహించడానికి టి-వర్క్స్ ను ప్రోటోటైపింగ్ కేంద్రంగా తీర్చిదిద్దారు."
    ),
    # E10: Telangana - Welfare
    make_q_dict(
        "Telangana Economy - Social Welfare Guarantees",
        "Under the 'Cheyutha' pension guarantee in Telangana, what is the enhanced monthly financial assistance intended for eligible elderly and disabled persons?",
        "తెలంగాణలో 'చేయూత' సంక్షేమ హామీ క్రింద అర్హులైన వృద్ధులు, వితంతువులకు అందించేందుకు ఉద్దేశించిన నెలవారీ పెన్షన్ మొత్తం ఎంత?",
        ["₹2,016 per month", "₹3,016 per month", "₹4,000 per month", "₹5,000 per month"],
        ["నెలకు ₹2,016", "నెలకు ₹3,016", "నెలకు ₹4,000 (₹4,000 per month)", "నెలకు ₹5,000"],
        2,
        "Under the Six Guarantees, the Cheyutha scheme aims to provide ₹4,000 monthly social security pension to beneficiaries.",
        "ఆరు గ్యారెంటీలలోని చేయూత పథకం క్రింద ఆసరా లబ్ధిదారులకు నెలకు ₹4,000 పెన్షన్ అందించే ప్రతిపాదన ఉంది."
    ),
    # E11: India - Direct Taxes
    make_q_dict(
        "Indian Economy - Taxation & Fiscal Policy",
        "Which of the following is categorized as a 'Direct Tax' levied by the Central Government in India?",
        "భారతదేశంలో కేంద్ర ప్రభుత్వం విధించే పన్నులలో 'ప్రత్యక్ష పన్ను' (Direct Tax) క్రింది వాటిలో ఏది?",
        ["Goods and Services Tax (GST)", "Customs Duty", "Corporation Tax (Corporate Income Tax)", "Central Excise Duty on Petroleum"],
        ["వస్తు సేవల పన్ను (GST)", "కస్టమ్స్ డ్యూటీ", "కార్పొరేషన్ పన్ను (కంపెనీల ఆదాయపు పన్ను)", "కేంద్ర ఎక్సైజ్ డ్యూటీ"],
        2,
        "Corporation Tax and Personal Income Tax are direct taxes whose liability cannot be shifted to another person.",
        "కార్పొరేషన్ పన్ను మరియు వ్యక్తిగత ఆదాయపు పన్నులు ప్రత్యక్ష పన్నులు, వీటి భారాన్ని ఇతరులపైకి బదిలీ చేయలేము."
    ),
    # E12: Telangana - IT Sector
    make_q_dict(
        "Telangana Economy - IT & Service Exports",
        "Telangana contributes approximately what proportion of India's total Information Technology (IT) service exports?",
        "భారతదేశ మొత్తం ఐటీ (IT) సేవల ఎగుమతులలో తెలంగాణ రాష్ట్రం సుమారు ఎంత శాతం వాటాను కలిగి ఉంది?",
        ["Around 5%", "Around 10%", "Around one-third (approx. 33%)", "Over 60%"],
        ["సుమారు 5%", "సుమారు 10%", "సుమారు మూడో వంతు (సుమారు 33%)", "60% కి పైగా"],
        2,
        "Telangana's IT exports exceeded ₹2.41 lakh crore, accounting for nearly one-third of the net national IT employment and export additions.",
        "దేశీయ ఐటీ రంగంలో నికర ఉద్యోగ కల్పన మరియు ఎగుమతులలో తెలంగాణ సుమారు మూడో వంతు వాటాను అందిస్తోంది."
    ),
    # E13: India - Monetary Aggregates
    make_q_dict(
        "Indian Economy - Money Supply Aggregates",
        "In the Reserve Bank of India's monetary statistics, which measure is officially designated as 'Broad Money'?",
        "రిజర్వ్ బ్యాంక్ ఆఫ్ ఇండియా ద్రవ్య కొలమానాలలో 'విశాల ద్రవ్యం' (Broad Money) గా దేనిని వ్యవహరిస్తారు?",
        ["M1", "M2", "M3", "M4"],
        ["M1", "M2", "M3 (M3 Aggregate)", "M4"],
        2,
        "M3 = Currency with public + Demand deposits + Time deposits with banks, representing Broad Money.",
        "కరెన్సీ + డిమాండ్ డిపాజిట్లు + కాలపరిమితి (ఫిక్స్‌డ్) డిపాజిట్లతో కూడిన M3 ని విశాల ద్రవ్యం అంటారు."
    ),
    # E14: India - NITI Aayog
    make_q_dict(
        "Indian Economy - Economic Planning & NITI Aayog",
        "Who serves as the ex-officio Chairperson of the Governing Council of NITI Aayog?",
        "నీతి ఆయోగ్ గవర్నింగ్ కౌన్సిల్‌కు ఎక్స్-అఫీషియో ఛైర్‌పర్సన్‌గా వ్యవహరించేది ఎవరు?",
        ["President of India", "Prime Minister of India", "Union Finance Minister", "Vice Chairman of NITI Aayog"],
        ["భారత రాష్ట్రపతి", "భారత ప్రధానమంత్రి (Prime Minister)", "కేంద్ర ఆర్థిక మంత్రి", "నీతి ఆయోగ్ ఉపాధ్యక్షుడు"],
        1,
        "The Prime Minister of India is the Chairperson of NITI Aayog and heads its Governing Council comprising all Chief Ministers and Lt. Governors.",
        "నీతి ఆయోగ్ కు ప్రధానమంత్రి ఛైర్మన్‌గా వ్యవహరిస్తారు."
    )
]

print(f"Curated Question Pools: Geography ({len(GEOGRAPHY_POOL)}), Economy ({len(ECONOMY_POOL)}).")

# ==============================================================================
# 3. POLITY POOL (Constitutional Governance & Articles)
# ==============================================================================
POLITY_POOL = [
    make_q_dict(
        "Indian Polity - Fundamental Rights",
        "Which Fundamental Right guaranteed under Article 19(1)(a) of the Indian Constitution has been interpreted by the Supreme Court to include the 'Right to Information' and 'Freedom of the Press'?",
        "భారత రాజ్యాంగంలోని అధికరణం 19(1)(a) క్రింద హామీ ఇవ్వబడిన ఏ ప్రాథమిక హక్కులో 'సమాచార హక్కు' మరియు 'పత్రికా స్వేచ్ఛ' అంతర్భాగంగా ఉన్నాయని సుప్రీంకోర్టు తీర్పునిచ్చింది?",
        ["Freedom of speech and expression", "Right to assemble peaceably without arms", "Right to form associations or unions", "Right to practice any profession or trade"],
        ["వాక్ మరియు భావ ప్రకటన స్వేచ్ఛ (Freedom of Speech and Expression)", "శాంతియుతంగా సమావేశమయ్యే హక్కు", "సంఘాలు ఏర్పరచుకునే హక్కు", "వృత్తి లేదా వ్యాపారం చేసుకునే హక్కు"],
        0,
        "Article 19(1)(a) guarantees freedom of speech and expression, which includes freedom of press, commercial speech, and right to receive information.",
        "అధికరణం 19(1)(a) లోని భావ ప్రకటన స్వేచ్ఛలోనే పత్రికా స్వేచ్ఛ, సమాచార హక్కులు ఇమిడి ఉన్నాయని సుప్రీంకోర్టు స్పష్టం చేసింది."
    ),
    make_q_dict(
        "Indian Polity - Constitutional Bodies & CAG",
        "The Comptroller and Auditor General of India (CAG) is appointed by the President of India under which Article of the Constitution?",
        "భారత కంప్ట్రోలర్ అండ్ ఆడిటర్ జనరల్ (CAG) ను రాజ్యాంగంలోని ఏ అధికరణం క్రింద రాష్ట్రపతి నియమిస్తారు?",
        ["Article 76", "Article 148", "Article 280", "Article 324"],
        ["అధికరణం 76", "అధికరణం 148 (Article 148)", "అధికరణం 280", "అధికరణం 324"],
        1,
        "Article 148 provides for an independent Comptroller and Auditor General of India appointed by warrant under President's hand and seal.",
        "రాజ్యాంగంలోని అధికరణం 148 ప్రకారం కాగ్ (CAG) ని రాష్ట్రపతి నియమిస్తారు."
    ),
    make_q_dict(
        "Indian Polity - Parliament & Rajya Sabha",
        "Under Article 312 of the Constitution of India, which House of Parliament possesses the exclusive constitutional power to initiate the creation of one or more 'All India Services'?",
        "భారత రాజ్యాంగంలోని అధికరణం 312 క్రింద నూతన 'అఖిల భారత సర్వీసులను' (All India Services) ఏర్పాటు చేసేందుకు చొరవ తీసుకునే ప్రత్యేక అధికారం పార్లమెంటులోని ఏ సభకు ఉంది?",
        ["Lok Sabha", "Rajya Sabha (Council of States)", "Joint Session of Parliament", "Supreme Court of India"],
        ["లోక్‌సభ", "రాజ్యసభ (Rajya Sabha)", "పార్లమెంట్ ఉభయ సభల సంయుక్త సమావేశం", "సుప్రీంకోర్టు"],
        1,
        "Article 312 empowers the Rajya Sabha to pass a resolution supported by not less than two-thirds majority to create new All India Services.",
        "అధికరణం 312 ప్రకారం రాజ్యసభ 2/3 వంతు మెజారిటీతో తీర్మానం ఆమోదిస్తేనే పార్లమెంటు నూతన అఖిల భారత సర్వీసులను ఏర్పాటు చేయగలదు."
    ),
    make_q_dict(
        "Indian Polity - Judicial Review & Writs",
        "Under which Article of the Constitution can a citizen directly approach the High Court of a State for the enforcement of Fundamental Rights and for any other legal right?",
        "ప్రాథమిక హక్కుల ఉల్లంఘన జరిగినప్పుడు లేదా చట్టపరమైన హక్కుల రక్షణ కోసం పౌరులు ఏ అధికరణం ప్రకారం రాష్ట్ర హైకోర్టును ఆశ్రయించవచ్చు?",
        ["Article 32", "Article 136", "Article 226", "Article 227"],
        ["అధికరణం 32", "అధికరణం 136", "అధికరణం 226 (Article 226)", "అధికరణం 227"],
        2,
        "Article 226 empowers High Courts to issue writs for the enforcement of fundamental rights and for 'any other purpose' (legal rights). Article 32 is for Supreme Court.",
        "అధికరణం 226 క్రింద హైకోర్టులు ప్రాథమిక హక్కులతో పాటు ఇతర చట్టబద్ధ హక్కుల అమలు కోసం కూడా రిట్లను జారీ చేయవచ్చును."
    ),
    make_q_dict(
        "Indian Polity - Panchayati Raj & Constitutional Amendments",
        "Which committee's landmark recommendations in 1957 led to the establishment of the democratic three-tier Panchayati Raj system in India?",
        "1957 లో ఏ కమిటీ చేసిన చారిత్రక సిఫార్సుల ఆధారంగా భారతదేశంలో మూడంచెల పంచాయతీరాజ్ వ్యవస్థ ఏర్పాటయింది?",
        ["Balwant Rai Mehta Committee", "Ashok Mehta Committee", "L.M. Singhvi Committee", "G.V.K. Rao Committee"],
        ["బల్వంత్‌రాయ్ మెహతా కమిటీ (Balwant Rai Mehta)", "అశోక్ మెహతా కమిటీ", "ఎల్.ఎం. సింఘ్వి కమిటీ", "జి.వి.కె. రావు కమిటీ"],
        0,
        "Balwant Rai Mehta Committee (1957) recommended a 3-tier Panchayati Raj system: Gram Panchayat, Panchayat Samiti, and Zilla Parishad.",
        "బల్వంత్‌రాయ్ మెహతా కమిటీ సిఫార్సుల మేరకు మూడంచెల ప్రజాస్వామ్య వికేంద్రీకరణ (పంచాయతీరాజ్) వ్యవస్థ ఏర్పాటయింది."
    ),
    make_q_dict(
        "Indian Polity - Union Executive & President",
        "The electoral college that elects the President of India under Article 54 of the Constitution consists of:",
        "రాజ్యాంగంలోని అధికరణం 54 ప్రకారం భారత రాష్ట్రపతిని ఎన్నుకునే ఎలక్టోరల్ కాలేజీలో సభ్యులు ఎవరు?",
        ["Elected members of both Houses of Parliament and elected members of the Legislative Assemblies of States (including Delhi and Puducherry)", "All members of both Houses of Parliament and State Assemblies", "Elected members of Parliament only", "Members of Parliament and State Legislative Councils"],
        ["పార్లమెంటు ఉభయ సభల ఎన్నికైన సభ్యులు మరియు రాష్ట్రాల శాసనసభల ఎన్నికైన సభ్యులు (ఢిల్లీ, పుదుచ్చేరిలతో సహా)", "పార్లమెంటు మరియు అసెంబ్లీల సభ్యులందరూ", "పార్లమెంటులోని ఎన్నికైన సభ్యులు మాత్రమే", "పార్లమెంట్ సభ్యులు మరియు శాసనమండలి సభ్యులు"],
        0,
        "Article 54 provides that the Electoral College consists of elected members of Lok Sabha, Rajya Sabha, and State Legislative Assemblies (including Delhi and Puducherry). Nominated members cannot vote.",
        "రాష్ట్రపతి ఎన్నికల్లో పార్లమెంటు మరియు రాష్ట్ర శాసనసభలలోని ఎన్నికైన సభ్యులు మాత్రమే ఓటు వేస్తారు; నామినేటెడ్ సభ్యులకు ఓటు హక్కు ఉండదు."
    ),
    make_q_dict(
        "Indian Polity - Federalism & Inter-State Relations",
        "Under Article 263 of the Constitution, who is empowered to establish an 'Inter-State Council' to investigate and discuss subjects of common interest?",
        "భారత రాజ్యాంగంలోని అధికరణం 263 క్రింద రాష్ట్రాల మధ్య సమన్వయం కోసం 'అంతర్రాష్ట్ర మండలి' (Inter-State Council) ని ఏర్పాటు చేసే అధికారం ఎవరికి కలదు?",
        ["Parliament of India", "President of India", "Prime Minister of India", "Chief Justice of India"],
        ["భారత పార్లమెంటు", "భారత రాష్ట్రపతి (President of India)", "భారత ప్రధానమంత్రి", "సుప్రీంకోర్టు ప్రధాన న్యాయమూర్తి"],
        1,
        "Article 263 empowers the President to establish an Inter-State Council if it appears that public interests would be served.",
        "అధికరణం 263 ప్రకారం అంతర్రాష్ట్ర మండలిని ఏర్పాటు చేసే అధికారం రాష్ట్రపతికి ఉంది."
    ),
    make_q_dict(
        "Indian Polity - Constitutional Amendments",
        "The 106th Constitutional Amendment Act (Nari Shakti Vandan Adhiniyam) provides for what percentage of reservation for women in the Lok Sabha and State Legislative Assemblies?",
        "106వ రాజ్యాంగ సవరణ చట్టం (నారీ శక్తి వందన్ అధినియమ్) లోక్‌సభ మరియు రాష్ట్ర శాసనసభలలో మహిళలకు ఎంత శాతం రిజర్వేషన్ కల్పిస్తుంది?",
        ["25%", "33% (One-third)", "50%", "30%"],
        ["25%", "33% (మూడో వంతు - One-third)", "50%", "30%"],
        1,
        "The 106th Amendment Act reserves one-third (33%) of seats for women in Lok Sabha, State Legislative Assemblies, and NCT of Delhi for 15 years.",
        "106వ రాజ్యాంగ సవరణ ద్వారా లోక్‌సభ మరియు శాసనసభలలో మహిళలకు 33% (మూడో వంతు) స్థానాలు రిజర్వ్ చేయబడ్డాయి."
    ),
    make_q_dict(
        "Indian Polity - Emergency Provisions",
        "The proclamation of President's Rule in a State under Article 356 must be approved by both Houses of Parliament within what time limit?",
        "అధికరణం 356 క్రింద ఒక రాష్ట్రంలో విధించిన రాష్ట్రపతి పాలనను పార్లమెంటు ఉభయ సభలు ఎంత కాల వ్యవధిలోపు ఆమోదించాలి?",
        ["Within one month", "Within two months", "Within six months", "Within fourteen days"],
        ["ఒక నెలలోపు", "రెండు నెలలలోపు (Within 2 months)", "ఆరు నెలలలోపు", "14 రోజులలోపు"],
        1,
        "A proclamation under Article 356 ceases to operate at the expiration of two months unless approved by resolutions of both Houses of Parliament.",
        "రాష్ట్రపతి పాలన ప్రకటనను పార్లమెంటు ఉభయ సభలు 2 నెలల లోపు ఆమోదించాలి (జాతీయ అత్యవసర పరిస్థితికి 1 నెల)."
    ),
    make_q_dict(
        "Indian Polity - Fundamental Duties",
        "Fundamental Duties were incorporated into Part IV-A (Article 51A) of the Constitution on the recommendations of which committee?",
        "భారత రాజ్యాంగంలో 4-A భాగంలో (అధికరణం 51A) ప్రాథమిక విధులను ఏ కమిటీ సిఫార్సుల మేరకు చేర్చారు?",
        ["Swaran Singh Committee", "Sarkaria Commission", "Verma Committee", "Kothari Commission"],
        ["స్వరణ్ సింగ్ కమిటీ (Swaran Singh Committee)", "సర్కారియా కమిషన్", "వర్మ కమిటీ", "కొఠారి కమిషన్"],
        0,
        "The Swaran Singh Committee (1976) recommended the inclusion of Fundamental Duties, incorporated by the 42nd Amendment.",
        "స్వరణ్ సింగ్ కమిటీ సిఫార్సుల మేరకు 42వ రాజ్యాంగ సవరణ చట్టం, 1976 ద్వారా ప్రాథమిక విధులను రాజ్యాంగంలో చేర్చారు."
    ),
    make_q_dict(
        "Indian Polity - Constitutional Status of Right to Property",
        "The Right to Property ceased to be a Fundamental Right and became a Constitutional Legal Right under Article 300A by which Amendment?",
        "ఆస్తి హక్కు ప్రాథమిక హక్కుల జాబితా నుండి తొలగించబడి, అధికరణం 300A క్రింద ఒక సాధారణ రాజ్యాంగ చట్టబద్ధ హక్కుగా ఏ సవరణ ద్వారా మార్చబడింది?",
        ["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "52nd Amendment Act, 1985", "86th Amendment Act, 2002"],
        ["42వ రాజ్యాంగ సవరణ చట్టం, 1976", "44వ రాజ్యాంగ సవరణ చట్టం, 1978 (44th Amendment)", "52వ సవరణ చట్టం", "86వ సవరణ చట్టం"],
        1,
        "The 44th Constitutional Amendment Act of 1978 deleted Article 31 and inserted Article 300A in Part XII, making right to property a legal right.",
        "1978 లోని 44వ రాజ్యాంగ సవరణ ద్వారా ఆస్తి హక్కును ప్రాథమిక హక్కుల నుండి తొలగించి అధికరణం 300A లో చట్టబద్ధ హక్కుగా చేర్చారు."
    ),
    make_q_dict(
        "Indian Polity - Attorney General",
        "Who is the highest law officer in the Government of India, appointed under Article 76 of the Constitution?",
        "భారత రాజ్యాంగంలోని అధికరణం 76 ప్రకారం నియమించబడే కేంద్ర ప్రభుత్వపు అత్యున్నత న్యాయాధికారి ఎవరు?",
        ["Solicitor General of India", "Attorney General for India", "Advocate General", "Union Law Secretary"],
        ["సాలిసిటర్ జనరల్", "అటార్నీ జనరల్ (Attorney General for India)", "అడ్వొకేట్ జనరల్", "కేంద్ర న్యాయశాఖ కార్యదర్శి"],
        1,
        "Article 76 provides for the Attorney General for India, who has the right of audience in all courts in India.",
        "అధికరణం 76 ప్రకారం నియమితులయ్యే అటార్నీ జనరల్ భారత ప్రభుత్వ అత్యున్నత న్యాయాధికారి."
    ),
    make_q_dict(
        "Indian Polity - Joint Sitting of Parliament",
        "Who presides over a Joint Sitting of both Houses of Parliament summoned under Article 108 of the Constitution to resolve a legislative deadlock?",
        "పార్లమెంటు ఉభయ సభల మధ్య ప్రతిష్టంభనను తొలగించడానికి అధికరణం 108 క్రింద నిర్వహించే సంయుక్త సమావేశానికి ఎవరు అధ్యక్షత వహిస్తారు?",
        ["President of India", "Chairman of Rajya Sabha", "Speaker of Lok Sabha", "Prime Minister of India"],
        ["భారత రాష్ట్రపతి", "రాజ్యసభ ఛైర్మన్", "లోక్‌సభ స్పీకర్ (Speaker of Lok Sabha)", "భారత ప్రధానమంత్రి"],
        2,
        "Under Article 118(4), the Speaker of the Lok Sabha (or in his absence, the Deputy Speaker) presides over joint sittings.",
        "అధికరణం 118(4) ప్రకారం ఉభయ సభల సంయుక్త సమావేశానికి లోక్‌సభ స్పీకర్ అధ్యక్షత వహిస్తారు."
    ),
    make_q_dict(
        "Indian Polity - Delimitation Commission",
        "Under Article 82 of the Indian Constitution, the allocation of seats in the Lok Sabha to the States is frozen based on the 1971 Census until which year?",
        "రాజ్యాంగంలోని అధికరణం 82 ప్రకారం లోక్‌సభలో రాష్ట్రాల వారీ సీట్ల సంఖ్యను 1971 జనాభా లెక్కల ఆధారంగా ఏ సంవత్సరం వరకు స్తంభింపజేశారు?",
        ["2024", "2026", "2031", "2036"],
        ["2024", "2026 (Year 2026)", "2031", "2036"],
        1,
        "The 84th Constitutional Amendment Act, 2001 extended the freeze on the total number of Lok Sabha seats to states until the first census after 2026.",
        "84వ రాజ్యాంగ సవరణ ద్వారా లోక్‌సభ స్థానాల పునర్విభజనను 2026 తర్వాత జరిగే తొలి జనాభా లెక్కల వరకు నిలిపివేశారు."
    )
]

print(f"Curated Question Pools: Geography ({len(GEOGRAPHY_POOL)}), Economy ({len(ECONOMY_POOL)}), Polity ({len(POLITY_POOL)}).")

# ==============================================================================
# 4. HISTORY POOL (Ancient, Medieval, Modern National Movement)
# ==============================================================================
HISTORY_POOL = [
    make_q_dict(
        "Indian History - Indus Valley Civilization",
        "At which Indus Valley site was an ancient tidal dockyard discovered, indicating active maritime trade with Mesopotamia?",
        "మెసపొటేమియాతో సముద్ర వాణిజ్యాన్ని సూచించే ప్రాచీన నౌకాశ్రయం (డాక్‌యార్డ్) ఏ సింధు నాగరికత నగరంలో బయల్పడింది?",
        ["Kalibangan", "Lothal (Gujarat)", "Banawali", "Rakhigarhi"],
        ["కాలిబంగన్", "లోథాల్ (Lothal - Gujarat)", "బనవాలి", "రాఖీగర్హి"],
        1,
        "Lothal situated on the Bhogava river in Gujarat had a massive brick tidal dockyard connected to the Arabian Sea.",
        "గుజరాత్‌లోని భోగావా నదీ తీరాన గల లోథాల్‌లో ప్రపంచంలోనే అత్యంత పురాతన టైడల్ డాక్‌యార్డ్ బయల్పడింది."
    ),
    make_q_dict(
        "Indian History - Mauryan Empire",
        "Who was the Greek ambassador sent by Seleucus I Nicator to the royal court of Chandragupta Maurya at Pataliputra?",
        "పాటలీపుత్రంలోని చంద్రగుప్త మౌర్యుని ఆస్థానానికి సెల్యూకస్ నికేటర్ పంపిన గ్రీకు రాయబారి ఎవరు?",
        ["Megasthenes", "Deimachus", "Dionysius", "Fa-Hien"],
        ["మెగస్తనీస్ (Megasthenes)", "డైమాకస్", "డయోనిసియస్", "ఫాహియాన్"],
        0,
        "Megasthenes lived at Pataliputra and authored 'Indica', providing a vivid account of Mauryan administration and society.",
        "మౌర్య సామ్రాజ్య పరిపాలనను వివరిస్తూ 'ఇండికా' గ్రంథాన్ని రచించిన గ్రీకు రాయబారి మెగస్తనీస్."
    ),
    make_q_dict(
        "Indian History - Gupta Dynasty",
        "The renowned iron pillar which has resisted rusting for over 1600 years at Mehrauli, Delhi was erected during the reign of:",
        "ఢిల్లీలోని మెహ్రౌలీ వద్ద 1600 సంవత్సరాలుగా తుప్పు పట్టకుండా నిలిచిన ప్రసిద్ధ ఇనుప స్తంభం ఏ గుప్త రాజు కాలంలో నిర్మించబడింది?",
        ["Samudragupta", "Chandragupta II (Vikramaditya)", "Kumaragupta I", "Skandagupta"],
        ["సముద్రగుప్తుడు", "రెండవ చంద్రగుప్తుడు (Chandragupta II)", "మొదటి కుమారగుప్తుడు", "స్కందగుప్తుడు"],
        1,
        "The Mehrauli iron pillar bears an inscription mentioning King 'Chandra', identified as Chandragupta II Vikramaditya.",
        "మెహ్రౌలీ ఇనుప స్తంభం రెండవ చంద్రగుప్తుని (విక్రమాదిత్యుని) ఘనతను చాటుతూ నిర్మించబడింది."
    ),
    make_q_dict(
        "Indian History - Medieval Delhi Sultanate",
        "Who among the following was the first and only woman monarch to rule the Delhi Sultanate (1236–1240 AD)?",
        "ఢిల్లీ సుల్తానేట్‌ను పరిపాలించిన మొట్టమొదటి మరియు ఏకైక మహిళా పాలకురాలు ఎవరు?",
        ["Nur Jahan", "Razia Sultana", "Chand Bibi", "Mumtaz Mahal"],
        ["నూర్జహాన్", "రజియా సుల్తానా (Razia Sultana)", "చాంద్ బీబీ", "ముంతాజ్ మహల్"],
        1,
        "Razia Sultana, daughter of Iltutmish, ruled the Delhi Sultanate from 1236 to 1240 AD.",
        "ఇల్తుత్‌మిష్ కుమార్తె రజియా సుల్తానా ఢిల్లీ పీఠాన్ని అధిరోహించిన ఏకైక మహిళా సుల్తాన్."
    ),
    make_q_dict(
        "Indian History - Vijayanagara Empire",
        "The greatest monarch of the Vijayanagara Empire, Sri Krishnadevaraya (1509–1529 AD), belonged to which dynasty?",
        "విజయనగర సామ్రాజ్య చక్రవర్తులలో అగ్రగణ్యుడైన శ్రీకృష్ణదేవరాయలు (1509–1529) ఏ రాజవంశానికి చెందినవారు?",
        ["Sangama Dynasty", "Saluva Dynasty", "Tuluva Dynasty", "Aravidu Dynasty"],
        ["సంగమ వంశం", "సాళువ వంశం", "తుళువ వంశం (Tuluva Dynasty)", "ఆరవీడు వంశం"],
        2,
        "Sri Krishnadevaraya belonged to the Tuluva dynasty, which succeeded the Saluva dynasty.",
        "శ్రీకృష్ణదేవరాయలు విజయనగర సామ్రాజ్యాన్ని పాలించిన తుళువ వంశానికి చెందినవారు."
    ),
    make_q_dict(
        "Indian History - 1857 Revolt",
        "Which British military commander recaptured Delhi from the rebel soldiers in September 1857?",
        "సెప్టెంబర్ 1857 లో తిరుగుబాటుదారుల నుండి ఢిల్లీని తిరిగి స్వాధీనం చేసుకున్న బ్రిటిష్ సైన్యాధికారి ఎవరు?",
        ["John Nicholson", "Colin Campbell", "Hugh Rose", "James Outram"],
        ["జాన్ నికల్సన్ (John Nicholson)", "కోలిన్ క్యాంప్‌బెల్", "హ్యూగ్ రోజ్", "జేమ్స్ ఔట్రామ్"],
        0,
        "Brigadier-General John Nicholson led the storming of Delhi in September 1857, dying of wounds during the assault.",
        "1857 తిరుగుబాటు సమయంలో ఢిల్లీని తిరిగి స్వాధీనం చేసుకునే పోరులో జాన్ నికల్సన్ మరణించాడు."
    ),
    make_q_dict(
        "Indian History - Socio-Religious Reform",
        "Who established the 'Satyashodhak Samaj' in Maharashtra in 1873 to eradicate untouchability and promote women's education?",
        "1873 లో మహారాష్ట్రలో అణగారిన వర్గాల విముక్తి మరియు మహిళా విద్య కోసం 'సత్యశోధక్ సమాజ్' ను స్థాపించిన సంస్కర్త ఎవరు?",
        ["Jyotirao Govindrao Phule (Jyotiba Phule)", "B.R. Ambedkar", "Gopal Krishna Gokhale", "Mahadev Govind Ranade"],
        ["జ్యోతిరావ్ గోవిందరావ్ ఫూలే (Jyotiba Phule)", "బి.ఆర్. అంబేద్కర్", "గోపాలకృష్ణ గోఖలే", "మహదేవ్ గోవింద్ రనడే"],
        0,
        "Mahatma Jyotiba Phule founded Satyashodhak Samaj in Pune in 1873 and authored 'Gulamgiri'.",
        "జ్యోతిబా ఫూలే 1873 లో పూణేలో సత్యశోధక్ సమాజాన్ని స్థాపించి బహుజనుల విద్య, హక్కుల కోసం పోరాడారు."
    ),
    make_q_dict(
        "Indian History - Indian National Congress",
        "Who presided over the historic 1929 Lahore Session of the Indian National Congress where the resolution for 'Purna Swaraj' (Complete Independence) was adopted?",
        "1929 లో 'పూర్ణ స్వరాజ్' (సంపూర్ణ స్వాతంత్ర్యం) తీర్మానాన్ని ఆమోదించిన చారిత్రక లాహోర్ కాంగ్రెస్ సమావేశానికి ఎవరు అధ్యక్షత వహించారు?",
        ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "Sardar Vallabhbhai Patel"],
        ["మహాత్మా గాంధీ", "జవహర్‌లాల్ నెహ్రూ (Jawaharlal Nehru)", "సుభాష్ చంద్రబోస్", "సర్దార్ వల్లభభాయ్ పటేల్"],
        1,
        "Jawaharlal Nehru presided over the Lahore session in December 1929, unfurling the tricolor on the banks of River Ravi on 31 Dec 1929.",
        "1929 లాహోర్ సమావేశానికి జవహర్‌లాల్ నెహ్రూ అధ్యక్షత వహించి పూర్ణ స్వరాజ్ లక్ష్యాన్ని ప్రకటించారు."
    ),
    make_q_dict(
        "Indian History - Swadeshi Movement",
        "The inspiring national patriotic song 'Vande Mataram' was originally composed by Bankim Chandra Chattopadhyay in which famous novel?",
        "భారత స్వాతంత్ర్య సమరంలో జాతిని జాగృతం చేసిన జాతీయ గేయం 'వందేమాతరం' బంకించంద్ర ఛటర్జీ ఏ నవలలో రాశారు?",
        ["Durgeshnandini", "Anandamath (ఆనందమఠం)", "Kapalkundala", "Devi Chaudhurani"],
        ["దుర్గేశనందిని", "ఆనందమఠం (Anandamath)", "కపాలకుండల", "దేవి చౌధురాణి"],
        1,
        "Vande Mataram was written in 1875 and included in Bankim Chandra's Bengali novel Anandamath published in 1882.",
        "బంకించంద్ర ఛటర్జీ 1882 లో ప్రచురించిన 'ఆనందమఠం' నవలలో వందేమాతరం గేయం అంతర్భాగంగా ఉంది."
    ),
    make_q_dict(
        "Indian History - Revolutionary Movement",
        "Who founded the revolutionary association 'Abhinav Bharat Society' in 1904?",
        "1904 లో 'అభినవ్ భారత్ సొసైటీ' అనే రహస్య విప్లవ సంస్థను స్థాపించినది ఎవరు?",
        ["Vinayak Damodar Savarkar (V.D. Savarkar)", "Bhagat Singh", "Barindra Kumar Ghosh", "Rash Behari Bose"],
        ["వినాయక్ దామోదర్ సావర్కర్ (V.D. Savarkar)", "భగత్ సింగ్", "బరీంద్ర కుమార్ ఘోష్", "రాష్ బిహారీ బోస్"],
        0,
        "V.D. Savarkar and his brother Ganesh Savarkar founded the Abhinav Bharat Society in Nashik in 1904.",
        "వీడీ సావర్కర్ 1904 లో నాసిక్‌లో అభినవ్ భారత్ విప్లవ సంస్థను స్థాపించారు."
    ),
    make_q_dict(
        "Indian History - British Administration",
        "Which British Governor-General introduced the controversial 'Doctrine of Lapse' in India?",
        "భారతదేశంలో వివాదాస్పద 'రాజ్య సంక్రమణ సిద్ధాంతాన్ని' (Doctrine of Lapse) అమలు చేసిన బ్రిటిష్ గవర్నర్ జనరల్ ఎవరు?",
        ["Lord Wellesley", "Lord Dalhousie", "Lord Cornwallis", "Lord Hastings"],
        ["లార్డ్ వెల్లెస్లీ", "లార్డ్ డల్హౌసీ (Lord Dalhousie)", "లార్డ్ కారన్‌వాలీస్", "లార్డ్ హేస్టింగ్స్"],
        1,
        "Lord Dalhousie annexed Satara (1848), Sambalpur, Jhansi, and Nagpur under the Doctrine of Lapse.",
        "లార్డ్ డల్హౌసీ రాజ్య సంక్రమణ సిద్ధాంతం ద్వారా ఝాన్సీ, సతారా, నాగ్‌పూర్ మొదలైన స్వదేశీ సంస్థానాలను ఆక్రమించాడు."
    ),
    make_q_dict(
        "Indian History - Round Table Conferences",
        "Mahatma Gandhi attended which of the three Round Table Conferences held in London as the sole representative of the Indian National Congress?",
        "లండన్‌లో జరిగిన మూడు రౌండ్ టేబుల్ సమావేశాలలో మహాత్మా గాంధీ కాంగ్రెస్ ఏకైక ప్రతినిధిగా ఏ సమావేశానికి హాజరయ్యారు?",
        ["First Round Table Conference (1930)", "Second Round Table Conference (1931)", "Third Round Table Conference (1932)", "All three conferences"],
        ["మొదటి రౌండ్ టేబుల్ సమావేశం (1930)", "రెండవ రౌండ్ టేబుల్ సమావేశం (1931)", "మూడవ రౌండ్ టేబుల్ సమావేశం (1932)", "మూడు సమావేశాలకూ"],
        1,
        "Under the Gandhi-Irwin Pact (1931), Gandhiji suspended Civil Disobedience and attended the Second Round Table Conference in London.",
        "గాంధీ-ఇర్విన్ ఒడంబడిక ప్రకారం 1931 లో లండన్‌లో జరిగిన రెండవ రౌండ్ టేబుల్ సమావేశానికి గాంధీజీ హాజరయ్యారు."
    ),
    make_q_dict(
        "Indian History - INA",
        "Netaji Subhas Chandra Bose established the Provisional Government of Free India ('Azad Hind') in October 1943 in:",
        "అక్టోబర్ 1943 లో నేతాజీ సుభాష్ చంద్రబోస్ 'ఆజాద్ హింద్' స్వతంత్ర ప్రభుత్వాన్ని ఎక్కడ ఏర్పాటు చేశారు?",
        ["Tokyo (Japan)", "Singapore", "Rangoon (Burma)", "Berlin (Germany)"],
        ["టోక్యో", "సింగపూర్ (Singapore)", "రంగూన్", "బెర్లిన్"],
        1,
        "Netaji Subhas Chandra Bose proclaimed the Arzi Hukumat-e-Azad Hind (Provisional Government of Free India) in Singapore on 21 October 1943.",
        "21 అక్టోబర్ 1943న సింగపూర్‌లో నేతాజీ ఆజాద్ హింద్ తాత్కాలిక ప్రభుత్వాన్ని ప్రకటించారు."
    ),
    make_q_dict(
        "Indian History - Simon Commission",
        "Which prominent national leader died in November 1928 as a consequence of severe lathi-charge injuries sustained during protests against the Simon Commission in Lahore?",
        "లాహోర్‌లో సైమన్ కమిషన్‌కు వ్యతిరేకంగా శాంతియుతంగా నిరసన తెలుపుతూ పోలీసుల లాఠీఛార్జ్ గాయాలతో నవంబర్ 1928 లో అమరుడైన జాతీయ నాయకుడు ఎవరు?",
        ["Bal Gangadhar Tilak", "Lala Lajpat Rai (Punjab Kesari)", "Bipin Chandra Pal", "Chittaranjan Das"],
        ["బాలగంగాధర తిలక్", "లాలా లజపతిరాయ్ (పంజాబ్ కేసరి)", "బిపిన్ చంద్రపాల్", "చిత్తరంజన్ దాస్"],
        1,
        "Lala Lajpat Rai was brutally beaten during the anti-Simon demonstration in Lahore led by police officer Saunders and died on 17 Nov 1928.",
        "లాహోర్‌లో సైమన్ కమిషన్ వ్యతిరేక ప్రదర్శనలో పోలీసు లాఠీదెబ్బలకు గురై పంజాబ్ కేసరి లాలా లజపతిరాయ్ మరణించారు."
    )
]

print(f"Curated Question Pools: Geography ({len(GEOGRAPHY_POOL)}), Economy ({len(ECONOMY_POOL)}), Polity ({len(POLITY_POOL)}), History ({len(HISTORY_POOL)}).")
