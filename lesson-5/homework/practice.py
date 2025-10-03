# ==============================
# 1. Leap Year Function
# ==============================

def is_leap(year):
    # Kiritilgan yil kabisa yili ekanligini tekshiradi
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# test
print(is_leap(2000))   # True
print(is_leap(1900))   # False
print(is_leap(2024))   # True
print(is_leap(2023))   # False



# ==============================
# 2. Conditional Statements Exercise
# ==============================

n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")



# ==============================
# 3. Even Numbers Between a and b
# ==============================

# --- Solution 1 (with if-else) ---
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a % 2 != 0:   # agar a toq bo‘lsa, keyingi juftdan boshlanadi
    a = a + 1
if b % 2 != 0:   # agar b toq bo‘lsa, oldingi juftgacha olinadi
    b = b - 1

# range ishlatib, list yaratish
evens1 = list(range(a, b+1, 2))
print("Even numbers (solution 1):", evens1)


# --- Solution 2 (without if-else) ---
# max() va min() bilan qisqa yechim
evens2 = list(range(a + a % 2, b - b % 2 + 1, 2))
print("Even numbers (solution 2):", evens2)
