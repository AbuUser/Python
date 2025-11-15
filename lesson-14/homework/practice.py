# ============================================================
# Homework — Lesson 14
# Barcha 4 ta vazifa bitta menyu ostida
# Har bir funksiya izoh bilan, aniq va minimal
# ============================================================

import json
import requests
import random


# ------------------------------------------------------------
# 1. JSON Parsing (students.json o‘qish)
# ------------------------------------------------------------
def read_students():
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("students.json topilmadi.\n")
        return

    for s in data.get("students", []):
        print(f"Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
    print()


# ------------------------------------------------------------
# 2. Weather API (OpenWeatherMap)
# API_KEY talab qilinadi
# ------------------------------------------------------------
def weather():
    API_KEY = "YOUR_API_KEY"   # O‘zingiznikini qo‘ying
    city = input("Shahar: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        d = requests.get(url).json()
        print("Temperature:", d["main"]["temp"])
        print("Humidity:", d["main"]["humidity"])
        print("Weather:", d["weather"][0]["description"])
    except:
        print("Ma'lumot olinmadi.")
    print()


# ------------------------------------------------------------
# 3. JSON Modification (books.json ustida CRUD)
# ------------------------------------------------------------

FILE = "books.json"

def load_books():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"books": []}

def save_books(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def manage_books():
    while True:
        print("\n1. Add  2. Update  3. Delete  0. Back")
        c = input("Tanlang: ")

        data = load_books()
        books = data["books"]

        if c == "1":
            title = input("Title: ")
            author = input("Author: ")
            books.append({"title": title, "author": author})
            save_books(data)

        elif c == "2":
            title = input("Qaysi kitob?: ")
            found = False
            for b in books:
                if b["title"] == title:
                    b["author"] = input("Yangi author: ")
                    save_books(data)
                    found = True
                    break
            if not found:
                print("Topilmadi.")

        elif c == "3":
            title = input("O‘chiriladigan kitob: ")
            books = [b for b in books if b["title"] != title]
            data["books"] = books
            save_books(data)

        elif c == "0":
            break

        else:
            print("Noto‘g‘ri tanlov.")


# ------------------------------------------------------------
# 4. Movie Recommendation (OMDb API)
# ------------------------------------------------------------
def recommend_movie():
    API_KEY = "YOUR_API_KEY"   # O‘zingiznikini qo‘ying
    genre = input("Genre: ").lower()

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&type=movie&s={genre}"

    try:
        r = requests.get(url).json()
        if "Search" not in r:
            print("Topilmadi.\n")
            return

        movie = random.choice(r["Search"])
        print("Title:", movie["Title"])
        print("Year:", movie["Year"])
    except:
        print("Xatolik.")
    print()


# ============================================================
#                      MAIN MENU
# ============================================================

while True:
    print("""
1. Students JSON o‘qish
2. Ob-havo (API)
3. Books JSON boshqarish
4. Tasodifiy film tavsiya (API)
0. Chiqish
""")

    choice = input("Tanlang: ")

    if choice == "1": read_students()
    elif choice == "2": weather()
    elif choice == "3": manage_books()
    elif choice == "4": recommend_movie()
    elif choice == "0":
        print("Dastur tugadi.")
        break
    else:
        print("Noto‘g‘ri tanlov.\n")
