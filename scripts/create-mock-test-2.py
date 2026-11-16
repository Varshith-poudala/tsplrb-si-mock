#!/usr/bin/env python3
"""
Generates TSPLRB SI Full-Length Mock Test 2 (200 Questions)
Official PWT Pattern:
- 50 Arithmetic (Q1-Q50)
- 50 Reasoning (Q51-Q100)
- 100 General Studies & Telangana Movement (Q101-Q200):
  * 30 General Science (from reference_science_gk_200.json)
  * 35 Current Affairs 2026 (from reference_current_affairs_400.json)
  * 35 Telangana History, Movement, Schemes & Geography (including PM MITRA Warangal, Musi Rejuvenation, etc.)
"""

import json
import os

with open('public/data/reference_science_gk_200.json', 'r', encoding='utf-8') as f:
    science_bank = json.load(f)

with open('public/data/reference_current_affairs_400.json', 'r', encoding='utf-8') as f:
    ca_data = json.load(f)
    ca_bank = ca_data['questions']

questions = []

print("Starting generation of 200 Questions for Mock Test 2...")
