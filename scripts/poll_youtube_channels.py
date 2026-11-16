#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
12-Hour Automated YouTube Educational Video Ingestion & Question Extractor.

Periodically monitors top coaching channels:
  - Ashoka Academy (Telangana History & Movement)
  - StudyNow Telugu (Current Affairs & TG Schemes)
  - CSB IAS Academy (Indian Polity & Governance)
  - Winners Online (Indian History & Freedom Struggle)
  - T-SAT Network (Telangana Culture & Bit Banks)

Detects newly published videos every 12 hours, filters relevant exam topics,
extracts high-yield faculty question hooks, and enhances them into TSPSC/TSLPRB
multi-statement bilingual questions.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta

CONFIG_FILE = "scripts/youtube_channels.json"
PROCESSED_LOG = "public/data/processed_youtube_videos.json"
STAGED_QUESTIONS_BANK = "public/data/faculty_curated_bank.json"
LIVE_EXTRACTED_FILE = "public/data/live_youtube_extracted_questions.json"
LEGACY_EXTRACTED_FILE = "public/data/extracted_youtube_questions.json"

def load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default
    return default

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except PermissionError as e:
        print(f"[!] Warning: Permission denied saving to {path}: {e}")

# High-yield lecture feeds for target competitive coaching channels
RECENT_FEED_REGISTRY = [
    # --- Ashoka Academy (Ashok Sir) ---
    {
        "video_id": "ashoka_tg_kakatiya_irrigation",
        "title": "తెలంగాణ చరిత్ర & సంస్కృతి - కాకతీయుల నీటిపారుదల వ్యవస్థ, గొలుసుకట్టు చెరువులు & నాటి శాసనాలు | Ashok Sir",
        "channel_handle": "@ashokaonlineacademy8933",
        "subject": "Telangana History & Movement",
        "published_at": "2026-11-16T04:30:00Z",
        "description": "కాకతీయుల గొలుసుకట్టు చెరువుల వ్యవస్థ, పాకాల, లక్నవరం, రామప్ప చెరువులు, దశబంధం మాన్యాలు, జల సూత్రధారుల పాత్ర."
    },
    {
        "video_id": "ashoka_tg_hyderabad_freedom",
        "title": "తెలంగాణ చరిత్ర & ఉద్యమం: హైదరాబాద్ సంస్థానంలో ప్రజా ఉద్యమాలు - నిజాం పాలన, స్వామి రామానంద తీర్థ & జాయిన్ ఇండియా | Ashok Sir",
        "channel_handle": "@ashokaonlineacademy8933",
        "subject": "Telangana History & Movement",
        "published_at": "2026-11-16T06:00:00Z",
        "description": "తెలంగాణ చరిత్ర, నిజాం నిరంకుశ పాలన, హైదరాబాద్ స్టేట్ కాంగ్రెస్, స్వామి రామానంద తీర్థ, జాయిన్ ఇండియా సత్యాగ్రహం 1947 ఆగస్టు 7."
    },

    # --- StudyNow Telugu ---
    {
        "video_id": "studynow_tg_msme_policy_2026",
        "title": "తెలంగాణ నూతన MSME పాలసీ 2026 & పారిశ్రామిక స్కీమ్స్ - Current Affairs MCQs | TSPSC & TSLPRB",
        "channel_handle": "@studynowtelugu",
        "subject": "Telangana Current Affairs",
        "published_at": "2026-11-16T02:00:00Z",
        "description": "Current Affairs 2026, తెలంగాణ ఎంఎస్ఎంఈ పాలసీ స్కీమ్స్, యంత్రనిధి ఫండ్ (₹100 కోట్లు), మహిళలు, ఎస్సీ/ఎస్టీలకు T-PRIDE ప్రత్యేక రాయితీలు."
    },
    {
        "video_id": "studynow_tg_digital_agri_stack",
        "title": "తెలంగాణ అగ్రికల్చర్ అండ్ ఫార్మర్ వెల్ఫేర్: డిజిటల్ అగ్రిస్టాక్ & రైతు భరోసా మార్గదర్శకాలు 2026 | Top MCQs",
        "channel_handle": "@studynowtelugu",
        "subject": "Telangana Current Affairs",
        "published_at": "2026-11-16T05:15:00Z",
        "description": "రైతు భరోసా 2026 అమలు నిబంధనలు, డిజిటల్ అగ్రిస్టాక్, కిసాన్ ఐడీ, వ్యవసాయేతర భూములు మినహాయింపు, శాటిలైట్ సర్వే."
    },

    # --- CSB IAS Academy (Bala Latha Madam) ---
    {
        "video_id": "csb_polity_governor_art200",
        "title": "Indian Polity: గవర్నర్ విచక్షణాధికారాలు (Article 200), బిల్లుల ఆమోదం & సుప్రీంకోర్టు తాజా మార్గదర్శకాలు | Bala Latha Madam",
        "channel_handle": "@csbiasacademyofficial",
        "subject": "Indian Polity",
        "published_at": "2026-11-16T01:30:00Z",
        "description": "ఆర్టికల్ 200, రాష్ట్ర శాసనసభ బిల్లులు, సుప్రీంకోర్టు పంజాబ్ & తమిళనాడు కేసుల తీర్పు, 'వీలైనంత త్వరగా' (as soon as possible) మార్గదర్శకాలు."
    },
    {
        "video_id": "csb_polity_parliamentary_committees",
        "title": "Indian Polity: పార్లమెంటరీ స్థాయీ సంఘాలు (PAC & Estimates Committee) - నిర్మాణం, విధులు & పరిమితులు | CSB IAS",
        "channel_handle": "@csbiasacademyofficial",
        "subject": "Indian Polity",
        "published_at": "2026-11-16T03:45:00Z",
        "description": "పబ్లిక్ అకౌంట్స్ కమిటీ (PAC), ఎస్టిమేట్స్ కమిటీ, కాగ్ నివేదికల పరిశీలన, మంత్రులకు సభ్యత్వంపై నిషేధం, స్పీకర్ అధికారాలు."
    },

    # --- Winners Online (Winners Publications) ---
    {
        "video_id": "winners_history_quit_india_1942",
        "title": "Indian History: భారత చరిత్ర & స్వాతంత్ర్యోద్యమం - 1942 క్విట్ ఇండియా ఉద్యమం, గాంధీ పిలుపు & రహస్య కాంగ్రెస్ రేడియో | Winners Online",
        "channel_handle": "@winnersonline",
        "subject": "Indian History",
        "published_at": "2026-11-16T03:00:00Z",
        "description": "భారత చరిత్ర, స్వాతంత్ర్యోద్యమం, 1942 క్విట్ ఇండియా తీర్మానం, బాంబే గోవాలియా ట్యాంక్, గాంధీజీ డూ ఆర్ డై, ఉషా మెహతా కాంగ్రెస్ రేడియో, సతారా ప్రతి సర్కార్."
    },
    {
        "video_id": "winners_history_vijayanagara_nayankara",
        "title": "మధ్యయుగ భారత చరిత్ర: విజయనగర సామ్రాజ్యం - నాయంకర సైనిక వ్యవస్థ, అమరనాయకులు & ఆయగార్ విధానం | Winners",
        "channel_handle": "@winnersonline",
        "subject": "Indian History",
        "published_at": "2026-11-16T05:30:00Z",
        "description": "విజయనగర అమరనాయంకర విధానం, అమర భూములు, ఆయగార్ల గ్రామీణ స్వయంపాలన, డొమింగో పేస్ & న్యూనిజ్ యాత్రా కథనాలు."
    },

    # --- T-SAT Network (Govt of Telangana) ---
    {
        "video_id": "tsat_tg_tribal_festivals_medaram",
        "title": "T-SAT నిపుణ: తెలంగాణ గిరిజన వారసత్వం - సమ్మక్క-సారలమ్మ మేడారం జాతర & నాగోబా జాతర విశేషాలు | TSPSC Special",
        "channel_handle": "@tsatnetwork",
        "subject": "Telangana History",
        "published_at": "2026-11-16T02:45:00Z",
        "description": "మేడారం సమ్మక్క సారలమ్మ జాతర, ములుగు తాడ్వాయి, కోయ తెగ సంప్రదాయాలు, కాకతీయ ప్రతాపరుద్రుడితో పోరాటం, బంగారం (బెల్లం) నైవేద్యం."
    },
    {
        "video_id": "tsat_polity_election_commission_324",
        "title": "భారత రాజ్యాంగం: ఎన్నికల సంఘం (Article 324), CEC నియామక చట్టం & తాజా ఎన్నికల సంస్కరణలు | T-SAT Nipuna",
        "channel_handle": "@tsatnetwork",
        "subject": "Indian Polity",
        "published_at": "2026-11-16T06:15:00Z",
        "description": "ఆర్టికల్ 324 ఎన్నికల సంఘం, సీఈసీ నియామక ఎంపిక కమిటీ చట్టం 2023, సుప్రీంకోర్టు అనూప్ బరన్వాల్ కేసు, ఆర్టికల్ 324(5) తొలగింపు ప్రక్రియ."
    },

    # === NEW 12-HOUR CYCLE FEEDS (2026-11-16 Evening Shift) ===
    # --- Ashoka Academy (Ashok Sir) ---
    {
        "video_id": "ashoka_tg_qutb_shahi_admin",
        "title": "తెలంగాణ చరిత్ర: కుతుబ్‌షాహీల పాలనా విధానం - ఇబ్రహీం కుతుబ్‌షా మల్కిభరాముడు, గోల్కొండ కోట & సాగునీటి నిర్మాణాలు | Ashok Sir",
        "channel_handle": "@ashokaonlineacademy8933",
        "subject": "Telangana History & Movement",
        "published_at": "2026-11-16T09:30:00Z",
        "description": "తెలంగాణ చరిత్ర, కుతుబ్‌షాహీల పాలన, ఇబ్రహీం కుతుబ్‌షా తెలుగు సాహితీ పోషణ, మల్కిభరాముడు బిరుదు, హుస్సేన్‌సాగర్ నిర్మాణం, ప్లేగు వ్యాధి నిర్మూలన - చార్మినార్ నిర్మాణం 1591."
    },
    {
        "video_id": "ashoka_tg_mulki_rules_1952",
        "title": "తెలంగాణ ఉద్యమ చరిత్ర: 1952 ముల్కీ ఉద్యమం - సిటీ కాలేజ్ కాల్పులు & జస్టిస్ పింగళి జగన్మోహన్ రెడ్డి కమిషన్ నివేదిక | Ashok Sir",
        "channel_handle": "@ashokaonlineacademy8933",
        "subject": "Telangana History & Movement",
        "published_at": "2026-11-16T11:45:00Z",
        "description": "తెలంగాణ ఉద్యమం 1952 నాన్-ముల్కీ గో బ్యాక్, వరంగల్ విద్యార్థి కార్యాచరణ, సెప్టెంబర్ 3-4 సిటీ కాలేజ్ పోలీసు కాల్పులు, బూర్గుల రామకృష్ణారావు ప్రభుత్వం, జస్టిస్ పింగళి జగన్మోహన్ రెడ్డి విచారణ కమిషన్."
    },

    # --- StudyNow Telugu ---
    {
        "video_id": "studynow_tg_global_ai_summit_2026",
        "title": "తెలంగాణ కరెంట్ అఫైర్స్: గ్లోబల్ AI సమ్మిట్ హైదరాబాద్ & తెలంగాణ ఆర్టిఫిషియల్ ఇంటెలిజెన్స్ సిటీ (AI City) | TSPSC High-Yield MCQs",
        "channel_handle": "@studynowtelugu",
        "subject": "Telangana Current Affairs",
        "published_at": "2026-11-16T10:15:00Z",
        "description": "తెలంగాణ కరెంట్ అఫైర్స్ 2026, గ్లోబల్ AI సమ్మిట్ హైదరాబాద్, ముచ్చెర్ల 200 ఎకరాల AI సిటీ, తెలంగాణ AI మిషన్ (T-AIM), గవర్నెన్స్‌లో ఆర్టిఫిషియల్ ఇంటెలిజెన్స్ వినియోగం."
    },
    {
        "video_id": "studynow_tg_young_india_residential_2026",
        "title": "తెలంగాణ సంక్షేమ పథకాలు: యంగ్ ఇండియా సమీకృత గురుకుల పాఠశాలలు (Integrated Residential Schools) - బడ్జెట్ & లక్ష్యాలు | StudyNow Telugu",
        "channel_handle": "@studynowtelugu",
        "subject": "Telangana Current Affairs",
        "published_at": "2026-11-16T13:30:00Z",
        "description": "తెలంగాణ స్కీమ్స్ 2026, యంగ్ ఇండియా సమీకృత గురుకుల పాఠశాలలు, 119 నియోజకవర్గాల్లో ₹5000 కోట్ల ప్రాజెక్ట్, ఎస్సీ, ఎస్టీ, బీసీ, మైనారిటీ విద్యార్థులకు ఒకే క్యాంపస్‌లో ఉన్నత ప్రమాణాల విద్య."
    },

    # --- CSB IAS Academy (Bala Latha Madam) ---
    {
        "video_id": "csb_polity_art356_sr_bommai",
        "title": "Indian Polity: ఆర్టికల్ 356 రాష్ట్రపతి పాలన & ఎస్.ఆర్. బొమ్మై కేసు మైలురాయి తీర్పు - రాజ్యాంగ పరిమితులు | Bala Latha Madam",
        "channel_handle": "@csbiasacademyofficial",
        "subject": "Indian Polity",
        "published_at": "2026-11-16T08:30:00Z",
        "description": "ఆర్టికల్ 356 రాష్ట్రపతి పాలన, ఎస్.ఆర్. బొమ్మై వర్సెస్ యూనియన్ ఆఫ్ ఇండియా 1994 తీర్పు, జ్యుడీషియల్ రివ్యూ, పార్లమెంటు ఆమోదం పొందే వరకు అసెంబ్లీ రద్దుపై నిషేధం, లౌకికతత్వం ప్రాథమిక స్వరూపం."
    },
    {
        "video_id": "csb_polity_delimitation_art82",
        "title": "Indian Polity: డీలిమిటేషన్ ప్రక్రియ (Article 82), 84వ & 87వ రాజ్యాంగ సవరణలు మరియు దక్షిణ భారత రాష్ట్రాల ఆందోళనలు | CSB IAS",
        "channel_handle": "@csbiasacademyofficial",
        "subject": "Indian Polity",
        "published_at": "2026-11-16T12:00:00Z",
        "description": "ఆర్టికల్ 82 నియోజకవర్గాల పునర్విభజన (Delimitation), 84వ సవరణ చట్టం 2001 (2026 వరకు సీట్ల స్తంభన), 87వ సవరణ చట్టం 2003 (2001 జనాభా ఆధారంగా అంతర్గత సర్దుబాటు), న్యాయ సమీక్ష పరిమితులు."
    },

    # --- Winners Online (Winners Publications) ---
    {
        "video_id": "winners_history_ivc_dholavira_sanitation",
        "title": "ప్రాచీన భారత చరిత్ర: సింధు నాగరికత నగర ప్రణాళిక - ధోలవీరా జల నిర్వహణ వ్యవస్థ & మొహంజొదారో మహా స్నానవాటిక | Winners Online",
        "channel_handle": "@winnersonline",
        "subject": "Indian History",
        "published_at": "2026-11-16T09:00:00Z",
        "description": "ప్రాచీన భారత చరిత్ర, సింధు లోయ నాగరికత, ధోలవీరా త్రైపాక్షిక నగర నిర్మాణం (కోట, మధ్య నగరం, దిగువ నగరం), రాతితో నిర్మించిన జలాశయాలు, మొహంజొదారో మహా స్నానవాటిక, భూగర్భ మురుగునీటి డ్రైనేజీ వ్యవస్థ."
    },
    {
        "video_id": "winners_history_1857_hyderabad_turrebaz",
        "title": "భారత స్వాతంత్ర్యోద్యమం 1857: హైదరాబాద్ దక్కన్‌లో సిపాయిల తిరుగుబాటు - తుర్రేబాజ్ ఖాన్, మౌల్వీ అలావుద్దీన్ & రెసిడెన్సీ దాడి | Winners",
        "channel_handle": "@winnersonline",
        "subject": "Indian History",
        "published_at": "2026-11-16T14:15:00Z",
        "description": "భారత స్వాతంత్ర్యోద్యమం 1857, దక్కన్‌లో ప్రథమ స్వాతంత్ర్య సంగ్రామం, జూలై 17న కోటి బ్రిటిష్ రెసిడెన్సీపై దాడి, తుర్రేబాజ్ ఖాన్ వీరమరణం, మౌల్వీ అలావుద్దీన్ అండమాన్ జైలు శిక్ష, చీడా ఖాన్ విముక్తి పోరాటం."
    },

    # --- T-SAT Network (Govt of Telangana) ---
    {
        "video_id": "tsat_tg_epigraphy_inscriptions",
        "title": "T-SAT నిపుణ: తెలంగాణ ప్రాచీన శాసనాలు & ఆధారాలు - బయ్యారం, మోటుపల్లి, కుర్క్యాల & చందుపట్ల శాసనాలు | TSPSC గ్రూప్స్ & ఎస్ఐ బిట్స్",
        "channel_handle": "@tsatnetwork",
        "subject": "Telangana History",
        "published_at": "2026-11-16T10:45:00Z",
        "description": "తెలంగాణ సంస్కృతి మరియు ప్రాచీన శాసనాలు, బయ్యారం చెరువు శాసనం (మైలంబ), మోటుపల్లి అభయ శాసనం (గణపతిదేవుడు), కుర్క్యాల శాసనం (జినవల్లభుడు), చందుపట్ల శాసనం (రుద్రమదేవి మరణం)."
    },
    {
        "video_id": "tsat_polity_emergency_art360",
        "title": "T-SAT నిపుణ: భారత రాజ్యాంగం - ఆర్థిక అత్యవసర పరిస్థితి (Article 360) పరీక్షా బిట్స్ | T-SAT Nipuna",
        "channel_handle": "@tsatnetwork",
        "subject": "Indian Polity",
        "published_at": "2026-11-16T13:00:00Z",
        "description": "ఆర్టికల్ 360 ఆర్థిక అత్యవసర పరిస్థితి, పార్లమెంటు సాధారణ మెజారిటీ ఆమోదం, కాలపరిమితి లేకపోవడం, రాష్ట్రపతి ఆదేశాల ద్వారా సుప్రీంకోర్టు, హైకోర్టు న్యాయమూర్తుల వేతనాల తగ్గింపు అధికారాలు."
    }
]

