#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

with open('public/data/reference_science_gk_200.json') as f:
    science_bank = json.load(f)

with open('public/data/reference_current_affairs_400.json') as f:
    ca_bank = json.load(f)['questions']

print("References successfully loaded.")
