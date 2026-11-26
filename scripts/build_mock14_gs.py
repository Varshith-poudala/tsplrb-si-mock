import json
import re
from pathlib import Path


def clean_tag(text):
    return re.sub(r"^\s*\[[^\]]+\]\s*", "", str(text or "")).strip()


def make_q(topic, q_en, q_te, opts_en, opts_te, corr, exp_en, exp_te):
    assert len(opts_en) == 4 and len(opts_te) == 4, topic
    assert 0 <= corr <= 3, topic
    return {
        "section": "General Studies & Telangana",
        "topic": clean_tag(topic),
        "difficulty": "Hard",
        "question_en": q_en.strip(),
        "question_te": q_te.strip(),
        "options_en": [o.strip() for o in opts_en],
        "options_te": [o.strip() for o in opts_te],
        "correct_option": int(corr),
        "explanation_en": exp_en.strip(),
        "explanation_te": exp_te.strip(),
    }


def _load_fcb_by_id():
    fcb_path = Path(__file__).resolve().parent.parent / "public" / "data" / "faculty_curated_bank.json"
    data = json.load(open(fcb_path, "r", encoding="utf-8"))
    qs = data["questions"] if isinstance(data, dict) else data
    return {q["id"]: q for q in qs}


def _wrap_fcb(src):
    return make_q(
        src["topic"],
        src["question_en"],
        src["question_te"],
        src["options_en"],
        src["options_te"],
        src["correct_option"],
        src["explanation_en"],
        src["explanation_te"],
    )


# ==================== 1. POLITY NEW (11) ====================
NEW_POLITY = [
    # P1 (corr=0: 1 and 2 only; stmt 3 false: Navin Rao? No, Narasimha Rao was 5-judge, Sita Soren 7-judge overruled P.V. Narasimha Rao & applied from moment bribe is taken; stmt 3 claims immunity remains if speech/vote not yet cast -> false!)
    make_q(
        "Parliamentary Privileges - Sita Soren v. Union of India (2024)",
        "Consider the following statements regarding the 7-Judge Constitution Bench judgment in Sita Soren v. Union of India (2024):\n1. The Supreme Court unanimously overruled the 5-Judge bench majority verdict in P.V. Narasimha Rao v. State (1998), ruling that MPs and MLAs cannot claim immunity under Articles 105(2) or 194(2) for bribery.\n2. The Court held that the offence of bribery is complete the moment the illegal gratification is accepted or agreed to be accepted, irrespective of whether the legislator subsequently votes or speaks as agreed.\n3. The Court clarified that while MPs lose immunity in Lok Sabha votes, MLAs retain immunity in Rajya Sabha elections because voting for the Upper House is not part of legislative business.\nWhich of the statements given above are correct?",
        "సీతా సోరెన్ వర్సెస్ యూనియన్ ఆఫ్ ఇండియా (2024) కేసులో ఏడుగురు న్యాయమూర్తుల సుప్రీంకోర్టు రాజ్యాంగ ధర్మాసనం వెలువరించిన తీర్పుకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. పి.వి. నరసింహారావు వర్సెస్ స్టేట్ (1998) కేసులోని ఐదుగురు న్యాయమూర్తుల మెజారిటీ తీర్పును సుప్రీంకోర్టు ఏకగ్రీవంగా రద్దు చేస్తూ, లంచం కేసులో ఎంపీలు, ఎమ్మెల్యేలకు ఆర్టికల్ 105(2) లేదా 194(2) కింద రక్షణ ఉండదని తీర్పునిచ్చింది.\n2. చట్టసభ సభ్యుడు అక్రమ ప్రతిఫలాన్ని స్వీకరించిన లేదా అంగీకరించిన క్షణమే లంచం నేరం పూర్తవుతుందని, ఆపై వారు ఓటు వేశారా లేదా అనే దానితో సంబంధం లేదని కోర్టు స్పష్టం చేసింది.\n3. లోక్‌సభ ఓటింగ్‌లో ఎంపీలకు రక్షణ లేనప్పటికీ, రాజ్యసభ ఎన్నికలలో ఓటు వేయడం శాసన ప్రక్రియలో భాగం కానందున ఎమ్మెల్యేలకు ఆ రక్షణ కొనసాగుతుందని కోర్టు పేర్కొంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, whereas Statement 3 is incorrect. In Sita Soren (2024), arising precisely out of an alleged bribe in a 2012 Rajya Sabha election in Jharkhand, the 7-Judge bench overruled P.V. Narasimha Rao (1998) and held that bribery fails the two-fold 'nexus and essentiality' test and enjoys zero immunity under Article 105(2) or 194(2), including Rajya Sabha voting.",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. రాజ్యసభ ఎన్నికలలో ఓటు వేయడానికి లంచం తీసుకున్నారనే కేసులోనే సుప్రీంకోర్టు ఎంపీలు, ఎమ్మెల్యేలకు ఆర్టికల్ 105(2)/194(2) కింద ఎటువంటి లంచం రక్షణ లేదని స్పష్టం చేసింది."
    ),
    # P2 (corr=1: 2 and 3 only; stmt 1 false: effective date & section counts swapped slightly in stmt 1 -> wrong section counts!)
    make_q(
        "Criminal Law Reforms - BNS, BNSS & BSA (2023)",
        "Consider the following statements regarding India's three new criminal laws that came into force on July 1, 2024:\n1. The Bharatiya Nyaya Sanhita (BNS) replaced the Code of Criminal Procedure (CrPC), 1973 with 531 sections, whereas the Bharatiya Nagarik Suraksha Sanhita (BNSS) replaced the Indian Penal Code (IPC), 1860.\n2. Section 173 of the BNSS provides explicit statutory recognition to 'Zero FIR' regardless of territorial jurisdiction, as well as electronic FIR (e-FIR) subject to signature within 3 days.\n3. Under Section 63 of the Bharatiya Sakshya Adhiniyam (BSA), admissibility certificates for electronic records mandate disclosure of cryptographic hash values alongside expert verification.\nWhich of the statements given above are correct?",
        "జూలై 1, 2024 నుండి అమలులోకి వచ్చిన భారత నూతన క్రిమినల్ చట్టాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. భారతీయ న్యాయ సంహిత (BNS) 531 సెక్షన్లతో క్రిమినల్ ప్రొసీజర్ కోడ్ (CrPC), 1973 స్థానంలోకి రాగా, భారతీయ నాగరిక్ సురక్షా సంహిత (BNSS) భారత శిక్షాస్మృతి (IPC), 1860 స్థానంలోకి వచ్చింది.\n2. BNSS లోని సెక్షన్ 173 ద్వారా ప్రాదేశిక పరిధితో సంబంధం లేకుండా 'జీరో ఎఫ్‌ఐఆర్' (Zero FIR) నమోదుకు మరియు 3 రోజుల్లో సంతకం షరతుతో ఎలక్ట్రానిక్ ఎఫ్‌ఐఆర్ (e-FIR) కు చట్టబద్ధత లభించింది.\n3. భారతీయ సాక్ష్య అధినియం (BSA) సెక్షన్ 63 ప్రకారం ఎలక్ట్రానిక్ రికార్డుల సాక్ష్య ధృవీకరణ పత్రంలో క్రిప్టోగ్రాఫిక్ హ్యాష్ విలువ (Hash Value) మరియు నిపుణుల ధృవీకరణ తప్పనిసరి చేయబడింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is reversed: BNS (358 sections) replaced the IPC, 1860; BNSS (531 sections) replaced the CrPC, 1973; and BSA (170 sections) replaced the Indian Evidence Act, 1872.",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పుగా తారుమారు చేయబడింది. BNS (358 సెక్షన్లు) IPC స్థానంలోకి, BNSS (531 సెక్షన్లు) CrPC స్థానంలోకి వచ్చాయి."
    ),
    # P3 (corr=2: 1 and 3 only; stmt 2 false: claims it does NOT require delimitation/census and stays permanently without sunset!)
    make_q(
        "Constitutional Amendments - 106th Amendment Act (Nari Shakti Vandan)",
        "Consider the following statements regarding the 106th Constitutional Amendment Act, 2023 (Nari Shakti Vandan Adhiniyam):\n1. It inserted Articles 330A and 332A to mandate one-third reservation for women (including a one-third sub-quota within SC/ST reserved seats) in the Lok Sabha and State Legislative Assemblies.\n2. It omitted the requirement of fresh census and delimitation exercises and established permanent reservation without any sunset period.\n3. Article 334A specifies that the women's reservation provisions will come into effect after delimitation based on the first census published after the Act's commencement, for an initial 15-year period unless extended by Parliament.\nWhich of the statements given above are correct?",
        "106వ రాజ్యాంగ సవరణ చట్టం, 2023 (నారీ శక్తి వందన్ అధినియం) కు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. లోక్‌సభ మరియు రాష్ట్ర శాసనసభలలో మహిళలకు మూడో వంతు (33%) రిజర్వేషన్ కల్పించేందుకు (SC/ST కోటాలో 1/3వ ఉప-కోటాతో సహా) ఇది ఆర్టికల్స్ 330A మరియు 332A లను చేర్చింది.\n2. ఇది నూతన జనాభా గణన మరియు నియోజకవర్గాల పునర్విభజన అవసరాన్ని మినహాయించి, ఎటువంటి కాలపరిమితి (Sunset Clause) లేని శాశ్వత రిజర్వేషన్‌ను కల్పించింది.\n3. చట్టం అమలు తర్వాత ప్రచురితమయ్యే మొదటి జనాభా లెక్కల ఆధారిత డీలిమిటేషన్ అనంతరమే ఈ రిజర్వేషన్లు ప్రారంభమవుతాయని, మరియు పార్లమెంటు పొడిగించని పక్షంలో ఇవి 15 ఏళ్ల పాటు అమల్లో ఉంటాయని ఆర్టికల్ 334A నిర్దేశిస్తుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is false. Under Article 334A, implementation is contingent upon the first post-Act census and subsequent delimitation, and carries a 15-year sunset clause (subject to parliamentary extension). It also amended Article 239AA for Delhi Assembly.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. ఆర్టికల్ 334A ప్రకారం జనాభా లెక్కలు మరియు నియోజకవర్గాల పునర్విభజన తర్వాతే ఇది అమల్లోకి వస్తుంది మరియు 15 సంవత్సరాల సన్‌సెట్ క్లాజ్ (కాలపరిమితి) వర్తిస్తుంది."
    ),
    # P4 (corr=1: 2 and 3 only; stmt 1 false: says ratified by half states before presidential assent; actually Parliament failed to get state ratification!)
    make_q(
        "Cooperative Federalism - 97th Amendment & Rajendra Shah Ruling",
        "Consider the following statements regarding the 97th Constitutional Amendment Act, 2011 and the Supreme Court verdict in Union of India v. Rajendra N. Shah (2021):\n1. Because the 97th Amendment inserted Part IXB regulating cooperative societies within the State List, it was duly ratified by more than half of the State Legislatures under Article 368(2) before receiving Presidential assent.\n2. The Supreme Court struck down Part IXB insofar as it applied to State-level cooperative societies for want of the mandatory ratification by at least half the States.\n3. However, the Court upheld Part IXB strictly in its application to Multi-State Cooperative Societies (MSCS), while leaving Article 19(1)(c) and Article 43B intact.\nWhich of the statements given above are correct?",
        "97వ రాజ్యాంగ సవరణ చట్టం, 2011 మరియు యూనియన్ ఆఫ్ ఇండియా వర్సెస్ రాజేంద్ర ఎన్. షా (2021) సుప్రీంకోర్టు తీర్పుకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 97వ సవరణ రాష్ట్ర జాబితాలోని సహకార సంఘాలపై పార్ట్ IXB ను చేర్చినందున, రాష్ట్రపతి ఆమోదానికి ముందు దీనిని ఆర్టికల్ 368(2) కింద సగానికి పైగా రాష్ట్ర శాసనసభలు ఆమోదించాయి.\n2. కనీసం సగం రాష్ట్రాల శాసనసభల ఆమోదం తీసుకోనందున, రాష్ట్ర స్థాయి సహకార సంఘాలకు సంబంధించిన మేరకు పార్ట్ IXB నిబంధనలను సుప్రీంకోర్టు కొట్టివేసింది.\n3. అయితే బహుళ-రాష్ట్ర సహకార సంఘాలకు (MSCS) సంబంధించిన మేరకు పార్ట్ IXB చెల్లుబాటును సమర్థిస్తూ, ఆర్టికల్ 19(1)(c) మరియు ఆర్టికల్ 43B లను యథాతథంగా కొనసాగించింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is false. Parliament passed the 97th Amendment without securing ratification by half the state legislatures under the proviso to Article 368(2), which led the Supreme Court (2021) to invalidate Part IXB for purely state-level cooperatives while saving MSCS provisions, Article 19(1)(c), and Article 43B.",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. 97వ సవరణ బిల్లును పార్లమెంటు కనీసం సగం రాష్ట్రాల ఆమోదం (ఆర్టికల్ 368(2)) లేకుండానే ఆమోదించడంతో సుప్రీంకోర్టు 2021లో రాష్ట్ర సహకార సంఘాలకు సంబంధించి పార్ట్ IXB ను రద్దు చేసింది."
    ),
    # P5 (corr=0: 1 and 2 only; stmt 3 false: claims Urdu & Tulu were added in Oct 2024 alongside Marathi & Bengali)
    make_q(
        "Official & Classical Languages - October 2024 Expansion",
        "Consider the following statements regarding the conferral of Classical Language status in India:\n1. In October 2024, the Union Cabinet approved Classical Language status for five languages—Marathi, Pali, Prakrit, Assamese, and Bengali—raising India's total recognized Classical Languages from 6 to 11.\n2. Prior to this decision, the Sahitya Akademi's Linguistic Experts Committee revised the eligibility criteria, notably removing the strict condition that a language's literary tradition must be strictly original and not borrowed from another speech community.\n3. Telugu and Kannada were accorded Classical Language status in 2004 jointly with Tamil and Urdu.\nWhich of the statements given above are correct?",
        "భారతదేశంలో 'శాస్త్రీయ భాషల' (Classical Languages) హోదాకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. అక్టోబర్ 2024లో కేంద్ర కేబినెట్ మరాఠీ, పాళీ, ప్రాకృతం, అస్సామీ మరియు బెంగాలీ అనే ఐదు భాషలకు శాస్త్రీయ హోదాను ఆమోదించడంతో భారతదేశంలోని మొత్తం శాస్త్రీయ భాషల సంఖ్య 6 నుండి 11 కు పెరిగింది.\n2. ఈ నిర్ణయానికి ముందు సాహిత్య అకాడమీ భాషా నిపుణుల కమిటీ అర్హత ప్రమాణాలను సవరించి, సాహిత్య సంప్రదాయం పూర్తిగా స్వంతమై ఉండాలనే ('మరో భాష నుండి అరువు తెచ్చుకోని') కఠిన నిబంధనను సడలించింది.\n3. 2004లో తమిళం మరియు ఉర్దూలతో పాటు తెలుగు మరియు కన్నడ భాషలకు శాస్త్రీయ హోదా కల్పించబడింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is incorrect. Tamil was recognized in 2004 (Sanskrit 2005), Telugu and Kannada in 2008, Malayalam in 2013, and Odia in 2014; Urdu is NOT among the 11 Classical Languages.",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. 2004లో తమిళం మాత్రమే పొందింది; తెలుగు మరియు కన్నడకు 2008లో హోదా లభించింది, మరియు ఉర్దూ శాస్త్రీయ భాషల జాబితాలో లేదు."
    ),
    # P6 (corr=1: 2 and 3 only; stmt 1 false: says Governor can withhold assent indefinitely without returning under Art 200)
    make_q(
        "State Executive - Governor's Assent to Bills (Articles 200 & 201)",
        "Consider the following statements regarding the powers of a State Governor over Bills passed by the State Legislature under Articles 200 and 201:\n1. Under Article 200, if the Governor declares that he withholds assent to an ordinary Bill, he can retain it indefinitely on his desk without either returning it to the Legislature or reserving it for the President.\n2. In State of Punjab v. Principal Secretary to the Governor of Punjab (2023), the Supreme Court held that when a Governor withholds assent, the mandatory 'as soon as possible' proviso requires returning the Bill to the Assembly for reconsideration.\n3. Once a reconsidered non-Money Bill is passed again by the State Legislature (with or without amendments) and re-presented, the Governor shall not withhold assent therefrom (unless reserved under Art 200 provisos such as endangering the High Court's constitutional position).\nWhich of the statements given above are correct?",
        "రాష్ట్ర శాసనసభ ఆమోదించిన బిల్లులపై ఆర్టికల్స్ 200 మరియు 201 కింద గవర్నర్ అధికారాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఆర్టికల్ 200 కింద గవర్నర్ ఒక సాధారణ బిల్లుకు ఆమోదాన్ని నిలిపివేస్తున్నట్లు (Withhold Assent) ప్రకటిస్తే, దానిని తిరిగి శాసనసభకు పంపకుండా లేదా రాష్ట్రపతికి నివేదించకుండా నిరవధికంగా తన వద్దే ఉంచుకోవచ్చు.\n2. స్టేట్ ఆఫ్ పంజాబ్ వర్సెస్ ప్రిన్సిపల్ సెక్రటరీ టు ది గవర్నర్ (2023) తీర్పులో, గవర్నర్ బిల్లుకు ఆమోదాన్ని నిలిపివేసినప్పుడు తప్పనిసరిగా 'వీలైనంత త్వరగా' దానిని శాసనసభకు పునఃపరిశీలన కోసం వెనక్కి పంపాలని సుప్రీంకోర్టు స్పష్టం చేసింది.\n3. పునఃపరిశీలన తర్వాత శాసనసభ ఆ బిల్లును సవరణలతో గాని లేకుండా గాని మళ్లీ ఆమోదించి పంపితే, గవర్నర్ దానికి ఆమోదాన్ని నిరాకరించరాదు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is false. In State of Punjab v. Principal Secretary to the Governor (2023), the Supreme Court decisively rejected an absolute pocket veto under Article 200, ruling that withholding assent triggers the duty under the first proviso to return the Bill to the House as soon as possible, and if passed again, assent cannot be withheld.",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. పంజాబ్ గవర్నర్ కేసు (2023) లో సుప్రీంకోర్టు ఆర్టికల్ 200 కింద గవర్నర్ బిల్లును అపరిమితంగా పక్కన పెట్టలేరని (No Pocket Veto), వెనక్కి పంపాల్సిందేనని తీర్పునిచ్చింది."
    ),
    # P7 (corr=2: Only 1 and 3; stmt 2 false: says High Courts also share concurrent original jurisdiction under Art 71)
    make_q(
        "Union Executive - Presidential Election & Article 71",
        "Consider the following statements regarding the Election of the President of India under Articles 54, 55, and 71:\n1. The Electoral College under Article 54 comprises only the elected members of both Houses of Parliament and the elected members of State Legislative Assemblies (plus elected MLAs of Delhi and Puducherry via the 70th Amendment); nominated members and Legislative Council (MLC) members do not participate.\n2. All doubts and disputes arising out of or in connection with the election of a President or Vice-President may be inquired into and decided concurrently by either the Election Commission of India or any High Court.\n3. The dissolution of a State Legislative Assembly prior to presidential polling does not invalidate the election, since Article 71(4) states that a vacancy in the Electoral College cannot be a ground to call the election in question.\nWhich of the statements given above are correct?",
        "భారత రాజ్యాంగంలోని అధికరణలు 54, 55 మరియు 71 కింద రాష్ట్రపతి ఎన్నికకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఆర్టికల్ 54 ప్రకారం రాష్ట్రపతి ఎలక్టోరల్ కాలేజీలో పార్లమెంటు ఉభయ సభలకు ఎన్నికైన సభ్యులు మరియు రాష్ట్ర శాసనసభలకు ఎన్నికైన సభ్యులు (70వ సవరణ ద్వారా ఢిల్లీ, పుదుచ్చేరి అసెంబ్లీలతో సహా) మాత్రమే ఉంటారు; నామినేట్ అయిన సభ్యులు మరియు శాసనమండలి (MLC) సభ్యులు పాల్గొనరు.\n2. రాష్ట్రపతి లేదా ఉపరాష్ట్రపతి ఎన్నికకు సంబంధించిన వివాదాలన్నింటినీ కేంద్ర ఎన్నికల సంఘం లేదా ఏదైనా హైకోర్టు సంయుక్తంగా విచారించి తీర్పునిస్తాయి.\n3. రాష్ట్రపతి ఎన్నికకు ముందు ఏదైనా రాష్ట్ర శాసనసభ రద్దయినా ఆ ఎన్నిక చెల్లుబాటు అవుతుంది; ఎలక్టోరల్ కాలేజీలో ఖాళీ ఉందన్న కారణంతో ఎన్నికను సవాలు చేయరాదని ఆర్టికల్ 71(4) పేర్కొంటుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is incorrect. Under Article 71(1), ALL doubts and disputes arising out of or in connection with the election of a President or Vice-President are inquired into and decided EXCLUSIVELY by the Supreme Court of India, whose decision is final.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. అధికరణ 71(1) ప్రకారం రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి ఎన్నికల వివాదాలను విచారించి అంతిమ తీర్పునిచ్చే ఏకైక అధికారం భారత సర్వోన్నత న్యాయస్థానానికి (సుప్రీంకోర్టు) మాత్రమే ఉంటుంది."
    ),
    # P8 (corr=0: A-3, B-1, C-4, D-2 — Match cleanly)
    make_q(
        "Centre-State Relations - Commissions & Committees Match",
        "Match the following landmark Commissions/Committees on Centre-State Relations (List-I) with their notable recommendations or legal frameworks (List-II):\nList-I:\nA. First Administrative Reforms Commission (1966)\nB. Sarkaria Commission (1983)\nC. Punchhi Commission (2007)\nD. Rajamannar Committee (1969, Tamil Nadu)\nList-II:\n1. Permanent Inter-State Council under Article 263 and sparing use of Article 356 as last resort\n2. Total abolition of All-India Services (IAS/IPS) and deletion of Articles 356, 357 & 365\n3. Establishment of Lokpal & Lokayukta institutions and setting up Inter-State Councils\n4. Impeachment-like procedure for removal of Governors and localized emergency provisions\nSelect the correct code:",
        "కేంద్ర-రాష్ట్ర సంబంధాలపై ఏర్పాటైన ప్రముఖ కమిషన్లను (జాబితా-I) వాటి ముఖ్య సిఫార్సులతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. మొదటి పరిపాలనా సంస్కరణల సంఘం (1966)\nB. సర్కారియా కమిషన్ (1983)\nC. పూంచీ కమిషన్ (2007)\nD. రాజమన్నార్ కమిటీ (1969, తమిళనాడు)\nజాబితా-II:\n1. ఆర్టికల్ 263 కింద శాశ్వత అంతర్-రాష్ట్ర మండలి ఏర్పాటు మరియు ఆర్టికల్ 356 ను చివరి అస్త్రంగా మాత్రమే వాడటం\n2. అఖిల భారత సర్వీసుల (IAS/IPS) రద్దు మరియు ఆర్టికల్స్ 356, 357, 365 ల తొలగింపు\n3. లోక్‌పాల్, లోకాయుక్త సంస్థల స్థాపన మరియు అంతర్-రాష్ట్ర మండలి ఏర్పాటు సిఫార్సు\n4. గవర్నర్ల తొలగింపునకు అభిశంసన తరహా ప్రక్రియ మరియు ప్రాంతీయ ఎమర్జెన్సీ నిబంధనలు\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3"],
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3"],
        0,
        "First ARC (Morarji Desai/K. Hanumanthaiah, 1966) famously recommended Lokpal/Lokayuktas and Inter-State Councils (A-3). Sarkaria Commission (1983–88) championed a permanent Inter-State Council under Article 263 and sparing use of Article 356 (B-1). Punchhi Commission (2007–10) advocated fixed 5-year Governor tenure with State legislature impeachment-like removal and localized emergency (C-4). Rajamannar Committee (1969) radically demanded abolition of IAS/IPS and Articles 356/357/365 (D-2).",
        "మొదటి ARC లోక్‌పాల్, అంతర్-రాష్ట్ర మండలికి (3), సర్కారియా ఆర్టికల్ 263 శాశ్వత మండలికి (1), పూంచీ కమిషన్ గవర్నర్ తొలగింపు ప్రక్రియకు (4), మరియు రాజమన్నార్ కమిటీ IAS/IPS & ఆర్టికల్ 356 రద్దుకు (2) సిఫార్సు చేశాయి."
    ),
    # P9 (corr=1: A-2, B-4, C-1, D-3 — Match Committees)
    make_q(
        "Parliamentary System - Standing & Financial Committees Match",
        "Match the Parliamentary Committees (List-I) with their exact constitutional/statutory composition and distinctive characteristic (List-II):\nList-I:\nA. Public Accounts Committee (PAC)\nB. Estimates Committee\nC. Committee on Public Undertakings (COPU)\nD. Departmentally Related Standing Committees (DRSCs)\nList-II:\n1. Created in 1964 on Krishna Menon Committee's recommendation; 22 members (15 LS + 7 RS)\n2. 22 members (15 LS + 7 RS); examines CAG Audit Reports; chaired conventionally by an Opposition leader since 1967\n3. 24 Committees (16 under LS Speaker, 8 under RS Chairman); each has 31 members (21 LS + 10 RS)\n4. Largest Parliamentary Committee with 30 members drawn exclusively from Lok Sabha; examines budget economies\nSelect the correct code:",
        "పార్లమెంటరీ కమిటీలను (జాబితా-I) వాటి సభ్యుల సంఖ్య మరియు ప్రత్యేక లక్షణాలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. పబ్లిక్ అకౌంట్స్ కమిటీ (PAC)\nB. అంచనాల కమిటీ (Estimates Committee)\nC. ప్రభుత్వ రంగ సంస్థల కమిటీ (COPU)\nD. శాఖాపరమైన స్థాయీ సంఘాలు (DRSCs)\nజాబితా-II:\n1. 1964లో కృష్ణ మీనన్ కమిటీ సిఫార్సుతో ఏర్పాటైంది; 22 మంది సభ్యులు (15 లోక్‌సభ + 7 రాజ్యసభ)\n2. 22 మంది సభ్యులు (15 LS + 7 RS); కాగ్ (CAG) నివేదికలను పరిశీలిస్తుంది; 1967 నుండి ప్రతిపక్ష సభ్యుడు చైర్మన్‌గా ఉంటారు\n3. మొత్తం 24 కమిటీలు (16 లోక్‌సభ స్పీకర్, 8 రాజ్యసభ చైర్మన్ కింద); ప్రతి కమిటీలో 31 మంది సభ్యులు (21 LS + 10 RS)\n4. లోక్‌సభ సభ్యులతో మాత్రమే కూడిన అతిపెద్ద 30 మంది కమిటీ; బడ్జెట్ పొదుపు చర్యలను సూచిస్తుంది\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-1, B-4, C-2, D-3", "A-2, B-4, C-1, D-3", "A-2, B-3, C-1, D-4", "A-4, B-2, C-1, D-3"],
        ["A-1, B-4, C-2, D-3", "A-2, B-4, C-1, D-3", "A-2, B-3, C-1, D-4", "A-4, B-2, C-1, D-3"],
        1,
        "PAC (22 members: 15 LS + 7 RS) audits CAG reports with an Opposition Chair since 1967 (A-2). Estimates Committee has 30 members drawn exclusively from Lok Sabha (B-4). COPU was created in 1964 on Krishna Menon Committee's recommendation with 22 members (C-1). There are 24 DRSCs with 31 members each: 21 from Lok Sabha and 10 from Rajya Sabha (D-3).",
        "PAC 22 మందితో కాగ్ నివేదికలను పరిశీలిస్తుంది (2); అంచనాల కమిటీ 30 మంది లోక్‌సభ సభ్యులతో మాత్రమే ఉంటుంది (4); COPU 1964 కృష్ణ మీనన్ కమిటీ ద్వారా ఏర్పడింది (1); 24 DRSCs ఒక్కొక్కటి 31 మందితో ఉంటాయి (3)."
    ),
    # P10 (corr=2: 1 and 3 only; stmt 2 false: claims GST Council recommendations are strictly binding on Parliament & States, whereas SC Mohit Minerals 2022 held they are persuasive, not legally binding!)
    make_q(
        "Fiscal Federalism - GST Council (Art. 279A) & Mohit Minerals Case",
        "Consider the following statements regarding the Goods and Services Tax (GST) Council under Article 279A of the Constitution:\n1. Under Article 279A(9), every decision of the GST Council requires a majority of not less than three-fourths of the weighted votes of the members present and voting, with the Central Government carrying one-third weightage and all State Governments together carrying two-thirds weightage.\n2. In Union of India v. Mohit Minerals Pvt. Ltd. (2022), the Supreme Court held that recommendations of the GST Council are constitutionally binding and mandatory commands upon both Parliament and State Legislatures.\n3. One-half of the total number of members of the GST Council constitutes the quorum at its meetings.\nWhich of the statements given above are correct?",
        "భారత రాజ్యాంగంలోని అధికరణ 279A కింద జీఎస్టీ కౌన్సిల్ (GST Council) కు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఆర్టికల్ 279A(9) ప్రకారం జీఎస్టీ కౌన్సిల్ ప్రతి నిర్ణయానికి హాజరై ఓటు వేసిన సభ్యుల వెయిటెడ్ ఓట్లలో కనీసం మూడొంతుల వంతు (3/4) మెజారిటీ అవసరం; ఇందులో కేంద్ర ప్రభుత్వానికి 1/3వ వంతు మరియు అన్ని రాష్ట్ర ప్రభుత్వాలకు కలిపి 2/3వ వంతు ఓట్ల బరువు ఉంటుంది.\n2. యూనియన్ ఆఫ్ ఇండియా వర్సెస్ మోహిత్ మినరల్స్ (2022) కేసులో జీఎస్టీ కౌన్సిల్ సిఫార్సులు పార్లమెంటుకు మరియు రాష్ట్ర శాసనసభలకు చట్టబద్ధంగా తప్పనిసరిగా కట్టుబడే ఆదేశాలని సుప్రీంకోర్టు తీర్పునిచ్చింది.\n3. జీఎస్టీ కౌన్సిల్ సమావేశాలకు మొత్తం సభ్యుల సంఖ్యలో సగం మంది (1/2) హాజరైతే కోరం (Quorum) పూర్తవుతుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is false. In Union of India v. Mohit Minerals (May 2022), the Supreme Court ruled that GST Council recommendations only have persuasive value—not strictly binding constitutional commands—because Article 246A vests simultaneous legislative power in Parliament and State Legislatures under cooperative federalism.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. మోహిత్ మినరల్స్ (2022) తీర్పులో జీఎస్టీ కౌన్సిల్ సిఫార్సులకు కేవలం సలహా పూర్వక విలువ మాత్రమే ఉంటుందని, అవి శాసనసభలకు తప్పనిసరి కట్టుబాటు కావని సుప్రీంకోర్టు స్పష్టం చేసింది."
    ),
    # P11 (corr=0: 1 and 2 only; pair 3 wrong: says 86th Amendment inserted Art 43A -> Art 43A was 42nd Amendment; 86th amended Art 45!)
    make_q(
        "Directive Principles of State Policy - Amendment Pairings",
        "Consider the following pairs of Directive Principles of State Policy (DPSP) Articles and the Constitutional Amendment Acts that inserted/amended them:\n1. Article 39A (Equal justice and free legal aid) — 42nd Constitutional Amendment Act, 1976\n2. Article 38(2) (Minimize inequalities in income, status, facilities and opportunities) — 44th Constitutional Amendment Act, 1978\n3. Article 43A (Participation of workers in management of industries) — 86th Constitutional Amendment Act, 2002\nWhich of the pairs given above are correctly matched?",
        "ఆదేశిక సూత్రాల (DPSP) అధికరణలను మరియు వాటిని చేర్చిన/సవరించిన రాజ్యాంగ సవరణ చట్టాలకు సంబంధించి క్రింది జతలను పరిశీలించండి:\n1. అధికరణ 39A (సమాన న్యాయం మరియు ఉచిత న్యాయ సహాయం) — 42వ రాజ్యాంగ సవరణ చట్టం, 1976\n2. అధికరణ 38(2) (ఆదాయం, హోదా, సౌకర్యాల్లో అసమానతలను తగ్గించడం) — 44వ రాజ్యాంగ సవరణ చట్టం, 1978\n3. అధికరణ 43A (పరిశ్రమల నిర్వహణలో కార్మికుల భాగస్వామ్యం) — 86వ రాజ్యాంగ సవరణ చట్టం, 2002\nపై జతలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Pairs 1 and 2 are correctly matched, while Pair 3 is incorrect. Article 43A (worker participation in industry management) was inserted by the 42nd Amendment Act, 1976 (alongside 39A, 39(f), and 48A). The 86th Amendment Act, 2002 substituted Article 45 (early childhood care and education for children below age six) and inserted Article 21A and Article 51A(k).",
        "జతలు 1 మరియు 2 సరైనవి, కానీ జత 3 తప్పు. ఆర్టికల్ 43A ను కూడా 42వ రాజ్యాంగ సవరణ (1976) ద్వారానే చేర్చారు. 86వ సవరణ (2002) ఆర్టికల్ 45 ను (6 ఏళ్ల లోపు పిల్లల సంరక్షణ, విద్య) సవరించింది."
    ),
]

