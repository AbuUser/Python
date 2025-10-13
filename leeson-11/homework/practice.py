# ==============================
# 1. VIRTUAL ENVIRONMENT
# ==============================
# Terminalda quyidagilarni bajarish kerak:
# python -m venv venv
# venv\Scripts\activate        (Windows)
# source venv/bin/activate     (Mac/Linux)
# pip install requests numpy

# ==============================
# 2. CUSTOM MODULES
# ==============================

# ---- math_operations.py ----
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

# ---- string_utils.py ----
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


# ==============================
# 3. CUSTOM PACKAGES
# ==============================

# ---- geometry/circle.py ----
import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

def calculate_circumference(radius):
    return 2 * math.pi * radius

# ---- file_operations/file_reader.py ----
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found!"

# ---- file_operations/file_writer.py ----
def write_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return "File written successfully."
    except Exception as e:
        return f"Error writing file: {e}"


# ==============================
# 4. TEST (main.py)
# ==============================

# Math operations
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))
print("Multiply:", multiply(10, 5))
print("Divide:", divide(10, 5))

# String utils
text = "Hello World"
print("Reversed:", reverse_string(text))
print("Vowel count:", count_vowels(text))

# Geometry
radius = 5
print("Circle area:", calculate_area(radius))
print("Circle circumference:", calculate_circumference(radius))

# File operations
file_path = "test.txt"
print(write_file(file_path, "This is a test content."))
print("File content:", read_file(file_path))
