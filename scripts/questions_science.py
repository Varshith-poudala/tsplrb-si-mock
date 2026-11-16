#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part C: General Studies & Telangana Movement (Questions 101 to 200)
- Q101-Q130 (30 Qs): General Science (Biology, Physics, Chemistry) derived from reference_science_gk_200.json
- Q131-Q165 (35 Qs): Current Affairs 2026 derived from reference_current_affairs_400.json
- Q166-Q200 (35 Qs): Telangana History, Movement, Culture & Contemporary Schemes
All questions feature full bilingual text (English & Telugu), 4 options, and step-by-step explanations.
"""

import json
import os

def get_science_30():
    """Q101 to Q130: 30 General Science questions directly matching reference_science_gk_200.json."""
    return [
        # 101. Discovery of Cell
        {
            "id": 101,
            "qNumber": 101,
            "section": "General Studies",
            "topic": "General Science - Biology: Cytology",
            "question_en": "Which scientist discovered the cell for the first time in 1665 by observing a thin slice of cork under a microscope?",
            "question_te": "1665 లో సూక్ష్మదర్శిని క్రింద కార్క్ యొక్క పలుచని ముక్కను పరిశీలించడం ద్వారా మొట్టమొదటిసారిగా కణాన్ని (Cell) కనుగొన్న శాస్త్రవేత్త ఎవరు?",
            "options_en": ["Robert Hooke", "Robert Brown", "Anton van Leeuwenhoek", "Theodor Schwann"],
            "options_te": ["రాబర్ట్ హుక్", "రాబర్ట్ బ్రౌన్", "ఆంటోన్ వాన్ లీవెన్‌హుక్", "థియోడర్ ష్వాన్"],
            "correct_option": 0,
            "explanation_en": "Robert Hooke discovered the cell in 1665 using an early microscope to examine cork cells. Robert Brown discovered the cell nucleus in 1831.",
            "explanation_te": "1665 లో రాబర్ట్ హుక్ కార్క్ కణాలను పరిశీలించి కణాన్ని కనుగొన్నాడు. రాబర్ట్ బ్రౌన్ 1831 లో కణ కేంద్రకాన్ని కనుగొన్నాడు."
        },
        # 102. Powerhouse of the Cell
        {
            "id": 102,
            "qNumber": 102,
            "section": "General Studies",
            "topic": "General Science - Biology: Cell Organelles",
            "question_en": "Which cell organelle is known as the 'Powerhouse of the Cell' because it generates most of the chemical energy needed by the cell in the form of ATP?",
            "question_te": "కణానికి అవసరమైన రసాయన శక్తిని ATP రూపంలో ఉత్పత్తి చేయడం వల్ల ఏ కణాంగాన్ని 'కణ శక్త్యాగారాలు' (Powerhouse of the cell) అని పిలుస్తారు?",
            "options_en": ["Mitochondria", "Ribosomes", "Golgi apparatus", "Plastids"],
            "options_te": ["మైటోకాండ్రియా", "రైబోజోములు", "గాల్జీ సంక్లిష్టం", "ప్లాస్టిడ్లు"],
            "correct_option": 0,
            "explanation_en": "Mitochondria produce cellular energy (ATP) through cellular respiration and are universally designated as the powerhouses of the cell.",
            "explanation_te": "కణ శ్వాసక్రియ ద్వారా ATP రూపంలో శక్తిని ఉత్పత్తి చేయడం వల్ల మైటోకాండ్రియాను కణ శక్త్యాగారాలు అని పిలుస్తారు."
        },
        # 103. Suicidal Bags
        {
            "id": 103,
            "qNumber": 103,
            "section": "General Studies",
            "topic": "General Science - Biology: Cell Organelles",
            "question_en": "Which cell organelles are commonly referred to as the 'Suicidal Bags of the Cell' due to the presence of destructive hydrolytic digestive enzymes?",
            "question_te": "శక్తివంతమైన జలవిశ్లేషణ ఎంజైమ్‌లను కలిగి ఉండి, కణం దెబ్బతిన్నప్పుడు విచ్ఛిన్నం చెంది కణాన్నే జీర్ణం చేసుకోగల ఏ కణాంగాలను 'కణ ఆత్మహత్య కోశాలు' (Suicidal bags) అని పిలుస్తారు?",
            "options_en": ["Lysosomes", "Centrosomes", "Peroxisomes", "Endoplasmic Reticulum"],
            "options_te": ["లైసోజోములు", "సెంట్రోజోములు", "పెరాక్సిజోములు", "అంతర్జీవద్రవ్య జాలకం"],
            "correct_option": 0,
            "explanation_en": "Lysosomes contain acidic hydrolases. If a cell is damaged, lysosomes burst and their enzymes digest their own cell, earning them the name 'suicidal bags'.",
            "explanation_te": "లైసోజోములు హైడ్రోలైటిక్ ఎంజైమ్‌లను కలిగి ఉంటాయి. కణం దెబ్బతిన్నప్పుడు ఇవి పగిలి సొంత కణాన్నే నాశనం చేస్తాయి కాబట్టి వీటిని ఆత్మహత్య కోశాలు అంటారు."
        },
        # 104. Protein Factories
        {
            "id": 104,
            "qNumber": 104,
            "section": "General Studies",
            "topic": "General Science - Biology: Cell Organelles",
            "question_en": "Which granular organelles are known as the 'Protein Factories' of the cell?",
            "question_te": "కణంలో ప్రోటీన్ల సంశ్లేషణను నిర్వహించడం వల్ల ఏ కణాంగాలను 'కణ ప్రోటీన్ కర్మాగారాలు' అని పిలుస్తారు?",
            "options_en": ["Ribosomes", "Mitochondria", "Lysosomes", "Vacuoles"],
            "options_te": ["రైబోజోములు", "మైటోకాండ్రియా", "లైసోజోములు", "రిక్తికలు"],
            "correct_option": 0,
            "explanation_en": "Ribosomes synthesize proteins by translating messenger RNA (mRNA), making them the protein factories of the cell.",
            "explanation_te": "mRNA సంకేతాల ద్వారా అమైనో ఆమ్లాలను ప్రోటీన్లుగా మార్చడం వల్ల రైబోజోములను ప్రోటీన్ ఫ్యాక్టరీలు అంటారు."
        },
        # 105. Largest Organ & Largest Gland
        {
            "id": 105,
            "qNumber": 105,
            "section": "General Studies",
            "topic": "General Science - Human Anatomy",
            "question_en": "Which is the largest organ and which is the largest internal gland in the human body respectively?",
            "question_te": "మానవ శరీరంలో అత్యంత పెద్ద అవయవం మరియు అత్యంత పెద్ద గ్రంథి వరుసగా ఏవి?",
            "options_en": ["Skin and Liver", "Liver and Pancreas", "Skin and Thyroid", "Brain and Liver"],
            "options_te": ["చర్మం మరియు కాలేయం", "కాలేయం మరియు క్లోమం", "చర్మం మరియు థైరాయిడ్", "మెదడు మరియు కాలేయం"],
            "correct_option": 0,
            "explanation_en": "The largest organ of the human body is the skin (integumentary system), and the largest gland (and internal organ) is the liver, weighing around 1.5 kg.",
            "explanation_te": "మానవ శరీరంలో బాహ్యంగా ఉండే అతిపెద్ద అవయవం చర్మం, మరియు శరీరంలో అతిపెద్ద గ్రంథి కాలేయం (సుమారు 1.5 కిలోలు)."
        },
        # 106. Bones in Human Body
        {
            "id": 106,
            "qNumber": 106,
            "section": "General Studies",
            "topic": "General Science - Human Skeletal System",
            "question_en": "Which is the longest/strongest bone and which is the smallest bone in the human body respectively?",
            "question_te": "మానవ శరీరంలో అత్యంత పొడవైన/బలమైన ఎముక మరియు అత్యంత చిన్న ఎముక వరుసగా ఏవి?",
            "options_en": ["Femur (thigh bone) and Stapes (middle ear)", "Tibia and Incus", "Femur and Malleus", "Humerus and Stapes"],
            "options_te": ["ఫీమర్ (తొడ ఎముక) మరియు స్టేప్స్ (మధ్య చెవి ఎముక)", "టిబియా మరియు ఇంకస్", "ఫీమర్ మరియు మాలియస్", "హ్యూమరస్ మరియు స్టేప్స్"],
            "correct_option": 0,
            "explanation_en": "The longest and strongest bone is the Femur (thigh bone). The smallest bone is the Stapes (stirrup bone) located in the middle ear.",
            "explanation_te": "మానవ శరీరంలో అతి పొడవైన ఎముక ఫీమర్ (తొడ ఎముక), అతి చిన్న ఎముక చెవిలోని స్టేప్స్ (కర్ణాంతరాస్థి)."
        },
        # 107. RBC Lifespan & Universal Donor
        {
            "id": 107,
            "qNumber": 107,
            "section": "General Studies",
            "topic": "General Science - Blood & Circulatory System",
            "question_en": "What is the average lifespan of human Red Blood Cells (RBCs) and which blood group is designated as the universal donor?",
            "question_te": "మానవ రక్తంలోని ఎర్ర రక్త కణాల (RBC) సగటు జీవిత కాలం ఎంత మరియు ఏ రక్త వర్గాన్ని విశ్వదాత (Universal Donor) అంటారు?",
            "options_en": ["120 days and O Negative", "100 days and AB Positive", "120 days and O Positive", "60 days and O Negative"],
            "options_te": ["120 రోజులు మరియు O నెగెటివ్", "100 రోజులు మరియు AB పాజిటివ్", "120 రోజులు మరియు O పాజిటివ్", "60 రోజులు మరియు O నెగెటివ్"],
            "correct_option": 0,
            "explanation_en": "The average lifespan of erythrocytes (RBCs) is approximately 120 days. Blood group O-negative has neither A, B antigens nor Rh factor, making it the true universal donor.",
            "explanation_te": "ఎర్ర రక్త కణాల జీవిత కాలం సుమారు 120 రోజులు. O నెగెటివ్ రక్తం లో ఎటువంటి యాంటిజెన్లు ఉండవు కాబట్టి దీనిని విశ్వదాత అంటారు."
        },
        # 108. Master Gland
        {
            "id": 108,
            "qNumber": 108,
            "section": "General Studies",
            "topic": "General Science - Endocrine System",
            "question_en": "Which endocrine gland is located at the base of the brain and is known as the 'Master Gland' because it controls the functions of most other endocrine glands?",
            "question_te": "మెదడు అడుగుభాగంలో ఉండి, శరీరంలోని ఇతర అంతఃస్రావ గ్రంథుల పనితీరును నియంత్రించడం వల్ల 'మాస్టర్ గ్లాండ్' (ప్రధాన గ్రంథి) అని దేనిని పిలుస్తారు?",
            "options_en": ["Pituitary Gland", "Thyroid Gland", "Adrenal Gland", "Pancreas"],
            "options_te": ["పిట్యూటరీ గ్రంథి (పీయూష గ్రంథి)", "థైరాయిడ్ గ్రంథి", "అడ్రినల్ గ్రంథి", "క్లోమ గ్రంథి"],
            "correct_option": 0,
            "explanation_en": "The pituitary gland produces hormones (TSH, ACTH, GH, FSH, LH) that regulate other endocrine organs, earning it the title 'master gland'.",
            "explanation_te": "పిట్యూటరీ గ్రంథి ఇతర గ్రంథులను ఉత్తేజపరిచే హార్మోన్లను విడుదల చేయడం వల్ల దీనిని ప్రధాన లేదా మాస్టర్ గ్రంథి అంటారు."
        },
        # 109. Vitamins & Deficiency
        {
            "id": 109,
            "qNumber": 109,
            "section": "General Studies",
            "topic": "General Science - Vitamins & Nutrition",
            "question_en": "Match the following vitamins with their chemical names / deficiency diseases correctly:\n1. Vitamin A - Retinol - Night Blindness\n2. Vitamin C - Ascorbic Acid - Scurvy\n3. Vitamin D - Calciferol - Rickets\n4. Vitamin K - Phylloquinone - Blood Clotting Failure",
            "question_te": "విటమిన్లు మరియు వాటి రసాయన నామాలు/లోప వ్యాధులను జతపరచండి:\n1. విటమిన్ A - రెటినాల్ - రేచీకటి\n2. విటమిన్ C - ఆస్కార్బిక్ ఆమ్లం - స్కర్వీ\n3. విటమిన్ D - కాల్సిఫెరాల్ - రికెట్స్\n4. విటమిన్ K - ఫిల్లోక్వినోన్ - రక్తం గడ్డకట్టకపోవడం\nపై వాటిలో ఏవి సరిగ్గా జతచేయబడ్డాయి?",
            "options_en": ["All 1, 2, 3, and 4 are correct", "Only 1 and 2 are correct", "Only 2 and 3 are correct", "Only 1, 2, and 3 are correct"],
            "options_te": ["1, 2, 3, మరియు 4 అన్నీ సరైనవే", "1 మరియు 2 మాత్రమే సరైనవి", "2 మరియు 3 మాత్రమే సరైనవి", "1, 2, మరియు 3 మాత్రమే సరైనవి"],
            "correct_option": 0,
            "explanation_en": "All pairs are scientifically accurate: Vitamin A (Retinol/Night blindness), Vitamin C (Ascorbic acid/Scurvy), Vitamin D (Calciferol/Rickets), Vitamin K (Phylloquinone/Blood clotting factor).",
            "explanation_te": "ఇచ్చిన జతలన్నీ సరైనవే. విటమిన్ A (రేచీకటి), C (స్కర్వీ), D (రికెట్స్), K (రక్తం గడ్డకట్టడంలో తోడ్పడుతుంది)."
        },
        # 110. Element in Vitamin B12 & Chlorophyll
        {
            "id": 110,
            "qNumber": 110,
            "section": "General Studies",
            "topic": "General Science - Biochemistry",
            "question_en": "Which metallic elements are present at the core of Vitamin B12 (Cyanocobalamin) and Chlorophyll respectively?",
            "question_te": "విటమిన్ B12 (సయనోకోబాలమిన్) మరియు క్లోరోఫిల్ (పత్రహరితం) లలో కేంద్ర ధాతువులుగా ఉండే లోహాలు వరుసగా ఏవి?",
            "options_en": ["Cobalt and Magnesium", "Iron and Zinc", "Copper and Magnesium", "Cobalt and Iron"],
            "options_te": ["కోబాల్ట్ మరియు మెగ్నీషియం", "ఇనుము మరియు జింక్", "రాగి మరియు మెగ్నీషియం", "కోబాల్ట్ మరియు ఇనుము"],
            "correct_option": 0,
            "explanation_en": "Vitamin B12 contains Cobalt at its core coordination complex. Chlorophyll contains a Magnesium ion coordinated at the center of its porphyrin ring.",
            "explanation_te": "విటమిన్ B12 లో కోబాల్ట్ లోహం ఉంటుంది, క్లోరోఫిల్ లో మెగ్నీషియం లోహం కేంద్ర స్థానంలో ఉంటుంది."
        },
        # 111. Insulin & Diabetes
        {
            "id": 111,
            "qNumber": 111,
            "section": "General Studies",
            "topic": "General Science - Human Physiology",
            "question_en": "Insulin is a peptide hormone secreted by which specific cells of the Pancreas to regulate blood glucose levels?",
            "question_te": "రక్తంలో గ్లూకోజ్ స్థాయిలను నియంత్రించే ఇన్సులిన్ అనే హార్మోన్ క్లోమ గ్రంథిలోని ఏ నిర్దిష్ట కణాల ద్వారా స్రవించబడుతుంది?",
            "options_en": ["Beta cells of Islets of Langerhans", "Alpha cells", "Delta cells", "Acinar cells"],
            "options_te": ["లాంగర్‌హాన్స్ పుటికలలోని బీటా (Beta) కణాలు", "ఆల్ఫా కణాలు", "డెల్టా కణాలు", "ఎసినార్ కణాలు"],
            "correct_option": 0,
            "explanation_en": "Beta cells of the Islets of Langerhans in the pancreas secrete insulin. Alpha cells secrete glucagon.",
            "explanation_te": "క్లోమ గ్రంథి లోని లాంగర్‌హాన్స్ పుటికల బీటా కణాలు ఇన్సులిన్‌ను ఉత్పత్తి చేస్తాయి. ఆల్ఫా కణాలు గ్లూకగాన్‌ను విడుదల చేస్తాయి."
        },
        # 112. Blood Pressure Normal Range
        {
            "id": 112,
            "qNumber": 112,
            "section": "General Studies",
            "topic": "General Science - Human Physiology",
            "question_en": "What is the normal resting blood pressure of a healthy human adult, and which instrument is used to measure it?",
            "question_te": "ఆరోగ్యవంతమైన మానవ వయోజనుడి సాధారణ రక్తపోటు (BP) విలువ ఎంత మరియు దానిని కొలవడానికి ఏ పరికరాన్ని ఉపయోగిస్తారు?",
            "options_en": ["120/80 mm Hg and Sphygmomanometer", "140/90 mm Hg and Stethoscope", "110/70 mm Hg and Barometer", "120/80 mm Hg and Spirometer"],
            "options_te": ["120/80 mm Hg మరియు స్పిగ్మోమానోమీటర్", "140/90 mm Hg మరియు స్టెతస్కోప్", "110/70 mm Hg మరియు బారోమీటర్", "120/80 mm Hg మరియు స్పైరోమీటర్"],
            "correct_option": 0,
            "explanation_en": "Normal blood pressure is 120 mm Hg (systolic) over 80 mm Hg (diastolic), measured using a Sphygmomanometer.",
            "explanation_te": "సాధారణ రక్తపోటు 120/80 mm Hg. దీనిని స్పిగ్మోమానోమీటర్ (Sphygmomanometer) పరికరంతో కొలుస్తారు."
        },
        # 113. Eye Defects & Corrective Lenses
        {
            "id": 113,
            "qNumber": 113,
            "section": "General Studies",
            "topic": "General Science - Physics: Optics",
            "question_en": "Which types of lenses are used to correct Myopia (short-sightedness) and Hypermetropia (long-sightedness) respectively?",
            "question_te": "హ్రస్వదృష్టి (Myopia) మరియు దూరదృష్టి (Hypermetropia) అనే దృష్టి లోపాలను సరిదిద్దడానికి వరుసగా ఏ కటకాలను ఉపయోగిస్తారు?",
            "options_en": ["Concave lens and Convex lens", "Convex lens and Concave lens", "Bifocal lens and Cylindrical lens", "Cylindrical lens and Convex lens"],
            "options_te": ["పుటాకార కటకం మరియు కుంభాకార కటకం", "కుంభాకార కటకం మరియు పుటాకార కటకం", "ద్విఫోకల్ కటకం మరియు స్థూపాకార కటకం", "స్థూపాకార కటకం మరియు కుంభాకార కటకం"],
            "correct_option": 0,
            "explanation_en": "Myopia (image forms in front of retina) is corrected using diverging concave lenses. Hypermetropia (image forms behind retina) is corrected using converging convex lenses.",
            "explanation_te": "హ్రస్వదృష్టికి పుటాకార (Concave) కటకం, దూరదృష్టికి కుంభాకార (Convex) కటకం ఉపయోగిస్తారు."
        },
        # 114. Speed of Light & Sound
        {
            "id": 114,
            "qNumber": 114,
            "section": "General Studies",
            "topic": "General Science - Physics",
            "question_en": "What is the speed of light in vacuum, and through which medium can sound waves NOT travel at all?",
            "question_te": "శూన్యంలో కాంతి వేగం ఎంత మరియు ధ్వని తరంగాలు క్రింది వాటిలో దేని గుండా అస్సలు ప్రయాణించలేవు?",
            "options_en": ["3 * 10^8 m/s and Vacuum", "3 * 10^6 m/s and Water", "332 m/s and Steel", "3 * 10^8 km/s and Air"],
            "options_te": ["3 * 10^8 మీ/సె మరియు శూన్యం (Vacuum)", "3 * 10^6 మీ/సె మరియు నీరు", "332 మీ/సె మరియు ఉక్కు", "3 * 10^8 కిమీ/సె మరియు గాలి"],
            "correct_option": 0,
            "explanation_en": "The speed of light in vacuum is approx 3 * 10^8 m/s. Sound waves are mechanical longitudinal waves requiring an elastic material medium and cannot propagate through vacuum.",
            "explanation_te": "శూన్యంలో కాంతి వేగం 3 * 10^8 మీ/సె (3 లక్షల కి.మీ/సెకను). ధ్వని తరంగాలు యాంత్రిక తరంగాలు కాబట్టి శూన్యం గుండా ప్రయాణించలేవు."
        },
        # 115. Total Internal Reflection
        {
            "id": 115,
            "qNumber": 115,
            "section": "General Studies",
            "topic": "General Science - Physics: Optics",
            "question_en": "Which optical phenomenon is primarily responsible for the sparkling of diamonds, optical fibre communication, and mirages in deserts?",
            "question_te": "వజ్రం మిరుమిట్లు గొలపడం, ఆప్టికల్ ఫైబర్ కమ్యూనికేషన్, మరియు ఎడారిలో ఎండమావులు ఏర్పడటానికి ప్రధాన కారణమైన దృగ్విషయం ఏది?",
            "options_en": ["Total Internal Reflection", "Diffraction", "Interference", "Dispersion"],
            "options_te": ["సంపూర్ణాంతర పరావర్తనం (Total Internal Reflection)", "వివర్తనం", "వ్యతికరణం", "విక్షేపణం"],
            "correct_option": 0,
            "explanation_en": "Total Internal Reflection occurs when light travels from a denser to a rarer medium at an angle of incidence greater than the critical angle. It governs optical fibers, diamond brilliance, and mirages.",
            "explanation_te": "కాంతి సాంద్రతర యానకం నుండి విరళ యానకంలోకి ప్రవేశించేటప్పుడు సంపూర్ణాంతర పరావర్తనం చెందుతుంది. దీని వల్లే వజ్రం మెరవడం, ఆప్టికల్ ఫైబర్ పనిచేయడం మరియు ఎండమావులు సంభవిస్తాయి."
        },
        # 116. Blue Color of Sky
        {
            "id": 116,
            "qNumber": 116,
            "section": "General Studies",
            "topic": "General Science - Physics: Light",
            "question_en": "The clear sky appears blue during the day primarily due to which phenomenon of light?",
            "question_te": "పగటిపూట ఆకాశం నీలిరంగులో కనిపించడానికి కాంతి యొక్క ఏ దృగ్విషయం ప్రధాన కారణం?",
            "options_en": ["Rayleigh Scattering of light", "Refraction of light", "Total internal reflection", "Dispersion of light"],
            "options_te": ["కాంతి పరిక్షేపణం (Rayleigh Scattering)", "కాంతి వక్రీభవనం", "సంపూర్ణాంతర పరావర్తనం", "కాంతి విక్షేపణం"],
            "correct_option": 0,
            "explanation_en": "According to Rayleigh's law, scattering intensity is inversely proportional to λ^4. Shorter blue wavelengths are scattered much more strongly by atmospheric molecules than red wavelengths.",
            "explanation_te": "తక్కువ తరంగదైర్ఘ్యం ఉన్న నీలి రంగు కాంతి వాతావరణంలోని రేణువుల చేత ఎక్కువగా పరిక్షేపణం (Scattering) చెందడం వల్ల ఆకాశం నీలంగా కనిపిస్తుంది."
        },
        # 117. Rear-View Mirrors in Vehicles
        {
            "id": 117,
            "qNumber": 117,
            "section": "General Studies",
            "topic": "General Science - Physics: Mirrors",
            "question_en": "Which type of mirror is installed as a rear-view mirror in automobiles because it always produces an erect, diminished image and provides a wider field of view?",
            "question_te": "ఎల్లప్పుడూ నిటారుగా ఉండే చిన్న ప్రతిబింబాన్ని ఏర్పరుస్తూ విస్తృత దృశ్య పరిధిని అందించడం వల్ల వాహనాలలో రియర్-వ్యూ మిర్రర్‌గా ఏ దర్పణాన్ని ఉపయోగిస్తారు?",
            "options_en": ["Convex mirror", "Concave mirror", "Plane mirror", "Parabolic mirror"],
            "options_te": ["కుంభాకార దర్పణం (Convex mirror)", "పుటాకార దర్పణం", "సమతల దర్పణం", "పారాబోలిక్ దర్పణం"],
            "correct_option": 0,
            "explanation_en": "Convex mirrors always produce erect, virtual, and diminished images, offering drivers a broader field of view of traffic behind them.",
            "explanation_te": "కుంభాకార దర్పణాలు ఎల్లప్పుడూ నిటారైన, చిన్నదైన మిధ్యా ప్రతిబింబాన్ని ఇస్తాయి మరియు విస్తారమైన వెనుక రోడ్డును చూపిస్తాయి."
        },
        # 118. SI Units of Physics
        {
            "id": 118,
            "qNumber": 118,
            "section": "General Studies",
            "topic": "General Science - Physics: Units",
            "question_en": "Match the following physical quantities with their standard SI units:\n1. Electric Current - Ampere\n2. Electrical Resistance - Ohm\n3. Power - Watt\n4. Frequency - Hertz",
            "question_te": "కింది భౌతిక రాశులను వాటి అంతర్జాతీయ SI ప్రమాణాలతో జతపరచండి:\n1. విద్యుత్ ప్రవాహం - ఆంపియర్\n2. విద్యుత్ నిరోధం - ఓమ్\n3. సామర్థ్యం - వాట్\n4. పౌనఃపున్యం - హెర్ట్జ్\nపై వాటిలో సరైనవి ఏవి?",
            "options_en": ["All 1, 2, 3, and 4 are correct", "Only 1 and 2 are correct", "Only 3 and 4 are correct", "Only 1, 2, and 3 are correct"],
            "options_te": ["1, 2, 3, మరియు 4 అన్నీ సరైనవే", "1 మరియు 2 మాత్రమే సరైనవి", "3 మరియు 4 మాత్రమే సరైనవి", "1, 2, మరియు 3 మాత్రమే సరైనవి"],
            "correct_option": 0,
            "explanation_en": "Electric Current (Ampere A), Electrical Resistance (Ohm Ω), Power (Watt W = J/s), Frequency (Hertz Hz = s^-1). All 4 are correct SI units.",
            "explanation_te": "విద్యుత్ ప్రవాహం (ఆంపియర్), నిరోధం (ఓమ్), సామర్థ్యం (వాట్), పౌనఃపున్యం (హెర్ట్జ్) - అన్నీ సరైన SI ప్రమాణాలు."
        },
        # 119. Escape Velocity of Earth
        {
            "id": 119,
            "qNumber": 119,
            "section": "General Studies",
            "topic": "General Science - Physics: Gravitation",
            "question_en": "What is the escape velocity required for an object to break free from Earth's gravitational pull?",
            "question_te": "భూమి యొక్క గురుత్వాకర్షణ క్షేత్రం నుండి ఒక వస్తువు అంతరిక్షంలోకి తప్పించుకోవడానికి అవసరమైన పలాయన వేగం (Escape velocity) ఎంత?",
            "options_en": ["11.2 km/s", "9.8 m/s", "7.9 km/s", "15.4 km/s"],
            "options_te": ["11.2 కి.మీ/సెకను", "9.8 మీ/సెకను", "7.9 కి.మీ/సెకను", "15.4 కి.మీ/సెకను"],
            "correct_option": 0,
            "explanation_en": "Earth's escape velocity is given by v = sqrt(2GM/R) ≈ 11.2 km/s (approx 40,320 km/h).",
            "explanation_te": "భూమి నుండి తప్పించుకోవడానికి అవసరమైన పలాయన వేగం v = √(2gR) = 11.2 కి.మీ/సెకను."
        },
        # 120. Audible Range of Human Ear
        {
            "id": 120,
            "qNumber": 120,
            "section": "General Studies",
            "topic": "General Science - Physics: Sound",
            "question_en": "What is the frequency range of sound waves audible to the normal human ear?",
            "question_te": "సాధారణ మానవుని చెవి వినగలిగే ధ్వని తరంగాల శ్రవ్య పౌనఃపున్య పరిధి ఎంత?",
            "options_en": ["20 Hz to 20,000 Hz", "10 Hz to 10,000 Hz", "50 Hz to 50,000 Hz", "200 Hz to 20,000 Hz"],
            "options_te": ["20 Hz నుండి 20,000 Hz", "10 Hz నుండి 10,000 Hz", "50 Hz నుండి 50,000 Hz", "200 Hz నుండి 20,000 Hz"],
            "correct_option": 0,
            "explanation_en": "Human hearing spans the frequency range from 20 Hz to 20,000 Hz (20 kHz). Below 20 Hz is infrasonic; above 20 kHz is ultrasonic.",
            "explanation_te": "మానవుని శ్రవ్య పరిధి 20 హెర్ట్జ్ నుండి 20,000 హెర్ట్జ్ వరకు ఉంటుంది. 20 Hz కంటే తక్కువ అయితే పరశ్రావ్యాలు, 20 kHz కంటే ఎక్కువ అయితే అతిధ్వనులు అంటారు."
        },
        # 121. Subatomic Particles & Discoverers
        {
            "id": 121,
            "qNumber": 121,
            "section": "General Studies",
            "topic": "General Science - Chemistry: Atomic Structure",
            "question_en": "Who discovered the Electron and the Neutron respectively?",
            "question_te": "ఎలక్ట్రాన్ మరియు న్యూట్రాన్‌లను కనుగొన్న శాస్త్రవేత్తలు వరుసగా ఎవరు?",
            "options_en": ["J.J. Thomson and James Chadwick", "Ernest Rutherford and J.J. Thomson", "James Chadwick and John Dalton", "Niels Bohr and Robert Millikan"],
            "options_te": ["జే.జే. థామ్సన్ మరియు జేమ్స్ చాడ్విక్", "ఎర్నెస్ట్ రూథర్‌ఫర్డ్ మరియు జే.జే. థామ్సన్", "జేమ్స్ చాడ్విక్ మరియు జాన్ డాల్టన్", "నీల్స్ బోర్ మరియు రాబర్ట్ మిల్లికన్"],
            "correct_option": 0,
            "explanation_en": "The electron was discovered by J.J. Thomson in 1897 using cathode rays. The neutron was discovered by James Chadwick in 1932.",
            "explanation_te": "ఎలక్ట్రాన్‌ను 1897 లో జే.జే. థామ్సన్, మరియు న్యూట్రాన్‌ను 1932 లో జేమ్స్ చాడ్విక్ కనుగొన్నారు."
        },
        # 122. Litmus & pH of Blood
        {
            "id": 122,
            "qNumber": 122,
            "section": "General Studies",
            "topic": "General Science - Chemistry: Acids and Bases",
            "question_en": "What is the normal pH of human blood and how do acids affect blue litmus paper?",
            "question_te": "మానవ రక్తం యొక్క సాధారణ pH విలువ ఎంత మరియు ఆమ్లాలు నీలి లిట్మస్ కాగితాన్ని ఏ రంగులోకి మారుస్తాయి?",
            "options_en": ["7.4 and turns Blue litmus to Red", "7.0 and turns Red litmus to Blue", "6.5 and turns Blue litmus to Green", "8.2 and leaves it unchanged"],
            "options_te": ["7.4 మరియు నీలి లిట్మస్‌ను ఎరుపు రంగులోకి మారుస్తాయి", "7.0 మరియు ఎరుపు లిట్మస్‌ను నీలి రంగులోకి మారుస్తాయి", "6.5 మరియు నీలి లిట్మస్‌ను ఆకుపచ్చగా మారుస్తాయి", "8.2 మరియు రంగు మార్చవు"],
            "correct_option": 0,
            "explanation_en": "Human blood pH is slightly alkaline at 7.35–7.45 (mean ~7.4). Acids turn blue litmus red; bases turn red litmus blue.",
            "explanation_te": "మానవ రక్తం యొక్క pH విలువ సుమారు 7.4 (స్వల్ప క్షార గుణం). ఆమ్లాలు నీలి లిట్మస్ కాగితాన్ని ఎరుపు రంగులోకి మారుస్తాయి."
        },
        # 123. Acids in Everyday Substances
        {
            "id": 123,
            "qNumber": 123,
            "section": "General Studies",
            "topic": "General Science - Chemistry: Organic Acids",
            "question_en": "Which acid is present in vinegar, and which acid causes irritation during an ant sting?",
            "question_te": "వెనిగర్‌లో ఉండే ఆమ్లం ఏది మరియు చీమ కుట్టినప్పుడు మంటను కలిగించే ఆమ్లం ఏది?",
            "options_en": ["Acetic acid and Formic acid", "Citric acid and Lactic acid", "Tartaric acid and Oxalic acid", "Formic acid and Maleic acid"],
            "options_te": ["ఎసిటిక్ ఆమ్లం మరియు ఫార్మిక్ ఆమ్లం (మిథనోయిక్ ఆమ్లం)", "సిట్రిక్ ఆమ్లం మరియు లాక్టిక్ ఆమ్లం", "టార్టారిక్ ఆమ్లం మరియు ఆక్సాలిక్ ఆమ్లం", "ఫార్మిక్ ఆమ్లం మరియు మాలీయిక్ ఆమ్లం"],
            "correct_option": 0,
            "explanation_en": "Vinegar contains acetic acid (CH3COOH, 5-8% solution). Ant venom contains formic acid (methanoic acid HCOOH).",
            "explanation_te": "వెనిగర్‌లో ఎసిటిక్ ఆమ్లం ఉంటుంది. చీమలు లేదా కందిరీగలు కుట్టినప్పుడు విడుదలయ్యేది ఫార్మిక్ ఆమ్లం."
        },
        # 124. Chemical Names: Baking Soda & Washing Soda
        {
            "id": 124,
            "qNumber": 124,
            "section": "General Studies",
            "topic": "General Science - Chemistry: Common Salts",
            "question_en": "What are the chemical names of Baking Soda and Washing Soda respectively?",
            "question_te": "వంట సోడా (Baking Soda) మరియు బట్టల సోడా (Washing Soda) ల రసాయన నామాలు వరుసగా ఏవి?",
            "options_en": ["Sodium Bicarbonate (NaHCO3) and Sodium Carbonate (Na2CO3.10H2O)", "Sodium Carbonate and Sodium Hydroxide", "Sodium Chloride and Sodium Bicarbonate", "Calcium Carbonate and Sodium Carbonate"],
            "options_te": ["సోడియం బైకార్బోనేట్ (NaHCO3) మరియు సోడియం కార్బోనేట్ (Na2CO3.10H2O)", "సోడియం కార్బోనేట్ మరియు సోడియం హైడ్రాక్సైడ్", "సోడియం క్లోరైడ్ మరియు సోడియం బైకార్బోనేట్", "కాల్షియం కార్బోనేట్ మరియు సోడియం కార్బోనేట్"],
            "correct_option": 0,
            "explanation_en": "Baking soda is Sodium Bicarbonate (NaHCO3). Washing soda is hydrated Sodium Carbonate decahydrate (Na2CO3·10H2O).",
            "explanation_te": "వంట సోడా రసాయన నామం సోడియం బైకార్బోనేట్ (NaHCO3). బట్టల సోడా సోడియం కార్బోనేట్ (Na2CO3·10H2O)."
        },
        # 125. Plaster of Paris & Bleaching Powder
        {
            "id": 125,
            "qNumber": 125,
            "section": "General Studies",
            "topic": "General Science - Chemistry: Industrial Compounds",
            "question_en": "What is the chemical formulation of Plaster of Paris (POP)?",
            "question_te": "ప్లాస్టర్ ఆఫ్ ప్యారిస్ (POP) యొక్క రసాయన సూత్రం ఏది?",
            "options_en": ["CaSO4 . 1/2 H2O", "CaSO4 . 2 H2O", "CaCO3", "CaOCl2"],
            "options_te": ["CaSO4 . 1/2 H2O (కాల్షియం సల్ఫేట్ హెమీహైడ్రేట్)", "CaSO4 . 2 H2O (జిప్సం)", "CaCO3", "CaOCl2 (బ్లీచింగ్ పౌడర్)"],
            "correct_option": 0,
            "explanation_en": "Plaster of Paris is Calcium Sulphate Hemihydrate (CaSO4·1/2H2O), produced by heating gypsum (CaSO4·2H2O) to 373 K.",
            "explanation_te": "జిప్సంను 373 K వద్ద వేడి చేస్తే ప్లాస్టర్ ఆఫ్ ప్యారిస్ (CaSO4·1/2H2O) ఏర్పడుతుంది."
        },
        # 126. Liquid Elements at Room Temperature
        {
            "id": 126,
            "qNumber": 126,
            "section": "General Studies",
            "topic": "General Science - Chemistry: Periodic Table",
            "question_en": "Which metal and which non-metal exist as liquids at room temperature respectively?",
            "question_te": "గది ఉష్ణోగ్రత వద్ద ద్రవ రూపంలో ఉండే ఏకైక లోహం మరియు ఏకైక అలోహం వరుసగా ఏవి?",
            "options_en": ["Mercury and Bromine", "Gallium and Chlorine", "Mercury and Iodine", "Lead and Bromine"],
            "options_te": ["పాదరసం (Mercury) మరియు బ్రోమిన్ (Bromine)", "గాలియం మరియు క్లోరిన్", "పాదరసం మరియు అయోడిన్", "సీసం మరియు బ్రోమిన్"],
            "correct_option": 0,
            "explanation_en": "Mercury (Hg) is the only metallic element liquid at standard room temperature. Bromine (Br) is the only liquid non-metallic element.",
            "explanation_te": "గది ఉష్ణోగ్రత వద్ద ద్రవ స్థితిలో ఉండే లోహం పాదరసం (Hg), మరియు అలోహం బ్రోమిన్ (Br)."
        },
        # 127. Laughing Gas & Dry Ice
        {
            "id": 127,
            "qNumber": 127,
            "section": "General Studies",
            "topic": "General Science - Chemistry: Gases",
            "question_en": "What are the chemical compositions of 'Laughing Gas' and 'Dry Ice'?",
            "question_te": "'లాఫింగ్ గ్యాస్' (నవ్వు పుట్టించే వాయువు) మరియు 'డ్రై ఐస్' (పొడి మంచు) ల రసాయన స్వరూపాలు ఏవి?",
            "options_en": ["Nitrous Oxide (N2O) and Solid Carbon Dioxide (CO2)", "Nitric Oxide (NO) and Solid Methane", "Nitrous Oxide (N2O) and Liquid Nitrogen", "Nitrogen Dioxide (NO2) and Solid CO2"],
            "options_te": ["నైట్రస్ ఆక్సైడ్ (N2O) మరియు ఘన కార్బన్ డయాక్సైడ్ (CO2)", "నైట్రిక్ ఆక్సైడ్ (NO) మరియు ఘన మీథేన్", "నైట్రస్ ఆక్సైడ్ మరియు ద్రవ నైట్రోజన్", "నైట్రోజన్ డయాక్సైడ్ మరియు ఘన CO2"],
            "correct_option": 0,
            "explanation_en": "Laughing gas is Nitrous Oxide (N2O). Dry ice is Carbon Dioxide (CO2) frozen directly in solid form without liquefying.",
            "explanation_te": "లాఫింగ్ గ్యాస్ నైట్రస్ ఆక్సైడ్ (N2O). డ్రై ఐస్ అంటే ఘన స్థితిలో ఉన్న కార్బన్ డయాక్సైడ్ (Solid CO2)."
        },
        # 128. Rusting of Iron
        {
            "id": 128,
            "qNumber": 128,
            "section": "General Studies",
            "topic": "General Science - Chemistry: Chemical Reactions",
            "question_en": "What kind of process is the rusting of iron, and what happens to the weight of an iron nail when it rusts?",
            "question_te": "ఇనుము తుప్పు పట్టడం అనేది ఎలాంటి ప్రక్రియ మరియు ఇనుప మేకు తుప్పు పట్టినప్పుడు దాని బరువులో ఎలాంటి మార్పు వస్తుంది?",
            "options_en": ["Chemical oxidation process; weight increases", "Physical process; weight decreases", "Chemical reduction process; weight remains constant", "Physical change; weight increases"],
            "options_te": ["రసాయన ఆక్సీకరణ ప్రక్రియ; బరువు పెరుగుతుంది", "భౌతిక ప్రక్రియ; బరువు తగ్గుతుంది", "క్షయకరణ ప్రక్రియ; బరువు స్థిరంగా ఉంటుంది", "భౌతిక మార్పు; బరువు పెరుగుతుంది"],
            "correct_option": 0,
            "explanation_en": "Rusting is an electrochemical oxidation reaction forming hydrated iron(III) oxide (Fe2O3·xH2O). Because oxygen and water molecules bond with iron atoms, the weight of the iron object increases.",
            "explanation_te": "తుప్పు పట్టడం రసాయన ఆక్సీకరణ చర్య. ఇనుముకు ఆక్సిజన్ మరియు నీటి అణువులు కలవడం వల్ల తుప్పు పట్టినప్పుడు ఇనుము బరువు పెరుగుతుంది."
        },
        # 129. Purest Form of Carbon & Natural Hardest Substance
        {
            "id": 129,
            "qNumber": 129,
            "section": "General Studies",
            "topic": "General Science - Chemistry: Allotropes of Carbon",
            "question_en": "Which allotrope of carbon is the hardest naturally occurring substance known and has a 3D tetrahedral network structure?",
            "question_te": "త్రిమితీయ టెట్రాహైడ్రల్ స్పటిక నిర్మాణాన్ని కలిగి ఉండి, ప్రకృతిలో లభించే అత్యంత కఠినమైన పదార్థంగా గుర్తించబడిన కార్బన్ రూపాంతరం ఏది?",
            "options_en": ["Diamond", "Graphite", "Fullerene", "Graphene"],
            "options_te": ["వజ్రం (Diamond)", "గ్రాఫైట్", "ఫుల్లరీన్", "గ్రాఫేన్"],
            "correct_option": 0,
            "explanation_en": "Diamond is an allotrope of carbon where each carbon atom is covalently bonded to 4 others in a rigid tetrahedral lattice, making it the hardest natural material with a Mohs hardness of 10.",
            "explanation_te": "వజ్రం కార్బన్ యొక్క రూపాంతరం, దృఢమైన టెట్రాహైడ్రల్ బంధాల వల్ల ఇది ప్రకృతిలో అత్యంత కఠినమైన పదార్థం (Mohs స్కేలుపై 10)."
        },
        # 130. Greenhouse Gases & Global Warming
        {
            "id": 130,
            "qNumber": 130,
            "section": "General Studies",
            "topic": "General Science - Environmental Science",
            "question_en": "Which gas contributes the most to the greenhouse effect on planet Earth?",
            "question_te": "భూమిపై హరితగృహ ప్రభావానికి (Greenhouse effect) అత్యధికంగా దోహదపడే సహజ వాయువు ఏది?",
            "options_en": ["Water Vapour", "Carbon Dioxide", "Methane", "Ozone"],
            "options_te": ["నీటి ఆవిరి (Water Vapour)", "కార్బన్ డయాక్సైడ్", "మీథేన్", "ఓజోన్"],
            "correct_option": 0,
            "explanation_en": "Water vapour is the most potent natural greenhouse gas, accounting for 36-70% of Earth's natural greenhouse warming, followed by Carbon Dioxide (9-26%).",
            "explanation_te": "భూమి సహజ హరితగృహ ప్రభావంలో 36-70% వాటా నీటి ఆవిరిదే, ఆ తర్వాత కార్బన్ డయాక్సైడ్ (9-26%) ఉంటుంది."
        }
    ]

print("Science module loaded with 30 high-yield questions.")
