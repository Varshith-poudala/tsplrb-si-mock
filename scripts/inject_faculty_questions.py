#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inject 30 high-yield faculty-curated questions from live_youtube_extracted_questions.json
into Mock Tests 1 through 7, targeting older/duplicate Current Affairs, Polity, and Telangana sections.
"""

import json
import os

SOURCE_FILE = "public/data/live_youtube_extracted_questions.json"

# Original Mock 1 Q101 and Q102 to ensure Demo Test 15/15 2026 Current Affairs compliance
MOCK1_Q101_ORIGINAL = {
    "id": 101,
    "section": "General Studies",
    "topic": "Current Affairs - Telangana & National Conclaves",
    "question_en": "Where was the premier biennial civil aviation conclave and exhibition 'Wings India 2026' organized?",
    "question_te": "ప్రతిష్టాత్మక ద్వైవార్షిక పౌర విమానయాన సదస్సు మరియు ప్రదర్శన 'వింగ్స్ ఇండియా 2026' (Wings India 2026) ఎక్కడ నిర్వహించబడింది?",
    "options_en": [
        "Begumpet Airport, Hyderabad",
        "Indira Gandhi International Airport, New Delhi",
        "Kempegowda International Airport, Bengaluru",
        "Cochin International Airport, Kochi"
    ],
    "options_te": [
        "బేగంపేట్ విమానాశ్రయం, హైదరాబాద్",
        "ఇందిరా గాంధీ అంతర్జాతీయ విమానాశ్రయం, న్యూఢిల్లీ",
        "కెంపేగౌడ అంతర్జాతీయ విమానాశ్రయం, బెంగళూరు",
        "కొచ్చిన్ అంతర్జాతీయ విమానాశ్రయం, కొచ్చి"
    ],
    "correct_option": 0,
    "explanation_en": "Asia's largest commercial aviation event 'Wings India 2026' was organized at Begumpet Airport, Hyderabad by the Ministry of Civil Aviation and FICCI.",
    "explanation_te": "ఆసియాలోనే అతిపెద్ద పౌర విమానయాన ప్రదర్శన 'వింగ్స్ ఇండియా 2026' హైదరాబాద్‌లోని బేగంపేట్ విమానాశ్రయంలో కేంద్ర పౌర విమానయాన మంత్రిత్వ శాఖ మరియు FICCI సంయుక్తంగా నిర్వహించాయి."
}

MOCK1_Q102_ORIGINAL = {
    "id": 102,
    "section": "General Studies",
    "topic": "Current Affairs - Telangana Industrial Schemes",
    "question_en": "In which district of Telangana was the state's flagship PM MITRA (Mega Integrated Textile Region and Apparel) mega park operationalized in 2026?",
    "question_te": "తెలంగాణలోని ఏ జిల్లాలో ప్రతిష్టాత్మక PM మిత్రా (PM MITRA) మెగా టెక్స్‌టైల్ పార్కు 2026లో పూర్తి స్థాయిలో కార్యకలాపాలు ప్రారంభించింది?",
    "options_en": [
        "Warangal",
        "Karimnagar",
        "Nalgonda",
        "Rangareddy"
    ],
    "options_te": [
        "వరంగల్",
        "కరీంనగర్",
        "నల్గొండ",
        "రంగారెడ్డి"
    ],
    "correct_option": 0,
    "explanation_en": "The PM MITRA Mega Textile Park at Kakatiya Mega Textile Park (KMTP) in Warangal, Telangana was inaugurated to make the region a world-class textile manufacturing and export hub.",
    "explanation_te": "వరంగల్‌లోని కాకతీయ మెగా టెక్స్‌టైల్ పార్క్ (KMTP) ఆవరణలో PM మిత్రా మెగా టెక్స్‌టైల్ పార్క్ తెలంగాణను గ్లోబల్ టెక్స్‌టైల్ తయారీ మరియు ఎగుమతి కేంద్రంగా తీర్చిదిద్దడానికి ప్రారంభించబడింది."
}

PLAN = {
    "public/data/mock_test_full_200.json": [
        {"slot": 171, "source_id": 11}, # Speaker Removal (Art 94)
        {"slot": 178, "source_id": 1},  # Two-Child Norm Repeal (Telangana Governance)
        {"slot": 179, "source_id": 2},  # Bhoo Bharati Land Titling (Telangana Governance)
        {"slot": 188, "source_id": 18}, # Kakatiya Motupalli
        {"slot": 189, "source_id": 19}, # 1969 Agitation Genesis
    ],
    "public/data/mock_test_full_200_2.json": [
        {"slot": 151, "source_id": 3},  # Operation Crack Down (Cyber Policing)
        {"slot": 152, "source_id": 4},  # HYDRAA (Urban Waterbodies & Disaster Management)
        {"slot": 171, "source_id": 12}, # 106th Amendment (Polity)
        {"slot": 172, "source_id": 20}, # Kumar Lalit & Bhargava Committees (Telangana Movement)
        {"slot": 188, "source_id": 21}, # Operation Polo (Telangana Integration)
    ],
    "public/data/mock_test_full_200_3.json": [
        {"slot": 103, "source_id": 5},  # Wings India Conclave
        {"slot": 104, "source_id": 6},  # Indiramma Indlu
        {"slot": 171, "source_id": 13}, # Governor's Assent (Art 200)
        {"slot": 172, "source_id": 22}, # 1952 Non-Mulki City College
    ],
    "public/data/mock_test_full_200_4.json": [
        {"slot": 103, "source_id": 7},  # Young India Skill University
        {"slot": 104, "source_id": 8},  # National Tribal Healers Conclave
        {"slot": 171, "source_id": 14}, # Anti-Defection 10th Schedule
        {"slot": 172, "source_id": 23}, # Komaram Bheem & Jodeghat
    ],
    "public/data/mock_test_full_200_5.json": [
        {"slot": 103, "source_id": 9},  # IIT Hyderabad ANUJA Program
        {"slot": 104, "source_id": 10}, # Comprehensive Caste Survey
        {"slot": 171, "source_id": 15}, # Inter-State River Water (Art 262)
        {"slot": 186, "source_id": 24}, # Gentlemen's Agreement 1956
    ],
    "public/data/mock_test_full_200_6.json": [
        {"slot": 171, "source_id": 16}, # 16th Finance Commission (Art 280)
        {"slot": 188, "source_id": 25}, # Salar Jung Reforms
        {"slot": 151, "source_id": 26}, # Buddhism & Sarnath UNESCO
        {"slot": 152, "source_id": 27}, # 1919 Montagu-Chelmsford
    ],
    "public/data/mock_test_full_200_7.json": [
        {"slot": 171, "source_id": 17}, # 73rd Amendment Panchayati Raj
        {"slot": 151, "source_id": 28}, # 1935 Government of India Act
        {"slot": 153, "source_id": 29}, # Socio-Religious Reforms
        {"slot": 154, "source_id": 30}, # 1942 Quit India Movement
    ]
}

def main():
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        source_data = json.load(f)
    
    source_map = {q["id"]: q for q in source_data["questions"]}
    print(f"Loaded {len(source_map)} source questions from {SOURCE_FILE}")
    
    total_injected = 0
    used_source_ids = set()
    
    for filepath, injections in PLAN.items():
        with open(filepath, "r", encoding="utf-8") as f:
            test_data = json.load(f)
        
        qs = test_data.get("questions", [])
        assert len(qs) == 200, f"{filepath} does not have 200 questions!"
        
        # If Mock 1, restore original Q101 and Q102
        if "mock_test_full_200.json" in filepath and "mock_test_full_200_2" not in filepath:
            qs[100] = MOCK1_Q101_ORIGINAL
            qs[101] = MOCK1_Q102_ORIGINAL
            print("  [mock_test_full_200.json] Restored Q101 & Q102 (Demo Test 2026 Current Affairs compliance)")
        
        for inj in injections:
            slot = inj["slot"]
            sid = inj["source_id"]
            sq = source_map[sid]
            used_source_ids.add(sid)
            
            # Target question index is slot - 1
            idx = slot - 1
            existing_sec = qs[idx].get("section", "General Studies")
            
            # Format combined topic
            topic_str = f"{sq.get('subject', 'General Studies')} - {sq.get('topic', '')}"
            
            qs[idx] = {
                "id": slot,
                "section": existing_sec,
                "topic": topic_str,
                "question_en": sq["question_en"],
                "question_te": sq["question_te"],
                "options_en": sq["options_en"],
                "options_te": sq["options_te"],
                "correct_option": sq["correct_option"],
                "explanation_en": sq["explanation_en"],
                "explanation_te": sq["explanation_te"]
            }
            total_injected += 1
            print(f"  [{os.path.basename(filepath)}] Slot {slot} <- Source Q{sid} ({sq['topic'][:40]}...)")
            
        test_data["questions"] = qs
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)
            
    print(f"\nSuccessfully injected {total_injected} questions across 7 mock tests!")
    print(f"Unique source questions used: {len(used_source_ids)} / {len(source_map)}")
    assert len(used_source_ids) == 30, "Not all 30 questions were used!"

if __name__ == "__main__":
    main()