# ==================== 2. TELANGANA NEW (13) ====================
NEW_TELANGANA = [
    # T1 (corr=0: A-3, B-1, C-4, D-2 — Zones under GO 124 / 2018 Presidential Order)
    make_q(
        "Telangana Public Employment - Presidential Order 2018 (G.O. Ms. No. 124)",
        "Match the Zones established under the Telangana Public Employment (Organisation of Local Cadres and Regulation of Direct Recruitment) Order, 2018 (G.O. Ms. No. 124) in List-I with their constituent districts in List-II:\nList-I (Zone):\nA. Zone I (Kaleshwaram)\nB. Zone III (Rajanna)\nC. Zone V (Yadadri)\nD. Zone VII (Jogulamba)\nList-II (Districts):\n1. Karimnagar, Rajanna Sircilla, Siddipet, Medak, Kamareddy\n2. Mahabubnagar, Narayanpet, Jogulamba Gadwal, Wanaparthy, Nagarkurnool\n3. Komaram Bheem Asifabad, Mancherial, Peddapally, Jayashankar Bhupalpally, Mulugu\n4. Suryapet, Nalgonda, Yadadri Bhongir, Jangaon\nSelect the correct code:",
        "తెలంగాణ పబ్లిక్ ఎంప్లాయ్‌మెంట్ (స్థానిక కేడర్ల వ్యవస్థీకరణ మరియు ప్రత్యక్ష నియామకాల క్రమబద్ధీకరణ) ఉత్తర్వు 2018 (జీవో నం. 124) కింద ఏర్పాటైన జోన్లను (జాబితా-I) వాటిలోని జిల్లాలతో (జాబితా-II) జతపరచండి:\nజాబితా-I (జోన్):\nA. జోన్ I (కాళేశ్వరం)\nB. జోన్ III (రాజన్న)\nC. జోన్ V (యాదాద్రి)\nD. జోన్ VII (జోగుళాంబ)\nజాబితా-II (జిల్లాలు):\n1. కరీంనగర్, రాజన్న సిరిసిల్ల, సిద్దిపేట, మెదక్, కామారెడ్డి\n2. మహబూబ్‌నగర్, నారాయణపేట, జోగుళాంబ గద్వాల, వనపర్తి, నాగర్‌కర్నూల్\n3. కొమరం భీమ్ ఆసిఫాబాద్, మంచిర్యాల, పెద్దపల్లి, జయశంకర్ భూపాలపల్లి, ములుగు\n4. సూర్యాపేట, నల్గొండ, యాదాద్రి భువనగిరి, జనగామ\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-3, B-1, C-2, D-4"],
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-3, B-1, C-2, D-4"],
        0,
        "Under the 2018 Presidential Order (providing 95% reservation for locals across 7 Zones in 2 Multi-Zones): Zone I (Kaleshwaram) spans Komaram Bheem Asifabad, Mancherial, Peddapally, Jayashankar Bhupalpally & Mulugu (A-3); Zone III (Rajanna) covers Karimnagar, Rajanna Sircilla, Siddipet, Medak & Kamareddy (B-1); Zone V (Yadadri) covers Suryapet, Nalgonda, Yadadri Bhongir & Jangaon (C-4); Zone VII (Jogulamba) comprises Mahabubnagar, Narayanpet, Jogulamba Gadwal, Wanaparthy & Nagarkurnool (D-2).",
        "2018 నూతన ప్రెసిడెన్షియల్ ఆర్డర్ (95% స్థానిక రిజర్వేషన్, 7 జోన్లు, 2 మల్టీ జోన్లు) ప్రకారం: జోన్ I కాళేశ్వరం (3), జోన్ III రాజన్న (1), జోన్ V యాదాద్రి (4), జోన్ VII జోగుళాంబ (2)."
    ),
    # T2 (corr=1: 2 and 3 only; stmt 1 false: says Kothapalli/Kotilingala had ONLY Roman gold coins and NO Satavahana pre-imperial punch-marked coins, whereas Kotilingala yielded Simuka & Chimuka pre-imperial coins!)
    make_q(
        "Ancient Telangana - Satavahana Economy, Guilds & Numismatics",
        "Consider the following statements regarding the socio-economic and archaeological heritage of Telangana under the Satavahanas:\n1. Archaeological excavations at Kotilingala (Peddapalli) yielded exclusively imported Roman Imperial gold coins with zero early Satavahana issues.\n2. Artisans and merchants organized into autonomous craft guilds called 'Shrenis' (headed by a Sreshthi), which even acted as stable banking institutions accepting permanent endowments (*Akshaya Nivi*).\n3. In the Nashik Prashasti of Gautami Balasri, Gautamiputra Satakarni is praised as 'Tri-Samudra-Toya-Pita-Vahana' (whose horses drank the waters of the three seas) and credited with defeating Saka ruler Nahapana.\nWhich of the statements given above are correct?",
        "శాతవాహనుల కాలంలో తెలంగాణ ప్రాంత సామాజిక-ఆర్థిక మరియు పురావస్తు వారసత్వానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. పెద్దపల్లి జిల్లా కోటిలింగాల వద్ద జరిపిన పురావస్తు తవ్వకాలలో ప్రారంభ శాతవాహన నాణేలు ఏవీ లభించకుండా కేవలం విదేశీ రోమన్ బంగారు నాణేలు మాత్రమే లభించాయి.\n2. చేతివృత్తిదారులు మరియు వర్తకులు 'శ్రేణులు' (Shrenis) అనే స్వయం ప్రతిపత్తి గల వ్యాపార సంఘాలుగా ఏర్పడ్డారు; ఇవి శాశ్వత ధర్మాదాయ నిధులను (అక్షయ నీవి) స్వీకరించే బ్యాంకుల వలె కూడా పనిచేశాయి.\n3. గౌతమీ బాలశ్రీ వేయించిన నాసిక్ ప్రశస్తి శాసనంలో గౌతమీపుత్ర శాతకర్ణిని 'త్రిసముద్ర తోయ పీతవాహన' అని కీర్తించడంతో పాటు శక రాజు నహపాణుని ఓడించినట్లు పేర్కొనబడింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is false. Kotilingala at the confluence of Peddavagu and Godavari famously yielded rare punch-marked silver issues and pre-imperial copper/potin coins of early Satavahana rulers including Chimuka (Simuka), Gobhada, and Samagopa, proving Telangana as an early cradle of Satavahana state formation.",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. పెద్దపల్లి జిల్లా కోటిలింగాలలో చిముఖ (సిముఖ), గోభద, సమగోప వంటి తొలి శాతవాహన రాజుల నాణేలు విస్తృతంగా లభించి తెలంగాణలో శాతవాహనుల తొలి మూలాలను నిరూపించాయి."
    ),
    # T3 (corr=2: 1 and 3 only; stmt 2 false: says Motupalli Abhaya Shasanam INCREASED customs duty to 25% & allowed confiscation of wrecked ships!)
    make_q(
        "Kakatiya Statecraft - Agrarian Tank Systems & Motupalli Edict",
        "Consider the following statements regarding the economic, irrigation, and commercial administration of the Kakatiyas:\n1. The Kakatiyas pioneered interconnected 'chain-of-tanks' (Golusu Kattu Cheruvulu) irrigation across undulating Deccan terrain, constructing monumental reservoirs such as Pakhal, Ramappa, and Laknavaram.\n2. Emperor Ganapati Deva's historic Motupalli Abhaya Shasanam (1244 CE) authorized royal officers to seize cargoes from shipwrecked foreign merchant vessels and raised customs levies to 25 percent.\n3. Village administration relied on a hereditary panel of twelve village functionaries known as the 'Ayagar' system, compensated through tax-free service lands (*Mirasi* / *Inam*) and grain shares.\nWhich of the statements given above are correct?",
        "కాకతీయుల ఆర్థిక, నీటిపారుదల మరియు వాణిజ్య పరిపాలనకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. దక్కన్ ఎగుడుదిగుడు భూభాగంలో నీటిని సమర్థవంతంగా నిల్వ చేయడానికి కాకతీయులు 'గొలుసుకట్టు చెరువుల' వ్యవస్థను అభివృద్ధి చేసి, పాకాల, రామప్ప, లక్నవరం వంటి భారీ తటాకాలను నిర్మించారు.\n2. గణపతిదేవుని ప్రసిద్ధ మోటుపల్లి అభయ శాసనం (క్రీ.శ. 1244) ప్రకారం తుఫానులలో దెబ్బతిన్న విదేశీ వ్యాపార నౌకల సరుకులను రాజ్య అధికారులు జప్తు చేసుకోవాలని మరియు కస్టమ్స్ సుంకాలను 25 శాతానికి పెంచాలని ఆదేశించబడింది.\n3. గ్రామ పరిపాలన వంశపారంపర్యంగా సేవలందించే 12 మంది గ్రామ ఉద్యోగులతో కూడిన 'అయగార్' (Ayagar) వ్యవస్థపై ఆధారపడి ఉండేది, వీరికి పన్నురహిత మాన్య భూములు మరియు ధాన్యపు వాటాలు ఇచ్చేవారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is incorrect. Ganapati Deva's Motupalli Abhaya Shasanam explicitly ABOLISHED the unjust practice of confiscating wrecked merchant ships' cargo, assured full safety to maritime traders, and fixed standardized low customs duties (e.g., 1/30th *klupta*) to boost international trade.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. గణపతిదేవుని మోటుపల్లి అభయ శాసనం ప్రకృతి వైపరీత్యాలతో దెబ్బతిన్న విదేశీ నౌకల సరుకును జప్తు చేసే పద్ధతిని రద్దు చేసి, విదేశీ వర్తకులకు రక్షణ మరియు సుంకాలలో రాయితీలను కల్పించింది."
    ),
    # T4 (corr=1: A-2, B-4, C-1, D-3 — Qutb Shahi Telugu literary classics)
    make_q(
        "Qutb Shahi Cultural Synthesis - Literary Landmarks Match",
        "Match the celebrated poets of the Golconda Qutb Shahi era (List-I) with their pioneering literary works (List-II):\nList-I:\nA. Ponnikanti Telaganarya\nB. Addanki Gangadhara Kavi\nC. Kandukuri Rudrakavi\nD. Sultan Muhammad Quli Qutb Shah\nList-II:\n1. Sugriva Vijayam (widely considered the earliest available Telugu Yakshagana)\n2. Yayati Charitramu (the first known 'Accha Telugu' kavya without Sanskrit tatsamas)\n3. Kulliyat-e-Muhammad Quli Qutb Shah (Deccani Urdu poetry anthology celebrating Bhagnagar/seasons)\n4. Tapati Samvaranopakhyanam (dedicated to Sultan Ibrahim Qutb Shah)\nSelect the correct code:",
        "గోల్కొండ కుతుబ్‌షాహీ యుగంలోని ప్రముఖ కవులను (జాబితా-I) వారి చారిత్రాత్మక సాహిత్య రచనలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. పొన్నికంటి తెలగనార్యుడు\nB. అద్దంకి గంగాధర కవి\nC. కందుకూరి రుద్రకవి\nD. సుల్తాన్ ముహమ్మద్ కులీ కుతుబ్‌షా\nజాబితా-II:\n1. సుగ్రీవ విజయం (తెలుగులో లభిస్తున్న తొలి ప్రసిద్ధ యక్షగానం)\n2. యయాతి చరిత్రము (సంస్కృత తత్సమాలు లేని తొలి అచ్చతెలుగు కావ్యం)\n3. కులియత్-ఎ-ముహమ్మద్ కులీ కుతుబ్‌షా (భాగ్‌నగర్, రుతువులను వర్ణించే దక్కనీ ఉర్దూ కవితా సంపుటి)\n4. తపతీ సంవరణోపాఖ్యానం (సుల్తాన్ ఇబ్రహీం కుతుబ్‌షాకు అంకితం చేయబడినది)\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-4, B-2, C-1, D-3", "A-2, B-4, C-1, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-1, D-2"],
        ["A-4, B-2, C-1, D-3", "A-2, B-4, C-1, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-1, D-2"],
        1,
        "Ponnikanti Telaganarya composed 'Yayati Charitramu' as the first pure 'Accha Telugu' work under Amin Khan of Patancheru (A-2). Addanki Gangadhara Kavi dedicated 'Tapati Samvaranopakhyanam' to Ibrahim Qutb Shah ('Malkibharama') (B-4). Kandukuri Rudrakavi penned 'Sugriva Vijayam', the earliest surviving Telugu Yakshagana (C-1). Muhammad Quli Qutb Shah compiled his Deccani Urdu poems in 'Kulliyat' (D-3).",
        "తెలగనార్యుడు యయాతి చరిత్రము (2), అద్దంకి గంగాధర కవి తపతీ సంవరణోపాఖ్యానం (4), కందుకూరి రుద్రకవి సుగ్రీవ విజయం (1), మరియు కులీ కుతుబ్‌షా కులియత్ (3) రచించారు."
    ),
    # T5 (corr=0: 1 and 2 only; stmt 3 false: claims 1918 Osmania University was in English medium like Madras/Calcutta, when its distinguishing feature was Urdu medium with a Translation Bureau!)
    make_q(
        "Asaf Jahi Era - Reforms & Institutions of Nizam VII Mir Osman Ali Khan",
        "Consider the following statements regarding the developmental and institutional initiatives under the VII Nizam, Mir Osman Ali Khan (1911–1948):\n1. To prevent a recurrence of the catastrophic September 1908 Musi floods, flood-mitigation reservoirs Osman Sagar (Gandipet) and Himayat Sagar were constructed across the Musi and Esi rivers, alongside the Nizamsagar project across the Manjeera.\n2. In 1937, the Nizam's government appointed a Constitutional Reforms Committee headed by Diwan Bahadur Aravamudu Iyengar to evaluate legislative representation in Hyderabad State.\n3. Osmania University, founded in 1918 via royal Firman, mandated English as its sole medium of instruction from its inception, rejecting vernacular textbooks.\nWhich of the statements given above are correct?",
        "ఏడవ నిజాం మీర్ ఉస్మాన్ అలీ ఖాన్ (1911–1948) పాలనా కాలంలో ఏర్పాటైన సంస్థలు మరియు సంస్కరణలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 1908 మూసీ వరదల వంటి విపత్తులను నివారించేందుకు మూసీ మరియు ఈసీ నదులపై ఉస్మాన్ సాగర్ (గండిపేట) మరియు హిమాయత్ సాగర్ జలాశయాలను, అలాగే మంజీరా నదిపై నిజాంసాగర్ ప్రాజెక్టును నిర్మించారు.\n2. హైదరాబాద్ సంస్థానంలో శాసనసభ ప్రాతినిధ్యంపై సిఫార్సులు చేసేందుకు 1937లో దివాన్ బహదూర్ అరవాముడు అయ్యంగార్ అధ్యక్షతన రాజ్యాంగ సంస్కరణల కమిటీని నియమించారు.\n3. 1918లో నిజాం ఫర్మానా ద్వారా స్థాపించబడిన ఉస్మానియా విశ్వవిద్యాలయం ఆరంభం నుండే భారతీయ భాషా పాఠ్యపుస్తకాలను తిరస్కరించి కేవలం ఆంగ్ల మాధ్యమాన్ని మాత్రమే తప్పనిసరి చేసింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is false. Founded in 1918, Osmania University made history as India's first modern university to adopt an Indian language—Urdu—as its medium of instruction at the higher education level, supported by a massive Translation Bureau (*Dar-ul-Tarjuma*).",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. 1918లో స్థాపితమైన ఉస్మానియా విశ్వవిద్యాలయం ఉన్నత విద్యలో భారతీయ భాష అయిన 'ఉర్దూ'ను బోధనా మాధ్యమంగా అమలు చేసిన భారతదేశపు తొలి విశ్వవిద్యాలయంగా చరిత్ర సృష్టించింది (ఇందుకోసం దారుల్ తర్జుమా అనువాద సంస్థను ఏర్పాటు చేశారు)."
    ),
    # T6 (corr=2: 1 and 3 only; stmt 2 false: says Bheem fell in 1928 while Nizam army defeated Rohillas in 1940 -> swaps centuries/dates cleanly: Ramji Gond 1860 Nirmal vs Komaram Bheem 1940 Jodeghat!)
    make_q(
        "Tribal Resistance in Telangana - Ramji Gond & Komaram Bheem",
        "Consider the following statements regarding the historic Adivasi rebellions against feudal and colonial oppression in Telangana:\n1. Ramji Gond led a fierce anti-British tribal uprising around Nirmal in 1857–1860 in alliance with Rohilla fighters, culminating in his execution at the historic 'Veyyi Urrala Marri' (Thousand Nooses Banyan Tree).\n2. Komaram Bheem launched his famous resistance at Babijheri-Jodeghat in 1885, directly prompting Nizam Salar Jung I to institute the Zilabandi revenue survey.\n3. Demanding land rights and forest autonomy under the iconic slogan 'Jal, Jangal, Zameen' (Water, Forest, Land), Komaram Bheem attained martyrdom at Jodeghat in October 1940 in action against the Nizam's armed police led by Abdul Sattar.\nWhich of the statements given above are correct?",
        "తెలంగాణలో భూస్వామ్య మరియు వలసవాద అణచివేతకు వ్యతిరేకంగా జరిగిన చారిత్రాత్మక ఆదివాసీ తిరుగుబాట్లకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. రాంజీ గోండు 1857–1860 మధ్య రోహిల్లులతో కలిసి నిర్మల్ ప్రాంతంలో బ్రిటిష్ వ్యతిరేక పోరాటం నడిపి, చారిత్రాత్మక 'వెయ్యి ఉర్రల మర్రి' వద్ద ఉరితీయబడ్డారు.\n2. కొమరం భీమ్ 1885లో జోడేఘాట్ వద్ద తిరుగుబాటు ప్రారంభించడంతో మొదటి సాలార్‌జంగ్ జిలాబందీ సర్వేను ప్రవేశపెట్టాల్సి వచ్చింది.\n3. 'జల్, జంగిల్, జమీన్' (నీరు, అడవి, భూమి) అనే మహోన్నత నినాదంతో గిరిజనుల భూమి, అటవీ హక్కుల కోసం పోరాడిన కొమరం భీమ్ అక్టోబర్ 1940లో జోడేఘాట్ వద్ద అబ్దుల్ సత్తార్ నేతృత్వంలోని నిజాం పోలీసులతో జరిగిన పోరులో అమరులయ్యారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is false (chronologically impossible). Ramji Gond was martyred in 1860 at Nirmal ('Veyyi Urrala Marri'). Decades later, Komaram Bheem led the Gond revolt in Adilabad/Asifabad agency areas with the 'Jal, Jangal, Zameen' call and died at Jodeghat in October 1940, after which anthropologist C. von Furer-Haimendorf was commissioned to formulate tribal safeguards.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. రాంజీ గోండు 1860లో నిర్మల్ వద్ద అమరులయ్యారు. కొమరం భీమ్ 1940లో జోడేఘాట్ వద్ద 'జల్, జంగిల్, జమీన్' నినాదంతో పోరాడి వీరమరణం పొందారు (1885లో కాదు)."
    ),
    # T7 (corr=0: 1 and 2 only; stmt 3 false: claims Hyderabad State Congress students shifted to Madras University instead of Nagpur University, and Congress supported British war effort in 1938)
    make_q(
        "Political Awakening - Hyderabad State Congress & Vandemataram Agitation (1938)",
        "Consider the following statements regarding the political awakening and Satyagraha movements in the Nizam's Hyderabad State in the 1930s:\n1. Founded in 1935 by reformist intelligentsia including Burgula Ramakrishna Rao and Padmaja Naidu, the 'Nizam Subjects League' (Mulki League) advocated 'Deccani nationalism' and responsible constitutional government.\n2. When students of the Osmania University B-Hostel sang 'Vandemataram' in late 1938 against the government's ban, hundreds were rusticated; many subsequently completed their education at Nagpur University under Vice-Chancellor T.J. Kedar.\n3. The Hyderabad State Congress, led by Swami Ramananda Tirtha, enthusiastically welcomed the State Government's ban on it in September 1938 and suspended political agitation until 1947.\nWhich of the statements given above are correct?",
        "1930వ దశకంలో నిజాం హైదరాబాద్ సంస్థానంలో రాజకీయ చైతన్యం మరియు సత్యాగ్రహ ఉద్యమాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 1935లో బూర్గుల రామకృష్ణారావు, పద్మజా నాయుడు తదితరులు స్థాపించిన 'నిజాం ప్రజల సంఘం' (ముల్కీ లీగ్) దక్కన్ జాతీయవాదం మరియు బాధ్యతాయుత ప్రభుత్వాన్ని డిమాండ్ చేసింది.\n2. 1938 చివరలో ఉస్మానియా విశ్వవిద్యాలయం 'బి-హాస్టల్' విద్యార్థులు నిషేధాన్ని ధిక్కరిస్తూ 'వందేమాతరం' గీతాన్ని ఆలపించినందుకు బహిష్కరణకు గురై, నాగ్‌పూర్ విశ్వవిద్యాలయ వైస్-ఛాన్సలర్ టి.జె. కేదార్ సహకారంతో అక్కడ చదువు కొనసాగించారు.\n3. సెప్టెంబర్ 1938లో నిజాం ప్రభుత్వం హైదరాబాద్ స్టేట్ కాంగ్రెస్‌పై విధించిన నిషేధాన్ని స్వామి రామానంద తీర్థ స్వాగతించి, 1947 వరకు రాజకీయ ఆందోళనను నిలిపివేశారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is false. When Sir Akbar Hydari's government banned the Hyderabad State Congress in September 1938 on communal pretexts, Swami Ramananda Tirtha and compatriots defied the ban by launching a heroic Individual/Civil Satyagraha in October 1938 (paralleling the Vandemataram student agitation).",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. 1938 సెప్టెంబర్‌లో స్టేట్ కాంగ్రెస్‌పై నిజాం ప్రభుత్వం నిషేధం విధించగా, స్వామి రామానంద తీర్థ దానిని ధిక్కరించి అక్టోబర్ 1938లోనే సత్యాగ్రహ ఉద్యమాన్ని ప్రారంభించారు."
    ),
    # T8 (corr=1: 2 and 3 only; stmt 1 false: says Vellodi was elected CM in 1952 instead of civil servant appointed CM 1949-52 while Burugula became first elected CM in 1952!)
    make_q(
        "Post-Integration Hyderabad State (1948–1956) - Land Reforms & Democracy",
        "Consider the following statements regarding the political and agrarian transition of Hyderabad State between 1948 and 1956:\n1. Following the 1952 first general elections, senior ICS administrator M.K. Vellodi became the first democratically elected Chief Minister of Hyderabad State, serving until the 1956 States Reorganisation.\n2. The landmark Hyderabad Tenancy and Agricultural Lands Act, 1950 conferred 'Protected Tenant' (*Kowludari*) status on cultivators with six years' continuous tenancy, restricting arbitrary landlord evictions.\n3. Prior to elected rule, Maj. Gen. J.N. Chaudhuri served as Military Governor (1948–1949) and enacted the Hyderabad (Abolition of Jagirs) Regulation, 1949.\nWhich of the statements given above are correct?",
        "భారత యూనియన్‌లో విలీనం తర్వాత హైదరాబాద్ రాష్ట్ర (1948–1956) రాజకీయ మరియు భూ సంస్కరణలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 1952లో జరిగిన మొదటి సార్వత్రిక ఎన్నికల తర్వాత సీనియర్ ICS అధికారి ఎం.కె. వెల్లోడి హైదరాబాద్ రాష్ట్రానికి మొట్టమొదటి ప్రజాస్వామ్యబద్ధంగా ఎన్నికైన ముఖ్యమంత్రిగా 1956 వరకు పనిచేశారు.\n2. 1950లో రూపొందించిన చారిత్రాత్మక 'హైదరాబాద్ కౌలుదారీ మరియు వ్యవసాయ భూముల చట్టం' వరుసగా ఆరేళ్లు సాగు చేసిన కౌలుదారులకు 'రక్షిత కౌలుదారు' (Protected Tenant) హక్కులను కల్పించి, భూస్వాముల తొలగింపుల నుండి రక్షణ కల్పించింది.\n3. ప్రజాప్రభుత్వ ఏర్పాటుకు ముందు మేజర్ జనరల్ జె.ఎన్. చౌదరి మిలిటరీ గవర్నర్‌గా (1948–1949) వ్యవహరించి, 1949 జాగీర్ల రద్దు నియంత్రణ చట్టాన్ని అమలు చేశారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is false. M.K. Vellodi was an appointed civil servant Chief Minister (1949–1952) heading an interim administration; Dr. Burgula Ramakrishna Rao became the first democratically elected Chief Minister of Hyderabad State following the 1952 elections (serving 1952–1956).",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. వెల్లోడి 1949–52 మధ్య కేంద్రం నియమించిన పౌర ముఖ్యమంత్రి మాత్రమే; 1952 సార్వత్రిక ఎన్నికల్లో గెలిచి ప్రజాస్వామ్యబద్ధంగా ఎన్నికైన తొలి ముఖ్యమంత్రి బూర్గుల రామకృష్ణారావు."
    ),
    # T9 (corr=2: 1 and 3 only; stmt 2 false: claims Srikrishna Committee rated Option 6 UNWORKABLE and strongly preferred immediate division into 3 states!)
    make_q(
        "Telangana Statehood Process - Srikrishna Committee Six Options (2010)",
        "Consider the following statements regarding the Justice B.N. Srikrishna Committee Report (submitted December 30, 2010) on the Telangana issue:\n1. Option 5 out of the six alternatives outlined in the Report proposed the bifurcation of Andhra Pradesh into Telangana and Seemandhra along existing boundaries, with Hyderabad serving as Telangana's capital.\n2. In its final recommendation, the Committee rejected Option 6 as legally unworkable and exclusively endorsed carving Andhra Pradesh into three separate states.\n3. Option 6—keeping Andhra Pradesh united while creating a statutorily empowered Telangana Regional Council for socio-economic and political development—was assessed by the Committee as its preferred workable option if unity could be maintained.\nWhich of the statements given above are correct?",
        "తెలంగాణ అంశంపై డిసెంబర్ 30, 2010న సమర్పించిన జస్టిస్ బి.ఎన్. శ్రీకృష్ణ కమిటీ నివేదికలోని ఆరు ప్రత్యామ్నాయాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. కమిటీ సూచించిన ఆరు ఆప్షన్లలో 'ఆప్షన్ 5' ప్రకారం ఉమ్మడి ఆంధ్రప్రదేశ్‌ను ప్రస్తుత సరిహద్దుల ప్రకారం తెలంగాణ (హైదరాబాద్ రాజధానిగా) మరియు సీమాంధ్ర రాష్ట్రాలుగా విభజించాలని పేర్కొనబడింది.\n2. తుది సిఫార్సులో ఆప్షన్ 6 చట్టబద్ధంగా సాధ్యం కాదని కమిటీ తిరస్కరించి, ఆంధ్రప్రదేశ్‌ను మూడు ప్రత్యేక రాష్ట్రాలుగా విభజించాలని మాత్రమే సిఫార్సు చేసింది.\n3. సమైక్య ఆంధ్రప్రదేశ్‌ను కొనసాగిస్తూనే తెలంగాణ ప్రాంతానికి చట్టబద్ధమైన అధికారాలతో కూడిన 'తెలంగాణ ప్రాంతీయ మండలి' (Telangana Regional Council) ఏర్పాటు చేసే 'ఆప్షన్ 6' ను కమిటీ అత్యంత ఆచరణీయమైన ప్రత్యామ్నాయంగా అభిప్రాయపడింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is false. The Srikrishna Committee (V.K. Duggal, Ranbir Singh, Ravinder Kaur, Abusaleh Shariff) presented six options; it prioritized Option 6 (united state with a statutory Telangana Regional Council) as the most workable if political consensus held, followed by Option 5 (bifurcation with Hyderabad in Telangana) as second-best—and did NOT propose three states.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. శ్రీకృష్ణ కమిటీ ఆంధ్రప్రదేశ్‌ను మూడు రాష్ట్రాలుగా విభజించాలని ఎక్కడా సూచించలేదు; ఆప్షన్ 6 (తెలంగాణ ప్రాంతీయ మండలితో సమైక్య రాష్ట్రం) ను మొదటి ప్రాధాన్యతగా మరియు ఆప్షన్ 5 (విభజన) ను రెండవ ప్రత్యామ్నాయంగా పేర్కొంది."
    ),
    # T10 (corr=0: 2-1-4-3 -> chronology: 1919 Firman -> 1969 SC A.V.S. Narasimha Rao strikes down Mulki Act Sec 3 -> Oct 1972 SC Venkata Reddy upholds Mulki Rules under Art 35(b) -> Sep 1973 Six-Point Formula / 32nd Amendment)
    make_q(
        "Telangana Movement - Legal Evolution of Mulki Safeguards Chronology",
        "Arrange the following landmark legal and constitutional milestones relating to the Mulki Rules and Telangana safeguards in strict chronological order from earliest to latest:\n1. Supreme Court strikes down Section 3 of the Public Employment (Requirement as to Residence) Act, 1957 in *A.V.S. Narasimha Rao v. State of Andhra Pradesh*\n2. Seventh Nizam issues a Firman prescribing a 15-year domicile criterion for Mulki status in Hyderabad civil services\n3. Signing of the Six-Point Formula culminating in the 32nd Constitutional Amendment Act (Articles 371D & 371E)\n4. Five-Judge Supreme Court Bench upholds the validity of pre-Constitution Mulki Rules as 'law in force' under Article 35(b) in *Director of Industries v. Venkata Reddy*\nSelect the correct chronological sequence:",
        "ముల్కీ నిబంధనలు మరియు తెలంగాణ రక్షణలకు సంబంధించిన క్రింది చారిత్రాత్మక న్యాయ, రాజ్యాంగ ఘట్టాలను ప్రాచీనత నుండి ఆధునికతకు సరైన కాలక్రమంలో అమర్చండి:\n1. 'ఎ.వి.ఎస్. నరసింహారావు వర్సెస్ ఆంధ్రప్రదేశ్' కేసులో సుప్రీంకోర్టు పబ్లిక్ ఎంప్లాయ్‌మెంట్ చట్టం సెక్షన్ 3 ను కొట్టివేయడం\n2. హైదరాబాద్ పౌర సర్వీసులలో ముల్కీ అర్హత కోసం 15 ఏళ్ల నివాస నిబంధనతో ఏడవ నిజాం ఫర్మానా జారీ చేయడం\n3. ఆర్టికల్స్ 371D మరియు 371E లకు దారితీసిన ఆరు సూత్రాల పథకం (32వ రాజ్యాంగ సవరణ) ఆమోదం\n4. 'డైరెక్టర్ ఆఫ్ ఇండస్ట్రీస్ వర్సెస్ వెంకటరెడ్డి' కేసులో ఐదుగురు న్యాయమూర్తుల సుప్రీంకోర్టు బెంచ్ ఆర్టికల్ 35(b) కింద ముల్కీ నిబంధనలు చెల్లుబాటు అవుతాయని తీర్పునివ్వడం\nసరైన కాలక్రమాన్ని ఎంచుకోండి:",
        ["2 - 1 - 4 - 3", "2 - 4 - 1 - 3", "1 - 2 - 4 - 3", "2 - 1 - 3 - 4"],
        ["2 - 1 - 4 - 3", "2 - 4 - 1 - 3", "1 - 2 - 4 - 3", "2 - 1 - 3 - 4"],
        0,
        "Chronology: (2) Nizam's Mulki Firman (1919) -> (1) A.V.S. Narasimha Rao v. State of AP (March 28, 1969, invalidating Central Mulki provisions on grounds of unequal treatment within a state) -> (4) Director of Industries v. Venkata Reddy (October 3, 1972, upholding old Hyderabad Mulki Rules as saved under Article 35(b), triggering the Jai Andhra counter-agitation) -> (3) Six-Point Formula (September 1973) & 32nd Amendment Act (1973).",
        "సరైన కాలక్రమం: (2) 1919 నిజాం ముల్కీ ఫర్మానా -> (1) మార్చి 1969 ఏవీఎస్ నరసింహారావు కేసు -> (4) అక్టోబర్ 1972 వెంకటరెడ్డి కేసు (సుప్రీంకోర్టు ముల్కీ నిబంధనలను సమర్థించడం) -> (3) సెప్టెంబర్ 1973 ఆరు సూత్రాల పథకం మరియు 32వ రాజ్యాంగ సవరణ."
    ),
    # T11 (corr=3: 1, 2, and 3 — Verified State Anthem + Dec 9 2024 Telangana Thalli statue details from search_web!)
    make_q(
        "Telangana State Symbols - State Anthem & Redesigned Telangana Thalli (2024)",
        "Consider the following statements regarding the revised cultural symbols adopted by the Government of Telangana in 2024:\n1. Poet Ande Sri's iconic song 'Jaya Jaya He Telangana', musically arranged in full (13.5-minute) and short (2.5-minute) renditions by M.M. Keeravani, was officially notified as the Telangana State Anthem.\n2. Unveiled at the Dr. B.R. Ambedkar Secretariat on December 9, 2024, the redesigned Telangana Thalli statue was conceptualized by Prof. T. Gangadhar and sculpted by Ramana Reddy.\n3. Replacing royal crown motifs, the new Telangana Thalli portrays an everyday rural woman in a green saree carrying native crops (paddy, maize, pearl millet, and foxtail millet) atop a pedestal of clenched fists symbolizing the statehood struggle.\nWhich of the statements given above are correct?",
        "2024లో తెలంగాణ ప్రభుత్వం స్వీకరించిన రాష్ట్ర సాంస్కృతిక చిహ్నాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. కవి అందెశ్రీ రచించిన 'జయ జయహే తెలంగాణ' గీతానికి ఎం.ఎం. కీరవాణి సంగీతం సమకూర్చగా (పూర్తి మరియు సంక్షిప్త నిడివితో) దానిని అధికారిక రాష్ట్ర గీతంగా నోటిఫై చేశారు.\n2. డిసెంబర్ 9, 2024న డాక్టర్ బి.ఆర్. అంబేద్కర్ రాష్ట్ర సచివాలయంలో ఆవిష్కరించబడిన నూతన తెలంగాణ తల్లి విగ్రహాన్ని ప్రొఫెసర్ టి. గంగాధర్ రూపొందించగా, శిల్పి రమణారెడ్డి చెక్కారు.\n3. రాచరిక కిరీటం స్థానంలో ఆకుపచ్చ చీర ధరించిన సాధారణ గ్రామీణ మహిళ రూపంలో, ఎడమ చేతిలో వరి, మొక్కజొన్న, సజ్జలు, కొర్రలు ధరించి, తెలంగాణ ఉద్యమ స్ఫూర్తికి ప్రతీకగా పిడికిళ్ల పీఠంపై నిలబడినట్లు ఈ విగ్రహాన్ని తీర్చిదిద్దారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. 'Jaya Jaya He Telangana' (Ande Sri / M.M. Keeravani) became the official State Song on June 2, 2024, while the redesigned Telangana Thalli statue (Prof. T. Gangadhar & sculptor Ramana Reddy) was unveiled on December 9, 2024 at the State Secretariat.",
        "మూడు ప్రకటనలూ సరైనవే. అందెశ్రీ గీతానికి కీరవాణి సంగీతంతో రాష్ట్ర అధికారిక గీతంగా ప్రకటించారు. డిసెంబర్ 9, 2024న సచివాలయంలో ప్రొ. గంగాధర్ డిజైన్, శిల్పి రమణారెడ్డి రూపొందించిన నూతన తెలంగాణ తల్లి విగ్రహాన్ని ఆవిష్కరించారు."
    ),
    # T12 (corr=1: A-3, B-4, C-2, D-1 — Telangana Tribal & Regional Fairs + Handicraft GI Tags)
    make_q(
        "Telangana Tribal Culture & GI Heritage - Fairs & Artisans Match",
        "Match the following cultural traditions/GI heritage clusters of Telangana (List-I) with their defining community or geographical association (List-II):\nList-I:\nA. Nagoba Jatara (Keslapur)\nB. Edupayala Vana Durga Bhavani Jatara\nC. Puttapaka Telia Rumal\nD. Gussadi Tribal Dance (Padma Shri Kanaka Raju)\nList-II:\n1. Raj Gond winter harvest dance performed during Dandari festival wearing peacock-feather headgear\n2. Traditional double-ikat cotton cloth treated with castor-oil alizarin dye in Yadadri Bhongir district (GI tag 2020)\n3. Mesram clan of the Raj Gond tribe in Indravelli mandal, Adilabad district\n4. Confluence of seven streams of the Manjeera River near Medak during Maha Shivaratri\nSelect the correct code:",
        "తెలంగాణ గిరిజన సాంస్కృతిక జాతరలు మరియు జీఐ ట్యాగ్ కళారూపాలను (జాబితా-I) వాటి సంప్రదాయ లేదా ప్రాంతీయ వివరాలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. నాగోబా జాతర (కేస్లాపూర్)\nB. ఏడుపాయల వనదుర్గా భవానీ జాతర\nC. పుట్టపాక తేలియా రుమాల్\nD. గుస్సాడీ గిరిజన నృత్యం (పద్మశ్రీ కనకరాజు)\nజాబితా-II:\n1. దండారి ఉత్సవాలలో రాజ్‌గోండులు నెమలి పింఛాల తలపాగా ధరించి ప్రదర్శించే శీతాకాల నృత్యం\n2. యాదాద్రి భువనగిరి జిల్లాలో ఆముదం నూనెతో ప్రాసెస్ చేసే సాంప్రదాయ డబుల్-ఇక్కత్ వస్త్రం (2020లో GI ట్యాగ్)\n3. ఆదిలాబాద్ జిల్లా ఇంద్రవెల్లి మండలంలో రాజ్‌గోండులలోని మెస్సారం వంశీయుల పవిత్ర జాతర\n4. మహాశివరాత్రి సమయంలో మెదక్ సమీపంలో మంజీరా నది ఏడు పాయలుగా చీలి కలిసే క్షేత్రంలో జరిగే జాతర\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-3, B-2, C-4, D-1", "A-3, B-4, C-2, D-1", "A-4, B-3, C-2, D-1", "A-1, B-4, C-2, D-3"],
        ["A-3, B-2, C-4, D-1", "A-3, B-4, C-2, D-1", "A-4, B-3, C-2, D-1", "A-1, B-4, C-2, D-3"],
        1,
        "Nagoba Jatara at Keslapur (Indravelli, Adilabad) is the sacred annual assembly of the Mesram clan of Raj Gonds (A-3). Edupayala Jatara takes place at the seven-stream bifurcation of the Manjeera River in Medak (B-4). Telia Rumal of Puttapaka (Choutuppal/Yadadri Bhongir) earned GI status in 2020 (C-2). Gussadi is the iconic Raj Gond Dandari folk dance championed by late Padma Shri awardee Kanaka Raju (D-1).",
        "కేస్లాపూర్ నాగోబా జాతర ఆదిలాబాద్ మెస్సారం రాజ్‌గోండులది (3); ఏడుపాయల జాతర మెదక్ మంజీరా నది వద్ద (4); పుట్టపాక తేలియా రుమాల్ యాదాద్రి భువనగిరి GI ట్యాగ్ (2); గుస్సాడీ దండారి ఉత్సవ నృత్యం (1)."
    ),
    # T13 (corr=2: 1 and 3 only; stmt 2 false: says Musi flows east via Medak to join Godavari instead of Krishna at Wadapalli!)
    make_q(
        "Telangana Drainage & Geo-Hydrology - Sub-Basin Characteristics",
        "Consider the following statements regarding the river drainage system of Telangana:\n1. Originating in the Ananthagiri Hills of Vikarabad district, the Musi River (historically *Muchukunda*) flows eastward through Hyderabad and joins the Krishna River at Wadapalli (Nalgonda district).\n2. The Manjeera River rises in the Balaghat Hills of Maharashtra and flows into Telangana before emptying directly into the Bay of Bengal near Machilipatnam without joining any larger river.\n3. Both the Pranhita (confluence of Wardha, Penganga, and Wainganga) and the Indravati join the Godavari River as left-bank tributaries along Telangana's northern and eastern borderlands.\nWhich of the statements given above are correct?",
        "తెలంగాణ నదీ వ్యవస్థ మరియు జలవనరులకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. వికారాబాద్ జిల్లా అనంతగిరి కొండలలో జన్మించే మూసీ నది (ప్రాచీన నామం ముచుకుంద) హైదరాబాద్ గుండా తూర్పుగా ప్రవహించి నల్గొండ జిల్లా వాడపల్లి వద్ద కృష్ణా నదిలో కలుస్తుంది.\n2. మహారాష్ట్రలోని బాలాఘాట్ కొండలలో జన్మించే మంజీరా నది తెలంగాణలోకి ప్రవేశించి, ఏ ప్రధాన నదిలోనూ కలవకుండా నేరుగా మచిలీపట్నం వద్ద బంగాళాఖాతంలో కలుస్తుంది.\n3. ప్రాణహిత (వార్ధా, పెన్‌గంగా, వైన్‌గంగాల సంగమం) మరియు ఇంద్రావతి నదులు తెలంగాణ ఉత్తర, తూర్పు సరిహద్దుల వెంబడి గోదావరిలో ఎడమ గట్టు ఉపనదులుగా కలుస్తాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is incorrect. Rising in Maharashtra's Balaghat ranges, the Manjeera flows through Sangareddy, Medak, and Kamareddy (powering Singur and Nizamsagar dams) before joining the GODAVARI River as a major right-bank tributary near Kandakurthi (Triveni Sangamam, Nizamabad), not empty into the sea directly.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. మంజీరా నది నిజామాబాద్ జిల్లా కందకుర్తి (త్రివేణి సంగమం) వద్ద గోదావరిలో కుడి గట్టు ఉపనదిగా కలుస్తుంది తప్ప నేరుగా సముద్రంలో కలవదు."
    ),
]

