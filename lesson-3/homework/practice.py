# ==========================
# Lesson-3: List and Tuple Exercises
# ==========================

# 1. Create and Access List Elements
fruits = ["apple", "banana", "cherry", "grape", "orange"]
print("1. Third fruit:", fruits[2])
print()

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("2. Concatenated list:", merged_list)
print()

# 3. Extract Elements from a List
nums = [10, 20, 30, 40, 50]
first = nums[0]
middle = nums[len(nums)//2]
last = nums[-1]
new_list = [first, middle, last]
print("3. New list:", new_list)
print()

# 4. Convert List to Tuple
movies = ["Inception", "Titanic", "Avengers", "Gladiator", "Joker"]
movies_tuple = tuple(movies)
print("4. Movies tuple:", movies_tuple)
print()

# 5. Check Element in a List
cities = ["London", "Paris", "New York", "Tokyo"]
print("5. Is Paris in cities?", "Paris" in cities)
print()

# 6. Duplicate a List Without Using Loops
numbers = [1, 2, 3]
dup_numbers = numbers * 2
print("6. Duplicated list:", dup_numbers)
print()

# 7. Swap First and Last Elements of a List
nums = [100, 200, 300, 400]
nums[0], nums[-1] = nums[-1], nums[0]
print("7. Swapped list:", nums)
print()

# 8. Slice a Tuple
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("8. Tuple slice (3 to 7):", t[3:8])
print()

# 9. Count Occurrences in a List
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
print("9. Count of 'blue':", colors.count("blue"))
print()

# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger")
print("10. Index of lion:", animals.index("lion"))
print()

# 11. Merge Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged_tuple = t1 + t2
print("11. Merged tuple:", merged_tuple)
print()

# 12. Find the Length of a List and Tuple
lst = [10, 20, 30]
tpl = (100, 200, 300, 400)
print("12. Length of list:", len(lst))
print("12. Length of tuple:", len(tpl))
print()

# 13. Convert Tuple to List
tpl = (5, 10, 15, 20, 25)
tpl_to_list = list(tpl)
print("13. Converted list:", tpl_to_list)
print()

# 14. Find Maximum and Minimum in a Tuple
tpl = (12, 45, 2, 89, 34)
print("14. Max:", max(tpl))
print("14. Min:", min(tpl))
print()

# 15. Reverse a Tuple
words = ("Python", "is", "fun")
print("15. Reversed tuple:", words[::-1])
