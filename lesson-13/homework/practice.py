# ================================================================
# 10 ta praktikum vazifasi — yagona menyu asosida
# Har bir bo‘limda aniq va minimal izohlar mavjud.
# ================================================================

from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import time
import re


# ------------------------------------------------
# 1. Age Calculator
# ------------------------------------------------
def age_calculator():
    birth = input("Tug‘ilgan kun (YYYY-MM-DD): ")
    b = datetime.strptime(birth, "%Y-%m-%d").date()
    today = date.today()

    years = today.year - b.year
    months = today.month - b.month
    days = today.day - b.day

    # Kun manfiy chiqsa, oldingi oyning kunlarini qo‘shamiz
    if days < 0:
        months -= 1
        prev_month = (today.month - 1) or 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days += (date(prev_year, prev_month + 1, 1) - date(prev_year, prev_month, 1)).days

    # Oy manfiy chiqsa, yilni bitta kamaytiramiz
    if months < 0:
        years -= 1
        months += 12

    print(f"Yosh: {years} yil, {months} oy, {days} kun\n")


# ------------------------------------------------
# 2. Days Until Next Birthday
# ------------------------------------------------
def days_until_birthday():
    birth = input("Tug‘ilgan kun (YYYY-MM-DD): ")
    b = datetime.strptime(birth, "%Y-%m-%d").date()
    today = date.today()

    next_b = date(today.year, b.month, b.day)
    if next_b < today:
        next_b = date(today.year + 1, b.month, b.day)

    print("Qolgan kunlar:", (next_b - today).days, "\n")


# ------------------------------------------------
# 3. Meeting Scheduler
# ------------------------------------------------
def meeting_scheduler():
    now = input("Hozirgi vaqt (YYYY-MM-DD HH:MM): ")
    dur_h = int(input("Soat: "))
    dur_m = int(input("Daqiqa: "))

    start = datetime.strptime(now, "%Y-%m-%d %H:%M")
    end = start + timedelta(hours=dur_h, minutes=dur_m)

    print("Uchrashuv tugash vaqti:", end, "\n")


# ------------------------------------------------
# 4. Timezone Converter
# ------------------------------------------------
def timezone_converter():
    dt = input("Vaqt (YYYY-MM-DD HH:MM): ")
    from_tz = input("Joriy timezone (masalan: Asia/Tashkent): ")
    to_tz = input("O‘tkaziladigan timezone: ")

    t = datetime.strptime(dt, "%Y-%m-%d %H:%M")
    t = t.replace(tzinfo=ZoneInfo(from_tz))
    converted = t.astimezone(ZoneInfo(to_tz))

    print("Natija:", converted, "\n")


# ------------------------------------------------
# 5. Countdown Timer
# ------------------------------------------------
def countdown_timer():
    target = input("Maqsad vaqt (YYYY-MM-DD HH:MM:SS): ")
    t = datetime.strptime(target, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        diff = t - now

        if diff.total_seconds() <= 0:
            print("Taymer tugadi!\n")
            break

        print(diff)
        time.sleep(1)


# ------------------------------------------------
# 6. Email Validator
# ------------------------------------------------
def email_validator():
    email = input("Email: ")
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(pattern, email):
        print("Email to‘g‘ri.\n")
    else:
        print("Email noto‘g‘ri.\n")


# ------------------------------------------------
# 7. Phone Number Formatter
# ------------------------------------------------
def phone_formatter():
    num = input("Raqam (faqat raqamlar): ")
    clean = ''.join(filter(str.isdigit, num))

    if len(clean) == 10:
        print(f"Formatlangan: ({clean[:3]}) {clean[3:6]}-{clean[6:]}\n")
    else:
        print("10 xonali raqam kiriting.\n")


# ------------------------------------------------
# 8. Password Strength Checker
# ------------------------------------------------
def password_checker():
    pwd = input("Parol: ")

    rules = [
        len(pwd) >= 8,
        re.search(r"[A-Z]", pwd),
        re.search(r"[a-z]", pwd),
        re.search(r"[0-9]", pwd)
    ]

    if all(rules):
        print("Kuchli parol.\n")
    else:
        print("Parol talabga javob bermaydi.\n")


# ------------------------------------------------
# 9. Word Finder
# ------------------------------------------------
def word_finder():
    text = "This is a sample text. This text is used for testing word search."
    word = input("Qidiriladigan so‘z: ")

    idx = []
    start = 0

    # Har safar topilgan joy qayd qilinadi
    while True:
        pos = text.lower().find(word.lower(), start)
        if pos == -1:
            break
        idx.append(pos)
        start = pos + 1

    print("Topilgan indekslar:", idx, "\n")


# ------------------------------------------------
# 10. Date Extractor
# ------------------------------------------------
def date_extractor():
    txt = input("Matn kiriting: ")
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    dates = re.findall(pattern, txt)

    print("Topilgan sanalar:", dates, "\n")


# ================================================================
#                   MAIN MENU
# ================================================================

while True:
    print("""
1. Yosh hisoblash
2. Keyingi tug‘ilgan kungacha kun
3. Uchrashuv tugash vaqtini hisoblash
4. Timezone o‘tkazish
5. Countdown timer
6. Email tekshirish
7. Telefon raqam formatlash
8. Parol kuchi tekshiruvi
9. Matndan so‘z qidirish
10. Matndan sanalarni ajratish
0. Chiqish
""")

    choice = input("Tanlang: ")

    if choice == "1": age_calculator()
    elif choice == "2": days_until_birthday()
    elif choice == "3": meeting_scheduler()
    elif choice == "4": timezone_converter()
    elif choice == "5": countdown_timer()
    elif choice == "6": email_validator()
    elif choice == "7": phone_formatter()
    elif choice == "8": password_checker()
    elif choice == "9": word_finder()
    elif choice == "10": date_extractor()
    elif choice == "0":
        print("Dastur yakunlandi.")
        break
    else:
        print("Noto‘g‘ri tanlov.\n")