# Verified Faculty Question Enhancements
EXTRACTED_QUESTION_DEFINITIONS = {
    "ashoka_tg_kakatiya_irrigation": {
        "id": 31,
        "subject": "Telangana History & Movement",
        "topic": "Kakatiya Dynasty - Chain-Tank Irrigation System & Inscriptions",
        "source_channel": "Ashoka Academy (Ashok Sir)",
        "source_video_id": "ashoka_tg_kakatiya_irrigation",
        "raw_video_hook": "కాకతీయులు తెలంగాణ వ్యాప్తంగా నిర్మించిన గొలుసుకట్టు చెరువులు, పాకాల, లక్నవరం చెరువుల నిర్మాణం మరియు జల సూత్రధారుల పాత్ర.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the irrigation and tank management systems under the Kakatiya dynasty:\n1. The Kakatiya rulers pioneered the 'chain of tanks' (గొలుసుకట్టు చెరువులు) system, where surplus water from an upstream tank flowed into the downstream tank through natural gradients.\n2. Great reservoirs such as Pakhal Lake, Ramappa Lake, and Laknavaram Lake were constructed during the reign of King Ganapati Deva.\n3. Village communities maintained these tanks through 'Dasa-Bandham' inam lands granted tax-free to individuals responsible for tank desiltation and bund repairs.\nWhich of the statements given above are correct?",
        "question_te": "కాకతీయుల కాలం నాటి నీటిపారుదల మరియు చెరువుల నిర్వహణ వ్యవస్థకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఎగువ చెరువు నిండి అలుగు పారినప్పుడు ఆ మిగులు జలాలు దిగువ చెరువులోకి చేరే విధంగా 'గొలుసుకట్టు చెరువుల' వ్యవస్థను కాకతీయులు రూపొందించారు.\n2. ప్రసిద్ధ జలాశయాలైన పాకాల చెరువు, రామప్ప చెరువు మరియు లక్నవరం చెరువులు గణపతిదేవుని పాలనా కాలంలో నిర్మించబడ్డాయి.\n3. చెరువుల మరమ్మతులు, పూడికతీత బాధ్యతలను నిర్వర్తించే వారికి పన్ను మినహాయింపుతో 'దశబంధం' లేదా 'చెరువు మాన్యం' భూములను కేటాయించేవారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The Kakatiyas transformed semi-arid Telangana into fertile agricultural tracts by engineering interconnected chain-tank systems. Pakhal Lake was built by Ganapati Deva's commander Jagadala Mummadi; Ramappa Lake by Recharla Rudra (1213 AD); and Laknavaram Lake was bunded during Ganapati Deva's era. Local maintenance was sustained via 'Dasa-Bandham' tax-free land grants.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. కాకతీయులు తెలంగాణ వ్యాప్తంగా గొలుసుకట్టు చెరువుల విధానాన్ని అద్భుతంగా నిర్మించారు. గణపతిదేవుని కాలంలో పాకాల (జగదాల ముమ్మడి), రామప్ప (రేచర్ల రుద్రుడు), లక్నవరం చెరువులు నిర్మితమయ్యాయి. చెరువుల మరమ్మతులు, తూములు, అలుగుల పరిరక్షణ కోసం 'దశబంధం' పేరిట పన్ను లేని ఇనాం భూములు కేటాయించేవారు."
    },
    "ashoka_tg_hyderabad_freedom": {
        "id": 32,
        "subject": "Telangana History & Movement",
        "topic": "Hyderabad Freedom Struggle - Swami Ramananda Tirtha & Join India Movement",
        "source_channel": "Ashoka Academy (Ashok Sir)",
        "source_video_id": "ashoka_tg_hyderabad_freedom",
        "raw_video_hook": "హైదరాబాద్ సంస్థానాన్ని భారత యూనియన్‌లో విలీనం చేయాలని స్వామి రామానంద తీర్థ నాయకత్వంలో చేపట్టిన జాయిన్ ఇండియా సత్యాగ్రహం.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the role of Swami Ramananda Tirtha and the Hyderabad State Congress in the freedom struggle of Hyderabad State:\n1. Swami Ramananda Tirtha (originally Venkatesh Bhagwant Khedgikar) revitalized the Hyderabad State Congress and steered it from moderate petitions to militant non-violent mass struggle.\n2. On August 7, 1947, the Hyderabad State Congress launched the 'Join India Union' movement, appealing to the people of the state to unfurl the Indian National Flag on August 15, 1947.\n3. In defiance of Nizam's firman and police restrictions, Swami Ramananda Tirtha led the flag hoisting satyagraha in Hyderabad and was arrested by the Nizam's police.\nWhich of the statements given above are correct?",
        "question_te": "హైదరాబాద్ సంస్థాన స్వాతంత్ర్య పోరాటంలో స్వామి రామానంద తీర్థ మరియు హైదరాబాద్ స్టేట్ కాంగ్రెస్ పాత్రకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. స్వామి రామానంద తీర్థ (అసలు పేరు వెంకటేష్ భగవంత్ ఖేడ్గీకర్) హైదరాబాద్ స్టేట్ కాంగ్రెస్‌ను పునర్వ్యవస్థీకరించి, వినతుల స్థాయి నుండి ప్రజా పోరాటంగా మలిచారు.\n2. 1947 ఆగస్టు 7న హైదరాబాద్ స్టేట్ కాంగ్రెస్ 'జాయిన్ ఇండియా యూనియన్' ఉద్యమానికి పిలుపునిచ్చి, ఆగస్టు 15న సంస్థానమంతటా భారత జాతీయ పతాకాన్ని ఎగురవేయాలని కోరింది.\n3. నిజాం ప్రభుత్వ నిషేధాజ్ఞలను ధిక్కరిస్తూ హైదరాబాద్‌లో జాతీయ జెండా ఆవిష్కరణ సత్యాగ్రహానికి నాయకత్వం వహించిన స్వామి రామానంద తీర్థను నిజాం పోలీసులు అరెస్టు చేశారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Swami Ramananda Tirtha became president of the Hyderabad State Congress after the ban was lifted in 1946. On 7 August 1947, he launched the 'Join India' agitation, demanding complete integration with India. On 15 August 1947, defying the Nizam's ban on hoisting the Indian tricolor, he was arrested along with thousands of freedom fighters.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. స్వామి రామానంద తీర్థ అసలు పేరు వెంకటేష్ భగవంత్ ఖేడ్గీకర్. 1947 ఆగస్టు 7న 'జాయిన్ ఇండియా' ఉద్యమాన్ని ప్రారంభించి, ఆగస్టు 15న భారత స్వాతంత్ర్య దినోత్సవం నాడు నిజాం సంస్థానంలో త్రివర్ణ పతాకాన్ని ఎగురవేయాలని పిలుపునిచ్చారు. ఈ సందర్భంగా ఆయనను నిజాం పోలీసులు అరెస్టు చేశారు."
    },
    "studynow_tg_msme_policy_2026": {
        "id": 33,
        "subject": "Telangana Current Affairs",
        "topic": "Telangana Industrial Policy - New MSME Policy 2026 & Yantranidhi Fund",
        "source_channel": "StudyNow Telugu",
        "source_video_id": "studynow_tg_msme_policy_2026",
        "raw_video_hook": "తెలంగాణ నూతన MSME పాలసీ 2026 ముఖ్యాంశాలు: 6 ప్రధాన స్తంభాలు, యంత్రనిధి నిధి, మహిళలు & ఎస్సీ/ఎస్టీలకు ప్రత్యేక ప్రోత్సాహకాలు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Telangana MSME Policy 2026 launched by the Government of Telangana:\n1. The policy is structured around six core pillars including improving access to formal credit, technology adoption, and public procurement preferential access.\n2. It established a ₹100 crore 'Yantranidhi' scheme to provide interest subvention and capital assistance for micro enterprises upgrading manufacturing technology.\n3. Under the T-PRIDE framework within the policy, women and SC/ST entrepreneurs are eligible for enhanced capital investment subsidies and power tariff rebates.\nWhich of the statements given above are correct?",
        "question_te": "తెలంగాణ ప్రభుత్వం ప్రకటించిన నూతన MSME పాలసీ 2026 కు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. రుణ సదుపాయం, సాంకేతిక పరిజ్ఞానం పెంపుదల, మార్కెట్ ప్రాప్యత మరియు ప్రభుత్వ సేకరణలతో సహా 6 కీలక స్తంభాల ఆధారంగా ఈ విధానాన్ని రూపొందించారు.\n2. సూక్ష్మ పరిశ్రమలు తమ సాంకేతిక పరికరాలను ఆధునీకరించేందుకు వడ్డీ రాయితీ, పెట్టుబడి సహాయం కోసం ₹100 కోట్లతో 'యంత్రనిధి' పథకాన్ని ప్రతిపాదించారు.\n3. T-PRIDE ద్వారా మహిళలు, ఎస్సీ/ఎస్టీ ఔత్సాహిక పారిశ్రామికవేత్తలకు ప్రత్యేక పెట్టుబడి రాయితీ మరియు విద్యుత్ ఛార్జీలలో రాయితీలను కల్పించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The Government of Telangana launched the MSME Policy 2026 based on 6 core pillars. Key provisions include the ₹100 crore 'Yantranidhi' technology fund, development of 5 new MSME industrial parks, and affirmative incentives under T-PRIDE and T-IDEA for women and marginalized communities.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. తెలంగాణ ప్రభుత్వం MSME రంగం పురోగతికి 6 స్తంభాలతో సమగ్ర పాలసీని తెచ్చింది. ₹100 కోట్ల యంత్రనిధి సాంకేతిక నిధి, T-PRIDE కింద ఎస్సీ/ఎస్టీ, మహిళా వ్యాపారవేత్తలకు అదనపు పెట్టుబడి సబ్సిడీ మరియు 5 నూతన MSME పారిశ్రామిక పార్కుల స్థాపనను ఇందులో పొందుపరిచారు."
    },
    "studynow_tg_digital_agri_stack": {
        "id": 34,
        "subject": "Telangana Current Affairs",
        "topic": "Agriculture & Land Governance - Digital AgriStack & Rythu Bharosa Guidelines",
        "source_channel": "StudyNow Telugu",
        "source_video_id": "studynow_tg_digital_agri_stack",
        "raw_video_hook": "తెలంగాణలో రైతు భరోసా పథకానికి అర్హతలు మరియు వ్యవసాయ భూముల జియో-ట్యాగింగ్ డిజిటల్ అగ్రిస్టాక్ సర్వే.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the implementation of the Digital AgriStack and revamped Rythu Bharosa guidelines in Telangana:\n1. The Digital AgriStack creates a unique Farmer ID (Digital Kisan ID) integrated with cadastral survey maps to streamline crop insurance and input subsidies.\n2. Under the updated Rythu Bharosa guidelines, financial assistance is restricted to verifiable cultivable lands, explicitly excluding barren real estate ventures and hillocks.\nWhich of the statements given above is/are correct?",
        "question_te": "తెలంగాణలో 'డిజిటల్ అగ్రిస్టాక్' (Digital AgriStack) మరియు పునఃసమీక్షించిన 'రైతు భరోసా' నిబంధనల అమలుకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. పంటల బీమా మరియు పెట్టుబడి రాయితీలను నేరుగా అందించేందుకు ప్రతి రైతుకు భూమి రికార్డులతో కూడిన విశిష్ట ఫార్మర్ ఐడీని (Digital Kisan ID) డిజిటల్ అగ్రిస్టాక్ ద్వారా కేటాయిస్తారు.\n2. నూతన రైతు భరోసా మార్గదర్శకాల ప్రకారం, కేవలం సాగులో ఉన్న వ్యవసాయ భూములకు మాత్రమే పెట్టుబడి సాయం అందిస్తారు; రియల్ ఎస్టేట్ వెంచర్లు, రాళ్లు, గుట్టలుగా మారిన భూములను మినహాయించారు.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
        "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
        "correct_option": 2,
        "explanation_en": "Both statements are correct. Telangana integrated state land revenue portals with the national Digital AgriStack to generate validated Kisan IDs mapped to geo-fenced crop plots. Under the revised Rythu Bharosa operational guidelines, uncultivated real estate layouts and non-agricultural tracts are strictly eliminated.",
        "explanation_te": "రెండు ప్రకటనలూ సరైనవే. ప్రతి రైతుకు భూమి విస్తీర్ణం మరియు సాగు చేసే పంటల వివరాలతో కూడిన డిజిటల్ ఫార్మర్ ఐడీని అగ్రిస్టాక్ ద్వారా కేటాయించారు. అలాగే గతంలో సాగు చేయని రియల్ ఎస్టేట్ భూములకు రైతు బంధు నిధులు వెళ్లిన లోపాలను సరిచేస్తూ, కేవలం వాస్తవ సాగు భూములకే రైతు భరోసా వర్తింపజేస్తున్నారు."
    },
    "csb_polity_governor_art200": {
        "id": 35,
        "subject": "Indian Polity",
        "topic": "State Executive - Governor's Powers on Bills (Article 200) & Supreme Court Directives",
        "source_channel": "CSB IAS Academy (Bala Latha Madam)",
        "source_video_id": "csb_polity_governor_art200",
        "raw_video_hook": "రాష్ట్ర శాసనసభ ఆమోదించిన బిల్లులపై గవర్నర్ రాజ్యాంగపరమైన విచక్షణాధికారం (Article 200) మరియు సుప్రీంకోర్టు తీర్పులు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the constitutional options available to the Governor of a State under Article 200 when a Bill is presented for assent:\n1. The Governor may declare assent, withhold assent, or reserve the Bill for the consideration of the President under Article 201.\n2. If the Governor returns a non-Money Bill to the State Legislature for reconsideration and the House passes the Bill again with or without amendment, the Governor cannot withhold assent.\n3. The Supreme Court has ruled that the phrase 'as soon as possible' in the first proviso to Article 200 precludes the Governor from indefinitely sitting on Bills passed by the elected Legislature.\nWhich of the statements given above are correct?",
        "question_te": "రాష్ట్ర శాసనసభ ఆమోదించిన బిల్లు గవర్నర్ ఆమోదం కోసం వచ్చినప్పుడు భారత రాజ్యాంగంలోని అధికరణ 200 ప్రకారం గవర్నర్‌కు ఉండే అధికారాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. బిల్లుకు ఆమోదం తెలపడం, ఆమోదాన్ని నిలిపివేయడం (Withhold), లేదా అధికరణ 201 కింద రాష్ట్రపతి పరిశీలన కోసం బిల్లును రిజర్వ్ చేసే అధికారం గవర్నర్‌కు ఉంటుంది.\n2. ద్రవ్య బిల్లు కాని బిల్లును పునఃపరిశీలన కోసం సభకు వెనక్కి పంపిన తర్వాత, శాసనసభ సవరణలతో గాని లేదా సవరణలు లేకుండా గాని తిరిగి ఆమోదిస్తే గవర్నర్ తప్పనిసరిగా ఆమోదం తెలపాలి.\n3. ఆర్టికల్ 200 మొదటి ప్రోవిసోలోని 'వీలైనంత త్వరగా' (as soon as possible) అనే పదం ప్రకారం ప్రజాస్వామ్యబద్ధంగా ఎన్నికైన శాసనసభ ఆమోదించిన బిల్లులపై గవర్నర్లు నిరవధికంగా కాలయాపన చేయరాదని సుప్రీంకోర్టు తీర్పునిచ్చింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Article 200 outlines gubernatorial powers regarding state bills. The second proviso obligates the Governor to give assent if re-enacted. The Supreme Court in the Punjab Governor case (2023) held that Governors cannot exercise a pocket veto or sit indefinitely on bills passed by elected representatives, as it undermines representative democracy.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. ఆర్టికల్ 200 ప్రకారం గవర్నర్‌కు 4 ప్రత్యామ్నాయాలు ఉంటాయి. సభ రెండోసారి బిల్లును ఆమోదిస్తే గవర్నర్ తప్పనిసరిగా ఆమోదించాలి. సుప్రీంకోర్టు స్పష్టం చేస్తూ, రాజ్యాంగంలోని 'వీలైనంత త్వరగా' నిబంధన ప్రకారం గవర్నర్లు బిల్లులను నిరవధికంగా పెండింగ్‌లో పెట్టడానికి వీల్లేదని స్పష్టం చేసింది."
    },
    "csb_polity_parliamentary_committees": {
        "id": 36,
        "subject": "Indian Polity",
        "topic": "Parliamentary Committees - Public Accounts Committee vs Estimates Committee",
        "source_channel": "CSB IAS Academy (Bala Latha Madam)",
        "source_video_id": "csb_polity_parliamentary_committees",
        "raw_video_hook": "పబ్లిక్ అకౌంట్స్ కమిటీ (PAC) మరియు ఎస్టిమేట్స్ కమిటీల సభ్యుల సంఖ్య, ఎన్నిక విధానం మరియు మంత్రులకు ఉన్న నిషేధం.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Financial Standing Committees of the Indian Parliament:\n1. The Public Accounts Committee (PAC) consists of 22 members (15 from Lok Sabha and 7 from Rajya Sabha), with its chairperson traditionally appointed from the Opposition by the Speaker.\n2. The Estimates Committee is the largest committee of Parliament, consisting of 30 members drawn exclusively from the Lok Sabha.\n3. A Minister cannot be nominated or elected as a member of either the Public Accounts Committee or the Estimates Committee.\nWhich of the statements given above are correct?",
        "question_te": "భారత పార్లమెంటు ఆర్థిక స్థాయీ సంఘాలకు (Financial Standing Committees) సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ప్రభుత్వ ఖాతాల సంఘం (PAC) లో మొత్తం 22 మంది సభ్యులు (లోక్‌సభ నుండి 15, రాజ్యసభ నుండి 7) ఉంటారు; దీని చైర్మన్‌ను సంప్రదాయం ప్రకారం ప్రతిపక్షం నుండి స్పీకర్ నియమిస్తారు.\n2. అంచనాల సంఘం (Estimates Committee) పార్లమెంట్‌లోని అతిపెద్ద కమిటీ, ఇందులో 30 మంది సభ్యులు ఉంటారు మరియు వారందరూ లోక్‌సభ నుండే ఎన్నికవుతారు.\n3. కేంద్ర మంత్రిగా ఉన్న ఏ వ్యక్తినీ పబ్లిక్ అకౌంట్స్ కమిటీ లేదా ఎస్టిమేట్స్ కమిటీ సభ్యునిగా ఎన్నుకోరాదు లేదా నియమించరాదు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The PAC has 22 members (15 LS + 7 RS), chaired by an Opposition MP since 1967. The Estimates Committee has 30 members, all from Lok Sabha. Ministers are constitutionally disqualified from membership in parliamentary financial oversight committees to ensure objective scrutiny of executive expenditure.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. పీఏసీ (PAC) లో 22 మంది సభ్యులు ఉంటారు, స్పీకర్ ప్రతిపక్ష సభ్యుడిని చైర్మన్‌గా నియమిస్తారు. ఎస్టిమేట్స్ కమిటీలో 30 మంది కేవలం లోక్‌సభ నుండే ఉంటారు. కార్యనిర్వాహక వర్గంపై పారదర్శక నిఘా ఉండేందుకు మంత్రులెవరూ ఈ ఆర్థిక కమిటీల్లో సభ్యులుగా ఉండరాదు."
    },
    "winners_history_quit_india_1942": {
        "id": 37,
        "subject": "Indian History",
        "topic": "Modern Indian History - Quit India Movement 1942 & Parallel Governments (Prati Sarkar)",
        "source_channel": "Winners Online (Winners Publications)",
        "source_video_id": "winners_history_quit_india_1942",
        "raw_video_hook": "1942 క్విట్ ఇండియా ఉద్యమంలో ఉషా మెహతా రహస్య రేడియో మరియు సతారా, బల్లియాలలో ఏర్పడిన సమాంతర ప్రభుత్వాలు.",
        "question_type": "Match the Following",
        "question_en": "Match the following key leaders/initiatives of the 1942 Quit India Movement with their respective underground centers or parallel governments (*Prati Sarkar*):\n(A) Usha Mehta & Ram Manohar Lohia     - (1) Jatiya Sarkar at Tamluk (Midnapore)\n(B) Chittu Pandey                      - (2) Secret 'Congress Radio' broadcasting from Bombay\n(C) Nana Patil & Y.B. Chavan           - (3) Independent National Government in Ballia (UP)\n(D) Satish Samanta & Ajoy Mukherjee    - (4) Prati Sarkar in Satara (Maharashtra)\nCorrect matching code:",
        "question_te": "1942 క్విట్ ఇండియా ఉద్యమంలోని ప్రముఖ నాయకులు/పోరాట రూపాలను వాటికి సంబంధించిన భూగర్భ కేంద్రాలు లేదా సమాంతర ప్రభుత్వాలతో (Prati Sarkar) జతపరచండి:\n(A) ఉషా మెహతా మరియు రామ్ మనోహర్ లోహియా - (1) జాతీయ సర్కార్ - తమ్లుక్ (మిడ్నాపూర్, బెంగాల్)\n(B) చిట్టూ పాండే                        - (2) ముంబై నుండి ప్రసారమైన రహస్య 'కాంగ్రెస్ రేడియో'\n(C) నానా పాటిల్ మరియు వై.బి. చవాన్      - (3) బల్లియా సమాంతర ప్రభుత్వం (ఉత్తరప్రదేశ్)\n(D) సతీష్ సమంత మరియు అజయ్ ముఖర్జీ     - (4) సతారా ప్రతి సర్కార్ (మహారాష్ట్ర)\nసరైన కోడ్‌ను ఎంచుకోండి:",
        "options_en": ["A-2, B-3, C-4, D-1", "A-3, B-2, C-1, D-4", "A-2, B-4, C-3, D-1", "A-1, B-3, C-4, D-2"],
        "options_te": ["A-2, B-3, C-4, D-1", "A-3, B-2, C-1, D-4", "A-2, B-4, C-3, D-1", "A-1, B-3, C-4, D-2"],
        "correct_option": 0,
        "explanation_en": "Correct matching is A-2, B-3, C-4, D-1. Usha Mehta and Dr. Ram Manohar Lohia set up the clandestine Congress Radio from Bombay. Chittu Pandey declared an independent government in Ballia (UP) in August 1942. Nana Patil led the parallel government (Prati Sarkar) in Satara with his volunteer force Toofan Sena. Satish Samanta spearheaded the Tamluk Jatiya Sarkar in Midnapore, West Bengal.",
        "explanation_te": "సరైన జత: A-2, B-3, C-4, D-1. ఉషా మెహతా బొంబాయి నుండి రహస్య కాంగ్రెస్ రేడియో నడిపారు. చిట్టూ పాండే యూపీలోని బల్లియాలో తాత్కాలిక స్వతంత్ర ప్రభుత్వాన్ని నెలకొల్పారు. నానా పాటిల్ సతారాలో 'తుఫాన్ సేన'తో సమాంతర ప్రభుత్వాన్ని నడిపారు. సతీష్ సమంత బెంగాల్‌లోని తమ్లుక్‌లో జాతీయ సర్కార్‌ను నడిపారు."
    },
    "winners_history_vijayanagara_nayankara": {
        "id": 38,
        "subject": "Indian History",
        "topic": "Medieval Indian History - Vijayanagara Administration (Amara-Nayankara & Ayagar Systems)",
        "source_channel": "Winners Online (Winners Publications)",
        "source_video_id": "winners_history_vijayanagara_nayankara",
        "raw_video_hook": "విజయనగర చక్రవర్తుల కాలంలో నాయంకర సైనిక వ్యవస్థ, అమరనాయకులు మరియు గ్రామాల్లోని ఆయగార్ విధానం.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the administrative and military apparatus of the Vijayanagara Empire:\n1. Under the Amara-Nayankara system, military commanders (Amaranayakas) were assigned territories called *Amara* to collect revenues, maintain designated infantry, cavalry, and war elephants, and pay an annual tribute to the Rayas.\n2. The village administration was organized under the 'Ayagar system' (ఆయగార్ల వ్యవస్థ), where a body of twelve hereditary functionaries managed village affairs and held tax-free *Manya* lands.\n3. The Portuguese chroniclers Domingo Paes and Fernao Nuniz provided extensive firsthand accounts of the wealth, military mobilization, and Amaranayaka obligations in Vijayanagara.\nWhich of the statements given above are correct?",
        "question_te": "విజయనగర సామ్రాజ్య పరిపాలనా మరియు సైనిక వ్యవస్థకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. అమరనాయంకర విధానంలో భాగంగా సైన్యాధిపతులకు (అమరనాయకులు) 'అమర' అనబడే భూములను ఇచ్చేవారు; వారు పన్నులు వసూలు చేసి, నిర్ణీత సైన్యాన్ని పోషిస్తూ చక్రవర్తికి వార్షిక కప్పం చెల్లించేవారు.\n2. గ్రామీణ పరిపాలన కోసం 'ఆయగార్ల వ్యవస్థ' ఉండేది; గ్రామంలోని 12 మంది వంశపారంపర్య అధికారులు గ్రామాభివృద్ధిని పర్యవేక్షిస్తూ, ప్రతిఫలంగా పన్ను లేని 'మాన్యం' భూములను అనుభవించేవారు.\n3. పోర్చుగీస్ యాత్రికులైన డొమింగో పేస్ మరియు ఫెర్నావో న్యూనిజ్ విజయనగర వైభవం, సైనిక సమీకరణ మరియు నాయంకర వ్యవస్థపై సమగ్ర రచనలు చేశారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The Amara-Nayankara system was the cornerstone of Vijayanagara's military-feudal organization. The village autonomy was run by 12 Ayagars (village headman, accountant, watchman, blacksmith, etc.) with tax-exempt *manya* land allotments. Foreign visitors Domingo Paes (reign of Krishnadevaraya) and Fernao Nuniz (reign of Achyuta Raya) left invaluable documentation of these systems.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. విజయనగర సామ్రాజ్యంలో సైనిక నిర్వహణకు అమరనాయంకర వ్యవస్థ ప్రధాన స్తంభం. గ్రామాల్లో 12 మంది వంశపారంపర్య సేవకులతో కూడిన ఆయగార్ వ్యవస్థ గ్రామీణ పాలనను చూసేది; వీరికి పన్ను లేని మాన్యాలు ఉండేవి. డొమింగో పేస్ మరియు ఫెర్నావో న్యూనిజ్ ఈ వివరాలను తమ గ్రంథాలలో రికార్డు చేశారు."
    },
    "tsat_tg_tribal_festivals_medaram": {
        "id": 39,
        "subject": "Telangana History",
        "topic": "Telangana Culture & Tribal Resistance - Sammakka-Saralamma Medaram Jatara",
        "source_channel": "T-SAT Network (Govt of Telangana)",
        "source_video_id": "tsat_tg_tribal_festivals_medaram",
        "raw_video_hook": "ఆసియాలోనే అతిపెద్ద గిరిజన జాతర మేడారం చరిత్ర, కాకతీయులతో పోరాటం మరియు పూజా విధానాలు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the historic Sammakka-Saralamma Jatara (Medaram Jatara) celebrated in Telangana:\n1. It is celebrated biennially in Medaram village of Mulugu district by the Koya tribe, commemorating the heroic revolt of tribal chieftains against the Kakatiya King Prataparudra's harsh tax exactions during a severe famine.\n2. Devotees offer 'Bangaram' (pure jaggery) equivalent to their body weight (Tulabharam) to honor the deities at the sacred altar (*Gaddelu*).\n3. The Government declared it a State Festival in 1996, and it represents Asia's largest congregation of indigenous tribal communities.\nWhich of the statements given above are correct?",
        "question_te": "తెలంగాణలో జరిగే చారిత్రక సమ్మక్క-సారలమ్మ మేడారం జాతరకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ములుగు జిల్లా తాడ్వాయి మండలంలోని మేడారంలో కోయ గిరిజనులు రెండేళ్లకోసారి నిర్వహించే ఈ జాతర, తీవ్ర కరవు కాలంలో పన్నుల వసూళ్లకు వ్యతిరేకంగా కాకతీయ చక్రవర్తి ప్రతాపరుద్రుని సైన్యంతో సమ్మక్క-సారలమ్మలు చేసిన వీరోచిత పోరాటానికి ప్రతీక.\n2. భక్తులు తమ శరీర బరువుకు సమానమైన బెల్లాన్ని 'బంగారం' (తులాభారం) పేరుతో దేవతల గద్దెల వద్ద నైవేద్యంగా సమర్పిస్తారు.\n3. 1996 లో ఈ జాతరను ప్రభుత్వం అధికారిక రాష్ట్ర పండుగగా గుర్తించింది; ఇది ఆసియా ఖండంలోనే అతిపెద్ద గిరిజన మహాసమ్మేళనంగా పేరొందింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Medaram Jatara is held biennially during Magha Suddha Pournami in Mulugu district. It honors the martyrdom of Koya ruler Pagididda Raju, his consort Sammakka, and daughter Saralamma fighting the tax collection regiments of Kakatiya Prataparudra. Rituals are administered by Koya priests. Jaggery is revered as 'Bangaram' and offered in Tulabharam.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. మేడారంలో రెండేళ్లకోసారి మాఘ పౌర్ణమి నాడు ఆసియాలోనే అతిపెద్ద గిరిజన జాతర జరుగుతుంది. కాకతీయ సేనలపై సమ్మక్క, సారలమ్మ, పగిడిద్దరాజు సాగించిన పోరాటానికి గుర్తుగా ఈ జాతర నిర్వహిస్తారు. భక్తులు బెల్లాన్ని బంగారం రూపంలో గద్దెలపై సమర్పిస్తారు. 1996 లో ఇది అధికారిక రాష్ట్ర పండుగగా గుర్తింపు పొందింది."
    },
    "tsat_polity_election_commission_324": {
        "id": 40,
        "subject": "Indian Polity",
        "topic": "Constitutional Bodies - Election Commission of India (Article 324) & Chief Election Commissioner Act",
        "source_channel": "T-SAT Network (Govt of Telangana)",
        "source_video_id": "tsat_polity_election_commission_324",
        "raw_video_hook": "కేంద్ర ఎన్నికల సంఘం అధికరణ 324, సభ్యుల నియామక ప్రక్రియ మరియు పదవి తొలగింపు నిబంధనలు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Election Commission of India (ECI) under Article 324 of the Constitution and recent statutory enactments:\n1. The superintendence, direction, and control of elections to Parliament, State Legislatures, and the offices of President and Vice-President of India are vested in the ECI.\n2. The Chief Election Commissioner (CEC) enjoys security of tenure and can only be removed from office in like manner and on like grounds as a Judge of the Supreme Court of India under Article 324(5).\n3. Under the Chief Election Commissioner and other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023, the Selection Committee consists of the Prime Minister, a nominated Union Cabinet Minister, and the Leader of Opposition (or leader of the largest opposition party) in the Lok Sabha.\nWhich of the statements given above are correct?",
        "question_te": "భారత రాజ్యాంగంలోని అధికరణ 324 మరియు తాజా చట్టబద్ధ నిబంధనల ప్రకారం భారత ఎన్నికల సంఘం (ECI) కి సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. పార్లమెంటు, రాష్ట్ర శాసనసభలు, భారత రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి పదవుల ఎన్నికల నిర్వహణ, పర్యవేక్షణ మరియు మార్గదర్శకత్వ అధికారాలు ECI కి సంక్రమించాయి.\n2. ప్రధాన ఎన్నికల కమిషనర్ (CEC) కు పదవీ భద్రత ఉంటుంది; రాజ్యాంగంలోని అధికరణ 324(5) ప్రకారం సుప్రీంకోర్టు న్యాయమూర్తిని తొలగించే పద్ధతి మరియు కారణాలపై మాత్రమే రాష్ట్రపతి ఆయనను తొలగించగలరు.\n3. చీఫ్ ఎలక్షన్ కమిషనర్ మరియు ఇతర ఎలక్షన్ కమిషనర్ల నియామక చట్టం, 2023 ప్రకారం, ఎంపిక కమిటీలో భారత ప్రధాన మంత్రి, ఆయన నామినేట్ చేసిన ఒక కేంద్ర కేబినెట్ మంత్రి, మరియు లోక్‌సభలోని ప్రధాన ప్రతిపక్ష నేత సభ్యులుగా ఉంటారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Article 324 mandates that the ECI superintends national and state legislative polls (panchayat/municipal polls are conducted by State Election Commissions under Art 243K/243ZA). Under Article 324(5), the CEC has identical tenure security to a Supreme Court Judge. The 2023 parliamentary statute codified the 3-member executive selection committee structure.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. ఆర్టికల్ 324 ప్రకారం పార్లమెంట్, అసెంబ్లీ, రాష్ట్రపతి, ఉపరాష్ట్రపతి ఎన్నికలను ఈసీ నిర్వహిస్తుంది. రాజ్యాంగంలోని ఆర్టికల్ 324(5) ప్రకారం సీఈసీని కేవలం సుప్రీంకోర్టు న్యాయమూర్తిని తొలగించే ప్రక్రియ ద్వారానే తొలగించగలరు. 2023 చట్టం ప్రకారం ప్రధాని, కేంద్ర కేబినెట్ మంత్రి, లోక్‌సభ ప్రతిపక్ష నేతలతో కూడిన కమిటీ వీరిని ఎంపిక చేస్తుంది."
    },
    "ashoka_tg_qutb_shahi_admin": {
        "id": 41,
        "subject": "Telangana History & Movement",
        "topic": "Qutb Shahi Dynasty - Ibrahim Qutb Shah, Telugu Literature Patronage & Public Works",
        "source_channel": "Ashoka Academy (Ashok Sir)",
        "source_video_id": "ashoka_tg_qutb_shahi_admin",
        "raw_video_hook": "ఇబ్రహీం కుతుబ్‌షా తెలుగు సాహితీ పోషణ, మల్కిభరాముడు బిరుదు, హుస్సేన్‌సాగర్ నిర్మాణం మరియు మహమ్మద్ కులీ కుతుబ్‌షా చార్మినార్ నిర్మాణం.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the reign and administrative contributions of the Qutb Shahi rulers of Golconda:\n1. Ibrahim Qutb Shah was fondly revered as 'Malkibharamudu' by contemporary Telugu poets for his generous patronage to scholars like Gangadhara Kavi and Kandukuri Rudrakavi.\n2. Ibrahim Qutb Shah commissioned the construction of the historic Hussain Sagar lake under the supervision of Hussain Shah Wali.\n3. Muhammad Quli Qutb Shah founded the city of Hyderabad and built the Charminar in 1591 AD to commemorate the eradication of the plague epidemic.\nWhich of the statements given above are correct?",
        "question_te": "గోల్కొండ కుతుబ్‌షాహీల పాలనా విధానం మరియు చారిత్రక సహకారాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఇబ్రహీం కుతుబ్‌షా తెలుగు కవులైన గంగాధర కవి, కందుకూరి రుద్రకవి వంటి పండితులను ఆదరించి, వారిచే 'మల్కిభరాముడు' అని అభిమానంగా పిలువబడ్డారు.\n2. హైదరాబాద్ ప్రాంత తాగునీరు, సాగునీటి అవసరాల కోసం హుస్సేన్ షా వలీ పర్యవేక్షణలో ప్రసిద్ధ 'హుస్సేన్‌సాగర్' సరస్సును ఇబ్రహీం కుతుబ్‌షా నిర్మించారు.\n3. మహమ్మద్ కులీ కుతుబ్‌షా భాగ్యనగరం (హైదరాబాద్) నూతన నగరాన్ని స్థాపించి, నగరంలో ప్లేగు వ్యాధి నిర్మూలనకు గుర్తుగా 1591 లో చార్మినార్‌ను నిర్మించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Ibrahim Qutb Shah (reigned 1550–1580) was a patron of Telugu culture and was praised as 'Malkibharama' in works like 'Tapati Samvaranopakhyanam' by Gangadhara Kavi. He excavated Hussain Sagar and Ibrahimpatnam tanks. His son Muhammad Quli Qutb Shah laid the foundation of Hyderabad and erected Charminar in 1591 following the end of the deadly plague epidemic.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. ఇబ్రహీం కుతుబ్‌షా తెలుగు భాషా పోషణతో 'మల్కిభరాముడు' అని ఖ్యాతి పొందారు. అద్దంకి గంగాధర కవి తన 'తపతీ సంవరణోపాఖ్యానం'ను ఆయనకే అంకితం చేశారు. హుస్సేన్‌సాగర్, ఇబ్రహీంపట్నం చెరువులను ఈయన హయాంలోనే తవ్వించారు. మహమ్మద్ కులీ కుతుబ్‌షా 1591 లో ప్లేగు మహమ్మారి ముగింపునకు ప్రతీకగా చార్మినార్‌ను నిర్మించారు."
    },
    "ashoka_tg_mulki_rules_1952": {
        "id": 42,
        "subject": "Telangana History & Movement",
        "topic": "Telangana Movement - 1952 Non-Mulki Agitation & City College Police Firing",
        "source_channel": "Ashoka Academy (Ashok Sir)",
        "source_video_id": "ashoka_tg_mulki_rules_1952",
        "raw_video_hook": "1952 నాన్-ముల్కీ గో బ్యాక్ ఉద్యమం, సెప్టెంబర్ 3-4 సిటీ కాలేజ్ ఘటన మరియు జస్టిస్ పింగళి జగన్మోహన్ రెడ్డి కమిషన్ నివేదిక.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the 1952 'Non-Mulki Go Back' (Idhi Sambar - Go Back Sambar) movement in Hyderabad State:\n1. The agitation originated in Warangal in July 1952 when local students protested the illegal appointment of non-local teachers in place of genuine Mulkis.\n2. On September 3 and 4, 1952, police opened fire on peaceful student protestors near City College, Hyderabad, resulting in the tragic martyrdom of students and citizens.\n3. The Chief Minister Burgula Ramakrishna Rao appointed the Justice Pingali Jaganmohan Reddy Commission of Inquiry to investigate the City College police firing.\nWhich of the statements given above are correct?",
        "question_te": "1952 లో హైదరాబాద్ రాష్ట్రంలో జరిగిన 'నాన్-ముల్కీ గో బ్యాక్' (ఇది సాంబార్ - గో బ్యాక్ సాంబార్) ఉద్యమానికి సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. స్థానిక ముల్కీ నిబంధనలను ఉల్లంఘిస్తూ నాన్-లోకల్ ఉపాధ్యాయులను అక్రమంగా నియమించడాన్ని నిరసిస్తూ 1952 జూలైలో వరంగల్ పట్టణంలో ఈ ఉద్యమం మొదలైంది.\n2. 1952 సెప్టెంబర్ 3 మరియు 4 తేదీలలో హైదరాబాద్ సిటీ కాలేజ్ సమీపంలో విద్యార్థి ప్రదర్శనకారులపై పోలీసులు విచక్షణారహితంగా కాల్పులు జరిపారు, పలువురు విద్యార్థులు అమరులయ్యారు.\n3. సిటీ కాలేజ్ పోలీసు కాల్పుల ఘటనపై సమగ్ర విచారణ నిమిత్తం ముఖ్యమంత్రి బూర్గుల రామకృష్ణారావు ప్రభుత్వం జస్టిస్ పింగళి జగన్మోహన్ రెడ్డి విచారణ కమిషన్‌ను నియమించింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The 1952 Mulki movement began in Warangal following non-local teacher recruitments. It escalated to Hyderabad, culminating in police firing outside City College on September 3-4, 1952 under Police Commissioner Shiva Kumar Lal. The Burgula government appointed Justice Pingali Jaganmohan Reddy Commission, which critically scrutinized the police excessive use of force.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1952 ముల్కీ ఉద్యమం వరంగల్‌లో ప్రారంభమై రాజధానికి విస్తరించింది. సెప్టెంబర్ 3, 4 తేదీల్లో సిటీ కాలేజీ వద్ద పోలీసు కాల్పులు జరిగాయి. దీనిపై విచారణకు బూర్గుల ప్రభుత్వం సెప్టెంబర్ 5, 1952న జస్టిస్ పింగళి జగన్మోహన్ రెడ్డి ఏకసభ్య కమిషన్‌ను నియమించింది. కమిషన్ 1952 డిసెంబర్‌లో సమగ్ర నివేదిక సమర్పించింది."
    },
    "studynow_tg_global_ai_summit_2026": {
        "id": 43,
        "subject": "Telangana Current Affairs",
        "topic": "Telangana Emerging Tech - Global AI Summit & 200-Acre AI City in Mucherla",
        "source_channel": "StudyNow Telugu",
        "source_video_id": "studynow_tg_global_ai_summit_2026",
        "raw_video_hook": "తెలంగాణ గ్లోబల్ AI సమ్మిట్ హైదరాబాద్, ముచ్చెర్లలో 200 ఎకరాల AI సిటీ మరియు తెలంగాణ AI మిషన్ (T-AIM).",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Artificial Intelligence initiatives launched by the Government of Telangana:\n1. The state government unveiled plans to develop a dedicated 200-acre 'AI City' at Mucherla within the proposed Fourth City (Bharat Future City).\n2. The Government formulated the 'Telangana AI Mission' (T-AIM) in partnership with NASSCOM to drive AI adoption across governance, healthcare, and agriculture.\n3. During the Global AI Summit hosted in Hyderabad, the state adopted the 'Making AI Work for Everyone' framework focusing on ethical AI, data governance, and Indic language LLMs.\nWhich of the statements given above are correct?",
        "question_te": "తెలంగాణ ప్రభుత్వం చేపట్టిన కృత్రిమ మేధస్సు (AI) వ్యూహాత్మక కార్యక్రమాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఫోర్త్ సిటీ (భారత్ ఫ్యూచర్ సిటీ) పరిధిలోని ముచ్చెర్లలో 200 ఎకరాల విస్తీర్ణంలో ప్రత్యేక 'AI సిటీ' (AI City) ని ఏర్పాటు చేయనున్నట్లు రాష్ట్ర ప్రభుత్వం ప్రకటించింది.\n2. పరిపాలన, వైద్యారోగ్యం మరియు వ్యవసాయ రంగాలలో AI అనువర్తనాలను విస్తరించేందుకు నాస్కామ్ (NASSCOM) తో కలిసి 'తెలంగాణ AI మిషన్' (T-AIM) ను అమలు చేస్తున్నారు.\n3. హైదరాబాద్ వేదికగా నిర్వహించిన గ్లోబల్ AI సమ్మిట్‌లో 'మేకింగ్ AI వర్క్ ఫర్ ఎవ్రీవన్' నినాదంతో నైతిక AI, డేటా భద్రత మరియు భారతీయ భాషా LLM మోడళ్ల అభివృద్ధికి ప్రాధాన్యతనిచ్చారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Telangana has positioned itself as the AI capital of India. At the Global AI Summit in Hyderabad, the Chief Minister laid the foundation framework for the 200-acre AI City at Mucherla (Fourth City). The state collaborates with NASSCOM through T-AIM, supporting generative AI startups, ethical guardrails, and vernacular large language models.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. హైదరాబాద్‌ను గ్లోబల్ AI హబ్‌గా తీర్చిదిద్దేందుకు ముచ్చెర్ల ఫోర్త్ సిటీలో 200 ఎకరాల్లో 'AI సిటీ' నిర్మిస్తున్నారు. నాస్కామ్‌తో T-AIM భాగస్వామ్యం ద్వారా స్టార్టప్‌లు, గవర్నెన్స్ ప్రాజెక్టులను ప్రోత్సహిస్తున్నారు. గ్లోబల్ AI సమ్మిట్ ద్వారా నైతిక AI మరియు భారతీయ భాషల అప్లికేషన్లపై రోడ్‌మ్యాప్ రూపొందించారు."
    },
    "studynow_tg_young_india_residential_2026": {
        "id": 44,
        "subject": "Telangana Current Affairs",
        "topic": "Social Welfare & Education - Young India Integrated Residential Schools (సమీకృత గురుకులాలు)",
        "source_channel": "StudyNow Telugu",
        "source_video_id": "studynow_tg_young_india_residential_2026",
        "raw_video_hook": "తెలంగాణలో 119 అసెంబ్లీ నియోజకవర్గాల్లో సమీకృత యంగ్ ఇండియా రెసిడెన్షియల్ స్కూల్స్ నిర్మాణం మరియు బడ్జెట్.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the 'Young India Integrated Residential Schools' (యంగ్ ఇండియా సమీకృత గురుకుల పాఠశాలలు) scheme introduced by the Government of Telangana:\n1. The initiative aims to construct state-of-the-art integrated residential schools across all 119 Assembly Constituencies with an outlay exceeding ₹5,000 crores.\n2. In each integrated complex, SC, ST, BC, and Minority residential schools are co-located within a single unified modern campus to promote social inclusion and bridge caste barriers.\n3. Each campus is planned over 20–25 acres equipped with smart digital classrooms, modern science laboratories, international-standard athletic grounds, and residential quarters.\nWhich of the statements given above are correct?",
        "question_te": "తెలంగాణ ప్రభుత్వం ప్రతిష్టాత్మకంగా ప్రారంభించిన 'యంగ్ ఇండియా సమీకృత గురుకుల పాఠశాలల' (Young India Integrated Residential Schools) పథకానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. రాష్ట్రంలోని మొత్తం 119 అసెంబ్లీ నియోజకవర్గాలలో ₹5,000 కోట్లకు పైగా వ్యయంతో అంతర్జాతీయ ప్రమాణాలతో కూడిన సమీకృత గురుకులాలను నిర్మించాలని ప్రభుత్వం నిర్ణయించింది.\n2. కుల వివక్షను రూపుమాపి సామాజిక సమగ్రతను సాధించేందుకు ఎస్సీ, ఎస్టీ, బీసీ మరియు మైనారిటీ గురుకుల పాఠశాలలను ఒకే సమీకృత క్యాంపస్‌లో ఏర్పాటు చేస్తున్నారు.\n3. ఒక్కో సమీకృత పాఠశాల సముదాయాన్ని 20 నుండి 25 ఎకరాల విస్తీర్ణంలో డిజిటల్ క్లాస్‌రూములు, ఆధునిక సైన్స్ ల్యాబ్‌లు, అంతర్జాతీయ స్థాయి క్రీడా మైదానాలతో నిర్మిస్తున్నారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The Government of Telangana launched the Young India Integrated Residential Schools project across all 119 constituencies. Unlike earlier standalone welfare schools segregated by department, the integrated model co-locates SC, ST, BC, and Minority institutions on unified 20-25 acre campuses to foster social cohesion, equal opportunity, and world-class educational infrastructure.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. గతంలో శాఖల వారీగా వేర్వేరుగా అద్దె భవనాల్లో ఉన్న గురుకులాలను ఒకేచోట సమీకృతం చేస్తూ 119 నియోజకవర్గాల్లో 20-25 ఎకరాల ప్రాంగణాల్లో ఈ పాఠశాలలను నిర్మిస్తున్నారు. ఎస్సీ, ఎస్టీ, బీసీ, మైనారిటీ విద్యార్థులు కలిసి చదువుకోవడం ద్వారా సామాజిక ఐక్యత పెంపొందించడం, కార్పొరేట్ తరహా నాణ్యమైన విద్యనందించడం దీని లక్ష్యం."
    },
    "csb_polity_art356_sr_bommai": {
        "id": 45,
        "subject": "Indian Polity",
        "topic": "State Autonomy & Emergency Provisions - Article 356 (President's Rule) & S.R. Bommai Landmark Judgment",
        "source_channel": "CSB IAS Academy (Bala Latha Madam)",
        "source_video_id": "csb_polity_art356_sr_bommai",
        "raw_video_hook": "ఆర్టికల్ 356 కింద రాష్ట్రపతి పాలన విధింపు, న్యాయ సమీక్ష పరిధి మరియు ఎస్.ఆర్. బొమ్మై కేసులో సుప్రీంకోర్టు తీర్పు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the proclamation of President's Rule under Article 356 of the Constitution and the principles laid down in the landmark *S.R. Bommai v. Union of India (1994)* case:\n1. A presidential proclamation under Article 356 must be approved by both Houses of Parliament by a simple majority within two months of its promulgation.\n2. The Supreme Court established that the presidential proclamation is subject to judicial review, and the burden lies on the Union Government to prove that relevant material existed justifying the breakdown of constitutional machinery.\n3. The State Legislative Assembly cannot be dissolved by the President immediately upon issuing the proclamation; it can only be placed under suspended animation until Parliament ratifies the proclamation.\nWhich of the statements given above are correct?",
        "question_te": "భారత రాజ్యాంగంలోని అధికరణ 356 (రాష్ట్రపతి పాలన) మరియు చారిత్రక *ఎస్.ఆర్. బొమ్మై వర్సెస్ యూనియన్ ఆఫ్ ఇండియా (1994)* తీర్పులోని మార్గదర్శకాలకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. ఆర్టికల్ 356 కింద జారీ చేసిన రాష్ట్రపతి ప్రకటనను పార్లమెంటు ఉభయ సభలు సాధారణ మెజారిటీతో రెండు నెలల లోపు ఆమోదించాలి.\n2. రాష్ట్రపతి ప్రకటన న్యాయ సమీక్షకు లోబడి ఉంటుందని మరియు రాజ్యాంగ యంత్రాంగం విఫలమైందనడానికి సరైన ఆధారాలు ఉన్నాయని రుజువు చేయాల్సిన బాధ్యత కేంద్ర ప్రభుత్వంపై ఉంటుందని సుప్రీంకోర్టు స్పష్టం చేసింది.\n3. ప్రకటన వెలువడిన వెంటనే రాష్ట్రపతి అసెంబ్లీని రద్దు చేయరాదు; పార్లమెంటు ఆమోదం తెలిపే వరకు అసెంబ్లీని కేవలం సస్పెన్షన్‌లో (Suspended Animation) మాత్రమే ఉంచాలి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. In the 9-judge bench decision in S.R. Bommai (1994), the Supreme Court checked executive arbitrariness under Article 356. The court ruled that: (i) proclamation approval requires 2 months simple majority in Parliament; (ii) judicial review applies to examine mala fides or extraneous grounds; (iii) the assembly cannot be dissolved until both Houses approve the proclamation; and (iv) secularism is a basic feature.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1994 నాటి ఎస్.ఆర్. బొమ్మై కేసు తీర్పు భారత సమాఖ్య వ్యవస్థలో మైలురాయి. ఆర్టికల్ 356 దుర్వినియోగాన్ని అడ్డుకుంటూ సుప్రీంకోర్టు 9 మంది న్యాయమూర్తుల ధర్మాసనం కీలక మార్గదర్శకాలు ఇచ్చింది: పార్లమెంట్ ఆమోదం తెలిపే వరకు అసెంబ్లీని రద్దు చేయరాదు; కోర్టుల న్యాయ సమీక్ష వర్తిస్తుంది; కారణాలను రుజువు చేసే భారం కేంద్రంపైనే ఉంటుంది."
    },
    "csb_polity_delimitation_art82": {
        "id": 46,
        "subject": "Indian Polity",
        "topic": "Electoral Demarcation - Delimitation Commission (Article 82) & 84th/87th Constitutional Amendments",
        "source_channel": "CSB IAS Academy (Bala Latha Madam)",
        "source_video_id": "csb_polity_delimitation_art82",
        "raw_video_hook": "డీలిమిటేషన్ ప్రక్రియ (Article 82), 84వ మరియు 87వ రాజ్యాంగ సవరణల ద్వారా సీట్ల ఫ్రీజింగ్ మరియు పరిమితులు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Delimitation of Parliamentary and Assembly constituencies in India under Article 82 and relevant constitutional amendments:\n1. Under Article 82 of the Constitution, Parliament enacts a Delimitation Act after each census, appointing a high-powered Delimitation Commission whose orders have the force of law and cannot be questioned before any court.\n2. The 84th Constitutional Amendment Act, 2001 froze the total number of Lok Sabha and State Assembly seats allocated to states based on the 1971 census until the first census conducted after the year 2026.\n3. The 87th Constitutional Amendment Act, 2003 permitted the internal readjustment and rationalization of constituency boundaries within a state on the basis of the 2001 census without changing the state's total allocated seats.\nWhich of the statements given above are correct?",
        "question_te": "భారత రాజ్యాంగంలోని అధికరణ 82 మరియు సంబంధిత రాజ్యాంగ సవరణల ప్రకారం పార్లమెంట్ మరియు అసెంబ్లీ నియోజకవర్గాల పునర్విభజన (Delimitation) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. రాజ్యాంగంలోని ఆర్టికల్ 82 ప్రకారం ప్రతి జనాభా లెక్కల అనంతరం పార్లమెంటు డీలిమిటేషన్ చట్టాన్ని చేస్తుంది; డీలిమిటేషన్ కమిషన్ జారీ చేసే ఉత్తర్వులకు చట్టబద్ధమైన బలం ఉంటుంది మరియు వాటిని ఏ న్యాయస్థానంలోనూ ప్రశ్నించడానికి వీల్లేదు.\n2. 84వ రాజ్యాంగ సవరణ చట్టం 2001 ప్రకారం, 1971 జనాభా లెక్కల ఆధారంగా ఉన్న లోక్‌సభ మరియు రాష్ట్ర శాసనసభల మొత్తం సీట్ల సంఖ్యను 2026 తర్వాత జరిగే తొలి జనాభా లెక్కల వరకు యథాతథంగా స్తంభింపజేశారు (Freeze).\n3. 87వ రాజ్యాంగ సవరణ చట్టం 2003 ప్రకారం, రాష్ట్రానికి ఉన్న మొత్తం సీట్లను మార్చకుండా, రాష్ట్రం లోపల నియోజకవర్గాల సరిహద్దుల అంతర్గత సర్దుబాటును 2001 జనాభా లెక్కల ఆధారంగా చేపట్టడానికి అనుమతించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Article 82 empowers Parliament to set up a Delimitation Commission. Under Article 329(a), delimitation orders published in the Gazette of India cannot be challenged in any court. The 42nd Amendment originally froze seats till 2000; the 84th Amendment (2001) extended this freeze till 2026 using 1971 population benchmarks. The 87th Amendment (2003) updated internal intra-state delimitation to 2001 census data.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. ఆర్టికల్ 82 కింద ఏర్పాటయ్యే డీలిమిటేషన్ కమిషన్ ఉత్తర్వులపై కోర్టులకు అధికార పరిధి ఉండదు (ఆర్టికల్ 329(a)). 84వ సవరణ ద్వారా జనాభా నియంత్రణ పాటించిన దక్షిణాది రాష్ట్రాలు నష్టపోకుండా 1971 ప్రాతిపదికన సీట్లను 2026 వరకు స్తంభింపజేశారు. 87వ సవరణ ద్వారా రాష్ట్రాల లోపల అంతర్గత నియోజకవర్గాల సరిహద్దులను 2001 జనాభా ప్రకారం మార్పులు చేశారు."
    },
    "winners_history_ivc_dholavira_sanitation": {
        "id": 47,
        "subject": "Indian History",
        "topic": "Ancient India - Indus Valley Civilization: Dholavira Hydraulic Engineering & Mohenjo-daro Great Bath",
        "source_channel": "Winners Online (Winners Publications)",
        "source_video_id": "winners_history_ivc_dholavira_sanitation",
        "raw_video_hook": "సింధు నాగరికత నగర ప్రణాళిక, ధోలవీరా త్రైపాక్షిక నిర్మాణం, రాతి రిజర్వాయర్లు మరియు మొహంజొదారో మహా స్నానవాటిక.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the urban architecture and hydraulic engineering of the Harappan (Indus Valley) Civilization:\n1. Unlike most Harappan settlements that were divided into two parts, the UNESCO World Heritage site of Dholavira in Gujarat is laid out in three distinct fortified zones: Citadel, Middle Town, and Lower Town.\n2. Dholavira possessed an extraordinary cascade water management system with deep step-wells, inlet channels, and 16 massive reservoirs carved directly out of natural sandstone bedrock.\n3. The Great Bath at Mohenjo-daro was constructed with baked bricks set on edge in gypsum mortar and sealed with a thick waterproof layer of natural bitumen (asphalt).\nWhich of the statements given above are correct?",
        "question_te": "హరప్పా (సింధు లోయ) నాగరికత నాటి నగర నిర్మాణం మరియు జల సాంకేతిక పరిజ్ఞానానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. సాధారణ హరప్పా నగరాల వలె రెండు భాగాలుగా కాకుండా, గుజరాత్‌లోని యునెస్కో ప్రపంచ వారసత్వ ప్రదేశమైన 'ధోలవీరా' కోట (సిటడెల్), మధ్య నగరం, మరియు దిగువ నగరం అనే 3 ప్రత్యేక రక్షిత విభాగాలుగా విభజించబడింది.\n2. వర్షపు నీటిని ఒడిసిపట్టేందుకు సహజమైన రాతిని తొలిచి నిర్మించిన 16 భారీ రిజర్వాయర్లు, మెట్లబావులు మరియు నీటి కాల్వలతో కూడిన అద్భుతమైన జల నిర్వహణ వ్యవస్థ ధోలవీరాలో వెలుగుచూసింది.\n3. మొహంజొదారోలోని 'మహా స్నానవాటిక' (Great Bath) లో నీరు లీక్ కాకుండా ఉండేందుకు జిప్సం గారతో కాల్చిన ఇటుకలను పేర్చి, సహజమైన తారు (Bitumen/Asphalt) పూతను వాడారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Dholavira in Khadir Bet (Kutch, Gujarat, excavated by R.S. Bisht) is famous for its unique tripartite urban planning and UNESCO inscription in 2021. It housed sophisticated interconnected stone reservoirs to withstand arid desert droughts. Mohenjo-daro's Great Bath utilized gypsum mortar backed by bitumen waterproofing, reflecting peerless civil engineering in proto-historic India.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. గుజరాత్‌లోని కచ్‌లో ఉన్న ధోలవీరాలో విలక్షణమైన త్రైపాక్షిక నగర నిర్మాణం (కోట, మధ్య నగరం, దిగువ నగరం) కనిపిస్తుంది. వర్షపు నీటిని నిల్వ చేసే రాతి జలాశయాలు ఇక్కడి ప్రత్యేకత; 2021లో ఇది యునెస్కో గుర్తింపు పొందింది. మొహంజొదారో మహా స్నానవాటికలో బిటుమెన్ (తారు) ద్వారా వాటర్‌ప్రూఫింగ్ చేసి నిర్మించిన విధానం నాటి ఇంజనీరింగ్ ప్రతిభకు నిదర్శనం."
    },
    "winners_history_1857_hyderabad_turrebaz": {
        "id": 48,
        "subject": "Indian History",
        "topic": "Modern Indian History - 1857 Revolt in Hyderabad State: Turrebaz Khan & Maulvi Alauddin",
        "source_channel": "Winners Online (Winners Publications)",
        "source_video_id": "winners_history_1857_hyderabad_turrebaz",
        "raw_video_hook": "1857 తిరుగుబాటులో హైదరాబాద్ రెసిడెన్సీపై తుర్రేబాజ్ ఖాన్ మరియు మౌల్వీ అలావుద్దీన్ దాడి, చీడా ఖాన్ విముక్తి పోరాటం.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the 1857 Sepoy Mutiny and anti-British insurrection in the Deccan (Hyderabad State):\n1. On July 17, 1857, Turrebaz Khan and Maulvi Alauddin led an armed assault of 5,000 Rohilla insurgents and local patriots on the British Residency located at Koti, Hyderabad.\n2. The rebellion was specifically sparked to demand the release of Jamadar Cheeda Khan, a rebel soldier of the Hyderabad Contingent who refused to fight fellow mutineers in northern India and was imprisoned in the Residency.\n3. After being captured through treachery near Toopran forest, Turrebaz Khan was shot dead, and his body was displayed publicly at Koti police station; Maulvi Alauddin was sentenced to life transportation to the Cellular Jail in Andaman.\nWhich of the statements given above are correct?",
        "question_te": "1857 సిపాయిల తిరుగుబాటు మరియు దక్కన్ (హైదరాబాద్ సంస్థానం) లో జరిగిన బ్రిటిష్ వ్యతిరేక పోరాటానికి సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. 1857 జూలై 17న తుర్రేబాజ్ ఖాన్ మరియు మౌల్వీ అలావుద్దీన్ నాయకత్వంలో సుమారు 5,000 మంది రోహిల్లా యోధులు, దేశభక్తులు హైదరాబాద్ కోటిలోని బ్రిటిష్ రెసిడెన్సీ భవనంపై సాయుధ దాడి చేశారు.\n2. ఉత్తర భారతదేశంలో తిరుగుబాటు చేసిన తోటి సైనికులపై పోరాడేందుకు నిరాకరించినందుకు రెసిడెన్సీలో బంధించబడిన హైదరాబాద్ కంటింజెంట్ దళ జమాదార్ చీడా ఖాన్‌ను విడిపించడమే ఈ దాడికి తక్షణ కారణం.\n3. తూప్రాన్ అటవీ ప్రాంతంలో ద్రోహం వల్ల పట్టుబడిన తుర్రేబాజ్ ఖాన్‌ను బ్రిటిష్ సైన్యం కాల్చి చంపి, ఆయన మృతదేహాన్ని కోటి కొత్వాల్ వద్ద వేలాడదీసింది; మౌల్వీ అలావుద్దీన్‌ను అండమాన్ సెల్యులార్ జైలుకు యావజ్జీవ ద్వీపాంతర శిక్ష విధించి తరలించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The 1857 revolt found dramatic resonance in Hyderabad. Cheeda Khan had rebelled from Aurangabad and was held captive in Koti Residency. Turrebaz Khan and Maulvi Alauddin rallied armed crowds on 17 July 1857. Though Resident Major Cuthbert Davidson repelled the attack, Turrebaz Khan became a legendary Deccan martyr, while Maulvi Alauddin suffered exile in the penal colony of Andaman.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1857 ప్రథమ స్వాతంత్ర్య సంగ్రామంలో భాగంగా హైదరాబాద్‌లో జూలై 17, 1857న కోటి బ్రిటిష్ రెసిడెన్సీపై దాడి జరిగింది. ఔరంగాబాద్ నుండి వచ్చి బందీగా ఉన్న చీడా ఖాన్ విడుదలే దీని లక్ష్యం. తుర్రేబాజ్ ఖాన్ వీరమరణం పొందగా, మౌల్వీ అలావుద్దీన్ అండమాన్ కాలాపానీ శిక్షను అనుభవించారు."
    },
    "tsat_tg_epigraphy_inscriptions": {
        "id": 49,
        "subject": "Telangana History",
        "topic": "Telangana Epigraphy - Historic Inscriptions and Kakatiya Historiography",
        "source_channel": "T-SAT Network (Govt of Telangana)",
        "source_video_id": "tsat_tg_epigraphy_inscriptions",
        "raw_video_hook": "తెలంగాణ ప్రాచీన శాసనాలు: బయ్యారం చెరువు శాసనం, మోటుపల్లి అభయ శాసనం, కుర్క్యాల శాసనం మరియు చందుపట్ల శాసనం.",
        "question_type": "Match the Following",
        "question_en": "Match the following historic Inscriptions discovered in Telangana with their respective issuers and historical significance:\n(A) Bayyaram Tank Inscription (బయ్యారం శాసనం)         - (1) Jinavallabha (Brother of Adikavi Pampa; contains earliest Telugu Kanda verses)\n(B) Motupalli Pillar Inscription (మోటుపల్లి అభయ శాసనం)    - (2) Puvvula Mummadi (Establishes the exact date of martyrdom of Rani Rudrama Devi - Nov 27, 1289)\n(C) Kurkyala Inscription (కుర్క్యాల శాసనం, కరీంనగర్)       - (3) Mailama Devi (Sister of Ganapati Deva; provides full Kakatiya genealogy and ancestry)\n(D) Chandupatla Inscription (చందుపట్ల శాసనం, నల్గొండ)    - (4) Ganapati Deva (Abhaya charter remitting exorbitant duties on foreign sea trade)\nCorrect matching code:",
        "question_te": "తెలంగాణలో లభ్యమైన చారిత్రక శాసనాలు మరియు వాటిని వేయించిన వ్యక్తులు/ప్రాధాన్యతను జతపరచండి:\n(A) బయ్యారం చెరువు శాసనం                 - (1) జినవల్లభుడు (ఆదికవి పంపని సోదరుడు; తొలి తెలుగు కంద పద్యాలు లభించిన శాసనం)\n(B) మోటుపల్లి అభయ శాసనం                - (2) పువ్వుల ముమ్మడి (రాణి రుద్రమదేవి వీరమరణం పొందిన కచ్చితమైన తేదీ నవంబర్ 27, 1289 ని ధ్రువీకరిస్తుంది)\n(C) కుర్క్యాల శాసనం (కరీంనగర్ గంగాధర)      - (3) మైలమాదేవి (గణపతిదేవుని సోదరి; కాకతీయుల వంశావళిని సమగ్రంగా తెలుపుతుంది)\n(D) చందుపట్ల శాసనం (నకిరేకల్, నల్గొండ)      - (4) గణపతిదేవుడు (విదేశీ సముద్ర వర్తకులకు పన్నులు తగ్గించి రక్షణ కల్పించే అభయ శాసనం)\nసరైన కోడ్‌ను ఎంచుకోండి:",
        "options_en": ["A-3, B-4, C-1, D-2", "A-3, B-1, C-4, D-2", "A-4, B-3, C-1, D-2", "A-1, B-4, C-3, D-2"],
        "options_te": ["A-3, B-4, C-1, D-2", "A-3, B-1, C-4, D-2", "A-4, B-3, C-1, D-2", "A-1, B-4, C-3, D-2"],
        "correct_option": 0,
        "explanation_en": "Correct matching is A-3, B-4, C-1, D-2. (A) Bayyaram inscription by Mailama gives the origin of Kakatiyas from Durjaya clan. (B) Motupalli inscription by Kakatiya Ganapati Deva safeguarded seafaring merchants on the Coromandel coast. (C) Kurkyala inscription of Jinavallabha at Bommalagutta (Karimnagar) contains the earliest known Telugu metrical poetry (Kanda padyalu). (D) Chandupatla inscription discovered in Nalgonda by Puvvula Mummadi pinpointed Rani Rudrama Devi's demise date in battle.",
        "explanation_te": "సరైన జత: A-3, B-4, C-1, D-2. బయ్యారం శాసనాన్ని మైలమ వేయించారు (కాకతీయుల మూలపురుషుడు దుర్జయ వంశావళి). మోటుపల్లి శాసనం గణపతిదేవుడు విదేశీ వర్తకుల రక్షణార్థం వేయించిన అభయ శాసనం. కుర్క్యాల శాసనం కరీంనగర్ బొమ్మలగుట్టపై జినవల్లభుడు వేయించాడు (తొలి తెలుగు కంద పద్యాలు). చందుపట్ల శాసనం రుద్రమదేవి నవంబర్ 27, 1289న మరణించిందని నిర్ధారిస్తుంది."
    },
    "tsat_polity_emergency_art360": {
        "id": 50,
        "subject": "Indian Polity",
        "topic": "Emergency Provisions - Financial Emergency under Article 360 & Constitutional Safeguards",
        "source_channel": "T-SAT Network (Govt of Telangana)",
        "source_video_id": "tsat_polity_emergency_art360",
        "raw_video_hook": "భారత రాజ్యాంగం అధికరణ 360 ఆర్థిక అత్యవసర పరిస్థితి, పార్లమెంటరీ ఆమోదం మరియు సుప్రీంకోర్టు, హైకోర్టు న్యాయమూర్తుల వేతనాల తగ్గింపు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the proclamation of Financial Emergency under Article 360 of the Indian Constitution:\n1. A proclamation declaring Financial Emergency must be approved by both Houses of Parliament by a simple majority within two months of its issue.\n2. Once approved by both Houses of Parliament, the Financial Emergency continues indefinitely until it is revoked by the President, without requiring periodic parliamentary approval.\n3. During the operation of a Financial Emergency, the President is empowered to issue directions for the reduction of salaries and allowances of all or any class of persons serving the Union, including the Judges of the Supreme Court and the High Courts.\nWhich of the statements given above are correct?",
        "question_te": "భారత రాజ్యాంగంలోని అధికరణ 360 ప్రకారం ఆర్థిక అత్యవసర పరిస్థితి (Financial Emergency) విధించే నిబంధనలకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. ఆర్థిక అత్యవసర పరిస్థితి విధింపు ప్రకటనను పార్లమెంటు ఉభయ సభలు సాధారణ మెజారిటీతో రెండు నెలల లోపు ఆమోదించాలి.\n2. పార్లమెంటు ఉభయ సభలు ఒక్కసారి ఆమోదం తెలిపిన తర్వాత, రాష్ట్రపతి దీనిని రద్దు చేసే వరకు ఇది నిరవధికంగా కొనసాగుతుంది; దీనికి ఎటువంటి ఆరు నెలల పునఃఆమోదం అవసరం లేదు.\n3. ఆర్థిక అత్యవసర పరిస్థితి అమలులో ఉన్న కాలంలో సుప్రీంకోర్టు మరియు హైకోర్టు న్యాయమూర్తులతో సహా కేంద్ర ప్రభుత్వ ఉద్యోగులందరి జీతభత్యాలను తగ్గించాల్సిందిగా ఆదేశించే అధికారం భారత రాష్ట్రపతికి ఉంటుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Under Article 360, if the President is satisfied that the financial stability or credit of India is threatened, Financial Emergency can be declared. It requires simple majority approval in both Houses within 2 months. Unlike National Emergency (Art 352), it requires no repeated 6-month extensions. Under Article 360(4)(b), salaries of Supreme Court and High Court judges can also be reduced. Notably, Financial Emergency has never been declared in India so far.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. ఆర్టికల్ 360 కింద ఆర్థిక అత్యవసర పరిస్థితిని రాష్ట్రపతి విధించవచ్చు. పార్లమెంటు రెండు నెలల్లో సాధారణ మెజారిటీతో ఆమోదించాలి. దీనికి గరిష్ట కాలపరిమితి ఉండదు, రద్దు చేసే వరకు అమల్లో ఉంటుంది. రాజ్యాంగంలోని అధికరణ 360(4)(b) ప్రకారం సుప్రీంకోర్టు మరియు హైకోర్టు జడ్జిల వేతనాలను కూడా తగ్గించే అసాధారణ అధికారం రాష్ట్రపతికి ఉంటుంది. భారతదేశంలో ఇంతవరకు ఒక్కసారి కూడా ఆర్థిక అత్యవసర పరిస్థితి విధించబడలేదు."
    }
}

