import json

with open('public/data/mock_test_full_200_5.json') as f:
    data = json.load(f)

qs = data['questions']

# 14 authentic General Science questions
science_qs = [
    (
        "Which law of physics explains why an iron ship floats on water while an iron nail sinks?",
        "ఇనుప మేకు నీటిలో మునిగిపోయినప్పటికీ, భారీ ఇనుప ఓడ నీటిపై తేలడానికి గల కారణాన్ని వివరించే భౌతిక సూత్రం ఏది?",
        ["Bernoulli's Principle", "Archimedes' Principle", "Pascal's Law", "Kepler's Law"],
        ["బెర్నౌలీ సూత్రం", "ఆర్కిమెడిస్ సూత్రం (Archimedes' Principle)", "పాస్కల్ నియమం", "కెప్లర్ నియమం"],
        1,
        "Archimedes' principle states that a body immersed in a fluid experiences an upward buoyant force equal to the weight of fluid displaced.",
        "ఓడ తన బరువుకు సమానమైన నీటిని స్థానభ్రంశం చెందించడం వల్ల కలిగే ఉత్ప్లావక బలం వలన తేలుతుంది."
    ),
    (
        "What is the audible frequency range of sound for a healthy adult human ear?",
        "ఆరోగ్యకరమైన మానవ చెవి వినగలిగే ధ్వని పౌనఃపున్య పరిధి (Audible range) ఎంత?",
        ["20 Hz to 20,000 Hz", "50 Hz to 50,000 Hz", "10 Hz to 10,000 Hz", "Above 20,000 Hz"],
        ["20 Hz నుండి 20,000 Hz", "50 Hz నుండి 50,000 Hz", "10 Hz నుండి 10,000 Hz", "20,000 Hz కంటే ఎక్కువ"],
        0,
        "The audible range of hearing for human beings extends from about 20 Hz to 20,000 Hz (20 kHz).",
        "మానవులు వినగలిగే శ్రవ్య ధ్వనుల పరిధి 20 హెర్ట్జ్ నుండి 20,000 హెర్ట్జ్ వరకు ఉంటుంది."
    ),
    (
        "Which pigment present in human red blood cells (RBCs) is responsible for transporting oxygen from the lungs to tissues?",
        "మానవ ఎర్ర రక్త కణాలలో (RBC) ఉండి, ఊపిరితిత్తుల నుండి కణజాలాలకు ఆక్సిజన్‌ను మోసుకెళ్ళే ఇనుముతో కూడిన వర్ణద్రవ్యం ఏది?",
        ["Hemoglobin", "Myoglobin", "Melanin", "Bilirubin"],
        ["హిమోగ్లోబిన్ (Hemoglobin)", "మయోగ్లోబిన్", "మెలనిన్", "బిలిరుబిన్"],
        0,
        "Hemoglobin is an iron-containing metalloprotein in RBCs that binds reversibly to oxygen to form oxyhemoglobin.",
        "ఎర్ర రక్త కణాలలోని హిమోగ్లోబిన్ ఆక్సిజన్‌తో కలిసి ఆక్సీహిమోగ్లోబిన్‌గా శరీర కణజాలాలకు ఆక్సిజన్‌ను సరఫరా చేస్తుంది."
    ),
    (
        "What is the pH value of pure distilled water at 25°C?",
        "25°C ఉష్ణోగ్రత వద్ద స్వచ్ఛమైన స్వేదన జలం (Distilled water) యొక్క pH విలువ ఎంత?",
        ["0", "7", "10", "14"],
        ["0", "7 (Neutral pH 7)", "10", "14"],
        1,
        "Pure water has a neutral pH of exactly 7 at 25°C, where [H+] = [OH-] = 10^-7 M.",
        "స్వచ్ఛమైన తటస్థ నీటి యొక్క pH విలువ 7."
    ),
    (
        "Which cell organelle is universally referred to as the 'Powerhouse of the Cell' due to ATP synthesis?",
        "కణ శ్వాసక్రియ జరిపి ATP రూపంలో శక్తిని ఉత్పత్తి చేయడం వలన 'కణ శక్త్యాగారాలు' (Powerhouse of the cell) అని పిలువబడే కణాంగాలు ఏవి?",
        ["Ribosomes", "Mitochondria", "Lysosomes", "Endoplasmic Reticulum"],
        ["రైబోజోములు", "మైటోకాండ్రియా (Mitochondria)", "లైసోజోములు", "అంతర్జీవ ద్రవ్యజాలం"],
        1,
        "Mitochondria generate cellular energy in the form of Adenosine Triphosphate (ATP) through oxidative phosphorylation.",
        "మైటోకాండ్రియాలు సెల్యులార్ ఎనర్జీని (ATP) ఉత్పత్తి చేయడం వల్ల వీటిని కణ శక్త్యాగారాలు అంటారు."
    ),
    (
        "Which gas protects life on Earth by absorbing hazardous ultraviolet-B (UV-B) rays in the stratosphere?",
        "భూమిపై జీవులను ప్రమాదకరమైన అతినీలలోహిత (UV-B) కిరణాల నుండి రక్షించే స్ట్రాటోస్ఫియర్‌లోని వాయువు ఏది?",
        ["Oxygen (O2)", "Ozone (O3)", "Carbon dioxide (CO2)", "Methane (CH4)"],
        ["ఆక్సిజన్", "ఓజోన్ (O3)", "కార్బన్ డయాక్సైడ్", "మీథేన్"],
        1,
        "The stratospheric ozone layer (O3) absorbs solar UV radiation, preventing DNA damage and skin cancers.",
        "స్ట్రాటోస్ఫియర్‌లోని ఓజోన్ పొర హానికర అతినీలలోహిత కిరణాలను శోషించుకుంటుంది."
    ),
    (
        "Which vitamin is synthesized in the human skin upon exposure to sunlight?",
        "సూర్యరశ్మి సోకినప్పుడు మానవ చర్మంలో సహజంగా సంశ్లేషణ చెందే విటమిన్ ఏది?",
        ["Vitamin A", "Vitamin B12", "Vitamin D (Sunshine Vitamin)", "Vitamin K"],
        ["విటమిన్ A", "విటమిన్ B12", "విటమిన్ D (సన్‌షైన్ విటమిన్)", "విటమిన్ K"],
        2,
        "Exposure of 7-dehydrocholesterol in the skin to solar UVB converts it into cholecalciferol (Vitamin D3).",
        "సూర్యకాంతి సమక్షంలో చర్మంలో విటమిన్ డి సంశ్లేషణ జరుగుతుంది, కాబట్టి దీనిని సన్‌షైన్ విటమిన్ అంటారు."
    ),
    (
        "Which catalyst is commonly utilized in the industrial hydrogenation of vegetable oils into vanaspati ghee?",
        "వనస్పతి నెయ్యి తయారీలో కూరగాయల నూనెలను హైడ్రోజనీకరణం చేయడానికి పారిశ్రామికంగా ఉపయోగించే ఉత్ప్రేరకం ఏది?",
        ["Nickel (Ni)", "Iron (Fe)", "Platinum (Pt)", "Zinc (Zn)"],
        ["నికెల్ (Nickel - Ni)", "ఇనుము", "ప్లాటినం", "జింక్"],
        0,
        "Finely divided Nickel (Ni) is used as a heterogeneous catalyst for the hydrogenation of unsaturated fats.",
        "నూనెల హైడ్రోజనీకరణ చర్యలో నికెల్ (Ni) ను ఉత్ప్రేరకంగా ఉపయోగిస్తారు."
    ),
    (
        "Which human blood type lacks both A and B antibodies in the plasma and is known as the 'Universal Recipient'?",
        "ప్లాస్మాలో A మరియు B యాంటీబాడీలు రెండూ లేకపోవడం వల్ల 'విశ్వ గ్రహీత' (Universal Recipient) గా పరిగణించబడే మానవ రక్త వర్గం ఏది?",
        ["O Negative", "AB Positive", "A Positive", "B Negative"],
        ["O నెగటివ్", "AB పాజిటివ్ (AB Positive)", "A పాజిటివ్", "B నెగటివ్"],
        1,
        "AB Positive individuals have both A and B antigens on RBCs and no antibodies in plasma, allowing them to safely receive blood from any ABO group.",
        "AB పాజిటివ్ వ్యక్తులు ఎవరి రక్తమైనా స్వీకరించగలరు కాబట్టి వీరిని 'విశ్వ గ్రహీతలు' అంటారు."
    ),
    (
        "What is the optical phenomenon that causes the blue colour of the clear sky during daytime?",
        "పగటి పూట నిర్మలమైన ఆకాశం నీలి రంగులో కనిపించడానికి కారణమైన కాంతి దృగ్విషయం ఏది?",
        ["Rayleigh Scattering of light", "Total Internal Reflection", "Dispersion of light through rain droplets", "Interference of light waves"],
        ["కాంతి రాలే పరిక్షేపణం (Rayleigh Scattering)", "సంపూర్ణాంతర పరావర్తనం", "కాంతి విక్షేపణం", "కాంతి వ్యతికరణం"],
        0,
        "According to Rayleigh's law of scattering, shorter blue wavelengths scatter much more strongly in the atmosphere than red light.",
        "తక్కువ తరంగదైర్ఘ్యం గల నీలి రంగు కాంతి వాతావరణ అణువుల చేత ఎక్కువగా పరిక్షేపణం చెందడం వల్ల ఆకాశం నీలంగా కనిపిస్తుంది."
    ),
    (
        "Which disease in humans is caused by the bacterial pathogen Mycobacterium tuberculosis?",
        "మైకోబాక్టీరియం ట్యూబర్‌క్యులోసిస్ అనే బ్యాక్టీరియా సంక్రమణ వలన మానవులలో కలిగే వ్యాధి ఏది?",
        ["Cholera", "Tuberculosis (TB)", "Typhoid", "Tetanus"],
        ["కలరా", "క్షయ వ్యాధి (Tuberculosis - TB)", "టైఫాయిడ్", "ధనుర్వాతం"],
        1,
        "Tuberculosis is an infectious bacterial disease primarily affecting lungs, diagnosed by sputum smear and GeneXpert tests.",
        "మైకోబాక్టీరియం ట్యూబర్‌క్యులోసిస్ వల్ల ప్రధానంగా ఊపిరితిత్తులకు సోకే సాంక్రమిక వ్యాధి క్షయ (TB)."
    ),
    (
        "Which metal is liquid at ordinary room temperature (25°C)?",
        "సాధారణ గది ఉష్ణోగ్రత వద్ద ద్రవ రూపంలో ఉండే లోహం ఏది?",
        ["Mercury (Hg)", "Bromine (Br)", "Gallium (Ga)", "Sodium (Na)"],
        ["పాదరసం (Mercury - Hg)", "బ్రోమిన్", "గాలియం", "సోడియం"],
        0,
        "Mercury (Hg) has a freezing point of -38.8°C and is the only pure metal in liquid state at standard room conditions. (Bromine is a non-metal).",
        "గది ఉష్ణోగ్రత వద్ద ద్రవ రూపంలో ఉండే ఏకైక లోహం పాదరసం (Hg). బ్రోమిన్ అలోహం."
    ),
    (
        "Which hormone secreted by the beta cells of the islets of Langerhans in the pancreas regulates glucose levels in blood?",
        "క్లోమ గ్రంథిలోని లాంగర్‌హాన్స్ పుటికల బీటా కణాలు స్రవించే ఏ హార్మోన్ రక్తంలో గ్లూకోజ్ స్థాయిలను నియంత్రిస్తుంది?",
        ["Glucagon", "Insulin", "Thyroxine", "Adrenaline"],
        ["గ్లూకగాన్", "ఇన్సులిన్ (Insulin)", "థైరాక్సిన్", "అడ్రినలిన్"],
        1,
        "Insulin lowers blood glucose by facilitating cellular glucose uptake. Deficiency causes Diabetes Mellitus.",
        "రక్తంలోని గ్లూకోజ్ స్థాయిని తగ్గించడానికి క్లోమం ఇన్సులిన్ హార్మోన్‌ను ఉత్పత్తి చేస్తుంది. దీని లోపం మధుమేహానికి దారితీస్తుంది."
    ),
    (
        "Which unit is used to measure the intensity or loudness of sound?",
        "ధ్వని తీవ్రతను కొలవడానికి ఉపయోగించే ప్రామాణిక ప్రమాణం ఏది?",
        ["Hertz (Hz)", "Decibel (dB)", "Joule (J)", "Watt (W)"],
        ["హెర్ట్జ్ (Hz)", "డెసిబెల్ (Decibel - dB)", "జౌల్", "వాట్"],
        1,
        "Decibel (dB) is a logarithmic unit used to express the ratio of acoustic pressure, measuring sound loudness.",
        "ధ్వని తీవ్రతను డెసిబెల్ (dB) లలో కొలుస్తారు."
    )
]

for idx, sq in enumerate(science_qs):
    q_num = 101 + idx
    qs[100 + idx] = {
        "id": q_num,
        "qNumber": q_num,
        "section": "General Studies",
        "topic": "General Science & Everyday Technology",
        "question_en": sq[0],
        "question_te": sq[1],
        "options_en": sq[2],
        "options_te": sq[3],
        "correct_option": sq[4],
        "explanation_en": sq[5],
        "explanation_te": sq[6]
    }

with open('public/data/mock_test_full_200_5.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Mock 5 Science questions fixed!")