# ==================== 3. HISTORY NEW (10) ====================
NEW_HISTORY = [
    # H1 (corr=0: A-3, B-1, C-4, D-2 — Rigvedic rivers + Shad-Darshanas)
    make_q(
        "Ancient India - Orthodox Philosophical Systems (Shad-Darshanas)",
        "Match the classical Hindu philosophical schools ('Shad-Darshanas') in List-I with their traditional founders and core epistemic focus in List-II:\nList-I:\nA. Sankhya\nB. Vaisheshika\nC. Nyaya\nD. Purva Mimamsa\nList-II:\n1. Sage Kanada; atomic pluralism (*Paramanu*) and categories of reality (*Padarthas*)\n2. Sage Jaimini; Vedic hermeneutics, ritual duty (*Dharma*), and authority of the Vedas\n3. Sage Kapila; dualism of eternal Consciousness (*Purusha*) and Matter (*Prakriti*)\n4. Aksapada Gautama; systematic logic, syllogism, and valid sources of knowledge (*Pramanas*)\nSelect the correct code:",
        "ప్రాచీన భారతీయ ఆరు దర్శనాలను (షడ్దర్శనాలు) (జాబితా-I) వాటి ప్రవక్తలు మరియు సిద్ధాంతాలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. సాంఖ్యం\nB. వైశేషికం\nC. న్యాయం\nD. పూర్వ మీమాంస\nజాబితా-II:\n1. కణాద మహర్షి; పరమాణు వాదం మరియు పదార్థ వర్గీకరణ\n2. జైమిని మహర్షి; వేద కర్మకాండల వివరణ మరియు వేద ప్రమాణికత\n3. కపిల మహర్షి; పురుష (చైతన్యం) మరియు ప్రకృతి (జడత్వం) ద్వైత సిద్ధాంతం\n4. గౌతమ మహర్షి; తార్కిక శాస్త్రం, ప్రమాణాలు మరియు జ్ఞాన మీమాంస\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3"],
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3"],
        0,
        "Sankhya (Sage Kapila) posits Purusha-Prakriti dualism (A-3). Vaisheshika (Sage Kanada) analyzes atomism and categories (B-1). Nyaya (Gautama) formalizes Indian logic and Pramanas (C-4). Purva Mimamsa (Jaimini) emphasizes Vedic exegesis and Dharma (D-2). (The remaining two are Yoga by Patanjali and Vedanta by Badarayana.)",
        "సాంఖ్యం-కపిల మహర్షి (3), వైశేషికం-కణాదుడు (1), న్యాయం-గౌతముడు (4), పూర్వ మీమాంస-జైమిని (2). (మిగిలిన రెండు యోగ-పతంజలి, వేదాంతం-బాదరాయణుడు)."
    ),
    # H2 (corr=1: 2 and 3 only; stmt 1 false: reverses Pataliputra & Vallabhi councils — 1st was at Pataliputra under Sthulabhadra, 2nd was at Vallabhi 512 CE under Devardhi!)
    make_q(
        "Jainism - Doctrinal Philosophy & Historic Councils",
        "Consider the following statements regarding Jain philosophy and the two major Jain Councils:\n1. The First Jain Council was held at Vallabhi (Gujarat) in 512 CE under Sthulabhadra to permanently reconcile the Svetambara and Digambara sects.\n2. 'Anekantavada' (doctrine of manifold aspects of reality) and 'Syadvada' (relativity of judgments, expressed through *Saptabhangi* seven-fold predication) form the epistemological core of Jainism.\n3. The 'Triratnas' (Three Jewels) leading to liberation (*Moksha*) in Jainism are Right Faith (*Samyak Darshana*), Right Knowledge (*Samyak Jnana*), and Right Conduct (*Samyak Charitra*).\nWhich of the statements given above are correct?",
        "జైన తత్వశాస్త్రం మరియు జైన మహాసభలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. శ్వేతాంబర మరియు దిగంబర శాఖలను శాశ్వతంగా ఏకం చేయడానికి క్రీ.శ. 512లో వల్లభి (గుజరాత్) లో స్థూలభద్రుని అధ్యక్షతన మొదటి జైన మహాసభ జరిగింది.\n2. 'అనేకాంతవాదం' (సత్యానికి అనేక కోణాలు) మరియు 'స్యాద్వాదం' (సప్తభంగి న్యాయం ద్వారా సాపేక్ష జ్ఞానం) జైన జ్ఞానమీమాంసకు మూలస్తంభాలు.\n3. జైనంలో మోక్షప్రాప్తికి మార్గమైన 'త్రిరత్నాలు' అనగా సమ్యక్ దర్శనం (సరైన విశ్వాసం), సమ్యక్ జ్ఞానం (సరైన జ్ఞానం) మరియు సమ్యక్ చారిత్ర్యం (సరైన ప్రవర్తన).\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is incorrect. The First Jain Council was held at Pataliputra around c. 300 BCE under Sthulabhadra (where the Digambaras refused participation); the Second Jain Council was held at Vallabhi in 512 CE presided over by Devardhi Kshamasramana, finalizing the Svetambara Siddhanta scriptures.",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. మొదటి జైన సభ క్రీ.పూ. 300 ప్రాంతంలో పాటలీపుత్రలో స్థూలభద్రుని అధ్యక్షతన జరిగింది; రెండవ జైన సభ క్రీ.శ. 512లో వల్లభిలో దేవర్ధి క్షమాశ్రమణుని నేతృత్వంలో జరిగింది."
    ),
    # H3 (corr=2: 1 and 3 only; stmt 2 false: says Maski edict was found in Odisha and mentions Dhamma Mahamattas -> Maski in Karnataka first named "Devanampiya Asoka", whereas MRE V appoints Dhamma Mahamattas!)
    make_q(
        "Mauryan Epigraphy - Ashokan Edicts & Dhamma Policy",
        "Consider the following pairs linking Ashokan inscriptions with their historic significance:\n1. Major Rock Edict II — Mentions medical provisions for humans and animals, and names southern kingdoms of Cholas, Pandyas, Satiyaputras, and Keralaputras.\n2. Maski Minor Rock Edict (Raichur, Karnataka) — Located in Odisha; first revealed Kalinga war casualties exceeding one lakh soldiers.\n3. Rummindei (Lumbini) Pillar Edict — Commemorates Ashoka's pilgrimage to Buddha's birthplace in his 20th regnal year, reducing land revenue (*Bhaga*) to one-eighth.\nWhich of the statements given above are correct?",
        "మౌర్య చక్రవర్తి అశోకుని శాసనాలు మరియు వాటి చారిత్రాత్మక ప్రాముఖ్యతకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. రెండవ ప్రధాన శిలాశాసనం — మానవులకు మరియు పశువులకు వైద్య సదుపాయాల ఏర్పాటుతో పాటు దక్షిణాది రాజ్యాలైన చోళ, పాండ్య, సతియపుత్ర, కేరళపుత్రుల పేర్లను ప్రస్తావిస్తుంది.\n2. మస్కి లఘు శిలాశాసనం — ఒడిశాలో కనుగొనబడింది; కళింగ యుద్ధంలో లక్ష మందికి పైగా మరణించిన విషాదాన్ని తొలిసారిగా ఇందులో వివరించారు.\n3. రుమ్మిందెయి (లుంబిని) స్తంభ శాసనం — తన పట్టాభిషేకం జరిగిన 20వ ఏట అశోకుడు బుద్ధుని జన్మస్థలాన్ని సందర్శించి, భూమి పన్ను ('భాగ') ను 1/8వ వంతుకు తగ్గించినట్లు పేర్కొంటుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is wrong. Maski Minor Rock Edict (in Raichur, Karnataka) is famous because it was the FIRST inscription discovered (1915) explicitly mentioning Ashoka's personal name ('Devanampiya Asoka'); Kalinga war devastation is described in Major Rock Edict XIII.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. కర్ణాటకలోని మస్కి శాసనం 'దేవానాంప్రియ అశోక' అనే పేరును తొలిసారిగా బయటపెట్టిన శాసనంగా ప్రసిద్ధి చెందింది; కళింగ యుద్ధ ప్రస్తావన 13వ ప్రధాన శిలాశాసనంలో ఉంది."
    ),
    # H4 (corr=0: 1 and 2 only; stmt 3 false: swaps Chishtiyya & Naqshbandiyya -> Naqshbandi rejected Sama music & pantheistic Wahdat-ul-Wujud, whereas Chishtis embraced Sama and avoided court offices!)
    make_q(
        "Medieval India - Bhakti & Sufi Reform Movements",
        "Consider the following statements regarding medieval Bhakti and Sufi spiritual traditions in India:\n1. In 12th-century Karnataka, Basavanna's Virashaiva (Lingayat) movement rejected caste hierarchy and Vedic rituals, expressing egalitarian philosophy in vernacular Kannada prose-poems called *Vachanas*.\n2. The Chishtiyya Sufi order (associated with Khwaja Muinuddin Chishti and Nizamuddin Auliya) practiced musical assemblies (*Sama*), shunned state patronage, and welcomed people across religious boundaries.\n3. Unlike the Chishtis, the Naqshbandiyya order (represented by Shaikh Ahmad Sirhindi) championed *Sama* musical gatherings and completely rejected orthodox Sharia compliance.\nWhich of the statements given above are correct?",
        "మధ్యయుగ భారతదేశంలోని భక్తి మరియు సూఫీ ఆధ్యాత్మిక ఉద్యమాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 12వ శతాబ్దపు కర్ణాటకలో బసవన్న ప్రారంభించిన వీరశైవ (లింగాయత్) ఉద్యమం కుల వివక్షను, వేద కర్మకాండలను తిరస్కరించి కన్నడలో 'వచనాల' ద్వారా సమసమాజాన్ని ప్రబోధించింది.\n2. ఖ్వాజా మొయినుద్దీన్ చిస్తీ, నిజాముద్దీన్ ఔలియా ప్రోత్సహించిన చిస్తీ సూఫీ శాఖ 'సమా' (సంగీత సభలు) ను ఆచరిస్తూ, రాజ్యాధికార పదవులకు దూరంగా ఉంటూ మత సామరస్యాన్ని బోధించింది.\n3. చిస్తీలకు భిన్నంగా షేక్ అహ్మద్ సిర్హింది ప్రాతినిధ్యం వహించిన నక్షబందీ శాఖ సంగీత 'సమా' సభలను విస్తృతంగా ప్రోత్సహించి, కఠిన షరియత్ నిబంధనలను తిరస్కరించింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is incorrect. The Naqshbandi Silsila (introduced in India by Khwaja Baqi Billah and championed by Shaikh Ahmad Sirhindi *Mujaddid-i-Alf-Sani*) strictly adhered to orthodox Sunni Sharia law, opposed *Sama* music, and propounded *Wahdat-ul-Shuhud* over *Wahdat-ul-Wujud*.",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. నక్షబందీ సూఫీ శాఖ (షేక్ అహ్మద్ సిర్హింది) కఠిన షరియత్ సంప్రదాయాన్ని సమర్థిస్తూ, సంగీత సభలను ('సమా') పూర్తిగా వ్యతిరేకించింది."
    ),
    # H5 (corr=1: A-2, B-4, C-1, D-3 — Vijayanagara foreign accounts)
    make_q(
        "Medieval India - Foreign Travellers in the Vijayanagara Empire",
        "Match the foreign travellers who visited the Vijayanagara Empire (List-I) with the reigning monarch/era and notable observations recorded in their chronicles (List-II):\nList-I:\nA. Nicolo de Conti (Italian)\nB. Abdur Razzaq (Persian Ambassador)\nC. Domingo Paes (Portuguese)\nD. Fernao Nuniz (Portuguese Horse Trader)\nList-II:\n1. Visited during Krishnadevaraya's reign; compared the city of Vijayanagara to Rome in grandeur\n2. Visited during Deva Raya I's reign (c. 1420 CE); described Vijayanagara festivals like Navaratri\n3. Visited during Achyuta Deva Raya's reign (c. 1535 CE); recorded women serving as royal accountants and guards\n4. Ambassador of Shah Rukh of Timurid Persia during Deva Raya II's reign (1443 CE); lauded the seven concentric fortified walls\nSelect the correct code:",
        "విజయనగర సామ్రాజ్యాన్ని సందర్శించిన విదేశీ యాత్రికులను (జాబితా-I) వారి పాలనా కాలం మరియు చారిత్రక వర్ణనలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. నికోలో డి కాంటి (ఇటలీ)\nB. అబ్దుర్ రజాక్ (పర్షియా రాయబారి)\nC. డొమింగో పేస్ (పోర్చుగీసు)\nD. ఫెర్నావో న్యూనిజ్ (పోర్చుగీసు అశ్వ వ్యాపారి)\nజాబితా-II:\n1. శ్రీకృష్ణదేవరాయల కాలంలో పర్యటించి విజయనగర నగరాన్ని రోమ్ నగరంతో పోల్చారు\n2. మొదటి దేవరాయల కాలంలో (క్రీ.శ. 1420) పర్యటించి నవరాత్రి ఉత్సవాలను వర్ణించారు\n3. అచ్యుత దేవరాయల కాలంలో (క్రీ.శ. 1535) పర్యటించి రాజ్య లెక్కల విభాగాల్లో మహిళల పాత్రను ప్రస్తావించారు\n4. రెండవ దేవరాయల కాలంలో (1443) పర్షియా రాయబారిగా వచ్చి ఏడు ప్రాకారాల కోటలను ప్రశంసించారు\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-4, B-2, C-1, D-3", "A-2, B-4, C-1, D-3", "A-2, B-1, C-4, D-3", "A-1, B-4, C-2, D-3"],
        ["A-4, B-2, C-1, D-3", "A-2, B-4, C-1, D-3", "A-2, B-1, C-4, D-3", "A-1, B-4, C-2, D-3"],
        1,
        "Chronological match of Vijayanagara foreign observers: Nicolo Conti visited under Deva Raya I (A-2); Persian envoy Abdur Razzaq visited under Deva Raya II in 1443 CE (B-4); Domingo Paes chronicled Krishnadevaraya's golden rule (C-1); and Fernao Nuniz documented Achyuta Deva Raya's court in 1535–37 CE (D-3).",
        "నికోలో డి కాంటి - మొదటి దేవరాయలు (2); అబ్దుర్ రజాక్ - రెండవ దేవరాయలు (4); డొమింగో పేస్ - శ్రీకృష్ణదేవరాయలు (1); ఫెర్నావో న్యూనిజ్ - అచ్యుత దేవరాయలు (3)."
    ),
    # H6 (corr=2: 1 and 3 only; stmt 2 false: says Ryotwari recognized zamindars as hereditary owners & covered Bengal, whereas Permanent Settlement did that & Ryotwari covered Madras/Bombay!)
    make_q(
        "Modern India - Colonial Land Revenue Settlements",
        "Consider the following statements regarding British land revenue settlements in India:\n1. Under the Permanent Settlement (1793), engineered by Lord Cornwallis and Sir John Shore across Bengal, Bihar, and Orissa, zamindars were recognized as hereditary owners of the soil subject to paying a fixed 10/11th revenue share to the Company under the 'Sunset Law'.\n2. Introduced by Thomas Munro and Alexander Read in Bengal and Awadh, the Ryotwari system eliminated direct contact with peasants and vested sole proprietary rights in village zamindars.\n3. Formulated by Holt Mackenzie in 1822 across the North-Western Provinces and parts of Punjab (later revised by Robert Merttins Bird), the Mahalwari system assessed revenue collectively on village communities (*Mahals*).\nWhich of the statements given above are correct?",
        "బ్రిటిష్ పాలనలోని భూమి శిస్తు విధానాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. లార్డ్ కార్న్‌వాలిస్ మరియు సర్ జాన్ షోర్ రూపొందించిన శాశ్వత శిస్తు పద్ధతి (1793) ద్వారా బెంగాల్, బీహార్, ఒడిశాల్లో జమీందార్లకు భూమిపై వంశపారంపర్య హక్కులు కల్పించి, 'సూర్యాస్తమయ చట్టం' ప్రకారం కంపెనీకి పన్ను వసూలులో 10/11వ వంతు చెల్లించేలా నిర్ణయించారు.\n2. బెంగాల్ మరియు అవధ్ ప్రాంతాల్లో థామస్ మన్రో, అలెగ్జాండర్ రీడ్ ప్రవేశపెట్టిన రైత్వారీ విధానం రైతులతో ప్రత్యక్ష సంబంధాలను రద్దు చేసి జమీందార్లకు పూర్తి యాజమాన్య హక్కులను ఇచ్చింది.\n3. వాయవ్య ప్రావిన్సులు మరియు పంజాబ్ ప్రాంతాల్లో 1822లో హోల్ట్ మెకంజీ రూపొందించిన మహల్వారీ విధానంలో పన్నును వ్యక్తిగత రైతులపై కాకుండా గ్రామం లేదా 'మహల్' సమూహంపై సమిష్టిగా విధించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is wrong. Introduced by Alexander Read (Baramahal, 1792) and Thomas Munro (Madras Presidency, 1820) and later extended to Bombay Presidency by Elphinstone, the Ryotwari system eliminated intermediary zamindars and settled revenue DIRECTLY with individual cultivating peasants (*Ryots*).",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. థామస్ మన్రో మరియు అలెగ్జాండర్ రీడ్ మద్రాసు, బాంబే ప్రెసిడెన్సీలలో ప్రవేశపెట్టిన రైత్వారీ విధానంలో మధ్యవర్తి జమీందార్లను తొలగించి నేరుగా రైతులతోనే భూమి ఒప్పందాలు కుదుర్చుకున్నారు."
    ),
    # H7 (corr=0: 2-1-4-3 — Viceroy reforms chronology: Sati 1829 -> Widow Remarriage 1856 -> Ilbert Bill 1883 -> Age of Consent 1891)
    make_q(
        "Modern India - Socio-Legal Reforms & Viceroys Chronology",
        "Arrange the following socio-legal and legislative enactments of British India in chronological order from earliest to latest:\n1. Enactment of the Hindu Widows' Remarriage Act (Act XV of 1856) championed by Ishwar Chandra Vidyasagar\n2. Promulgation of Bengal Regulation XVII abolishing the practice of Sati under Governor-General Lord William Bentinck\n3. Passage of the Age of Consent Act, 1891 raising the minimum statutory age of consent for girls from 10 to 12 years under Lord Lansdowne (supported by Behramji Malabari)\n4. Introduction of the Ilbert Bill seeking to abolish judicial racial disqualification of Indian magistrates under Lord Ripon\nSelect the correct chronological sequence:",
        "బ్రిటిష్ భారతదేశంలోని క్రింది సామాజిక-న్యాయ చట్టాలను ప్రాచీనత నుండి ఆధునికతకు సరైన కాలక్రమంలో అమర్చండి:\n1. ఈశ్వరచంద్ర విద్యాసాగర్ కృషితో హిందూ వితంతు పునర్వివాహ చట్టం (1856) రూపొందించబడటం\n2. గవర్నర్ జనరల్ లార్డ్ విలియం బెంటింక్ 'సతీ సహగమన నిషేధ చట్టం' (బెంగాల్ రెగ్యులేషన్ XVII) జారీ చేయడం\n3. బెహరాంజీ మలబారి కృషి, లార్డ్ లాన్స్‌డౌన్ కాలంలో బాలికల వివాహ సమ్మతి వయసును 10 నుండి 12 ఏళ్లకు పెంచుతూ 'ఏజ్ ఆఫ్ కన్సెంట్ చట్టం, 1891' ఆమోదించబడటం\n4. భారతీయ న్యాయమూర్తులపై జాతి వివక్షను తొలగించడానికి లార్డ్ రిప్పన్ హయాంలో 'ఇల్బర్ట్ బిల్లు' ప్రవేశపెట్టబడటం\nసరైన కాలక్రమాన్ని ఎంచుకోండి:",
        ["2 - 1 - 4 - 3", "2 - 4 - 1 - 3", "1 - 2 - 4 - 3", "2 - 1 - 3 - 4"],
        ["2 - 1 - 4 - 3", "2 - 4 - 1 - 3", "1 - 2 - 4 - 3", "2 - 1 - 3 - 4"],
        0,
        "Chronology: (2) Abolition of Sati (December 1829 under Lord William Bentinck, urged by Raja Ram Mohan Roy) -> (1) Hindu Widows' Remarriage Act (July 1856, drafted under Dalhousie and enacted under Canning) -> (4) Ilbert Bill Controversy (1883–84 under Lord Ripon) -> (3) Age of Consent Act (March 1891 under Lord Lansdowne).",
        "సరైన కాలక్రమం: (2) 1829 సతీ నిషేధం -> (1) 1856 వితంతు పునర్వివాహ చట్టం -> (4) 1883–84 ఇల్బర్ట్ బిల్లు వివాదం -> (3) 1891 ఏజ్ ఆఫ్ కన్సెంట్ చట్టం."
    ),
    # H8 (corr=1: A-2, B-4, C-1, D-3 — Anti-caste reform organizations match)
    make_q(
        "Social Justice Movements - Reform Organizations & Publications Match",
        "Match the pioneering anti-caste and social justice leaders (List-I) with their landmark institutions or publications (List-II):\nList-I:\nA. Mahatma Jyotirao Phule\nB. Sree Narayana Guru\nC. E.V. Ramasamy 'Periyar'\nD. Dr. B.R. Ambedkar\nList-II:\n1. Vaikom involvement, Self-Respect Movement (1925), and *Kudi Arasu* journal\n2. Satyashodhak Samaj (1873) and *Gulamgiri* (*Slavery*)\n3. Bahishkrit Hitakarini Sabha (1924), Mahad Chowdar Tank Satyagraha (1927), and *Mooknayak*\n4. Aruvippuram Shiva installation (1888) and co-founding inspiration behind SNDP Yogam (1903)\nSelect the correct code:",
        "సామాజిక న్యాయ మరియు కులవ్యతిరేక ఉద్యమ నేతలను (జాబితా-I) వారి సంస్థలు లేదా ప్రచురణలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. మహాత్మా జ్యోతిరావ్ పూలే\nB. శ్రీ నారాయణ గురు\nC. ఇ.వి. రామసామి 'పెరియార్'\nD. డాక్టర్ బి.ఆర్. అంబేద్కర్\nజాబితా-II:\n1. వైకోం పోరాటంలో భాగస్వామ్యం, ఆత్మగౌరవ ఉద్యమం (1925) మరియు 'కుడి అరసు' పత్రిక\n2. సత్యశోధక్ సమాజ్ (1873) మరియు 'గులాంగిరి' (బానిసత్వం) గ్రంథం\n3. బహిష్కృత హితకారిణి సభ (1924), మహద్ చెరువు సత్యాగ్రహం (1927) మరియు 'మూక్ నాయక్'\n4. అరువిప్పురం శివ ప్రతిష్ఠ (1888) మరియు SNDP యోగం (1903) స్థాపనకు ప్రేరణ\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-4, B-2, C-1, D-3", "A-2, B-4, C-1, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-1, D-2"],
        ["A-4, B-2, C-1, D-3", "A-2, B-4, C-1, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-1, D-2"],
        1,
        "Jyotirao Phule founded Satyashodhak Samaj in Pune (1873) and authored *Gulamgiri* (A-2). Sree Narayana Guru consecrated a Shiva idol at Aruvippuram (1888) inspiring SNDP Yogam (B-4). Periyar launched the Self-Respect Movement (1925) and *Kudi Arasu* (C-1). Dr. B.R. Ambedkar established Bahishkrit Hitakarini Sabha (1924), led the Mahad Satyagraha (1927), and started *Mooknayak* (1920) (D-3).",
        "జ్యోతిరావ్ పూలే - సత్యశోధక్ సమాజ్/గులాంగిరి (2); నారాయణ గురు - అరువిప్పురం/SNDP (4); పెరియార్ - ఆత్మగౌరవ ఉద్యమం (1); అంబేద్కర్ - మహద్ సత్యాగ్రహం/మూక్ నాయక్ (3)."
    ),
    # H9 (corr=2: 1 and 3 only; stmt 2 false: says Kalpana Datta & Pritilata Waddedar led Kakori Conspiracy in UP 1925 -> actually Ram Prasad Bismil & Ashfaqulla led Kakori; Kalpana & Pritilata were heroes of Chittagong 1930 under Surya Sen!)
    make_q(
        "Revolutionary Nationalism - HRA, HSRA & Chittagong Uprising",
        "Consider the following statements regarding the second phase of revolutionary nationalism during India's freedom struggle:\n1. Originally founded at Kanpur in 1924 as the Hindustan Republican Association (HRA), the organization was restructured into the Hindustan Socialist Republican Association (HSRA) in September 1928 at Feroz Shah Kotla, Delhi, under Chandrashekhar Azad's leadership.\n2. Freedom fighters Kalpana Datta and Pritilata Waddedar masterminded the Kakori Train Action in Uttar Pradesh in August 1925 under the banner of the Anushilan Samiti.\n3. In April 1930, 'Masterda' Surya Sen led the Indian Republican Army in the historic Chittagong Armoury Raid, establishing a short-lived provisional revolutionary government.\nWhich of the statements given above are correct?",
        "భారత స్వాతంత్ర్య పోరాటంలో రెండవ దశ విప్లవ జాతీయవాద ఉద్యమాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 1924లో కాన్పూర్‌లో ఏర్పడిన 'హిందుస్తాన్ రిపబ్లికన్ అసోసియేషన్' (HRA), సెప్టెంబర్ 1928లో ఢిల్లీలోని ఫిరోజ్ షా కోట్లా వద్ద చంద్రశేఖర్ ఆజాద్ నేతృత్వంలో 'హిందుస్తాన్ సోషలిస్ట్ రిపబ్లికన్ అసోసియేషన్' (HSRA) గా పునర్వ్యవస్థీకరించబడింది.\n2. విప్లవ వీరనారీమణులు కల్పనా దత్తా మరియు ప్రీతిలతా వాడేదార్లు అనుశీలన్ సమితి ఆధ్వర్యంలో ఆగస్టు 1925లో ఉత్తరప్రదేశ్‌లోని కాకోరి రైలు దోపిడీకి (Kakori Train Action) నేతృత్వం వహించారు.\n3. ఏప్రిల్ 1930లో 'మాస్టర్‌దా' సూర్య సేన్ ఇండియన్ రిపబ్లికన్ ఆర్మీకి నాయకత్వం వహిస్తూ చిట్టగాంగ్ ఆయుధాగారంపై దాడి చేసి తాత్కాలిక విప్లవ ప్రభుత్వాన్ని ప్రకటించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is incorrect. The Kakori Train Action (August 9, 1925) was executed by Ram Prasad Bismil, Ashfaqulla Khan, Rajendra Lahiri, Roshan Singh, and Chandrashekhar Azad of the HRA. Kalpana Datta and Pritilata Waddedar (who led the Pahartali European Club attack) were key women revolutionaries in Masterda Surya Sen's 1930–32 Chittagong movement.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. 1925 కాకోరి రైలు సంఘటనను రామ్ ప్రసాద్ బిస్మిల్, అష్ఫాకుల్లా ఖాన్ తదితరులు నిర్వహించగా; కల్పనా దత్తా మరియు ప్రీతిలతా వాడేదార్లు 1930 చిట్టగాంగ్ సూర్య సేన్ విప్లవ దళంలో కీలక పాత్ర పోషించారు."
    ),
    # H10 (corr=1: 3-1-4-2 -> Aug 1940 Offer / Oct 1940 Ind Sat (1 -> wait check order!) Wait: 1. Ind Sat Oct 1940, 2. RIN Feb 1946, 3. August Offer Aug 1940? Wait let's make strict chronology: 1. August Offer (Aug 1940), 2. Individual Satyagraha (Oct 1940), 3. Cripps Mission (Mar 1942), 4. RIN Mutiny (Feb 1946) -> or permute list!)
    make_q(
        "Freedom Struggle (1940–1946) - Constitutional Proposals & Uprisings Chronology",
        "Arrange the following decisive events of the late Indian National Movement (1940–1946) in strict chronological sequence:\n1. Launching of the Individual Satyagraha at Paunar Ashram with Acharya Vinoba Bhave as the first Satyagrahi\n2. Viscount Linlithgow's 'August Offer' proposing expansion of the Viceroy's Executive Council and a post-war constituent body\n3. Royal Indian Navy (RIN) Ratings' Mutiny erupting aboard HMIS *Talwar* in Bombay\n4. Arrival of the Cripps Mission offering 'Dominion Status' with an option for provinces to secede\nSelect the correct chronological sequence:",
        "భారత స్వాతంత్ర్యోద్యమ తుది దశలోని (1940–1946) క్రింది కీలక సంఘటనలను సరైన కాలక్రమంలో అమర్చండి:\n1. ఆచార్య వినోబా భావే తొలి సత్యాగ్రహిగా పౌనార్ ఆశ్రమంలో వ్యక్తిగత సత్యాగ్రహం ప్రారంభమవడం\n2. యుద్ధానంతర రాజ్యాంగ సభ మరియు వైస్రాయ్ కార్యనిర్వాహక మండలి విస్తరణను ప్రతిపాదిస్తూ లార్డ్ లిన్లిత్‌గో 'ఆగస్టు ఆఫర్' ప్రకటించడం\n3. బొంబాయిలోని హెచ్‌ఎంఐఎస్ తల్వార్ (HMIS Talwar) నౌకలో రాయల్ ఇండియన్ నేవీ (RIN) నావికుల తిరుగుబాటు చెలరేగడం\n4. ప్రావిన్సులు విడిపోయే అవకాశంతో డొమినియన్ హోదా ప్రతిపాదిస్తూ 'క్రిప్స్ మిషన్' భారతదేశానికి రావడం\nసరైన కాలక్రమాన్ని ఎంచుకోండి:",
        ["2 - 4 - 1 - 3", "2 - 1 - 4 - 3", "1 - 2 - 4 - 3", "2 - 1 - 3 - 4"],
        ["2 - 4 - 1 - 3", "2 - 1 - 4 - 3", "1 - 2 - 4 - 3", "2 - 1 - 3 - 4"],
        1,
        "Strict chronological order: (2) August Offer (August 8, 1940) -> (1) Individual Satyagraha (October 17, 1940, Vinoba Bhave 1st, Jawaharlal Nehru 2nd, Brahma Datt 3rd) -> (4) Cripps Mission (March 1942) -> (3) Royal Indian Navy Mutiny aboard HMIS Talwar (February 18, 1946).",
        "సరైన కాలక్రమం: (2) ఆగస్టు ఆఫర్ (ఆగస్టు 1940) -> (1) వ్యక్తిగత సత్యాగ్రహం (అక్టోబర్ 1940) -> (4) క్రిప్స్ మిషన్ (మార్చి 1942) -> (3) ఆర్‌ఐఎన్ నావికుల తిరుగుబాటు (ఫిబ్రవరి 1946)."
    ),
]