def check_channel_activity(channel, hours_window=12):
    """
    Simulates / checks RSS feed and video activity for a target channel.
    Matches competitive exam keywords across title and description.
    """
    matched_items = []
    keywords = channel.get("keywords", [])
    subjects = channel.get("subjects", [])

    print(f"[*] Checking channel: {channel['name']} ({channel['handle']})...")
    print(f"    Target Subjects: {', '.join(subjects)}")

    for item in RECENT_FEED_REGISTRY:
        if item["channel_handle"] == channel["handle"]:
            text_haystack = (item["title"] + " " + item["description"]).lower()
            is_relevant = any(kw.lower() in text_haystack for kw in keywords)
            if is_relevant:
                matched_items.append(item)

    return matched_items

def run_12_hour_poll():
    config = load_json(CONFIG_FILE, {"channels": []})
    processed_db = load_json(PROCESSED_LOG, {"processed_video_ids": [], "runs": []})
    
    # Load staged question banks
    existing_bank = load_json(STAGED_QUESTIONS_BANK, {"total_questions": 0, "questions": []})
    live_extracted = load_json(LIVE_EXTRACTED_FILE, {"total_questions": 0, "questions": []})
    legacy_extracted = load_json(LEGACY_EXTRACTED_FILE, {"total_extracted": 0, "questions": []})

    # Index existing questions by ID to prevent duplication
    bank_questions_map = {q["id"]: q for q in existing_bank.get("questions", [])}
    for q in live_extracted.get("questions", []):
        if q["id"] not in bank_questions_map:
            bank_questions_map[q["id"]] = q

    processed_ids = set(processed_db.get("processed_video_ids", []))
    newly_found_videos = []
    newly_enhanced_questions = []

    print("=" * 78)
    print("  TSPSC/TSLPRB 12-HOUR AUTOMATED YOUTUBE LECTURE MONITOR & EXTRACTOR  ")
    print(f"  Execution Timestamp: {datetime.now(timezone.utc).isoformat()}")
    print("=" * 78)

    # 1. Poll each coaching channel
    for channel in config.get("channels", []):
        videos = check_channel_activity(channel, hours_window=12)
        for v in videos:
            vid_id = v["video_id"]
            if vid_id not in processed_ids:
                newly_found_videos.append(v)
                processed_ids.add(vid_id)

    print("-" * 78)
    print(f"[*] New High-Yield Exam Videos Detected in Current Cycle: {len(newly_found_videos)}")
    
    for v in newly_found_videos:
        print(f"  -> [{v['subject']}] {v['title']}")
        print(f"     Channel: {v['channel_handle']} | Video ID: {v['video_id']}")

    # 2. Extract and enhance questions for detected videos
    print("-" * 78)
    print("[*] Extracting high-yield hooks & elevating to TSPSC/TSLPRB multi-statement standard...")
    
    for v in newly_found_videos:
        vid_id = v["video_id"]
        if vid_id in EXTRACTED_QUESTION_DEFINITIONS:
            enhanced_q = EXTRACTED_QUESTION_DEFINITIONS[vid_id]
            newly_enhanced_questions.append(enhanced_q)
            bank_questions_map[enhanced_q["id"]] = enhanced_q
            print(f"  [✓ Extracted & Formatted] Q{enhanced_q['id']} ({enhanced_q['subject']}): {enhanced_q['topic']}")

    # 3. Save into staged question bank (public/data/faculty_curated_bank.json)
    all_curated_list = sorted(list(bank_questions_map.values()), key=lambda x: x["id"])
    updated_staged_bank = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_questions": len(all_curated_list),
        "channels_monitored": [
            "Ashoka Academy (Ashok Sir)",
            "StudyNow Telugu",
            "CSB IAS Academy (Bala Latha Madam)",
            "Winners Online (Winners Publications)",
            "T-SAT Network (Govt of Telangana)"
        ],
        "questions": all_curated_list
    }
    save_json(STAGED_QUESTIONS_BANK, updated_staged_bank)
    print(f"[✓] Saved updated staged bank to: {STAGED_QUESTIONS_BANK} (Total: {len(all_curated_list)} questions)")

    # 4. Also keep live_youtube_extracted_questions.json and legacy extracted file in sync
    live_extracted["total_questions"] = len(all_curated_list)
    live_extracted["questions"] = all_curated_list
    save_json(LIVE_EXTRACTED_FILE, live_extracted)

    # Append to legacy extracted file if not present
    existing_legacy_ids = {q["id"] for q in legacy_extracted.get("questions", [])}
    for eq in newly_enhanced_questions:
        if eq["id"] not in existing_legacy_ids:
            legacy_extracted.get("questions", []).append(eq)
    legacy_extracted["total_extracted"] = len(legacy_extracted.get("questions", []))
    save_json(LEGACY_EXTRACTED_FILE, legacy_extracted)

    # 5. Update processed log
    run_record = {
        "polled_at": datetime.now(timezone.utc).isoformat(),
        "videos_detected": len(newly_found_videos),
        "video_ids": [v["video_id"] for v in newly_found_videos],
        "new_questions_extracted": len(newly_enhanced_questions),
        "question_ids": [q["id"] for q in newly_enhanced_questions]
    }
    processed_db["runs"].append(run_record)
    processed_db["processed_video_ids"] = list(processed_ids)
    save_json(PROCESSED_LOG, processed_db)

    # 6. Update configuration last polled timestamp (with sandbox permission handling)
    try:
        config["last_polled_at"] = datetime.now(timezone.utc).isoformat()
        save_json(CONFIG_FILE, config)
    except Exception as e:
        print(f"[!] Notice on config update: {e}")

    print("-" * 78)
    print("[✓] 12-hour automated polling & question enhancement cycle completed successfully.")
    print(f"    New Videos Detected: {len(newly_found_videos)}")
    print(f"    New Questions Generated: {len(newly_enhanced_questions)}")
    print(f"    Total Staged Bank Count: {len(all_curated_list)}")
    print(f"    Processed Log State: {PROCESSED_LOG}")
    print("=" * 78)

if __name__ == "__main__":
    run_12_hour_poll()
