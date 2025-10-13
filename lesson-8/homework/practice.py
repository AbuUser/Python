# ===============================
# 📘 Homework: Python Exception Handling & File I/O
# ===============================

# 1. ZeroDivisionError
try:
    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))
    print("Natija:", a / b)
except ZeroDivisionError:
    print("❌ Nolga bo‘lish mumkin emas!")

# 2. ValueError
try:
    n = int(input("Butun son kiriting: "))
    print("Siz kiritdingiz:", n)
except ValueError:
    print("❌ Bu butun son emas!")

# 3. FileNotFoundError
try:
    file = open("fayl.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("❌ Fayl topilmadi!")

# 4. TypeError
try:
    x = input("1-sonni kiriting: ")
    y = input("2-sonni kiriting: ")
    s = int(x) + int(y)
    print("Yig‘indi:", s)
except TypeError:
    print("❌ Faqat raqam kiritish kerak!")
except ValueError:
    print("❌ Noto‘g‘ri kiritish!")

# 5. PermissionError
try:
    with open("/system/secret.txt", "r") as f:
        print(f.read())
except PermissionError:
    print("❌ Ruxsat yo‘q!")

# 6. IndexError
try:
    lst = [10, 20, 30]
    i = int(input("Index kiriting: "))
    print(lst[i])
except IndexError:
    print("❌ Bunday index yo‘q!")

# 7. KeyboardInterrupt
try:
    num = input("Son kiriting (Ctrl+C bosmang): ")
    print("Siz kiritdingiz:", num)
except KeyboardInterrupt:
    print("\n❌ Kiritish bekor qilindi!")

# 8. ArithmeticError
try:
    a = int(input("a = "))
    b = int(input("b = "))
    c = a / b
    print("Natija:", c)
except ArithmeticError:
    print("❌ Arifmetik xatolik!")

# 9. UnicodeDecodeError
try:
    with open("matn.txt", "r", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("❌ Kodlash muammosi!")

# 10. AttributeError
try:
    x = 10
    x.append(5)
except AttributeError:
    print("❌ Bunday atribut yo‘q!")

# ===============================
# 📗 Python File I/O
# ===============================

# 1. Faylni to‘liq o‘qish
with open("data.txt", "r") as f:
    print(f.read())

# 2. Birinchi n qatorni o‘qish
n = 3
with open("data.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

# 3. Faylga qo‘shish
with open("data.txt", "a") as f:
    f.write("\nYangi qator qo‘shildi")
with open("data.txt", "r") as f:
    print(f.read())

# 4. Oxirgi n qatorni o‘qish
n = 2
with open("data.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

# 5. Faylni listga o‘qish
with open("data.txt", "r") as f:
    lines = f.readlines()
print(lines)

# 6. Faylni bitta o‘zgaruvchiga o‘qish
with open("data.txt", "r") as f:
    content = f.read()
print(content)

# 7. Faylni massivga saqlash
arr = []
with open("data.txt", "r") as f:
    for line in f:
        arr.append(line.strip())
print(arr)

# 8. Eng uzun so‘z(lar)ni topish
with open("data.txt", "r") as f:
    words = f.read().split()
longest = max(words, key=len)
print("Eng uzun so‘z:", longest)

# 9. Qatorlar soni
with open("data.txt", "r") as f:
    count = sum(1 for line in f)
print("Qatorlar soni:", count)

# 10. So‘zlar soni
with open("data.txt", "r") as f:
    words = f.read().replace(",", " ").split()
print("So‘zlar soni:", len(words))

# 11. Fayl hajmi
import os
size = os.path.getsize("data.txt")
print("Fayl hajmi:", size, "bayt")

# 12. Listni faylga yozish
my_list = ["olma", "nok", "banan"]
with open("fruits.txt", "w") as f:
    for item in my_list:
        f.write(item + "\n")

# 13. Fayl nusxasini olish
with open("data.txt", "r") as s, open("copy.txt", "w") as d:
    d.write(s.read())

# 14. 2 fayl qatorlarini birlashtirish
with open("data.txt") as f1, open("fruits.txt") as f2:
    for a, b in zip(f1, f2):
        print(a.strip(), b.strip())

# 15. Tasodifiy qator o‘qish
import random
with open("data.txt") as f:
    lines = f.readlines()
    print(random.choice(lines))

# 16. Fayl yopilganini tekshirish
f = open("data.txt")
print("Yopildimi?", f.closed)
f.close()
print("Yopildimi?", f.closed)

# 17. Yangi qatordan tozalash
with open("data.txt", "r") as f:
    clean = [line.strip() for line in f]
print(clean)

# 18. So‘zlar sonini hisoblash
with open("data.txt") as f:
    text = f.read().replace(",", " ")
    print("So‘zlar soni:", len(text.split()))

# 19. Belgilarni yig‘ish
chars = []
for filename in ["data.txt", "fruits.txt"]:
    with open(filename) as f:
        chars.extend(list(f.read()))
print(chars)

# 20. A.txt dan Z.txt gacha fayl yaratish
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"Bu {letter} fayli")

# 21. Har qatorga n ta harf yozish
n = 5
alphabet = string.ascii_lowercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(alphabet), n):
        f.write(alphabet[i:i+n] + "\n")
