# -*- coding: utf-8 -*-
"""
Builder for scripts/mock13_gs.py (Q101 to Q200)
TSPLRB SI Prelims (PWT) General Studies Blueprint (Medium Standard):
- Q101-Q116: Indian Polity & Governance (16 Qs: 3 FCB + 13 Authored)
- Q117-Q136: Telangana Movement, History, Culture & Governance (20 Qs: 17 FCB + 3 Authored)
- Q137-Q150: Indian History & National Movement (14 Qs: 3 FCB + 11 Authored)
- Q151-Q164: Geography & Environment (14 Qs Authored)
- Q165-Q174: Indian & Telangana Economy (10 Qs Authored)
- Q175-Q188: General Science & Technology (14 Qs: 2 FCB + 12 Authored)
- Q189-Q200: Current Affairs & International Events (12 Qs: 9 FCB + 3 StudyNow 2026)
Total = 100 Questions. Strictly 0 duplicates against Mocks 1-12.
"""
import json, re, glob

def clean_tag(s):
    if not s: return ""
    return re.sub(r'^\s*\[[^\]]+\]\s*', '', str(s)).strip()

def make_q(id_num, topic, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
    return {
        "id": id_num,
        "qNumber": id_num,
        "section": "General Studies",
        "topic": clean_tag(topic),
        "difficulty": "Medium",
        "question_en": clean_tag(q_en),
        "question_te": clean_tag(q_te),
        "options_en": [clean_tag(o) for o in opts_en],
        "options_te": [clean_tag(o) for o in opts_te],
        "correct_option": int(corr),
        "explanation_en": clean_tag(exp_en),
        "explanation_te": clean_tag(exp_te)
    }

def get_gs_100():
    with open('public/data/faculty_curated_bank.json', 'r', encoding='utf-8') as fp:
        fcb_all = json.load(fp)['questions']
    fcb_map = {q['id']: q for q in fcb_all}

    with open('public/data/reference_studynow_ca_2026.json', 'r', encoding='utf-8') as fp:
        sn_all = json.load(fp)

    gs_list = []

    # ---------------------------------------------------------
    # 1. INDIAN POLITY & GOVERNANCE (16 Qs: Q101 to Q116)
    # ---------------------------------------------------------
    # FCB 96 (Art 131), 100 (Art 312), 112 (Zonal Councils)
    for fid in [96, 100, 112]:
        q = fcb_map[fid]
        gs_list.append(make_q(
            101 + len(gs_list), q.get('topic', 'Indian Polity'),
            q['question_en'], q['question_te'],
            q['options_en'], q['options_te'],
            q['correct_option'], q['explanation_en'], q['explanation_te']
        ))

    authored_polity = [
        ("Indian Polity - Preamble & Basic Structure",
         "In which landmark verdict did the Supreme Court of India propound the 'Basic Structure Doctrine', establishing that Parliament cannot alter the basic features of the Constitution?",
         "భారత రాజ్యాంగంలోని ప్రాథమిక లక్షణాలను పార్లమెంటు మార్చడానికి వీల్లేదని తెలుపుతూ సుప్రీంకోర్టు 'ప్రాథమిక స్వరూప సిద్ధాంతాన్ని' (Basic Structure Doctrine) ఏ మైలురాయి తీర్పులో వెలువరించింది?",
         ["Golaknath Case (1967)", "Kesavananda Bharati Case (1973)", "Minerva Mills Case (1980)", "Maneka Gandhi Case (1978)"],
         ["గోలక్‌నాథ్ కేసు (1967)", "కేశవానంద భారతి కేసు (1973)", "మినర్వా మిల్స్ కేసు (1980)", "మేనకా గాంధీ కేసు (1978)"],
         1,
         "In Kesavananda Bharati v. State of Kerala (1973), a 13-judge constitutional bench ruled that Article 368 does not allow Parliament to damage or destroy the basic structure of the Constitution.",
         "1973 నాటి కేశవానంద భారతి కేసులో 13 మంది న్యాయమూర్తుల రాజ్యాంగ ధర్మాసనం తీర్పునిస్తూ రాజ్యాంగ ప్రాథమిక స్వరూపాన్ని సవరించే అధికారం పార్లమెంటుకు లేదని స్పష్టం చేసింది."),

        ("Indian Polity - Fundamental Rights: Article 19",
         "Under Article 19(1) of the Indian Constitution, which of the following is NOT an expressly recognized fundamental freedom?",
         "భారత రాజ్యాంగంలోని అధికరణ 19(1) ప్రకారం క్రింది వాటిలో స్పష్టంగా హామీ ఇవ్వబడని హక్కు ఏది?",
         ["Freedom of speech and expression", "Freedom to assemble peaceably and without arms", "Freedom to acquire, hold and dispose of property", "Freedom to practice any profession, trade or business"],
         ["వాక్ మరియు భావ ప్రకటనా స్వేచ్ఛ", "శాంతియుతంగా, నిరాయుధులుగా సమావేశమయ్యే స్వేచ్ఛ", "ఆస్తిని సంపాదించే, కలిగి ఉండే మరియు విక్రయించే స్వేచ్ఛ", "ఏదైనా వృత్తి, వ్యాపారం నిర్వహించుకునే స్వేచ్ఛ"],
         2,
         "The right to acquire, hold, and dispose of property under Article 19(1)(f) was repealed by the 44th Constitutional Amendment Act, 1978, and made a legal right under Article 300A.",
         "44వ రాజ్యాంగ సవరణ చట్టం (1978) ద్వారా అధికరణ 19(1)(f) లోని ఆస్తి సంపాదనా స్వేచ్ఛను ప్రాథమిక హక్కుల జాబితా నుండి తొలగించి, అధికరణ 300A కింద చట్టపరమైన హక్కుగా మార్చారు."),

        ("Indian Polity - Fundamental Rights: Article 20",
         "Article 20(3) of the Indian Constitution provides immunity against which of the following coercive state actions?",
         "భారత రాజ్యాంగంలోని అధికరణ 20(3) క్రింది వాటిలో దేని నుండి పౌరులకు రక్షణ కల్పిస్తుంది?",
         ["Double Jeopardy", "Ex-post facto criminal laws", "Self-incrimination (compulsion to be a witness against oneself)", "Preventive Detention beyond three months"],
         ["ద్విశిక్షా నిషేధం (Double Jeopardy)", "శాసనోల్లంఘనానంతర శిక్షల రక్షణ", "ఆత్మసాక్ష్యం/స్వీయ సాక్ష్య నిర్బంధం (Self-incrimination)", "మూడు నెలలు మించిన ముందస్తు నిర్బంధం"],
         2,
         "Article 20(3) states that no person accused of any offence shall be compelled to be a witness against himself (Protection against Self-Incrimination).",
         "అధికరణ 20(3) ప్రకారం ఏ నేరారోపణ ఎదుర్కొంటున్న వ్యక్తినీ తనకు వ్యతిరేకంగా తానే సాక్ష్యమిచ్చుకోవాలని బలవంతం చేయరాదు (స్వీయ సాక్ష్య రక్షణ)."),

        ("Indian Polity - Fundamental Rights: Child Labour",
         "Which Article of the Indian Constitution strictly prohibits the employment of children below the age of 14 years in factories, mines, or other hazardous occupations?",
         "14 సంవత్సరాల కంటే తక్కువ వయస్సు ఉన్న పిల్లలను కర్మాగారాలు, గనులు లేదా ఇతర ప్రమాదకరమైన పనుల్లో నియమించడాన్ని నిషేధించే రాజ్యాంగ అధికరణ ఏది?",
         ["Article 23", "Article 24", "Article 25", "Article 29"],
         ["అధికరణ 23", "అధికరణ 24", "అధికరణ 25", "అధికరణ 29"],
         1,
         "Article 24 provides that no child below the age of fourteen years shall be employed to work in any factory or mine or engaged in any other hazardous employment.",
         "అధికరణ 24 ప్రకారం 14 ఏళ్ల లోపు బాలబాలికలను కర్మాగారాలు, గనులు మరియు ప్రమాదకర పనులలో పనికి పెట్టుకోవడం నిషేధం."),

        ("Indian Polity - Pardoning Powers: President vs Governor",
         "Which of the following powers is exclusively vested in the President of India and NOT available to a State Governor under the Constitution?",
         "భారత రాజ్యాంగం ప్రకారం రాష్ట్ర గవర్నర్‌కు లేని, కేవలం భారత రాష్ట్రపతికి మాత్రమే ఉన్న ప్రత్యేక అధికారం ఏది?",
         ["Power to grant pardon in cases of punishment by a Court Martial", "Power to commute a sentence of rigorous imprisonment", "Power to remit punishment for offences against state laws", "Power to suspend sentences of fine"],
         ["కోర్టు మార్షల్ (సైనిక న్యాయస్థానం) విధించిన శిక్షను క్షమించే అధికారం", "కఠిన కారాగార శిక్షను తగ్గించే అధికారం", "రాష్ట్ర చట్టాల ఉల్లంఘనకు విధించిన శిక్షను ఉపశమనం చేసే అధికారం", "జరిమానా శిక్షను తాత్కాలికంగా నిలిపివేసే అధికారం"],
         0,
         "Under Article 72, the President alone has the power to pardon sentences by a Court Martial and death sentences. Under Article 161, a Governor cannot pardon a Court Martial sentence.",
         "అధికరణ 72 కింద సైనిక న్యాయస్థానాలు (కోర్టు మార్షల్) విధించిన శిక్షలపై క్షమాభిక్ష పెట్టే అధికారం రాష్ట్రపతికి మాత్రమే ఉంటుంది. గవర్నర్‌కు ఈ అధికారం లేదు."),

        ("Indian Polity - Parliament: Money Bill Certification",
         "Under Article 110 of the Constitution, whose decision is final and non-justiciable on whether a particular Bill is a Money Bill or not?",
         "రాజ్యాంగంలోని అధికరణ 110 ప్రకారం ఒక బిల్లు ద్రవ్య బిల్లా (Money Bill) కాదా అనే విషయంలో ఎవరి నిర్ణయం అంతిమమైనది?",
         ["President of India", "Speaker of the Lok Sabha", "Chairman of the Rajya Sabha", "Union Finance Minister"],
         ["భారత రాష్ట్రపతి", "లోక్‌సభ స్పీకర్", "రాజ్యసభ ఛైర్మన్", "కేంద్ర ఆర్థిక మంత్రి"],
         1,
         "Article 110(3) states that if any question arises whether a Bill is a Money Bill or not, the decision of the Speaker of the House of the People (Lok Sabha) thereon shall be final.",
         "అధికరణ 110(3) ప్రకారం ఏదైనా బిల్లు ద్రవ్య బిల్లా కాదా అనే వివాదం తలెత్తితే లోక్‌సభ స్పీకర్ తీసుకునే నిర్ణయమే అంతిమమైనది."),

        ("Indian Polity - Parliamentary Committees: PAC",
         "Consider the following statements regarding the Public Accounts Committee (PAC) of Parliament:\n1. It consists of 22 members (15 from Lok Sabha and 7 from Rajya Sabha).\n2. A Minister is not eligible to be elected as a member of the Committee.\nWhich of the statements given above is/are correct?",
         "పార్లమెంటు పబ్లిక్ అకౌంట్స్ కమిటీ (PAC) కి సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. ఇందులో మొత్తం 22 మంది సభ్యులు ఉంటారు (15 మంది లోక్‌సభ, 7 మంది రాజ్యసభ నుండి).\n2. కేంద్ర ప్రభుత్వంలోని ఏ మంత్రీ ఈ కమిటీలో సభ్యుడిగా ఎన్నిక కావడానికి అర్హుడు కాదు.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
         ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
         ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
         2,
         "Both statements are correct. The PAC has 22 members elected by proportional representation. Ministers cannot be members to ensure unbiased legislative scrutiny over executive expenditure.",
         "రెండు ప్రకటనలూ సరైనవే. PAC లో 22 మంది సభ్యులు ఉంటారు. కార్యనిర్వాహక వర్గంపై స్వతంత్ర పర్యవేక్షణ ఉండటానికి ఏ మంత్రీ PAC లో సభ్యుడిగా ఉండరాదు."),

        ("Indian Polity - State Legislature: Legislative Council",
         "Under Article 169 of the Constitution, a State Legislative Council can be created or abolished if the Legislative Assembly of the State passes a resolution by:",
         "రాజ్యాంగంలోని అధికరణ 169 ప్రకారం ఒక రాష్ట్ర శాసన మండలిని (Legislative Council) ఏర్పాటు చేయడానికి లేదా రద్దు చేయడానికి శాసనసభ ఏ మెజారిటీతో తీర్మానం ఆమోదించాలి?",
         ["Simple majority of members present and voting", "Special majority (majority of total membership and not less than 2/3rd of members present and voting)", "Absolute majority of total membership only", "3/4th majority of total membership"],
         ["హాజరై ఓటు వేసిన సభ్యుల సాధారణ మెజారిటీ", "ప్రత్యేక మెజారిటీ (మొత్తం సభ్యులలో మెజారిటీ మరియు హాజరై ఓటు వేసిన వారిలో కనీసం 2/3 వంతు)", "మొత్తం సభ్యుల సంపూర్ణ మెజారిటీ మాత్రమే", "మొత్తం సభ్యులలో 3/4 వంతు మెజారిటీ"],
         1,
         "Article 169 requires a resolution passed by a majority of the total membership of the Assembly and by a majority of not less than two-thirds of the members present and voting.",
         "అధికరణ 169 ప్రకారం శాసనసభ మొత్తం సభ్యులలో మెజారిటీ మరియు హాజరై ఓటు వేసిన వారిలో కనీసం 2/3 వంతు సభ్యుల ప్రత్యేక మెజారిటీతో తీర్మానం ఆమోదించాలి."),

        ("Indian Polity - Emergency Provisions: Article 356",
         "A Proclamation of President's Rule issued under Article 356 must be approved by both Houses of Parliament within what maximum timeframe?",
         "రాజ్యాంగంలోని అధికరణ 356 కింద విధించిన రాష్ట్రపతి పాలన ప్రకటనను పార్లమెంటు ఉభయ సభలు ఎంత కాల వ్యవధిలోగా ఆమోదించాలి?",
         ["14 days", "1 month", "2 months", "6 months"],
         ["14 రోజులు", "1 నెల", "2 నెలలు", "6 నెలలు"],
         2,
         "Under Article 356(3), a proclamation of President's Rule ceases to operate at the expiration of two months unless approved by resolutions of both Houses of Parliament.",
         "అధికరణ 356(3) ప్రకారం రాష్ట్రపతి పాలన ప్రకటన వెలువడిన నాటి నుండి 2 నెలల లోపు పార్లమెంటు ఉభయ సభల ఆమోదం పొందాలి."),

        ("Indian Polity - Constitutional Bodies: Finance Commission",
         "Under Article 280 of the Indian Constitution, the Finance Commission is constituted by the President of India at the expiration of every:",
         "భారత రాజ్యాంగంలోని అధికరణ 280 ప్రకారం కేంద్ర ఆర్థిక సంఘాన్ని (Finance Commission) రాష్ట్రపతి ఎన్ని సంవత్సరాలకు ఒకసారి ఏర్పాటు చేస్తారు?",
         ["3 years", "5 years", "6 years", "10 years"],
         ["3 సంవత్సరాలు", "5 సంవత్సరాలు", "6 సంవత్సరాలు", "10 సంవత్సరాలు"],
         1,
         "Article 280 provides that the President shall, at the expiration of every fifth year or at such earlier time as he considers necessary, constitute a Finance Commission.",
         "అధికరణ 280 ప్రకారం ప్రతి 5 సంవత్సరాలకు ఒకసారి లేదా అవసరమని భావించిన ముందస్తు సమయంలో రాష్ట్రపతి ఆర్థిక సంఘాన్ని నియమిస్తారు."),

        ("Indian Polity - Local Self-Government: 73rd Amendment",
         "Which Constitutional Amendment Act accorded constitutional status to Panchayati Raj Institutions and added the Eleventh Schedule containing 29 functional items?",
         "పంచాయతీరాజ్ సంస్థలకు రాజ్యాంగ ప్రతిపత్తి కల్పిస్తూ 29 అధికార విధులతో కూడిన 11వ షెడ్యూల్‌ను చేర్చిన రాజ్యాంగ సవరణ చట్టం ఏది?",
         ["71st Amendment Act, 1992", "73rd Amendment Act, 1992", "74th Amendment Act, 1992", "86th Amendment Act, 2002"],
         ["71వ సవరణ చట్టం, 1992", "73వ సవరణ చట్టం, 1992", "74వ సవరణ చట్టం, 1992", "86వ సవరణ చట్టం, 2002"],
         1,
         "The 73rd Constitutional Amendment Act, 1992 came into effect on April 24, 1993, adding Part IX and the Eleventh Schedule with 29 functional items.",
         "73వ రాజ్యాంగ సవరణ చట్టం, 1992 ద్వారా రాజ్యాంగంలో 9వ భాగం మరియు 29 విధులతో కూడిన 11వ షెడ్యూల్‌ను చేర్చి పంచాయతీలకు రాజ్యాంగ ప్రతిపత్తి కల్పించారు."),

        ("Indian Polity - Anti-Defection Law: 10th Schedule",
         "Under the Tenth Schedule (Anti-Defection Law) introduced by the 52nd Constitutional Amendment Act 1985, who is the competent adjudicating authority on questions of disqualification?",
         "52వ రాజ్యాంగ సవరణ చట్టం 1985 ద్వారా చేర్చబడిన పదవ షెడ్యూల్ (పార్టీ ఫిరాయింపుల నిరోధక చట్టం) కింద అనర్హత పిటిషన్లపై నిర్ణయం తీసుకునే అధికారం ఎవరికి ఉంటుంది?",
         ["President of India / Governor", "Election Commission of India", "Chairman / Speaker of the respective House", "Supreme Court of India"],
         ["భారత రాష్ట్రపతి / గవర్నర్", "భారత ఎన్నికల సంఘం", "సంబంధిత సభ ఛైర్మన్ / స్పీకర్", "భారత సుప్రీంకోర్టు"],
         2,
         "Paragraph 6 of the Tenth Schedule provides that any question regarding disqualification of a member is decided by the Chairman or the Speaker of such House.",
         "10వ షెడ్యూల్‌లోని పేరా 6 ప్రకారం సభ్యుల అనర్హతకు సంబంధించిన ఏ వివాదాన్నైనా ఆ సభ స్పీకర్ లేదా ఛైర్మన్ మాత్రమే పరిష్కరిస్తారు."),

        ("Indian Polity - Constitutional Amendments: Article 368",
         "Which Article in Part XX of the Indian Constitution deals explicitly with the powers and procedure of Parliament to amend the Constitution?",
         "భారత రాజ్యాంగంలోని 20వ భాగంలో రాజ్యాంగ సవరణ అధికారం మరియు పద్ధతిని స్పష్టంగా పేర్కొనే అధికరణ ఏది?",
         ["Article 352", "Article 360", "Article 368", "Article 370"],
         ["అధికరణ 352", "అధికరణ 360", "అధికరణ 368", "అధికరణ 370"],
         2,
         "Article 368 in Part XX grants Parliament constituent power to amend by way of addition, variation or repeal any provision of the Constitution in accordance with the prescribed procedure.",
         "రాజ్యాంగంలోని 20వ భాగంలో గల అధికరణ 368 రాజ్యాంగాన్ని సవరించే పార్లమెంటు అధికారాలు మరియు నిబంధనలను నిర్దేశిస్తుంది.")
    ]

    for item in authored_polity:
        gs_list.append(make_q(101 + len(gs_list), item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))

    assert len(gs_list) == 16, f"Expected 16 Polity questions, got {len(gs_list)}"

    # ---------------------------------------------------------
    # 2. TELANGANA MOVEMENT, HISTORY & CULTURE (20 Qs: Q117 to Q136)
    # ---------------------------------------------------------
    # FCB 17 Qs: 51, 59, 61, 62, 69, 71, 72, 79, 81, 82, 89, 91, 92, 99, 107, 108, 115
    fcb_tg_ids = [51, 59, 61, 62, 69, 71, 72, 79, 81, 82, 89, 91, 92, 99, 107, 108, 115]
    for fid in fcb_tg_ids:
        q = fcb_map[fid]
        gs_list.append(make_q(
            101 + len(gs_list), q.get('topic', 'Telangana History & Movement'),
            q['question_en'], q['question_te'],
            q['options_en'], q['options_te'],
            q['correct_option'], q['explanation_en'], q['explanation_te']
        ))

    authored_tg = [
        ("Telangana Movement - 1952 Non-Mulki Agitation & City College Police Firing",
         "Following the tragic police firing on student demonstrators near City College, Hyderabad during the 1952 'Non-Mulki Go Back' agitation, which judicial commission was appointed by the Hyderabad State Government to probe the incident?",
         "1952 'నాన్-ముల్కీ గో బ్యాక్' ఉద్యమ సమయంలో హైదరాబాద్ సిటీ కాలేజీ సమీపంలో విద్యార్థులపై జరిగిన పోలీసు కాల్పుల ఘటనపై విచారణ జరిపేందుకు హైదరాబాద్ రాష్ట్ర ప్రభుత్వం ఏ న్యాయ కమిషన్‌ను నియమించింది?",
         ["Justice Pingali Jaganmohan Reddy Commission", "Justice K.N. Wanchoo Committee", "Justice Vashishtha Bhargava Committee", "Kumar Lalith Committee"],
         ["జస్టిస్ పింగళి జగన్మోహన్ రెడ్డి కమిషన్", "జస్టిస్ కె.ఎన్. వాంచూ కమిటీ", "జస్టిస్ వశిష్ట భార్గవ కమిటీ", "కుమార్ లలిత్ కమిటీ"],
         0,
         "The Hyderabad State Government appointed the Justice Pingali Jaganmohan Reddy Commission on September 5, 1952, to investigate the police firing on students near City College.",
         "1952 సెప్టెంబర్ 3, 4 తేదీల్లో సిటీ కాలేజీ వద్ద విద్యార్థులపై జరిగిన పోలీసు కాల్పుల దుర్ఘటనపై విచారణ జరిపేందుకు హైదరాబాద్ ప్రభుత్వం జస్టిస్ పింగళి జగన్మోహన్ రెడ్డి కమిషన్‌ను నియమించింది."),

        ("Medieval Telangana History - Kakatiya Dynasty: Ganapati Deva",
         "Which renowned Kakatiya monarch ruled for over six decades (1199–1262 CE), unified the entire Telugu-speaking tracts, and shifted the imperial capital from Anumakonda (Hanamkonda) to Orugallu (Warangal)?",
         "ఆరు దశాబ్దాలకు పైగా (1199–1262 క్రీ.శ.) పరిపాలన సాగించి, తెలుగు ప్రాంతాలన్నింటినీ ఏకం చేసి, తన రాజధానిని అనుమకొండ నుండి ఓరుగల్లు (వరంగల్) కు మార్చిన కాకతీయ చక్రవర్తి ఎవరు?",
         ["Prola II", "Rudradeva (Prataparudra I)", "Ganapati Deva", "Prataparudra II"],
         ["రెండవ ప్రోలరాజు", "రుద్రదేవుడు (మొదటి ప్రతాపరుద్రుడు)", "గణపతి దేవుడు", "రెండవ ప్రతాపరుద్రుడు"],
         2,
         "Ganapati Deva had the longest reign among the Kakatiyas (1199–1262 CE), oversaw major expansion to Motupalli port, and shifted the capital to Warangal fort.",
         "కాకతీయులలో అత్యధిక కాలం పరిపాలించిన గణపతి దేవుడు రాజధానిని అనుమకొండ నుండి ఓరుగల్లు కోటకు మార్చాడు మరియు మోటుపల్లి అభయ శాసనాన్ని జారీ చేశాడు."),

        ("Medieval Telangana History - Qutb Shahi Dynasty: Ibrahim Qutb Shah",
         "Which Golconda Sultan was affectionately eulogized as 'Malkibharama' by contemporary Telugu poets for his generous literary patronage and public works including the Hussain Sagar lake?",
         "హుస్సేన్ సాగర్ చెరువు నిర్మాణం మరియు తెలుగు కవులకు చేసిన విశేష పోషణ వల్ల సమకాలీన తెలుగు కవులచే 'మల్కిభరాముడు' అని అభిమానంతో కొనియాడబడిన గోల్కొండ సుల్తాన్ ఎవరు?",
         ["Sultan Quli Qutb-ul-Mulk", "Ibrahim Qutb Shah", "Muhammad Quli Qutb Shah", "Abdullah Qutb Shah"],
         ["సుల్తాన్ కులీ కుతుబ్-ఉల్-ముల్క్", "ఇబ్రహీం కుతుబ్ షా", "మహమ్మద్ కులీ కుతుబ్ షా", "అబ్దుల్లా కుతుబ్ షా"],
         1,
         "Ibrahim Qutb Shah (reigned 1550–1580) patronized Telugu poets like Kandukuru Rudrakavi and Addanki Gangadhara, who praised him as Malkibharama. He also excavated Hussain Sagar in 1562.",
         "1550-1580 మధ్య పాలించిన ఇబ్రహీం కుతుబ్ షా తెలుగు భాషను, కవులను అమితంగా ఆదరించి 'మల్కిభరాముడు'గా ఖ్యాతికెక్కినాడు. ఇతని కాలంలోనే 1562 లో హుస్సేన్ సాగర్ నిర్మించబడింది.")
    ]

    for item in authored_tg:
        gs_list.append(make_q(101 + len(gs_list), item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))

    assert len(gs_list) == 36, f"Expected 36 cumulative questions (16+20), got {len(gs_list)}"

    # ---------------------------------------------------------
    # 3. INDIAN HISTORY & NATIONAL MOVEMENT (14 Qs: Q137 to Q150)
    # ---------------------------------------------------------
    # FCB 98, 113, 114
    for fid in [98, 113, 114]:
        q = fcb_map[fid]
        gs_list.append(make_q(
            101 + len(gs_list), q.get('topic', 'Indian History & National Movement'),
            q['question_en'], q['question_te'],
            q['options_en'], q['options_te'],
            q['correct_option'], q['explanation_en'], q['explanation_te']
        ))

    authored_history = [
        ("Ancient Indian History - Indus Valley Civilization",
         "At which prominent Harappan site was an artificial brick dockyard discovered, providing evidence of flourishing maritime trade with Mesopotamia?",
         "మెసపటోమియాతో జరిగిన సముద్ర వాణిజ్యానికి నిదర్శనంగా కృత్రిమ ఇటుకల రేవు (డాక్‌యార్డ్) కనుగొనబడిన ప్రముఖ సింధు నాగరికత కేంద్రం ఏది?",
         ["Kalibangan", "Lothal", "Mohenjo-daro", "Dholavira"],
         ["కాళీబంగన్", "లోథాల్", "మొహెంజొదారో", "ధోలవీర"],
         1,
         "Lothal in Gujarat was a prominent port city of the Indus Valley Civilization featuring a massive tidal dockyard connected to the Bhogavo river.",
         "గుజరాత్‌లోని భోగావో నదీ తీరాన గల లోథాల్ సింధు నాగరికత కాలం నాటి అంతర్జాతీయ నౌకాశ్రయం, ఇక్కడ ప్రపంచంలోనే అత్యంత పురాతన డాక్‌యార్డ్ బయల్పడింది."),

        ("Ancient Indian History - Ashokan Edicts: Kalinga War",
         "Which Major Rock Edict of Emperor Ashoka describes the horrors of the Kalinga War and marks his historic transformation towards 'Dhamma Vijaya' (Victory through Righteousness)?",
         "కళింగ యుద్ధ భయానకతను వివరిస్తూ, అశోకుడు యుద్ధ మార్గాన్ని వీడి 'ధమ్మ విజయ' మార్గాన్ని స్వీకరించిన చారిత్రక పరిణామాన్ని తెలిపే అశోకుని ప్రధాన శిలా శాసనం ఏది?",
         ["Major Rock Edict I", "Major Rock Edict V", "Major Rock Edict X", "Major Rock Edict XIII"],
         ["1వ ప్రధాన శిలా శాసనం", "5వ ప్రధాన శిలా శాసనం", "10వ ప్రధాన శిలా శాసనం", "13వ ప్రధాన శిలా శాసనం"],
         3,
         "Major Rock Edict XIII explicitly mentions the conquest of Kalinga (261 BCE), the grief caused by the bloodshed, and Ashoka's subsequent adoption of Dhamma Vijaya.",
         "13వ ప్రధాన శిలా శాసనం కళింగ యుద్ధం (క్రీ.పూ. 261) లో జరిగిన ప్రాణనష్టాన్ని వివరిస్తుంది మరియు అశోకుడు ధర్మ విజయ మార్గాన్ని స్వీకరించినట్లు తెలుపుతుంది."),

        ("Ancient Indian History - Buddhism: Councils",
         "The historic Third Buddhist Council, which codified the Abhidhamma Pitaka, was convened during the reign of which emperor at Pataliputra?",
         "అభిధమ్మ పిటకాన్ని క్రోడీకరించిన చారిత్రక మూడవ బౌద్ధ సంగీతి (సమావేశం) పాటలీపుత్రంలో ఏ చక్రవర్తి ఆధ్వర్యంలో నిర్వహించబడింది?",
         ["Ajatashatru", "Kalasoka", "Emperor Ashoka", "Kanishka"],
         ["అజాతశత్రువు", "కాలాశోకుడు", "అశోక చక్రవర్తి", "కనిష్కుడు"],
         2,
         "The Third Buddhist Council was held around 250 BCE at Pataliputra under the patronage of Emperor Ashoka, presided over by Moggaliputta Tissa.",
         "క్రీ.పూ. 250 లో పాటలీపుత్రంలో అశోక చక్రవర్తి పోషణలో మొగ్గలిపుత్త తిస్స అధ్యక్షతన మూడవ బౌద్ధ సంగీతి జరిగింది. ఇందులో అభిధమ్మ పిటకం సంకలనం చేయబడింది."),

        ("Medieval Indian History - Delhi Sultanate: Market Reforms",
         "Which Sultan of Delhi implemented rigid price controls, set up distinct markets (Sarai-i-Adl), and introduced the military branding system (Dagh and Chehra)?",
         "మార్కెట్ నియంత్రణ సంస్కరణలు, నిర్దిష్ట విపణులు (సరాయ్-ఇ-అద్ల్) మరియు గుర్రాలకు ముద్ర వేసే 'దాగ్' మరియు సైనికుల రికార్డు 'చెహ్రా' పద్ధతులను ప్రవేశపెట్టిన ఢిల్లీ సుల్తాన్ ఎవరు?",
         ["Balban", "Alauddin Khilji", "Muhammad bin Tughlaq", "Firoz Shah Tughlaq"],
         ["బాల్బన్", "అల్లావుద్దీన్ ఖిల్జీ", "మహమ్మద్ బిన్ తుగ్లక్", "ఫిరోజ్ షా తుగ్లక్"],
         1,
         "Alauddin Khilji established detailed price control systems, market superintendents (Shahna-i-Mandi), and introduced Dagh (branding horses) and Chehra (descriptive rolls).",
         "అల్లావుద్దీన్ ఖిల్జీ సైనిక ఖర్చులను తగ్గించుకోవడానికి మార్కెట్ సంస్కరణలను అమలు చేశాడు మరియు అవినీతిని అరికట్టడానికి 'దాగ్' మరియు 'చెహ్రా' విధానాలను ప్రవేశపెట్టాడు."),

        ("Medieval Indian History - Mughal Empire: Mansabdari System",
         "Under the Mughal administrative machinery introduced by Emperor Akbar, what did the dual terms 'Zat' and 'Sawar' signify in the Mansabdari system?",
         "అక్బర్ చక్రవర్తి ప్రవేశపెట్టిన మొఘల్ మన్సబ్దారీ వ్యవస్థలో 'జాత్' (Zat) మరియు 'సవార్' (Sawar) అను పదాలు వేటిని సూచిస్తాయి?",
         ["Zat indicated military rank, while Sawar indicated royal title", "Zat fixed personal status and salary, while Sawar indicated the required cavalry contingent", "Zat represented revenue collected, while Sawar represented tax exempted land", "Zat indicated court precedence, while Sawar indicated administrative territory"],
         ["జాత్ సైనిక హోదాను, సవార్ రాజరిక బిరుదును సూచిస్తుంది", "జాత్ వ్యక్తిగత హోదా మరియు జీతాన్ని నిర్ణయించగా, సవార్ పోషించాల్సిన అశ్వికదళ సైనికుల సంఖ్యను సూచిస్తుంది", "జాత్ వసూలు చేసిన పన్నును, సవార్ పన్ను మినహాయింపు భూమిని సూచిస్తుంది", "జాత్ దర్బారు మర్యాదను, సవార్ పరిపాలనా విభాగాన్ని సూచిస్తుంది"],
         1,
         "In Akbar's Mansabdari system, 'Zat' determined the officer's personal rank and salary, while 'Sawar' specified the exact number of cavalrymen he had to maintain for imperial service.",
         "మన్సబ్దారీ విధానంలో 'జాత్' అనేది ఆ అధికారి వ్యక్తిగత హోదా మరియు వేతనాన్ని సూచించగా, 'సవార్' అనేది అతను సిద్ధంగా ఉంచాల్సిన గుర్రపు రౌతుల సంఖ్యను సూచిస్తుంది."),

        ("Modern Indian History - 1857 Revolt: Regional Leaders",
         "Match the following prominent leaders of the 1857 Great Revolt with their respective centers of rebellion:\nI. Kunwar Singh — A. Faizabad\nII. Begum Hazrat Mahal — B. Arrah (Bihar)\nIII. Maulvi Ahmadullah — C. Lucknow\nWhich of the combinations given below is correct?",
         "1857 తిరుగుబాటు నాయకులను వారి తిరుగుబాటు కేంద్రాలతో సరిగ్గా జతపరచండి:\nI. కున్వర్ సింగ్ — A. ఫైజాబాద్\nII. బేగం హజ్రత్ మహల్ — B. అర్రా (బీహార్)\nIII. మౌల్వీ అహ్మదుల్లా — C. లక్నో\nసరైన కలయిక ఏది?",
         ["I-B, II-C, III-A", "I-A, II-B, III-C", "I-C, II-A, III-B", "I-B, II-A, III-C"],
         ["I-B, II-C, III-A", "I-A, II-B, III-C", "I-C, II-A, III-B", "I-B, II-A, III-C"],
         0,
         "Kunwar Singh led from Arrah/Jagdishpur in Bihar; Begum Hazrat Mahal led the uprising from Lucknow; Maulvi Ahmadullah mobilized resistance from Faizabad.",
         "కున్వర్ సింగ్ బీహార్‌లోని జగదీష్‌పూర్/అర్రా నుండి, బేగం హజ్రత్ మహల్ లక్నో నుండి మరియు మౌల్వీ అహ్మదుల్లా ఫైజాబాద్ నుండి 1857 తిరుగుబాటుకు నాయకత్వం వహించారు."),

        ("Modern Indian History - Socio-Religious Reform: Arya Samaj",
         "Who founded the Arya Samaj in 1875 in Bombay, gave the clarion call 'Go Back to the Vedas', and authored the influential treatise 'Satyarth Prakash'?",
         "1875లో బొంబాయిలో ఆర్యసమాజ్‌ను స్థాపించి, 'వేదాలకు తరలిరండి' అనే నినాదాన్ని ఇచ్చి, ప్రసిద్ధ 'సత్యార్థ ప్రకాశ్' గ్రంథాన్ని రచించిన సంస్కర్త ఎవరు?",
         ["Raja Ram Mohan Roy", "Swami Dayanand Saraswati", "Swami Vivekananda", "Ishwar Chandra Vidyasagar"],
         ["రాజా రామ్ మోహన్ రాయ్", "స్వామి దయానంద సరస్వతి", "స్వామి వివేకానంద", "ఈశ్వర చంద్ర విద్యాసాగర్"],
         1,
         "Swami Dayanand Saraswati founded the Arya Samaj in 1875, advocated Vedic purity, opposed idol worship, and wrote 'Satyarth Prakash'.",
         "స్వామి దయానంద సరస్వతి 1875లో ఆర్యసమాజాన్ని స్థాపించారు. వేదాల ప్రామాణికతను పునరుద్ధరించాలని పిలుపునిస్తూ 'సత్యార్థ ప్రకాశ్' గ్రంథాన్ని రాశారు."),

        ("Modern Indian History - National Movement: Swadeshi 1905",
         "The historic Swadeshi Movement (1905) was sparked as a direct popular protest against which colonial policy undertaken by Viceroy Lord Curzon?",
         "వైస్రాయ్ లార్డ్ కర్జన్ చేపట్టిన ఏ వలసవాద విధానానికి నిరసనగా భారతదేశంలో చారిత్రక స్వదేశీ ఉద్యమం (1905) ఉద్భవించింది?",
         ["Partition of Bengal", "Ilbert Bill controversy", "Vernacular Press Act", "Sedition Act"],
         ["బెంగాల్ విభజన", "ఇల్బర్ట్ బిల్లు వివాదం", "వర్నాక్యులర్ ప్రెస్ చట్టం", "రాజద్రోహ చట్టం"],
         0,
         "The Swadeshi and Boycott Movement erupted in August 1905 following Lord Curzon's announcement of the Partition of Bengal to divide Hindu and Muslim populations.",
         "లార్డ్ కర్జన్ 1905లో హిందూ-ముస్లిం ఐక్యతను దెబ్బతీసేందుకు చేపట్టిన బెంగాల్ విభజనకు వ్యతిరేకంగా స్వదేశీ మరియు బహిష్కరణ ఉద్యమం ప్రారంభమైంది."),

        ("Modern Indian History - National Movement: Surat Split 1907",
         "At which Indian National Congress session held in 1907 did the historic split between the Moderates and Extremists occur over the question of extending boycott?",
         "బహిష్కరణ ఉద్యమ విస్తరణ మరియు అధ్యక్ష పదవి విషయంలో మితవాదులు మరియు అతివాదుల మధ్య వివాదం ముదిరి 1907 లో ఏ కాంగ్రెస్ సమావేశంలో చారిత్రక చీలిక ఏర్పడింది?",
         ["Calcutta Session", "Surat Session", "Madras Session", "Lahore Session"],
         ["కలకత్తా సమావేశం", "సూరత్ సమావేశం", "మద్రాస్ సమావేశం", "లాహోర్ సమావేశం"],
         1,
         "The Surat Session of 1907, presided over by Rash Behari Ghosh, witnessed an open split between the Moderates (Gokhale) and the Extremists (Tilak, Lal, Pal).",
         "1907లో రాష్ బిహారీ ఘోష్ అధ్యక్షతన జరిగిన సూరత్ కాంగ్రెస్ సమావేశంలో మితవాదులు మరియు అతివాదుల మధ్య విభేదాలు తారస్థాయికి చేరి కాంగ్రెస్ చీలిపోయింది."),

        ("Modern Indian History - National Movement: Non-Cooperation Movement",
         "Mahatma Gandhi abruptly suspended the nationwide Non-Cooperation Movement in February 1922 following which violent incident?",
         "1922 ఫిబ్రవరిలో జరిగిన ఏ హింసాత్మక దుర్ఘటన కారణంగా మహాత్మా గాంధీ దేశవ్యాప్త సహాయ నిరాకరణ ఉద్యమాన్ని హఠాత్తుగా నిలిపివేశారు?",
         ["Jallianwala Bagh Massacre", "Chauri Chaura Incident", "Kakori Train Action", "Komagata Maru Incident"],
         ["జలియన్‌వాలా బాగ్ దురంతం", "చౌరీ చౌరా ఘటన", "కాకోరీ రైలు దోపిడీ", "కోమగాటా మారు ఘటన"],
         1,
         "On February 4, 1922, a crowd set fire to a police station at Chauri Chaura (Gorakhpur, UP), killing 22 policemen. Distressed by violence, Gandhi withdrew the movement.",
         "ఉత్తరప్రదేశ్‌లోని గోరఖ్‌పూర్ వద్ద గల చౌరీ చౌరా పోలీస్ స్టేషన్‌ను ఆందోళనకారులు తగలబెట్టి 22 మంది పోలీసులను సజీవ దహనం చేయడంతో గాంధీజీ ఉద్యమాన్ని ఉపసంహరించుకున్నారు."),

        ("Modern Indian History - National Movement: Quit India 1942",
         "During the 1942 Quit India Movement, who operated an underground, clandestine radio transmitter called 'Congress Radio' to evade British colonial surveillance?",
         "1942 క్విట్ ఇండియా ఉద్యమ సమయంలో బ్రిటిష్ ప్రభుత్వ నిఘాను తప్పిస్తూ 'కాంగ్రెస్ రేడియో' పేరిట రహస్య రేడియో కేంద్రాన్ని విజయవంతంగా నడిపిన స్వాతంత్ర్య సమరయోధురాలు ఎవరు?",
         ["Aruna Asaf Ali", "Usha Mehta", "Sucheta Kripalani", "Sarojini Naidu"],
         ["అరుణా అసఫ్ అలీ", "ఉషా మెహతా", "సుచేతా కృపలానీ", "సరోజినీ నాయుడు"],
         1,
         "Usha Mehta played a pioneering role during the Quit India Movement by operating an underground radio broadcast station known as the 'Secret Congress Radio'.",
         "1942 క్విట్ ఇండియా ఉద్యమ నాయకులకు ప్రజలతో సంబంధాలు తెగిపోకుండా ఉషా మెహతా బొంబాయి కేంద్రంగా రహస్యంగా 'కాంగ్రెస్ రేడియో'ను నడిపారు.")
    ]

    for item in authored_history:
        gs_list.append(make_q(101 + len(gs_list), item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))

    assert len(gs_list) == 50, f"Expected 50 cumulative questions (16+20+14), got {len(gs_list)}"

    # ---------------------------------------------------------
    # 4. GEOGRAPHY & ENVIRONMENT (14 Qs: Q151 to Q164)
    # ---------------------------------------------------------
    authored_geog = [
        ("Indian Geography - Mountain Passes: Western Ghats",
         "Which mountain pass in the Western Ghats connects Mumbai with Pune and serves as the primary rail and highway corridor across the Sahyadri range?",
         "సహ్యాద్రి పర్వత శ్రేణులలో ముంబై మరియు పూణే నగరాలను కలుపుతూ ప్రధాన రహదారి మరియు రైలు మార్గంగా ఉపయోగపడే పశ్చిమ కనుమల కనుమ (Pass) ఏది?",
         ["Thal Ghat", "Bhor Ghat", "Palghat Gap", "Shencottah Gap"],
         ["థాల్ ఘాట్", "భోర్ ఘాట్", "పాల్ఘాట్ గ్యాప్", "షెన్‌కోట్టా గ్యాప్"],
         1,
         "Bhor Ghat connects Mumbai with Pune in Maharashtra. Thal Ghat connects Mumbai with Nashik, while Palghat connects Kerala with Tamil Nadu.",
         "మహారాష్ట్రలోని భోర్ ఘాట్ ముంబై-పూణే నగరాలను కలుపుతుంది. థాల్ ఘాట్ ముంబై-నాసిక్ నగరాలను మరియు పాల్ఘాట్ కేరళ-తమిళనాడులను కలుపుతాయి."),

        ("Indian Geography - River Drainage: Krishna Basin",
         "Which of the following major tributaries of River Krishna originates in Karnataka and joins the Krishna River near Alampur in Telangana?",
         "కృష్ణా నది యొక్క ప్రధాన ఉపనదులలో కర్ణాటకలో జన్మించి తెలంగాణలోని అలంపూర్ సమీపంలో కృష్ణా నదిలో సంగమించే నది ఏది?",
         ["Bhima River", "Tungabhadra River", "Koyna River", "Ghataprabha River"],
         ["భీమా నది", "తుంగభద్ర నది", "కొయ్నా నది", "ఘటప్రభ నది"],
         1,
         "The Tungabhadra River, formed by the union of the Tunga and Bhadra rivers in Karnataka, flows eastwards and merges with the Krishna River near Alampur in Jogulamba Gadwal district.",
         "కర్ణాటకలో తుంగ మరియు భద్ర నదుల కలయికతో ఏర్పడిన తుంగభద్ర నది తెలంగాణలోని జోగులాంబ గద్వాల జిల్లా అలంపూర్ సమీపంలో కృష్ణా నదిలో కలుస్తుంది."),

        ("Indian Geography - Climate: Southwest Monsoon",
         "The Southwest Monsoon in India splits into two main branches upon reaching the Indian landmass. What are these two distinct branches?",
         "భారత భూభాగాన్ని తాకిన తర్వాత నైరుతి రుతుపవనాలు రెండు ప్రధాన శాఖలుగా చీలిపోతాయి. ఆ రెండు శాఖలు ఏవి?",
         ["Arabian Sea branch and Bay of Bengal branch", "Northern branch and Southern branch", "Himalayan branch and Peninsular branch", "Western branch and Coromandel branch"],
         ["అరేబియా సముద్ర శాఖ మరియు బంగాళాఖాతం శాఖ", "ఉత్తర శాఖ మరియు దక్షిణ శాఖ", "హిమాలయ శాఖ మరియు ద్వీపకల్ప శాఖ", "పశ్చిమ శాఖ మరియు కోరమాండల్ శాఖ"],
         0,
         "The Southwest Monsoon bifurcates into the Arabian Sea branch (which brings rain to Western Ghats) and the Bay of Bengal branch (which moves towards Bengal and Assam).",
         "నైరుతి రుతుపవనాలు భారతదేశాన్ని తాకి అరేబియా సముద్ర శాఖ మరియు బంగాళాఖాతం శాఖలుగా చీలి దేశవ్యాప్తంగా విస్తారమైన వర్షపాతాన్ని ఇస్తాయి."),

        ("Indian Geography - Soils of India: Black Regur Soil",
         "Black soils (Regur soils), famous for dry-farming and commercial cotton cultivation, are primarily derived from the weathering of which type of volcanic rocks?",
         "పత్తి సాగుకు అత్యంత అనుకూలమైన 'రేగడి నేలలు' (నల్లరేగడి నేలలు) ఏ రకమైన అగ్నిపర్వత శిలలు శైథిల్యం చెందడం ద్వారా ఏర్పడ్డాయి?",
         ["Granite rocks", "Basaltic lava rocks (Deccan Trap)", "Sandstone rocks", "Limestone rocks"],
         ["గ్రెనైట్ శిలలు", "బసాల్ట్ లావా శిలలు (దక్కన్ ట్రాప్)", "ఇసుకరాయి శిలలు", "సున్నపురాయి శిలలు"],
         1,
         "Black soils are formed due to the weathering of basaltic rocks of the Deccan volcanic plateau. They are clayey, moisture-retentive, and rich in calcium carbonate and potash.",
         "దక్కన్ పీఠభూమిలోని బసాల్ట్ లావా శిలల శైథిల్యం వల్ల నల్లరేగడి నేలలు ఏర్పడ్డాయి. వీటిలో తేమను నిల్వ ఉంచుకునే సామర్థ్యం అధికం, ఇవి పత్తి పంటకు ప్రసిద్ధి."),

        ("Indian Geography - Minerals & Mining",
         "Which mining region in Karnataka is globally renowned for vast deposits of hematite and magnetite iron ore, transported via pipelines to Mangalore port?",
         "కర్ణాటకలోని ఏ ప్రాంతం హెమటైట్ మరియు మాగ్నటైట్ ఇనుప ఖనిజ నిక్షేపాలకు ప్రసిద్ధి చెందింది మరియు పైప్‌లైన్ల ద్వారా మంగళూరు ఓడరేవుకు రవాణా చేయబడుతుంది?",
         ["Kolar Gold Fields", "Kudremukh", "Hutti", "Panna"],
         ["కోలార్ గోల్డ్ ఫీల్డ్స్", "కుద్రేముఖ్", "హుట్టి", "పన్నా"],
         1,
         "Kudremukh in the Western Ghats of Karnataka is known for its massive iron ore deposits. Slurry pipeline technology was used to transport ore to Mangalore port.",
         "కర్ణాటకలోని కుద్రేముఖ్ ఇనుప ఖనిజ నిక్షేపాలకు ప్రసిద్ధి. ఇక్కడి నుండి స్లర్రీ పైప్‌లైన్ ద్వారా మంగళూరు పోర్టుకు ఖనిజాన్ని రవాణా చేస్తారు."),

        ("Environment & Ecology - Protected Areas: Biosphere Reserves",
         "What is the designated zonation structure of a UNESCO Man and Biosphere (MAB) reserve from the interior core outwards?",
         "యునెస్కో 'మ్యాన్ అండ్ బయోస్పియర్' (MAB) నిబంధనల ప్రకారం బయోస్పియర్ రిజర్వ్ లోపలి నుండి వెలుపలికి ఉండే సరైన మండల విభజన ఏది?",
         ["Core zone -> Buffer zone -> Transition zone", "Buffer zone -> Core zone -> Transition zone", "Transition zone -> Buffer zone -> Core zone", "Core zone -> Industrial zone -> Urban zone"],
         ["కోర్ జోన్ -> బఫర్ జోన్ -> ట్రాన్సిషన్ జోన్", "బఫర్ జోన్ -> కోర్ జోన్ -> ట్రాన్సిషన్ జోన్", "ట్రాన్సిషన్ జోన్ -> బఫర్ జోన్ -> కోర్ జోన్", "కోర్ జోన్ -> ఇండస్ట్రియల్ జోన్ -> అర్బన్ జోన్"],
         0,
         "A Biosphere Reserve has 3 zones: Core zone (strictly protected legal area), Buffer zone (limited research and tourism), and Transition zone (human settlements and sustainable agriculture).",
         "బయోస్పియర్ రిజర్వ్ మూడు విభాగాలుగా ఉంటుంది: కోర్ జోన్ (పూర్తి రక్షిత ప్రాంతం), బఫర్ జోన్ (పరిశోధనలు, విద్య), మరియు ట్రాన్సిషన్ జోన్ (మానవ నివాసాలు, సుస్థిర వ్యవసాయం)."),

        ("Environment & Ecology - Biodiversity Hotspots",
         "Which of the following biogeographical regions of India is recognized as one of the world's 36 global Biodiversity Hotspots possessing exceptionally high species endemism?",
         "భారతదేశంలోని క్రింది భౌగోళిక ప్రాంతాలలో అత్యధిక స్థానిక జాతులు (Endemic species) కలిగి ప్రపంచంలోని 36 బయోడైవర్సిటీ హాట్‌స్పాట్లలో ఒకటిగా గుర్తింపు పొందినది ఏది?",
         ["Thar Desert", "Western Ghats", "Indo-Gangetic Plain", "Deccan Plateau Interior"],
         ["థార్ ఎడారి", "పశ్చిమ కనుమలు", "గంగా-సింధు మైదానం", "దక్కన్ అంతర్గత పీఠభూమి"],
         1,
         "The Western Ghats (along with the Himalayas, Indo-Burma, and Sundaland) is recognized as a global biodiversity hotspot with high floral and faunal endemism.",
         "పశ్చిమ కనుమలు ప్రపంచంలోని 36 జీవవైవిధ్య హాట్‌స్పాట్లలో ఒకటి. ఇక్కడ అనేక రకాల అరుదైన వృక్ష, జంతు జాతులు కేంద్రీకృతమై ఉన్నాయి."),

        ("Environment & Ecology - International Conventions: Ramsar",
         "The Ramsar Convention, signed in 1971 in the Iranian city of Ramsar, is an intergovernmental environmental treaty dedicated to the conservation and wise use of:",
         "1971 లో ఇరాన్ నగరమైన రామ్‌సర్‌లో ఆమోదించబడిన 'రామ్‌సర్ కన్వెన్షన్' వేటి సంరక్షణ మరియు సుస్థిర వినియోగానికి ఉద్దేశించిన అంతర్జాతీయ పర్యావరణ ఒప్పందం?",
         ["Wetlands", "Tropical Rainforests", "Coral Reefs", "Migratory Birds"],
         ["చిత్తడి నేలలు (Wetlands)", "ఉష్ణమండల వర్షారణ్యాలు", "పగడపు దిబ్బలు", "వలస పక్షులు"],
         0,
         "The Ramsar Convention on Wetlands provides the framework for national action and international cooperation for the conservation of wetlands and their resources.",
         "1971 రామ్‌సర్ కన్వెన్షన్ ప్రపంచవ్యాప్తంగా ఉన్న చిత్తడి నేలల (Wetlands) సంరక్షణ మరియు వాటి సహజ వనరుల సుస్థిర నిర్వహణకు ఉద్దేశించబడింది."),

        ("Environment & Ecology - Wildlife Conservation: Project Tiger",
         "In which year was the flagship wildlife conservation initiative 'Project Tiger' launched in India to protect Bengal tigers and their natural habitats?",
         "భారతదేశంలో బెంగాల్ పులులు మరియు వాటి సహజ ఆవాసాలను పరిరక్షించే లక్ష్యంతో 'ప్రాజెక్ట్ టైగర్' కార్యక్రమం ఏ సంవత్సరంలో ప్రారంభించబడింది?",
         ["1971", "1973", "1980", "1992"],
         ["1971", "1973", "1980", "1992"],
         1,
         "Project Tiger was launched on April 1, 1973 from Jim Corbett National Park in Uttarakhand to ensure a viable population of tigers in India.",
         "భారత ప్రభుత్వం 1973 ఏప్రిల్ 1న జిమ్ కార్బెట్ జాతీయ పార్క్ నుండి ప్రాజెక్ట్ టైగర్‌ను ప్రారంభించింది. ఇది ప్రపంచంలోనే అతిపెద్ద వన్యప్రాణి పరిరక్షణ కార్యక్రమాలలో ఒకటి."),

        ("Physical Geography - Atmosphere: Ozone Layer",
         "In which atmospheric layer is the stratospheric ozone layer located, which shields life on Earth by absorbing hazardous ultraviolet (UV) solar radiation?",
         "సూర్యుని నుండి వచ్చే ప్రమాదకరమైన అతినీలలోహిత (UV) వికిరణాన్ని శోషించుకోవడం ద్వారా భూమిపై జీవరాశిని రక్షించే 'ఓజోన్ పొర' వాతావరణంలోని ఏ పొరలో కేంద్రీకృతమై ఉంది?",
         ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
         ["ట్రోపోస్పియర్", "స్ట్రాటోస్పియర్", "మీసోస్పియర్", "థర్మోస్పియర్"],
         1,
         "The ozone layer is concentrated in the Stratosphere between 15 km and 35 km above Earth's surface, absorbing harmful UV-B radiation from the sun.",
         "స్ట్రాటోస్పియర్‌లో భూమి ఉపరితలం నుండి 15 నుండి 35 కి.మీ ఎత్తులో ఓజోన్ పొర కేంద్రీకృతమై ఉంటుంది. ఇది సూర్యుని నుండి వచ్చే హానికర అతినీలలోహిత కిరణాలను అడ్డుకుంటుంది."),

        ("Indian Geography - River Drainage: West Flowing Rivers",
         "Which of the following major rivers of Peninsular India flows westward through a rift valley between the Vindhya and Satpura mountain ranges into the Arabian Sea?",
         "ద్వీపకల్ప భారతదేశంలో వింధ్య మరియు సాత్పురా పర్వత శ్రేణుల మధ్య పగులు లోయ (Rift Valley) గుండా పశ్చిమంగా ప్రవహిస్తూ అరేబియా సముద్రంలో కలిసే నది ఏది?",
         ["Godavari River", "Mahanadi River", "Narmada River", "Cauvery River"],
         ["గోదావరి నది", "మహానది", "నర్మదా నది", "కావేరి నది"],
         2,
         "The Narmada River originates from Amarkantak plateau in Madhya Pradesh, flows westwards through a rift valley between Vindhyas and Satpuras, and drains into the Gulf of Khambhat.",
         "నర్మదా నది అమర్‌కంటక్ వద్ద జన్మించి, వింధ్య-సాత్పురా శ్రేణుల మధ్య గల పగులు లోయ గుండా పశ్చిమంగా ప్రవహిస్తూ ఖంభాట్ సింధుశాఖలో కలుస్తుంది."),

        ("Telangana Geography - Forests: Amrabad Tiger Reserve",
         "Which is the largest tiger reserve in Telangana, situated across the scenic Nallamala forest hills?",
         "నల్లమల అటవీ ప్రాంతంలో విస్తరించి ఉన్న తెలంగాణలోని అతిపెద్ద టైగర్ రిజర్వ్ ఏది?",
         ["Kawal Tiger Reserve", "Amrabad Tiger Reserve", "Pakhal Wildlife Sanctuary", "Pocharam Sanctuary"],
         ["కవ్వాల్ టైగర్ రిజర్వ్", "అమ్రాబాద్ టైగర్ రిజర్వ్", "పాఖాల్ వన్యప్రాణి అభయారణ్యం", "పోచారం అభయారణ్యం"],
         1,
         "Amrabad Tiger Reserve, spanning Nagarkurnool and Nalgonda districts in the Nallamala hills, is the largest tiger reserve in Telangana and the second largest in India by area.",
         "నల్లమల కొండల్లో విస్తరించి ఉన్న అమ్రాబాద్ టైగర్ రిజర్వ్ తెలంగాణలోనే అతిపెద్దది మరియు విస్తీర్ణంలో భారతదేశంలో రెండవ అతిపెద్ద టైగర్ రిజర్వ్."),

        ("Telangana Geography - River Confluences: Godavari Basin",
         "Near which holy pilgrimage center in Mancherial/Jayashankar Bhupalpally does the Pranahita river merge with the Godavari river?",
         "గోదావరి నదిలో ప్రాణహిత నది సంగమించే ప్రసిద్ధ పుణ్యక్షేత్రం ఏది?",
         ["Bhadrachalam", "Kaleshwaram", "Basar", "Dharmapuri"],
         ["భద్రాచలం", "కాళేశ్వరం", "బాసర", "ధర్మపురి"],
         1,
         "At Kaleshwaram, the Pranahita river merges with the Godavari river, forming the sacred Triveni Sangamam (with the underground Saraswati).",
         "కాళేశ్వరం వద్ద గోదావరి, ప్రాణహిత నదులు సంగమిస్తాయి. ఇక్కడి ముక్తేశ్వర క్షేత్రం త్రివేణి సంగమంగా ప్రసిద్ధి చెందింది."),

        ("Telangana Geography - Irrigation: Medigadda Barrage",
         "Under the Kaleshwaram Lift Irrigation Project (KLIP), what is the starting origin barrage constructed across the Godavari river below the confluence with Pranahita?",
         "కాళేశ్వరం ఎత్తిపోతల ప్రాజెక్టులో భాగంగా ప్రాణహిత-గోదావరి సంగమం దిగువన నిర్మించబడిన ప్రారంభ బ్యారేజీ పేరు ఏమిటి?",
         ["Sundilla Barrage", "Medigadda (Lakshmi) Barrage", "Annaram (Saraswati) Barrage", "Mid Manair Dam"],
         ["సుందిళ్ల బ్యారేజీ", "మేడిగడ్డ (లక్ష్మి) బ్యారేజీ", "అన్నారం (సరస్వతి) బ్యారేజీ", "మిడ్ మానేరు డ్యామ్"],
         1,
         "Medigadda Barrage (officially Lakshmi Barrage) is the foundation and starting barrage of the Kaleshwaram Lift Irrigation Project located in Jayashankar Bhupalpally district.",
         "కాళేశ్వరం ప్రాజెక్టు మొదటి దశలో భాగంగా ప్రాణహిత నీటిని ఎత్తిపోయడానికి నిర్మించిన ప్రారంభ బ్యారేజీ మేడిగడ్డ (లక్ష్మి) బ్యారేజీ.")
    ]

    for item in authored_geog:
        gs_list.append(make_q(101 + len(gs_list), item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))

    assert len(gs_list) == 64, f"Expected 64 cumulative questions (16+20+14+14), got {len(gs_list)}"

    # ---------------------------------------------------------
    # 5. INDIAN & TELANGANA ECONOMY (10 Qs: Q165 to Q174)
    # ---------------------------------------------------------
    authored_econ = [
        ("Indian Economy - Fiscal Federalism: 15th Finance Commission",
         "What vertical devolution share was recommended by the Fifteenth Finance Commission (headed by N.K. Singh) for the devolution of the divisible pool of central taxes to the States?",
         "ఎన్.కె. సింగ్ అధ్యక్షతన ఏర్పడిన 15వ ఆర్థిక సంఘం కేంద్ర పన్నుల విభజించదగిన నిధి నుండి రాష్ట్రాలకు ఎంత శాతం నిధులను బదిలీ చేయాలని (వర్టికల్ డివాల్యూషన్) సిఫార్సు చేసింది?",
         ["32%", "41%", "42%", "50%"],
         ["32%", "41%", "42%", "50%"],
         1,
         "The 15th Finance Commission recommended a vertical devolution share of 41% to States (adjusted from 14th FC's 42% due to Jammu & Kashmir and Ladakh becoming Union Territories).",
         "15వ ఆర్థిక సంఘం రాష్ట్రాల వాటాను 41% గా సిఫార్సు చేసింది (జమ్మూ కాశ్మీర్ మరియు లడఖ్ కేంద్రపాలిత ప్రాంతాలుగా మారినందున 14వ సంఘం సిఫార్సు చేసిన 42% నుండి 1% తగ్గించారు)."),

        ("Indian Economy - Monetary Policy: RBI Repo Rate",
         "What is defined as the 'Repo Rate' in the Reserve Bank of India's monetary policy toolkit?",
         "భారత రిజర్వ్ బ్యాంక్ (RBI) ద్రవ్య విధానంలో 'రెపో రేటు' (Repo Rate) అంటే ఏమిటి?",
         ["The rate at which commercial banks borrow short-term funds from RBI against approved government securities", "The rate at which RBI borrows funds from commercial banks", "The statutory percentage of deposits banks must keep as liquid cash", "The minimum lending rate below which banks cannot lend to borrowers"],
         ["వాణిజ్య బ్యాంకులు ప్రభుత్వ సెక్యూరిటీల పూచీకత్తుపై RBI నుండి స్వల్పకాలిక రుణాలు పొందే వడ్డీ రేటు", "RBI వాణిజ్య బ్యాంకుల నుండి నిధులను సేకరించే వడ్డీ రేటు", "బ్యాంకులు తమ డిపాజిట్లలో నగదు రూపంలో ఉంచుకోవాల్సిన చట్టబద్ధమైన శాతం", "బ్యాంకులు వినియోగదారులకు రుణాలు ఇచ్చే కనీస పరిమితి వడ్డీ రేటు"],
         0,
         "Repo Rate (Repurchase Option rate) is the policy rate at which the RBI lends money to commercial banks against government securities to control liquidity and inflation.",
         "ద్రవ్యోల్బణాన్ని నియంత్రించేందుకు వాణిజ్య బ్యాంకులకు RBI ప్రభుత్వ సెక్యూరిటీల హామీతో స్వల్పకాలిక రుణాలు ఇచ్చే రేటును రెపో రేటు అంటారు."),

        ("Indian Economy - Inflation: Headline vs Core",
         "In macroeconomics, how is 'Core Inflation' derived from 'Headline Inflation'?",
         "స్థూల ఆర్థిక శాస్త్రంలో 'కోర్ ద్రవ్యోల్బణం' (Core Inflation) ను 'హెడ్‌లైన్ ద్రవ్యోల్బణం' నుండి ఎలా లెక్కిస్తారు?",
         ["Headline inflation minus volatile food and fuel components", "Headline inflation plus import tariffs", "Headline inflation adjusted for depreciation", "Headline inflation minus manufacturing goods"],
         ["హెడ్‌లైన్ ద్రవ్యోల్బణం నుండి హెచ్చుతగ్గులు ఉండే ఆహార మరియు ఇంధన వస్తువులను మినహాయించడం ద్వారా", "హెడ్‌లైన్ ద్రవ్యోల్బణానికి దిగుమతి సుంకాలను కలపడం ద్వారా", "హెడ్‌లైన్ ద్రవ్యోల్బణం నుండి తరుగుదలను సర్దుబాటు చేయడం ద్వారా", "హెడ్‌లైన్ ద్రవ్యోల్బణం నుండి తయారీ రంగాన్ని తొలగించడం ద్వారా"],
         0,
         "Core Inflation excludes volatile items such as food and energy/fuel prices, providing a clearer measure of underlying long-term price trends.",
         "కోర్ ద్రవ్యోల్బణం అనేది తరచుగా ధరల్లో హెచ్చుతగ్గులు ఉండే ఆహారం మరియు ఇంధనం ధరలను మినహాయించి దీర్ఘకాలిక ధరల ధోరణిని లెక్కించే కొలమానం."),

        ("Indian Economy - National Income: GDP vs GNP",
         "What is the exact mathematical relationship between Gross National Product (GNP) and Gross Domestic Product (GDP)?",
         "స్థూల జాతీయోత్పత్తి (GNP) మరియు స్థూల దేశీయోత్పత్తి (GDP) ల మధ్య గల సరైన సంబంధం ఏది?",
         ["GNP = GDP + Net Factor Income from Abroad (NFIA)", "GNP = GDP - Depreciation", "GNP = GDP + Indirect Taxes - Subsidies", "GNP = GDP - Net Exports"],
         ["GNP = GDP + విదేశాల నుండి వచ్చే నికర కారక ఆదాయం (NFIA)", "GNP = GDP - తరుగుదల", "GNP = GDP + పరోక్ష పన్నులు - రాయితీలు", "GNP = GDP - నికర ఎగుమతులు"],
         0,
         "GNP measures the economic output produced by normal residents of a country: GNP = GDP + NFIA (Net Factor Income from Abroad).",
         "GNP = GDP + విదేశాల నుండి లభించే నికర కారక ఆదాయం (NFIA). ఇది ఒక దేశ పౌరులు దేశంలో మరియు విదేశాలలో సంపాదించిన మొత్తం ఆదాయాన్ని సూచిస్తుంది."),

        ("Indian Economy - Banking Reforms: Priority Sector Lending",
         "Under RBI guidelines, domestic scheduled commercial banks are mandated to allocate what minimum percentage of their Adjusted Net Bank Credit (ANBC) to Priority Sector Lending (PSL)?",
         "RBI నిబంధనల ప్రకారం దేశీయ షెడ్యూల్డ్ వాణిజ్య బ్యాంకులు తమ నికర రుణాలలో (ANBC) కనీసం ఎంత శాతాన్ని ప్రాధాన్యతా రంగానికి (PSL) రుణాల రూపంలో అందించాలి?",
         ["25%", "33%", "40%", "50%"],
         ["25%", "33%", "40%", "50%"],
         2,
         "Domestic commercial banks and foreign banks with 20 or more branches must allocate 40% of ANBC to priority sectors including agriculture, MSMEs, education, and housing.",
         "వాణిజ్య బ్యాంకులు వ్యవసాయం, MSME, విద్య, గృహ నిర్మాణం వంటి ప్రాధాన్యతా రంగాలకు తమ మొత్తం రుణాలలో కనీసం 40% నిధులను కేటాయించాలి."),

        ("Indian Economy - Taxation: GST Council",
         "Under Article 279A of the Constitution, what voting weightage is assigned to the Central Government in decisions taken by the Goods and Services Tax (GST) Council?",
         "రాజ్యాంగంలోని అధికరణ 279A ప్రకారం జిఎస్‌టి కౌన్సిల్ (GST Council) లో నిర్ణయాలు తీసుకునేటప్పుడు కేంద్ర ప్రభుత్వానికి గల ఓటింగ్ వాటా (వెయిటేజీ) ఎంత?",
         ["One-fourth (1/4th) of the total votes cast", "One-third (1/3rd) of the total votes cast", "One-half (1/2) of the total votes cast", "Two-thirds (2/3rds) of the total votes cast"],
         ["పోలైన మొత్తం ఓట్లలో నాల్గవ వంతు (1/4)", "పోలైన మొత్తం ఓట్లలో మూడవ వంతు (1/3)", "పోలైన మొత్తం ఓట్లలో సగం (1/2)", "పోలైన మొత్తం ఓట్లలో మూడింట రెండు వంతులు (2/3)"],
         1,
         "In the GST Council, the Central Government has a weightage of one-third (1/3rd) of total votes cast, while all State Governments combined have two-thirds (2/3rds) weightage.",
         "జీఎస్టీ కౌన్సిల్‌లో నిర్ణయాలకు 3/4వ వంతు మెజారిటీ అవసరం. ఇందులో కేంద్ర ప్రభుత్వానికి 1/3వ వంతు ఓటింగ్ బలం మరియు రాష్ట్రాలన్నింటికీ కలిపి 2/3వ వంతు బలం ఉంటుంది."),

        ("Indian Economy - Fiscal Policy: Deficits",
         "In public finance, what is defined as the 'Primary Deficit'?",
         "ప్రభుత్వ విత్త శాస్త్రంలో 'ప్రాథమిక లోటు' (Primary Deficit) అంటే ఏమిటి?",
         ["Fiscal Deficit minus Interest Payments", "Revenue Deficit minus Capital Expenditure", "Total Expenditure minus Total Receipts", "Budget Deficit minus Disinvestment Proceeds"],
         ["ద్రవ్య లోటు నుండి వడ్డీ చెల్లింపులను తీసివేయగా వచ్చేది", "రెవెన్యూ లోటు నుండి మూలధన వ్యయాన్ని తీసివేయగా వచ్చేది", "మొత్తం వ్యయం నుండి మొత్తం రాబడులను తీసివేయగా వచ్చేది", "బడ్జెట్ లోటు నుండి పెట్టుబడుల ఉపసంహరణను తీసివేయగా వచ్చేది"],
         0,
         "Primary Deficit is Fiscal Deficit minus interest payments on past borrowings. It reflects current government borrowing requirements excluding debt servicing.",
         "ప్రాథమిక లోటు = ద్రవ్య లోటు - గత రుణాలపై చెల్లించే వడ్డీలు. ప్రస్తుత ఆర్థిక సంవత్సరపు ప్రభుత్వ వాస్తవ రుణ అవసరాలను ఇది తెలుపుతుంది."),

        ("Telangana Economy - Sectoral Contribution to GSDP",
         "Which broad sector of the economy accounts for the largest share (over 60%) of Telangana's Gross State Domestic Product (GSDP)?",
         "తెలంగాణ స్థూల రాష్ట్ర దేశీయోత్పత్తిలో (GSDP) అత్యధిక వాటాను (60% కంటే ఎక్కువ) కలిగి ఉన్న ప్రధాన రంగం ఏది?",
         ["Agriculture & Allied Sector", "Industrial & Manufacturing Sector", "Services Sector", "Mining & Quarrying Sector"],
         ["వ్యవసాయం మరియు అనుబంధ రంగాలు", "పారిశ్రామిక మరియు తయారీ రంగం", "సేవల రంగం (Services Sector)", "గనుల తవ్వకం రంగం"],
         2,
         "The Services Sector (IT, financial services, real estate, trade, transport) dominates Telangana's GSDP, contributing over 63% to the state's economy.",
         "తెలంగాణ ఆర్థిక వ్యవస్థలో సేవా రంగం (ఐటీ, బ్యాంకింగ్, రియల్ ఎస్టేట్, వాణిజ్యం) అత్యంత కీలకమైనది, ఇది రాష్ట్ర జీఎస్డీపీలో 63% కంటే ఎక్కువ వాటాను కలిగి ఉంది."),

        ("Telangana Economy - State Own Tax Revenue (SOTR)",
         "Which of the following heads constitutes the single largest contributor to Telangana's State Own Tax Revenue (SOTR)?",
         "తెలంగాణ రాష్ట్ర స్వంత పన్ను రాబడిలో (SOTR) అత్యధిక ఆదాయాన్ని సమకూర్చే ప్రధాన పన్ను విభాగం ఏది?",
         ["State Goods and Services Tax (SGST)", "State Excise Duties on Liquor", "Stamps and Registration Fees", "Taxes on Motor Vehicles"],
         ["స్టేట్ జీఎస్టీ (SGST)", "రాష్ట్ర ఎక్సైజ్ సుంకం", "స్టాంపులు మరియు రిజిస్ట్రేషన్ ఫీజులు", "మోటారు వాహనాల పన్నులు"],
         0,
         "SGST is the single largest component of Telangana's Own Tax Revenue, followed by State Excise duties, Sales Tax (on petroleum), and Stamps and Registration fees.",
         "తెలంగాణ స్వంత పన్నుల రాబడిలో స్టేట్ జీఎస్టీ (SGST) అత్యధిక ఆదాయాన్ని అందించే ప్రధాన వనరుగా ఉంది, ఆ తర్వాత ఎక్సైజ్ మరియు స్టాంపుల విభాగం ఉన్నాయి."),

        ("Telangana Economy - Industrial Infrastructure: Life Sciences",
         "Hyderabad's Genome Valley, established as India's first organized life sciences cluster, is renowned for hosting which of the following global industries?",
         "భారతదేశంలోనే మొట్టమొదటి వ్యవస్థీకృత లైఫ్ సైన్సెస్ క్లస్టర్‌గా ప్రసిద్ధి చెందిన హైదరాబాద్‌లోని 'జీనోమ్ వ్యాలీ' క్రింది వాటిలో వేటికి ప్రధాన కేంద్రంగా ఉంది?",
         ["Textile manufacturing & power looms", "Vaccine manufacturing, biotechnology and R&D facilities", "Heavy earthmoving machinery manufacturing", "Automobile assembly and electric vehicles"],
         ["వస్త్ర తయారీ మరియు మరమగ్గాలు", "వ్యాక్సిన్ల తయారీ, బయోటెక్నాలజీ మరియు ఫార్మా పరిశోధన", "భారీ యంత్రాల తయారీ", "ఆటోమొబైల్ మరియు ఎలక్ట్రిక్ వాహనాల తయారీ"],
         1,
         "Genome Valley in Hyderabad is India's premier life sciences and biotechnology hub, home to Bharat Biotech, Biological E, and global R&D centers, producing 1/3rd of the world's vaccines.",
         "హైదరాబాద్ సమీపంలోని జీనోమ్ వ్యాలీ ప్రపంచ ప్రసిద్ధి చెందిన వ్యాక్సిన్ల తయారీ మరియు బయోటెక్నాలజీ హబ్. ప్రపంచంలోని టీకాలలో దాదాపు మూడో వంతు ఇక్కడే ఉత్పత్తి అవుతాయి.")
    ]

    for item in authored_econ:
        gs_list.append(make_q(101 + len(gs_list), item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))

    assert len(gs_list) == 74, f"Expected 74 cumulative questions (16+20+14+14+10), got {len(gs_list)}"

    # ---------------------------------------------------------
    # 6. GENERAL SCIENCE & TECHNOLOGY (14 Qs: Q175 to Q188)
    # ---------------------------------------------------------
    # FCB 102 (LRLACM), 103 (Proba-3)
    for fid in [102, 103]:
        q = fcb_map[fid]
        gs_list.append(make_q(
            101 + len(gs_list), q.get('topic', 'Science & Defence Technology'),
            q['question_en'], q['question_te'],
            q['options_en'], q['options_te'],
            q['correct_option'], q['explanation_en'], q['explanation_te']
        ))

    authored_science = [
        ("Physics - Optics: Total Internal Reflection",
         "The transmission of high-speed optical data through optical fiber cables operates on which fundamental optical principle?",
         "ఆప్టికల్ ఫైబర్ కేబుల్స్ ద్వారా అత్యంత వేగంగా డేటా సంకేతాలు ప్రసారమయ్యే భౌతిక దృగ్విషయం ఏది?",
         ["Refraction of light", "Total Internal Reflection", "Diffraction of light", "Polarization of light"],
         ["కాంతి వక్రీభవనం", "సంపూర్ణ అంతర్గత పరావర్తనం (Total Internal Reflection)", "కాంతి వివర్తనం", "కాంతి ధ్రువణం"],
         1,
         "Optical fibers utilize Total Internal Reflection: when light enters at an angle greater than the critical angle, it undergoes continuous internal reflection with minimal loss.",
         "ఆప్టికల్ ఫైబర్స్ సంపూర్ణ అంతర్గత పరావర్తనం సూత్రంపై పనిచేస్తాయి. కాంతి సందిగ్ధ కోణం కంటే ఎక్కువ కోణంలో ప్రవేశించినప్పుడు పూర్తి పరావర్తనం చెందుతూ ప్రయాణిస్తుంది."),

        ("Physics - Mechanics: Newton's Laws",
         "The recoil of a rifle when a bullet is fired from it is a direct practical illustration of which of Newton's Laws of Motion?",
         "తుపాకీ నుండి బుల్లెట్ దూసుకెళ్లినప్పుడు తుపాకీ వెనక్కి తన్నడం (Recoil) అనేది న్యూటన్ ఏ గమన నియమానికి ప్రత్యక్ష ఉదాహరణ?",
         ["Newton's First Law of Motion", "Newton's Second Law of Motion", "Newton's Third Law of Motion", "Newton's Law of Universal Gravitation"],
         ["న్యూటన్ మొదటి గమన నియమం", "న్యూటన్ రెండవ గమన నియమం", "న్యూటన్ మూడవ గమన నియమం", "న్యూటన్ విశ్వ గురుత్వాకర్షణ నియమం"],
         2,
         "Newton's Third Law states that every action has an equal and opposite reaction. The bullet is pushed forward (action), imparting an equal momentum backward to the gun (reaction).",
         "న్యూటన్ మూడవ నియమం ప్రకారం ప్రతి చర్యకూ సమానమైన మరియు వ్యతిరేక దిశలో ప్రతిచర్య ఉంటుంది. బుల్లెట్ ముందుకు వెళ్లడం చర్య అయితే, తుపాకీ వెనక్కి నెట్టబడటం ప్రతిచర్య."),

        ("Physics - Waves & Sound: Ultrasonic Waves",
         "Ultrasonic waves, commonly utilized in medical sonography and naval SONAR navigation, have frequencies:",
         "వైద్య రంగంలో సోనోగ్రఫీ మరియు నౌకాదళ సోనార్ (SONAR) వ్యవస్థలలో ఉపయోగించే అల్ట్రాసోనిక్ (అతిధ్వని) తరంగాల పౌనఃపున్యం ఎంత ఉంటుంది?",
         ["Below 20 Hz", "Between 20 Hz and 20,000 Hz", "Above 20,000 Hz (20 kHz)", "Between 10 Hz and 100 Hz"],
         ["20 Hz కంటే తక్కువ", "20 Hz నుండి 20,000 Hz మధ్య", "20,000 Hz (20 kHz) కంటే ఎక్కువ", "10 Hz నుండి 100 Hz మధ్య"],
         2,
         "Human audible sound range is 20 Hz to 20 kHz. Sound waves with frequencies above 20 kHz are termed ultrasonic waves, used in ultrasound imaging and submarine SONAR.",
         "మానవ చెవి వినగలిగే శ్రవ్య అవధి 20 నుండి 20,000 Hz. 20,000 Hz (20 kHz) కంటే ఎక్కువ పౌనఃపున్యం కలిగిన తరంగాలను అతిధ్వనులు (Ultrasonic) అంటారు."),

        ("Physics - Electricity: Domestic Circuits",
         "Why are domestic electrical appliances in household wiring connected in parallel rather than in series?",
         "గృహ అవసరాలకు ఉపయోగించే విద్యుత్ ఉపకరణాలను శ్రేణిలో కాకుండా సమాంతర సంధానంలో (Parallel) ఎందుకు కలుపుతారు?",
         ["To ensure that each appliance receives the full mains voltage and can be switched on/off independently", "To minimize total power consumption to zero", "To reduce the required current from the transformer", "To prevent fuse wires from blowing"],
         ["ప్రతి ఉపకరణానికి పూర్తి వోల్టేజ్ అందేలా చూడటానికి మరియు ఒకదానితో సంబంధం లేకుండా విడివిడిగా ఆన్/ఆఫ్ చేయడానికి", "మొత్తం విద్యుత్ వాడకాన్ని సున్నాకి తగ్గించడానికి", "ట్రాన్స్‌ఫార్మర్ నుండి వచ్చే కరెంట్‌ను తగ్గించడానికి", "ఫ్యూజ్ వైర్లు కాలిపోకుండా నిరోధించడానికి"],
         0,
         "In parallel connection, every appliance receives the full supply voltage (220V) and operates independently; if one fails, others remain unaffected.",
         "సమాంతర సంధానంలో ప్రతి ఉపకరణానికి సమానమైన వోల్టేజ్ (220V) అందుతుంది మరియు ఒక ఉపకరణం పాడైనా మిగతావి ఎలాంటి ఆటంకం లేకుండా పనిచేస్తాయి."),

        ("Chemistry - Acids & Bases: pH Scale",
         "A neutral aqueous solution has a pH of 7 at 25 deg C. What happens to the hydronium ion concentration [H3O+] as the pH value of a solution decreases from 7 to 2?",
         "25 డిగ్రీల వద్ద తటస్థ ద్రావణం pH విలువ 7. ఒక ద్రావణం యొక్క pH విలువ 7 నుండి 2 కు తగ్గినప్పుడు అందులోని హైడ్రోనియం అయాన్ల [H+] గాఢత ఏమవుతుంది?",
         ["It decreases by 5 times", "It increases by 10^5 (1,00,000) times", "It remains constant", "It decreases by 10^5 times"],
         ["5 రెట్లు తగ్గుతుంది", "10^5 (లక్ష) రెట్లు పెరుగుతుంది", "స్థిరంగా ఉంటుంది", "లక్ష రెట్లు తగ్గుతుంది"],
         1,
         "The pH scale is logarithmic: pH = -log[H+]. A decrease of 5 pH units (from 7 to 2) represents a 10^5 (100,000-fold) increase in H+ concentration.",
         "pH స్కేల్ లాగరిథమిక్ ఆధారంగా ఉంటుంది. pH విలువ 7 నుండి 2 కు తగ్గడం అంటే ద్రావణంలో హైడ్రోజన్ అయాన్ల గాఢత 10^5 రెట్లు (లక్ష రెట్లు) పెరిగిందని అర్థం."),

        ("Chemistry - Metallurgy: Galvanization",
         "Galvanization is a widely used industrial metallurgical process to protect iron and steel from rusting by coating them with a thin layer of which protective metal?",
         "ఇనుము మరియు ఉక్కు తుప్పు పట్టకుండా రక్షించడానికి వాటిపై ఏ లోహపు పలుచని పొరను పూతగా వేసే పద్ధతిని 'గాల్వనైజేషన్' (Galvanization) అంటారు?",
         ["Copper", "Zinc", "Lead", "Nickel"],
         ["రాగి (Copper)", "జింక్ (Zinc / జింకు)", "సీసం (Lead)", "నికెల్ (Nickel)"],
         1,
         "Galvanization involves coating iron or steel with a thin protective layer of Zinc (Zn). Zinc acts as a sacrificial anode, preventing oxidation of the underlying iron.",
         "గాల్వనైజేషన్ ప్రక్రియలో ఇనుముపై జింక్ లోహాన్ని పూతగా వేస్తారు. జింక్ ఆక్సీకరణం చెంది ఇనుము తుప్పు పట్టకుండా రక్షిస్తుంది."),

        ("Chemistry - Environmental: Acid Rain",
         "Acid rain, which damages vegetation, aquatic ecosystems, and marble monuments like the Taj Mahal, is primarily caused by atmospheric emissions of which gases?",
         "తాజ్ మహల్ వంటి పాలరాతి కట్టడాలకు నష్టం కలిగిస్తూ, పర్యావరణాన్ని కలుషితం చేసే 'ఆమ్ల వర్షాలు' (Acid Rain) ప్రధానంగా వాతావరణంలో ఏ వాయువుల ఉద్గారాల వల్ల సంభవిస్తాయి?",
         ["Carbon monoxide and Methane", "Sulphur dioxide (SO2) and Nitrogen oxides (NOx)", "Chlorofluorocarbons and Ozone", "Ammonia and Argon"],
         ["కార్బన్ మోనాక్సైడ్ మరియు మీథేన్", "సల్ఫర్ డయాక్సైడ్ (SO2) మరియు నైట్రోజన్ ఆక్సైడ్లు (NOx)", "క్లోరోఫ్లోరో కార్బన్లు మరియు ఓజోన్", "అమ్మోనియా మరియు ఆర్గాన్"],
         1,
         "Acid rain is caused by emissions of Sulphur dioxide (SO2) and Nitrogen oxides (NOx) from fossil fuel burning, forming sulphuric and nitric acids in rainwater.",
         "శిలాజ ఇంధనాలను మండించడం వల్ల విడుదలయ్యే సల్ఫర్ డయాక్సైడ్ మరియు నైట్రోజన్ ఆక్సైడ్లు వర్షపు నీటితో కలిసి సల్ఫ్యూరిక్, నైట్రిక్ ఆమ్లాలుగా మారి ఆమ్ల వర్షాలు కురుస్తాయి."),

        ("Biology - Human Physiology: Blood Groups",
         "In the human ABO and Rh blood grouping systems, which blood group is designated as the 'Universal Donor' because its red blood cells lack A, B, and Rh antigens?",
         "మానవ రక్త వర్గీకరణలో ఎర్ర రక్త కణాలపై A, B మరియు Rh యాంటిజెన్లు ఏవీ లేకపోవడం వల్ల ఏ రక్త వర్గాన్ని 'విశ్వ దాత' (Universal Donor) గా పరిగణిస్తారు?",
         ["AB positive (AB+)", "AB negative (AB-)", "O positive (O+)", "O negative (O-)"],
         ["AB పాజిటివ్ (AB+)", "AB నెగటివ్ (AB-)", "O పాజిటివ్ (O+)", "O నెగటివ్ (O-)"],
         3,
         "O negative (O-) red blood cells lack A, B, and Rh surface antigens, meaning they will not trigger an immune reaction in recipients of any blood group (Universal Donor).",
         "O నెగటివ్ (O-) రక్తంలో A, B మరియు Rh యాంటిజెన్లు ఏవీ ఉండవు. కాబట్టి ఈ రక్తాన్ని ఎవరికైనా సురక్షితంగా ఎక్కించవచ్చు, అందుకే దీనిని 'విశ్వ దాత' అంటారు."),

        ("Biology - Human Health: Vitamin Deficiencies",
         "Match the following vitamins with their characteristic clinical deficiency diseases:\nI. Vitamin C — A. Rickets\nII. Vitamin D — B. Beriberi\nIII. Vitamin B1 (Thiamine) — C. Scurvy\nWhich of the combinations given below is correct?",
         "క్రింది విటమిన్లను వాటి లోపం వల్ల కలిగే వ్యాధులతో సరిగ్గా జతపరచండి:\nI. విటమిన్ C — A. రికెట్స్\nII. విటమిన్ D — B. బెరిబెరి\nIII. విటమిన్ B1 (థయామిన్) — C. స్కర్వీ\nసరైన కలయిక ఏది?",
         ["I-C, II-A, III-B", "I-A, II-C, III-B", "I-B, II-A, III-C", "I-C, II-B, III-A"],
         ["I-C, II-A, III-B", "I-A, II-C, III-B", "I-B, II-A, III-C", "I-C, II-B, III-A"],
         0,
         "Vitamin C deficiency causes Scurvy (bleeding gums); Vitamin D deficiency causes Rickets (soft bones); Vitamin B1 (Thiamine) deficiency causes Beriberi.",
         "విటమిన్ సి లోపం వల్ల స్కర్వీ, విటమిన్ డి లోపం వల్ల రికెట్స్, మరియు విటమిన్ బి1 లోపం వల్ల బెరిబెరి వ్యాధులు వస్తాయి."),

        ("Biology - Human Respiratory System: Gas Exchange",
         "In human respiration, where does the actual diffusion and exchange of respiratory gases (Oxygen and Carbon Dioxide) occur in the lungs?",
         "మానవ శ్వాసక్రియలో ఊపిరితిత్తులలో ఆక్సిజన్ మరియు కార్బన్ డయాక్సైడ్ వాయువుల మార్పిడి ఖచ్చితంగా ఎక్కడ జరుగుతుంది?",
         ["Trachea", "Alveoli (Air sacs)", "Bronchi", "Larynx"],
         ["శ్వాసనాళం (Trachea)", "వాయుగోణులు (Alveoli)", "శ్వాసనాళికలు (Bronchi)", "స్వరపేటిక (Larynx)"],
         1,
         "Alveoli are microscopic, balloon-like air sacs surrounded by dense capillary networks where gas exchange takes place via simple diffusion across the thin respiratory membrane.",
         "ఊపిరితిత్తులలోని వాయుగోణులు (Alveoli) దట్టమైన రక్తకేశనాళికల వలయంతో చుట్టబడి ఉంటాయి. ఇక్కడే పల్చని పొర గుండా ఆక్సిజన్ రక్తంలోకి, కార్బన్ డయాక్సైడ్ బయటకు వ్యాపనం చెందుతాయి."),

        ("Biology - Infectious Diseases: Pathogens",
         "Which of the following infectious diseases is caused by a Protozoan parasite transmitted to humans through the bite of an infected female Anopheles mosquito?",
         "ఆడ అనాఫిలిస్ దోమ కాటు ద్వారా వ్యాప్తి చెందే ప్రోటోజోవా పరాన్నజీవి వల్ల మానవులకు సోకే అంటువ్యాధి ఏది?",
         ["Dengue fever", "Malaria", "Chikungunya", "Typhoid"],
         ["డెంగ్యూ జ్వరం", "మలేరియా (Malaria)", "చికున్‌గున్యా", "టైఫాయిడ్"],
         1,
         "Malaria is caused by the Plasmodium protozoan parasite, transmitted by female Anopheles mosquitoes. Dengue and Chikungunya are viral (Aedes mosquito), and Typhoid is bacterial.",
         "మలేరియా అనేది ప్లాస్మోడియం అనే ప్రోటోజోవా పరాన్నజీవి వల్ల వస్తుంది, ఇది ఆడ అనాఫిలిస్ దోమ కాటు ద్వారా వ్యాపిస్తుంది."),

        ("Space Technology - ISRO: Chandrayaan-3",
         "In ISRO's historic Chandrayaan-3 lunar mission that achieved a soft landing near the Moon's South Pole, what were the official names of the Lander and the Rover respectively?",
         "జాబిల్లి దక్షిణ ధ్రువం సమీపంలో సురక్షితంగా ల్యాండ్ అయిన ఇస్రో (ISRO) చారిత్రక 'చంద్రయాన్-3' మిషన్‌లో ల్యాండర్ మరియు రోవర్‌ల అధికారిక పేర్లు వరుసగా ఏవి?",
         ["Lander Vikram and Rover Pragyan", "Lander Pragyan and Rover Vikram", "Lander Dhruv and Rover Aditya", "Lander Pushpak and Rover Vyom"],
         ["ల్యాండర్ విక్రమ్ మరియు రోవర్ ప్రజ్ఞాన్", "ల్యాండర్ ప్రజ్ఞాన్ మరియు రోవర్ విక్రమ్", "ల్యాండర్ ధ్రువ్ మరియు రోవర్ ఆదిత్య", "ల్యాండర్ పుష్పక్ మరియు రోవర్ వ్యోమ్"],
         0,
         "Chandrayaan-3 successfully touched down on August 23, 2023. The lander was named Vikram (after Dr. Vikram Sarabhai) and the rover was named Pragyan ('wisdom').",
         "2023 ఆగస్టు 23న చంద్రయాన్-3 విజయవంతంగా ల్యాండ్ అయింది. ల్యాండర్‌కు 'విక్రమ్' (డాక్టర్ విక్రమ్ సారాభాయ్ గౌరవార్థం) మరియు రోవర్‌కు 'ప్రజ్ఞాన్' అని పేరు పెట్టారు.")
    ]

    for item in authored_science:
        gs_list.append(make_q(101 + len(gs_list), item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))

    assert len(gs_list) == 88, f"Expected 88 cumulative questions (16+20+14+14+10+14), got {len(gs_list)}"

    # ---------------------------------------------------------
    # 7. CURRENT AFFAIRS & CONTEMPORARY GOVERNANCE (12 Qs: Q189 to Q200)
    # ---------------------------------------------------------
    # FCB 9 Qs: 54, 64, 74, 83, 84, 104, 106, 109, 110
    fcb_ca_ids = [54, 64, 74, 83, 84, 104, 106, 109, 110]
    for fid in fcb_ca_ids:
        q = fcb_map[fid]
        gs_list.append(make_q(
            101 + len(gs_list), q.get('topic', 'Telangana Governance & Current Affairs'),
            q['question_en'], q['question_te'],
            q['options_en'], q['options_te'],
            q['correct_option'], q['explanation_en'], q['explanation_te']
        ))

    # StudyNow 2026 Unused (3 Qs):
    # Let's pick 3 verified unused questions: ICJS 2.0 Police Force ranking, Asia Power Index, and Climate Change Performance Index
    sn_picks = [
        # ICJS 2.0 Police Force Ranking
        ("Current Affairs 2026 - Law Enforcement: ICJS 2.0",
         "Which state's Police Force ranked first nationally in the effective operationalization and data entry of the Inter-Operable Criminal Justice System (ICJS 2.0)?",
         "ఇంటర్-ఆపరేబుల్ క్రిమినల్ జస్టిస్ సిస్టమ్ (ICJS 2.0) సమర్థవంతమైన అమలు మరియు డేటా నమోదులో దేశంలో ఏ రాష్ట్ర పోలీసు విభాగం మొదటి స్థానంలో నిలిచింది?",
         ["Telangana Police", "Uttar Pradesh Police", "Kerala Police", "Tamil Nadu Police"],
         ["తెలంగాణ పోలీస్", "ఉత్తరప్రదేశ్ పోలీస్", "కేరళ పోలీస్", "తమిళనాడు పోలీస్"],
         1,
         "Uttar Pradesh Police ranked first nationally in the ICJS 2.0 implementation, integrating courts, police stations, forensics, and prisons under the e-Courts and e-Prisons mission mode project.",
         "పోలీస్ స్టేషన్లు, కోర్టులు, జైళ్లు మరియు ఫోరెన్సిక్ ల్యాబ్‌లను అనుసంధానించే ICJS 2.0 అమలులో ఉత్తరప్రదేశ్ పోలీస్ దేశంలో ప్రథమ స్థానాన్ని కైవసం చేసుకుంది."),

        # Asia Power Index
        ("Current Affairs 2026 - Global Indices: Asia Power Index",
         "According to the Lowy Institute's Asia Power Index, what is India's rank among the most powerful nations shaping influence across the Asia-Pacific region?",
         "లోవీ ఇన్‌స్టిట్యూట్ విడుదల చేసిన 'ఆసియా పవర్ ఇండెక్స్' ప్రకారం ఆసియా-పసిఫిక్ ప్రాంతంలో అత్యంత ప్రభావవంతమైన దేశాలలో భారతదేశం ఎన్నవ స్థానంలో నిలిచింది?",
         ["2nd rank", "3rd rank", "4th rank", "5th rank"],
         ["2వ స్థానం", "3వ స్థానం", "4వ స్థానం", "5వ స్థానం"],
         1,
         "India secured the 3rd rank in the Lowy Institute Asia Power Index, following the United States (1st) and China (2nd), reflecting growing economic resilience and diplomatic clout.",
         "లోవీ ఇన్‌స్టిట్యూట్ నివేదిక ప్రకారం అమెరికా (1), చైనా (2) తర్వాత భారతదేశం 3వ స్థానంలో నిలిచింది. భారతదేశం ఆర్థిక మరియు దౌత్యపరమైన అంశాలలో పటిష్టమైన పురోగతిని నమోదు చేసింది."),

        # Climate Change Performance Index 2026
        ("Current Affairs 2026 - Environment: Climate Change Index",
         "In the Climate Change Performance Index (CCPI), what was India's commendable global ranking reflecting strong renewable energy deployment?",
         "పునరుత్పాదక ఇంధన ఉత్పత్తి మరియు పర్యావరణ విధానాలలో పురోగతిని సూచిస్తూ 'క్లైమేట్ చేంజ్ పెర్ఫార్మెన్స్ ఇండెక్స్' (CCPI) లో భారతదేశం ఏ ర్యాంకును సాధించింది?",
         ["7th rank", "10th rank", "12th rank", "15th rank"],
         ["7వ ర్యాంకు", "10వ ర్యాంకు", "12వ ర్యాంకు", "15వ ర్యాంకు"],
         1,
         "India was ranked 10th in the global Climate Change Performance Index (CCPI), retaining its position among top high-performing G20 nations in GHG emission reduction and renewable policies.",
         "గ్లోబల్ క్లైమేట్ చేంజ్ పెర్ఫార్మెన్స్ ఇండెక్స్ (CCPI) లో భారతదేశం 10వ స్థానాన్ని దక్కించుకుంది. G20 దేశాలలో హరిత ఇంధన విస్తరణలో అగ్రగామిగా నిలిచింది.")
    ]

    for item in sn_picks:
        gs_list.append(make_q(101 + len(gs_list), item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))

    assert len(gs_list) == 100, f"Expected 100 General Studies questions, got {len(gs_list)}"
    return gs_list

if __name__ == '__main__':
    qs = get_gs_100()
    print(f"Loaded {len(qs)} General Studies questions for Mock 13.")