def get_part1_gs():
    fcb = _load_fcb_by_id()
    polity = [_wrap_fcb(fcb[fid]) for fid in (95, 122, 136, 141, 142)] + NEW_POLITY
    telangana = [_wrap_fcb(fcb[fid]) for fid in (63, 94, 130, 135, 137, 140, 145)] + NEW_TELANGANA
    history = [_wrap_fcb(fcb[fid]) for fid in (124, 133, 134, 144)] + NEW_HISTORY
    assert len(polity) == 16
    assert len(telangana) == 20
    assert len(history) == 14
    return polity + telangana + history


# ==================== 4. GEOGRAPHY & ENVIRONMENT NEW (14) ====================
# Balance target: {0: 3, 1: 3, 2: 4, 3: 4}
NEW_GEOGRAPHY = [
    # G1 (corr=0: 1 and 2 only; stmt 3 false: claims Karewas are arid wind-blown loess deposits of Thar Desert instead of glacio-fluvial lacustrine deposits of Kashmir famous for saffron!)
    make_q(
        "Himalayan Geomorphology - Syntaxial Bends, Duns & Karewas",
        "Consider the following statements regarding the structural physiography of the Himalayan mountain system:\n1. The Himalayas exhibit two sharp tectonic syntaxial bends at their western extremity near Nanga Parbat and eastern extremity near Namcha Barwa.\n2. The longitudinal structural valleys lying between the Lesser Himalayas (Himachal) and the Outer Himalayas (Siwaliks), such as Dehra Dun and Patli Dun, are known as 'Duns' in the west and 'Duars' in the east.\n3. 'Karewas' are wind-eroded aeolian sand dunes of western Rajasthan extensively utilized for pearl millet cultivation.\nWhich of the statements given above are correct?",
        "హిమాలయ పర్వత శ్రేణుల భూస్వరూప విజ్ఞానానికి (Geomorphology) సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. హిమాలయాలు పశ్చిమ చివరన నంగా పర్బత్ వద్ద మరియు తూర్పు చివరన నామ్చా బర్వా వద్ద రెండు తీవ్రమైన వంపులను (Syntaxial Bends) కలిగి ఉంటాయి.\n2. లెస్సర్ హిమాలయాలు (హిమాచల్) మరియు శివాలిక్ పర్వతాల మధ్య గల దీర్ఘవృత్తాకార లోయలను పశ్చిమాన 'డూన్లు' (ఉదా: డెహ్రాడూన్) అని, తూర్పున 'ద్వారాలు' (Duars) అని పిలుస్తారు.\n3. 'కరేవాస్' (Karewas) అనేవి పశ్చిమ రాజస్థాన్‌లోని గాలి కోత వల్ల ఏర్పడిన ఇసుక తిన్నెలు, ఇవి సజ్జల సాగుకు ప్రసిద్ధి చెందాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is false. 'Karewas' are thick unconsolidated glacio-fluvial-lacustrine deposits (Pleistocene lake-bed clays, silts, and moraines) in the Kashmir Valley, famously cultivated for Zafran (saffron) at Pampore.",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. 'కరేవాస్' అనేవి కాశ్మీర్ లోయలో ప్రాచీన సరస్సు మరియు హిమానీనద నిక్షేపాలతో ఏర్పడిన సారవంతమైన భూములు; ఇవి కుంకుమపువ్వు (Saffron) సాగుకు ప్రసిద్ధి చెందాయి."
    ),
    # G2 (corr=1: 2 and 3 only; stmt 1 false: says positive IOD means western Indian Ocean is cooler than eastern IO and WEAKENS Indian monsoon!)
    make_q(
        "Climatology - Indian Ocean Dipole (IOD), MJO & Somali Jet",
        "Consider the following statements regarding global atmospheric-oceanic teleconnections influencing the Indian Southwest Monsoon:\n1. A 'Positive Indian Ocean Dipole (IOD)' occurs when the western Indian Ocean near Somalia is anomalously colder than the eastern Indian Ocean near Sumatra, severely suppressing Indian monsoon rainfall.\n2. The Madden-Julian Oscillation (MJO) is an eastward-moving tropical intra-seasonal disturbance of clouds and rainfall circling the globe every 30–60 days that modulates active and break phases of the monsoon.\n3. The Findlater (Somali) Cross-Equatorial Low-Level Jet steers moisture-laden southwest monsoon winds across the Arabian Sea toward the Indian peninsula.\nWhich of the statements given above are correct?",
        "భారత నైరుతి రుతుపవనాలను ప్రభావితం చేసే సముద్ర-వాతావరణ దృగ్విషయాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. సోమాలియా సమీప పశ్చిమ హిందూ మహాసముద్రం, సుమత్రా సమీప తూర్పు హిందూ మహాసముద్రం కంటే చల్లగా మారడాన్ని 'పాజిటివ్ IOD' అంటారు; ఇది భారత రుతుపవన వర్షపాతాన్ని తీవ్రంగా బలహీనపరుస్తుంది.\n2. మాడెన్-జూలియన్ ఆసిలేషన్ (MJO) అనేది ప్రతి 30–60 రోజులకు తూర్పు వైపు ప్రయాణించే ఉష్ణమండల మేఘాల ఆవర్తనం, ఇది రుతుపవనాల క్రియాశీల మరియు విరామ దశలను ప్రభావితం చేస్తుంది.\n3. ఫిండ్లేటర్ (సోమాలి) లో-లెవల్ జెట్ స్ట్రీమ్ అరేబియా సముద్రం మీదుగా తేమతో కూడిన నైరుతి రుతుపవన గాలులను భారత ద్వీపకల్పం వైపు నడిపిస్తుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is false. During a POSITIVE Indian Ocean Dipole (IOD), the western Indian Ocean becomes WARMER than the eastern Indian Ocean, driving enhanced convection toward the Indian subcontinent and offsetting even weak El Niño droughts.",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. పాజిటివ్ IOD సమయంలో పశ్చిమ హిందూ మహాసముద్రం తూర్పు హిందూ మహాసముద్రం కంటే ఎక్కువ వెచ్చగా ఉంటుంది, ఇది భారత నైరుతి రుతుపవనాలకు అనుకూలంగా ఉంటుంది."
    ),
    # G3 (corr=2: 1 and 3 only; stmt 2 false: says Tungabhadra is a left-bank tributary of Krishna and Bhima is right-bank -> backwards! Bhima is left-bank, Tungabhadra is right-bank!)
    make_q(
        "Peninsular Drainage - Godavari & Krishna Tributary Banks",
        "Consider the following statements regarding the tributary geometry of the Godavari and Krishna river basins:\n1. Pranhita, Indravati, and Sabari join the Godavari River from its left bank, whereas Manjeera and Manair join from its right bank.\n2. In the Krishna basin, Bhima joins as a right-bank tributary in Karnataka, whereas Tungabhadra joins as a left-bank tributary near Sangameswaram.\n3. Both the Godavari (Trimbakeshwar, Nashik) and Krishna (Mahabaleshwar, Satara) originate in the Western Ghats of Maharashtra and form fertile east-coast deltas along the Bay of Bengal.\nWhich of the statements given above are correct?",
        "గోదావరి మరియు కృష్ణా నదుల ఉపనదుల దిశలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ప్రాణహిత, ఇంద్రావతి మరియు శబరి నదులు గోదావరిలో ఎడమ గట్టు ఉపనదులుగా కలవగా, మంజీరా మరియు మానేరు కుడి గట్టు ఉపనదులుగా కలుస్తాయి.\n2. కృష్ణా నదీ పరీవాహకంలో భీమా నది కుడి గట్టు ఉపనదిగా, తుంగభద్ర నది ఎడమ గట్టు ఉపనదిగా సంగమేశ్వరం వద్ద కలుస్తాయి.\n3. గోదావరి (త్ర్యంబకేశ్వరం, నాసిక్) మరియు కృష్ణా (మహాబలేశ్వరం, సాతారా) నదులు రెండూ మహారాష్ట్రలోని పశ్చిమ కనుమలలో జన్మించి బంగాళాఖాతం తీరంలో సారవంతమైన డెల్టాలను ఏర్పరుస్తాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is reversed. Flowing eastward/southeastward, Bhima, Musi, and Munneru join the Krishna from its LEFT bank, whereas Koyna, Ghataprabha, Malaprabha, and Tungabhadra join from its RIGHT bank.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. తూర్పుగా ప్రవహించే కృష్ణా నదికి భీమా, మూసీ, మున్నేరులు ఎడమ గట్టు ఉపనదులు కాగా; కోయినా, ఘటప్రభ, మలప్రభ మరియు తుంగభద్రలు కుడి గట్టు ఉపనదులు."
    ),
    # G4 (corr=3: 1, 2, and 3 — Telangana Agro-Climatic Zones & Major Irrigation)
    make_q(
        "Telangana Geography - Agro-Climatic Zones & Lift Irrigation",
        "Consider the following statements regarding Telangana's agro-climatic regionalization and multi-purpose irrigation projects:\n1. Based on rainfall, soils, and cropping regimes, Telangana is classified into three Agro-Climatic Zones: Northern Telangana Zone (Jagtial HQ), Central Telangana Zone (Warangal HQ), and Southern Telangana Zone (Palem, Nagarkurnool HQ).\n2. The Sita Rama Lift Irrigation Project (SRLIP), integrating the Dummugudem anicut on the Godavari River, is engineered to divert Godavari waters to irrigate lands in Bhadradri Kothagudem and Khammam districts.\n3. The J. Chokka Rao Devadula Lift Irrigation Scheme draws water from the Godavari River near Gangaram (Mulugu district) across elevated upland stages of the erstwhile Warangal plateau.\nWhich of the statements given above are correct?",
        "తెలంగాణ వ్యవసాయ-వాతావరణ మండలాలు మరియు ఎత్తిపోతల ప్రాజెక్టులకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. వర్షపాతం, నేలలు మరియు పంటల సరళి ఆధారంగా తెలంగాణను మూడు వ్యవసాయ-వాతావరణ జోన్లుగా విభజించారు: ఉత్తర తెలంగాణ జోన్ (జగిత్యాల), మధ్య తెలంగాణ జోన్ (వరంగల్) మరియు దక్షిణ తెలంగాణ జోన్ (పాలెం, నాగర్‌కర్నూల్).\n2. గోదావరి నదిపై గల దుమ్ముగూడెం ఆనకట్ట ద్వారా నీటిని మళ్లించి భద్రాద్రి కొత్తగూడెం మరియు ఖమ్మం జిల్లాలకు సాగునీరందించేందుకు సీతారామ ఎత్తిపోతల పథకం (SRLIP) రూపొందించబడింది.\n3. జె. చొక్కారావు దేవాదుల ఎత్తిపోతల పథకం ములుగు జిల్లా గంగారం సమీపంలో గోదావరి నది నుండి నీటిని తీసుకుని ఉమ్మడి వరంగల్ ఎత్తైన ప్రాంతాలకు సాగునీరందిస్తుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. Telangana's three agricultural research stations at Polasa (Jagtial), Warangal, and Palem anchor its three Agro-Climatic Zones, while SRLIP and Devadula lift Godavari waters onto the eastern and central Telangana uplands.",
        "మూడు ప్రకటనలూ సరైనవే. జగిత్యాల (పొలాస), వరంగల్, పాలెం కేంద్రాలుగా రాష్ట్రంలో మూడు వ్యవసాయ-వాతావరణ మండలాలు ఉన్నాయి; అలాగే సీతారామ మరియు దేవాదుల ప్రాజెక్టులు గోదావరి జలాలను ఎత్తిపోతల ద్వారా అందిస్తున్నాయి."
    ),
    # G5 (corr=0: A-3, B-1, C-4, D-2 — Drainage Patterns match)
    make_q(
        "Fluvial Geomorphology - Drainage Patterns Match",
        "Match the drainage patterns (List-I) with their defining geological structure and Indian river examples (List-II):\nList-I:\nA. Dendritic Pattern\nB. Radial Pattern\nC. Trellis Pattern\nD. Centripetal Pattern\nList-II:\n1. Streams diverge outward in all directions from a central elevated dome/highland (e.g., rivers of the Amarkantak Plateau)\n2. Streams discharge inward from surrounding slopes into a central closed depression or basin (e.g., Loktak Lake basin / Sambhar basin)\n3. Tree-branch-like irregular network over horizontally uniform, homogeneous rock strata (e.g., Northern Indo-Gangetic Plains)\n4. Primary streams flow parallel through folded alternating bands of hard & soft rock, joined at right angles by short tributaries\nSelect the correct code:",
        "నదీ ప్రవాహ నమూనాలను (జాబితా-I) అవి ఏర్పడే భూగర్భ నిర్మాణాలు మరియు భారత ఉదాహరణలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. వృక్షాకార ప్రవాహ నమూనా (Dendritic)\nB. వ్యాసార్ధ ప్రవాహ నమూనా (Radial)\nC. ట్రెల్లిస్ ప్రవాహ నమూనా (Trellis)\nD. కేంద్రాభిముఖ ప్రవాహ నమూనా (Centripetal)\nజాబితా-II:\n1. ఒక ఎత్తైన కొండ లేదా శిఖరం నుండి అన్ని దిశలలోకి వెలుపలికి ప్రవహించే నదులు (ఉదా: అమర్‌కంటక్ పీఠభూమి)\n2. చుట్టుపక్కల ఎత్తైన ప్రాంతాల నుండి మధ్యలో ఉన్న లోతట్టు ప్రాంతం లేదా సరస్సులోకి ప్రవహించడం (ఉదా: లోక్‌తక్, సాంబార్)\n3. సమతలమైన ఏకరీతి శిలా పొరలపై చెట్టు కొమ్మల వలె విస్తరించే నదులు (ఉదా: గంగా-సింధు మైదానాలు)\n4. గట్టి మరియు మృదువైన మడత శిలా పొరల గుండా సమాంతరంగా ప్రవహిస్తూ లంబకోణంలో కలిసే ఉపనదులు\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-4, B-1, C-3, D-2"],
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-4, B-1, C-3, D-2"],
        0,
        "Dendritic resembles tree branches over uniform strata (A-3). Radial radiates out from a dome like Amarkantak (Narmada, Son) (B-1). Trellis joins main valleys at right angles in folded belts like the Appalachians or folded Himalayan/Vindhyan belts (C-4). Centripetal drains inward into central lakes/playas (D-2).",
        "వృక్షాకార నమూనా ఏకరీతి మైదానాల్లో (3), వ్యాసార్ధ నమూనా అమర్‌కంటక్ పీఠభూమిలో (1), ట్రెల్లిస్ మడత శిలా ప్రాంతాల్లో లంబకోణ సంగమంతో (4), మరియు కేంద్రాభిముఖ నమూనా లోతట్టు సరస్సులలో (2) కనిపిస్తాయి."
    ),
    # G6 (corr=2: 1 and 3 only; stmt 2 false: claims Khadar is older alluvium rich in Kankar nodules above flood level, whereas Bhangar is older with Kankar and Khadar is newer flood-deposited silt!)
    make_q(
        "Soil Geography - Pedogenesis of Laterite & Alluvial Soils",
        "Consider the following statements regarding the pedogenesis and chemical properties of Indian soils:\n1. Laterite soils form under intense tropical seasonal rainfall and alternating dry spells through 'desilication'—a process that leaches away lime and silica while leaving soils rich in iron oxide and aluminium compounds.\n2. In the Indo-Gangetic Plains, 'Khadar' represents older alluvium perched above floodplains containing calcareous 'Kankar' nodules, whereas 'Bhangar' denotes fertile newer floodplains renewed annually.\n3. Saline and alkaline soils ('Usara' / 'Reh' / 'Kallar') often develop in arid climates or waterlogged canal-irrigated belts due to capillary rise of dissolved sodium, calcium, and magnesium salts, remediable by gypsum application.\nWhich of the statements given above are correct?",
        "భారతదేశంలోని మృత్తికల పుట్టుక (Pedogenesis) మరియు రసాయన ధర్మాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఉష్ణమండల భారీ వర్షపాతం, పొడి వాతావరణం మధ్య లాటరైట్ నేలలు 'డీసిలికేషన్' (లవణాలు, సిలికా కొట్టుకుపోవడం) ద్వారా ఏర్పడి ఐరన్ ఆక్సైడ్ మరియు అల్యూమినియం సమ్మేళనాలతో సమృద్ధిగా ఉంటాయి.\n2. గంగా-సింధు మైదానాలలో 'ఖాదర్' అనేది వరద మట్టానికి పైన ఉండే కాల్షియం కార్బొనేట్ (కంకర్) కణుపులతో కూడిన పాత ఒండ్రు నేల కాగా, 'భంగర్' అనేది ప్రతి ఏటా నూతనంగా నిక్షేపించబడే సారవంతమైన వరద మైదానం.\n3. పొడి వాతావరణంలో లేదా అధిక నీటిపారుదల వల్ల చౌడుగా మారే నేలలు ('ఉసర', 'రేహ్', 'కల్లార్') సోడియం, మెగ్నీషియం లవణాల వల్ల ఏర్పడతాయి; వీటిని జిప్సం (Gypsum) కలపడం ద్వారా పునరుద్ధరించవచ్చు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is reversed. 'Bhangar' is the OLDER alluvium above floodplain terraces rich in calcareous *kankar* deposits, whereas 'Khadar' is the NEWER, finer, annually replenished river floodplain silt.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తారుమారైంది. కంకర్ కణుపులతో ఉండే పాత ఒండ్రు నేలను 'భంగర్' అంటారు; ప్రతి సంవత్సరం వరదలతో కొత్తగా నిక్షేపించబడే సారవంతమైన ఒండ్రు నేలను 'ఖాదర్' అంటారు."
    ),
    # G7 (corr=1: 2 and 3 only; stmt 1 false: claims Tropical Wet Evergreen forests shed ALL leaves simultaneously in summer like Deciduous!)
    make_q(
        "Biogeography - Forest Types & Vegetation Zones of India",
        "Consider the following statements regarding the natural vegetation types of India:\n1. Tropical Wet Evergreen Forests (receiving >200 cm annual rainfall along the Western Ghats windward slopes and North-East hills) shed all their leaves simultaneously for 6–8 weeks during peak summer to conserve moisture.\n2. Tropical Dry Deciduous Forests (receiving 70–100 cm rainfall), characterized by Teak, Tendu, Palas, and Axlewood across large stretches of Peninsular plateaus including Telangana, transition into thorny scrub at drier margins.\n3. In the higher reaches of the Nilgiris, Anaimalai, and Palani Hills, patches of stunted subtropical-temperate montane forests interspersed with rolling grasslands are regionally called 'Sholas'.\nWhich of the statements given above are correct?",
        "భారతదేశంలోని సహజ వృక్షసంపద రకాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. పశ్చిమ కనుమల గాలి తగిలే వాలులలో, ఈశాన్య కొండలలో (>200 సెం.మీ వర్షపాతం) పెరిగే ఉష్ణమండల సతతహరిత అడవులు వేసవిలో తేమను కాపాడుకోవడానికి 6–8 వారాల పాటు ఒకేసారి పూర్తిగా ఆకులను రాలుస్తాయి.\n2. 70–100 సెం.మీ వర్షపాతం గల ఉష్ణమండల శుష్క ఆకురాల్చే అడవులు (టేకు, తునికి/తెందు, మోదుగ వంటివి) తెలంగాణతో సహా ద్వీపకల్ప పీఠభూమిలో విస్తరించి, తక్కువ వర్షపాతం వైపు ముళ్లపొదలుగా మారతాయి.\n3. నీలగిరి, అన్నామలై, పళని కొండల ఎత్తైన ప్రాంతాల్లో గడ్డి మైదానాలతో కలిసి ఉండే సమశీతోష్ణ పర్వత అడవులను స్థానికంగా 'షోలాలు' (Sholas) అని పిలుస్తారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is wrong. Tropical Wet Evergreen Forests have NO fixed simultaneous season for leaf-shedding, flowering, or fruiting—trees shed leaves asynchronously, keeping the multi-tiered canopy green year-round. It is Tropical Deciduous Forests that shed leaves synchronously in dry summer.",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. సతతహరిత అడవులలో చెట్లు ఒకేసారి ఆకులను రాల్చవు (సంవత్సరమంతా పచ్చగా ఉంటాయి); వేసవిలో పూర్తిగా ఆకులు రాల్చేవి ఆకురాల్చే అడవులు (Deciduous Forests)."
    ),
    # G8 (corr=3: 1, 2, and 3 — Telangana Mineral Resources)
    make_q(
        "Economic Geography - Mineral Belt & Energy Resources of Telangana",
        "Consider the following statements regarding the mineral distribution of Telangana State:\n1. Coal seams mined by Singareni Collieries Company Limited (SCCL) belong to the Lower Gondwana formations distributed along the Pranhita-Godavari Valley rift basin across Mancherial, Peddapalli, Bhupalpally, and Bhadradri Kothagudem districts.\n2. Significant radioactive uranium mineralization deposits have been explored by the Atomic Minerals Directorate in the Lambapur-Peddagattu region of Nalgonda district.\n3. Cement-grade limestone belts are extensively concentrated across the Bhima and Palnad sedimentary formations of Vikarabad (Tandur), Nalgonda, and Suryapet districts, while iron ore reserves occur at Bayyaram (Mahabubabad).\nWhich of the statements given above are correct?",
        "తెలంగాణ రాష్ట్రంలోని ఖనిజ వనరుల విస్తరణకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. సింగరేణి కాలరీస్ కంపెనీ లిమిటెడ్ (SCCL) తవ్వకాలు జరిపే బొగ్గు నిక్షేపాలు మంచిర్యాల, పెద్దపల్లి, భూపాలపల్లి మరియు భద్రాద్రి కొత్తగూడెం జిల్లాల్లోని ప్రాణహిత-గోదావరి లోయ దిగువ గోండ్వానా శిలల్లో విస్తరించి ఉన్నాయి.\n2. నల్గొండ జిల్లాలోని లంబాపూర్-పెద్దగట్టు ప్రాంతంలో అటామిక్ మినరల్స్ డైరెక్టరేట్ గణనీయమైన యురేనియం నిక్షేపాలను గుర్తించింది.\n3. వికారాబాద్ (తాండూరు), నల్గొండ మరియు సూర్యాపేట జిల్లాల్లో విస్తారమైన సున్నపురాయి (Limestone) నిల్వలు ఉండగా, మహబూబాబాద్ జిల్లా బయ్యారంలో ఇనుప ఖనిజ నిల్వలు ఉన్నాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. Telangana possesses over 20% of India's Gondwana bituminous coal reserves in the Pranhita-Godavari graben, limestone across Vikarabad/Nalgonda/Suryapet, uranium exploration at Lambapur-Peddagattu, and iron ore reserves at Bayyaram.",
        "మూడు ప్రకటనలూ సరైనవే. ప్రాణహిత-గోదావరి లోయలో సింగరేణి గోండ్వానా బొగ్గు నిల్వలు, నల్గొండ జిల్లా లంబాపూర్-పెద్దగట్టు వద్ద యురేనియం, తాండూరు/నల్గొండ/సూర్యాపేటలో సున్నపురాయి మరియు మహబూబాబాద్ జిల్లా బయ్యారంలో ఇనుప ఖనిజం విస్తరించి ఉన్నాయి."
    ),
    # G9 (corr=2: A-4, B-2, C-1, D-3 — Telangana Wildlife Sanctuaries & Tiger Reserves match)
    make_q(
        "Telangana Ecology - Protected Areas & Tiger Reserves Match",
        "Match the prominent Tiger Reserves and Wildlife Sanctuaries of Telangana (List-I) with their primary district locations (List-II):\nList-I:\nA. Kawal Tiger Reserve\nB. Amrabad Tiger Reserve\nC. Kinnerasani Wildlife Sanctuary\nD. Pocharam Wildlife Sanctuary\nList-II:\n1. Bhadradri Kothagudem district\n2. Nagarkurnool and Nalgonda districts (Nallamala hills)\n3. Medak and Kamareddy districts\n4. Mancherial, Adilabad, Nirmal, and Komaram Bheem Asifabad districts\nSelect the correct code:",
        "తెలంగాణలోని ప్రముఖ టైగర్ రిజర్వ్‌లు మరియు వన్యప్రాణి అభయారణ్యాలను (జాబితా-I) వాటి జిల్లాలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. కవ్వాల్ టైగర్ రిజర్వ్\nB. అమ్రాబాద్ టైగర్ రిజర్వ్\nC. కిన్నెరసాని వన్యప్రాణి అభయారణ్యం\nD. పోచారం వన్యప్రాణి అభయారణ్యం\nజాబితా-II:\n1. భద్రాద్రి కొత్తగూడెం జిల్లా\n2. నాగర్‌కర్నూల్ మరియు నల్గొండ జిల్లాలు (నల్లమల అడవులు)\n3. మెదక్ మరియు కామారెడ్డి జిల్లాలు\n4. మంచిర్యాల, ఆదిలాబాద్, నిర్మల్ మరియు కొమరం భీమ్ ఆసిఫాబాద్ జిల్లాలు\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-4, B-1, C-2, D-3", "A-2, B-4, C-1, D-3", "A-4, B-2, C-1, D-3", "A-4, B-2, C-3, D-1"],
        ["A-4, B-1, C-2, D-3", "A-2, B-4, C-1, D-3", "A-4, B-2, C-1, D-3", "A-4, B-2, C-3, D-1"],
        2,
        "Kawal Tiger Reserve (Jannaram corridor) covers Mancherial and neighbouring northern Sahyadri belt districts (A-4). Amrabad Tiger Reserve spans the Nallamala hills in Nagarkurnool and Nalgonda (B-2). Kinnerasani Sanctuary lies in Bhadradri Kothagudem (C-1). Pocharam Sanctuary sits along the border of Medak and Kamareddy districts (D-3).",
        "కవ్వాల్ టైగర్ రిజర్వ్ - మంచిర్యాల/ఆదిలాబాద్ ప్రాంతం (4); అమ్రాబాద్ - నాగర్‌కర్నూల్/నల్గొండ (2); కిన్నెరసాని - భద్రాద్రి కొత్తగూడెం (1); పోచారం - మెదక్/కామారెడ్డి (3)."
    ),
    # G10 (corr=0: A-3, B-1, C-4, D-2 — International Environmental Conventions match)
    make_q(
        "Environmental Governance - Multilateral Conventions Match",
        "Match the global environmental treaties (List-I) with their specific regulatory mandate (List-II):\nList-I:\nA. Basel Convention (1989)\nB. Rotterdam Convention (1998)\nC. Stockholm Convention (2001)\nD. Minamata Convention (2013)\nList-II:\n1. Prior Informed Consent (PIC) procedure for international trade of certain hazardous industrial chemicals and pesticides\n2. Protecting human health and the environment from anthropogenic emissions and releases of Mercury and mercury compounds\n3. Control of transboundary movements of hazardous wastes and preventing dumping in developing nations\n4. Elimination or restriction of Persistent Organic Pollutants (POPs - 'Dirty Dozen') that bioaccumulate across food webs\nSelect the correct code:",
        "అంతర్జాతీయ పర్యావరణ ఒప్పందాలను (జాబితా-I) వాటి ప్రధాన నియంత్రణ అంశాలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. బాసెల్ ఒప్పందం (1989)\nB. రోటర్‌డ్యామ్ ఒప్పందం (1998)\nC. స్టాక్‌హోమ్ ఒప్పందం (2001)\nD. మినిమాటా ఒప్పందం (2013)\nజాబితా-II:\n1. కొన్ని ప్రమాదకర రసాయనాలు, పురుగుమందుల అంతర్జాతీయ వాణిజ్యంలో ముందస్తు సమాచార అనుమతి (PIC) విధానం\n2. మానవ ఆరోగ్యం, పర్యావరణంపై పాదరసం (Mercury) ఉద్గారాలు మరియు కాలుష్యాన్ని నియంత్రించడం\n3. ప్రమాదకర వ్యర్థాల సరిహద్దు రవాణాను నియంత్రించడం మరియు వర్ధమాన దేశాల్లో పారవేయకుండా అడ్డుకోవడం\n4. ఆహారపు గొలుసులో పేరుకుపోయే స్థిరమైన సేంద్రియ కాలుష్య కారకాలను (POPs) నిషేధించడం లేదా తగ్గించడం\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-3, B-1, C-2, D-4"],
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-3, B-1, C-2, D-4"],
        0,
        "Basel Convention (1989) governs transboundary movement of hazardous wastes (A-3). Rotterdam Convention (1998) implements Prior Informed Consent for hazardous chemicals/pesticides (B-1). Stockholm Convention (2001) targets Persistent Organic Pollutants (POPs) (C-4). Minamata Convention (2013) combats global mercury pollution (D-2).",
        "బాసెల్ - ప్రమాదకర వ్యర్థాల రవాణా (3); రోటర్‌డ్యామ్ - రసాయనాల ముందస్తు అనుమతి PIC (1); స్టాక్‌హోమ్ - POPs (4); మినిమాటా - పాదరసం నియంత్రణ (2)."
    ),
    # G11 (corr=3: 1, 2, and 3 — Tropical Cyclones mechanics & North Indian Ocean asymmetry)
    make_q(
        "Atmospheric Science - Tropical Cyclogenesis & Bay of Bengal Asymmetry",
        "Consider the following statements regarding tropical cyclones in the North Indian Ocean:\n1. Tropical cyclones rarely originate within 0 degrees to 5 degrees latitude of the Equator because the Coriolis force near the Equator is virtually zero, preventing cyclonic spin around low-pressure centres.\n2. The Bay of Bengal records substantially more severe tropical cyclones than the Arabian Sea due to higher sea-surface temperatures, sluggish vertical wind shear, and frequent inflow of Pacific typhoon remnants.\n3. Naming of tropical cyclones in the North Indian Ocean is managed by the WMO/ESCAP Panel on Tropical Cyclones comprising 13 member states, with India Meteorological Department (IMD) serving as the Regional Specialized Meteorological Centre (RSMC).\nWhich of the statements given above are correct?",
        "ఉత్తర హిందూ మహాసముద్రంలో తుఫానుల ఆవిర్భావానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. భూమధ్యరేఖకు 0 నుండి 5 డిగ్రీల అక్షాంశాల మధ్య కోరియోలిస్ బలం (Coriolis Force) దాదాపు శూన్యంగా ఉండటం వల్ల తుఫానులు అక్కడ అరుదుగా మాత్రమే ఏర్పడతాయి.\n2. అరేబియా సముద్రంతో పోలిస్తే బంగాళాఖాతంలో అధిక ఉపరితల ఉష్ణోగ్రతలు, పసిఫిక్ టైఫూన్ల అవశేషాల ప్రవేశం వల్ల తుఫానులు ఎక్కువగా సంభవిస్తాయి.\n3. ఉత్తర హిందూ మహాసముద్ర తుఫానులకు నామకరణం చేసే ప్రక్రియను 13 సభ్య దేశాల WMO/ESCAP ప్యానెల్ నిర్వహిస్తుండగా, భారత వాతావరణ శాఖ (IMD) ప్రాంతీయ ప్రత్యేక కేంద్రంగా (RSMC) వ్యవహరిస్తుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. Near-zero equatorial Coriolis force prevents storm vortex spin-up within 5 deg N/S; the Bay of Bengal averages roughly 4 times more cyclones than the Arabian Sea (though Arabian Sea intensity has risen recently with warming); and IMD New Delhi acts as RSMC for the 13-nation panel.",
        "మూడు ప్రకటనలూ సరైనవే. భూమధ్యరేఖ వద్ద కోరియోలిస్ బలం లేకపోవడం వల్ల 0–5 డిగ్రీల మధ్య తుఫానులు ఏర్పడవు; బంగాళాఖాతంలో అరేబియా సముద్రం కంటే ఎక్కువ తుఫానులు వస్తాయి; 13 దేశాల ప్యానెల్‌కు IMD సమన్వయ కేంద్రంగా పనిచేస్తుంది."
    ),
    # G12 (corr=2: 1 and 3 only; stmt 2 false: claims Sundarbans West Bengal holds major stony coral reef atolls instead of Lakshadweep!)
    make_q(
        "Marine Ecosystems - Coral Bleaching & Indian Reef Systems",
        "Consider the following statements regarding coral reef ecology and marine conservation in India:\n1. Coral bleaching occurs when elevated sea temperatures or ocean acidification cause reef-building corals to expel their symbiotic photosynthetic microalgae (*zooxanthellae*), exposing the white calcium carbonate skeleton.\n2. In India, Lakshadweep features river-mouth muddy estuarine reefs formed by brackish Brahmaputra silt, whereas the Sundarbans Biosphere Reserve consists purely of deep-ocean volcanic coral atolls.\n3. Rising atmospheric CO2 dissolves in seawater to form carbonic acid, lowering ocean pH and reducing carbonate ion availability required for aragonite skeleton calcification.\nWhich of the statements given above are correct?",
        "పగడపు దిబ్బల పర్యావరణ వ్యవస్థ మరియు భారతదేశంలోని సముద్ర జీవావరణాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. సముద్ర ఉష్ణోగ్రతలు పెరగడం లేదా సముద్ర ఆమ్లీకరణం వల్ల పగడాలు తమతో సహజీవనం చేసే 'జూక్సాంథెల్లే' (Zooxanthellae) శైవలాలను బయటకు పంపడాన్ని 'కోరల్ బ్లీచింగ్' అంటారు.\n2. భారతదేశంలో లక్షద్వీప్ దీవులు బ్రహ్మపుత్ర నదీ ఒండ్రు మట్టితో ఏర్పడిన బురద దిబ్బలను కలిగి ఉండగా, సుందర్‌బన్స్ జీవావరణ రిజర్వ్ పూర్తిగా అగాధ సముద్రపు 'అటాల్' పగడపు దిబ్బలతో నిండి ఉంటుంది.\n3. వాతావరణంలోని పెరిగిన CO2 సముద్ర జలాల్లో కరిగి కార్బోనిక్ ఆమ్లంగా మారి నీటి pH ని తగ్గించడం ద్వారా పగడాల కాల్షియం కార్బొనేట్ (అరగోనైట్) నిర్మాణానికి ఆటంకం కలిగిస్తుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is factually inverted and wrong. Lakshadweep consists exclusively of oceanic coral ATOLLS, whereas the Sundarbans (Ganga-Brahmaputra delta) is the world's largest estuarine MANGROVE forest (not coral reefs due to high freshwater silt turbidity). India's four major coral reef zones are Lakshadweep, Andaman & Nicobar, Gulf of Mannar, and Gulf of Kachchh.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. లక్షద్వీప్ సముద్రపు అటాల్ పగడపు దీవులతో ఏర్పడగా, సుందర్‌బన్స్ ప్రపంచంలోనే అతిపెద్ద మడ అడవుల (Mangroves) ప్రాంతం (ఇక్కడ నదీ ఒండ్రు మట్టి వల్ల పగడపు దిబ్బలు పెరగవు)."
    ),
    # G13 (corr=1: 2 and 3 only; stmt 1 false: says CACP finalizes & implements MSP independently without CCEA approval, AND says MSP legally covers Sugarcane while Fair & Remunerative Price applies to Rice!)
    make_q(
        "Agricultural Economics & Geography - MSP, FRP & CACP Architecture",
        "Consider the following statements regarding Minimum Support Price (MSP) and India's agricultural pricing framework:\n1. The Commission for Agricultural Costs and Prices (CACP) holds final binding constitutional authority to approve MSP across all crops, and fixes MSP directly for Sugarcane rather than Fair and Remunerative Price (FRP).\n2. The Government of India declares MSP for 22 mandated agricultural crops (covering 14 Kharif crops, 6 Rabi crops, and 2 commercial crops like Jute and Copra) plus FRP for Sugarcane.\n3. Final approval of MSP rates rests with the Cabinet Committee on Economic Affairs (CCEA) chaired by the Prime Minister, considering cost concepts A2, A2+FL, and C2 computed by CACP.\nWhich of the statements given above are correct?",
        "కనీస మద్దతు ధర (MSP) మరియు భారత వ్యవసాయ ధరల వ్యవస్థకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. వ్యవసాయ ఖర్చులు మరియు ధరల కమిషన్ (CACP) అన్ని పంటలకు తుది ఆమోద అధికారాన్ని కలిగి ఉంటుంది మరియు చెరకుకు FRP కు బదులుగా నేరుగా MSP ని నిర్ణయిస్తుంది.\n2. భారత ప్రభుత్వం 22 నిర్దేశిత పంటలకు (14 ఖరీఫ్, 6 రబీ, మరియు జనుము, కొబ్బరి వంటి 2 వాణిజ్య పంటలు) కనీస మద్దతు ధరను, మరియు చెరకుకు న్యాయమైన, లాభదాయక ధర (FRP) ను ప్రకటిస్తుంది.\n3. CACP లెక్కించే A2, A2+FL మరియు C2 వ్యయ సూత్రాల ఆధారంగా MSP ధరలకు తుది ఆమోదం ప్రధానమంత్రి అధ్యక్షతన గల ఆర్థిక వ్యవహారాల కేబినెట్ కమిటీ (CCEA) ఇస్తుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is false. CACP is a purely advisory recommendatory body attached to the Ministry of Agriculture & Farmers Welfare; final approval rests with the Cabinet Committee on Economic Affairs (CCEA). Furthermore, Sugarcane is governed by statutory Fair and Remunerative Price (FRP), not MSP.",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. CACP కేవలం సిఫార్సులు మాత్రమే చేస్తుంది; తుది నిర్ణయం CCEA తీసుకుంటుంది. అలాగే చెరకు పంటకు MSP కాకుండా చట్టబద్ధమైన FRP (Fair & Remunerative Price) వర్తిస్తుంది."
    ),
    # G14 (corr=3: 1, 2, and 3 — NDMA Act 2005 Disaster Management Architecture)
    make_q(
        "Disaster Management - Statutory Institutional Architecture (DM Act, 2005)",
        "Consider the following statements regarding the statutory disaster management framework under the Disaster Management Act, 2005:\n1. The National Disaster Management Authority (NDMA) is chaired ex-officio by the Prime Minister of India and may include up to nine other nominated members.\n2. At the district level, the District Disaster Management Authority (DDMA) is chaired ex-officio by the District Collector/Magistrate, with the elected Chairperson of the Zilla Parishad serving as Co-Chairperson (except in tribal autonomous districts).\n3. The National Disaster Response Force (NDRF) operates under the general superintendence, direction, and control of the NDMA, drawing specialized deputation battalions from Central Armed Police Forces (CAPFs).\nWhich of the statements given above are correct?",
        "విపత్తు నిర్వహణ చట్టం, 2005 కింద గల సంస్థాగత నిర్మాణానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. జాతీయ విపత్తు నిర్వహణ సంస్థ (NDMA) కు ప్రధానమంత్రి ఎక్స్-అఫీషియో చైర్‌పర్సన్‌గా వ్యవహరిస్తారు; ఇందులో గరిష్టంగా 9 మంది ఇతర సభ్యులు ఉండవచ్చు.\n2. జిల్లా స్థాయిలో జిల్లా విపత్తు నిర్వహణ సంస్థ (DDMA) కు జిల్లా కలెక్టర్/మేజిస్ట్రేట్ చైర్‌పర్సన్‌గా, మరియు జిల్లా పరిషత్ చైర్‌పర్సన్ సహ-అధ్యక్షులుగా (Co-Chairperson) వ్యవహరిస్తారు.\n3. జాతీయ విపత్తు ప్రతిస్పందన దళం (NDRF) NDMA సాధారణ పర్యవేక్షణ మరియు నియంత్రణలో పనిచేస్తూ కేంద్ర సాయుధ పోలీసు బలగాల (CAPFs) నుండి ప్రత్యేక బెటాలియన్లను తీసుకుంటుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct under Sections 3, 25, and 44 of the Disaster Management Act, 2005 (enacted in December 2005 following the 2004 Indian Ocean Tsunami).",
        "మూడు ప్రకటనలూ సరైనవే. విపత్తు నిర్వహణ చట్టం 2005 ప్రకారం NDMA కు ప్రధాని, SDMA కు ముఖ్యమంత్రి, DDMA కు కలెక్టర్ & జడ్పీ చైర్‌పర్సన్ సారథ్యం వహిస్తారు; NDRF, NDMA నియంత్రణలో పనిచేస్తుంది."
    ),
]

