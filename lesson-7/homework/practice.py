# Lesson-7 Homeworks
# Author: Abdulaziz
# Date: 2025-10-03
# Daftar uslubi: har bir topshiriq yonma-yon, tartib bilan yozilgan.

# ==============================
# MAP va FILTER tushunchasi
# ==============================
# map(func, iterable) -> berilgan funksiya elementlarga qo'llanadi
# filter(func, iterable) -> shartni qanoatlantirgan elementlar saralanadi

numbers = [1, 2, 3, 4, 5] ; squares = list(map(lambda x: x**2, numbers)) ; print("map misol:", squares)  # [1, 4, 9, 16, 25]
nums = [10, 15, 20, 25, 30] ; evens = list(filter(lambda x: x % 2 == 0, nums)) ; print("filter misol:", evens)  # [10, 20, 30]

# ==============================
# 1-masala: is_prime(n)
# ==============================
def is_prime(n: int) -> bool:
    """n > 0 bo'lgan sonning tub yoki yo'qligini aniqlaydi"""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print("is_prime(4) =", is_prime(4)) ; print("is_prime(7) =", is_prime(7))

# ==============================
# 2-masala: digit_sum(k)
# ==============================
def digit_sum(k: int) -> int:
    """k sonining raqamlari yig'indisini hisoblaydi"""
    return sum(int(d) for d in str(k))

print("digit_sum(24) =", digit_sum(24)) ; print("digit_sum(502) =", digit_sum(502))

# ==============================
# 3-masala: powers_of_two(limit)
# ==============================
def powers_of_two(limit: int):
    """limit dan oshmaydigan barcha 2 ning darajalarini chiqaradi"""
    power = 1
    while power * 2 <= limit:
        power *= 2 ; print(power, end=" ")
    print()

powers_of_two(10)  # 2 4 8
