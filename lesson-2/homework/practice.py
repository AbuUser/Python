# ==========================
# 2-dars uyga vazifa
# ==========================

# 1. Age Calculator
# Foydalanuvchidan ismi va tug'ilgan yilini olib, yoshini hisoblash
name = input("Ismingizni kiriting: ")
yil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2025 - yil
print("Salom", name + "!", "Sizning yoshingiz:", yosh)
print()

# 2. Extract Car Names
# Berilgan matndan mashina nomini ajratib olish
txt = 'LMaasleitbtui'
car = txt[1] + txt[3] + txt[5]   # "M" + "e" + "r" = "Mer"
car += txt[7] + txt[9] + txt[11] # "c" + "e" + "d" = "ced"
print("2-mashina nomi:", car)    # Mercedes
print()

# 3. Extract Car Names
txt = 'MsaatmiazD'
car2 = txt[0] + txt[2] + txt[4] + txt[6] + txt[8]  # "M" + "a" + "t" + "a" + "z" = "Mataz"
car2 += txt[9]                                     # + "D" = "MatazD" → Mazda
print("3-mashina nomi:", car2)
print()

# 4. Extract Residence Area
txt = "I'am John. I am from London"
qayerdan = txt.split("from ")[1]
print("4-yashash joyi:", qayerdan)
print()

# 5. Reverse String
s = input("Matn kiriting: ")
print("Teskari tartibda:", s[::-1])
print()

# 6. Count Vowels
s = input("Matn kiriting (unlilarni sanash): ")
vowels = "aeiouAEIOU"
soni = 0
for ch in s:
    if ch in vowels:
        soni += 1
print("Unli harflar soni:", soni)
print()

# 7. Find Maximum Value
sonlar = [12, 45, 67, 2, 99, 23]
maxi = sonlar[0]
for x in sonlar:
    if x > maxi:
        maxi = x
print("Ro'yxatdagi eng katta qiymat:", maxi)
print()

# 8. Check Palindrome
word = input("So'z kiriting: ")
if word == word[::-1]:
    print("Bu so'z palindrom")
else:
    print("Bu so'z palindrom emas")
print()

# 9. Extract Email Domain
email = input("Email kiriting: ")
domain = email.split("@")[1]
print("Email domainingiz:", domain)
print()

# 10. Generate Random Password
import random
import string
belgilar = string.ascii_letters + string.digits + "!@#$%^&*"
parol = "".join(random.choice(belgilar) for i in range(8))
print("Tasodifiy parol:", parol)
