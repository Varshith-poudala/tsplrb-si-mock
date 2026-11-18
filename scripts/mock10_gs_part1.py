# -*- coding: utf-8 -*-
"""
Mock Test 10 - General Studies Part 1 (Q101 to Q150)
Strictly adheres to TSPLRB SI PWT Blueprint & Shentu's feedback:
- 101 to 116: Indian Polity & Governance (16 Questions)
  * ECI Appointment Act 2023, 106th Amendment (Nari Shakti), Census & Delimitation, Writs, DPSP, CAG, Pardoning, etc.
- 117 to 136: Telangana Movement & Statehood History (20 Questions)
  * 1919 Farman, 1952 Non-Mulki/City College, 1956 Gentlemen's Agreement, 1969 Agitation, 8-Point & 6-Point Formulas, G.O. 610/Girglani, Million March, Sakala Janula Samme, Srikrishna Committee, AP Reorganisation Act, Armed Struggle, Qutb Shahis, Kakatiyas, Operation Polo, Festivals.
- 137 to 150: Indian History & National Movement (14 Questions)
  * Indus Valley Lothal/Dholavira, Ashoka Edicts, Delhi Sultanate market reforms, Mughal Mansabdari, 1857 leaders, Swadeshi/Vandemataram, Non-Cooperation, Dandi March, INA Subhash Chandra Bose.
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

def get_gs_part1():
    qs = []

    # =========================================================================
    # POLITY & GOVERNANCE (101 - 116: 16 Questions)
    # =========================================================================

    # Q101: ECI Appointment Act 2023
    qs.append(make_q(
        101, "Indian Polity - Election Commission of India",
        "Consider the following statements regarding the 'Chief Election Commissioner and other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023':\n\nStatement I: The Selection Committee to recommend appointments consists of the Prime Minister, the Chief Justice of India, and the Leader of the Opposition.\nStatement II: A Search Committee headed by the Union Minister of Law and Justice prepares a panel of five candidates for the Selection Committee's consideration.\n\nWhich of the statements given above is/are correct?",
        "భారత ఎన్నికల సంఘం (నియామకం, సేవా నిబంధనలు) చట్టం, 2023 కు సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: నియామకాలను సిఫార్సు చేసే ఎంపిక కమిటీలో ప్రధాన మంత్రి, భారత ప్రధాన న్యాయమూర్తి (CJI) మరియు ప్రతిపక్ష నాయకుడు సభ్యులుగా ఉంటారు.\nప్రకటన II: కేంద్ర న్యాయ శాఖ మంత్రి నేతృత్వంలోని సెర్చ్ కమిటీ ఎంపిక కమిటీ పరిశీలన కోసం ఐదుగురు అభ్యర్థుల ప్యానెల్‌ను సిద్ధం చేస్తుంది.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        1,
        "Under the 2023 Act, the Selection Committee consists of: (1) Prime Minister (Chairperson), (2) A nominated Union Cabinet Minister, and (3) Leader of Opposition / Leader of largest opposition party. The CJI is NOT a member in the enacted legislation. Hence Statement I is incorrect and Statement II is correct.",
        "2023 చట్టం ప్రకారం ఎంపిక కమిటీలో ప్రధాని, ఒక కేంద్ర క్యాబినెట్ మంత్రి మరియు ప్రతిపక్ష నాయకుడు ఉంటారు (CJI లేరు). కాబట్టి ప్రకటన I తప్పు, ప్రకటన II సరైనది."
    ))

    # Q102: 106th Amendment Act
    qs.append(make_q(
        102, "Indian Polity - Constitutional Amendments",
        "Which of the following constitutional provisions was inserted by the 106th Constitutional Amendment Act, 2023 (Nari Shakti Vandan Adhiniyam)?",
        "106వ రాజ్యాంగ సవరణ చట్టం, 2023 (నారీ శక్తి వందన్ అధినియం) ద్వారా రాజ్యాంగంలో చేర్చబడిన నిబంధన ఏది?",
        ["Reservation of 33% seats for women in the Rajya Sabha and State Legislative Councils", "Reservation of one-third (33%) of seats for women in Lok Sabha, State Legislative Assemblies, and NCT of Delhi", "Reservation of 50% seats for women in Panchayati Raj Institutions across all states", "Reservation of 27% OBC quota in local bodies"],
        ["రాజ్యసభ మరియు రాష్ట్ర శాసన మండళ్లలో మహిళలకు 33% సీట్ల రిజర్వేషన్", "లోక్‌సభ, రాష్ట్ర శాసనసభలు మరియు ఢిల్లీ అసెంబ్లీలో మహిళలకు మూడింట ఒక వంతు (33%) సీట్ల రిజర్వేషన్", "అన్ని రాష్ట్రాల్లోని పంచాయతీ రాజ్ సంస్థలలో మహిళలకు 50% సీట్ల రిజర్వేషన్", "స్థానిక సంస్థలలో 27% ఓబీసీ కోటా"],
        1,
        "The 106th Amendment Act introduced Articles 330A, 332A, and 239AA(2)(b) reserving 33% seats for women in the Lok Sabha, State Legislative Assemblies, and the Delhi Assembly. It does not apply to the Rajya Sabha or Legislative Councils.",
        "106వ సవరణ ద్వారా ఆర్టికల్ 330A, 332A మరియు 239AA లలో లోక్‌సభ, శాసనసభలలో మహిళలకు 33% రిజర్వేషన్ కల్పించబడింది. ఇది రాజ్యసభ లేదా శాసన మండళ్లకు వర్తించదు."
    ))

    # Q103: Census & Delimitation
    qs.append(make_q(
        103, "Indian Polity - Delimitation & Parliament",
        "Consider the following statements regarding the freeze on Delimitation of Parliamentary constituencies in India:\n\nStatement I: The 84th Constitutional Amendment Act, 2001 froze the total number of seats allocated to each state in the Lok Sabha until the first Census taken after the year 2026.\nStatement II: The internal readjustment and rationalisation of territorial constituencies within each state was carried out based on the 2001 Census.\n\nWhich of the statements given above is/are correct?",
        "భారతదేశంలో పార్లమెంటరీ నియోజకవర్గాల డీలిమిటేషన్ (పునర్విభజన) పై ఉన్న నిలుపుదలకు సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: 84వ రాజ్యాంగ సవరణ చట్టం, 2001 ప్రకారం 2026 తర్వాత నిర్వహించే మొదటి జనాభా లెక్కల వరకు లోక్‌సభలోని రాష్ట్రాల సీట్ల సంఖ్యను స్తంభింపజేశారు.\nప్రకటన II: రాష్ట్రాల లోపల ప్రాదేశిక నియోజకవర్గాల అంతర్గత సరిహద్దుల పునర్వ్యవస్థీకరణ 2001 జనాభా లెక్కల ఆధారంగా జరిగింది.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏదీ సరైనది కాదు"],
        2,
        "Both statements are correct. The 84th Amendment froze inter-state seat allocation until after 2026 (based on 1971 census totals), while allowing internal boundary delimitation based on the 2001 census (87th Amendment).",
        "రెండు ప్రకటనలు సరైనవి. 84వ సవరణ ద్వారా 2026 వరకు లోక్‌సభ సీట్ల సంఖ్యను ఫ్రీజ్ చేశారు మరియు 2001 జనాభా ఆధారంగా అంతర్గత సరిహద్దులను సవరించారు."
    ))

    # Q104: Fundamental Rights & Writs
    qs.append(make_q(
        104, "Indian Polity - Fundamental Rights & Writs",
        "Match List-I (Writ) with List-II (Literal Meaning / Purpose):\n\nList-I\t\t\tList-II\nA. Habeas Corpus\t1. By what authority or warrant?\nB. Mandamus\t\t2. We command a public official to perform duty\nC. Quo Warranto\t\t3. To have the body produced before the court\nD. Certiorari\t\t4. To be certified or quash an order of an inferior court\n\nChoose the correct code:",
        "జాబితా-I (రిట్) ను జాబితా-II (అర్థం / ప్రయోజనం) తో జతపరచండి:\n\nజాబితా-I\t\t\tజాబితా-II\nA. హెబియస్ కార్పస్\t1. ఏ అధికారంతో లేదా వారెంట్‌తో?\nB. మాండమస్\t\t2. ప్రభుత్వ విధిని నిర్వహించాలని మేం ఆజ్ఞాపిస్తున్నాం\nC. కో-వారంటో\t\t3. వ్యక్తి శరీరాన్ని కోర్టు ముందు హాజరుపరచడం\nD. సెర్షియోరరి\t\t4. కింది కోర్టు తీర్పును రద్దు చేయడం లేదా ధృవీకరించడం\n\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-3, B-2, C-1, D-4", "A-3, B-1, C-2, D-4", "A-2, B-3, C-4, D-1", "A-4, B-2, C-1, D-3"],
        ["A-3, B-2, C-1, D-4", "A-3, B-1, C-2, D-4", "A-2, B-3, C-4, D-1", "A-4, B-2, C-1, D-3"],
        0,
        "Habeas Corpus = You may have the body (A-3). Mandamus = We command (B-2). Quo Warranto = By what warrant (C-1). Certiorari = To be certified (D-4). Code: A-3, B-2, C-1, D-4.",
        "హెబియస్ కార్పస్ (A-3), మాండమస్ (B-2), కో-వారంటో (C-1), సెర్షియోరరి (D-4). సరైన కోడ్: A-3, B-2, C-1, D-4."
    ))

    # Q105: Directive Principles
    qs.append(make_q(
        105, "Indian Polity - Directive Principles of State Policy",
        "Under Part IV of the Indian Constitution, which of the following Articles directs the State to secure a 'Uniform Civil Code for the citizens throughout the territory of India'?",
        "భారత రాజ్యాంగంలోని 4వ భాగంలో, 'భారత భూభాగమంతటా పౌరులందరికీ ఏకరీతి పౌరస్మృతిని (Uniform Civil Code) రూపొందించడానికి రాజ్యం ప్రయత్నించాలి' అని ఆదేశించే ఆర్టికల్ ఏది?",
        ["Article 40", "Article 44", "Article 45", "Article 48A"],
        ["ఆర్టికల్ 40", "ఆర్టికల్ 44", "ఆర్టికల్ 45", "ఆర్టికల్ 48A"],
        1,
        "Article 44 directs the State to secure for the citizens a Uniform Civil Code throughout the territory of India. Article 40 relates to Village Panchayats, Article 45 to Early Childhood Care, and Article 48A to Environment Protection.",
        "ఆర్టికల్ 44 యూనిఫాం సివిల్ కోడ్ (UCC) గురించి పేర్కొంటుంది. ఆర్టికల్ 40 గ్రామ పంచాయతీల ఏర్పాటు గురించి చెబుతుంది."
    ))

    # Q106: Comptroller & Auditor General
    qs.append(make_q(
        106, "Indian Polity - Constitutional Bodies",
        "Consider the following statements regarding the Comptroller and Auditor General of India (CAG):\n\nStatement I: The CAG is appointed by the President by warrant under his hand and seal and can be removed only on grounds and in manner similar to a Judge of the Supreme Court.\nStatement II: The audit reports of the CAG relating to the accounts of the Union are submitted directly to the Public Accounts Committee of Parliament.\n\nWhich of the statements given above is/are correct?",
        "భారత కంప్ట్రోలర్ అండ్ ఆడిటర్ జనరల్ (CAG) కు సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: కాగ్‌ను రాష్ట్రపతి స్వయంగా సంతకం, ముద్రతో కూడిన వారెంట్ ద్వారా నియమిస్తారు మరియు సుప్రీంకోర్టు న్యాయమూర్తిని తొలగించే పద్ధతిలోనే తొలగించగలరు.\nప్రకటన II: కేంద్ర ప్రభుత్వ ఖాతాలకు సంబంధించిన కాగ్ ఆడిట్ నివేదికలను నేరుగా పార్లమెంటు పబ్లిక్ అకౌంట్స్ కమిటీకి (PAC) సమర్పిస్తారు.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        0,
        "Statement I is correct (Article 148). Statement II is incorrect because under Article 151, the CAG submits audit reports to the President of India, who causes them to be laid before each House of Parliament, after which the Public Accounts Committee examines them.",
        "ప్రకటన I సరైనది. ప్రకటన II తప్పు, ఎందుకంటే ఆర్టికల్ 151 ప్రకారం కాగ్ తన నివేదికలను రాష్ట్రపతికి సమర్పిస్తారు, రాష్ట్రపతి వాటిని పార్లమెంటు ఉభయ సభల ముందు ఉంచుతారు. ఆ తర్వాతే PAC పరిశీలిస్తుంది."
    ))

    # Q107: Pardoning Power of President & Governor
    qs.append(make_q(
        107, "Indian Polity - Executive Powers",
        "In which of the following aspects does the pardoning power of the President under Article 72 differ fundamentally from that of the Governor under Article 161 of the Constitution?",
        "ఆర్టికల్ 72 ప్రకారం రాష్ట్రపతికి ఉన్న క్షమాభిక్ష అధికారానికి, ఆర్టికల్ 161 ప్రకారం గవర్నర్‌కు ఉన్న క్షమాభిక్ష అధికారానికి మధ్య గల ప్రాథమిక వ్యత్యాసం ఏమిటి?",
        ["The Governor cannot commute a sentence of imprisonment, whereas the President can", "The Governor has no power to pardon a sentence of death, which is an exclusive power of the President", "The President's pardoning power is subject to judicial review, while the Governor's is completely immune", "The Governor cannot remit sentences under State laws"],
        ["గవర్నర్ జైలు శిక్షను మార్చలేరు, కానీ రాష్ట్రపతి మార్చగలరు", "గవర్నర్‌కు మరణశిక్షను రద్దు చేసే (క్షమాభిక్ష పెట్టే) అధికారం లేదు, ఇది రాష్ట్రపతికి మాత్రమే ఉన్న ప్రత్యేక అధికారం", "రాష్ట్రపతి క్షమాభిక్ష న్యాయ సమీక్షకు లోబడి ఉంటుంది, గవర్నర్‌ది కాదు", "రాష్ట్ర చట్టాల కింద గవర్నర్ శిక్షను తగ్గించలేరు"],
        1,
        "Under Article 72, the President has the exclusive power to pardon death sentences and sentences inflicted by a Court Martial. A Governor under Article 161 cannot grant pardon in case of a death sentence (though he can suspend, remit, or commute it).",
        "రాష్ట్రపతికి మాత్రమే మరణశిక్షను పూర్తిగా క్షమించే (Pardon) అధికారం ఉంది. గవర్నర్‌కు మరణశిక్షను క్షమించే అధికారం లేదు."
    ))

    # Q108: Money Bill
    qs.append(make_q(
        108, "Indian Polity - Parliament & Money Bill",
        "Consider the following statements regarding a Money Bill under Article 110 of the Indian Constitution:\n\nStatement I: A Money Bill can only be introduced in the Lok Sabha on the recommendation of the President.\nStatement II: If the Rajya Sabha does not return the Money Bill within 14 days, it is deemed to have been passed by both Houses in the form it was passed by the Lok Sabha.\n\nWhich of the statements given above is/are correct?",
        "భారత రాజ్యాంగంలోని ఆర్టికల్ 110 ప్రకారం ద్రవ్య బిల్లుకు (Money Bill) సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: ద్రవ్య బిల్లును రాష్ట్రపతి సిఫార్సుపై మాత్రమే లోక్‌సభలో ప్రవేశపెట్టాలి.\nప్రకటన II: రాజ్యసభ ద్రవ్య బిల్లును 14 రోజుల్లోగా తిరిగి పంపకపోతే, లోక్‌సభ ఆమోదించిన రూపంలోనే ఉభయ సభలు ఆమోదించినట్లుగా పరిగణించబడుతుంది.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏదీ సరైనది కాదు"],
        2,
        "Both statements are correct. Money Bills require presidential recommendation, can only originate in Lok Sabha, and the Rajya Sabha has strictly limited powers with a 14-day return deadline (Article 109).",
        "రెండు ప్రకటనలు సరైనవి. ద్రవ్య బిల్లులు లోక్‌సభలో మాత్రమే ప్రవేశపెట్టబడతాయి మరియు రాజ్యసభకు 14 రోజుల సమయం మాత్రమే ఉంటుంది."
    ))

    # Q109: Panchayati Raj & PESA 1996
    qs.append(make_q(
        109, "Indian Polity - Local Governance & PESA",
        "Under the Provisions of the Panchayats (Extension to the Scheduled Areas) Act, 1996 (PESA), which body is endowed with mandatory ownership of Minor Forest Produce (MFP) and the power to enforce prohibition or regulation of intoxicants?",
        "పంచాయితీల (షెడ్యూల్డ్ ప్రాంతాలకు విస్తరణ) చట్టం, 1996 (PESA) కింద, అటవీ లఘు ఉత్పత్తులపై (Minor Forest Produce) యాజమాన్యం మరియు మద్యపాన నిషేధాన్ని అమలు చేసే ప్రత్యేక అధికారం ఏ సంస్థకు కల్పించబడింది?",
        ["Gram Sabha", "Zilla Parishad", "District Collector", "Tribal Advisory Council"],
        ["గ్రామ సభ (Gram Sabha)", "జిల్లా పరిషత్", "జిల్లా కలెక్టర్", "గిరిజన సలహా మండలి"],
        0,
        "PESA Act 1996 specifically empowers the Gram Sabha at the village level with ownership of minor forest produce, approval of plans, and power to enforce prohibition of intoxicants in Fifth Schedule areas.",
        "PESA చట్టం 1996 ప్రకారం 5వ షెడ్యూల్ ప్రాంతాలలో గ్రామసభకు అటవీ లఘు ఉత్పత్తుల యాజమాన్యం మరియు మద్యపాన నియంత్రణపై చట్టబద్ధ అధికారాలు ఉన్నాయి."
    ))

    # Q110: Anti-Defection Law
    qs.append(make_q(
        110, "Indian Polity - Anti-Defection Law",
        "Under the Tenth Schedule of the Indian Constitution, as amended by the 91st Constitutional Amendment Act, 2003, what is the minimum proportion of members of a legislature party required to merge with another political party to avoid disqualification on ground of defection?",
        "91వ రాజ్యాంగ సవరణ చట్టం, 2003 ప్రకారం 10వ షెడ్యూల్ కింద ఫిరాయింపుల నిరోధక చట్టం నుండి మినహాయింపు పొందడానికి ఒక పార్టీకి చెందిన ఎంతమంది శాసనసభ్యులు మరొక పార్టీలో విలీనం కావాలి?",
        ["At least one-third (1/3rd)", "At least one-half (1/2)", "At least two-thirds (2/3rds)", "At least three-fourths (3/4ths)"],
        ["కనీసం మూడింట ఒక వంతు (1/3rd)", "కనీసం సగం మంది (1/2)", "కనీసం మూడింట రెండు వంతులు (2/3rds)", "కనీసం నాల్గింట మూడు వంతులు (3/4ths)"],
        2,
        "The 91st Amendment deleted the 1/3rd split exemption, mandating that at least two-thirds (2/3rds) of the members of a legislature party must agree to a merger to be exempt from disqualification.",
        "91వ సవరణ ద్వారా చీలిక నిబంధనను తొలగించి, కనీసం 2/3 వంతు మంది సభ్యులు ఆమోదిస్తేనే పార్టీ విలీనంగా పరిగణించి అనర్హత నుండి మినహాయింపు ఇస్తారు."
    ))

    # Q111: Emergency Provisions
    qs.append(make_q(
        111, "Indian Polity - Emergency Provisions",
        "A Proclamation of National Emergency under Article 352 must be approved by both Houses of Parliament within what time period from its issue, and by what type of majority?",
        "ఆర్టికల్ 352 ప్రకారం రాష్ట్రపతి విధించిన జాతీయ అత్యవసర పరిస్థితి ప్రకటనను పార్లమెంటు ఉభయ సభలు ఎంత కాల వ్యవధిలో మరియు ఏ రకమైన మెజారిటీతో ఆమోదించాలి?",
        ["Within 1 month by a Special Majority of both Houses", "Within 2 months by a Simple Majority of both Houses", "Within 14 days by a Simple Majority of Lok Sabha only", "Within 6 months by a Special Majority"],
        ["1 నెల లోపల ఉభయ సభల ప్రత్యేక మెజారిటీతో", "2 నెలల లోపల ఉభయ సభల సాధారణ మెజారిటీతో", "14 రోజుల లోపల లోక్‌సభ సాధారణ మెజారిటీతో", "6 నెలల లోపల ప్రత్యేక మెజారిటీతో"],
        0,
        "By the 44th Constitutional Amendment Act, 1978, a proclamation of emergency must be approved by both Houses within 1 month (reduced from 2 months) by a Special Majority (majority of total membership and not less than 2/3rds of members present and voting).",
        "44వ రాజ్యాంగ సవరణ ప్రకారం జాతీయ అత్యవసర పరిస్థితిని 1 నెలలోగా ఉభయ సభలు ప్రత్యేక మెజారిటీతో ఆమోదించాలి."
    ))

    # Q112: Supreme Court Advisory Jurisdiction
    qs.append(make_q(
        112, "Indian Polity - Judiciary & Jurisdiction",
        "Under Article 143 of the Indian Constitution, the President may seek the advisory opinion of the Supreme Court. Which of the following statements is correct regarding this advisory jurisdiction?",
        "భారత రాజ్యాంగంలోని ఆర్టికల్ 143 ప్రకారం రాష్ట్రపతి సుప్రీంకోర్టు సలహాను కోరవచ్చు. ఈ సలహా పరిధికి సంబంధించి కింది వాటిలో ఏది సరైనది?",
        ["The opinion tendered by the Supreme Court is binding on the President", "The Supreme Court is constitutionally bound to give its opinion on all matters referred to it under Article 143(1)", "The advisory opinion delivered by the Supreme Court is not binding on the President of India", "The President can only refer criminal matters under Article 143"],
        ["సుప్రీంకోర్టు ఇచ్చే సలహా రాష్ట్రపతిని కచ్చితంగా కట్టుబడి ఉండేలా చేస్తుంది", "ఆర్టికల్ 143(1) కింద అడిగిన అన్ని విషయాలపై సుప్రీంకోర్టు సలహా ఇవ్వడం తప్పనిసరి", "సుప్రీంకోర్టు ఇచ్చిన సలహా కేవలం సంప్రదింపు మాత్రమే, ఇది రాష్ట్రపతిపై కట్టుబడి ఉండదు", "ఆర్టికల్ 143 కింద కేవలం క్రిమినల్ వ్యవహారాలను మాత్రమే కోరవచ్చు"],
        2,
        "The opinion rendered by the Supreme Court under Article 143 is only advisory in nature and not binding on the President or the Government.",
        "ఆర్టికల్ 143 ప్రకారం సుప్రీంకోర్టు ఇచ్చే సలహా కేవలం సలహా మాత్రమే, ఇది రాష్ట్రపతిని లేదా ప్రభుత్వాన్ని కట్టుబడి ఉండేలా చేయదు."
    ))

    # Q113: Basic Structure Doctrine
    qs.append(make_q(
        113, "Indian Polity - Constitutional Landmark Judgments",
        "In which landmark case did the Supreme Court of India formulate the historic 'Basic Structure Doctrine', ruling that Parliament's constituent power under Article 368 cannot alter the fundamental framework of the Constitution?",
        "రాజ్యాంగంలోని ఆర్టికల్ 368 ప్రకారం పార్లమెంటుకు గల రాజ్యాంగ సవరణ అధికారం రాజ్యాంగ 'మౌలిక స్వరూపాన్ని' మార్చలేదని సుప్రీంకోర్టు ఏ చారిత్రాత్మక తీర్పులో పేర్కొంది?",
        ["Golaknath v. State of Punjab (1967)", "Kesavananda Bharati v. State of Kerala (1973)", "Minerva Mills v. Union of India (1980)", "Maneka Gandhi v. Union of India (1978)"],
        ["గోలక్‌నాథ్ వర్సెస్ పంజాబ్ రాష్ట్రం (1967)", "కేశవానంద భారతి వర్సెస్ కేరళ రాష్ట్రం (1973)", "మినర్వా మిల్స్ వర్సెస్ యూనియన్ ఆఫ్ ఇండియా (1980)", "మేనకా గాంధీ వర్సెస్ యూనియన్ ఆఫ్ ఇండియా (1978)"],
        1,
        "On April 24, 1973, a 13-judge constitutional bench ruled in Kesavananda Bharati v. State of Kerala that Parliament cannot alter the 'Basic Structure' of the Indian Constitution.",
        "1973 ఏప్రిల్ 24న కేశవానంద భారతి కేసులో 13 మంది న్యాయమూర్తుల ధర్మాసనం 'మౌలిక స్వరూప సిద్ధాంతాన్ని' (Basic Structure Doctrine) ప్రతిపాదించింది."
    ))

    # Q114: Inter-State Council
    qs.append(make_q(
        114, "Indian Polity - Centre-State Relations",
        "Who serves as the ex-officio Chairman of the Inter-State Council established under Article 263 of the Indian Constitution?",
        "భారత రాజ్యాంగంలోని ఆర్టికల్ 263 కింద ఏర్పాటు చేయబడిన అంతర్-రాష్ట్ర మండలికి (Inter-State Council) ఎక్స్-అఫీషియో ఛైర్మన్‌గా ఎవరు వ్యవహరిస్తారు?",
        ["President of India", "Prime Minister of India", "Union Home Minister", "Chief Justice of India"],
        ["భారత రాష్ట్రపతి", "భారత ప్రధాన మంత్రి", "కేంద్ర హోం మంత్రి", "భారత ప్రధాన న్యాయమూర్తి"],
        1,
        "Under Article 263 and the Presidential Order establishing it in 1990 based on Sarkaria Commission recommendations, the Prime Minister is the Chairman of the Inter-State Council.",
        "సర్కారియా కమిషన్ సిఫార్సుల మేరకు ఏర్పాటైన అంతర్-రాష్ట్ర మండలికి భారత ప్రధానమంత్రి ఛైర్మన్‌గా వ్యవహరిస్తారు."
    ))

    # Q115: Constitutional vs Statutory Bodies
    qs.append(make_q(
        115, "Indian Polity - Institutional Framework",
        "Which of the following bodies in India is a CONSTITUTIONAL body mentioned explicitly in the Constitution, and NOT merely a statutory body created by an Act of Parliament?",
        "కింది సంస్థలలో ఏది రాజ్యాంగంలో స్పష్టంగా పేర్కొనబడిన రాజ్యాంగబద్ధమైన సంస్థ (Constitutional Body)?",
        ["National Human Rights Commission (NHRC)", "National Commission for Scheduled Castes (NCSC)", "Central Information Commission (CIC)", "Central Vigilance Commission (CVC)"],
        ["జాతీయ మానవ హక్కుల కమిషన్ (NHRC)", "జాతీయ షెడ్యూల్డ్ కులాల కమిషన్ (NCSC)", "కేంద్ర సమాచార కమిషన్ (CIC)", "కేంద్ర విజిలెన్స్ కమిషన్ (CVC)"],
        1,
        "The National Commission for Scheduled Castes is established directly under Article 338 of the Constitution, making it a Constitutional Body. NHRC, CIC, and CVC were created by Acts of Parliament, making them statutory bodies.",
        "జాతీయ ఎస్సీ కమిషన్ రాజ్యాంగంలోని ఆర్టికల్ 338 కింద ఏర్పాటైన రాజ్యాంగబద్ధ సంస్థ. మిగిలినవి చట్టబద్ధ సంస్థలు (Statutory Bodies)."
    ))

    # Q116: Preamble
    qs.append(make_q(
        116, "Indian Polity - Preamble to the Constitution",
        "Which of the following is the exact sequential order of keywords characterizing the Indian Republic in the Preamble as modified by the 42nd Constitutional Amendment Act, 1976?",
        "42వ రాజ్యాంగ సవరణ చట్టం, 1976 తర్వాత భారత రాజ్యాంగ పీఠికలో (Preamble) భారత గణతంత్ర స్వభావాన్ని సూచించే కీలక పదాల సరైన క్రమం ఏది?",
        ["Sovereign, Democratic, Republic, Socialist, Secular", "Sovereign, Socialist, Secular, Democratic, Republic", "Secular, Socialist, Sovereign, Democratic, Republic", "Sovereign, Socialist, Democratic, Secular, Republic"],
        ["సర్వసత్తాక, ప్రజాస్వామ్య, గణతంత్ర, సామ్యవాద, లౌకిక", "సర్వసత్తాక, సామ్యవాద, లౌకిక, ప్రజాస్వామ్య, గణతంత్ర", "లౌకిక, సామ్యవాద, సర్వసత్తాక, ప్రజాస్వామ్య, గణతంత్ర", "సర్వసత్తాక, సామ్యవాద, ప్రజాస్వామ్య, లౌకిక, గణతంత్ర"],
        1,
        "The Preamble declares India to be a 'SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC'. The words 'Socialist', 'Secular', and 'Integrity' were added by the 42nd Amendment.",
        "సరైన క్రమం: సర్వసత్తాక (Sovereign), సామ్యవాద (Socialist), లౌకిక (Secular), ప్రజాస్వామ్య (Democratic), గణతంత్ర (Republic)."
    ))

    # =========================================================================
    # TELANGANA MOVEMENT & STATEHOOD HISTORY (117 - 136: 20 Questions)
    # =========================================================================

    # Q117: 1919 Nizam Farman
    qs.append(make_q(
        117, "Telangana Movement - Mulki Rules Origins",
        "In 1919, the VII Nizam of Hyderabad, Mir Osman Ali Khan, issued a historic Royal Farman establishing the Mulki Rules. What was the minimum period of continuous residence required in Hyderabad State to be classified as a 'Mulki' under this Farman?",
        "1919లో హైదరాబాద్ ఏడవ నిజాం మీర్ ఉస్మాన్ అలీ ఖాన్ ముల్కీ నిబంధనలపై చారిత్రాత్మక ఫర్మానా జారీ చేశారు. ఈ ఫర్మానా ప్రకారం ముల్కీగా గుర్తింపు పొందడానికి హైదరాబాద్ రాజ్యంలో కనీసం ఎన్ని సంవత్సరాల నిరంతర నివాసం అవసరం?",
        ["10 years", "12 years", "15 years", "20 years"],
        ["10 సంవత్సరాలు", "12 సంవత్సరాలు", "15 సంవత్సరాలు", "20 సంవత్సరాలు"],
        2,
        "The 1919 Royal Farman defined a Mulki as a person who had resided continuously in Hyderabad State for not less than 15 years and abandoned any intention to return to their place of origin.",
        "1919 నిజాం ఫర్మానా ప్రకారం హైదరాబాద్ రాజ్యంలో కనీసం 15 సంవత్సరాలు నిరంతరాయంగా నివసించిన వారే ముల్కీలు."
    ))

    # Q118: 1952 City College Firing
    qs.append(make_q(
        118, "Telangana Movement - 1952 Non-Mulki Agitation",
        "During the 1952 Non-Mulki agitation, police opened fire on student demonstrators near City College, Hyderabad on September 3-4, 1952. Which judicial commission was appointed to inquire into this police firing?",
        "1952 నాన్-ముల్కీ ఉద్యమంలో భాగంగా సెప్టెంబర్ 3-4 తేదీలలో హైదరాబాద్ సిటీ కాలేజీ సమీపంలో విద్యార్థులపై జరిగిన పోలీస్ కాల్పులపై విచారణ జరిపేందుకు నియమించబడిన న్యాయ కమిషన్ ఏది?",
        ["Justice Pingali Jaganmohan Reddy Commission", "Justice K.V. Bhargava Commission", "Justice J.M. Girglani Commission", "Justice Wanchoo Committee"],
        ["జస్టిస్ పింగళి జగన్మోహన్ రెడ్డి కమిషన్", "జస్టిస్ కె.వి. భార్గవ కమిషన్", "జస్టిస్ జె.ఎం. గిర్‌గ్లానీ కమిషన్", "జస్టిస్ వాంచూ కమిటీ"],
        0,
        "Chief Minister Burgula Ramakrishna Rao appointed the Justice Pingali Jaganmohan Reddy Commission to investigate the City College police firing incident of September 1952.",
        "1952 సిటీ కాలేజ్ కాల్పుల సంఘటనపై విచారణ జరిపేందుకు బూర్గుల రామకృష్ణారావు ప్రభుత్వం 'జస్టిస్ పింగళి జగన్మోహన్ రెడ్డి కమిషన్'ను నియమించింది."
    ))

    # Q119: Gentlemen's Agreement 1956
    qs.append(make_q(
        119, "Telangana Movement - Gentlemen's Agreement 1956",
        "Consider the following statements regarding the Gentlemen's Agreement signed on February 20, 1956 at Hyderabad House in New Delhi:\n\nStatement I: It provided that if the Chief Minister was from Andhra, the Deputy Chief Minister should be from Telangana and vice versa.\nStatement II: It mandated that expenditure on administration should be borne proportionately and the surplus revenue of Telangana should be spent exclusively on Telangana development.\n\nWhich of the statements given above is/are correct?",
        "1956 ఫిబ్రవరి 20న న్యూఢిల్లీలోని హైదరాబాద్ హౌస్‌లో కుదిరిన పెద్దమనుషుల ఒప్పందానికి (Gentlemen's Agreement) సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: ముఖ్యమంత్రి ఆంధ్ర ప్రాంతం నుండి ఉంటే, ఉప ముఖ్యమంత్రి తెలంగాణ ప్రాంతం నుండి ఉండాలి మరియు దీనికి విరుద్ధంగా ఉండాలి.\nప్రకటన II: పరిపాలనా వ్యయాన్ని దామాషా పద్ధతిలో భరించాలి మరియు తెలంగాణ మిగులు బడ్జెట్‌ను కేవలం తెలంగాణ ప్రాంత అభివృద్ధికి మాత్రమే వెచ్చించాలి.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are correct clauses of the 14-point Gentlemen's Agreement signed by 4 leaders of Andhra (B. Gopala Reddy, N. Sanjiva Reddy, G. Latchanna, A. Satyanarayana Raju) and 4 leaders of Telangana (B. Ramakrishna Rao, K.V. Ranga Reddy, M. Chenna Reddy, J.V. Narsing Rao).",
        "రెండు ప్రకటనలు సరైనవి. పెద్దమనుషుల ఒప్పందంలోని 14 అంశాలలో సీఎం/డిప్యూటీ సీఎం పదవుల పంపకం మరియు మిగులు నిధుల వినియోగం ముఖ్యమైన నిబంధనలు."
    ))

    # Q120: 1969 Agitation Palvancha
    qs.append(make_q(
        120, "Telangana Movement - 1969 Agitation",
        "The historic 1969 Telangana Agitation gained mass momentum in January 1969 when a student leader commenced an indefinite hunger strike at Palvancha (KTPS) demanding the implementation of safeguards for Telangana. Who was this student leader?",
        "1969 తెలంగాణ ఉద్యమం జనవరి 1969లో పాల్వంచ (KTPS) వద్ద ఒక విద్యార్థి నాయకుడు తెలంగాణ రక్షణలను అమలు చేయాలని నిరాహార దీక్ష ప్రారంభించడంతో తీవ్రరూపం దాల్చింది. ఆ విద్యార్థి నాయకుడు ఎవరు?",
        ["Kollisetty Ramadasu", "Annathula Ravindranath", "Mallikarjun", "Madan Mohan"],
        ["కొల్లిశెట్టి రామదాసు", "అన్నాబత్తుల రవీంద్రనాథ్", "మల్లికార్జున్", "మదన్ మోహన్"],
        1,
        "On January 8, 1969, Annathula Ravindranath, a student of Palvancha, began an indefinite hunger strike demanding the implementation of Gentlemen's Agreement safeguards and repatriation of non-locals.",
        "1969 జనవరి 8న పాల్వంచలో అన్నాబత్తుల రవీంద్రనాథ్ చేపట్టిన ఆమరణ నిరాహార దీక్ష 1969 ఉద్యమానికి నాంది పలికింది."
    ))

    # Q121: Eight-Point Formula 1969
    qs.append(make_q(
        121, "Telangana Movement - Political Formulas",
        "On April 11, 1969, Prime Minister Indira Gandhi announced the 'Eight-Point Formula' in the Lok Sabha to address grievances of Telangana. Which committee was constituted under this formula to determine the quantum of surplus revenues of Telangana?",
        "1969 ఏప్రిల్ 11న ప్రధానమంత్రి ఇందిరాగాంధీ లోక్‌సభలో 'ఎనిమిది సూత్రాల పథకాన్ని' (Eight-Point Formula) ప్రకటించారు. తెలంగాణ మిగులు నిధులను లెక్కించేందుకు ఈ పథకం కింద ఏర్పాటు చేయబడిన కమిటీ ఏది?",
        ["Justice Vashishtha Bhargava Committee", "Kumar Lalit Committee", "Wanchoo Committee", "Justice J.M. Girglani Committee"],
        ["జస్టిస్ వశిష్ట భార్గవ కమిటీ", "కుమార్ లలిత్ కమిటీ", "వాంచూ కమిటీ", "జస్టిస్ జె.ఎం. గిర్‌గ్లానీ కమిటీ"],
        0,
        "Under the Eight-Point Formula, the Justice Vashishtha Bhargava Committee was set up to determine Telangana surplus funds (following the preliminary report of Kumar Lalit).",
        "ఎనిమిది సూత్రాల పథకం కింద తెలంగాణ మిగులు నిధులను లెక్కించడానికి 'జస్టిస్ వశిష్ట భార్గవ కమిటీ'ని నియమించారు."
    ))

    # Q122: Six-Point Formula 1973
    qs.append(make_q(
        122, "Telangana Movement - Six-Point Formula & 371D",
        "The Six-Point Formula of September 1973 was incorporated into the Constitution of India through which Constitutional Amendment Act, creating Article 371D?",
        "1973 సెప్టెంబర్ నాటి ఆరు సూత్రాల పథకానికి రాజ్యాంగ భద్రత కల్పిస్తూ ఆర్టికల్ 371D ని చేర్చిన రాజ్యాంగ సవరణ చట్టం ఏది?",
        ["31st Constitutional Amendment Act, 1973", "32nd Constitutional Amendment Act, 1973", "36th Constitutional Amendment Act, 1975", "42nd Constitutional Amendment Act, 1976"],
        ["31వ రాజ్యాంగ సవరణ చట్టం, 1973", "32వ రాజ్యాంగ సవరణ చట్టం, 1973", "36వ రాజ్యాంగ సవరణ చట్టం, 1975", "42వ రాజ్యాంగ సవరణ చట్టం, 1976"],
        1,
        "The 32nd Constitutional Amendment Act, 1973 inserted Article 371D and 371E, giving effect to the Six-Point Formula and dividing AP into zones for education and public employment.",
        "32వ రాజ్యాంగ సవరణ చట్టం, 1973 ద్వారా ఆర్టికల్ 371D ని చేర్చి ఆరు సూత్రాల పథకానికి చట్టబద్ధత కల్పించారు."
    ))

    # Q123: G.O. 610 & Girglani
    qs.append(make_q(
        123, "Telangana Movement - G.O. 610",
        "Government Order (G.O.) Ms. No. 610 was issued on December 30, 1985 by the Government of Andhra Pradesh headed by N.T. Rama Rao. What was its primary objective?",
        "1985 డిసెంబర్ 30న ఆంధ్రప్రదేశ్ ప్రభుత్వం జారీ చేసిన G.O. Ms. No. 610 యొక్క ప్రధాన ఉద్దేశ్యం ఏమిటి?",
        ["Bifurcation of the state electricity board", "Repatriation of all non-local employees illegally appointed in Telangana zones back to their parent zones by March 31, 1986", "Implementation of 33% reservation for women in police recruitment", "Establishment of Telangana Regional Development Board"],
        ["రాష్ట్ర విద్యుత్ బోర్డు విభజన", "తెలంగాణ జోన్లలో నిబంధనలకు విరుద్ధంగా నియమితులైన స్థానికేతరులను 1986 మార్చి 31 లోగా వారి సొంత ప్రాంతాలకు తిరిగి పంపడం", "పోలీస్ రిక్రూట్‌మెంట్‌లో మహిళలకు 33% రిజర్వేషన్", "తెలంగాణ ప్రాంతీయ అభివృద్ధి మండలి ఏర్పాటు"],
        1,
        "G.O. 610 was issued to rectify violations of the Presidential Order 1975 in Zones V and VI (Telangana) and repatriate all non-locals by March 31, 1986. Later, the J.M. Girglani Commission was appointed in 2001 to investigate its non-implementation.",
        "జీవో 610 ప్రకారం జోన్ 5 మరియు 6 లలో నిబంధనలకు విరుద్ధంగా ఉద్యోగాలు పొందిన స్థానికేతరులను వెనక్కి పంపించాలని నిర్దేశించారు."
    ))

    # Q124: Formation of TRS 2001
    qs.append(make_q(
        124, "Telangana Movement - Revival of Movement",
        "Kalvakuntla Chandrashekar Rao (KCR) resigned from the post of Deputy Speaker of the AP Legislative Assembly and founded the Telangana Rashtra Samithi (TRS) on April 27, 2001 at which historic venue in Hyderabad?",
        "కల్వకుంట్ల చంద్రశేఖర రావు (KCR) ఆంధ్రప్రదేశ్ శాసనసభ డిప్యూటీ స్పీకర్ పదవికి రాజీనామా చేసి, 2001 ఏప్రిల్ 27న హైదరాబాద్‌లోని ఏ వేదికపై తెలంగాణ రాష్ట్ర సమితి (TRS) పార్టీని స్థాపించారు?",
        ["Nizam College Grounds", "Jala Drushyam", "Indira Park", "Secunderabad Parade Grounds"],
        ["నిజాం కాలేజ్ గ్రౌండ్స్", "జలదృశ్యం (Jala Drushyam)", "ఇందిరా పార్క్", "సికింద్రాబాద్ పరేడ్ గ్రౌండ్స్"],
        1,
        "KCR launched TRS on April 27, 2001 at Jala Drushyam, the residence of Konda Lakshman Bapuji overlooking Hussainsagar.",
        "కొండా లక్ష్మణ్ బాపూజీ నివాసమైన 'జలదృశ్యం' వద్ద 2001 ఏప్రిల్ 27న కేసీఆర్ టీఆర్‌ఎస్ పార్టీని స్థాపించారు."
    ))

    # Q125: Million March 2011
    qs.append(make_q(
        125, "Telangana Movement - Mass Struggles",
        "The historic 'Million March' organised by the Telangana Joint Action Committee (TJAC) in defiance of heavy police barricades and curfew took place on which date at Tank Bund, Hyderabad?",
        "తెలంగాణ జాయింట్ యాక్షన్ కమిటీ (TJAC) ఆధ్వర్యంలో వేలాది మంది ప్రజలు నిర్బంధాలను ఛేదించుకుని హైదరాబాద్ ట్యాంక్ బండ్‌పై నిర్వహించిన చారిత్రాత్మక 'మిలియన్ మార్చ్' ఏ తేదీన జరిగింది?",
        ["December 9, 2009", "March 10, 2011", "September 13, 2011", "March 23, 2013"],
        ["డిసెంబర్ 9, 2009", "మార్చి 10, 2011", "సెప్టెంబర్ 13, 2011", "మార్చి 23, 2013"],
        1,
        "The Million March was held on March 10, 2011 on Tank Bund, modeled after Egypt's Tahrir Square protests.",
        "ఈజిప్టు తహ్రీర్ స్క్వేర్ తరహాలో 2011 మార్చి 10న ట్యాంక్ బండ్‌పై చారిత్రాత్మక 'మిలియన్ మార్చ్' జరిగింది."
    ))

    # Q126: Sakala Janula Samme
    qs.append(make_q(
        126, "Telangana Movement - General Strike",
        "How many days did the historic 'Sakala Janula Samme' (All People's Strike) last from September 13 to October 24, 2011, paralyzing administration, schools, RTC buses, and Singareni coal production?",
        "2011 సెప్టెంబర్ 13 నుండి అక్టోబర్ 24 వరకు పాలన, పాఠశాలలు, ఆర్టీసీ బస్సులు మరియు సింగరేణి బొగ్గు ఉత్పత్తిని స్తంభింపజేస్తూ సాగిన చారిత్రాత్మక 'సకల జనుల సమ్మె' ఎన్ని రోజుల పాటు కొనసాగింది?",
        ["28 days", "36 days", "42 days", "48 days"],
        ["28 రోజులు", "36 రోజులు", "42 రోజులు", "48 రోజులు"],
        2,
        "The Sakala Janula Samme lasted for 42 consecutive days, proving to be one of the longest and largest general strikes in post-independence India.",
        "సకల జనుల సమ్మె వరుసగా 42 రోజుల పాటు కొనసాగి భారత ప్రజా ఉద్యమాలలో అరుదైన మైలురాయిగా నిలిచింది."
    ))

    # Q127: Srikrishna Committee 2010
    qs.append(make_q(
        127, "Telangana Movement - Srikrishna Committee",
        "The Justice B.N. Srikrishna Committee, appointed by the Union Government in February 2010 to look into the demand for Telangana statehood, recommended which option as the most workable in its final report?",
        "తెలంగాణ డిమాండ్‌పై కేంద్ర ప్రభుత్వం నియమించిన జస్టిస్ బి.ఎన్. శ్రీకృష్ణ కమిటీ తన నివేదికలో ఏ అవకాశాన్ని (Option) అత్యంత ఆమోదయోగ్యమైనదిగా సిఫార్సు చేసింది?",
        ["Option 1: Maintaining the status quo", "Option 5: Bifurcation of the State into Telangana and Seemandhra as per existing boundaries", "Option 6: Keeping the State united and providing constitutional statutory measures for Telangana socio-economic empowerment through a Statutory Regional Council", "Option 4: Division into Rayala-Telangana and Coastal Andhra"],
        ["ఆప్షన్ 1: యథాతథ స్థితిని కొనసాగించడం", "ఆప్షన్ 5: రాష్ట్రాన్ని తెలంగాణ మరియు సీమాంధ్రగా విభజించడం", "ఆప్షన్ 6: రాష్ట్రాన్ని సమైక్యంగా ఉంచుతూనే చట్టబద్ధ ప్రాంతీయ మండలి ద్వారా తెలంగాణకు సాధికారత కల్పించడం", "ఆప్షన్ 4: రాయల-తెలంగాణ మరియు కోస్తాంధ్రగా విభజన"],
        2,
        "The Srikrishna Committee formulated 6 options. Option 5 recommended bifurcation into two states, but the committee favored Option 6 (keeping state united with a statutory regional empowerment council) as the best workable option, which was rejected by the people of Telangana.",
        "శ్రీకృష్ణ కమిటీ 6 ఆప్షన్లు ఇచ్చింది. విభజనను ఆప్షన్ 5 లో పేర్కొన్నప్పటికీ, రాష్ట్రాన్ని సమైక్యంగా ఉంచి ప్రాంతీయ మండలి ఏర్పాటు చేయాలని ఆప్షన్ 6 ను మొదటి ప్రాధాన్యతగా సిఫార్సు చేసింది."
    ))

    # Q128: AP Reorganisation Act 2014 Section 5
    qs.append(make_q(
        128, "Telangana Movement - AP Reorganisation Act 2014",
        "Under Section 5 of the Andhra Pradesh Reorganisation Act, 2014, for what maximum period was the city of Hyderabad designated as the common capital for both the State of Telangana and the State of Andhra Pradesh?",
        "ఆంధ్రప్రదేశ్ పునర్వ్యవస్థీకరణ చట్టం, 2014 లోని సెక్షన్ 5 ప్రకారం, హైదరాబాద్ నగరం తెలంగాణ మరియు ఆంధ్రప్రదేశ్ ఉమ్మడి రాజధానిగా గరిష్టంగా ఎన్ని సంవత్సరాలు ఉంటుందని పేర్కొన్నారు?",
        ["5 years", "10 years", "12 years", "15 years"],
        ["5 సంవత్సరాలు", "10 సంవత్సరాలు", "12 సంవత్సరాలు", "15 సంవత్సరాలు"],
        1,
        "Section 5(1) provided that on and from the appointed day (June 2, 2014), Hyderabad shall be the common capital of the State of Telangana and the State of Andhra Pradesh for such period not exceeding ten years (until June 2, 2024).",
        "సెక్షన్ 5 ప్రకారం 2014 జూన్ 2 నుండి గరిష్టంగా 10 సంవత్సరాల పాటు హైదరాబాద్ ఉమ్మడి రాజధానిగా ఉంటుంది."
    ))

    # Q129: Telangana Martyrs Memorial
    qs.append(make_q(
        129, "Telangana Movement - Cultural Symbols",
        "The famous Telangana Martyrs Memorial (Amaraveerula Stupam) erected at Gun Park opposite the State Legislative Assembly in memory of the 1969 martyrs was sculpted by which renowned artist?",
        "1969 అమరవీరుల జ్ఞాపకార్థం అసెంబ్లీ ఎదురుగా ఉన్న గన్ పార్క్ వద్ద ఏర్పాటు చేసిన తెలంగాణ అమరవీరుల స్తూపాన్ని తీర్చిదిద్దిన ప్రముఖ శిల్పి ఎవరు?",
        ["Aekka Yadagiri Rao", "B. Vaikuntam", "Kapu Rajaiah", "Laxma Goud"],
        ["ఎక్కా యాదగిరి రావు (Aekka Yadagiri Rao)", "బి. వైకుంఠం", "కాపు రాజయ్య", "లక్ష్మా గౌడ్"],
        0,
        "The Amaraveerula Stupam at Gun Park was sculpted by renowned Telangana artist and sculptor Aekka Yadagiri Rao.",
        "గన్ పార్క్ లోని అమరవీరుల స్తూపాన్ని ప్రముఖ శిల్పి ఎక్కా యాదగిరి రావు రూపొందించారు."
    ))

    # Q130: Doddi Komaraiah & Armed Struggle
    qs.append(make_q(
        130, "Telangana History - Armed Struggle 1946-51",
        "The historic Telangana Armed Struggle (1946–1951) was sparked by the martyrdom of peasant leader Doddi Komaraiah on July 4, 1946. At which village in Jangaon did this fateful incident occur?",
        "1946 జూలై 4న రైతు నాయకుడు దొడ్డి కొమరయ్య అమరత్వంతో చారిత్రాత్మక తెలంగాణ సాయుధ పోరాటం (1946-51) ప్రారంభమైంది. జనగామ తాలూకాలోని ఏ గ్రామంలో ఈ సంఘటన జరిగింది?",
        ["Kadavendi", "Palakurthi", "Akunoor", "Machireddypally"],
        ["కడవెండి (Kadavendi)", "పాలకుర్తి", "ఆకునూరు", "మచిరెడ్డిపల్లి"],
        0,
        "Doddi Komaraiah was shot dead on July 4, 1946 at Kadavendi village when the rowdies of Visnoor Deshmukh Ramachandra Reddy fired upon a peaceful procession.",
        "విస్నూర్ దేశ్‌ముఖ్ రౌడీలు జరిపిన కాల్పుల్లో కడవెండి గ్రామంలో దొడ్డి కొమరయ్య అమరుడయ్యాడు."
    ))

    # Q131: Chakali Ilamma
    qs.append(make_q(
        131, "Telangana History - Peasant Resistance",
        "Chakali Ilamma (Chityala Ilamma) became a legendary symbol of resistance during the Telangana Armed Struggle when she successfully defended her harvested crop against which oppressive feudal landlord?",
        "తెలంగాణ సాయుధ పోరాటంలో చాకలి ఐలమ్మ (చిట్యాల ఐలమ్మ) ఏ భూస్వామికి వ్యతిరేకంగా తన భూమిలోని పంటను ధైర్యంగా కాపాడుకుని ప్రతిఘటనకు ప్రతీకగా నిలిచారు?",
        ["Visnoor Deshmukh Ramachandra Reddy", "Jannepally Pratap Reddy", "Pingle Venkatrama Reddy", "Kalluri Subba Rao"],
        ["విస్నూర్ దేశ్‌ముఖ్ రామచంద్రారెడ్డి", "జన్నేపల్లి ప్రతాప్ రెడ్డి", "పింగళి వెంకట్రామారెడ్డి", "కల్లూరి సుబ్బారావు"],
        0,
        "Chakali Ilamma valiantly fought against the armed goons of Visnoor Deshmukh Ramachandra Reddy and his mother Janamma who attempted to seize her harvested paddy at Palakurthi.",
        "పాలకుర్తిలో విస్నూర్ దేశ్‌ముఖ్ రామచంద్రారెడ్డికి వ్యతిరేకంగా పోరాడి తన పంటను కాపాడుకున్న ధీరవనిత చాకలి ఐలమ్మ."
    ))

    # Q132: Operation Polo 1948
    qs.append(make_q(
        132, "Telangana History - Hyderabad Integration",
        "Operation Polo, the police action launched by the Government of India that led to the accession of Hyderabad State into the Indian Union, took place between which dates in September 1948?",
        "హైదరాబాద్ సంస్థానాన్ని భారత యూనియన్‌లో విలీనం చేయడానికి భారత ప్రభుత్వం చేపట్టిన పోలీస్ చర్య 'ఆపరేషన్ పోలో' 1948 సెప్టెంబర్‌లో ఏ తేదీల మధ్య జరిగింది?",
        ["September 1 to September 5, 1948", "September 13 to September 17, 1948", "September 17 to September 21, 1948", "September 24 to September 28, 1948"],
        ["సెప్టెంబర్ 1 నుండి సెప్టెంబర్ 5, 1948", "సెప్టెంబర్ 13 నుండి సెప్టెంబర్ 17, 1948", "సెప్టెంబర్ 17 నుండి సెప్టెంబర్ 21, 1948", "సెప్టెంబర్ 24 నుండి సెప్టెంబర్ 28, 1948"],
        1,
        "Operation Polo commenced on September 13, 1948 under Major General J.N. Chaudhuri and concluded with the surrender of the Nizam's forces on September 17, 1948.",
        "ఆపరేషన్ పోలో 1948 సెప్టెంబర్ 13న ప్రారంభమై సెప్టెంబర్ 17న నిజాం సైన్యం లొంగుబాటుతో ముగిసింది."
    ))

    # Q133: Ramappa Temple UNESCO
    qs.append(make_q(
        133, "Telangana History - Kakatiya Heritage",
        "Consider the following statements regarding the Ramappa Temple at Palampet in Mulugu district:\n\nStatement I: It was constructed in 1213 CE during the reign of Kakatiya ruler Ganapati Deva by his general Recherla Rudra.\nStatement II: The temple is built using lightweight 'floating bricks' and was inscribed as a UNESCO World Heritage Site in 2021.\n\nWhich of the statements given above is/are correct?",
        "ములుగు జిల్లా పాలంపేటలోని రామప్ప దేవాలయానికి సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: దీనిని కాకతీయ గణపతిదేవుని పాలనా కాలంలో క్రీ.శ. 1213లో సేనాని రేచర్ల రుద్రుడు నిర్మించాడు.\nప్రకటన II: ఈ ఆలయాన్ని నీటిపై తేలియాడే తేలికపాటి ఇటుకలతో నిర్మించారు మరియు 2021లో ఇది యునెస్కో ప్రపంచ వారసత్వ సంపదగా గుర్తింపు పొందింది.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are correct. The Ramalingeswara (Ramappa) Temple was built in 1213 CE by Recherla Rudra during Ganapati Deva's reign and was inscribed on UNESCO's World Heritage list in 2021.",
        "రెండు ప్రకటనలు సరైనవి. రామప్ప ఆలయాన్ని 1213లో రేచర్ల రుద్రుడు నిర్మించాడు మరియు 2021లో యునెస్కో గుర్తింపు పొందింది."
    ))

    # Q134: Qutb Shahi Dynasty Charminar
    qs.append(make_q(
        134, "Telangana History - Qutb Shahi Dynasty",
        "The iconic monument Charminar was built in 1591 CE by which Qutb Shahi Sultan to commemorate the eradication of a devastating plague epidemic in Hyderabad?",
        "హైదరాబాద్‌లో ప్లేగు వ్యాధి నిర్మూలనకు గుర్తుగా 1591లో చార్మినార్‌ను నిర్మించిన కుతుబ్‌షాహీ సుల్తాన్ ఎవరు?",
        ["Sultan Quli Qutb Shah", "Ibrahim Qutb Shah", "Muhammad Quli Qutb Shah", "Abdullah Qutb Shah"],
        ["సుల్తాన్ కులీ కుతుబ్ షా", "ఇబ్రహీం కుతుబ్ షా", "మహ్మద్ కులీ కుతుబ్ షా", "అబ్దుల్లా కుతుబ్ షా"],
        2,
        "Muhammad Quli Qutb Shah, the fifth ruler of the Qutb Shahi dynasty and founder of Hyderabad city, built Charminar in 1591 CE.",
        "హైదరాబాద్ నగర నిర్మాత, ఐదవ కుతుబ్‌షాహీ పాలకుడు మహ్మద్ కులీ కుతుబ్ షా 1591లో చార్మినార్‌ను నిర్మించారు."
    ))

    # Q135: Bathukamma Festival
    qs.append(make_q(
        135, "Telangana Culture - Festivals",
        "The floral festival of Telangana, Bathukamma, is celebrated for 9 days during the Navratri season. What is the name given to the first day and the grand final ninth day of the festival respectively?",
        "తెలంగాణ పూల పండుగ బతుకమ్మ నవరాత్రుల సమయంలో 9 రోజుల పాటు జరుపుకుంటారు. ఆ పండుగలోని మొదటి రోజు మరియు తొమ్మిదవ రోజైన ముగింపు రోజును వరుసగా ఏమని పిలుస్తారు?",
        ["Engili Pula Bathukamma and Saddula Bathukamma", "Boddemma and Engili Pula Bathukamma", "Chinna Bathukamma and Pedda Bathukamma", "Mudda Pula Bathukamma and Bangaru Bathukamma"],
        ["ఎంగిలిపూల బతుకమ్మ మరియు సద్దుల బతుకమ్మ", "బొడ్డెమ్మ మరియు ఎంగిలిపూల బతుకమ్మ", "చిన్న బతుకమ్మ మరియు పెద్ద బతుకమ్మ", "ముద్దపూల బతుకమ్మ మరియు బంగారు బతుకమ్మ"],
        0,
        "The Bathukamma festival begins on Mahalaya Amavasya with 'Engili Pula Bathukamma' and concludes on Durgashtami with the grand 'Saddula Bathukamma'.",
        "బతుకమ్మ మొదటి రోజును 'ఎంగిలిపూల బతుకమ్మ' అని, ఆఖరి 9వ రోజును 'సద్దుల బతుకమ్మ' అని పిలుస్తారు."
    ))

    # Q136: Telangana GI Tags
    qs.append(make_q(
        136, "Telangana Culture - Handicrafts & GI Tags",
        "Match List-I (Telangana GI Product) with List-II (Associated District / Town):\n\nList-I\t\t\t\tList-II\nA. Pochampally Ikat\t\t1. Jogulamba Gadwal\nB. Silver Filigree\t\t2. Yadadri Bhuvanagiri\nC. Telia Rumal\t\t\t3. Karimnagar\nD. Handloom Zari Sarees\t\t4. Nalgonda (Puttapaka)\n\nChoose the correct code:",
        "జాబితా-I (తెలంగాణ జీఐ ట్యాగ్ ఉత్పత్తి) ను జాబితా-II (సంబంధిత జిల్లా / ప్రాంతం) తో జతపరచండి:\n\nజాబితా-I\t\t\t\tజాబితా-II\nA. పోచంపల్లి ఇక్కత్\t\t1. జోగులాంబ గద్వాల\nB. సిల్వర్ ఫిలిగ్రీ\t\t2. యాదాద్రి భువనగిరి\nC. తేలియా రుమాల్\t\t3. కరీంనగర్\nD. జరీ చేనేత చీరలు\t\t4. నల్గొండ (పుట్టపాక)\n\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-2, B-3, C-4, D-1", "A-2, B-1, C-4, D-3", "A-4, B-3, C-2, D-1", "A-3, B-2, C-1, D-4"],
        ["A-2, B-3, C-4, D-1", "A-2, B-1, C-4, D-3", "A-4, B-3, C-2, D-1", "A-3, B-2, C-1, D-4"],
        0,
        "Pochampally Ikat = Yadadri Bhuvanagiri (A-2). Silver Filigree = Karimnagar (B-3). Telia Rumal = Puttapaka, Nalgonda (C-4). Gadwal Zari Sarees = Jogulamba Gadwal (D-1). Code: A-2, B-3, C-4, D-1.",
        "పోచంపల్లి ఇక్కత్ (A-2), సిల్వర్ ఫిలిగ్రీ (B-3), తేలియా రుమాల్ (C-4), గద్వాల చీరలు (D-1). సరైన కోడ్: A-2, B-3, C-4, D-1."
    ))

    # =========================================================================
    # INDIAN HISTORY & NATIONAL MOVEMENT (137 - 150: 14 Questions)
    # =========================================================================

    # Q137: Indus Valley Civilization
    qs.append(make_q(
        137, "Indian History - Indus Valley Civilization",
        "Consider the following statements regarding major Harappan archaeological sites:\n\nStatement I: Lothal in Gujarat possessed an artificial tidal dockyard connected to the Bhogavo river.\nStatement II: Dholavira in the Rann of Kutch is renowned for its sophisticated water reservoir harvesting system and unique three-tier city planning.\n\nWhich of the statements given above is/are correct?",
        "ప్రధాన హరప్పా పురావస్తు ప్రదేశాలకు సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: గుజరాత్‌లోని లోథాల్‌లో భోగావో నదితో అనుసంధానించబడిన కృత్రిమ నౌకాశ్రయం (డాక్‌యార్డ్) ఉంది.\nప్రకటన II: కచ్ ప్రాంతంలోని ధోలవీరా అద్భుతమైన నీటి నిల్వ రిజర్వాయర్ వ్యవస్థకు మరియు మూడు అంచెల నగర నిర్మాణానికి ప్రసిద్ధి చెందింది.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are historically correct. Lothal had the earliest known tidal port/dockyard, and Dholavira is noted for its stone-cut water reservoirs and unique tri-partite division (Citadel, Middle town, Lower town).",
        "రెండు ప్రకటనలు సరైనవి. లోథాల్‌లో ప్రసిద్ధ డాక్‌యార్డ్ ఉంది, ధోలవీరా నీటి సంరక్షణ రిజర్వాయర్లు మరియు మూడు భాగాల నగర నిర్మాణానికి ప్రసిద్ధి."
    ))

    # Q138: Ashokan Rock Edict XIII
    qs.append(make_q(
        138, "Indian History - Mauryan Empire",
        "Which Major Rock Edict of Emperor Ashoka provides an authentic first-hand account of the Kalinga War (261 BCE), the remorse felt by the King, and his subsequent transformation to Dhamma Vijaya?",
        "కళింగ యుద్ధం (క్రీ.పూ. 261), ఆ యుద్ధం వల్ల కలిగిన రక్తపాతానికి చక్రవర్తి అశోకుడు పొందిన పశ్చాత్తాపం మరియు 'ధర్మ విజయ' విధానాన్ని వివరించే అశోకుని ప్రధాన శిలాశాసనం ఏది?",
        ["Major Rock Edict I", "Major Rock Edict V", "Major Rock Edict XIII", "Major Rock Edict VII"],
        ["1వ ప్రధాన శిలాశాసనం", "5వ ప్రధాన శిలాశాసనం", "13వ ప్రధాన శిలాశాసనం (Major Rock Edict XIII)", "7వ ప్రధాన శిలాశాసనం"],
        2,
        "Major Rock Edict XIII gives a vivid description of the Kalinga War, the devastation it caused, and Ashoka's renunciation of conquest by war in favor of conquest by righteousness (Dhamma Vijaya).",
        "అశోకుని 13వ ప్రధాన శిలాశాసనం కళింగ యుద్ధం మరియు యుద్ధ విజయం స్థానంలో ధర్మ విజయాన్ని ఎంచుకున్న వైనాన్ని వివరిస్తుంది."
    ))

    # Q139: Gupta Dynasty
    qs.append(make_q(
        139, "Indian History - Gupta Golden Age",
        "Chinese Buddhist pilgrim Fa-Hien (Faxian) visited India and recorded peaceful administrative and social conditions during the reign of which famous Gupta monarch?",
        "ప్రసిద్ధ చైనా బౌద్ధ యాత్రికుడు ఫాహియాన్ (ఫాక్సియాన్) ఏ గుప్త చక్రవర్తి పాలనా కాలంలో భారతదేశాన్ని సందర్శించి, ఇక్కడి ప్రశాంత పరిపాలనను గ్రంథస్థం చేశాడు?",
        ["Samudragupta", "Chandragupta I", "Chandragupta II (Vikramaditya)", "Skandagupta"],
        ["సముద్రగుప్తుడు", "మొదటి చంద్రగుప్తుడు", "రెండవ చంద్రగుప్తుడు (విక్రమాదిత్య)", "స్కందగుప్తుడు"],
        2,
        "Fa-Hien visited India between 399 and 412 CE during the reign of Chandragupta II Vikramaditya.",
        "ఫాహియాన్ గుప్త చక్రవర్తి రెండవ చంద్రగుప్తుని (విక్రమాదిత్యుడు) కాలంలో భారతదేశాన్ని సందర్శించాడు."
    ))

    # Q140: Delhi Sultanate Alauddin Khilji
    qs.append(make_q(
        140, "Indian History - Delhi Sultanate",
        "Which Sultan of Delhi established strict market price control regulations, set up specialized grain markets called 'Shahna-i-Mandi', and introduced the branding of horses ('Dagh') and descriptive rolls of soldiers ('Chehra')?",
        "మార్కెట్లలో ధరల నియంత్రణ నిబంధనలను ప్రవేశపెట్టి, 'షహనా-ఇ-మండి' మార్కెట్లను ఏర్పాటు చేయడంతో పాటు, గుర్రాలకు ముద్ర వేసే 'దాగ్' మరియు సైనికుల వివరాల నమోదు 'చెహ్రా' పద్ధతులను ప్రారంభించిన ఢిల్లీ సుల్తాన్ ఎవరు?",
        ["Iltutmish", "Balban", "Alauddin Khilji", "Muhammad bin Tughlaq"],
        ["ఇల్తుత్మిష్", "బాల్బన్", "అల్లావుద్దీన్ ఖిల్జీ (Alauddin Khilji)", "మహ్మద్ బిన్ తుగ్లక్"],
        2,
        "Alauddin Khilji introduced comprehensive market control reforms, strict price ceilings monitored by the Shahna-i-Mandi, and the Dagh and Chehra military systems.",
        "అల్లావుద్దీన్ ఖిల్జీ మార్కెట్ సంస్కరణలను, దాగ్ మరియు చెహ్రా సైనిక విధానాలను ప్రవేశపెట్టాడు."
    ))

    # Q141: Mughal Mansabdari System
    qs.append(make_q(
        141, "Indian History - Mughal Administration",
        "Under the Mansabdari system introduced by Mughal Emperor Akbar, what did the numerical ranks 'Zat' and 'Sawar' specifically denote?",
        "మొఘల్ చక్రవర్తి అక్బర్ ప్రవేశపెట్టిన మన్సబ్దారీ విధానంలో 'జాత్' (Zat) మరియు 'సవార్' (Sawar) లు దేనిని సూచిస్తాయి?",
        ["Zat indicated personal status and salary, while Sawar indicated the required cavalry contingent to maintain", "Zat indicated the military rank, while Sawar indicated revenue collected from jagirs", "Zat represented judicial powers, while Sawar represented police powers", "Zat indicated artillery, while Sawar indicated infantry soldiers"],
        ["జాత్ వ్యక్తిగత హోదా మరియు జీతాన్ని సూచిస్తుంది, సవార్ సైన్యంలో నిర్వహించాల్సిన అశ్వికదళ సంఖ్యను సూచిస్తుంది", "జాత్ సైనిక ర్యాంకును, సవార్ జాగీర్ల నుండి వచ్చే ఆదాయాన్ని సూచిస్తుంది", "జాత్ న్యాయ అధికారాలను, సవార్ పోలీస్ అధికారాలను సూచిస్తుంది", "జాత్ ఫిరంగి దళాన్ని, సవార్ కాల్బలాన్ని సూచిస్తుంది"],
        0,
        "In the Mansabdari system, 'Zat' fixed the personal status and salary scale of the noble, while 'Sawar' determined the number of horsemen (cavalry) he was obligated to maintain for imperial service.",
        "మన్సబ్దారీ విధానంలో 'జాత్' అనేది అధికారి వ్యక్తిగత హోదా మరియు జీతాన్ని, 'సవార్' అనేది నిర్వహించాల్సిన గుర్రపు రౌతుల సంఖ్యను సూచిస్తుంది."
    ))

    # Q142: Shivaji Administration
    qs.append(make_q(
        142, "Indian History - Maratha Administration",
        "Consider the following statements regarding the administration of Chhatrapati Shivaji Maharaj:\n\nStatement I: Shivaji was assisted by a council of eight ministers known as the 'Ashta Pradhan', headed by the Peshwa.\nStatement II: 'Chauth' was a levy of one-fourth (25%) of land revenue paid by non-Maratha territories to avoid Maratha raids, while 'Sardeshmukhi' was an additional 10% tax claimed as hereditary head.\n\nWhich of the statements given above is/are correct?",
        "ఛత్రపతి శివాజీ మహారాజ్ పరిపాలనకు సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: శివాజీకి పాలనలో సలహాలు ఇచ్చేందుకు పీష్వా నేతృత్వంలో ఎనిమిది మంది మంత్రులతో కూడిన 'అష్ట ప్రధాన్' మండలి ఉండేది.\nప్రకటన II: మరాఠాల దాడుల నుండి రక్షణ కోసం ఇతర ప్రాంతాల నుండి వసూలు చేసే 1/4 వంతు పన్ను 'చౌత్', మరియు వంశపారపర్య హక్కుగా వసూలు చేసే అదనపు 10% పన్ను 'సర్దేశ్‌ముఖి'.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are correct. Shivaji's Ashta Pradhan managed central departments, while Chauth (25%) and Sardeshmukhi (10%) were distinctive Maratha fiscal levies on neighbouring regions.",
        "రెండు ప్రకటనలు సరైనవి. శివాజీ మంత్రుల మండలిని అష్ట ప్రధాన్ అంటారు. చౌత్ (25%), సర్దేశ్‌ముఖి (10%) లు మరాఠా పన్నుల విధానం."
    ))

    # Q143: 1857 Revolt Match
    qs.append(make_q(
        143, "Indian History - 1857 Revolt Leaders",
        "Match List-I (1857 Revolt Centre) with List-II (Principal Leader):\n\nList-I\t\t\tList-II\nA. Kanpur\t\t1. Begum Hazrat Mahal\nB. Lucknow\t\t2. Nana Sahib\nC. Arrah (Bihar)\t3. Khan Bahadur Khan\nD. Bareilly\t\t4. Kunwar Singh\n\nChoose the correct code:",
        "జాబితా-I (1857 తిరుగుబాటు కేంద్రం) ను జాబితా-II (ప్రధాన నాయకుడు) తో జతపరచండి:\n\nజాబితా-I\t\t\tజాబితా-II\nA. కాన్పూర్\t\t1. బేగం హజ్రత్ మహల్\nB. లక్నో\t\t2. నానా సాహెబ్\nC. అర్రా (బీహార్)\t3. ఖాన్ బహదూర్ ఖాన్\nD. బరేలీ\t\t4. కున్వర్ సింగ్\n\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-2, B-1, C-4, D-3", "A-2, B-4, C-1, D-3", "A-1, B-2, C-4, D-3", "A-3, B-1, C-4, D-2"],
        ["A-2, B-1, C-4, D-3", "A-2, B-4, C-1, D-3", "A-1, B-2, C-4, D-3", "A-3, B-1, C-4, D-2"],
        0,
        "Kanpur = Nana Sahib (A-2). Lucknow = Begum Hazrat Mahal (B-1). Arrah/Bihar = Kunwar Singh (C-4). Bareilly = Khan Bahadur Khan (D-3). Code: A-2, B-1, C-4, D-3.",
        "కాన్పూర్: నానా సాహెబ్ (A-2), లక్నో: బేగం హజ్రత్ మహల్ (B-1), బీహార్: కున్వర్ సింగ్ (C-4), బరేలీ: ఖాన్ బహదూర్ ఖాన్ (D-3). సరైన కోడ్: A-2, B-1, C-4, D-3."
    ))

    # Q144: Jyotirao Phule
    qs.append(make_q(
        144, "Indian History - Socio-Religious Reformers",
        "Which prominent 19th-century social reformer founded the 'Satyashodhak Samaj' in Pune in 1873 to liberate the lower castes from exploitation and authored the famous book 'Gulamgiri'?",
        "1873లో పూణేలో అణగారిన వర్గాల విముక్తి కోసం 'సత్యశోధక్ సమాజ్' ను స్థాపించి, ప్రసిద్ధ 'గులాంగిరి' గ్రంథాన్ని రచించిన 19వ శతాబ్దపు ప్రముఖ సంఘసంస్కర్త ఎవరు?",
        ["B.R. Ambedkar", "Jyotirao Govindrao Phule", "Gopal Ganesh Agarkar", "Ishwar Chandra Vidyasagar"],
        ["బి.ఆర్. అంబేద్కర్", "జ్యోతిరావ్ గోవిందరావు ఫూలే (Jyotirao Phule)", "గోపాల్ గణేష్ అగార్కర్", "ఈశ్వర చంద్ర విద్యాసాగర్"],
        1,
        "Mahatma Jyotirao Phule founded the Satyashodhak Samaj in 1873 and authored Gulamgiri (Slavery) in 1873, dedicating it to the American movement to abolish slavery.",
        "మహాత్మా జ్యోతిరావ్ ఫూలే 1873లో సత్యశోధక్ సమాజ్‌ను స్థాపించారు మరియు 'గులాంగిరి' గ్రంథాన్ని రచించారు."
    ))

    # Q145: Indian National Congress Formation
    qs.append(make_q(
        145, "Indian History - Freedom Struggle Early Phase",
        "The first session of the Indian National Congress was held in December 1885 in Bombay under the presidency of Womesh Chandra Bonnerjee. At which venue was this inaugural session held?",
        "1885 డిసెంబర్‌లో డబ్ల్యూ.సి. బెనర్జీ అధ్యక్షతన భారత జాతీయ కాంగ్రెస్ (INC) మొదటి సమావేశం బొంబాయిలోని ఏ ప్రదేశంలో జరిగింది?",
        ["Gokuldas Tejpal Sanskrit College", "Elphinstone College", "Sundarayya Vignana Kendram", "Fergusson College"],
        ["గోకుల్‌దాస్ తేజ్‌పాల్ సంస్కృత కళాశాల", "ఎల్ఫిన్‌స్టోన్ కళాశాల", "సుందరయ్య విజ్ఞాన కేంద్రం", "ఫెర్గూసన్ కళాశాల"],
        0,
        "The founding session of the Indian National Congress was held at Gokuldas Tejpal Sanskrit College in Bombay from December 28 to 31, 1885, attended by 72 delegates.",
        "భారత జాతీయ కాంగ్రెస్ తొలి సమావేశం 1885 డిసెంబర్ 28న బొంబాయిలోని గోకుల్‌దాస్ తేజ్‌పాల్ సంస్కృత కళాశాలలో 72 మంది ప్రతినిధులతో జరిగింది."
    ))

    # Q146: Swadeshi Movement & Vandemataram
    qs.append(make_q(
        146, "Indian History - Swadeshi Movement 1905",
        "Consider the following statements regarding the 1905 Swadeshi and Anti-Partition Movement:\n\nStatement I: Bankim Chandra Chattopadhyay's song 'Vande Mataram' became the national hymn and rallying slogan of the anti-partition agitation.\nStatement II: On the day the partition of Bengal took effect (October 16, 1905), Rabindranath Tagore suggested observing 'Raksha Bandhan' to celebrate brotherhood between Hindus and Muslims.\n\nWhich of the statements given above is/are correct?",
        "1905 నాటి స్వదేశీ మరియు వందేమాతరం ఉద్యమానికి సంబంధించి కింది ప్రకటనలను పరిశీలించండి:\n\nప్రకటన I: బంకించంద్ర ఛటర్జీ రచించిన 'వందేమాతరం' గీతం బెంగాల్ విభజన వ్యతిరేక ఉద్యమానికి ప్రధాన నినాదంగా మరియు ఉద్యమ గీతంగా మారింది.\nప్రకటన II: బెంగాల్ విభజన అమలులోకి వచ్చిన రోజున (అక్టోబర్ 16, 1905), హిందూ-ముస్లింల ఐక్యతకు ప్రతీకగా 'రాఖీ బంధన్' దినోత్సవంగా జరపాలని రవీంద్రనాథ్ ఠాగూర్ పిలుపునిచ్చారు.\n\nపై ప్రకటనలలో ఏది/వి సరైనది/వి?",
        ["Only Statement I is correct", "Only Statement II is correct", "Both Statements I and II are correct", "Neither Statement I nor II is correct"],
        ["ప్రకటన I మాత్రమే సరైనది", "ప్రకటన II మాత్రమే సరైనది", "రెండు ప్రకటనలు I మరియు II సరైనవి", "ఏ ప్రకటన కూడా సరైనది కాదు"],
        2,
        "Both statements are historically accurate. Vande Mataram became the battle cry of the Swadeshi movement, and Rabindranath Tagore organised the Rakhi Bandhan day on October 16, 1905.",
        "రెండు ప్రకటనలు సరైనవి. వందేమాతరం గీతం ఉద్యమ స్ఫూర్తిగా నిలవగా, రవీంద్రనాథ్ ఠాగూర్ ఐక్యత కోసం రాఖీ బంధన్ దినోత్సవాన్ని నిర్వహించారు."
    ))

    # Q147: Non-Cooperation Movement
    qs.append(make_q(
        147, "Indian History - Gandhian Era",
        "Mahatma Gandhi abruptly suspended the Non-Cooperation Movement in February 1922 following which violent incident where an agitated crowd set fire to a police station, killing 22 policemen?",
        "1922 ఫిబ్రవరిలో నిరసనకారులు పోలీస్ స్టేషన్‌కు నిప్పు పెట్టడంతో 22 మంది పోలీసులు మరణించిన ఏ హింసాత్మక సంఘటన తర్వాత మహాత్మా గాంధీ సహాయ నిరాకరణ ఉద్యమాన్ని అర్ధాంతరంగా నిలిపివేశారు?",
        ["Jallianwala Bagh firing", "Chauri Chaura incident", "Kakori train action", "Chittagong armoury raid"],
        ["జలియన్ వాలాబాగ్ కాల్పులు", "చౌరీ చౌరా సంఘటన (Chauri Chaura)", "కాకోరి రైలు సంఘటన", "చిట్టగాంగ్ ఆయుధాగార దాడి"],
        1,
        "On February 4, 1922, protestors clashed with police and set the police station on fire at Chauri Chaura in Gorakhpur district, UP, leading Gandhi to call off the Non-Cooperation Movement on February 12, 1922.",
        "గోరఖ్‌పూర్ జిల్లాలోని చౌరీ చౌరా వద్ద జరిగిన హింసాత్మక సంఘటన వల్ల గాంధీజీ 1922 ఫిబ్రవరిలో సహాయ నిరాకరణ ఉద్యమాన్ని విరమించారు."
    ))

    # Q148: Salt Satyagraha Dandi March
    qs.append(make_q(
        148, "Indian History - Civil Disobedience Movement",
        "During the historic Salt March (Dandi March) that inaugurated the Civil Disobedience Movement in 1930, how many chosen followers accompanied Mahatma Gandhi on his 240-mile walk from Sabarmati Ashram to Dandi?",
        "1930లో శాసనోల్లంఘన ఉద్యమాన్ని ప్రారంభిస్తూ సబర్మతి ఆశ్రమం నుండి దండి వరకు చేపట్టిన చారిత్రాత్మక ఉప్పు సత్యాగ్రహం (దండి మార్చ్) లో మహాత్మా గాంధీతో పాటు ఎంతమంది ఎంపిక చేసిన ఆశ్రమ సహచరులు నడిచారు?",
        ["72 followers", "78 followers", "84 followers", "100 followers"],
        ["72 మంది అనుచరులు", "78 మంది అనుచరులు", "84 మంది అనుచరులు", "100 మంది అనుచరులు"],
        1,
        "Gandhi began his 240-mile march on March 12, 1930 with 78 trusted volunteers from Sabarmati Ashram, reaching Dandi on April 5 and breaking the salt law on April 6, 1930.",
        "1930 మార్చి 12న గాంధీజీ 78 మంది అనుచరులతో సబర్మతి నుండి పాదయాత్ర ప్రారంభించి ఏప్రిల్ 6న దండి వద్ద ఉప్పు చట్టాన్ని ఉల్లంఘించారు."
    ))

    # Q149: HSRA & Bhagat Singh
    qs.append(make_q(
        149, "Indian History - Revolutionary Movement",
        "In September 1928, at the Feroz Shah Kotla grounds in Delhi, young revolutionaries reorganized the Hindustan Republican Association into the 'Hindustan Socialist Republican Association' (HSRA) under whose ideological leadership?",
        "1928 సెప్టెంబర్‌లో ఢిల్లీలోని ఫిరోజ్ షా కోట్లా మైదానంలో ఎవరి సిద్ధాంత నాయకత్వంలో యువ విప్లవకారులు హిందూస్థాన్ రిపబ్లికన్ అసోసియేషన్‌ను 'హిందూస్థాన్ సోషలిస్ట్ రిపబ్లికన్ అసోసియేషన్' (HSRA) గా పునర్వ్యవస్థీకరించారు?",
        ["Ram Prasad Bismil", "Chandrashekhar Azad and Bhagat Singh", "Surya Sen", "Sachindra Nath Sanyal"],
        ["రామ్ ప్రసాద్ బిస్మిల్", "చంద్రశేఖర్ ఆజాద్ మరియు భగత్ సింగ్", "సూర్యా సేన్", "శచీంద్ర నాథ్ సన్యాల్"],
        1,
        "Under the leadership of Chandrashekhar Azad, Bhagat Singh, Sukhdev, and Vijay Kumar Sinha, the party added 'Socialist' to its name at Feroz Shah Kotla in 1928, committing to socialist revolution.",
        "1928లో చంద్రశేఖర్ ఆజాద్ మరియు భగత్ సింగ్ నాయకత్వంలో పార్టీ పేరులో 'సోషలిస్ట్' పదాన్ని చేర్చి HSRA గా మార్చారు."
    ))

    # Q150: Indian National Army (INA)
    qs.append(make_q(
        150, "Indian History - Subhash Chandra Bose & INA",
        "On October 21, 1943, Netaji Subhash Chandra Bose proclaimed the establishment of the Provisional Government of Free India ('Arzi Hukumat-e-Azad Hind') in which foreign city?",
        "1943 అక్టోబర్ 21న నేతాజీ సుభాష్ చంద్రబోస్ తాత్కాలిక స్వతంత్ర భారత ప్రభుత్వాన్ని ('ఆర్జీ హుకుమత్-ఎ-ఆజాద్ హింద్') ఏ విదేశీ నగరంలో ప్రకటించారు?",
        ["Tokyo, Japan", "Singapore", "Rangoon, Burma", "Berlin, Germany"],
        ["టోక్యో (జపాన్)", "సింగపూర్ (Singapore)", "రంగూన్ (బర్మా)", "బెర్లిన్ (జర్మనీ)"],
        1,
        "Netaji proclaimed the Provisional Government of Free India on October 21, 1943 at the Cathay Cinema Hall in Singapore.",
        "1943 అక్టోబర్ 21న నేతాజీ సుభాష్ చంద్రబోస్ సింగపూర్‌లో తాత్కాలిక ఆజాద్ హింద్ ప్రభుత్వాన్ని ఏర్పాటు చేశారు."
    ))

    return qs
