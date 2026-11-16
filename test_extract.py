#!/usr/bin/env python3
"""
Full 200-Question Paper Generator for 3 New Mock Tests:
- Mock Test 3: Easy (Foundational PWT)
- Mock Test 4: Medium (Official 2022 PWT Standard)
- Mock Test 5: Tough (Advanced High-Yield PWT Simulation)

Each paper contains exactly 200 bilingual questions:
  - Part A: Arithmetic (Q1 - Q50)
  - Part B: Reasoning & Mental Ability (Q51 - Q100)
  - Part C: General Studies & Telangana Movement (Q101 - Q200)
"""

import json
import os
import re
import subprocess

PDF_DIR = '/Users/provakil/.gemini/antigravity/brain/1b989ebf-8e44-423e-b96d-31d216f15bff/.user_uploaded'

def clean_text(s):
    if not s:
        return ""
    # remove excessive spaces and form feeds
    s = s.replace('\x0c', ' ')
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()

def parse_pdf_raw_questions(fname):
    p = os.path.join(PDF_DIR, fname)
    if not os.path.exists(p):
        print(f"Warning: {p} not found")
        return []
    txt = subprocess.run(['/opt/homebrew/bin/pdftotext', p, '-'], capture_output=True, text=True).stdout
    matches = list(re.finditer(r'\n(\d+)\.\s+\1\s*\n', txt))
    items = []
    for i in range(len(matches)):
        start = matches[i].end()
        end = matches[i+1].start() if i+1 < len(matches) else len(txt)
        chunk = txt[start:end].strip()
        
        opt_matches = list(re.finditer(r'(?:^|\n)([1-4])\.\s+[1-4](.*?)(?=(?:\n[1-4]\.\s+[1-4])|$)', chunk, re.DOTALL))
        if len(opt_matches) == 4:
            first_opt_idx = re.search(r'\n1\.\s+1', chunk)
            stmt = chunk[:first_opt_idx.start()].strip() if first_opt_idx else chunk
            
            m_tel = re.search(r'([\u0C00-\u0C7F].*)', stmt, re.DOTALL)
            if m_tel:
                q_en = stmt[:m_tel.start()].strip()
                q_te = m_tel.group(1).strip()
            else:
                q_en = stmt
                q_te = stmt
                
            opts_en = []
            opts_te = []
            for om in opt_matches:
                otext = om.group(2).strip()
                m_otel = re.search(r'([\u0C00-\u0C7F].*)', otext)
                if m_otel:
                    o_en = otext[:m_otel.start()].strip() or otext
                    o_te = m_otel.group(1).strip()
                else:
                    o_en = otext
                    o_te = otext
                opts_en.append(clean_text(o_en))
                opts_te.append(clean_text(o_te))
                
            items.append({
                'num': int(matches[i].group(1)),
                'q_en': clean_text(q_en),
                'q_te': clean_text(q_te),
                'opts_en': opts_en,
                'opts_te': opts_te,
            })
    return items

print("Extracting authentic questions from uploaded PDFs...")
raw_gs = parse_pdf_raw_questions('media_1794466169506_0ce19a1b.pdf')
raw_arith1 = parse_pdf_raw_questions('media_1794466169500_02e6c2db.pdf')
raw_arith2 = parse_pdf_raw_questions('media_1794466169497_3e2cc500.pdf')
raw_arith3 = parse_pdf_raw_questions('media_1794466169495_0c7c8f96.pdf')

print(f"Loaded: GS={len(raw_gs)}, Arith1={len(raw_arith1)}, Arith2={len(raw_arith2)}, Arith3={len(raw_arith3)}")