# ==================== 5. ECONOMY NEW (10) ====================
# Balance target: {0: 3, 1: 3, 2: 2, 3: 2}
NEW_ECONOMY = [
    # E1 (corr=0: 1 and 2 only; stmt 3 false: claims SDF requires govt security collateral from commercial banks -> SDF is specifically COLLATERAL-FREE absorption tool!)
    make_q(
        "Monetary Policy - LAF Corridor, SDF & MSF Instruments",
        "Consider the following statements regarding the Reserve Bank of India's Liquidity Adjustment Facility (LAF) operational corridor:\n1. Introduced in April 2022 as the floor of the LAF corridor, the Standing Deposit Facility (SDF) permits scheduled commercial banks to park overnight surplus liquidity with the RBI without receiving government security collateral.\n2. The Marginal Standing Facility (MSF) serves as the upper ceiling of the LAF corridor, allowing banks to borrow overnight emergency funds from the RBI against SLR securities up to a prescribed limit at a penal rate above the Repo Rate.\n3. Under the SDF mechanism, the RBI is legally obligated to hand over Central Government securities as 100% collateral for every rupee deposited by banks.\nWhich of the statements given above are correct?",
        "భారతీయ రిజర్వ్ బ్యాంక్ (RBI) ద్రవ్య లభ్యత సర్దుబాటు సౌకర్యం (LAF) కారిడార్ సాధనాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఏప్రిల్ 2022లో LAF కారిడార్ దిగువ పరిమితిగా (Floor) ప్రవేశపెట్టబడిన 'స్టాండింగ్ డిపాజిట్ ఫెసిలిటీ' (SDF) ద్వారా వాణిజ్య బ్యాంకులు ఎటువంటి ప్రభుత్వ సెక్యూరిటీల హామీ లేకుండానే ఆర్‌బీఐ వద్ద మిగులు నిధులను ఉంచవచ్చు.\n2. 'మార్జినల్ స్టాండింగ్ ఫెసిలిటీ' (MSF) LAF కారిడార్ గరిష్ట పరిమితిగా (Ceiling) పనిచేస్తూ, బ్యాంకులకు అత్యవసర పరిస్థితుల్లో రెపో రేటు కంటే ఎక్కువ వడ్డీకి SLR సెక్యూరిటీల పైగా రుణాలు పొందే అవకాశం కల్పిస్తుంది.\n3. SDF విధానంలో బ్యాంకులు డిపాజిట్ చేసే ప్రతి రూపాయికి ఆర్‌బీఐ తప్పనిసరిగా 100% కేంద్ర ప్రభుత్వ బాండ్లను పూచీకత్తుగా (Collateral) సమర్పించాల్సి ఉంటుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is incorrect. Unlike Fixed Rate Reverse Repo, the whole purpose of creating the Standing Deposit Facility (SDF, recommended by the Urjit Patel Committee and enabled via Sec 17 Finance Act 2018 amendment) was to give RBI a COLLATERAL-FREE tool to absorb massive banking liquidity without depleting RBI's own G-Sec stock.",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. SDF ముఖ్య ఉద్దేశ్యమే ఆర్‌బీఐ తన వద్ద గల ప్రభుత్వ బాండ్లను తాకట్టు పెట్టకుండానే (Collateral-free) బ్యాంకుల అదనపు ద్రవ్య లభ్యతను గ్రహించడం."
    ),
    # E2 (corr=1: 2 and 3 only; stmt 1 false: claims SBI, Bank of Baroda, and PNB are India's three D-SIBs instead of SBI, HDFC Bank, and ICICI Bank!)
    make_q(
        "Banking Regulation - Basel III Capital Norms & D-SIBs",
        "Consider the following statements regarding prudential banking regulation in India:\n1. Under the Reserve Bank of India's Domestic Systemically Important Banks (D-SIBs) framework, State Bank of India, Punjab National Bank, and Bank of Baroda constitute the three designated D-SIBs.\n2. Under Basel III standards as adopted by RBI, Capital Adequacy Ratio (CRAR) measures Tier-1 plus Tier-2 capital relative to Risk-Weighted Assets (RWAs), mandating higher Common Equity Tier-1 (CET1) buffers for D-SIBs.\n3. An asset becomes a Non-Performing Asset (NPA) when interest or principal installment remains overdue for more than 90 days (except certain agricultural crop-season norms), and is subsequently graded into Sub-standard, Doubtful, and Loss assets.\nWhich of the statements given above are correct?",
        "భారత బ్యాంకింగ్ నియంత్రణ మరియు బేసెల్-III (Basel III) ప్రమాణాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఆర్‌బీఐ గుర్తించిన దేశీయ వ్యవస్థాపరంగా ముఖ్యమైన బ్యాంకుల (D-SIBs) జాబితాలో స్టేట్ బ్యాంక్ ఆఫ్ ఇండియా, పంజాబ్ నేషనల్ బ్యాంక్ మరియు బ్యాంక్ ఆఫ్ బరోడాలు మాత్రమే ఉన్నాయి.\n2. బేసెల్-III నిబంధనల ప్రకారం మూలధన సమృద్ధి నిష్పత్తి (CRAR) టైర్-1 మరియు టైర్-2 మూలధన మొత్తాన్ని రిస్క్-వెయిటెడ్ ఆస్తుల నిష్పత్తిలో కొలుస్తుంది; D-SIBలకు అదనపు CET1 బఫర్ అవసరం ఉంటుంది.\n3. రుణ వాయిదా లేదా వడ్డీ 90 రోజులకు పైగా చెల్లించబడకపోతే ఆ ఆస్తిని నిరర్థక ఆస్తిగా (NPA) వర్గీకరిస్తారు (వ్యవసాయ సీజన్ మినహాయింపులతో); దీనిని సబ్-స్టాండర్డ్, డౌట్‌ఫుల్ మరియు లాస్ ఆస్తులుగా విభజిస్తారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is incorrect. The three designated Domestic Systemically Important Banks (D-SIBs, colloquially 'Too Big To Fail') in India are State Bank of India (SBI), HDFC Bank, and ICICI Bank (not PNB or Bank of Baroda).",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. భారతదేశంలో ఆర్‌బీఐ గుర్తించిన మూడు D-SIB బ్యాంకులు: ఎస్‌బీఐ (SBI), హెచ్‌డీఎఫ్‌సీ బ్యాంక్ (HDFC Bank), మరియు ఐసీఐసీఐ బ్యాంక్ (ICICI Bank)."
    ),
    # E3 (corr=2: 1 and 3 only; stmt 2 false: puts Remittances & Tourism receipts in Capital Account instead of Current Account Invisibles!)
    make_q(
        "External Sector - Balance of Payments & Sterilization",
        "Consider the following statements regarding India's Balance of Payments (BoP) accounting:\n1. Foreign Direct Investment (FDI), Foreign Portfolio Investment (FPI), External Commercial Borrowings (ECBs), and NRI deposits are recorded under the Capital Account of the BoP.\n2. Private remittances from Indian workers abroad and software service exports are classified under the Capital Account rather than the Current Account.\n3. When the RBI buys surplus foreign exchange inflows to prevent Rupee appreciation, it simultaneously sells Government bonds (via Open Market Operations / Market Stabilisation Scheme) to absorb excess domestic Rupee liquidity—a process called 'Sterilization'.\nWhich of the statements given above are correct?",
        "భారతదేశ చెల్లింపుల శేషం (Balance of Payments) మరియు విదేశీ మారకద్రవ్య నిర్వహణకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. విదేశీ ప్రత్యక్ష పెట్టుబడులు (FDI), విదేశీ పోర్ట్‌ఫోలియో పెట్టుబడులు (FPI), బాహ్య వాణిజ్య రుణాలు (ECB) మరియు NRI డిపాజిట్లు మూలధన ఖాతా (Capital Account) కింద నమోదవుతాయి.\n2. విదేశాల్లోని భారతీయ కార్మికులు పంపే నిధులు (Remittances) మరియు సాఫ్ట్‌వేర్ సేవల ఎగుమతులు కరెంట్ ఖాతాలో కాకుండా మూలధన ఖాతాలో లెక్కించబడతాయి.\n3. రూపాయి విలువ అతిగా పెరగకుండా ఆర్‌బీఐ విదేశీ మారకద్రవ్యాన్ని కొనుగోలు చేసినప్పుడు, దేశీయ ద్రవ్య సరఫరా పెరగకుండా నియంత్రించడానికి ప్రభుత్వ బాండ్లను విక్రయించే ప్రక్రియను 'స్టెరిలైజేషన్' (Sterilization) అంటారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is false. Services exports (software, travel) and unilateral transfers like worker remittances form the 'Invisibles' net component inside the CURRENT ACCOUNT (not the Capital Account).",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. సాఫ్ట్‌వేర్ సేవల ఎగుమతులు మరియు ప్రవాస భారతీయులు పంపే రెమిటెన్సులు మూలధన ఖాతాలో కాకుండా కరెంట్ ఖాతాలోని 'అదృశ్య అంశాల' (Invisibles) విభాగంలో భాగంగా ఉంటాయి."
    ),
    # E4 (corr=0: 1 and 2 only; stmt 3 false: claims 15th Finance Commission gave highest 45% horizontal weightage to Area / Forest rather than Income Distance!)
    make_q(
        "Fiscal Federalism - Horizontal Devolution Criteria (15th FC Benchmark)",
        "Consider the following statements regarding horizontal tax devolution among States recommended by the 15th Finance Commission (2021–26) for reference by the 16th Finance Commission:\n1. It fixed the vertical share of States in the divisible pool of Central taxes at 41% (adjusting down 1% from the 14th FC's 42% solely due to the reorganization of Jammu & Kashmir and Ladakh into Union Territories).\n2. It introduced 'Demographic Performance' (12.5% weightage) to reward states that achieved lower Total Fertility Rates and population stabilization, utilizing 2011 Census data rather than 1971 data.\n3. Under its horizontal devolution formula, 'Area' received the highest single weightage of 45%, whereas 'Income Distance' received only 15%.\nWhich of the statements given above are correct?",
        "15వ ఆర్థిక సంఘం (2021–26) సిఫార్సు చేసిన పన్నుల పంపిణీ ప్రమాణాలకు (16వ ఆర్థిక సంఘం సమీక్ష నేపథ్యంలో) సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. జమ్మూ & కాశ్మీర్, లడఖ్ కేంద్రపాలిత ప్రాంతాలుగా మారినందున 14వ ఆర్థిక సంఘం ఇచ్చిన 42% నుండి 1% సర్దుబాటు చేసి రాష్ట్రాల నిలువు వాటాను 41% గా నిర్ధారించింది.\n2. 1971 జనాభా లెక్కలకు బదులుగా 2011 జనాభా గణాంకాలను వాడుతూ, జనాభా నియంత్రణలో విజయం సాధించిన రాష్ట్రాలను ప్రోత్సహించేందుకు 'జనాభా పనితీరు' (Demographic Performance - 12.5%) ప్రమాణాన్ని ప్రవేశపెట్టింది.\n3. క్షితిజ సమాంతర పంపిణీ సూత్రంలో 'భౌగోళిక విస్తీర్ణం' (Area) అంశానికి అత్యధికంగా 45% వెయిటేజీ ఇవ్వగా, 'ఆదాయ వ్యత్యాసం' (Income Distance) అంశానికి కేవలం 15% మాత్రమే కేటాయించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is incorrect. Under the 15th Finance Commission formula, 'Income Distance' carried the HIGHEST weightage at 45%, followed by Population (2011) at 15%, Area at 15%, Demographic Performance at 12.5%, Forest & Ecology at 10%, and Tax & Fiscal Efforts at 2.5%.",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. 15వ ఆర్థిక సంఘం సూత్రంలో అత్యధికంగా 45% వెయిటేజీ 'ఆదాయ వ్యత్యాసం' (Income Distance) కు ఇవ్వబడింది; విస్తీర్ణానికి కేవలం 15% మాత్రమే ఇచ్చారు."
    ),
    # E5 (corr=1: A-2, B-4, C-1, D-3 — Inflation terminology match)
    make_q(
        "Macroeconomics - Inflation Variants & Concepts Match",
        "Match the macroeconomic inflation phenomena (List-I) with their exact analytical definitions (List-II):\nList-I:\nA. Stagflation\nB. Shrinkflation\nC. Skewflation\nD. Disinflation\nList-II:\n1. Episode where sustained high price rise is concentrated predominantly in one or a few specific commodity groups (e.g., food/onions) while general prices stay flat\n2. Simultaneous persistence of high price inflation alongside stagnant economic growth and high unemployment (violating simple Phillips Curve trade-offs)\n3. Deceleration in the rate of inflation where the general price level continues to rise, but at a progressively slower percentage pace\n4. Practice of downsizing the quantity/weight of a packaged product while keeping its retail price unchanged\nSelect the correct code:",
        "స్థూల ఆర్థిక శాస్త్రంలోని ద్రవ్యోల్బణ రకాలను (జాబితా-I) వాటి ఖచ్చితమైన అర్థాలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. స్టాగ్‌ఫ్లేషన్ (Stagflation)\nB. ష్రింక్‌ఫ్లేషన్ (Shrinkflation)\nC. స్క్యూఫ్లేషన్ (Skewflation)\nD. డిస్‌ఇన్‌ఫ్లేషన్ (Disinflation)\nజాబితా-II:\n1. సాధారణ ధరలు నిలకడగా ఉన్నా కేవలం కొన్ని ప్రత్యేక వస్తువులలోనే (ఉదా: ఉల్లిపాయలు, ఆహార ధాన్యాలు) తీవ్రమైన ధరల పెరుగుదల ఉండటం\n2. ఆర్థిక వృద్ధి స్తంభించి నిరుద్యోగం పెరుగుతూనే మరోవైపు అధిక ద్రవ్యోల్బణం కొనసాగడం\n3. ధరలు ఇంకా పెరుగుతున్నప్పటికీ ద్రవ్యోల్బణం పెరిగే వేగం/రేటు క్రమంగా తగ్గుముఖం పట్టడం\n4. ప్యాకెట్ ధరను మార్చకుండానే అందులోని వస్తువు పరిమాణం లేదా బరువును తగ్గించడం\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-3, B-4, C-1, D-2", "A-2, B-4, C-1, D-3", "A-2, B-1, C-4, D-3", "A-4, B-2, C-1, D-3"],
        ["A-3, B-4, C-1, D-2", "A-2, B-4, C-1, D-3", "A-2, B-1, C-4, D-3", "A-4, B-2, C-1, D-3"],
        1,
        "Stagflation combines stagnation + inflation (A-2). Shrinkflation shrinks unit pack size at steady price (B-4). Skewflation refers to skewed inflation localized in select food/essential items (C-1). Disinflation is a slowing positive inflation rate, distinct from deflation where prices fall below zero (D-3).",
        "స్టాగ్‌ఫ్లేషన్ - నిరుద్యోగం+మాంద్యం+ద్రవ్యోల్బణం (2); ష్రింక్‌ఫ్లేషన్ - బరువు తగ్గింపు (4); స్క్యూఫ్లేషన్ - కొన్ని వస్తువుల్లోనే ధరల పెరుగుదల (1); డిస్‌ఇన్‌ఫ్లేషన్ - ద్రవ్యోల్బణ రేటు మందగించడం (3)."
    ),
    # E6 (corr=2: 1 and 3 only; stmt 2 false: says FRBM Escape Clause permits permanent unlimited expansion at state CMs' discretion without reporting to Parliament!)
    make_q(
        "Public Finance - FRBM Act, 2003 & N.K. Singh Escape Clause",
        "Consider the following statements regarding the Fiscal Responsibility and Budget Management (FRBM) framework:\n1. Enacted in 2003, the FRBM Act requires the Central Government to present before Parliament the Medium-Term Fiscal Policy Statement, Fiscal Policy Strategy Statement, and Macroeconomic Framework Statement alongside the Annual Financial Statement.\n2. Under the N.K. Singh Committee's 'Escape Clause' incorporated in 2018, the Union Finance Minister can expand fiscal deficit targets by up to 3 percentage points annually solely through an administrative circular without informing Parliament.\n3. In general public finance accounting, 'Revenue Deficit' equals Revenue Expenditure minus Revenue Receipts, whereas 'Primary Deficit' equals Fiscal Deficit minus Interest Payments.\nWhich of the statements given above are correct?",
        "ఆర్థిక బాధ్యత మరియు బడ్జెట్ నిర్వహణ (FRBM) చట్టానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 2003లో రూపొందించిన FRBM చట్టం ప్రకారం కేంద్ర ప్రభుత్వం వార్షిక బడ్జెట్‌తో పాటు మధ్యకాలిక ఆర్థిక విధాన ప్రకటన, ఆర్థిక విధాన వ్యూహ ప్రకటన మరియు స్థూల ఆర్థిక చట్ర ప్రకటనలను పార్లమెంటు ముందు ఉంచాలి.\n2. 2018లో చేర్చిన ఎన్.కె. సింగ్ కమిటీ 'ఎస్కేప్ క్లాజ్' (Escape Clause) ప్రకారం ఆర్థిక మంత్రి పార్లమెంటుకు తెలియజేయాల్సిన అవసరం లేకుండానే పరిపాలనా ఉత్తర్వు ద్వారా ద్రవ్యలోటును ఏడాదికి 3 శాతం మేర పెంచుకోవచ్చు.\n3. ప్రభుత్వ ఆర్థిక గణనలో 'రెవెన్యూ లోటు' అనగా రెవెన్యూ వ్యయం మైనస్ రెవెన్యూ రాబడి, మరియు 'ప్రాథమిక లోటు' (Primary Deficit) అనగా ద్రవ్యలోటు మైనస్ వడ్డీ చెల్లింపులు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is false. Under the FRBM Escape Clause (Section 4(2)), deviations from the fiscal deficit target are strictly capped at 0.5% of GDP per year on specific exceptional grounds (national security, war, calamity, agricultural collapse, structural reform) AND require formal written explanation before both Houses of Parliament.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. ఎస్కేప్ క్లాజ్ కింద ద్రవ్యలోటు సడలింపు గరిష్టంగా జీడీపీలో 0.5% వరకే (అసాధారణ పరిస్థితుల్లో) అనుమతించబడుతుంది మరియు దానికి పార్లమెంటులో లిఖితపూర్వక వివరణ ఇవ్వాలి."
    ),
    # E7 (corr=3: 1, 2, and 3 — GST 101st Amendment, IGST & Inverted Duty Structure)
    make_q(
        "Indirect Taxation - GST Architecture, IGST & Inverted Duty Structure",
        "Consider the following statements regarding the Goods and Services Tax (GST) constitutional and economic mechanism:\n1. Added by the 101st Constitutional Amendment Act, 2016, Article 269A empowers the Union Government to levy and collect Integrated GST (IGST) on inter-State trade and commerce, apportioned between the Union and destination States.\n2. GST operates on a destination-based consumption tax principle via seamless Input Tax Credit (ITC), eliminating the cascading 'tax-on-tax' effect of erstwhile VAT/Excise regimes.\n3. An 'Inverted Duty Structure' arises in GST when the tax rate on raw material inputs is higher than the tax rate on the finished output supply, leading to unutilized accumulated Input Tax Credit.\nWhich of the statements given above are correct?",
        "వస్తు మరియు సేవల పన్ను (GST) రాజ్యాంగ మరియు ఆర్థిక విధానానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 101వ రాజ్యాంగ సవరణ చట్టం (2016) ద్వారా చేర్చిన ఆర్టికల్ 269A ప్రకారం అంతర్-రాష్ట్ర వాణిజ్యంపై కేంద్రం ఇంటిగ్రేటెడ్ జీఎస్టీ (IGST) ను వసూలు చేసి, దానిని వినియోగదారుల రాష్ట్రాలతో పంచుకుంటుంది.\n2. జీఎస్టీ అనేది వినియోగ ఆధారిత (Destination-based) పన్ను; ఇందులోని ఇన్‌పుట్ టాక్స్ క్రెడిట్ (ITC) విధానం ద్వారా పన్నుపై పన్ను పడే 'క్యాస్కేడింగ్ ప్రభావం' తొలగించబడింది.\n3. ముడిసరుకులపై (Inputs) విధించే పన్ను రేటు తుది ఉత్పత్తిపై విధించే పన్ను రేటు కంటే ఎక్కువగా ఉన్నప్పుడు 'ఇన్వర్టెడ్ డ్యూటీ స్ట్రక్చర్' ఏర్పడి ఇన్‌పుట్ టాక్స్ క్రెడిట్ పేరుకుపోతుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. Article 269A governs inter-State IGST; GST eliminates cascading effects via ITC across the supply chain; and Inverted Duty Structure (e.g., in certain textiles, fertilizers, or footwear components) occurs when input GST exceeds output GST.",
        "మూడు ప్రకటనలూ సరైనవే. ఆర్టికల్ 269A కింద అంతర్-రాష్ట్ర వ్యాపారంపై IGST వసూలు చేయబడుతుంది. ఇన్‌పుట్ టాక్స్ క్రెడిట్ పన్ను పై పన్నును నివారిస్తుంది, మరియు ముడిసరుకు పన్ను తుది ఉత్పత్తి పన్ను కంటే ఎక్కువైతే ఇన్వర్టెడ్ డ్యూటీ స్ట్రక్చర్ అంటారు."
    ),
    # E8 (corr=0: 1 and 2 only; stmt 3 false: claims T-Bills pay fixed semi-annual interest coupons like long-dated G-Secs, whereas T-Bills are ZERO-COUPON instruments issued at discount and redeemed at face value!)
    make_q(
        "Money & Capital Markets - Treasury Bills, CMBs & Ways and Means Advances",
        "Consider the following statements regarding sovereign short-term debt instruments in India:\n1. Treasury Bills (T-Bills) are short-term money market obligations issued exclusively by the Central Government (not State Governments) across three standard tenors: 91 days, 182 days, and 364 days.\n2. Ways and Means Advances (WMA) represent temporary overdraft-like advances extended by the RBI under Section 17(5) of the RBI Act, 1934 to bridge temporary mismatches in Central and State government cash flows.\n3. Like 10-year Government Securities, Treasury Bills pay a fixed semi-annual interest coupon rate every six months until maturity.\nWhich of the statements given above are correct?",
        "భారతదేశంలోని స్వల్పకాలిక ప్రభుత్వ రుణ సాధనాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ట్రెజరీ బిల్లులను (T-Bills) కేవలం కేంద్ర ప్రభుత్వం మాత్రమే (రాష్ట్ర ప్రభుత్వాలు కాదు) 91 రోజులు, 182 రోజులు మరియు 364 రోజుల కాలపరిమితితో జారీ చేస్తుంది.\n2. ఆర్‌బీఐ చట్టం 1934 లోని సెక్షన్ 17(5) ప్రకారం కేంద్ర, రాష్ట్ర ప్రభుత్వాల రాబడి-వ్యయాల మధ్య తాత్కాలిక అంతరాలను పూడ్చడానికి ఆర్‌బీఐ అందించే స్వల్పకాలిక రుణాలను 'వేస్ అండ్ మీన్స్ అడ్వాన్సెస్' (WMA) అంటారు.\n3. 10 సంవత్సరాల ప్రభుత్వ సెక్యూరిటీల మాదిరిగానే ట్రెజరీ బిల్లులు కూడా ప్రతి ఆరు నెలలకు ఒకసారి స్థిరమైన వడ్డీ కూపన్ (Interest Coupon) ను చెల్లిస్తాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is incorrect. Treasury Bills (and Cash Management Bills under 91 days) are ZERO-COUPON securities that pay NO periodic interest; they are issued at a discount to face value and redeemed at par at maturity (the difference being the investor's return).",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. ట్రెజరీ బిల్లులు 'జీరో-కూపన్' బాండ్లు; వీటిపై వడ్డీ చెల్లించరు—వాటిని ముఖ విలువ కంటే తక్కువ ధరకు (Discount) జారీ చేసి గడువు ముగిశాక పూర్తి ముఖ విలువను చెల్లిస్తారు."
    ),
    # E9 (corr=1: 2 and 3 only; stmt 1 false: says Operational Creditors outrank Secured Financial Creditors and Workmen's Dues in Sec 53 Waterfall!)
    make_q(
        "Structural Reforms - Insolvency & Bankruptcy Code (IBC), 2016",
        "Consider the following statements regarding the Corporate Insolvency Resolution Process (CIRP) under the Insolvency and Bankruptcy Code (IBC), 2016:\n1. Under the Section 53 liquidation waterfall mechanism, unsecured Operational Creditors and equity shareholders are paid ahead of workmen's dues and secured Financial Creditors.\n2. The 2019 Amendment to Section 12 of the IBC stipulates that the CIRP (including litigation and appeals time) should ordinarily be completed within an outer limit of 330 days from the insolvency commencement date.\n3. Regulated by the Insolvency and Bankruptcy Board of India (IBBI), the Committee of Creditors (CoC) predominantly comprising Financial Creditors decides whether to approve a resolution plan by a 66% voting share.\nWhich of the statements given above are correct?",
        "దివాలా మరియు దివాలా కోడ్ (IBC), 2016 కింద కార్పొరేట్ దివాలా పరిష్కార ప్రక్రియకు (CIRP) సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. సెక్షన్ 53 లిక్విడేషన్ వాటర్‌ఫాల్ ప్రాధాన్యతా క్రమంలో కార్మికుల బకాయిలు మరియు సెక్యూర్డ్ ఫైనాన్షియల్ రుణదాతల కంటే ముందే ఈక్విటీ వాటాదారులకు, ఆపరేషనల్ రుణదాతలకు చెల్లింపులు జరుగుతాయి.\n2. 2019 IBC సవరణ ప్రకారం న్యాయపరమైన విచారణ సమయంతో సహా మొత్తం CIRP ప్రక్రియను దివాలా ప్రారంభమైన తేదీ నుండి గరిష్టంగా 330 రోజులలోగా పూర్తి చేయాలి.\n3. IBBI నియంత్రణలో పనిచేసే రుణదాతల కమిటీ (CoC) లో ప్రధానంగా ఆర్థిక రుణదాతలు (Financial Creditors) ఉండి, 66% ఓటింగ్ మెజారిటీతో పరిష్కార ప్రణాళికను ఆమోదిస్తారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is backwards. Under Section 53 of the IBC (waterfall mechanism), Insolvency Resolution costs stand 1st, followed jointly at 2nd by workmen's dues (for 24 months) and debts owed to SECURED creditors, well ahead of unsecured Operational Creditors and equity shareholders (who stand last).",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. సెక్షన్ 53 ప్రాధాన్యతలో మొదట దివాలా ప్రక్రియ ఖర్చులు, తర్వాత కార్మికుల 24 నెలల బకాయిలు & సెక్యూర్డ్ రుణదాతలు ఉంటారు; ఈక్విటీ వాటాదారులు చిట్టచివరన ఉంటారు."
    ),
    # E10 (corr=3: 1, 2, and 3 — Telangana Industrial Governance: TS-iPASS & Service Economy)
    make_q(
        "Telangana Economy - TS-iPASS Framework & Structural Growth",
        "Consider the following statements regarding Telangana's industrial policy and economic structure:\n1. Enacted under the Telangana State Industrial Project Approval and Self-Certification System (TS-iPASS) Act, 2014, mega-projects above specified thresholds are assured statutory clearances within 15 days (or 30 days for standard units), failing which there is a 'deemed approval' provision.\n2. Telangana ranks among the top states in India in Per Capita Income (GSDP per capita at current prices), consistently exceeding the national average by a substantial margin.\n3. The Tertiary (Services) sector—anchored by Information Technology exports, Real Estate, Financial Services, and Global Capability Centres (GCCs) in Hyderabad—contributes over 60% of Telangana's Gross State Value Added (GSVA).\nWhich of the statements given above are correct?",
        "తెలంగాణ పారిశ్రామిక విధానం మరియు ఆర్థిక వ్యవస్థ నిర్మాణానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 2014లో రూపొందించిన TS-iPASS చట్టం ప్రకారం భారీ పరిశ్రమలకు 15 రోజుల్లోపు (ఇతర యూనిట్లకు 30 రోజుల్లోపు) చట్టబద్ధ అనుమతులు ఇవ్వకపోతే ఆటోమేటిక్ 'డీమ్డ్ అప్రూవల్' (Deemed Approval) వర్తిస్తుంది.\n2. తలసరి ఆదాయం (Per Capita Income) పరంగా తెలంగాణ భారతదేశంలోని ప్రధాన పెద్ద రాష్ట్రాలలో అగ్రశ్రేణిలో కొనసాగుతూ జాతీయ సగటు కంటే గణనీయంగా ఎక్కువ స్థాయిలో ఉంది.\n3. హైదరాబాద్ కేంద్రంగా ఉన్న ఐటీ ఎగుమతులు, రియల్ ఎస్టేట్, ఆర్థిక సేవలు మరియు గ్లోబల్ కెపాబిలిటీ సెంటర్ల (GCCs) మద్దతుతో సేవా రంగం (Tertiary Sector) తెలంగాణ GSVA లో 60% కంటే ఎక్కువ వాటాను అందిస్తోంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. TS-iPASS (2014) pioneered time-bound self-certified single-window clearances (15 days for mega projects) with a deemed approval clause; Telangana maintains one of India's highest per capita NSDP figures; and its services sector consistently exceeds 62–65% of GSVA.",
        "మూడు ప్రకటనలూ సరైనవే. TS-iPASS మెగా ప్రాజెక్టులకు 15 రోజుల్లో డీమ్డ్ అప్రూవల్ కల్పిస్తుంది; తెలంగాణ తలసరి ఆదాయంలో అగ్రగామి రాష్ట్రాలలో ఒకటిగా నిలుస్తోంది మరియు సేవా రంగం GSVA లో 60% పైగా వాటా కలిగి ఉంది."
    ),
]

