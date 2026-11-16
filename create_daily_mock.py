#!/usr/bin/env python3
"""
TSPLRB SI Prelims Daily Mock Test Generator
Generates full-length 100-question papers (50 Arithmetic + 50 Reasoning)
following official TSPLRB SI Prelims syllabus and difficulty weighting.
"""

import os
import sys
import json
import argparse
from datetime import datetime

# Import base question bank
from generate_questions import questions as base_questions

def create_mock_test(day_number=1, output_file=None):
    if output_file is None:
        output_file = f"public/data/mock_test_{day_number}.json"
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # In day 2+, we can use the comprehensive verified questions
    # with customized test metadata
    payload = {
        "testId": f"tsplrb-si-mock-{day_number:02d}",
        "title": f"TSPLRB SI Prelims Daily Mock Test - Day {day_number}",
        "title_te": f"తెలంగాణ ఎస్సై ప్రిలిమ్స్ రోజువారీ మాక్ టెస్ట్ - డే {day_number}",
        "exam": "Telangana State Police Sub-Inspector (SI) Preliminary Written Test",
        "paper": "Paper I: Arithmetic and Test of Reasoning / Mental Ability",
        "generatedAt": datetime.now().isoformat(),
        "totalQuestions": len(base_questions),
        "totalMarks": 100,
        "durationMinutes": 180,
        "marksPerQuestion": 1.0,
        "negativeMarking": 0.20,
        "sections": [
            {"id": "arithmetic", "name": "Arithmetic", "start": 1, "end": 50, "count": 50},
            {"id": "reasoning", "name": "Reasoning & Mental Ability", "start": 51, "end": 100, "count": 50}
        ],
        "questions": base_questions
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        
    print(f"✅ Successfully created Day {day_number} Mock Test with {len(base_questions)} questions at: {output_file}")
    return output_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate TSPLRB SI Prelims Daily Mock Tests")
    parser.add_argument("--day", type=int, default=1, help="Day number (default: 1)")
    parser.add_argument("--out", type=str, default=None, help="Output path (default: public/data/mock_test_{day}.json)")
    args = parser.parse_args()
    
    create_mock_test(args.day, args.out)
