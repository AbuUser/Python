# ================================================
# 📚 LESSON 12 — PYTHON THREADING HOMEWORK
# Exercise 1 & 2
# ================================================

import threading
from math import sqrt
from collections import Counter

# ==================================================
# 🧮 Exercise 1: Threaded Prime Number Checker
# ==================================================

# Prime number tekshiruvchi funksiya
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Har bir thread ishlaydigan funksiya
def prime_worker(start, end, result_list):
    for num in range(start, end + 1):
        if is_prime(num):
            result_list.append(num)

def threaded_prime_checker(start_range, end_range, num_threads=4):
    threads = []
    result = []
    step = (end_range - start_range + 1) // num_threads

    for i in range(num_threads):
        sub_start = start_range + i * step
        sub_end = sub_start + step - 1 if i != num_threads - 1 else end_range
        t = threading.Thread(target=prime_worker, args=(sub_start, sub_end, result))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return sorted(result)


# ==================================================
# 📂 Exercise 2: Threaded File Processing (Word Count)
# ==================================================

def file_worker(lines, counter_list):
    c = Counter()
    for line in lines:
        words = line.strip().lower().split()
        c.update(words)
    counter_list.append(c)

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    threads = []
    counters = []
    total_lines = len(lines)
    step = total_lines // num_threads

    for i in range(num_threads):
        sub_start = i * step
        sub_end = (i + 1) * step if i != num_threads - 1 else total_lines
        t = threading.Thread(target=file_worker, args=(lines[sub_start:sub_end], counters))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_counter = Counter()
    for c in counters:
        total_counter.update(c)

    return total_counter


# ==================================================
# 🧪 MAIN — Test qilish
# ==================================================
if __name__ == "__main__":
    # ✅ Test 1: Prime checker
    print("🔹 Prime numbers from 1 to 50:")
    primes = threaded_prime_checker(1, 50, num_threads=4)
    print(primes)

    # ✅ Test 2: File word count
    # Avval test fayl yaratamiz:
    file_path = "test_file.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Hello world\n")
        f.write("Hello Abdulaziz\n")
        f.write("Python threading example\n")
        f.write("world of python\n")

    print("\n🔹 Word Count from file:")
    result = threaded_word_count(file_path, num_threads=4)
    for word, count in result.items():
        print(f"{word}: {count}")