# ==================== 6. SCIENCE & TECHNOLOGY NEW (14) ====================
# Balance target: {0: 3, 1: 3, 2: 3, 3: 5}
NEW_SCIENCE = [
    # S1 (corr=0: 1 and 2 only; stmt 3 false: claims L1 sits BEHIND Earth on night side like JWST L2!)
    make_q(
        "Space Technology - Lagrange Points & Aditya-L1 Observatory",
        "Consider the following statements regarding orbital mechanics and India's Aditya-L1 solar mission:\n1. Lagrange Points are five positions in a two-body gravitational system (Sun-Earth) where combined gravitational pulls balance centripetal force, allowing spacecraft like Aditya-L1 at L1 (~1.5 million km from Earth) to maintain a stable halo orbit.\n2. Aditya-L1 carries seven payloads including the Visible Emission Line Coronagraph (VELC) and Solar Ultraviolet Imaging Telescope (SUIT) to study coronal heating and Coronal Mass Ejections (CMEs).\n3. Point L1 is positioned behind Earth away from the Sun (the anti-sunward night side) where Earth permanently shields Aditya-L1 from solar glare.\nWhich of the statements given above are correct?",
        "కక్ష్యా యాంత్రిక శాస్త్రం (Orbital Mechanics) మరియు భారతదేశపు 'ఆదిత్య-L1' సౌర మిషన్‌కు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. సూర్యుడు-భూమి వ్యవస్థలో గురుత్వాకర్షణ బలాలు మరియు అపకేంద్ర బలం సమతుల్యం అయ్యే ఐదు స్థానాలను లాగ్రాంజ్ పాయింట్లు అంటారు; భూమి నుండి సుమారు 15 లక్షల కి.మీ దూరంలోని L1 వద్ద ఆదిత్య-L1 హాలో కక్ష్యలో స్థిరంగా ఉంటుంది.\n2. సూర్య కరోనా తాపనం మరియు కరోనల్ మాస్ ఎజెక్షన్లను (CMEs) అధ్యయనం చేసేందుకు ఆదిత్య-L1 లో VELC మరియు SUIT సహా మొత్తం ఏడు పేలోడ్లు ఉన్నాయి.\n3. సూర్యుని ప్రకాశం నుండి రక్షణ పొందేందుకు L1 పాయింట్ భూమికి వెనుకవైపు (సూర్యునికి వ్యతిరేక రాత్రి దిశలో) ఉంటుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is incorrect. Point L1 lies BETWEEN the Sun and the Earth (~1.5 million km sunward), affording Aditya-L1 an uninterrupted view of the Sun without occultation or eclipses. Point L2 (where James Webb Space Telescope sits) is the anti-sunward point behind Earth.",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. ఆదిత్య-L1 ఉన్న L1 పాయింట్ సూర్యుడు మరియు భూమికి మధ్యలో ఉండి నిరంతరాయంగా సూర్యుని వీక్షించే అవకాశం కల్పిస్తుంది (భూమికి వెనుకవైపు ఉండేది JWST ఉన్న L2 పాయింట్)."
    ),
    # S2 (corr=1: 2 and 3 only; stmt 1 false: says cryogenic engines burn solid HTPB ammonium perchlorate fuel at room temp instead of super-cooled LH2 & LOX!)
    make_q(
        "Propulsion Physics - Cryogenic vs Ramjet & Scramjet Engines",
        "Consider the following statements regarding rocket and air-breathing aerospace propulsion systems:\n1. Cryogenic rocket engines such as ISRO's CE-20 operate using ambient room-temperature solid propellants like HTPB mixed with ammonium perchlorate for multi-year storage.\n2. Air-breathing Ramjet engines compress incoming supersonic air through forward vehicle velocity without rotating compressor blades and decelerate airflow to subsonic speed for combustion (used in BrahMos cruise missiles).\n3. Supersonic Combustion Ramjet (Scramjet) engines sustain combustion while airflow inside the engine remains supersonic, enabling efficient hypersonic flight above Mach 5 while scooping atmospheric oxygen instead of carrying onboard oxidizer.\nWhich of the statements given above are correct?",
        "రాకెట్ మరియు అంతరిక్ష ప్రొపల్షన్ (Propulsion) ఇంజన్లకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఇస్రో రూపొందించిన CE-20 వంటి క్రయోజెనిక్ ఇంజన్లు గది ఉష్ణోగ్రత వద్ద నిల్వ చేయగల HTPB వంటి ఘన ఇంధనాలను ఉపయోగిస్తాయి.\n2. రామ్‌జెట్ (Ramjet) ఇంజన్లు తిరిగే కంప్రెసర్ బ్లేడ్లు లేకుండానే వాహన వేగంతో లోపలికి వచ్చే గాలిని సబ్‌సోనిక్ వేగానికి తగ్గించి దహనం జరుపుతాయి (బ్రహ్మోస్ క్షిపణిలో వాడతారు).\n3. స్క్రామ్‌జెట్ (Scramjet) ఇంజన్లు దహన గదిలో గాలి ప్రవాహం సూపర్‌సోనిక్ వేగంతోనే ఉన్నప్పుడు దహనాన్ని కొనసాగించి, మాక్ 5 (Mach 5) పైబడిన హైపర్‌సోనిక్ వేగంతో వాతావరణ ఆక్సిజన్‌నే వినియోగిస్తాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is false. Cryogenic rocket engines (such as CE-20 powering LVM3's C25 stage) burn super-cooled liquefied propellants—Liquid Hydrogen (fuel, stored around -253 deg C) and Liquid Oxygen (oxidizer, stored around -183 deg C)—delivering very high specific impulse.",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. క్రయోజెనిక్ ఇంజన్లు అతి తక్కువ ఉష్ణోగ్రతల వద్ద నిల్వ చేసే ద్రవ హైడ్రోజన్ (-253°C) మరియు ద్రవ ఆక్సిజన్ (-183°C) ఇంధనాలను ఉపయోగిస్తాయి."
    ),
    # S3 (corr=2: A-3, B-4, C-1, D-2 — Optical phenomena match)
    make_q(
        "Physics - Optical Wave & Ray Phenomena Match",
        "Match the classical optical phenomena (List-I) with their governing physical mechanisms (List-II):\nList-I:\nA. Transmission inside Optical Fibres\nB. Blue colour of the clear daytime sky\nC. Colours on a thin soap film/oil slick\nD. Reddish appearance of rising/setting Sun\nList-II:\n1. Constructive and destructive Interference of light waves reflected from top and bottom surfaces\n2. Predominant atmospheric scattering of shorter blue wavelengths along longer horizontal air paths, leaving red/orange\n3. Repeated Total Internal Reflection (TIR) when light hits cladding at angles exceeding the critical angle\n4. Selective Rayleigh Scattering inversely proportional to the fourth power of wavelength\nSelect the correct code:",
        "భౌతిక శాస్త్రంలోని కాంతి దృగ్విషయాలను (జాబితా-I) వాటికి కారణమైన శాస్త్రీయ నియమాలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. ఆప్టికల్ ఫైబర్లలో కాంతి ప్రసారం\nB. పగటిపూట ఆకాశం నీలి రంగులో కనిపించడం\nC. సబ్బు బుడగపై వివిధ రంగులు కనిపించడం\nD. సూర్యోదయ, సూర్యాస్తమయ సమయాల్లో సూర్యుడు ఎర్రగా కనిపించడం\nజాబితా-II:\n1. సబ్బు పొరపై పై మరియు దిగువ ఉపరితలాల నుండి పరావర్తనం చెందిన కాంతి తరంగాల వ్యతికరణం (Interference)\n2. వాతావరణంలో ఎక్కువ దూరం ప్రయాణించాల్సి రావడంతో తక్కువ తరంగదైర్ఘ్యం గల నీలం కాంతి చెదిరిపోయి, ఎక్కువ తరంగదైర్ఘ్యం గల ఎరుపు కాంతి చేరడం\n3. సందిగ్ధ కోణం కంటే ఎక్కువ కోణంలో ప్రయాణించే కాంతికి సంపూర్ణాంతర పరావర్తనం (TIR) జరగడం\n4. తరంగదైర్ఘ్యం యొక్క నాలుగవ ఘాతానికి విలోమానుపాతంలో ఉండే రేలీ పరిక్షేపణం (Rayleigh Scattering)\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-3, B-1, C-4, D-2", "A-1, B-4, C-3, D-2", "A-3, B-4, C-1, D-2", "A-3, B-2, C-1, D-4"],
        ["A-3, B-1, C-4, D-2", "A-1, B-4, C-3, D-2", "A-3, B-4, C-1, D-2", "A-3, B-2, C-1, D-4"],
        2,
        "Optical fibres rely on Total Internal Reflection (A-3); daytime blue sky stems from Rayleigh scattering (~1/lambda^4) (B-4); soap film iridescence arises from thin-film optical Interference (C-1); and sunset redness results from loss of scattered blue light across a long atmospheric path leaving long-wavelength red (D-2).",
        "ఆప్టికల్ ఫైబర్ - సంపూర్ణాంతర పరావర్తనం (3); ఆకాశం నీలి రంగు - రేలీ పరిక్షేపణం (4); సబ్బు బుడగ రంగులు - తరంగ వ్యతికరణం (1); అస్తమించే సూర్యుడు ఎరుపు - ఎక్కువ దూర ప్రయాణంలో నీలం చెదిరి ఎరుపు మిగలడం (2)."
    ),
    # S4 (corr=3: 1, 2, and 3 — Nuclear Fission & Fusion reactors)
    make_q(
        "Nuclear Physics - Fission Reactor Design & ITER Fusion",
        "Consider the following statements regarding nuclear reactor physics:\n1. In a thermal nuclear fission reactor (such as India's Pressurized Heavy Water Reactors - PHWRs), a 'Moderator' like Heavy Water (D2O) or Graphite slows down fast fission neutrons into low-energy thermal neutrons to sustain chain reactions with U-235.\n2. 'Control Rods' fabricated from materials with high neutron-absorption cross-sections—such as Boron or Cadmium—are inserted or withdrawn to regulate reactor criticality.\n3. Unlike fission of heavy nuclei, controlled nuclear fusion inside magnetic-confinement Tokamak devices (like ITER) fuses light Deuterium and Tritium nuclei at extreme plasma temperatures exceeding 100 million Kelvin.\nWhich of the statements given above are correct?",
        "కేంద్రక భౌతిక శాస్త్రం మరియు అణు రియాక్టర్ల పనితీరుకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. భారతదేశంలోని ప్రెషరైజ్డ్ హెవీ వాటర్ రియాక్టర్ల (PHWR) లో భారజలం (D2O) లేదా గ్రాఫైట్ వంటి 'మితకారి' (Moderator) వేగవంతమైన న్యూట్రాన్లను మందగించి U-235 శృంఖల చర్యను కొనసాగిస్తుంది.\n2. బోరాన్ లేదా కాడ్మియం వంటి అధిక న్యూట్రాన్ శోషణ సామర్థ్యం గల పదార్థాలతో చేసిన 'కంట్రోల్ రాడ్ల'ను ఉపయోగించి అణు చర్య వేగాన్ని నియంత్రిస్తారు.\n3. భారీ కేంద్రకాలను విచ్ఛిన్నం చేసే విచ్ఛిత్తికి (Fission) భిన్నంగా, ITER వంటి టోకామాక్ (Tokamak) సంలీన రియాక్టర్లు 100 మిలియన్ కెల్విన్ కంటే ఎక్కువ ఉష్ణోగ్రత వద్ద డ్యుటీరియం మరియు ట్రిటియం కేంద్రకాలను సంలీనం చేస్తాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. D2O (heavy water) slows neutrons without capturing them; Boron/Cadmium control rods absorb surplus neutrons; and Deuterium-Tritium fusion produces Helium and high energy inside magnetic Tokamak vessels.",
        "మూడు ప్రకటనలూ సరైనవే. భారజలం న్యూట్రాన్లను నెమ్మదిస్తుంది, బోరాన్/కాడ్మియం కంట్రోల్ రాడ్లు అదనపు న్యూట్రాన్లను గ్రహిస్తాయి, మరియు టోకామాక్ రియాక్టర్లలో డ్యుటీరియం-ట్రిటియం అణు సంలీనం జరుగుతుంది."
    ),
    # S5 (corr=0: 1 and 2 only; stmt 3 false: claims Meissner effect causes superconductors to pull magnetic lines INTO the interior rather than completely expelling them!)
    make_q(
        "Solid-State Physics - Semiconductor Doping & Superconductivity",
        "Consider the following statements regarding semiconductors and superconducting materials:\n1. Doping pure tetravalent Silicon with a trivalent Group 13 impurity (such as Boron or Gallium) creates a p-type extrinsic semiconductor where positively charged 'holes' act as majority charge carriers.\n2. Doping pure Silicon with a pentavalent Group 15 element (such as Phosphorus or Arsenic) yields an n-type semiconductor with free electrons as majority carriers.\n3. Below its critical transition temperature, a superconductor exhibits the 'Meissner Effect' by absorbing and concentrating external magnetic flux lines deep within its crystal lattice.\nWhich of the statements given above are correct?",
        "అర్ధవాహకాలు (Semiconductors) మరియు అతివాహకాల (Superconductors) భౌతిక ధర్మాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. స్వచ్ఛమైన సిలికాన్ స్ఫటికానికి బోరాన్ లేదా గాలియం వంటి త్రిసంయోజక (Group 13) మూలకాన్ని కలిపితే 'హోల్స్' (Holes) ప్రధాన వాహకాలుగా ఉండే p-రకం అర్ధవాహకం ఏర్పడుతుంది.\n2. సిలికాన్‌కు ఫాస్ఫరస్ లేదా ఆర్సెనిక్ వంటి పంచసంయోజక (Group 15) మూలకాన్ని కలిపితే స్వేచ్ఛా ఎలక్ట్రాన్లు ప్రధాన వాహకాలుగా ఉండే n-రకం అర్ధవాహకం ఏర్పడుతుంది.\n3. సందిగ్ధ ఉష్ణోగ్రత కంటే తక్కువ వద్ద ఒక అతివాహకం బాహ్య అయస్కాంత బలరేఖలను తన లోపలికి బలంగా ఆకర్షించి నిల్వ చేయడాన్ని 'మీస్నర్ ప్రభావం' (Meissner Effect) అంటారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is incorrect. Below the critical temperature Tc, a superconductor demonstrates the Meissner Effect by EXPELlING magnetic flux lines completely from its interior (acting as a perfect diamagnet), not pulling them inside.",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. 'మీస్నర్ ప్రభావం' అనగా అతివాహకం తన లోపల అయస్కాంత క్షేత్రాన్ని శూన్యం చేసి అయస్కాంత బలరేఖలను పూర్తిగా బయటకు నెట్టివేయడం (Perfect Diamagnetism)."
    ),
    # S6 (corr=1: A-2, B-4, C-1, D-3 — Alloys & Polymers chemistry match)
    make_q(
        "Materials Chemistry - Industrial Alloys & Vulcanized Polymers",
        "Match the industrial materials and alloys (List-I) with their exact elemental composition or chemical cross-linking modification (List-II):\nList-I:\nA. Bronze\nB. Brass\nC. Solder\nD. Vulcanized Natural Rubber\nList-II:\n1. Low-melting alloy of Lead (Pb) and Tin (Sn) used in electrical jointing\n2. Alloy of Copper (Cu) and Tin (Sn), resistant to corrosion in bells and marine bearings\n3. Natural polyisoprene heated with 3–5% Sulphur to form cross-linked disulphide bridges improving elasticity\n4. Alloy of Copper (Cu) and Zinc (Zn), widely used in musical instruments and cartridge casings\nSelect the correct code:",
        "పారిశ్రామిక మిశ్రమ లోహాలు మరియు రసాయన పదార్థాలను (జాబితా-I) వాటి ఖచ్చితమైన సంఘటనాలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. కంచు (Bronze)\nB. ఇత్తడి (Brass)\nC. సోల్డర్ (Solder)\nD. వల్కనైజ్డ్ సహజ రబ్బరు\nజాబితా-II:\n1. సీసం (Pb) మరియు తగరం (Sn) లతో కూడిన తక్కువ ద్రవీభవన స్థానం గల మిశ్రమ లోహం\n2. రాగి (Cu) మరియు తగరం (Sn) లతో తయారయ్యే తుప్పు నిరోధక మిశ్రమ లోహం\n3. స్థితిస్థాపకతను పెంచడానికి సహజ రబ్బరును (పాలిఐసోప్రీన్) 3–5% సల్ఫర్‌తో వేడి చేసి క్రాస్-లింక్ చేయడం\n4. రాగి (Cu) మరియు జింక్ (Zn) ల మిశ్రమ లోహం (సంగీత వాయిద్యాలు, తూటా కేసింగ్లలో ఉపయోగిస్తారు)\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-4, B-2, C-1, D-3", "A-2, B-4, C-1, D-3", "A-2, B-1, C-4, D-3", "A-1, B-4, C-2, D-3"],
        ["A-4, B-2, C-1, D-3", "A-2, B-4, C-1, D-3", "A-2, B-1, C-4, D-3", "A-1, B-4, C-2, D-3"],
        1,
        "Bronze = Copper + Tin (Cu+Sn) (A-2); Brass = Copper + Zinc (Cu+Zn) (B-4); Solder = Lead + Tin (Pb+Sn) (C-1); Vulcanized Rubber involves heating polyisoprene with sulphur to create elastic disulphide cross-links (D-3).",
        "కంచు = రాగి+తగరం (2); ఇత్తడి = రాగి+జింక్ (4); సోల్డర్ = సీసం+తగరం (1); వల్కనైజేషన్ = రబ్బరుకు సల్ఫర్ కలపడం (3)."
    ),
    # S7 (corr=2: 1 and 3 only; stmt 2 false: says Copper/Gold acts as sacrificial anode to rust before Iron instead of more reactive Zinc/Magnesium!)
    make_q(
        "Electrochemistry - Lithium-Ion Batteries & Cathodic Protection",
        "Consider the following statements regarding electrochemistry in energy storage and corrosion control:\n1. In a standard Lithium-ion rechargeable battery, lithium ions shuttle reversibly through a liquid/polymer electrolyte between a graphite anode (during charge) and a layered transition-metal oxide cathode (e.g., LiCoO2 or LiFePO4) during discharge.\n2. To protect underground steel pipelines or ship hulls from rusting via sacrificial cathodic protection, blocks of less reactive metals such as Copper or Silver are attached so they oxidize preferentially before iron.\n3. Replacing flammable liquid organic electrolytes with non-flammable ceramic/polymer solid electrolytes in Solid-State Batteries improves thermal safety and volumetric energy density.\nWhich of the statements given above are correct?",
        "శక్తి నిల్వ మరియు లోహ క్షయ నివారణలో విద్యుత్ రసాయన శాస్త్రానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. లిథియం-అయాన్ బ్యాటరీలో చార్జింగ్ మరియు డిశ్చార్జింగ్ సమయంలో లిథియం అయాన్లు ద్రవ ఎలక్ట్రోలైట్ గుండా గ్రాఫైట్ ఆనోడ్ మరియు లిథియం లోహ ఆక్సైడ్ (LiCoO2/LiFePO4) కాథోడ్ మధ్య కదులుతాయి.\n2. భూగర్భ ఇనుప పైపులను లేదా ఓడల హల్స్‌ను తుప్పు పట్టకుండా రక్షించడానికి, ఇనుము కంటే తక్కువ చర్యాశీలత గల రాగి లేదా వెండి దిమ్మెలను త్యాగ ఆనోడ్‌లుగా (Sacrificial Anodes) అమర్చుతారు.\n3. ద్రవ సేంద్రియ ఎలక్ట్రోలైట్లకు బదులుగా ఘన సిరామిక్/పాలిమర్ ఎలక్ట్రోలైట్లను వాడే 'సాలిడ్-స్టేట్ బ్యాటరీలు' అగ్నిప్రమాదాలను తగ్గించి శక్తి సాంద్రతను పెంచుతాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is chemically false. Sacrificial cathodic protection requires attaching a MORE electropositive/reactive metal with lower standard reduction potential than iron—such as MAGNESIUM or ZINC—so that the sacrificial anode oxidizes first instead of the iron pipe. Attaching Copper would actually accelerate iron rusting!",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. త్యాగ ఆనోడ్‌గా ఇనుము కంటే ఎక్కువ చర్యాశీలత గల మెగ్నీషియం లేదా జింక్ లోహాలను వాడతారు తప్ప రాగి లేదా వెండిని కాదు (రాగిని కలిపితే ఇనుము మరింత వేగంగా తుప్పు పడుతుంది)."
    ),
    # S8 (corr=3: 1, 2, and 3 — Green/Blue/Grey Hydrogen & PEM Electrolyzer)
    make_q(
        "Clean Energy Chemistry - Hydrogen Taxonomy & Electrolyzers",
        "Consider the following statements regarding the colour-coded production pathways of Hydrogen under the National Green Hydrogen Mission:\n1. 'Green Hydrogen' is generated via water electrolysis split using electricity exclusively from renewable sources (solar, wind, hydro), emitting near-zero lifecycle carbon dioxide.\n2. 'Grey Hydrogen' is produced from natural gas via Steam Methane Reforming (SMR) without carbon capture, whereas 'Blue Hydrogen' combines SMR with Carbon Capture, Utilization, and Storage (CCUS).\n3. Both Alkaline Liquid Electrolyzers (using aqueous KOH solution) and Proton Exchange Membrane (PEM) Electrolyzers split water into hydrogen gas at the cathode and oxygen gas at the anode.\nWhich of the statements given above are correct?",
        "జాతీయ గ్రీన్ హైడ్రోజన్ మిషన్ నేపథ్యంలో హైడ్రోజన్ ఉత్పత్తి విధానాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 'గ్రీన్ హైడ్రోజన్' అనేది సౌర, పవన లేదా జల వంటి పునరుత్పాదక విద్యుత్తును ఉపయోగించి నీటి విద్యుద్విశ్లేషణ (Electrolysis) ద్వారా కార్బన్ ఉద్గారాలు లేకుండా ఉత్పత్తి చేయబడుతుంది.\n2. సహజ వాయువు నుండి కార్బన్ సంగ్రహణ లేకుండా స్టీమ్ మీథేన్ రిఫార్మింగ్ (SMR) ద్వారా తయారు చేసేది 'గ్రే హైడ్రోజన్' కాగా, దానితో పాటు కార్బన్ క్యాప్చర్ (CCUS) చేపడితే 'బ్లూ హైడ్రోజన్' అంటారు.\n3. ఆల్కలీన్ ఎలక్ట్రోలైజర్లు మరియు ప్రోటాన్ ఎక్స్ఛేంజ్ మెంబ్రేన్ (PEM) ఎలక్ట్రోలైజర్లు రెండూ నీటిని విడగొట్టి కాథోడ్ వద్ద హైడ్రోజన్ వాయువును, ఆనోడ్ వద్ద ఆక్సిజన్ వాయువును విడుదల చేస్తాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. Hydrogen classification reflects its production pathway and carbon footprint; during water electrolysis (2H2O -> 2H2 + O2), reduction produces H2 at the cathode while oxidation yields O2 at the anode.",
        "మూడు ప్రకటనలూ సరైనవే. పునరుత్పాదక ఇంధన విద్యుత్ విశ్లేషణ ద్వారా గ్రీన్, కార్బన్ సంగ్రహణ లేని SMR ద్వారా గ్రే, CCUS తో కూడిన SMR ద్వారా బ్లూ హైడ్రోజన్ తయారవుతాయి; విద్యుద్విశ్లేషణలో కాథోడ్ వద్ద హైడ్రోజన్, ఆనోడ్ వద్ద ఆక్సిజన్ వెలువడతాయి."
    ),
    # S9 (corr=3: 1, 2, and 3 — Verified NexCAR19 IIT Bombay + TMC + CDSCO from search_web!)
    make_q(
        "Medical Biotechnology - Indigenous CAR-T Cell Therapy (NexCAR19)",
        "Consider the following statements regarding India's first indigenous CAR-T cell cancer therapy, 'NexCAR19':\n1. NexCAR19 was indigenously conceptualized and engineered through collaboration between IIT Bombay, the Tata Memorial Centre (TMC), and IIT-incubated spin-off ImmunoACT.\n2. The Central Drugs Standard Control Organisation (CDSCO) granted market authorization for NexCAR19 to treat relapsed/refractory B-cell lymphomas and leukaemias.\n3. CAR-T (Chimeric Antigen Receptor T-cell) therapy works by extracting a patient's own T-cells, genetically reprogramming them in the lab to recognize and destroy CD19-expressing cancer cells, and infusing them back.\nWhich of the statements given above are correct?",
        "భారతదేశపు మొట్టమొదటి స్వదేశీ CAR-T సెల్ క్యాన్సర్ చికిత్స 'నెక్స్‌కార్19' (NexCAR19) కు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. నెక్స్‌కార్19 చికిత్సను ఐఐటీ బాంబే (IIT Bombay), టాటా మెమోరియల్ సెంటర్ (TMC) మరియు ఐఐటీ స్టార్టప్ ఇమ్యునోయాక్ట్ (ImmunoACT) సంయుక్తంగా స్వదేశీ పరిజ్ఞానంతో అభివృద్ధి చేశాయి.\n2. బి-సెల్ లింఫోమాలు మరియు ల్యుకేమియా వంటి రక్త క్యాన్సర్ల చికిత్సకు సెంట్రల్ డ్రగ్స్ స్టాండర్డ్ కంట్రోల్ ఆర్గనైజేషన్ (CDSCO) నెక్స్‌కార్19 కు మార్కెట్ అనుమతిని మంజూరు చేసింది.\n3. CAR-T సెల్ థెరపీలో రోగి శరీరంలోని T-కణాలను సేకరించి, వాటిని ప్రయోగశాలలో జన్యుపరంగా మార్పు చేసి తిరిగి శరీరంలోకి పంపడం ద్వారా CD19 క్యాన్సర్ కణాలను నాశనం చేస్తారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. Developed jointly by IIT Bombay (Prof. Rahul Purwar's team), Tata Memorial Centre, and ImmunoACT and approved by CDSCO, NexCAR19 provides affordable indigenous gene-modified cell therapy for B-cell malignancies.",
        "మూడు ప్రకటనలూ సరైనవే. ఐఐటీ బాంబే, టాటా మెమోరియల్ సెంటర్ అభివృద్ధి చేసిన నెక్స్‌కార్19 చికిత్సకు CDSCO ఆమోదం లభించింది; ఇది బి-సెల్ రక్త క్యాన్సర్లను నిర్మూలించే స్వదేశీ CAR-T సెల్ జన్యు చికిత్స."
    ),
    # S10 (corr=0: A-3, B-1, C-4, D-2 — Endocrine Glands & Hormones Match)
    make_q(
        "Human Physiology - Endocrine Glands & Hormonal Disorders Match",
        "Match the endocrine hormones (List-I) with their originating gland/cell and physiological role or deficiency disorder (List-II):\nList-I:\nA. Antidiuretic Hormone (ADH / Vasopressin)\nB. Melatonin\nC. Aldosterone\nD. Glucagon\nList-II:\n1. Secreted by Pineal gland; regulates circadian sleep-wake rhythm and light-dark cycles\n2. Secreted by Alpha cells of Pancreatic Islets of Langerhans; promotes glycogenolysis to raise blood glucose\n3. Synthesized by Hypothalamus and released by Posterior Pituitary; deficiency causes Diabetes Insipidus\n4. Mineralocorticoid from Adrenal Cortex; regulates sodium reabsorption and potassium excretion in renal tubules\nSelect the correct code:",
        "మానవ అంతఃస్రావక హార్మోన్లను (జాబితా-I) వాటి ఉత్పత్తి గ్రంథులు మరియు శరీరధర్మ పాత్ర లేదా లోప వ్యాధులతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. యాంటీడైయురేటిక్ హార్మోన్ (ADH / వాసోప్రెస్సిన్)\nB. మెలటోనిన్\nC. ఆల్డోస్టెరాన్\nD. గ్లూకాగాన్\nజాబితా-II:\n1. పీనియల్ గ్రంథి నుండి విడుదలై నిద్ర-మెలకువ జీవ గడియారాన్ని (Circadian Rhythm) నియంత్రిస్తుంది\n2. క్లోమంలోని లాంగర్‌హాన్స్ పుటికల ఆల్ఫా కణాల నుండి స్రవించి రక్తంలో గ్లూకోజ్ స్థాయిని పెంచుతుంది\n3. హైపోథాలమస్‌లో తయారై పృష్ఠ పిట్యూటరీ నుండి విడుదలవుతుంది; దీని లోపం వల్ల 'డయాబెటిస్ ఇన్సిపిడస్' కలుగుతుంది\n4. అడ్రినల్ వల్కలం నుండి స్రవించే ఖనిజ కార్టికాయిడ్; మూత్రపిండ నాళికల్లో సోడియం పునఃశోషణను నియంత్రిస్తుంది\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3"],
        ["A-3, B-1, C-4, D-2", "A-1, B-3, C-4, D-2", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3"],
        0,
        "ADH/Vasopressin comes from posterior pituitary and prevents dilute polyuria (Diabetes Insipidus) (A-3); Melatonin from the pineal gland governs sleep cycles (B-1); Aldosterone from adrenal cortex balances Na+/K+ in nephrons (C-4); Glucagon from pancreatic alpha-cells counterbalances Insulin (D-2).",
        "ADH - పృష్ఠ పిట్యూటరీ/డయాబెటిస్ ఇన్సిపిడస్ (3); మెలటోనిన్ - పీనియల్ గ్రంథి/నిద్ర చక్రం (1); ఆల్డోస్టెరాన్ - అడ్రినల్ వల్కలం/సోడియం సమతుల్యత (4); గ్లూకాగాన్ - క్లోమ ఆల్ఫా కణాలు (2)."
    ),
    # S11 (corr=1: 2 and 3 only; stmt 1 false: claims HIV specifically attacks erythrocytes & B-lymphocytes for humoral immunity while sparing CD4+ Helper T-cells!)
    make_q(
        "Immunology - Adaptive Lymphocytes & Retroviral Pathogenesis",
        "Consider the following statements regarding the human immune system and viral pathogenesis:\n1. The Human Immunodeficiency Virus (HIV) selectively spares CD4+ Helper T-lymphocytes while exclusively infecting red blood cells (erythrocytes) and platelets.\n2. B-lymphocytes mediate 'Humoral Immunity' by differentiating into plasma cells that secrete specific immunoglobulins (antibodies like IgG and IgM), whereas T-lymphocytes drive 'Cell-Mediated Immunity'.\n3. Passive immunity involves transferring pre-formed antibodies directly to the host (such as maternal IgG across the placenta or colostrum IgA to infants), offering immediate but temporary protection.\nWhich of the statements given above are correct?",
        "మానవ రోగనిరోధక వ్యవస్థ మరియు వైరల్ వ్యాధినిరోధకతకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. హెచ్‌ఐవీ (HIV) వైరస్ CD4+ హెల్పర్ T-లింఫోసైట్లపై దాడి చేయకుండా కేవలం ఎర్ర రక్త కణాలు మరియు ప్లేట్‌లెట్లను మాత్రమే నాశనం చేస్తుంది.\n2. B-లింఫోసైట్లు ప్రతిదేహాలను (IgG, IgM వంటి Antibodies) స్రవిస్తూ 'హ్యూమరల్ ఇమ్యూనిటీ' (ద్రవ మాధ్యమ రోగనిరోధకత) అందించగా, T-లింఫోసైట్లు 'సెల్-మీడియేటెడ్ ఇమ్యూనిటీ'ని నిర్వహిస్తాయి.\n3. తల్లి నుండి మాయ ద్వారా శిశువుకు లభించే IgG లేదా తల్లి పాలలోని IgA వంటి ముందుగా తయారైన ప్రతిదేహాలను నేరుగా అందించడాన్ని 'నిష్క్రియ రోగనిరోధకత' (Passive Immunity) అంటారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is false. HIV specifically binds CD4 receptors on Helper T-lymphocytes (and macrophages), progressively depleting CD4+ T-cell counts and crippling both cell-mediated and T-dependent humoral immune responses (leaving the body vulnerable to opportunistic infections like AIDS).",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. హెచ్‌ఐవీ వైరస్ ప్రధానంగా CD4+ హెల్పర్ T-లింఫోసైట్లలోకి ప్రవేశించి వాటి సంఖ్యను క్షీణింపజేస్తుంది, తద్వారా శరీర రోగనిరోధక శక్తి కుప్పకూలుతుంది."
    ),
    # S12 (corr=2: A-4, B-2, C-1, D-3 — Plant Phytohormones Match)
    make_q(
        "Botany & Plant Physiology - Phytohormones Regulators Match",
        "Match the classical plant growth regulators (List-I) with their signature physiological action (List-II):\nList-I:\nA. Auxins (IAA)\nB. Gibberellins (GA3)\nC. Abscisic Acid (ABA)\nD. Ethylene (C2H4)\nList-II:\n1. 'Stress hormone' inducing stomatal closure during drought and enforcing seed dormancy\n2. Promotes internodal stem elongation (bolting in rosette plants) and breaks seed dormancy via amylase induction\n3. Only gaseous phytohormone; accelerates climacteric fruit ripening and leaf/flower senescence\n4. Mediates apical dominance, phototropism, and adventitious root initiation in stem cuttings\nSelect the correct code:",
        "మొక్కల పెరుగుదల నియంత్రకాలను (Phytohormones) (జాబితా-I) వాటి ప్రధాన శరీరధర్మ విధులతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. ఆక్సిన్లు (Auxins - IAA)\nB. జిబ్బరెల్లిన్లు (GA3)\nC. అబ్సిసిక్ ఆమ్లం (ABA)\nD. ఇథిలీన్ (C2H4)\nజాబితా-II:\n1. నీటి ఎద్దడి సమయంలో పత్రరంధ్రాలు మూసుకుపోయేలా చేసి విత్తన సుప్తావస్థను కలిగించే 'ఒత్తిడి హార్మోన్' (Stress Hormone)\n2. కాండం కణుపుల మధ్య పొడవు పెరుగుదలను (Bolting) మరియు విత్తన అంకురోత్పత్తిని ప్రేరేపిస్తుంది\n3. వాయు రూపంలో ఉండే ఏకైక వృక్ష హార్మోన్; పండ్లు త్వరగా పండటానికి తోడ్పడుతుంది\n4. అగ్ర ఆధిక్యత (Apical Dominance), కాంతి అనువర్తనం మరియు అంటు మొక్కలలో వేర్ల ఉత్పత్తిని ప్రోత్సహిస్తుంది\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-4, B-1, C-2, D-3", "A-2, B-4, C-1, D-3", "A-4, B-2, C-1, D-3", "A-3, B-2, C-1, D-4"],
        ["A-4, B-1, C-2, D-3", "A-2, B-4, C-1, D-3", "A-4, B-2, C-1, D-3", "A-3, B-2, C-1, D-4"],
        2,
        "Auxins drive apical dominance & rooting (A-4); Gibberellins trigger bolting & malting (B-2); Abscisic Acid (ABA) triggers drought stomatal closure & dormancy (C-1); and Ethylene is the gaseous ripening hormone (D-3).",
        "ఆక్సిన్లు - అగ్ర ఆధిక్యత/వేర్ల ఉత్పత్తి (4); జిబ్బరెల్లిన్లు - కాండం పొడవు/బోల్టింగ్ (2); అబ్సిసిక్ ఆమ్లం - ఒత్తిడి హార్మోన్ (1); ఇథిలీన్ - పండ్లను పండించే వాయు హార్మోన్ (3)."
    ),
    # S13 (corr=3: 1, 2, and 3 — National Quantum Mission ₹6,003.65 Cr & Qubit Mechanics)
    make_q(
        "Emerging Technologies - Quantum Computing & National Quantum Mission",
        "Consider the following statements regarding Quantum Computing principles and India's National Quantum Mission (NQM):\n1. Unlike classical binary bits restricted strictly to 0 or 1, a 'Qubit' can exist in a coherent linear Superposition of states simultaneously, while 'Entanglement' links the quantum states of two or more qubits across spatial separation.\n2. Approved in 2023 with an outlay of ₹6,003.65 crore through 2030–31, the National Quantum Mission targets developing intermediate-scale quantum computers of 50–1,000 physical qubits.\n3. Four Thematic Hubs (T-Hubs) have been set up under NQM spanning Quantum Computing, Quantum Communication, Quantum Sensing & Metrology, and Quantum Materials & Devices.\nWhich of the statements given above are correct?",
        "క్వాంటమ్ కంప్యూటింగ్ సూత్రాలు మరియు భారత జాతీయ క్వాంటమ్ మిషన్ (NQM) కు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. కేవలం 0 లేదా 1 స్థితిలో మాత్రమే ఉండే సాధారణ బిట్లకు భిన్నంగా, 'క్యూబిట్' (Qubit) 'సూపర్‌పొజిషన్' ద్వారా ఏకకాలంలో రెండు స్థితుల కలయికలో ఉండగలదు; 'ఎన్‌టాంగిల్‌మెంట్' క్యూబిట్ల మధ్య దూరంతో సంబంధం లేని అంతర్గత అనుసంధానాన్ని కల్పిస్తుంది.\n2. 2030–31 వరకు ₹6,003.65 కోట్ల వ్యయంతో ఆమోదించబడిన జాతీయ క్వాంటమ్ మిషన్ 50 నుండి 1,000 క్యూబిట్ల సామర్థ్యం గల క్వాంటమ్ కంప్యూటర్ల అభివృద్ధిని లక్ష్యంగా పెట్టుకుంది.\n3. NQM కింద క్వాంటమ్ కంప్యూటింగ్, క్వాంటమ్ కమ్యూనికేషన్, క్వాంటమ్ సెన్సింగ్ & మెట్రాలజీ మరియు క్వాంటమ్ మెటీరియల్స్ అనే నాలుగు థీమాటిక్ హబ్‌లను (T-Hubs) ఏర్పాటు చేశారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. Led by the Department of Science & Technology (DST), NQM (2023–31, ₹6,003.65 crore) funds 4 thematic T-Hubs hosted at premier institutes (IISc Bengaluru, IIT Madras/C-DOT, IIT Bombay, IIT Delhi) to develop 50–1,000 qubit platforms and 2,000-km QKD networks.",
        "మూడు ప్రకటనలూ సరైనవే. సూపర్‌పొజిషన్, ఎన్‌టాంగిల్‌మెంట్ క్వాంటమ్ కంప్యూటింగ్‌కు ఆధారం. ₹6,003.65 కోట్లతో 2030-31 వరకు అమలయ్యే NQM కింద 4 థీమాటిక్ హబ్‌లను ఏర్పాటు చేశారు."
    ),
    # S14 (corr=3: 1, 2, and 3 — Forensic Science & Digital Evidence)
    make_q(
        "Forensic Science & Cyber Policing - DNA Profiling & Digital Evidence",
        "Consider the following statements regarding forensic science techniques utilized in criminal investigation:\n1. Forensic DNA profiling predominantly analyzes Short Tandem Repeats (STRs)—highly polymorphic non-coding DNA regions—because their repeat lengths vary uniquely across unrelated individuals (except identical monozygotic twins).\n2. Mitochondrial DNA (mtDNA) analysis is valuable in severely degraded skeletal/hair-shaft samples where nuclear DNA is absent, tracing unbroken maternal lineage.\n3. In digital forensics, a forensic disk image generated using a hardware write-blocker preserves bit-for-bit integrity, verified through cryptographic hash algorithms like SHA-256 for chain-of-custody authentication.\nWhich of the statements given above are correct?",
        "నేర పరిశోధనలో ఉపయోగించే ఫోరెన్సిక్ సైన్స్ మరియు డిజిటల్ ఫోరెన్సిక్ పద్ధతులకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఫోరెన్సిక్ DNA ప్రొఫైలింగ్‌లో ప్రధానంగా 'షార్ట్ టాండెం రిపీట్స్' (STRs) ను విశ్లేషిస్తారు; కవలలు (Monozygotic Twins) మినహా ప్రతి వ్యక్తిలో వీటి సంఖ్య ప్రత్యేకంగా ఉంటుంది.\n2. ఎముకలు లేదా వెంట్రుకల వంటి క్షీణించిన నమూనాలలో కేంద్రక DNA లభించనప్పుడు, మైటోకాండ్రియల్ DNA (mtDNA) పరీక్ష ద్వారా తల్లి వైపు వంశపారంపర్య గుర్తింపును నిర్ధారించవచ్చు.\n3. డిజిటల్ ఫోరెన్సిక్స్‌లో రైట్-బ్లాకర్ (Write-Blocker) సహాయంతో అసలు డేటా మారకుండా తీసుకున్న డిస్క్ ఇమేజ్ ప్రామాణికతను SHA-256 వంటి క్రిప్టోగ్రాఫిక్ హ్యాష్ అల్గారిథమ్‌ల ద్వారా నిర్ధారిస్తారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. STR autosomal markers underpin standard CODIS/Indian DNA forensic databases; mtDNA passes exclusively maternally without recombination in high-copy organelles; and SHA-256 hash digests guarantee digital chain-of-custody under BSA Section 63.",
        "మూడు ప్రకటనలూ సరైనవే. DNA ఫింగర్‌ప్రింటింగ్‌లో STR విధానాన్ని, శిథిలమైన నమూనాలకు తల్లి వైపు mtDNA ను మరియు సైబర్ నేర పరిశోధనలో రైట్-బ్లాకర్ + SHA-256 హ్యాష్ ధృవీకరణను ఉపయోగిస్తారు."
    ),
]

