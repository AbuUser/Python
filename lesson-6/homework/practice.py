# Lesson-5 Homework

# 1. Modify String with Underscores
txt = "abcabcabcdeabcdefabcdefg"
res = ""
count = 0
skip = False
vowels = "aeiou"

for i, ch in enumerate(txt):
    res += ch
    count += 1
    if skip:
        skip = False
        continue
    if count == 3:
        if ch in vowels:
            skip = True
        elif i != len(txt) - 1:
            res += "_"
        count = 0
print(res)   # example: abc_abcab_cdeabcd_efabcdef_g


# 2. Integer Squares Exercise
n = 5
for i in range(n):
    print(i ** 2)


# 3. Loop-Based Exercises

# Ex1: Print first 10 natural numbers
i = 1
while i <= 10:
    print(i)
    i += 1

# Ex2: Pattern
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Ex3: Sum of numbers 1..n
n = 10
s = 0
for i in range(1, n+1):
    s += i
print("Sum is:", s)

# Ex4: Multiplication table
num = 2
for i in range(1, 11):
    print(num * i)

# Ex5: Display numbers from list
numbers = [12, 75, 150, 180, 145, 525, 50]
for x in numbers:
    if x > 500:
        break
    if x % 5 == 0 and x <= 150:
        print(x)

# Ex6: Count digits
num = 75869
print("Digits:", len(str(num)))

# Ex7: Reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Ex8: List in reverse
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

# Ex9: Numbers from -10 to -1
for i in range(-10, 0):
    print(i)

# Ex10: Done after loop
for i in range(5):
    print(i)
print("Done!")

# Ex11: Prime numbers in range
start, end = 25, 50
print("Prime numbers between 25 and 50:")
for num in range(start, end+1):
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            print(num)

# Ex12: Fibonacci sequence up to 10 terms
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(10):
    print(a, end=" ")
    a, b = b, a+b
print()

# Ex13: Factorial
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! =", fact)


# 4. Return Uncommon Elements of Lists
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
res = []
for x in list1:
    if x in list2:
        list2.remove(x)
    else:
        res.append(x)
res.extend(list2)
print(res)   # -> [2, 2, 5]


# uncommon elements of lists
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

res = []

# list1 elementlari bo'lib list2 da yo'q bo'lganlarini olish
for x in list1:
    if x not in list2:
        res.append(x)
    else:
        list2.remove(x)   # umumiy elementni olib tashlaymiz

# endi qolgan list2 elementlarini ham qo'shamiz
res.extend(list2)

print(res)   # -> [2, 2, 5]

txt = "abcabcdabcdeabcdefabcdefg"
result = ""
count = 0
skip_next = False   # unli yoki oldidan _ qo'yilgan holatda belgini keyinga surish

vowels = "aeiou"

for i, ch in enumerate(txt):
    result += ch
    count += 1

    if skip_next:
        skip_next = False
        continue

    if count == 3:
        if ch in vowels:
            skip_next = True   # unli bo'lsa keyingi belgidan keyin qo'yiladi
        elif result[-2:] == "_"+ch:  
            skip_next = True   # oldingi belgidan keyin _ qo'yilgan bo'lsa
        elif i != len(txt) - 1:   # oxirgi belgi emas
            result += "_"
        count = 0

print(result)



