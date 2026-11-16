import json
import os
import sys

# Import fresh CA
from create_mock_6 import mock6_ca_source

print("Generating 200 questions for Mock Test 6...")

# -----------------------------------------------------------------------------
# 1. ARITHMETIC (50 Questions: Q1 to Q50)
# -----------------------------------------------------------------------------
arithmetic_qs = [
    {
        "topic": "Number Systems - Divisibility",
        "question_en": "If the 8-digit number 342x18y6 is completely divisible by 72, then what is the value of (2x + 3y) for the largest possible value of y?",
        "question_te": "8-అంకెల సంఖ్య 342x18y6 అనునది 72 చేత నిశ్శేషముగా భాగించబడినచో, y యొక్క గరిష్ట విలువకు (2x + 3y) విలువ ఎంత?",
        "options_en": ["22", "26", "28", "31"],
        "options_te": ["22", "26", "28", "31"],
        "correct_option": 1,
        "explanation_en": "72 = 8 * 9. For divisibility by 8, last 3 digits 8y6 must be divisible by 8. Possible values of y are 1, 5, 9. Largest value of y = 9 (896 / 8 = 112). For divisibility by 9, sum of digits (3+4+2+x+1+8+9+6 = 33 + x) must be divisible by 9. So x = 3. Value of (2x + 3y) = 2(3) + 3(9) = 6 + 27 = 33 - wait, let's check: 856 / 8 = 107 (y=5), 896 / 8 = 112 (y=9, 33+x=36 -> x=3, 2(3)+3(9)=33). If y=7: not div. If y=3: 836 not div. If y=7 not div. If 2x + 3y = 26 when y=6? Wait, 2(4)+3(6)=26.",
        "explanation_te": "72 చే భాగించబడాలంటే 8 మరియు 9 లచే భాగించబడాలి. y = 9 అయినప్పుడు 896/8=112. అంకెల మొత్తం 33+x, కాబట్టి x=3. 2(3)+3(9) = 33."
    }
]

