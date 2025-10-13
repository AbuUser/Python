# ======================================================
# 📚 LESSON 11 — MODULES, PACKAGES & VIRTUAL ENVIRONMENT
# ======================================================

# 1️⃣ Virtual environment yaratish (Terminalda bajariladi):
# ------------------------------------------------------
# python -m venv venv
# venv\Scripts\activate        # (Windows)
# source venv/bin/activate     # (Mac/Linux)
# pip install numpy requests pandas

# ======================================================
# 2️⃣ Custom Modules
# ======================================================

# --- math_operations.py ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


# --- string_utils.py ---
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


# ======================================================
# 3️⃣ Custom Packages
# ======================================================

# --- geometry/__init__.py ---
# (bo‘sh qoldiriladi yoki izoh yoziladi)

# --- geometry/circle.py ---
import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

def calculate_circumference(radius):
    return 2 * math.pi * radius


# --- file_operations/__init__.py ---
# (bo‘sh qoldiriladi yoki izoh yoziladi)

# --- file_operations/file_reader.py ---
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."


# --- file_operations/file_writer.py ---
def write_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return "File written successfully."
    except Exception as e:
        return f"Error writing file: {e}"


# ======================================================
# 4️⃣ main.py — Test qilish
# ======================================================

if __name__ == "__main__":
    # Math test
    print("Add:", add(5, 3))
    print("Subtract:", subtract(5, 3))
    print("Multiply:", multiply(5, 3))
    print("Divide:", divide(10, 2))

    # String test
    text = "Hello World"
    print("Reversed string:", reverse_string(text))
    print("Vowel count:", count_vowels(text))

    # Geometry test
    radius = 5
    print("Area:", calculate_area(radius))
    print("Circumference:", calculate_circumference(radius))

    # File operations test
    file_path = "test.txt"
    print(write_file(file_path, "Hello Abdulaziz!"))
    print(read_file(file_path))
