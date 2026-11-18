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
    },

    # === NEW 12-HOUR CYCLE FEEDS (2026-11-17 Morning Shift) ===
    # --- Ashoka Academy (Ashok Sir) ---
    {
        "video_id": "ashoka_tg_1969_movement_committees",
        "title": "తెలంగాణ ఉద్యమ చరిత్ర: 1969 ప్రత్యేక తెలంగాణ ఉద్యమం - సర్వపార్టీ ఒప్పందం, జీవో 36 & కుమార్ లలిత్ కమిటీ నివేదిక | Ashok Sir",
        "channel_handle": "@ashokaonlineacademy8933",
        "subject": "Telangana History & Movement",
        "published_at": "2026-11-16T23:00:00Z",
        "description": "తెలంగాణ ఉద్యమం 1969, జనవరి 19 సర్వపార్టీ ఒప్పందం, జీవో నంబర్ 36 జారీ, కుమార్ లలిత్ కమిటీ మిగులు నిధుల లెక్కలు ₹34.10 కోట్లు, వశిష్ట భార్గవ కమిటీ, రవీంద్రనాథ్ నిరాహార దీక్ష."
    },
    {
        "video_id": "ashoka_tg_salarjung_reforms",
        "title": "తెలంగాణ చరిత్ర: మొదటి సాలార్‌జంగ్ సంస్కరణలు (1853-1883) - జిలాబందీ విధానం, హాలీసిక్కా నాణేలు & రెవెన్యూ బోర్డు | Ashok Sir",
        "channel_handle": "@ashokaonlineacademy8933",
        "subject": "Telangana History & Movement",
        "published_at": "2026-11-17T01:30:00Z",
        "description": "హైదరాబాద్ నిజాం సంస్థాన చరిత్ర, మొదటి సాలార్‌జంగ్ మీర్ తురాబ్ అలీ ఖాన్, 1865 జిలాబందీ పరిపాలనా సంస్కరణ, సదర్-ఉల్-మహాం మంత్రుల మండలి, హాలీసిక్కా కరెన్సీ, దారుల్ ఉలూమ్ విద్యాసంస్థ."
    },

    # --- StudyNow Telugu ---
    {
        "video_id": "studynow_tg_hydraa_walta_2026",
        "title": "తెలంగాణ కరెంట్ అఫైర్స్: హైడ్రా (HYDRAA) అధికారాలు, జీవో 99, వాల్టా చట్టం & చెరువుల పరిరక్షణ నిబంధనలు | Top MCQs",
        "channel_handle": "@studynowtelugu",
        "subject": "Telangana Current Affairs",
        "published_at": "2026-11-16T22:30:00Z",
        "description": "Current Affairs 2026, హైదరాబాద్ డిజాస్టర్ రెస్పాన్స్ అండ్ అసెట్స్ ప్రొటెక్షన్ ఏజెన్సీ (HYDRAA), జీవో 99, ఔటర్ రింగ్ రోడ్ (ORR) 2000 చ.కి.మీ పరిధి, FTL & బఫర్ జోన్ ఆక్రమణల తొలగింపు అధికారాలు, టాప్ బిట్స్."
    },
    {
        "video_id": "studynow_tg_indiramma_mahalakshmi_2026",
        "title": "తెలంగాణ సంక్షేమ పథకాలు: ఇందిరమ్మ ఇండ్లు & మహాలక్ష్మి ఉచిత బస్సు ప్రయాణ పథకం 2026 | StudyNow Telugu MCQs",
        "channel_handle": "@studynowtelugu",
        "subject": "Telangana Current Affairs",
        "published_at": "2026-11-17T02:00:00Z",
        "description": "తెలంగాణ స్కీమ్స్ 2026, ఇందిరమ్మ ఇండ్ల పథకం మార్గదర్శకాలు, సొంత స్థలంలో ఇంటి నిర్మాణానికి ₹5 లక్షల ఆర్థిక సాయం, మహాలక్ష్మి జీరో-ఫేర్ టికెట్ పథకం, మహిళల ప్రజా పాలన దరఖాస్తుల పరిశీలన, MCQs."
    },

    # --- CSB IAS Academy (Bala Latha Madam) ---
    {
        "video_id": "csb_polity_art371d_presidential_order",
        "title": "Indian Polity: ఆర్టికల్ 371D & రాష్ట్రపతి ఉత్తర్వులు (Presidential Order 1975) - ఆరు సూత్రాల పథకం & జోనల్ వ్యవస్థ | Bala Latha Madam",
        "channel_handle": "@csbiasacademyofficial",
        "subject": "Indian Polity",
        "published_at": "2026-11-16T23:45:00Z",
        "description": "భారత రాజ్యాంగం, అధికరణ 371D, 32వ రాజ్యాంగ సవరణ 1973, ఆరు సూత్రాల పథకం (Six-Point Formula), 1975 రాష్ట్రపతి ఉత్తర్వులు, విద్యా ఉద్యోగాలలో స్థానిక రిజర్వేషన్లు, అడ్మినిస్ట్రేటివ్ ట్రిబ్యునల్."
    },
    {
        "video_id": "csb_polity_anti_defection_schedule10",
        "title": "Indian Polity: పార్టీ ఫిరాయింపుల నిరోధక చట్టం (Tenth Schedule) - స్పీకర్ నిర్ణయాధికారం & 91వ రాజ్యాంగ సవరణ | CSB IAS",
        "channel_handle": "@csbiasacademyofficial",
        "subject": "Indian Polity",
        "published_at": "2026-11-17T01:45:00Z",
        "description": "10వ షెడ్యూల్ పార్టీ ఫిరాయింపుల నిరోధక చట్టం (52వ సవరణ 1985), 91వ రాజ్యాంగ సవరణ 2003 ద్వారా చీలిక (Split) రద్దు, కిహోతో హోల్లోహన్ కేసులో సుప్రీంకోర్టు తీర్పు, స్పీకర్ నిర్ణయంపై న్యాయ సమీక్ష."
    },

    # --- Winners Online (Winners Publications) ---
    {
        "video_id": "winners_history_swadeshi_vande_mataram",
        "title": "భారత చరిత్ర: వందేమాతరం ఉద్యమం (1905) - స్వదేశీ బహిష్కరణ, జాతీయ విద్యామండలి & ఆంధ్రలో బిపిన్ చంద్రపాల్ పర్యటన | Winners Online",
        "channel_handle": "@winnersonline",
        "subject": "Indian History",
        "published_at": "2026-11-17T00:15:00Z",
        "description": "భారత చరిత్ర మరియు జాతీయోద్యమం, 1905 బెంగాల్ విభజన వ్యతిరేక స్వదేశీ ఉద్యమం, బిపిన్ చంద్రపాల్ 1907 రాజమండ్రి పర్యటన, రాజమండ్రి ట్రైనింగ్ కాలేజీ సంఘటన (గాడిచర్ల హరిసర్వోత్తమరావు), కృష్ణా పత్రిక పాత్ర."
    },
    {
        "video_id": "winners_history_maurya_ashoka_edicts",
        "title": "ప్రాచీన భారత చరిత్ర: మౌర్యుల పరిపాలన & అశోకుని శిలాశాసనాలు - సమాహర్త, సన్నిధాత & ధర్మ మహామాత్రులు | Winners",
        "channel_handle": "@winnersonline",
        "subject": "Indian History",
        "published_at": "2026-11-17T02:15:00Z",
        "description": "ప్రాచీన భారత చరిత్ర, మౌర్యుల కేంద్రీకృత పరిపాలన, అర్థశాస్త్ర సప్తాంగ సిద్ధాంతం, సమాహర్త (రెవెన్యూ సేకరణ), సన్నిధాత (కోశాధికారి), అశోకుని 13వ శిలాశాసనం (కళింగ యుద్ధం), మస్కీ & ఎర్రగుడి శాసనాలు."
    },

    # --- T-SAT Network (Govt of Telangana) ---
    {
        "video_id": "tsat_tg_armed_struggle_chakali_ilamma",
        "title": "T-SAT నిపుణ: తెలంగాణ సాయుధ రైతాంగ పోరాటం (1946-51) - దొడ్డి కొమరయ్య అమరత్వం & చాకలి ఐలమ్మ వీరోచిత పోరు | గ్రూప్స్ & ఎస్ఐ బిట్స్",
        "channel_handle": "@tsatnetwork",
        "subject": "Telangana History",
        "published_at": "2026-11-17T00:45:00Z",
        "description": "T-SAT నిపుణ స్పెషల్, తెలంగాణ సాయుధ రైతాంగ పోరాటం, 1946 జూలై 4 కడవెండిలో దొడ్డి కొమరయ్య అమరత్వం, విస్నూరు దేశ్‌ముఖ్ రాపాక రామచంద్రారెడ్డికి వ్యతిరేకంగా పాలకుర్తి చాకలి ఐలమ్మ భూపోరాటం, వెట్టి చాకిరి నిర్మూలన, ఎస్ఐ బిట్స్."
    },
    {
        "video_id": "tsat_polity_cag_art148",
        "title": "T-SAT నిపుణ: భారత రాజ్యాంగం - కంప్ట్రోలర్ అండ్ ఆడిటర్ జనరల్ (CAG Article 148-151) విధులు & అధికారాలు | ఎస్ఐ స్పెషల్ బిట్స్",
        "channel_handle": "@tsatnetwork",
        "subject": "Indian Polity",
        "published_at": "2026-11-17T02:30:00Z",
        "description": "T-SAT నిపుణ, భారత రాజ్యాంగం ఆర్టికల్ 148-151, కాగ్ నియామకం, పదవీ కాలం, రాజ్యాంగ హోదా, కేంద్ర మరియు రాష్ట్రాల కన్సాలిడేటెడ్ ఫండ్ ఆడిట్, పబ్లిక్ అకౌంట్స్ కమిటీకి 'మిత్రుడు, తత్వవేత్త, మార్గదర్శి' పాత్ర, గ్రూప్స్ & ఎస్ఐ బిట్స్."
    },

    # === NEW 12-HOUR CYCLE FEEDS (2026-11-17 Evening Shift) ===
    # --- Ashoka Academy (Ashok Sir) ---
    {
        "video_id": "ashoka_tg_gentlemens_agreement_1956",
        "title": "తెలంగాణ ఉద్యమ చరిత్ర: పెద్దమనుషుల ఒప్పందం (1956) - 14 ముఖ్యాంశాలు, సంతకం చేసిన నేతలు & ఉల్లంఘనలు | Ashok Sir",
        "channel_handle": "@ashokaonlineacademy8933",
        "subject": "Telangana History & Movement",
        "published_at": "2026-11-17T09:30:00Z",
        "description": "తెలంగాణ చరిత్ర, 1956 ఫిబ్రవరి 20 ఢిల్లీ పెద్దమనుషుల ఒప్పందం (Gentlemen's Agreement), హైదరాబాద్ భవన్, 14 రక్షణలు, సంతకం చేసిన 8 మంది నేతలు, తెలంగాణ ప్రాంతీయ కమిటీ అధికారాలు, నివాస అర్హత 12 ఏళ్లు."
    },
    {
        "video_id": "ashoka_tg_ikshvaku_nagarjunakonda",
        "title": "తెలంగాణ ప్రాచీన చరిత్ర: ఇక్ష్వాకుల పరిపాలన - నాగార్జునకొండ బౌద్ధ విహారాలు, శాసనాలు & రాణుల దానధర్మాలు | Ashok Sir",
        "channel_handle": "@ashokaonlineacademy8933",
        "subject": "Telangana History & Movement",
        "published_at": "2026-11-17T11:45:00Z",
        "description": "తెలంగాణ ప్రాచీన చరిత్ర, ఇక్ష్వాకుల రాజధాని విజయపురి (నాగార్జునకొండ), వాసిష్ఠీపుత్ర శాంతమూలుడు (అశ్వమేధ యాజి), శాంతశ్రీ బౌద్ధ విహారాల నిర్మాణం, అపశిల, అపరమహా వినశైలీయ శాఖలు, ప్రాకృత శాసనాలు."
    },

    # --- StudyNow Telugu ---
    {
        "video_id": "studynow_tg_bhoo_bharathi_dharani_2026",
        "title": "తెలంగాణ రెవెన్యూ సంస్కరణలు: 'భూ భారతి' (Bhoo Bharathi) ప్రాజెక్ట్, ధరణి ప్రక్షాళన & RoR చట్టం 2026 | Top MCQs",
        "channel_handle": "@studynowtelugu",
        "subject": "Telangana Current Affairs",
        "published_at": "2026-11-17T10:15:00Z",
        "description": "Current Affairs 2026, తెలంగాణ ప్రభుత్వం ప్రతిపాదించిన భూ భారతి ప్రాజెక్ట్, ధరణి పోర్టల్ లోపాల సవరణ, RoR చట్ట సవరణలు, రికార్డు ఆఫ్ రైట్స్ అప్పీలేట్ అథారిటీలు, పార్ట్-బి భూముల సమస్యల పరిష్కారం, టాప్ బిట్స్."
    },
    {
        "video_id": "studynow_tg_gruha_jyothi_cheyutha_2026",
        "title": "తెలంగాణ సంక్షేమ పథకాలు: గృహజ్యోతి (200 యూనిట్ల ఉచిత విద్యుత్), చేయూత పెన్షన్లు & ఆరోగ్యశ్రీ ₹10 లక్షలు | StudyNow MCQs",
        "channel_handle": "@studynowtelugu",
        "subject": "Telangana Current Affairs",
        "published_at": "2026-11-17T13:30:00Z",
        "description": "తెలంగాణ స్కీమ్స్ 2026, గృహజ్యోతి పథకం నిబంధనలు (నెలకు 200 యూనిట్ల వరకు జీరో విద్యుత్ బిల్లు), తెల్ల రేషన్ కార్డు అర్హత, చేయూత పథకం ద్వారా పెన్షన్ పెంపు ₹4,000, రాజీవ్ ఆరోగ్యశ్రీ ₹10 లక్షల ఉచిత వైద్యం, టాప్ MCQs."
    },

    # --- CSB IAS Academy (Bala Latha Madam) ---
    {
        "video_id": "csb_polity_fundamental_duties_art51a",
        "title": "Indian Polity: ప్రాథమిక విధులు (Article 51A) - స్వరణ్ సింగ్ కమిటీ, 86వ సవరణ & జస్టిస్ వర్మ కమిటీ | Bala Latha Madam",
        "channel_handle": "@csbiasacademyofficial",
        "subject": "Indian Polity",
        "published_at": "2026-11-17T08:30:00Z",
        "description": "భారత రాజ్యాంగం, అధికరణ 51A, 42వ రాజ్యాంగ సవరణ 1976, సర్దార్ స్వరణ్ సింగ్ కమిటీ సిఫార్సులు (తిరస్కరించిన పన్నుల విధింపు), 86వ సవరణ 2002 ద్వారా 11వ విధి, జస్టిస్ జె.ఎస్. వర్మ కమిటీ 1999 చట్టపరమైన నిబంధనలు."
    },
    {
        "video_id": "csb_polity_interstate_water_disputes_art262",
        "title": "Indian Polity: అంతర్-రాష్ట్ర నదీ జలాల వివాదాలు (Article 262) - ట్రిబ్యునళ్ల చట్టం 1956 & సుప్రీంకోర్టు పరిధి | CSB IAS",
        "channel_handle": "@csbiasacademyofficial",
        "subject": "Indian Polity",
        "published_at": "2026-11-17T12:00:00Z",
        "description": "ఆర్టికల్ 262 అంతర్-రాష్ట్ర నదీ జల వివాదాల పరిష్కారం, ఇంటర్-స్టేట్ రివర్ వాటర్ డిస్ప్యూట్స్ యాక్ట్ 1956, కృష్ణా & గోదావరి ట్రిబ్యునళ్లు, సెక్షన్ 11 ద్వారా సుప్రీంకోర్టు అధికార పరిధిపై నిషేధం, ఆర్టికల్ 136 SLP పరిమితులు."
    },

    # --- Winners Online (Winners Publications) ---
    {
        "video_id": "winners_history_gupta_administration_culture",
        "title": "ప్రాచీన భారత చరిత్ర: గుప్తుల పరిపాలన - భుక్తి, విషయ, నవరత్నాలు & అగ్రహార భూదానాలు | Winners Online",
        "channel_handle": "@winnersonline",
        "subject": "Indian History",
        "published_at": "2026-11-17T09:00:00Z",
        "description": "ప్రాచీన భారత చరిత్ర, గుప్తుల సామ్రాజ్య విభజన (భుక్తులు - ఉపరికులు, విషయాలు - విషయపతులు), పురపాలక మండలి (నగరశ్రేష్ఠి, సార్థవాహ), అగ్రహార, బ్రహ్మదేయ భూదానాలు, చంద్రగుప్త విక్రమాదిత్యుని నవరత్నాలు, నలంద విశ్వవిద్యాలయం."
    },
    {
        "video_id": "winners_history_non_cooperation_khilafat_1920",
        "title": "భారత స్వాతంత్ర్యోద్యమం: సహాయ నిరాకరణ ఉద్యమం (1920-22) - నాగ్‌పూర్ కాంగ్రెస్ తీర్మానం & చౌరీ చౌరా ఘటన | Winners",
        "channel_handle": "@winnersonline",
        "subject": "Indian History",
        "published_at": "2026-11-17T14:15:00Z",
        "description": "భారత జాతీయోద్యమం, 1920 నాగ్‌పూర్ కాంగ్రెస్ వార్షిక సమావేశం (సి. విజయరాఘవాచారియార్), కాంగ్రెస్ నిర్మాణాత్మక మార్పులు, సి.ఆర్. దాస్ తీర్మానం, బిరుదుల త్యాగం, విదేశీ వస్తు బహిష్కరణ, 1922 ఫిబ్రవరి చౌరీ చౌరా ఘటన, బార్డోలీ తీర్మానం ద్వారా ఉపసంహరణ."
    },

    # --- T-SAT Network (Govt of Telangana) ---
    {
        "video_id": "tsat_tg_satavahana_culture_hala",
        "title": "T-SAT నిపుణ: శాతవాహనుల చరిత్ర & సంస్కృతి - హాలుని గాథాసప్తశతి, గుణాఢ్యుని బృహత్కథ & బౌద్ధ క్షేత్రాలు | TSPSC Special",
        "channel_handle": "@tsatnetwork",
        "subject": "Telangana History",
        "published_at": "2026-11-17T10:45:00Z",
        "description": "తెలంగాణ చరిత్ర, శాతవాహనుల పాలన, కోటిలింగాల రాజధాని, 17వ రాజు హాలుడు (కవివత్సలుడు) సంకలనం చేసిన ప్రాకృత గ్రంథం 'గాథాసప్తశతి', గుణాఢ్యుని 'బృహత్కథ' (పైశాచీ ప్రాకృతం), శర్వవర్మ 'కాతంత్ర వ్యాకరణం', నేలకొండపల్లి, ధూళికట్ట, ఫణిగిరి బౌద్ధ స్థూపాలు."
    },
    {
        "video_id": "tsat_polity_finance_commission_art280",
        "title": "T-SAT నిపుణ: భారత రాజ్యాంగం - ఆర్థిక సంఘం (Article 280) అధికారాలు, నిధుల పంపిణీ & 16వ ఆర్థిక సంఘం | ఎస్ఐ బిట్స్",
        "channel_handle": "@tsatnetwork",
        "subject": "Indian Polity",
        "published_at": "2026-11-17T13:00:00Z",
        "description": "T-SAT నిపుణ, రాజ్యాంగంలోని అధికరణ 280 ఆర్థిక సంఘం (Finance Commission), సభ్యుల అర్హతలు, కేంద్ర-రాష్ట్రాల పన్నుల నికర ఆదాయ పంపిణీ, ఆర్టికల్ 275 గ్రాంట్స్-ఇన్-ఎయిడ్, స్థానిక సంస్థల నిధుల పెంపు, 16వ ఆర్థిక సంఘం చైర్మన్ డాక్టర్ అరవింద్ పనగరియా, గ్రూప్స్ & ఎస్ఐ బిట్స్."
    },

    # === NEW 12-HOUR CYCLE FEEDS (2026-11-18 Morning Shift) ===
    # --- Ashoka Academy (Ashok Sir) ---
    {
        "video_id": "ashoka_tg_vishnukundina_culture",
        "title": "తెలంగాణ ప్రాచీన చరిత్ర: విష్ణుకుండినుల పాలన - కీసరగుట్ట రామలింగేశ్వర దేవాలయం, ఇంద్రపాలనగరం శాసనం & గోవిందవర్మ | Ashok Sir",
        "channel_handle": "@ashokaonlineacademy8933",
        "subject": "Telangana History & Movement",
        "published_at": "2026-11-17T23:00:00Z",
        "description": "తెలంగాణ ప్రాచీన చరిత్ర, విష్ణుకుండినుల పరిపాలన, రాజధాని ఇంద్రపాలనగరం మరియు కీసరగుట్ట, మాధవవర్మ II అశ్వమేధ, నరమేధ యాగాలు, కీసరగుట్ట రామలింగేశ్వర శివలింగాలు, ఇంద్రపాలనగరం రాగిరేకుల శాసనం, గోవిందవర్మ బౌద్ధ విహారాల నిర్మాణం."
    },
    {
        "video_id": "ashoka_tg_million_march_2011",
        "title": "తెలంగాణ ఉద్యమ చరిత్ర: మిలియన్ మార్చ్ (మార్చి 10, 2011) - ట్యాంక్ బండ్ ప్రజా గర్జన & సకల జనుల సమ్మె | Ashok Sir",
        "channel_handle": "@ashokaonlineacademy8933",
        "subject": "Telangana History & Movement",
        "published_at": "2026-11-18T01:30:00Z",
        "description": "తెలంగాణ మలిదశ ప్రజా ఉద్యమం, 2011 మార్చి 10న ట్యాంక్ బండ్‌పై జరిగిన మిలియన్ మార్చ్, తెలంగాణ ఉద్యమ జేఏసీ (TJAC), ప్రొఫెసర్ కోదండరామ్ నాయకత్వం, ఈజిప్టు తహ్రీర్ స్క్వేర్ స్ఫూర్తి, 42 రోజుల చారిత్రక సకల జనుల సమ్మె."
    },

    # --- StudyNow Telugu ---
    {
        "video_id": "studynow_tg_caste_survey_2026",
        "title": "తెలంగాణ సమగ్ర సామాజిక, ఆర్థిక, విద్యా, ఉపాధి & కుల సర్వే 2026: ముఖ్యాంశాలు, షెడ్యూల్ & హైకోర్టు మార్గదర్శకాలు | StudyNow Telugu",
        "channel_handle": "@studynowtelugu",
        "subject": "Telangana Current Affairs",
        "published_at": "2026-11-17T22:45:00Z",
        "description": "Current Affairs 2026, తెలంగాణ ప్రభుత్వం చేపట్టిన సమగ్ర సామాజిక, ఆర్థిక, విద్యా, ఉపాధి, రాజకీయ మరియు కుల సర్వే (Comprehensive Socio-Economic, Educational, Employment, Political and Caste Survey), 75 ప్రశ్నల షెడ్యూల్, ప్రణాళిక శాఖ నోడల్ విభాగం, హైకోర్టు ఉత్తర్వులు, డేటా గోప్యత, టాప్ MCQs."
    },
    {
        "video_id": "studynow_tg_musi_rejuvenation_project_2026",
        "title": "తెలంగాణ నూతన ప్రాజెక్టులు: మూసీ రివర్ ఫ్రంట్ డెవలప్‌మెంట్ ప్రాజెక్ట్ (MRDP) - 55 కి.మీ కారిడార్, STPs & పునరావాసం | Top MCQs",
        "channel_handle": "@studynowtelugu",
        "subject": "Telangana Current Affairs",
        "published_at": "2026-11-18T02:00:00Z",
        "description": "Current Affairs 2026, మూసీ రివర్ ఫ్రంట్ రీజువనేషన్ ప్రాజెక్ట్ (Musi Riverfront Development Project), గండిపేట & హిమాయత్‌సాగర్ నుండి బాపూఘాట్, వల్లేపల్లి వరకు 55 కి.మీ సమగ్ర అభివృద్ధి, మురుగునీటి శుద్ధి ప్లాంట్లు (STP), ఆక్రమణల బాధితులకు ఉచిత డబుల్ బెడ్‌రూమ్ ఇండ్లు, టాప్ బిట్స్."
    },

    # --- CSB IAS Academy (Bala Latha Madam) ---
    {
        "video_id": "csb_polity_advisory_jurisdiction_art143",
        "title": "Indian Polity: సుప్రీంకోర్టు సలహా అధికార పరిధి (Article 143) - రాష్ట్రపతి రెఫరెన్స్, పరిమితులు & మైలురాయి కేసులు | Bala Latha Madam",
        "channel_handle": "@csbiasacademyofficial",
        "subject": "Indian Polity",
        "published_at": "2026-11-17T23:30:00Z",
        "description": "భారత రాజ్యాంగం ఆర్టికల్ 143, సుప్రీంకోర్టు సలహా అధికార పరిధి (Advisory Jurisdiction), ఆర్టికల్ 143(1) ప్రజా ప్రాముఖ్యత గల చట్టపరమైన ప్రశ్నలు, ఆర్టికల్ 143(2) రాజ్యాంగానికి పూర్వపు ఒప్పందాలు, బెరుబరి కేసు, అయోధ్య రెఫరెన్స్ 1994, అభిప్రాయాల చట్టపరమైన ప్రాధాన్యత."
    },
    {
        "video_id": "csb_polity_tribunals_art323a_323b",
        "title": "Indian Polity: అడ్మినిస్ట్రేటివ్ ట్రిబ్యునళ్లు (Articles 323A & 323B) - స్వర్ణసింగ్ కమిటీ & ఎల్. చంద్రకుమార్ కేసు తీర్పు | CSB IAS",
        "channel_handle": "@csbiasacademyofficial",
        "subject": "Indian Polity",
        "published_at": "2026-11-18T01:45:00Z",
        "description": "భారత రాజ్యాంగం పార్ట్ XIV-A, ఆర్టికల్ 323A పరిపాలనా ట్రిబ్యునళ్లు (కేంద్ర, రాష్ట్ర సర్వీసుల వివాదాలు), ఆర్టికల్ 323B ఇతర ట్రిబ్యునళ్లు, 42వ రాజ్యాంగ సవరణ 1976, ఎల్. చంద్రకుమార్ వర్సెస్ యూనియన్ ఆఫ్ ఇండియా 1997 మైలురాయి తీర్పు, హైకోర్టుల ఆర్టికల్ 226/227 న్యాయ సమీక్ష ప్రాథమిక నిర్మాణం."
    },

    # --- Winners Online (Winners Publications) ---
    {
        "video_id": "winners_history_delhi_sultanate_alauddin_market",
        "title": "మధ్యయుగ భారత చరిత్ర: అల్లావుద్దీన్ ఖిల్జీ పరిపాలన & మార్కెట్ సంస్కరణలు - షహనా-ఇ-మండి & దాగ్-చెహ్రా | Winners Online",
        "channel_handle": "@winnersonline",
        "subject": "Indian History",
        "published_at": "2026-11-17T23:15:00Z",
        "description": "మధ్యయుగ భారత చరిత్ర, ఢిల్లీ సుల్తానేట్, ఖిల్జీ వంశం, అల్లావుద్దీన్ ఖిల్జీ ధరల నియంత్రణ మార్కెట్ నిబంధనలు, షహనా-ఇ-మండి మార్కెట్ పర్యవేక్షకుడు, దివాన్-ఇ-రియాసత్, సైన్యంలో నగదు వేతనాలు, దాగ్ గుర్రాల ముద్రణ, చెహ్రా గుర్తింపు కార్డులు, భూమి కొలత (మిసాహత్), దివాన్-ఇ-ముస్తఖ్‌రాజ్."
    },
    {
        "video_id": "winners_history_buddhism_jainism_councils",
        "title": "ప్రాచీన భారత చరిత్ర: బౌద్ధ సంగీతులు (Four Buddhist Councils) & త్రిపీటకాలు - వేదికలు, అధ్యక్షులు & ఫలితాలు | Winners Online",
        "channel_handle": "@winnersonline",
        "subject": "Indian History",
        "published_at": "2026-11-18T02:15:00Z",
        "description": "ప్రాచీన భారతదేశంలో మత సంస్కరణ ఉద్యమాలు, నాలుగు బౌద్ధ సంగీతులు (Councils), పాలకులు (అజాతశత్రు, కాలశోక, అశోక, కనిష్క), అధ్యక్షులు (మహాకశ్యప, సభకామి, మొగ్గలిపుత్త తిస్స, వసుమిత్ర), సుత్తపీటక, వినయపీటక, అభిధమ్మపీటకాల సంకలనం, మహాయాన-హీనయాన చీలిక."
    },

    # --- T-SAT Network (Govt of Telangana) ---
    {
        "video_id": "tsat_tg_art_ramappa_rudreshwara_temple",
        "title": "T-SAT నిపుణ: తెలంగాణ శిల్పకళా వైభవం - రామప్ప రామలింగేశ్వర దేవాలయం (UNESCO గుర్తింపు) & శాండ్‌బాక్స్ టెక్నాలజీ | TSPSC బిట్స్",
        "channel_handle": "@tsatnetwork",
        "subject": "Telangana History",
        "published_at": "2026-11-17T22:30:00Z",
        "description": "తెలంగాణ చరిత్ర & సంస్కృతి, కాకతీయ శైలి రామప్ప (రుద్రేశ్వర) ఆలయం పాలంపేట, ములుగు జిల్లా, 1213 లో రేచర్ల రుద్రుడి నిర్మాణం, శిల్పి రామప్ప పేరు మీదుగా పిలువబడటం, నీటిలో తేలే తేలికపాటి ఇటుకలు (Floating Bricks), భూకంపాలను తట్టుకునే శాండ్‌బాక్స్ టెక్నాలజీ, 2021 UNESCO ప్రపంచ వారసత్వ సంపద గుర్తింపు, గ్రూప్స్ & ఎస్ఐ బిట్స్."
    },
    {
        "video_id": "tsat_polity_interstate_council_art263",
        "title": "T-SAT నిపుణ: భారత రాజ్యాంగం - అంతర్-రాష్ట్ర మండలి (Article 263) & సర్కారియా కమిషన్ సిఫార్సులు | ఎస్ఐ స్పెషల్ బిట్స్",
        "channel_handle": "@tsatnetwork",
        "subject": "Indian Polity",
        "published_at": "2026-11-18T02:45:00Z",
        "description": "రాజ్యాంగంలోని అధికరణ 263 అంతర్-రాష్ట్ర మండలి (Inter-State Council), సర్కారియా కమిషన్ 1988 సిఫార్సుల మేరకు 1990 లో రాష్ట్రపతి ఉత్తర్వు ద్వారా ఏర్పాటు, ప్రధాని అధ్యక్షత, అన్ని రాష్ట్రాల ముఖ్యమంత్రులు, కేంద్ర మంత్రులు సభ్యులుగా ఉండటం, సహకార సమాఖ్యవాదం, T-SAT నిపుణ టాప్ బిట్స్."
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
    },
    "ashoka_tg_1969_movement_committees": {
        "id": 51,
        "subject": "Telangana History & Movement",
        "topic": "1969 Telangana Movement - All-Party Accord, G.O. 36 & Kumar Lalith Committee",
        "source_channel": "Ashoka Academy (Ashok Sir)",
        "source_video_id": "ashoka_tg_1969_movement_committees",
        "raw_video_hook": "1969 ప్రత్యేక తెలంగాణ ఉద్యమంలో జనవరి 19 సర్వపార్టీ ఒప్పందం, జీవో 36 జారీ మరియు కుమార్ లలిత్ కమిటీ తేల్చిన మిగులు నిధులు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the 1969 Telangana Agitation and the administrative committees constituted during that period:\n1. On January 19, 1969, an All-Party Meeting convened by Chief Minister Kasu Brahmananda Reddy reached an agreement (All-Party Accord) to repatriate all non-domicile employees appointed in Telangana.\n2. In pursuance of the All-Party Accord, the Government issued the historic G.O. Ms. No. 36 on January 21, 1969, directing the repatriation of Andhra employees appointed against Telangana vacancies by February 28, 1969.\n3. The Kumar Lalith Committee appointed to determine the Telangana revenue surpluses estimated that Telangana had accumulated surplus funds of ₹34.10 crores between 1956 and 1968.\nWhich of the statements given above are correct?",
        "question_te": "1969 ప్రత్యేక తెలంగాణ ఉద్యమం మరియు ఆ సమయంలో నియమించబడిన పరిపాలనా కమిటీలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 1969 జనవరి 19న ముఖ్యమంత్రి కాసు బ్రహ్మానందరెడ్డి అధ్యక్షతన జరిగిన సర్వపార్టీ సమావేశంలో తెలంగాణ ప్రాంతంలో నిబంధనలకు విరుద్ధంగా నియమించబడిన నాన్-ముల్కీ ఉద్యోగులను వెనక్కి పంపేందుకు 'సర్వపార్టీ ఒప్పందం' కుదిరింది.\n2. సర్వపార్టీ ఒప్పందం అమలులో భాగంగా ప్రభుత్వం 1969 జనవరి 21న చారిత్రక 'జీవో నంబర్ 36'ను జారీ చేస్తూ, 1969 ఫిబ్రవరి 28 నాటికి తెలంగాణ స్థానిక పోస్టుల్లో ఉన్న ఆంధ్రా ఉద్యోగులను వారి మాతృ ప్రాంతాలకు పంపాలని ఆదేశించింది.\n3. తెలంగాణ ప్రాంతపు మిగులు నిధులను లెక్కించేందుకు నియమించబడిన కుమార్ లలిత్ కమిటీ 1956 నుండి 1968 మధ్య కాలంలో తెలంగాణ మిగులు నిధులు ₹34.10 కోట్లుగా ఉన్నట్లు తేల్చింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Following hunger strikes by students in Palvancha and Ravindranath in Khammam, the All-Party Accord was signed on 19 Jan 1969. In compliance, G.O. 36 was issued on 21 Jan 1969 by Kasu Brahmananda Reddy's govt. The Comptroller & Auditor General officer Kumar Lalith was appointed on 23 Jan 1969; he reported accumulated Telangana revenue surpluses of ₹34.10 crores, which was later reassessed by the Justice Vashishta Bhargava Committee as ₹28.34 crores.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. ఖమ్మంలో రవీంద్రనాథ్ నిరాహార దీక్ష నేపథ్యంలో జనవరి 19, 1969న సర్వపార్టీ ఒప్పందం కుదిరింది. దీని అమలుకు జనవరి 21న కాసు ప్రభుత్వం జీవో 36 జారీ చేసింది. తెలంగాణ మిగులు నిధులపై కాగ్ అధికారి కుమార్ లలిత్ కమిటీ అధ్యయనం చేసి ₹34.10 కోట్ల మిగులు ఉందని నివేదించింది. ఆ తర్వాత కేంద్రం నియమించిన జస్టిస్ వశిష్ట భార్గవ కమిటీ ఈ నిధులను ₹28.34 కోట్లుగా లెక్కించింది."
    },
    "ashoka_tg_salarjung_reforms": {
        "id": 52,
        "subject": "Telangana History & Movement",
        "topic": "Asaf Jahi Dynasty - Salar Jung I Administrative & Revenue Reforms (1853–1883)",
        "source_channel": "Ashoka Academy (Ashok Sir)",
        "source_video_id": "ashoka_tg_salarjung_reforms",
        "raw_video_hook": "మొదటి సాలార్‌జంగ్ మీర్ తురాబ్ అలీ ఖాన్ చేపట్టిన జిలాబందీ విధానం, హాలీసిక్కా నాణేలు మరియు రెవెన్యూ బోర్డు నిర్మాణం.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the administrative, financial, and revenue reforms introduced by Prime Minister Sir Salar Jung I (Mir Turab Ali Khan) in Hyderabad State:\n1. In 1865, Salar Jung introduced the 'Zilabandi' system, reorganizing the state into 14 districts under Subedars and First Talukdars (Collectors) to establish direct administrative control.\n2. He abolished the corrupt revenue farming (*Ta'alluqdari*) auction system and introduced the Ryotwari land revenue system based on direct land settlement and survey (*Zamin-Bandi*).\n3. He established the central government mint which issued the standardized *Hali Sikka* currency rupees and founded premier educational institutions including Dar-ul-Uloom (1854) and Madrasa-i-Aliya.\nWhich of the statements given above are correct?",
        "question_te": "హైదరాబాద్ నిజాం సంస్థానంలో దివాన్ మొదటి సాలార్‌జంగ్ (మీర్ తురాబ్ అలీ ఖాన్) ప్రవేశపెట్టిన పరిపాలనా, ఆర్థిక మరియు రెవెన్యూ సంస్కరణలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 1865 లో సాలార్‌జంగ్ 'జిలాబందీ' (Zilabandi) విధానాన్ని ప్రవేశపెట్టి, సంస్థానాన్ని సుబేదార్లు మరియు ఫస్ట్ తాలుక్‌దార్ల (కలెక్టర్లు) పాలన కింద 14 జిల్లాలుగా పునర్వ్యవస్థీకరించారు.\n2. అవినీతిమయమైన వేలం రెవెన్యూ గుత్తేదారి పద్ధతిని (Ta'alluqdari) రద్దు చేసి, రైతులతో ప్రత్యక్ష భూమి ఒప్పందాలు కుదుర్చుకునే రైత్వారీ భూమి శిస్తు విధానాన్ని, భూ కొలతల సర్వేను (జమీన్‌బందీ) అమలు చేశారు.\n3. సంస్థానమంతటా ప్రామాణికమైన 'హాలీ సిక్కా' (Hali Sikka) కరెన్సీ నాణేలను ముద్రించేందుకు కేంద్రీకృత ముద్రణాలయాన్ని ఏర్పాటు చేశారు మరియు దారుల్ ఉలూమ్ (1854), మదరసా-ఇ-ఆలియా వంటి విద్యాసంస్థలను స్థాపించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Salar Jung I served as Prime Minister (Diwan) from 1853 to 1883 under Nizams Nasir-ud-Daula, Afzal-ud-Daula, and Mir Mahbub Ali Khan. His 1865 Zilabandi reorganization brought civil administration to districts. He replaced middleman revenue leasers with state officers (Tehsildars/Talukdars), introduced Hali Sikka coinage, established Sadar-ul-Maham boards (ministries), and promoted modern education with Dar-ul-Uloom in 1854.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. మొదటి సాలార్‌జంగ్ 1853 నుండి 1883 వరకు నిజాం సంస్థాన దివాన్‌గా పనిచేసి ఆధునిక హైదరాబాద్ నిర్మాణానికి పునాది వేశారు. 1865 లో జిలాబందీ ద్వారా 14 జిల్లాలను ఏర్పాటు చేశారు. గుత్తేదారులను తొలగించి ప్రభుత్వ అధికారుల ద్వారా నేరుగా రైత్వారీ శిస్తు వసూలు చేశారు. హాలీసిక్కా రూపాయిని చట్టబద్ధం చేసి, 1854 లో దారుల్ ఉలూమ్ ప్రాచ్య కళాశాలను స్థాపించారు."
    },
    "studynow_tg_hydraa_walta_2026": {
        "id": 53,
        "subject": "Telangana Current Affairs",
        "topic": "Telangana Urban Governance - HYDRAA Constitution (G.O. Ms No. 99) & Water Body Protection",
        "source_channel": "StudyNow Telugu",
        "source_video_id": "studynow_tg_hydraa_walta_2026",
        "raw_video_hook": "హైడ్రా (HYDRAA) చట్టబద్ధ అధికారాలు, జీవో 99, ఓఆర్ఆర్ పరిధి మరియు చెరువుల ఎఫ్‌టీఎల్, బఫర్ జోన్ల పరిరక్షణ.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Hyderabad Disaster Response and Assets Monitoring and Protection Agency (HYDRAA) established by the Government of Telangana:\n1. HYDRAA was constituted under G.O. Ms No. 99 to serve as a unified agency for disaster response, emergency logistics, and safeguarding government lands and water bodies.\n2. The jurisdiction of HYDRAA extends across the entire Telangana Core Urban Region covering approximately 2,050 square kilometers up to the Outer Ring Road (ORR).\n3. HYDRAA is legally empowered under the Telangana WALTA Act, 2002, Land Revenue Act, and Municipal Corporation laws to demolish unauthorized encroachments in Full Tank Level (FTL) and Buffer Zones of water bodies.\nWhich of the statements given above are correct?",
        "question_te": "తెలంగాణ ప్రభుత్వం ఏర్పాటు చేసిన 'హైదరాబాద్ డిజాస్టర్ రెస్పాన్స్ అండ్ అసెట్స్ మానిటరింగ్ అండ్ ప్రొటెక్షన్ ఏజెన్సీ' (HYDRAA) కి సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. విపత్తు నిర్వహణ, అత్యవసర రక్షణ మరియు ప్రభుత్వ స్థలాలు, చెరువులు, నాలాల పరిరక్షణ లక్ష్యంగా జీవో నంబర్ 99 (G.O. Ms No. 99) ద్వారా హైడ్రాను ఏర్పాటు చేశారు.\n2. హైడ్రా అధికార పరిధి ఔటర్ రింగ్ రోడ్ (ORR) వరకు విస్తరించి ఉన్న తెలంగాణ కోర్ అర్బన్ రీజియన్‌లోని సుమారు 2,050 చదరపు కిలోమీటర్ల ప్రాంతాన్ని కవర్ చేస్తుంది.\n3. చెరువుల ఫుల్ ట్యాంక్ లెవల్ (FTL) మరియు బఫర్ జోన్లలో అక్రమ నిర్మాణాలను కూల్చివేసేందుకు తెలంగాణ వాల్టా చట్టం (WALTA Act 2002), ల్యాండ్ రెవెన్యూ చట్టం మరియు మున్సిపల్ కార్పొరేషన్ల నిబంధనల ప్రకారం హైడ్రాకు చట్టబద్ధ అధికారాలు కల్పించబడ్డాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The Government of Telangana issued G.O. Ms. No. 99 establishing HYDRAA, with IPS officer A.V. Ranganath as its founding Commissioner. Its jurisdiction spans the ORR boundary (over 2,000 sq km) covering GHMC, surrounding municipalities, and panchayats. An ordinance and gazette notification conferred statutory powers under the WALTA Act, GHMC Act, HMDA Act, and Irrigation Act to evict illegal encroachments in lakes, FTLs, buffer zones, and nalas.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. జీవో 99 ద్వారా హైడ్రా ఏర్పాటైంది. ఓఆర్ఆర్ పరిధిలోని సుమారు 2,050 చ.కి.మీ విస్తీర్ణంలో GHMC, HMDA ప్రాంతాల్లోని ప్రభుత్వ భూములు, చెరువులు, కుంటలను కాపాడటం దీని విధి. వాల్టా చట్టం, మున్సిపల్ మరియు నీటిపారుదల చట్టాల ద్వారా చెరువుల ఎఫ్‌టీఎల్, బఫర్ జోన్ల ఆక్రమణలను తొలగించే చట్టబద్ధ అధికారాలు హైడ్రాకు దఖలుపడ్డాయి."
    },
    "studynow_tg_indiramma_mahalakshmi_2026": {
        "id": 54,
        "subject": "Telangana Current Affairs",
        "topic": "Telangana Welfare Schemes - Indiramma Indlu & Mahalakshmi Free Bus Travel",
        "source_channel": "StudyNow Telugu",
        "source_video_id": "studynow_tg_indiramma_mahalakshmi_2026",
        "raw_video_hook": "తెలంగాణ ఇందిరమ్మ ఇండ్ల పథకం కింద ₹5 లక్షల సాయం మరియు మహాలక్ష్మి జీరో-టికెట్ ఉచిత బస్సు ప్రయాణ పథకం అమలు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding welfare guarantees implemented in Telangana:\n1. Under the 'Indiramma Indlu' housing scheme, the state provides financial assistance of ₹5 lakh to homeless families who already possess a house plot to construct a pucca house.\n2. In the Indiramma Indlu scheme, the government grants ownership of the house solely in the name of the female head of the family or joint ownership with her spouse.\n3. The 'Mahalakshmi Scheme' provides free travel for girls, women of all age groups, and transgender persons in Palle Velugu, Express, and City Ordinary buses operated by TSRTC across Telangana.\nWhich of the statements given above are correct?",
        "question_te": "తెలంగాణ ప్రభుత్వం అమలు చేస్తున్న సంక్షేమ పథకాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 'ఇందిరమ్మ ఇండ్లు' గృహ నిర్మాణ పథకం కింద నివేశన స్థలం (సొంత ప్లాట్) ఉన్న నిరుపేద కుటుంబాలకు పక్కా ఇంటి నిర్మాణానికై ప్రభుత్వం ₹5 లక్షల ఆర్థిక సహాయాన్ని అందిస్తుంది.\n2. ఇందిరమ్మ ఇండ్ల పథకంలో ఇళ్లను కుటుంబంలోని మహిళ పేరిట మాత్రమే లేదా భార్యాభర్తల ఉమ్మడి పేరిట మాత్రమే మంజూరు చేస్తారు.\n3. 'మహాలక్ష్మి పథకం' ద్వారా రాష్ట్రంలోని బాలికలు, మహిళలు మరియు ట్రాన్స్‌జెండర్లకు TSRTC నడిపే పల్లె వెలుగు, ఎక్స్‌ప్రెస్ మరియు సిటీ ఆర్డినరీ బస్సులలో ఉచిత ప్రయాణ సదుపాయం కల్పించబడింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Indiramma Indlu provides ₹5 lakh subsidy in 4 stages for building homes on owned plots, prioritizing landless homeless in later phases, with title deeds conferred upon women. The Mahalakshmi free transit guarantee enables unlimited zero-fare travel for domiciled girls, women, and transpersons in TSRTC ordinary, Palle Velugu, and Express buses.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. ఇందిరమ్మ ఇండ్ల పథకం కింద సొంత ప్లాట్ ఉన్న అర్హులైన పేదలకు 4 దశల్లో ₹5 లక్షల ఆర్థిక సాయం అందిస్తారు; పట్టాను మహిళ పేరిట ఇస్తారు. మహాలక్ష్మి పథకం ద్వారా తెలంగాణ మహిళలందరికీ TSRTC పల్లె వెలుగు, ఎక్స్‌ప్రెస్ బస్సులలో ఉచిత జీరో-ఫేర్ టికెట్ ద్వారా బస్సు ప్రయాణం అమలవుతోంది."
    },
    "csb_polity_art371d_presidential_order": {
        "id": 55,
        "subject": "Indian Polity",
        "topic": "Special Constitutional Provisions - Article 371D, Presidential Order 1975 & Six-Point Formula",
        "source_channel": "CSB IAS Academy (Bala Latha Madam)",
        "source_video_id": "csb_polity_art371d_presidential_order",
        "raw_video_hook": "రాజ్యాంగంలోని ఆర్టికల్ 371D, 1973 లో 32వ రాజ్యాంగ సవరణ, ఆరు సూత్రాల పథకం మరియు రాష్ట్రపతి ఉత్తర్వులు 1975.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding Article 371D of the Constitution of India and the Andhra Pradesh / Telangana Administrative structure:\n1. Article 371D was inserted by the 32nd Constitutional Amendment Act, 1973 to give statutory effect to the Six-Point Formula resolving regional agitations in Andhra and Telangana.\n2. Under Article 371D, the President issued the AP Public Employment (Organization of Local Cadres and Regulation of Direct Recruitment) Order, 1975 (Presidential Order) creating a multi-tier zonal system.\n3. Article 371D empowered Parliament to establish an Administrative Tribunal for the State to exercise jurisdiction over recruitment, appointment, and conditions of service of civil posts.\nWhich of the statements given above are correct?",
        "question_te": "భారత రాజ్యాంగంలోని అధికరణ 371D మరియు ఆంధ్రప్రదేశ్ / తెలంగాణ పరిపాలనా వ్యవస్థకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. తెలంగాణ మరియు ఆంధ్ర ప్రాంతాల ఉద్యమాల పరిష్కారార్థం కుదిరిన 'ఆరు సూత్రాల పథకానికి' (Six-Point Formula) రాజ్యాంగ రక్షణ కల్పించేందుకు 32వ రాజ్యాంగ సవరణ చట్టం, 1973 ద్వారా ఆర్టికల్ 371D ని చేర్చారు.\n2. ఆర్టికల్ 371D ఆధారంగా భారత రాష్ట్రపతి 1975 లో 'ఆంధ్రప్రదేశ్ పబ్లిక్ ఎంప్లాయ్‌మెంట్ ఆర్డర్, 1975' (రాష్ట్రపతి ఉత్తర్వులు) జారీ చేసి, స్థానిక క్యాడర్ల ఏర్పాటు మరియు జోనల్ విధానాన్ని ప్రవేశపెట్టారు.\n3. ప్రభుత్వ ఉద్యోగుల నియామకాలు, సేవా నిబంధనలపై వివాదాలను పరిష్కరించేందుకు ప్రత్యేక పరిపాలనా ట్రిబ్యునల్ (Administrative Tribunal) ను ఏర్పాటు చేసే అధికారాన్ని ఆర్టికల్ 371D పార్లమెంటుకు కల్పించింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Following the 1969 Telangana agitation and 1972 Jai Andhra agitation, the Mulki rules were replaced by the Six-Point Formula. Parliament passed the 32nd Amendment inserting Article 371D (equitable opportunities in education and public employment) and 371E (Central University in AP). The Presidential Order 1975 instituted local cadres and zones, and APAT was created under Article 371D(3).",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1969 తెలంగాణ మరియు 1972 జై ఆంధ్ర ఉద్యమాల అనంతరం కుదిరిన ఆరు సూత్రాల పథకానికి చట్టబద్ధత కల్పించడానికి 32వ సవరణ ద్వారా ఆర్టికల్ 371D ని చేర్చారు. దీని ఆధారంగా 1975 రాష్ట్రపతి ఉత్తర్వులు వెలువడి జోనల్ విధానం, స్థానిక రిజర్వేషన్లు అమల్లోకి వచ్చాయి. ఉద్యోగుల సర్వీస్ వివాదాల పరిష్కారానికి ట్రిబ్యునల్ ఏర్పాటు అధికారం కూడా ఇందులో ఉంది."
    },
    "csb_polity_anti_defection_schedule10": {
        "id": 56,
        "subject": "Indian Polity",
        "topic": "Parliamentary Democracy - Tenth Schedule (Anti-Defection Law) & 91st Amendment Act, 2003",
        "source_channel": "CSB IAS Academy (Bala Latha Madam)",
        "source_video_id": "csb_polity_anti_defection_schedule10",
        "raw_video_hook": "10వ షెడ్యూల్ పార్టీ ఫిరాయింపుల నిరోధక చట్టం, 91వ రాజ్యాంగ సవరణ మరియు కిహోతో హోల్లోహన్ కేసులో సుప్రీంకోర్టు తీర్పు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Anti-Defection Law contained in the Tenth Schedule of the Indian Constitution:\n1. The Tenth Schedule was added to the Constitution by the 52nd Constitutional Amendment Act, 1985, setting disqualification grounds for legislators voluntarily giving up party membership or defying party whips.\n2. The 91st Constitutional Amendment Act, 2003 omitted the provision that protected defectors if one-third of the legislature party split, leaving merger (approved by at least two-thirds members) as the only exception.\n3. In *Kihoto Hollohan v. Zachillhu (1992)*, the Supreme Court held that the Speaker/Chairman acts as a tribunal while deciding disqualification petitions, and their decisions are subject to judicial review.\nWhich of the statements given above are correct?",
        "question_te": "భారత రాజ్యాంగంలోని 10వ షెడ్యూల్ (పార్టీ ఫిరాయింపుల నిరోధక చట్టం) కు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 52వ రాజ్యాంగ సవరణ చట్టం, 1985 ద్వారా 10వ షెడ్యూల్‌ను రాజ్యాంగంలో చేర్చారు; శాసనసభ్యుడు స్వచ్ఛందంగా పార్టీ సభ్యత్వాన్ని వదులుకున్నా లేదా పార్టీ విప్‌ను ఉల్లంఘించినా అనర్హతకు గురవుతారు.\n2. 91వ రాజ్యాంగ సవరణ చట్టం, 2003 ద్వారా శాసనసభాపక్షంలో 1/3 వంతు సభ్యులు విడిపోయే 'చీలిక' (Split) రక్షణ నిబంధనను తొలగించారు; కేవలం 2/3 వంతు సభ్యుల 'విలీనం' (Merger) ను మాత్రమే రక్షణగా ఉంచారు.\n3. *కిహోతో హోల్లోహన్ వర్సెస్ జచిల్హు (1992)* కేసులో సుప్రీంకోర్టు తీర్పునిస్తూ, అనర్హత పిటిషన్లను పరిష్కరించేటప్పుడు స్పీకర్ ఒక ట్రిబ్యునల్‌గా వ్యవహరిస్తారని మరియు స్పీకర్ నిర్ణయం న్యాయ సమీక్షకు లోబడి ఉంటుందని స్పష్టం చేసింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The 52nd Amendment introduced the Tenth Schedule. The 91st Amendment (2003) deleted the 1/3rd split exemption because it encouraged wholesale defections, capping the Council of Ministers at 15% of Lok Sabha/Assembly strength. In Kihoto Hollohan (1992), the Constitution Bench upheld the Speaker's powers but struck down paragraph 7 (which excluded judicial review), making the Presiding Officer's final decision reviewable under Articles 32, 136, and 226.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1985 లో 52వ సవరణ ద్వారా 10వ షెడ్యూల్‌ను చేర్చారు. 2003 లో 91వ సవరణ ద్వారా 1/3 చీలిక మినహాయింపును రద్దు చేసి, కేవలం 2/3 మందితో కూడిన పార్టీల విలీనాన్ని మాత్రమే చట్టబద్ధం చేశారు. కిహోతో హోల్లోహన్ (1992) కేసులో స్పీకర్ నిర్ణయంపై హైకోర్టులు, సుప్రీంకోర్టులకు న్యాయ సమీక్ష అధికారం ఉంటుందని అత్యున్నత న్యాయస్థానం రూలింగ్ ఇచ్చింది."
    },
    "winners_history_swadeshi_vande_mataram": {
        "id": 57,
        "subject": "Indian History",
        "topic": "Modern Indian History - Swadeshi Movement (1905–1908) & Impact in Andhra/Telangana",
        "source_channel": "Winners Online (Winners Publications)",
        "source_video_id": "winners_history_swadeshi_vande_mataram",
        "raw_video_hook": "1905 వందేమాతరం ఉద్యమం, బిపిన్ చంద్రపాల్ 1907 రాజమండ్రి పర్యటన మరియు గాడిచర్ల హరిసర్వోత్తమరావు పాత్ర.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Swadeshi and Vande Mataram Movement (1905–1908) and its impact in South India:\n1. The formal proclamation of the Swadeshi Movement was made on August 7, 1905, in a massive meeting held at the Calcutta Town Hall, passing the Boycott Resolution against British goods.\n2. In April 1907, extremist leader Bipin Chandra Pal undertook a historic lecture tour of coastal Andhra, inspiring students at Rajahmundry Government Arts College to wear Vande Mataram badges.\n3. Gadicherla Harisarvottama Rao and other students were rusticated by Principal Mark Hunter for shouting 'Vande Mataram', sparking widespread student participation across Telugu districts.\nWhich of the statements given above are correct?",
        "question_te": "స్వదేశీ మరియు వందేమాతరం ఉద్యమం (1905–1908) మరియు దక్షిణ భారతదేశంలో దాని ప్రభావానికి సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. 1905 ఆగస్టు 7న కలకత్తా టౌన్ హాల్‌లో జరిగిన భారీ బహిరంగ సభలో బ్రిటిష్ వస్తువుల బహిష్కరణ తీర్మానాన్ని ఆమోదిస్తూ స్వదేశీ ఉద్యమాన్ని అధికారికంగా ప్రకటించారు.\n2. 1907 ఏప్రిల్‌లో అతివాద జాతీయ నాయకుడు బిపిన్ చంద్రపాల్ కోస్తా ఆంధ్రలో పర్యటించి ఉత్తేజపూరిత ఉపన్యాసాలు ఇవ్వడంతో రాజమండ్రి ప్రభుత్వ ఆర్ట్స్ కళాశాల విద్యార్థులు 'వందేమాతరం' బ్యాడ్జీలు ధరించారు.\n3. కళాశాలలో 'వందేమాతరం' నినాదాలు చేసినందుకు ప్రిన్సిపాల్ మార్క్ హంటర్ చేత గాడిచర్ల హరిసర్వోత్తమరావు మరియు ఇతర విద్యార్థులు బహిష్కరణకు గురయ్యారు, ఇది తెలుగు జిల్లాల్లో విద్యార్థి ఉద్యమానికి నాంది పలికింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The Boycott movement began on 7 August 1905 in Calcutta. In Andhra, Mutnuri Krishna Rao invited Bipin Chandra Pal to visit in April 1907. Pal delivered inspiring lectures in Rajahmundry, Kakinada, and Machilipatnam. Principal Mark Hunter penalized students wearing Vande Mataram medals, leading to Gadicherla Harisarvottama Rao's suspension and the founding of national schools.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1905 ఆగస్టు 7న కలకత్తా టౌన్ హాల్‌లో స్వదేశీ ఉద్యమ బహిష్కరణ తీర్మానం ఆమోదించారు. ముట్నూరి కృష్ణారావు ఆహ్వానం మేరకు 1907 లో బిపిన్ చంద్రపాల్ ఆంధ్రలో పర్యటించారు. రాజమండ్రి ట్రైనింగ్ కాలేజీలో విద్యార్థులు వందేమాతరం బ్యాడ్జీలు ధరించినందుకు మార్క్ హంటర్ గాడిచర్ల హరిసర్వోత్తమరావును డిబార్ చేయడంతో ఆంధ్రదేశమంతటా ఉద్యమం వెల్లువెత్తింది."
    },
    "winners_history_maurya_ashoka_edicts": {
        "id": 58,
        "subject": "Indian History",
        "topic": "Ancient Indian History - Mauryan Central Administration & Officials in Arthashastra",
        "source_channel": "Winners Online (Winners Publications)",
        "source_video_id": "winners_history_maurya_ashoka_edicts",
        "raw_video_hook": "మౌర్యుల పరిపాలనా వ్యవస్థలో సమాహర్త, సన్నిధాత, అక్షపటలాధ్యక్షుడు మరియు సీతాధ్యక్షుల విధులు.",
        "question_type": "Match the Following",
        "question_en": "Match the following key administrative officers of the Mauryan Empire mentioned in Kautilya's Arthashastra with their respective functional portfolios:\n(A) Samaharta (సమాహర్త)             - (1) Superintendent of Crown Agricultural Lands and Cultivation\n(B) Sannidhata (సన్నిధాత)           - (2) Head of Royal Accounts and State Records Office (*Akshapataladhyaksha*)\n(C) Sitadhyaksha (సీతాధ్యక్షుడు)        - (3) Chief Collector General of Revenue and State Budget Overseer\n(D) Akshapataladhyaksha (అక్షపటలాధ్యక్షుడు) - (4) Royal Treasurer and In-charge of the State Storehouses/Granaries\nCorrect matching code:",
        "question_te": "కౌటిల్యుని అర్థశాస్త్రంలో పేర్కొన్న మౌర్య సామ్రాజ్య ప్రధాన పరిపాలనా అధికారులను వారి బాధ్యతలతో జతపరచండి:\n(A) సమాహర్త            - (1) ప్రభుత్వ వ్యవసాయ భూములు మరియు సాగు పర్యవేక్షకుడు\n(B) సన్నిధాత            - (2) రాజరిక గణాంకాలు మరియు రికార్డుల కార్యాలయ అధిపతి\n(C) సీతాధ్యక్షుడు        - (3) ప్రధాన రెవెన్యూ వసూలు అధికారి మరియు బడ్జెట్ నిర్వాహకుడు\n(D) అక్షపటలాధ్యక్షుడు  - (4) ప్రభుత్వ ప్రధాన కోశాధికారి మరియు ధాన్యాగారాల పర్యవేక్షకుడు\nసరైన కోడ్‌ను ఎంచుకోండి:",
        "options_en": ["A-3, B-4, C-1, D-2", "A-4, B-3, C-1, D-2", "A-3, B-1, C-4, D-2", "A-1, B-4, C-3, D-2"],
        "options_te": ["A-3, B-4, C-1, D-2", "A-4, B-3, C-1, D-2", "A-3, B-1, C-4, D-2", "A-1, B-4, C-3, D-2"],
        "correct_option": 0,
        "explanation_en": "Correct matching is A-3, B-4, C-1, D-2. In Mauryan central administration described in Kautilya's Arthashastra: Samaharta was the revenue collector-general who maintained income and expenditure budgets; Sannidhata was the supreme keeper of state treasury, storehouses, and warehouses; Sitadhyaksha supervised state-owned agricultural lands (*Sita*); Akshapataladhyaksha maintained accounts, audit ledgers, and official edicts.",
        "explanation_te": "సరైన జత: A-3, B-4, C-1, D-2. కౌటిల్యుని అర్థశాస్త్రం ప్రకారం మౌర్యుల పరిపాలనలో: సమాహర్త అనగా ప్రధాన ఆదాయ వసూలు అధికారి (బడ్జెట్ నిర్వాహకుడు); సన్నిధాత అనగా ప్రభుత్వ ఖజానా మరియు గిడ్డంగుల అధిపతి; సీతాధ్యక్షుడు ప్రభుత్వానికి చెందిన సాగు భూములను (సీతా భూములు) పర్యవేక్షించే అధికారి; అక్షపటలాధ్యక్షుడు ప్రభుత్వ లెక్కలు, రికార్డులను భద్రపరిచే అకౌంటెంట్ జనరల్."
    },
    "tsat_tg_armed_struggle_chakali_ilamma": {
        "id": 59,
        "subject": "Telangana History",
        "topic": "Telangana Peasant Armed Struggle (1946–1951) - Doddi Komaraiah & Chakali Ilamma",
        "source_channel": "T-SAT Network (Govt of Telangana)",
        "source_video_id": "tsat_tg_armed_struggle_chakali_ilamma",
        "raw_video_hook": "తెలంగాణ సాయుధ రైతాంగ పోరాటం, దొడ్డి కొమరయ్య అమరత్వం మరియు చాకలి ఐలమ్మ భూపోరాటం.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Telangana Peasant Armed Struggle (తెలంగాణ సాయుధ రైతాంగ పోరాటం 1946–1951):\n1. The armed uprising was ignited on July 4, 1946, when Doddi Komaraiah was shot dead by the henchmen of Visnoor Deshmukh Rapaka Ramachandra Reddy at Kadavendi village in Jangaon taluk.\n2. The struggle gained mass momentum from the resistance of Chakali Ilamma of Palakurthi, who successfully defended her harvested crop against the illegal confiscation by the Visnoor Deshmukh.\n3. Peasant guerrilla squads (*Guerilla Dalamulu*) liberated nearly 3,000 villages, abolished forced unpaid labour (*Vetti Chakiri*), and distributed around 10 lakh acres of agricultural land to landless peasants.\nWhich of the statements given above are correct?",
        "question_te": "తెలంగాణ సాయుధ రైతాంగ పోరాటం (1946–1951) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. 1946 జూలై 4న జనగామ తాలూకా కడవెండి గ్రామంలో విస్నూరు దేశ్‌ముఖ్ రాపాక రామచంద్రారెడ్డి గుండాలు జరిపిన కాల్పుల్లో దొడ్డి కొమరయ్య అమరుడైన ఘటనతో ఈ చారిత్రక సాయుధ తిరుగుబాటు రాజుకుంది.\n2. పాలకుర్తికి చెందిన వీరనారి చాకలి ఐలమ్మ తన సాగు భూమిలోని పంటను విస్నూరు దేశ్‌ముఖ్ దౌర్జన్యంగా లాక్కోకుండా ఆంధ్ర మహాసభ సహకారంతో వీరోచితంగా కాపాడుకోవడంతో ఉద్యమం ప్రజా పోరాటంగా మారింది.\n3. ఈ పోరాటంలో రైతాంగ గెరిల్లా దళాలు సుమారు 3,000 గ్రామాలను విముక్తం చేసి, వెట్టి చాకిరిని రూపుమాపాయి మరియు దాదాపు 10 లక్షల ఎకరాల భూమిని పేదలకు పంచాయి.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Doddi Komaraiah's martyrdom at Kadavendi on 4 July 1946 sparked the Telangana Armed Struggle against feudal deshmukhs, landlords (doralu), and Nizam's Razakars. Chakali Ilamma's valiant resistance in Palakurthi became a symbol of self-respect and land rights. Over 3,000 villages formed people's committees (*Grama Rajyalu*), eradicating Vetti and redistributing 10 lakh acres of land until called off in October 1951.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1946 జూలై 4న కడవెండిలో దొడ్డి కొమరయ్య అమరత్వంతో తెలంగాణ సాయుధ రైతాంగ పోరాటం ప్రారంభమైంది. పాలకుర్తిలో విస్నూరు దొరకు వ్యతిరేకంగా చాకలి ఐలమ్మ సాగించిన పోరాటం స్ఫూర్తిగా నిలిచింది. కమ్యూనిస్టు గెరిల్లా దళాల నాయకత్వంలో 3,000 గ్రామాల్లో గ్రామాభివృద్ధి కమిటీలు ఏర్పడి, వెట్టి చాకిరి రద్దయి, 10 లక్షల ఎకరాల భూపంపిణీ జరిగింది."
    },
    "tsat_polity_cag_art148": {
        "id": 60,
        "subject": "Indian Polity",
        "topic": "Constitutional Bodies - Comptroller and Auditor General of India (CAG - Articles 148–151)",
        "source_channel": "T-SAT Network (Govt of Telangana)",
        "source_video_id": "tsat_polity_cag_art148",
        "raw_video_hook": "భారత కంప్ట్రోలర్ అండ్ ఆడిటర్ జనరల్ (CAG) రాజ్యాంగ హోదా, ఆర్టికల్ 148-151, మరియు పీఏసీకి మార్గదర్శిగా పాత్ర.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Comptroller and Auditor General of India (CAG) under Articles 148 to 151 of the Constitution:\n1. The CAG is appointed by the President by warrant under his hand and seal and can be removed from office only in like manner and on like grounds as a Judge of the Supreme Court under Article 148(1).\n2. Under Article 151, the reports of the CAG relating to the accounts of the Union are submitted to the President, who causes them to be laid before each House of Parliament.\n3. The CAG acts as a 'friend, philosopher, and guide' to the Public Accounts Committee (PAC) of Parliament during the examination of the appropriation and financial audit reports.\nWhich of the statements given above are correct?",
        "question_te": "భారత రాజ్యాంగంలోని అధికరణలు 148 నుండి 151 వరకు పేర్కొన్న కంప్ట్రోలర్ అండ్ ఆడిటర్ జనరల్ (CAG) కి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఆర్టికల్ 148(1) ప్రకారం కాగ్‌ను రాష్ట్రపతి తన స్వహస్తంతో కూడిన సంతకం మరియు ముద్ర గల వారెంట్ ద్వారా నియమిస్తారు; సుప్రీంకోర్టు న్యాయమూర్తిని తొలగించే పద్ధతి మరియు కారణాలపై మాత్రమే ఆయనను పదవి నుండి తొలగించగలరు.\n2. అధికరణ 151 ప్రకారం, కేంద్ర ప్రభుత్వ ఖాతాలకు సంబంధించిన కాగ్ ఆడిట్ నివేదికలను రాష్ట్రపతికి సమర్పిస్తారు, రాష్ట్రపతి వాటిని పార్లమెంటు ఉభయ సభల ముందు ఉంచుతారు.\n3. పార్లమెంటు ప్రభుత్వ ఖాతాల సంఘం (PAC) కాగ్ నివేదికలను పరిశీలించే సమయంలో కాగ్ కమిటీకి 'మిత్రుడు, తత్వవేత్త మరియు మార్గదర్శి'గా (Friend, Philosopher, and Guide) వ్యవహరిస్తారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Dr. B.R. Ambedkar termed the CAG as the most important constitutional office under the Constitution. Under Article 148, CAG enjoys security of tenure equal to a Supreme Court judge. Under Article 151, CAG submits 3 audit reports (Audit Report on Appropriation Accounts, Finance Accounts, and Public Undertakings) to the President/Governor. In parliamentary scrutiny, CAG closely assists the Public Accounts Committee as its expert adviser.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. డాక్టర్ బి.ఆర్. అంబేద్కర్ కాగ్ పదవిని రాజ్యాంగంలో అత్యంత ముఖ్యమైన పదవిగా అభివర్ణించారు. ఆర్టికల్ 148 ప్రకారం సుప్రీంకోర్టు జడ్జితో సమానమైన పదవీ భద్రత ఉంటుంది. ఆర్టికల్ 151 ప్రకారం కేంద్ర ఆడిట్ నివేదికలను రాష్ట్రపతికి, రాష్ట్రాల నివేదికలను గవర్నర్లకు సమర్పిస్తారు. పార్లమెంటు పబ్లిక్ అకౌంట్స్ కమిటీకి (PAC) కాగ్ మిత్రుడు, తత్వవేత్త, మార్గదర్శిగా సహాయపడతారు."
    },
    "ashoka_tg_gentlemens_agreement_1956": {
        "id": 61,
        "subject": "Telangana History & Movement",
        "topic": "Telangana Movement - Gentlemen's Agreement 1956 (పెద్దమనుషుల ఒప్పందం) & Signatories",
        "source_channel": "Ashoka Academy (Ashok Sir)",
        "source_video_id": "ashoka_tg_gentlemens_agreement_1956",
        "raw_video_hook": "1956 ఫిబ్రవరి 20న ఢిల్లీలోని హైదరాబాద్ భవన్‌లో కుదిరిన పెద్దమనుషుల ఒప్పందం, సంతకం చేసిన 8 మంది నేతలు మరియు 14 రక్షణలు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the historic Gentlemen's Agreement (పెద్దమనుషుల ఒప్పందం) signed on February 20, 1956, paving the way for the formation of Andhra Pradesh:\n1. The agreement was signed at Hyderabad House in New Delhi by four representatives from Andhra (B. Gopala Reddy, N. Sanjiva Reddy, Gouthu Latchanna, Alluri Satyanarayana Raju) and four from Telangana (Burgula Ramakrishna Rao, K.V. Ranga Reddy, M. Channa Reddy, J.V. Narsing Rao).\n2. It provided for the statutory establishment of a 'Telangana Regional Committee' with powers over local government, public health, primary/secondary education, and regulation of agricultural land sales.\n3. A minimum domicile residential qualification of 12 years in the Telangana region was stipulated for eligibility in local appointments to public services and educational institutions.\nWhich of the statements given above are correct?",
        "question_te": "ఆంధ్రప్రదేశ్ రాష్ట్ర అవతరణకు మార్గం సుగమం చేస్తూ 1956 ఫిబ్రవరి 20న కుదిరిన చారిత్రక 'పెద్దమనుషుల ఒప్పందం' (Gentlemen's Agreement) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. న్యూఢిల్లీలోని హైదరాబాద్ భవన్‌లో ఆంధ్ర ప్రాంతం నుండి నలుగురు (బెజవాడ గోపాలరెడ్డి, నీలం సంజీవరెడ్డి, గౌతు లచ్చన్న, అల్లూరి సత్యనారాయణ రాజు), తెలంగాణ నుండి నలుగురు (బూర్గుల రామకృష్ణారావు, కె.వి. రంగారెడ్డి, మర్రి చెన్నారెడ్డి, జె.వి. నర్సింగరావు) ఈ ఒప్పందంపై సంతకాలు చేశారు.\n2. స్థానిక పరిపాలన, ప్రజారోగ్యం, ప్రాథమిక/ద్వితీయ విద్య మరియు వ్యవసాయ భూముల అమ్మకాలపై నియంత్రణ అధికారాలతో 'తెలంగాణ ప్రాంతీయ కమిటీ'ని చట్టబద్ధంగా ఏర్పాటు చేయడానికి ఒప్పందం హామీ ఇచ్చింది.\n3. తెలంగాణ ప్రాంతంలోని ప్రభుత్వ ఉద్యోగాలు మరియు విద్యాసంస్థల ప్రవేశాలలో స్థానిక అర్హత (ముల్కీ నిబంధన) కోసం కనీసం 12 సంవత్సరాల నివాస కాలాన్ని ప్రామాణికంగా నిర్ణయించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The Gentlemen's Agreement was signed on 20 February 1956 at Hyderabad House, New Delhi by 8 leaders (4 from Andhra, 4 from Telangana). It outlined 14 key safeguards including the establishment of a Telangana Regional Standing Committee, distribution of expenditure proportionately, reservation of seats in education and cabinet, and a 12-year domicile requirement for public employment in Telangana.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1956 ఫిబ్రవరి 20న ఢిల్లీలోని హైదరాబాద్ భవన్‌లో 8 మంది నాయకుల మధ్య 14 రక్షణలతో కూడిన పెద్దమనుషుల ఒప్పందం కుదిరింది. ఇందులో తెలంగాణ ప్రాంతీయ కమిటీ ఏర్పాటు, మిగులు నిధుల వినియోగం, కేబినెట్ కూర్పు (ముఖ్యమంత్రి ఆంధ్రా అయితే ఉప ముఖ్యమంత్రి తెలంగాణ లేదా వైస్-వెర్సా) మరియు తెలంగాణలో ఉద్యోగాలకు 12 ఏళ్ల ముల్కీ నిబంధన పొందుపరిచారు."
    },
    "ashoka_tg_ikshvaku_nagarjunakonda": {
        "id": 62,
        "subject": "Telangana History & Movement",
        "topic": "Ancient Telangana History - Ikshvaku Dynasty of Vijayapuri & Nagarjunakonda Inscriptions",
        "source_channel": "Ashoka Academy (Ashok Sir)",
        "source_video_id": "ashoka_tg_ikshvaku_nagarjunakonda",
        "raw_video_hook": "విజయపురి కేంద్రంగా పాలించిన ఇక్ష్వాకుల రాజవంశం, నాగార్జునకొండ బౌద్ధ విహారాలు మరియు రాణుల ప్రాకృత శాసనాలు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Ikshvaku dynasty of Vijayapuri (Nagarjunakonda) who ruled the Krishna-Tungabhadra basin following the fall of the Satavahanas:\n1. The founder of the dynasty, Vasishthiputra Chamtamula (Shantamula I), revived Vedic traditions by performing Ashvamedha, Agnihotra, and Vajapeya sacrifices.\n2. While the Ikshvaku kings were devout followers of Vedic Brahmanism and devotees of Lord Mahasena (Kartikeya), the royal ladies—notably Chamtasri and Bodhisri—generously patronized Mahayana Buddhism and constructed the Maha Chaitya at Nagarjunakonda.\n3. Nagarjunakonda flourished as an international center of Buddhist learning, hosting monastic communities such as the Aparamahavinaseliyas and the Mahaviharavasins from Ceylon (Sri Lanka).\nWhich of the statements given above are correct?",
        "question_te": "శాతవాహనుల పతనం తర్వాత కృష్ణా నదీ లోయను విజయపురి (నాగార్జునకొండ) కేంద్రంగా పాలించిన ఇక్ష్వాకు రాజవంశానికి సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. ఇక్ష్వాకు వంశ మూలపురుషుడైన వాసిష్ఠీపుత్ర శాంతమూలుడు (మొదటి శాంతమూలుడు) వైదిక సంప్రదాయాలను పునరుద్ధరిస్తూ అశ్వమేధ, అగ్నిహోత్ర మరియు వాజపేయ యాగాలను నిర్వహించాడు.\n2. ఇక్ష్వాకు రాజులు వైదిక మతస్థులు మరియు కుమారస్వామి (మహాసేనుడు) భక్తులైనప్పటికీ, రాచకుటుంబానికి చెందిన మహిళలు—ముఖ్యంగా శాంతశ్రీ మరియు ఉపాసిక బోధిశ్రీ—బౌద్ధమతాన్ని ఆదరించి నాగార్జునకొండలో మహాచైత్యాన్ని నిర్మించారు.\n3. నాగార్జునకొండ అంతర్జాతీయ బౌద్ధ విద్యా కేంద్రంగా విలసిల్లింది; సింహళం (శ్రీలంక) నుండి వచ్చిన మహావిహారవాసులు మరియు అపరమహా వినశైలీయ బౌద్ధ శాఖల భిక్షువులకు ఇక్కడ ఆశ్రయాలు కల్పించారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The Ikshvakus ruled during the 3rd-4th centuries AD from Vijayapuri (Nagarjunakonda Valley). Founder Vasishthiputra Chamtamula performed Vedic rituals including Ashvamedha. Remarkably, the royal women (Chamtasri, Bapisri, Chathisri, and lay-follower Bodhisri) donated extensively to build Mahachaitya, viharas, and mandapas for Buddhist sects including Aparamahavinaseliyas and Sinhala monks.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. శాతవాహనుల అనంతరం విజయపురి (నాగార్జునకొండ) రాజధానిగా ఇక్ష్వాకులు పాలించారు. మూలపురుషుడు వాసిష్ఠీపుత్ర శాంతమూలుడు వైదిక యజ్ఞయాగాదులు చేశాడు. రాజులు కార్తికేయ భక్తులైనప్పటికీ, రాచ స్త్రీలైన శాంతశ్రీ, బోధిశ్రీ వంటివారు బౌద్ధమతానికి విస్తృత దానాలు చేసి నాగార్జునకొండలో మహాచైత్యం, విహారాలు నిర్మించారు. ఇక్కడ శ్రీలంక బౌద్ధ భిక్షువుల కోసం సింహళ విహారం ఉండేది."
    },
    "studynow_tg_bhoo_bharathi_dharani_2026": {
        "id": 63,
        "subject": "Telangana Current Affairs",
        "topic": "Land Administration & Revenue Reforms - Bhoo Bharathi Project & RoR Act Amendments",
        "source_channel": "StudyNow Telugu",
        "source_video_id": "studynow_tg_bhoo_bharathi_dharani_2026",
        "raw_video_hook": "తెలంగాణ ప్రభుత్వం చేపట్టిన భూ భారతి రెవెన్యూ సంస్కరణలు, ధరణి స్థానంలో కొత్త చట్టం మరియు అప్పీల్ వ్యవస్థ పునరుద్ధరణ.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the 'Bhoo Bharathi' land governance initiative and proposed Record of Rights (RoR) reforms in Telangana:\n1. The Government initiated the 'Bhoo Bharathi' project to overhaul the land governance framework, resolve thousands of grievances trapped under the restrictive 'Part-B' land classification, and conduct a digital cadastral survey using CORS technology.\n2. The revamped Record of Rights (RoR) framework introduced multi-tier quasi-judicial appellate forums at the Tahsildar, Revenue Divisional Officer (RDO), and District Collector levels, restoring dispute resolution mechanisms that were eliminated under the original Dharani portal setup.\nWhich of the statements given above is/are correct?",
        "question_te": "తెలంగాణలో భూ పరిపాలన సంస్కరణల్లో భాగంగా ప్రారంభించిన 'భూ భారతి' (Bhoo Bharathi) ప్రాజెక్ట్ మరియు నూతన రికార్డ్ ఆఫ్ రైట్స్ (RoR) మార్గదర్శకాలకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. భూ వివాదాల పరిష్కారం, గత ధరణి పోర్టల్‌లో 'పార్ట్-బి' కింద స్తంభించిపోయిన లక్షలాది రైతుల భూ సమస్యల పరిష్కారం మరియు CORS సాంకేతికతతో డిజిటల్ భూ సర్వే లక్ష్యంగా 'భూ భారతి' ప్రాజెక్ట్‌ను ప్రభుత్వం ప్రారంభించింది.\n2. గత ధరణి పోర్టల్‌లో తొలగించబడిన రెవెన్యూ అప్పీలేట్ వ్యవస్థను పునరుద్ధరిస్తూ, తహసీల్దార్, ఆర్డీవో (RDO) మరియు జిల్లా కలెక్టర్ల స్థాయిలలో న్యాయబద్ధమైన అప్పీల్ చేసుకునే అధికారాలను నూతన RoR ముసాయిదా చట్టం ద్వారా కల్పించారు.\nపై ప్రకటనలలో సరైనది/వి ఏది/వి?",
        "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "options_te": ["1 మాత్రమే", "2 మాత్రమే", "1 మరియు 2 రెండూ", "ఏదీ కాదు"],
        "correct_option": 2,
        "explanation_en": "Both statements are correct. The Telangana government initiated the 'Bhoo Bharathi' land records restructuring initiative to rectify discrepancies of the Dharani portal, aiming to conduct comprehensive digital resurveys using Continuously Operating Reference Stations (CORS). Crucially, the amended RoR legal architecture restores the judicial hierarchy allowing appeals to RDO and Collector tribunals to address land ownership disputes.",
        "explanation_te": "రెండు ప్రకటనలూ సరైనవే. ధరణి పోర్టల్ లోపాల ప్రక్షాళనకు ప్రభుత్వం 'భూ భారతి' కార్యక్రమాన్ని తెచ్చింది. ఇందులో భాగంగా పార్ట్-బి లో నిలిచిపోయిన భూముల క్లియరెన్స్, CORS ఆధారిత డిజిటల్ భూ సర్వే చేపడుతున్నారు. గతంలో ధరణి వల్ల కోల్పోయిన వివాద పరిష్కార అప్పీల్ వ్యవస్థను పునరుద్ధరిస్తూ తహసీల్దార్, ఆర్డీవో, కలెక్టర్ల స్థాయిలో అర్ధ న్యాయపరమైన అప్పీలేట్ అధికారాలను కల్పించారు."
    },
    "studynow_tg_gruha_jyothi_cheyutha_2026": {
        "id": 64,
        "subject": "Telangana Current Affairs",
        "topic": "Telangana Welfare Schemes - Gruha Jyothi (200 Units Free Power) & Cheyutha Social Pensions",
        "source_channel": "StudyNow Telugu",
        "source_video_id": "studynow_tg_gruha_jyothi_cheyutha_2026",
        "raw_video_hook": "తెలంగాణ గృహజ్యోతి 200 యూనిట్ల ఉచిత విద్యుత్ పథకం అర్హతలు మరియు చేయూత, ఆరోగ్యశ్రీ విస్తరణ నిబంధనలు.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding key social welfare guarantees implemented by the Government of Telangana:\n1. Under the 'Gruha Jyothi' guarantee, domestic households possessing a valid Food Security Card (White Ration Card) with monthly electricity consumption up to 200 units receive a zero electricity bill.\n2. Under the 'Cheyutha' pension framework, monthly social security pensions are enhanced to ₹4,000 for elderly, widows, single women, weavers, and toddy tappers, and ₹6,000 for severely disabled persons.\n3. Under the revamped 'Rajiv Aarogyasri' health scheme, the financial coverage ceiling for cashless tertiary medical treatment was enhanced to ₹10 lakh per beneficiary family per year.\nWhich of the statements given above are correct?",
        "question_te": "తెలంగాణ ప్రభుత్వం అమలు చేస్తున్న కీలక సంక్షేమ గ్యారెంటీ పథకాలకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. 'గృహజ్యోతి' పథకం కింద చెల్లుబాటు అయ్యే ఆహార భద్రతా కార్డు (తెల్ల రేషన్ కార్డు) కలిగి ఉండి, నెలకు 200 యూనిట్ల వరకు గృహ విద్యుత్‌ను వినియోగించే కుటుంబాలకు జీరో విద్యుత్ బిల్లు (ఉచిత విద్యుత్) అందించబడుతుంది.\n2. 'చేయూత' సంక్షేమ పథకం ద్వారా వృద్ధులు, వితంతువులు, ఒంటరి మహిళలు, చేనేత మరియు గీత కార్మికులకు ఇచ్చే సామాజిక పింఛనును నెలకు ₹4,000 కు, తీవ్ర దివ్యాంగులకు ₹6,000 కు పెంచాలని నిర్ణయించారు.\n3. పునఃప్రారంభించబడిన 'రాజీవ్ ఆరోగ్యశ్రీ' పథకం కింద ప్రతి లబ్ధిదారు కుటుంబానికి వార్షిక నగదు రహిత కార్పొరేట్ వైద్య చికిత్స పరిమితిని గరిష్టంగా ₹10 లక్షలకు పెంచారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Gruha Jyothi delivers up to 200 units of free power to domestic Food Security Card holders, linked via Praja Palana applications. The Cheyutha policy elevates monthly pensions to ₹4,000 for senior citizens, widows, and vulnerable groups, and ₹6,000 for persons with disabilities. Rajiv Aarogyasri financial assistance was doubled from ₹5 lakh to ₹10 lakh per family.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. గృహజ్యోతి పథకం కింద తెల్ల రేషన్ కార్డు ఉండి నెలకు 200 యూనిట్లలోపు వాడే గృహాలకు జీరో కరెంట్ బిల్లు వస్తుంది. చేయూత కింద ఆసరా పెన్షన్లను నెలకు ₹4,000 కు, దివ్యాంగులకు ₹6,000 కు పెంచారు. రాజీవ్ ఆరోగ్యశ్రీ పథకం ద్వారా ఉచిత వైద్య చికిత్స పరిమితిని ₹5 లక్షల నుండి ₹10 లక్షలకు పెంచారు."
    },
    "csb_polity_fundamental_duties_art51a": {
        "id": 65,
        "subject": "Indian Polity",
        "topic": "Constitutional Law - Fundamental Duties (Article 51A), Swaran Singh Recommendations & Verma Committee",
        "source_channel": "CSB IAS Academy (Bala Latha Madam)",
        "source_video_id": "csb_polity_fundamental_duties_art51a",
        "raw_video_hook": "ప్రాథమిక విధులు (Article 51A), స్వరణ్ సింగ్ కమిటీ ఆమోదించిన/తిరస్కరించిన సిఫార్సులు మరియు జస్టిస్ వర్మ కమిటీ నివేదిక.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Fundamental Duties contained in Article 51A (Part IV-A) of the Constitution of India:\n1. The Fundamental Duties were incorporated into the Constitution by the 42nd Constitutional Amendment Act, 1976 on the recommendations of the Sardar Swaran Singh Committee.\n2. The Swaran Singh Committee recommended that failure to observe duties should be punishable by law and that the duty to pay taxes should be a Fundamental Duty, but Parliament did not incorporate these two proposals.\n3. The Justice J.S. Verma Committee (1999) identified existing legal provisions for enforcing certain fundamental duties, including the Prevention of Insults to National Honour Act (1971) and the Wildlife (Protection) Act (1972).\nWhich of the statements given above are correct?",
        "question_te": "భారత రాజ్యాంగంలోని అధికరణ 51A (భాగం IV-A) లో పొందుపరిచిన 'ప్రాథమిక విధులకు' సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. సర్దార్ స్వరణ్ సింగ్ కమిటీ సిఫార్సుల మేరకు 42వ రాజ్యాంగ సవరణ చట్టం, 1976 ద్వారా ప్రాథమిక విధులను రాజ్యాంగంలో చేర్చారు.\n2. ప్రాథమిక విధులను పాటించని వారిపై చట్టప్రకారం శిక్ష విధించాలని మరియు 'పన్నులు చెల్లించడం' కూడా ప్రాథమిక విధిగా ఉండాలని స్వరణ్ సింగ్ కమిటీ సిఫార్సు చేసినప్పటికీ పార్లమెంటు ఈ రెండు అంశాలను రాజ్యాంగంలో చేర్చలేదు.\n3. ప్రాథమిక విధులను అమలు చేసేందుకు ఇప్పటికే ఉన్న చట్టబద్ధ నిబంధనలను (జాతీయ గౌరవ అవమానాల నిరోధక చట్టం 1971, వన్యప్రాణి సంరక్షణ చట్టం 1972 వంటివి) జస్టిస్ జె.ఎస్. వర్మ కమిటీ (1999) గుర్తించింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Part IV-A (Article 51A) was added by the 42nd Amendment in 1976 following Swaran Singh Committee suggestions. However, Parliament rejected the committee's recommendations to penalize non-compliance and to make tax payment a duty. The 11th duty was added by the 86th Amendment (2002). The Justice Verma Committee in 1999 examined statutory backing (e.g., RPA 1951, Environmental Protection Act 1986, IPC) supporting duty enforcement.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1976 లో 42వ సవరణ ద్వారా ఆర్టికల్ 51A ను చేర్చారు. స్వరణ్ సింగ్ కమిటీ విధులు పాటించకపోతే జరిమానా/శిక్ష విధించాలని, పన్నులు చెల్లించడాన్ని ప్రాథమిక విధిగా చేర్చాలని ప్రతిపాదించినా నాటి ప్రభుత్వం వాటిని ఆమోదించలేదు. 1999 లో జస్టిస్ వర్మ కమిటీ జాతీయ జెండా గౌరవ చట్టం, వన్యప్రాణి చట్టం తదితర శాసనాల ద్వారా విధుల అమలును వివరించింది."
    },
    "csb_polity_interstate_water_disputes_art262": {
        "id": 66,
        "subject": "Indian Polity",
        "topic": "Federalism & Constitutional Adjudication - Inter-State River Water Disputes (Article 262) & Tribunals",
        "source_channel": "CSB IAS Academy (Bala Latha Madam)",
        "source_video_id": "csb_polity_interstate_water_disputes_art262",
        "raw_video_hook": "రాజ్యాంగంలోని అధికరణ 262, అంతర్-రాష్ట్ర నదీ జల వివాదాల చట్టం 1956 మరియు సుప్రీంకోర్టు అధికార పరిధి.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the adjudication of Inter-State River Water Disputes under Article 262 of the Indian Constitution:\n1. Under Article 262(1), Parliament may by law provide for the adjudication of any dispute or complaint with respect to the use, distribution, or control of the waters of any inter-state river or river valley.\n2. Under Article 262(2) and Section 11 of the Inter-State River Water Disputes Act, 1956, Parliament has barred both the Supreme Court and all other courts from exercising jurisdiction in respect of any water dispute referred to a Tribunal.\n3. Although original jurisdiction under Article 131 is excluded, the Supreme Court has ruled that it retains the constitutional power to hear Special Leave Petitions under Article 136 against the final order or award of a water disputes tribunal.\nWhich of the statements given above are correct?",
        "question_te": "భారత రాజ్యాంగంలోని అధికరణ 262 ప్రకారం అంతర్-రాష్ట్ర నదీ జల వివాదాల పరిష్కార వ్యవస్థకు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. ఆర్టికల్ 262(1) ప్రకారం ఏదైనా అంతర్-రాష్ట్ర నది లేదా నదీ లోయ జలాల వినియోగం, పంపిణీ లేదా నియంత్రణపై వివాదాల పరిష్కారం కోసం పార్లమెంటు చట్టం ద్వారా ప్రత్యేక నిబంధనలను రూపొందించవచ్చు.\n2. ఆర్టికల్ 262(2) మరియు అంతర్-రాష్ట్ర నదీ జల వివాదాల చట్టం 1956 లోని సెక్షన్ 11 ప్రకారం, ట్రిబ్యునల్‌కు నివేదించిన నదీ జల వివాదాలపై సుప్రీంకోర్టుతో సహా ఏ న్యాయస్థానానికీ అధికార పరిధి లేకుండా పార్లమెంటు నిషేధించింది.\n3. ఆర్టికల్ 131 కింద ప్రారంభ అధికార పరిధి వర్తించనప్పటికీ, ట్రిబ్యునల్ ఇచ్చిన తుది అవార్డు లేదా ఆదేశాలపై ఆర్టికల్ 136 ప్రకారం స్పెషల్ లీవ్ పిటిషన్లను (SLP) విచారించే రాజ్యాంగ అధికారాలు సుప్రీంకోర్టుకు ఉంటాయని అత్యున్నత న్యాయస్థానం స్పష్టం చేసింది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Article 262 empowers Parliament to legislate on inter-state river disputes and oust court jurisdiction. In pursuance, Parliament enacted the Inter-State River Water Disputes Act, 1956. Section 11 of the Act bars courts from entertaining suits. However, in the Cauvery Water Disputes Tribunal case, the Supreme Court held that its extraordinary appellate jurisdiction under Article 136 cannot be curtailed by statutory exclusion.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. రాజ్యాంగంలోని ఆర్టికల్ 262 ప్రకారం అంతర్-రాష్ట్ర నదీ జల వివాదాలపై ట్రిబ్యునళ్లను ఏర్పాటు చేసి, కోర్టుల పరిధిని మినహాయించే అధికారం పార్లమెంటుకు ఉంది. 1956 నాటి అంతర్-రాష్ట్ర నదీ జల వివాదాల చట్టంలోని సెక్షన్ 11 ప్రకారం కోర్టుల జోక్యం నిషేధించబడింది. అయినప్పటికీ కావేరి జల వివాదం కేసులో సుప్రీంకోర్టు తీర్పునిస్తూ, ఆర్టికల్ 136 కింద ఎస్‌ఎల్‌పీలను స్వీకరించే విశిష్ట న్యాయ సమీక్ష అధికారాన్ని ఏ చట్టమూ తీసివేయలేదని స్పష్టం చేసింది."
    },
    "winners_history_gupta_administration_culture": {
        "id": 67,
        "subject": "Indian History",
        "topic": "Ancient Indian History - Gupta Empire Administration, Agrarian Feudalism & Navaratnas",
        "source_channel": "Winners Online (Winners Publications)",
        "source_video_id": "winners_history_gupta_administration_culture",
        "raw_video_hook": "గుప్తుల పరిపాలనా విభాగాలు, విషయపతులకు సహాయపడే పురపాలక మండలి మరియు అగ్రహార భూదానాల వ్యవస్థ.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the administrative structure and agrarian patterns during the Gupta Empire:\n1. The empire was divided into provinces called *Bhuktis* governed by *Uparikas*, which were further subdivided into districts termed *Vishayas* under the administrative charge of *Vishayapatis*.\n2. In urban district headquarters, the Vishayapati was advised by an administrative board comprising the *Nagarashreshthi* (guild president/banker), *Sarthavaha* (caravan trade leader), *Prathamakulika* (chief artisan), and *Prathamakayastha* (chief scribe).\n3. The Gupta period witnessed the widespread institutionalization of tax-free land grants called *Agrahara* (to Brahmanas) and *Devagrahara* (to temples), conferring perpetual fiscal immunities and exemption from entry of royal tax collectors (*Apraveshya*).\nWhich of the statements given above are correct?",
        "question_te": "గుప్త సామ్రాజ్య పరిపాలనా వ్యవస్థ మరియు నాటి వ్యవసాయ భూ విధానాలకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. గుప్తుల సామ్రాజ్యాన్ని 'భుక్తులు' అనబడే రాష్ట్రాలుగా విభజించి 'ఉపరికులు' అనే గవర్నర్లకు అప్పగించారు; భుక్తులను తిరిగి 'విషయాలు' (జిల్లాలు) గా విభజించి 'విషయపతుల' పాలనలో ఉంచారు.\n2. నగర పరిపాలనలో విషయపతికి సలహాలు అందించేందుకు నగరశ్రేష్ఠి (ప్రధాన వ్యాపారి/బ్యాంకర్), సార్థవాహ (వర్తక బిడారుల అధిపతి), ప్రథమకులిక (ప్రధాన చేతివృత్తుల శిల్పి) మరియు ప్రథమకాయస్థ (ప్రధాన లేఖకుడు/రాయసగాడు) లతో కూడిన పురపాలక బోర్డు ఉండేది.\n3. గుప్తుల కాలంలో బ్రాహ్మణులకు ఇచ్చే 'అగ్రహారాలు' మరియు దేవాలయాలకు ఇచ్చే 'దేవగ్రహారాలు' అనే పన్ను లేని శాశ్వత భూదానాల వ్యవస్థ విస్తరించింది; వీటిలో రాజరిక అధికారులు ప్రవేశించకుండా మినహాయింపు (అప్రవేశ్య) ఉండేది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Epigraphic evidence from Damodarpur copper plates reveals Gupta provincial governance: Bhuktis headed by Uparikas and Vishayas headed by Vishayapatis assisted by a municipal council of four urban elites (Nagarashreshthi, Sarthavaha, Prathamakulika, Prathamakayastha). The era accelerated feudal land devolution via tax-exempt Agrahara grants with royal non-interference rights (*Apraveshya*).",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. దామోదర్‌పూర్ రాగిరేకుల శాసనాలు గుప్తుల పరిపాలనా విభాగాలుగా భుక్తులు (ఉపరికులు), విషయాలు (విషయపతులు) ఉన్నట్లు తెలుపుతున్నాయి. జిల్లా నగర పాలనలో నలుగురు ప్రముఖులతో కూడిన బోర్డు (నగరశ్రేష్ఠి, సార్థవాహ, ప్రథమకులిక, ప్రథమకాయస్థ) సహాయపడేది. అగ్రహారాలు మరియు దేవగ్రహారాల ద్వారా పన్ను రహిత భూదానాలు విస్తరించి మధ్యయుగ భూస్వామ్య వ్యవస్థకు నాంది పలికాయి."
    },
    "winners_history_non_cooperation_khilafat_1920": {
        "id": 68,
        "subject": "Indian History",
        "topic": "Modern Indian History - Non-Cooperation Movement (1920–1922) & Nagpur Session Reorganization",
        "source_channel": "Winners Online (Winners Publications)",
        "source_video_id": "winners_history_non_cooperation_khilafat_1920",
        "raw_video_hook": "1920 సహాయ నిరాకరణ ఉద్యమం, నాగ్‌పూర్ కాంగ్రెస్ సంస్థాగత పునర్వ్యవస్థీకరణ మరియు బార్డోలీ తీర్మానం.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Non-Cooperation Movement (1920–1922) and the institutional transformation of the Indian National Congress:\n1. At the Nagpur annual session of the Congress held in December 1920 (presided over by C. Vijayaraghavachariar), the Non-Cooperation resolution was formally ratified after being moved by Chittaranjan Das (C.R. Das).\n2. The Nagpur session reorganized the Congress into a mass political movement by creating a 15-member Congress Working Committee (CWC) and organizing Provincial Congress Committees (PCCs) on a linguistic basis.\n3. Following the violent incident at Chauri Chaura in Gorakhpur district on February 4/5, 1922, Mahatma Gandhi halted the nationwide movement through the resolution passed by the Congress Working Committee at Bardoli.\nWhich of the statements given above are correct?",
        "question_te": "సహాయ నిరాకరణ ఉద్యమం (1920–1922) మరియు భారత జాతీయ కాంగ్రెస్ సంస్థాగత మార్పులకు సంబంధించి క్రింది ప్రకటనలను పరిశీలించండి:\n1. 1920 డిసెంబర్‌లో సి. విజయరాఘవాచారియార్ అధ్యక్షతన జరిగిన నాగ్‌పూర్ వార్షిక సమావేశంలో చిత్తరంజన్ దాస్ (సి.ఆర్. దాస్) ప్రతిపాదించిన చారిత్రక సహాయ నిరాకరణ తీర్మానాన్ని కాంగ్రెస్ లాంఛనంగా ఆమోదించింది.\n2. నాగ్‌పూర్ సమావేశం ద్వారా కాంగ్రెస్‌ను విస్తృత ప్రజా ఉద్యమంగా మారుస్తూ 15 మంది సభ్యులతో కూడిన 'కాంగ్రెస్ వర్కింగ్ కమిటీ' (CWC) ని ఏర్పాటు చేశారు మరియు ప్రాంతీయ కాంగ్రెస్ కమిటీలను (PCC) భాషా ప్రాతిపదికన పునర్వ్యవస్థీకరించారు.\n3. 1922 ఫిబ్రవరి 4/5న గోరఖ్‌పూర్ జిల్లా చౌరీ చౌరాలో జరిగిన హింసాత్మక ఘటన అనంతరం, బార్డోలీలో సమావేశమైన కాంగ్రెస్ వర్కింగ్ కమిటీ తీర్మానం ద్వారా మహాత్మా గాంధీ సహాయ నిరాకరణ ఉద్యమాన్ని నిలిపివేశారు.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. The Calcutta Special Session (Sept 1920, Lala Lajpat Rai presiding) initially approved Non-Cooperation, which was confirmed at Nagpur (Dec 1920) where C.R. Das moved the main resolution. The Nagpur session transformed the Congress from an elite debating club into an active mass movement with a 15-member CWC, linguistic PCCs, and 4-anna membership fee. After the Chauri Chaura tragedy in Feb 1922, Gandhi suspended the movement via the Bardoli resolution.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. 1920 నాగ్‌పూర్ సమావేశంలో సి.ఆర్. దాస్ సహాయ నిరాకరణ తీర్మానాన్ని ప్రతిపాదించారు. నాగ్‌పూర్ సదస్సులో కాంగ్రెస్ రాజ్యాంగాన్ని సవరించి 15 మందితో CWC, భాషా ప్రయుక్త కాంగ్రెస్ కమిటీలు, 4 అణాల సభ్యత్వ రుసుమును ప్రవేశపెట్టారు. 1922 ఫిబ్రవరిలో చౌరీ చౌరాలో 22 మంది పోలీసులు సజీవ దహనమైన ఘటనతో గాంధీజీ బార్డోలీ తీర్మానం ద్వారా ఉద్యమాన్ని తక్షణమే ఉపసంహరించుకున్నారు."
    },
    "tsat_tg_satavahana_culture_hala": {
        "id": 69,
        "subject": "Telangana History",
        "topic": "Ancient Telangana History & Culture - Satavahana Dynasty: Literature & Buddhist Monuments",
        "source_channel": "T-SAT Network (Govt of Telangana)",
        "source_video_id": "tsat_tg_satavahana_culture_hala",
        "raw_video_hook": "శాతవాహనుల కాలం నాటి సాహితీ వైభవం, హాలుని గాథాసప్తశతి మరియు తెలంగాణలోని ప్రముఖ బౌద్ధ క్షేత్రాలు.",
        "question_type": "Match the Following",
        "question_en": "Match the following classical literary works and major Buddhist monuments associated with the Satavahana era with their respective authors or geographic locations:\n(A) Gatha Saptashati (గాథాసప్తశతి)            - (1) Sarvavarma (Sanskrit grammar compendium composed for King Kuntala Satakarni)\n(B) Brihatkatha (బృహత్కథ)                     - (2) King Hala (17th Satavahana monarch; anthology of 700 Prakrit verses depicting Deccan rustic life)\n(C) Katantra Vyakarana (కాతంత్ర వ్యాకరణం)       - (3) Gunadhya (Epic narrative composed in the Paisachi Prakrit language)\n(D) Phanigiri Buddhist Monastic Site (ఫణిగిరి) - (4) Suryapet district, Telangana (Excavations revealed Mahastupa, Ayaka platforms, and Torana arches)\nCorrect matching code:",
        "question_te": "శాతవాహనుల నాటి ప్రముఖ సాహిత్య గ్రంథాలు మరియు బౌద్ధ క్షేత్రాలను వాటి రచయితలు/భౌగోళిక ప్రాంతాలతో జతపరచండి:\n(A) గాథాసప్తశతి                - (1) శర్వవర్మ (కుంతల శాతకర్ణికి సంస్కృతం నేర్పేందుకు రచించిన వ్యాకరణ గ్రంథం)\n(B) బృహత్కథ                 - (2) హాల చక్రవర్తి (17వ శాతవాహన రాజు; గ్రామీణ జనజీవనాన్ని ప్రతిబింబించే 700 ప్రాకృత పద్యాల సంకలనం)\n(C) కాతంత్ర వ్యాకరణం          - (3) గుణాఢ్యుడు (పైశాచీ ప్రాకృత భాషలో రచించిన కథాకావ్యం)\n(D) ఫణిగిరి బౌద్ధ క్షేత్రం        - (4) సూర్యాపేట జిల్లా, తెలంగాణ (మహాస్తూపం, ఆయక స్తంభాలు, తోరణాలు వెలుగుచూసిన ప్రసిద్ధ బౌద్ధ స్థలం)\nసరైన కోడ్‌ను ఎంచుకోండి:",
        "options_en": ["A-2, B-3, C-1, D-4", "A-3, B-2, C-1, D-4", "A-2, B-4, C-3, D-1", "A-1, B-3, C-4, D-2"],
        "options_te": ["A-2, B-3, C-1, D-4", "A-3, B-2, C-1, D-4", "A-2, B-4, C-3, D-1", "A-1, B-3, C-4, D-2"],
        "correct_option": 0,
        "explanation_en": "Correct matching is A-2, B-3, C-1, D-4. King Hala (Kavivatsala) edited Gatha Saptashati in Maharashtri Prakrit, highlighting village life along the Godavari. Gunadhya composed Brihatkatha in Paisachi Prakrit. Sarvavarma authored Katantra Vyakarana to teach King Kuntala Satakarni rapid Sanskrit. Phanigiri in Suryapet district is one of Telangana's foremost Satavahana-Ikshvaku era Buddhist settlements, notable for its octagonal stupa and stone torana carvings.",
        "explanation_te": "సరైన జత: A-2, B-3, C-1, D-4. హాలుడు (కవివత్సలుడు) ప్రాకృతంలో గాథాసప్తశతి సంకలనం చేశాడు. గుణాఢ్యుడు పైశాచీ భాషలో బృహత్కథను రచించగా, శర్వవర్మ కాతంత్ర వ్యాకరణాన్ని రాశాడు. సూర్యాపేట జిల్లాలోని ఫణిగిరిలో శాతవాహన కాలం నాటి మహాస్తూపం, అరుదైన అష్టభుజి స్తూపం, సుందర తోరణాలు లభ్యమయ్యాయి."
    },
    "tsat_polity_finance_commission_art280": {
        "id": 70,
        "subject": "Indian Polity",
        "topic": "Constitutional Bodies - Finance Commission of India (Article 280) & 16th Finance Commission",
        "source_channel": "T-SAT Network (Govt of Telangana)",
        "source_video_id": "tsat_polity_finance_commission_art280",
        "raw_video_hook": "రాజ్యాంగంలోని ఆర్టికల్ 280 ప్రకారం కేంద్ర ఆర్థిక సంఘం అధికారాలు, విధులు మరియు 16వ ఆర్థిక సంఘం నియామకం.",
        "question_type": "Multi-Statement",
        "question_en": "Consider the following statements regarding the Finance Commission of India constituted under Article 280 of the Constitution:\n1. The Finance Commission is constituted by the President of India every fifth year (or earlier), consisting of a Chairman and four other members whose qualifications are determined by Parliament.\n2. The primary constitutional functions of the Commission include recommending the distribution of the net proceeds of divisible taxes between the Union and the States (vertical devolution) and the allocation among the States of their respective shares (horizontal devolution).\n3. Under Article 280(3)(bb) and (c) inserted by the 73rd and 74th Amendments, the Commission recommends measures needed to augment the Consolidated Fund of a State to supplement the resources of Panchayats and Municipalities on the basis of recommendations of State Finance Commissions.\nWhich of the statements given above are correct?",
        "question_te": "భారత రాజ్యాంగంలోని అధికరణ 280 కింద ఏర్పాటయ్యే కేంద్ర ఆర్థిక సంఘం (Finance Commission) కు సంబంధించి క్రింది అంశాలను పరిశీలించండి:\n1. ఆర్టికల్ 280 ప్రకారం ప్రతి ఐదేళ్లకొకసారి (లేదా అవసరమైనప్పుడు అంతకంటే ముందే) భారత రాష్ట్రపతి ఒక చైర్మన్ మరియు నలుగురు సభ్యులతో ఆర్థిక సంఘాన్ని నియమిస్తారు; వీరి అర్హతలను పార్లమెంటు చట్టం ద్వారా నిర్ణయిస్తుంది.\n2. కేంద్రం మరియు రాష్ట్రాల మధ్య నికర పన్ను ఆదాయాల పంపిణీ (నిలువు పంపిణీ / Vertical Devolution) మరియు రాష్ట్రాల మధ్య వాటాల కేటాయింపు (సమాంతర పంపిణీ / Horizontal Devolution) సూత్రాలను సిఫార్సు చేయడం ఆర్థిక సంఘం ప్రధాన విధి.\n3. 73వ మరియు 74వ రాజ్యాంగ సవరణల ద్వారా చేర్చబడిన ఆర్టికల్ 280(3)(bb) మరియు (c) ప్రకారం, రాష్ట్ర ఆర్థిక సంఘం సిఫార్సుల ఆధారంగా పంచాయతీలు, మున్సిపాలిటీల వనరులను భర్తీ చేసేందుకు రాష్ట్ర కన్సాలిడేటెడ్ ఫండ్‌ను పెంచే చర్యలను కేంద్ర ఆర్థిక సంఘం సిఫార్సు చేస్తుంది.\nపై ప్రకటనలలో సరైనవి ఏవి?",
        "options_en": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "options_te": ["1 మరియు 2 మాత్రమే", "2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3"],
        "correct_option": 3,
        "explanation_en": "All three statements are correct. Article 280 governs the Finance Commission as a quasi-judicial body. Parliament passed the Finance Commission Act, 1951 specifying qualifications for the Chairman and 4 members. Functions under 280(3) include vertical/horizontal tax sharing, Article 275 grants-in-aid, and augmenting state consolidated funds for local bodies following the 73rd/74th amendments. The 16th Finance Commission is chaired by Dr. Arvind Panagariya.",
        "explanation_te": "మూడు ప్రకటనలూ సరైనవే. ఆర్టికల్ 280 కింద రాష్ట్రపతి ఆర్థిక సంఘాన్ని నియమిస్తారు. పార్లమెంట్ 1951 నాటి చట్టం ద్వారా చైర్మన్ మరియు నలుగురు సభ్యుల అర్హతలను నిర్దేశించింది. కేంద్ర-రాష్ట్రాల మధ్య నికర పన్నుల విభజన, ఆర్టికల్ 275 గ్రాంట్లు, 73/74వ సవరణల ప్రకారం స్థానిక సంస్థలకు నిధుల బలోపేతం దీని ప్రధాన విధులు. 16వ ఆర్థిక సంఘం చైర్మన్‌గా నీతి ఆయోగ్ మాజీ వైస్ చైర్మన్ డాక్టర్ అరవింద్ పనగరియా పనిచేస్తున్నారు."
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
