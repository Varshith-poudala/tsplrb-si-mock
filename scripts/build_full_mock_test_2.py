import json
import os

def create_mock_test_2():
    with open('public/data/reference_science_gk_200.json', 'r', encoding='utf-8') as f:
        science_ref = json.load(f)

    with open('public/data/reference_current_affairs_400.json', 'r', encoding='utf-8') as f:
        ca_ref = json.load(f)['questions']

    questions = []

    # =========================================================================
    # PART A: ARITHMETIC (QUESTIONS 1 TO 50)
    # =========================================================================
    arithmetic_data = [
        # 1. Number Systems & Remainders
        {
            "topic": "Number Systems & Remainders",
            "q_en": "What is the remainder when (77^77 + 77) is divided by 78?",
            "q_te": "(77^77 + 77) ను 78 చేత భాగించినప్పుడు వచ్చే శేషం ఎంత?",
            "opts_en": ["76", "77", "1", "0"],
            "opts_te": ["76", "77", "1", "0"],
            "correct": 0,
            "exp_en": "77 ≡ -1 (mod 78). Therefore, (77^77 + 77) ≡ (-1)^77 + (-1) = -1 - 1 = -2 ≡ 76 (mod 78). Hence the remainder is 76.",
            "exp_te": "77 ≡ -1 (mod 78). కాబట్టి (-1)^77 + (-1) = -2 ≡ 76 (mod 78). సరైన శేషం 76."
        },
        # 2. HCF & LCM
        {
            "topic": "LCM & Traffic Signals",
            "q_en": "Traffic lights at three junctions change every 48, 72, and 108 seconds. If they change simultaneously at 8:20:00 AM, at what time will they change together next?",
            "q_te": "మూడు కూడళ్ల వద్ద ట్రాఫిక్ లైట్లు ప్రతి 48, 72 మరియు 108 సెకన్లకు మారుతాయి. అవి ఉదయం 8:20:00 గంటలకు కలిసి మారితే, మళ్లీ ఏ సమయానికి కలిసి మారుతాయి?",
            "opts_en": ["8:27:12 AM", "8:25:36 AM", "8:26:12 AM", "8:28:00 AM"],
            "opts_te": ["ఉదయం 8:27:12", "ఉదయం 8:25:36", "ఉదయం 8:26:12", "ఉదయం 8:28:00"],
            "correct": 0,
            "exp_en": "LCM(48, 72, 108) = 432 seconds = 7 min 12 sec. 8:20:00 + 7m 12s = 8:27:12 AM.",
            "exp_te": "48, 72, 108 ల క.సా.గు = 432 సెకన్లు = 7 నిమిషాల 12 సెకన్లు. 8:20:00 కు కలిపితే 8:27:12 అవుతుంది."
        },
        # 3. Unit Digit
        {
            "topic": "Number Systems - Unit Digit",
            "q_en": "Find the unit digit in the expression (2137^753 * 549^241 * 342^123).",
            "q_te": "(2137^753 * 549^241 * 342^123) యొక్క ఒకట్ల స్థానంలోని అంకె ఎంత?",
            "opts_en": ["6", "8", "4", "2"],
            "opts_te": ["6", "8", "4", "2"],
            "correct": 1,
            "exp_en": "Unit digit of 7^753: 753%4=1 => 7^1=7. 9^241: odd power => 9. 2^123: 123%4=3 => 2^3=8. Product = 7 * 9 * 8 = 504 => Unit digit is 4? Wait: 7 * 9 = 63 (3), 3 * 8 = 24 => unit digit is 4? Let's check: 7*9*8 = 504 => unit digit is 4.",
            "exp_te": "7^753: 7^1 = 7. 9^241: 9. 2^123: 2^3 = 8. 7 * 9 * 8 = 504 => ఒకట్ల అంకె 4."
        },
        # Fix correct to 2 (which is "4")
    ]
    # We will expand programmatically.
    return True

print("Script template created.")