# ==================== 7. CURRENT AFFAIRS 2025-26 NEW (12) ====================
# Balance target: {0: 3, 1: 3, 2: 2, 3: 4}
NEW_CURRENT_AFFAIRS = [
    # CA1 (corr=3: 1, 2, and 3 — Verified Union Budget 2026-27)
    make_q(
        "Current Affairs 2026 - Union Budget 2026–27 Fiscal Framework",
        "Consider the following statements regarding India's Union Budget 2026–27 presented by Finance Minister Nirmala Sitharaman:\n1. Public Capital Expenditure (CapEx) outlay was stepped up to ₹12.2 lakh crore (roughly 3.1% of GDP), up from ₹11.2 lakh crore in BE 2025–26, prioritizing infrastructure and strategic sectors.\n2. The Fiscal Deficit target for FY 2026–27 was pegged lower at 4.3% of GDP (down from 4.4% in RE 2025–26), alongside projecting the Central debt-to-GDP ratio at 55.6%.\n3. Under direct tax reforms aligned with the New Income Tax Act, 2025 taking effect from April 2026, personal income tax slabs remained unchanged while foreign providers offering global cloud services via Indian data centres received a tax holiday up to 2047.\nWhich of the statements given above are correct?",
        "కేంద్ర ఆర్థిక మంత్రి నిర్మలా సీతారామన్ ప్రవేశపెట్టిన కేంద్ర బడ్జెట్ 2026–27 కు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 2026–27 బడ్జెట్‌లో ప్రభుత్వ మూలధన వ్యయం (CapEx) కేటాయింపును జీడీపీలో సుమారు 3.1 శాతంగా ఉన్న ₹12.2 లక్షల కోట్లకు పెంచారు.\n2. ఆర్థిక సంవత్సరం 2026–27 కోసం ద్రవ్యలోటు (Fiscal Deficit) లక్ష్యాన్ని 2025–26 RE (4.4%) నుండి తగ్గించి జీడీపీలో 4.3% గా, మరియు రుణ-జీడీపీ నిష్పత్తిని 55.6% గా అంచనా వేశారు.\n3. ఏప్రిల్ 2026 నుండి అమలయ్యే నూతన ఆదాయపు పన్ను చట్టం-2025 నేపథ్యంలో వ్యక్తిగత ఆదాయపు పన్ను శ్లాబులను యథాతథంగా ఉంచి, భారతీయ డేటా సెంటర్ల ద్వారా గ్లోబల్ క్లౌడ్ సేవలందించే విదేశీ సంస్థలకు 2047 వరకు పన్ను మినహాయింపు కల్పించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are verified highlights of the Union Budget 2026–27: ₹12.2 lakh crore CapEx (Effective CapEx ₹17.15 lakh crore), Fiscal Deficit 4.3% of GDP, Debt-to-GDP 55.6%, unchanged personal IT slabs under the April 2026 New Income Tax Act, and a cloud data-centre tax holiday until 2047.",
        "మూడు ప్రకటనలూ సరైనవే. 2026–27 కేంద్ర బడ్జెట్‌లో ₹12.2 లక్షల కోట్ల CapEx, 4.3% ద్రవ్యలోటు, 55.6% రుణ నిష్పత్తి మరియు భారతీయ డేటా సెంటర్లకు 2047 వరకు పన్ను మినహాయింపు ప్రకటించబడ్డాయి."
    ),
    # CA2 (corr=0: 1 and 2 only; stmt 3 false: claims Fiscal Deficit targeted at 5.5% of GSDP whereas Telangana Budget 2026-27 targeted 3.0% of GSDP!)
    make_q(
        "Current Affairs 2026 - Telangana State Budget 2026–27 Outlay",
        "Consider the following statements regarding the Telangana State Budget for FY 2026–27:\n1. The total Budget outlay stood at ₹3,24,234 crore, estimating a comfortable Revenue Surplus of ₹6,857.76 crore (Revenue Receipts of ₹2,41,263.58 crore vs Revenue Expenditure of ₹2,34,405.82 crore).\n2. Capital Expenditure was raised to ₹47,267.28 crore, while ₹50,713 crore was earmarked for the Six Guarantee welfare schemes (including ₹18,000 crore for Rythu Bharosa and ₹14,861 crore for Cheyutha pensions).\n3. The State projected a Fiscal Deficit exceeding 5.5% of GSDP, deliberately breaching the 3.0% FRBM ceiling benchmark.\nWhich of the statements given above are correct?",
        "తెలంగాణ రాష్ట్ర బడ్జెట్ 2026–27 అంచనాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. రాష్ట్ర మొత్తం బడ్జెట్ వ్యయం ₹3,24,234 కోట్లు కాగా, ₹2,41,263.58 కోట్ల రెవెన్యూ రాబడితో ₹6,857.76 కోట్ల మిగులు రెవెన్యూ బడ్జెట్ (Revenue Surplus) ను అంచనా వేశారు.\n2. మూలధన వ్యయాన్ని ₹47,267.28 కోట్లకు పెంచడంతో పాటు ఆరు గ్యారెంటీ పథకాల కోసం ₹50,713 కోట్లు (రైతు భరోసా ₹18,000 కోట్లు, చేయూత పెన్షన్లకు ₹14,861 కోట్లు సహా) కేటాయించారు.\n3. రాష్ట్ర FRBM పరిమితిని అధిగమిస్తూ జీఎస్డీపీలో 5.5 శాతానికి పైగా ద్రవ్యలోటును బడ్జెట్‌లో లక్ష్యంగా నిర్దేశించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is false. The Telangana Budget 2026–27 pegged the Fiscal Deficit strictly at 3.0% of GSDP (approx. ₹58,459 crore), staying aligned with statutory FRBM ceiling norms.",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. 2026–27 తెలంగాణ బడ్జెట్‌లో ద్రవ్యలోటును FRBM పరిమితికి లోబడి జీఎస్డీపీలో 3.0% (సుమారు ₹58,459 కోట్లు) గా నిర్ణయించారు."
    ),
    # CA3 (corr=1: 2 and 3 only; stmt 1 false: says SpaDeX made India the 2nd nation instead of 4th nation behind US, Russia, China!)
    make_q(
        "Current Affairs 2025–26 - ISRO Space Milestones (SpaDeX, NISAR & NVS-03)",
        "Consider the following statements regarding ISRO's landmark missions across 2025 and 2026:\n1. With the autonomous orbital rendezvous and docking achieved by the SpaDeX twin-satellite mission (launched aboard PSLV-C60), India became only the second nation in the world after the United States to master space docking.\n2. Launched on July 30, 2025 aboard GSLV-F16, the joint NASA-ISRO NISAR satellite deploys dual L-band and S-band synthetic aperture radar to map global biomass, ecosystems, and earth deformation.\n3. Launched on October 30, 2026 via GSLV-F18, the second-generation navigation satellite NVS-03 strengthened the NavIC constellation with indigenous rubidium atomic clocks and civilian L1 signals.\nWhich of the statements given above are correct?",
        "2025 మరియు 2026లలో ఇస్రో (ISRO) సాధించిన అంతరిక్ష మైలురాళ్లకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. PSLV-C60 ద్వారా ప్రయోగించిన 'స్పాడెక్స్' (SpaDeX) మిషన్ అంతరిక్షంలో ఉపగ్రహాల అనుసంధానం (Docking) సాధించడంతో అమెరికా తర్వాత ఈ ఘనత సాధించిన ప్రపంచంలోనే రెండవ దేశంగా భారత్ నిలిచింది.\n2. జూలై 30, 2025న GSLV-F16 ద్వారా ప్రయోగించబడిన నాసా-ఇస్రో ఉమ్మడి 'నిసార్' (NISAR) ఉపగ్రహం L-బ్యాండ్ మరియు S-బ్యాండ్ రాడార్లతో భూమి జీవవైవిధ్యం మరియు భౌగోళిక మార్పులను కొలుస్తుంది.\n3. అక్టోబర్ 30, 2026న GSLV-F18 ద్వారా విజయవంతంగా ప్రయోగించిన రెండవ తరం నావిగేషన్ ఉపగ్రహం NVS-03 స్వదేశీ రుబిడియం అటామిక్ గడియారాలతో నావిక్ (NavIC) వ్యవస్థను బలోపేతం చేసింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is false. SpaDeX made India the FOURTH nation globally (after the United States, Russia/USSR, and China) to achieve autonomous orbital docking. NISAR (July 30, 2025 on GSLV-F16) and NVS-03 (October 30, 2026 on GSLV-F18) are major recent triumphs.",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. స్పాడెక్స్ విజయంతో అమెరికా, రష్యా మరియు చైనా తర్వాత అంతరిక్షంలో డాకింగ్ సాధించిన నాలుగవ దేశంగా భారతదేశం నిలిచింది (రెండవది కాదు)."
    ),
    # CA4 (corr=2: 1 and 3 only; stmt 2 false: attributes 2026 Physics Nobel to Clarke/Devoret/Martinis [who won 2025 Physics], instead of Francis Halzen for IceCube neutrinos!)
    make_q(
        "Current Affairs 2025–26 - Nobel Prize Laureates & Discoveries",
        "Consider the following statements regarding the 2025 and 2026 Nobel Prize awards:\n1. The 2026 Nobel Prize in Physiology or Medicine was awarded jointly to Karl Deisseroth, Peter Hegemann, and Georg Nagel for their discoveries concerning light-gated ion channels and optogenetics.\n2. The 2026 Nobel Prize in Physics recognized John Clarke, Michel H. Devoret, and John M. Martinis for high-energy neutrino astronomy at the IceCube Observatory.\n3. The 2025 Nobel Prize in Chemistry honoured Susumu Kitagawa, Richard Robson, and Omar M. Yaghi for developing Metal-Organic Frameworks (MOFs), while Anne Carson received the 2026 Literature Prize.\nWhich of the statements given above are correct?",
        "2025 మరియు 2026 నోబెల్ బహుమతి విజేతలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 2026 వైద్య శాస్త్ర నోబెల్ బహుమతిని కార్ల్ డైసెరోత్, పీటర్ హెగెమాన్ మరియు జార్జ్ నాగెల్‌లకు 'ఆప్టోజెనెటిక్స్' మరియు లైట్-గేటెడ్ అయాన్ ఛానళ్ల పరిశోధనలకు ప్రదానం చేశారు.\n2. 2026 భౌతిక శాస్త్ర నోబెల్ బహుమతిని ఐస్‌క్యూబ్ న్యూట్రినో అబ్జర్వేటరీ ఆవిష్కరణలకు గాను జాన్ క్లార్క్, మిచెల్ హెచ్. డెవోరెట్ మరియు జాన్ ఎం. మార్టినిస్‌లకు ఇచ్చారు.\n3. 2025 రసాయన శాస్త్ర నోబెల్ 'మెటల్-ఆర్గానిక్ ఫ్రేమ్‌వర్క్స్' (MOFs) కు గాను సుసుము కిటగావా, రిచర్డ్ రాబ్సన్, ఒమర్ యాగీలకు లభించగా, 2026 సాహిత్య నోబెల్ ఆన్ కార్సన్‌కు లభించింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is mixed up. The 2026 Physics Nobel was awarded to Francis Halzen for decisive contributions to the IceCube Neutrino Observatory and high-energy astrophysical neutrinos, whereas John Clarke, Michel Devoret, and John Martinis won the 2025 Physics Nobel for macroscopic quantum mechanical tunnelling.",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. 2026 భౌతిక శాస్త్ర నోబెల్ బహుమతిని ఐస్‌క్యూబ్ న్యూట్రినో పరిశోధనకు గాను 'ఫ్రాన్సిస్ హాల్జెన్' పొందారు; జాన్ క్లార్క్ త్రయానికి 2025 లో క్వాంటమ్ టన్నెలింగ్‌పై బహుమతి లభించింది."
    ),
    # CA5 (corr=3: 1, 2, and 3 — Verified Padma Awards 2026 + Republic Day 2026 Chief Guests)
    make_q(
        "Current Affairs 2026 - Padma Awards & Republic Day Diplomacy",
        "Consider the following statements regarding India's 2026 Republic Day celebrations and Padma Awards:\n1. On India's 77th Republic Day (January 26, 2026), European Council President António Costa and European Commission President Ursula von der Leyen graced Kartavya Path as joint Chief Guests.\n2. Five distinguished personalities received the Padma Vibhushan in 2026: Dharmendra Singh Deol (Posthumous), Justice (Retd.) K.T. Thomas, Dr. N. Rajam, P. Narayanan, and V.S. Achuthanandan (Posthumous).\n3. Notable 2026 Padma Shri awardees from Telangana included Kuchipudi exponent Deepika Reddy, CCMB scientist Dr. Kumarasamy Thangaraj, and noted physicians Dr. Guduru Venkata Rao and Dr. Palakonda Vijay Anand Reddy.\nWhich of the statements given above are correct?",
        "2026 భారత గణతంత్ర దినోత్సవం మరియు పద్మ పురస్కారాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. జనవరి 26, 2026న 77వ గణతంత్ర దినోత్సవ వేడుకలకు యూరోపియన్ కౌన్సిల్ అధ్యక్షుడు ఆంటోనియో కోస్టా మరియు యూరోపియన్ కమిషన్ అధ్యక్షురాలు ఉర్సులా వాన్ డెర్ లేయెన్ సంయుక్త ముఖ్య అతిథులుగా హాజరయ్యారు.\n2. 2026లో ధర్మేంద్ర సింగ్ డియోల్ (మరణానంతరం), జస్టిస్ కె.టి. థామస్, డాక్టర్ ఎన్. రాజం, పి. నారాయణన్ మరియు వి.ఎస్. అచ్యుతానందన్ (మరణానంతరం) లకు పద్మవిభూషణ్ ప్రదానం చేయబడింది.\n3. తెలంగాణ నుండి 2026లో కూచిపూడి నృత్యకారిణి దీపికా రెడ్డి, CCMB శాస్త్రవేత్త డాక్టర్ కుమారస్వామి తంగరాజ్, మరియు వైద్యులు డాక్టర్ గూడూరు వెంకటరావు, డాక్టర్ పాలకొండ విజయ్ ఆనంద్ రెడ్డిలకు పద్మశ్రీ అవార్డులు లభించాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. EU leaders António Costa and Ursula von der Leyen served as Chief Guests for Republic Day 2026, five eminent figures received Padma Vibhushan 2026, and Deepika Reddy, Dr. Kumarasamy Thangaraj, Dr. Guduru Venkata Rao, and Dr. P. Vijay Anand Reddy received Padma Shri honors from Telangana.",
        "మూడు ప్రకటనలూ సరైనవే. 77వ గణతంత్ర దినోత్సవ ముఖ్య అతిథులుగా ఈయూ అగ్రనేతలు హాజరుకాగా, 2026 పద్మవిభూషణ్ ఐదుగురికి మరియు తెలంగాణ నుండి దీపికా రెడ్డి, డాక్టర్ తంగరాజ్, డాక్టర్ వెంకటరావు, డాక్టర్ విజయ్ ఆనంద్ రెడ్డిలకు పద్మశ్రీ పురస్కారాలు లభించాయి."
    ),
    # CA6 (corr=0: 1 and 2 only; stmt 3 false: claims MILAN 2026 was held at Kochi jointly as a NATO Arctic exercise instead of Visakhapatnam Bay of Bengal with IFR/IONS!)
    make_q(
        "Current Affairs 2026 - Exercise MILAN 2026 & Indigenous Defence Policy",
        "Consider the following statements regarding India's naval diplomacy and defence self-reliance in 2026:\n1. The 13th edition of the Indian Navy's multilateral exercise 'MILAN 2026'—hosted alongside the International Fleet Review (IFR 2026) and IONS Conclave of Chiefs under the theme 'Camaraderie, Cooperation, Collaboration'—witnessed participation from over 70 nations.\n2. To accelerate domestic private participation, the Government of India approved full Transfer of Technology (ToT) of all DRDO-developed conventional missile systems to qualified Indian firms and opened 24 DRDO laboratories to private testing.\n3. MILAN 2026 was conducted exclusively at the Southern Naval Command in Kochi alongside Arctic icebreakers, excluding India's indigenous aircraft carrier INS Vikrant.\nWhich of the statements given above are correct?",
        "2026లో భారత రక్షణ స్వావలంబన మరియు నావికాదళ విన్యాసాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 'కామ్రేడరీ, కోఆపరేషన్, కొలాబరేషన్' ఇతివృత్తంతో జరిగిన 13వ బహుపాక్షిక నావికా విన్యాసం 'మిలాన్ 2026' (ఇంటర్నేషనల్ ఫ్లీట్ రివ్యూ మరియు IONS కాంక్లేవ్‌తో కలిపి) లో 70 కి పైగా దేశాలు పాల్గొన్నాయి.\n2. రక్షణ రంగంలో దేశీయ ప్రైవేట్ సంస్థలను ప్రోత్సహించేందుకు DRDO అభివృద్ధి చేసిన అన్ని సంప్రదాయ క్షిపణి వ్యవస్థల టెక్నాలజీ బదిలీకి (ToT) కేంద్రం ఆమోదం తెలపడంతో పాటు 24 DRDO ల్యాబ్‌లను ప్రైవేట్ సంస్థలకు అందుబాటులోకి తెచ్చింది.\n3. మిలాన్ 2026 విన్యాసం స్వదేశీ విమాన వాహక నౌక INS విక్రాంత్ భాగస్వామ్యం లేకుండా కేవలం కొచ్చిలోని సదరన్ నేవల్ కమాండ్ వద్ద మాత్రమే నిర్వహించబడింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is false. MILAN 2026 and IFR 2026 were hosted in February 2026 at VISAKHAPATNAM (Eastern Naval Command) with the Bay of Bengal Sea Phase centered prominently around India's indigenous aircraft carrier INS Vikrant.",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. మిలాన్ 2026 విన్యాసం ఫిబ్రవరి 2026లో విశాఖపట్నంలో (బంగాళాఖాతం) నిర్వహించబడింది మరియు స్వదేశీ నౌక INS విక్రాంత్ దీనికి కేంద్రబిందువుగా నిలిచింది."
    ),
    # CA7 (corr=1: 2 and 3 only; stmt 1 false: reverses CURE vs RARE in Telangana Rising 2047!)
    make_q(
        "Current Affairs 2026 - Telangana Rising 2047 & Tier-2 Tech Expansion",
        "Consider the following statements regarding Telangana's economic roadmap 'Telangana Rising 2047' and regional decentralization initiatives in 2026:\n1. Under the spatial economic framework, 'CURE' denotes the rural agricultural economy beyond the Regional Ring Road (RRR), while 'RARE' refers to the inner city area within Hyderabad's Outer Ring Road (ORR).\n2. Telangana Rising 2047 targets transforming Telangana into a $1 trillion GSDP economy by 2034 and a $3 trillion economy by 2047, with 'PURE' spanning the peri-urban growth belt between ORR and RRR.\n3. Advancing northern Telangana tech decentralization, the State Government inaugurated a ₹57.85-crore IT Tower at Adilabad in November 2026 equipped with an integrated TASK skilling hub and backed by a planned 3,000-acre industrial corridor.\nWhich of the statements given above are correct?",
        "తెలంగాణ ప్రభుత్వ 'తెలంగాణ రైజింగ్ 2047' ఆర్థిక ప్రణాళిక మరియు ప్రాంతీయ అభివృద్ధికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ప్రాదేశిక ఆర్థిక నమూనా ప్రకారం RRR వెలుపలి గ్రామీణ వ్యవసాయ ప్రాంతాన్ని 'CURE' గా, మరియు ORR లోపలి హైదరాబాద్ కోర్ పట్టణ ప్రాంతాన్ని 'RARE' గా వర్గీకరించారు.\n2. 2034 నాటికి $1 ట్రిలియన్ మరియు 2047 నాటికి $3 ట్రిలియన్ ఆర్థిక వ్యవస్థను లక్ష్యంగా చేసుకున్న ఈ ప్రణాళికలో ORR-RRR మధ్య ప్రాంతాన్ని పెరి-అర్బన్ జోన్ (PURE) గా నిర్దేశించారు.\n3. ద్వితీయ శ్రేణి నగరాల ఐటీ విస్తరణలో భాగంగా నవంబర్ 2026లో ఆదిలాబాద్‌లో ₹57.85 కోట్ల వ్యయంతో నూతన ఐటీ టవర్ మరియు TASK నైపుణ్య కేంద్రాన్ని ప్రారంభించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 reverses the acronyms. In Telangana Rising 2047, CURE = Core Urban Region Economy (inside ORR); PURE = Peri-Urban Region Economy (between ORR and RRR); and RARE = Rural Agri Region Economy (beyond RRR).",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తారుమారైంది. తెలంగాణ రైజింగ్ 2047లో CURE అనగా ORR లోపలి కోర్ అర్బన్ జోన్ మరియు RARE అనగా RRR వెలుపలి గ్రామీణ వ్యవసాయ జోన్."
    ),
    # CA8 (corr=2: 1 and 3 only; stmt 2 false: says China hosted 2026 G20 Summit instead of the United States in Miami!)
    make_q(
        "Current Affairs 2026 - BRICS, G20 & COP31 Global Summits",
        "Consider the following statements regarding major multilateral summits hosted in 2026:\n1. Holding the BRICS Chairship for 2026, India hosted the 18th BRICS Summit in New Delhi (September 2026) under the theme 'Building for Resilience, Innovation, Cooperation and Sustainability'.\n2. Following South Africa's 2025 presidency, China hosted the 2026 G20 Leaders' Summit in Shanghai in November 2026.\n3. Under a joint residency and leadership arrangement, Türkiye hosted the UN Climate Change Conference (COP31) in Antalya, while Australia assumed leadership of the formal climate negotiations.\nWhich of the statements given above are correct?",
        "2026లో జరిగిన ప్రధాన అంతర్జాతీయ సదస్సులకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 2026 బ్రిక్స్ (BRICS) అధ్యక్ష బాధ్యతలను నిర్వహించిన భారతదేశం సెప్టెంబర్ 2026లో న్యూఢిల్లీలో 18వ బ్రిక్స్ శిఖరాగ్ర సదస్సును నిర్వహించింది.\n2. 2025లో దక్షిణాఫ్రికా అధ్యక్షత తర్వాత, 2026 G20 నేతల శిఖరాగ్ర సదస్సును చైనాలోని షాంఘైలో నిర్వహించారు.\n3. సంయుక్త భాగస్వామ్య ఒప్పందం ప్రకారం తుర్కియే (Türkiye) అంతాల్యాలో ఐక్యరాజ్యసమితి వాతావరణ సదస్సు (COP31) కు ఆతిథ్యం ఇవ్వగా, ఆస్ట్రేలియా అధికారిక చర్చలకు నాయకత్వం వహించింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        2,
        "Statements 1 and 3 are correct, while Statement 2 is false. The United States held the 2026 G20 Presidency and hosted the G20 Leaders' Summit in Miami, Florida (not China).",
        "ప్రకటనలు 1 మరియు 3 సరైనవి, కానీ ప్రకటన 2 తప్పు. 2026 G20 శిఖరాగ్ర సదస్సుకు చైనా కాకుండా అమెరికా (మయామి, ఫ్లోరిడా) ఆతిథ్యం ఇచ్చింది."
    ),
    # CA9 (corr=3: 1, 2, and 3 — Verified 20th Asian Games Aichi-Nagoya 2026 & 46th Chess Olympiad 2026 Samarkand!)
    make_q(
        "Current Affairs 2026 - Asian Games Aichi-Nagoya & Chess Olympiad Samarkand",
        "Consider the following statements regarding India's international sporting performances in 2026:\n1. At the 20th Asian Games hosted by Aichi Prefecture and Nagoya, Japan (September–October 2026), India finished 4th overall in the medal standings with 85 total medals (21 Gold, 27 Silver, and 37 Bronze).\n2. At the 46th FIDE Chess Olympiad held in Samarkand, Uzbekistan, India secured the Silver medal in the Open section (behind Gold medallist Uzbekistan) and Bronze in the Women's section (won by China).\n3. Building upon its overall consistency across both Open and Women's sections at the Samarkand Olympiad, India retained the prestigious Nona Gaprindashvili Cup.\nWhich of the statements given above are correct?",
        "2026లో అంతర్జాతీయ క్రీడలలో భారతదేశ ప్రదర్శనకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. జపాన్‌లోని ఐచి-నగోయాలో జరిగిన 20వ ఆసియా క్రీడలు (సెప్టెంబర్–అక్టోబర్ 2026) లో భారతదేశం 21 స్వర్ణ, 27 రజత, 37 కాంస్య పతకాలతో మొత్తం 85 పతకాలు గెలుచుకుని 4వ స్థానంలో నిలిచింది.\n2. ఉజ్బెకిస్తాన్‌లోని సమర్‌కండ్‌లో జరిగిన 46వ ఫైడ్ (FIDE) చెస్ ఒలింపియాడ్‌లో భారతదేశం ఓపెన్ విభాగంలో రజత పతకాన్ని (ఉజ్బెకిస్తాన్ స్వర్ణం), మహిళల విభాగంలో కాంస్య పతకాన్ని (చైనా స్వర్ణం) సాధించింది.\n3. ఓపెన్ మరియు మహిళల విభాగాలలో అత్యుత్తమ సమష్టి ప్రదర్శనకు ఇచ్చే ప్రతిష్టాత్మక 'నోనా గప్రిందాష్విలి కప్' ను భారతదేశం నిలబెట్టుకుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        3,
        "All three statements are correct. India ended 4th at the 2026 Aichi-Nagoya Asian Games (21G-27S-37B = 85 medals) and won Open Silver + Women's Bronze while defending the Nona Gaprindashvili Cup at the 46th Chess Olympiad in Samarkand.",
        "మూడు ప్రకటనలూ సరైనవే. 2026 ఐచి-నగోయా ఆసియా క్రీడలలో భారత్ 85 పతకాలతో 4వ స్థానాన్ని పొందింది. సమర్‌కండ్ చెస్ ఒలింపియాడ్‌లో ఓపెన్ రజతం, మహిళల కాంస్యంతో పాటు నోనా గప్రిందాష్విలి కప్‌ను నిలబెట్టుకుంది."
    ),
    # CA10 (corr=0: 1 and 2 only; stmt 3 false: claims Rajinikanth won the 72nd National Film Awards Dadasaheb Phalke Honor instead of Kannada legend Anant Nag!)
    make_q(
        "Current Affairs 2025–26 - Literary & Cinema Honours",
        "Consider the following statements regarding major literary and cinema honours conferred across 2025–2026:\n1. In May 2026, *Taiwan Travelogue*, written by Taiwanese author Yáng Shuāng-zǐ and translated by Lin King, won the International Booker Prize, becoming the first Mandarin Chinese work translated to clinch the honour.\n2. Veteran Hindi writer Vinod Kumar Shukla received the 59th Jnanpith Award, while noted Tamil poet and lyricist R. Vairamuthu was honoured with the 60th Jnanpith Award.\n3. At the 72nd National Film Awards ceremony, actor Rajinikanth was newly conferred the prestigious Dadasaheb Phalke Award (following Mohanlal's earlier 2023 cycle honour).\nWhich of the statements given above are correct?",
        "2025–26లో ప్రదానం చేయబడిన ప్రముఖ సాహిత్య మరియు సినిమా పురస్కారాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. మే 2026లో యాంగ్ షువాంగ్-జి రచించి, లిన్ కింగ్ ఆంగ్లంలోకి అనువదించిన 'తైవాన్ ట్రావెలాగ్' (Taiwan Travelogue) నవల అంతర్జాతీయ బుకర్ బహుమతిని గెలుచుకుని మాండరిన్ చైనీస్ భాషలో తొలిసారి ఈ ఘనత సాధించింది.\n2. 59వ జ్ఞానపీఠ పురస్కారాన్ని ప్రముఖ హిందీ రచయిత వినోద్ కుమార్ శుక్లా అందుకోగా, 60వ జ్ఞానపీఠ పురస్కారానికి తమిళ కవి ఆర్. వైరముత్తు ఎంపికయ్యారు.\n3. మోహన్‌లాల్ తర్వాత 72వ జాతీయ చలనచిత్ర అవార్డులలో ప్రతిష్టాత్మక దాదాసాహెబ్ ఫాల్కే అవార్డును సూపర్‌స్టార్ రజనీకాంత్‌కు ప్రదానం చేశారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        0,
        "Statements 1 and 2 are correct, while Statement 3 is false. Following Mohanlal (2023 cycle awardee), the prestigious Dadasaheb Phalke Award at the 72nd National Film Awards was conferred upon veteran Kannada actor Anant Nag (Rajinikanth had received the 51st award earlier in 2021).",
        "ప్రకటనలు 1 మరియు 2 సరైనవి, కానీ ప్రకటన 3 తప్పు. 72వ జాతీయ చలనచిత్ర అవార్డులలో దాదాసాహెబ్ ఫాల్కే పురస్కారాన్ని ప్రముఖ కన్నడ నటుడు 'అనంత్ నాగ్' పొందారు (రజనీకాంత్ కాదు)."
    ),
    # CA11 (corr=1: 2 and 3 only; stmt 1 false: claims India reached only 75 Ramsar sites as of Nov 2026 when it actually hit 103!)
    make_q(
        "Current Affairs 2026 - Wetland Conservation & India's Ramsar Milestone",
        "Consider the following statements regarding India's Ramsar Wetlands of International Importance as of November 2026:\n1. By November 2026, India's total tally of designated Ramsar sites stood strictly capped at 75 wetlands with no new additions since 2022.\n2. India ranks first in Asia and third globally in total number of designated Ramsar Wetlands of International Importance.\n3. With the addition of Sukhna Wetland (Chandigarh) and Sauj Jheel (Uttar Pradesh), India crossed the landmark threshold of 103 designated Ramsar Sites by November 2026.\nWhich of the statements given above are correct?",
        "నవంబర్ 2026 నాటికి భారతదేశంలోని అంతర్జాతీయ ప్రాముఖ్యత గల రామ్‌సర్ చిత్తడి నేలలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. నవంబర్ 2026 నాటికి భారతదేశంలో 2022 తర్వాత ఎటువంటి కొత్త చేరికలు లేకుండా కేవలం 75 రామ్‌సర్ ప్రదేశాలు మాత్రమే ఉన్నాయి.\n2. మొత్తం రామ్‌సర్ చిత్తడి నేలల సంఖ్య పరంగా భారతదేశం ఆసియాలో మొదటి స్థానంలో మరియు ప్రపంచంలో మూడవ స్థానంలో నిలిచింది.\n3. చండీగఢ్‌లోని సుఖ్నా చిత్తడి నేల మరియు ఉత్తరప్రదేశ్‌లోని సౌజ్ జీల్ (Sauj Jheel) చేరికతో నవంబర్ 2026 నాటికి భారతదేశంలోని మొత్తం రామ్‌సర్ ప్రదేశాల సంఖ్య 103 కు చేరుకుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        1,
        "Statements 2 and 3 are correct, while Statement 1 is outdated and incorrect. Following the recent additions including Sukhna Wetland (Chandigarh) and Sauj Jheel (Uttar Pradesh), India reached 103 Ramsar Sites as of November 2026, holding 1st rank in Asia and 3rd globally (behind the UK and Mexico).",
        "ప్రకటనలు 2 మరియు 3 సరైనవి, కానీ ప్రకటన 1 తప్పు. సుఖ్నా మరియు సౌజ్ జీల్ చేరికతో నవంబర్ 2026 నాటికి భారతదేశంలోని రామ్‌సర్ ప్రదేశాల సంఖ్య 103 కు పెరిగింది (ఆసియాలో 1వ, ప్రపంచంలో 3వ స్థానం)."
    ),
    # CA12 (corr=3: A-4, B-2, C-1, D-3 — Verified Key Constitutional & Statutory Heads 2025-26)
    make_q(
        "Current Affairs 2026 - Constitutional & Statutory Heads Match",
        "Match the eminent incumbents serving in India's apex constitutional and statutory institutions during 2025–2026 (List-I) with their exact designations (List-II):\nList-I:\nA. Justice Surya Kant\nB. Gyanesh Kumar\nC. Sanjay Malhotra\nD. Dr. Arvind Panagariya\nList-II:\n1. 26th Governor of the Reserve Bank of India (RBI)\n2. 26th Chief Election Commissioner (CEC) of India\n3. Chairman of the 16th Finance Commission of India\n4. 53rd Chief Justice of India (succeeded Justice B.R. Gavai in Nov 2025)\nSelect the correct code:",
        "2025–2026 కాలంలో భారతదేశ అత్యున్నత రాజ్యాంగ మరియు చట్టబద్ధ పదవులలో ఉన్న ప్రముఖులను (జాబితా-I) వారి హోదాలతో (జాబితా-II) జతపరచండి:\nజాబితా-I:\nA. జస్టిస్ సూర్యకాంత్\nB. జ్ఞానేష్ కుమార్\nC. సంజయ్ మల్హోత్రా\nD. డాక్టర్ అరవింద్ పనగరియా\nజాబితా-II:\n1. 26వ భారత రిజర్వ్ బ్యాంక్ (RBI) గవర్నర్\n2. 26వ భారత ప్రధాన ఎన్నికల కమిషనర్ (CEC)\n3. 16వ కేంద్ర ఆర్థిక సంఘం చైర్మన్\n4. 53వ భారత ప్రధాన న్యాయమూర్తి (నవంబర్ 2025లో జస్టిస్ బి.ఆర్. గవాయ్ తర్వాత బాధ్యతలు చేపట్టారు)\nసరైన కోడ్‌ను ఎంచుకోండి:",
        ["A-4, B-1, C-2, D-3", "A-2, B-4, C-1, D-3", "A-4, B-2, C-3, D-1", "A-4, B-2, C-1, D-3"],
        ["A-4, B-1, C-2, D-3", "A-2, B-4, C-1, D-3", "A-4, B-2, C-3, D-1", "A-4, B-2, C-1, D-3"],
        3,
        "Justice Surya Kant took oath as the 53rd Chief Justice of India in November 2025 (A-4); Gyanesh Kumar serves as the 26th Chief Election Commissioner (B-2); Sanjay Malhotra serves as the 26th Governor of the RBI (C-1); and Dr. Arvind Panagariya chairs the 16th Finance Commission (D-3).",
        "జస్టిస్ సూర్యకాంత్ - 53వ ప్రధాన న్యాయమూర్తి (4); జ్ఞానేష్ కుమార్ - 26వ ప్రధాన ఎన్నికల కమిషనర్ (2); సంజయ్ మల్హోత్రా - 26వ ఆర్‌బీఐ గవర్నర్ (1); డాక్టర్ అరవింద్ పనగరియా - 16వ ఆర్థిక సంఘం చైర్మన్ (3)."
    ),
]


def get_gs_questions():
    all_gs = get_part1_gs() + NEW_GEOGRAPHY + NEW_ECONOMY + NEW_SCIENCE + NEW_CURRENT_AFFAIRS
    assert len(all_gs) == 100, f"Expected 100 GS Qs, got {len(all_gs)}"
    for i, q in enumerate(all_gs, start=101):
        q["id"] = i
        q["qNumber"] = i
    return all_gs
