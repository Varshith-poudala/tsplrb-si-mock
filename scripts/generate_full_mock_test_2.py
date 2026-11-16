#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full Paper Generator for TSPLRB SI Prelims Mock Test 2 (200 Questions)
"""

import json
import os

with open('public/data/reference_science_gk_200.json', 'r', encoding='utf-8') as f:
    science_ref = json.load(f)

with open('public/data/reference_current_affairs_400.json', 'r', encoding='utf-8') as f:
    ca_ref = json.load(f)['questions']

print("Loaded references successfully.")
