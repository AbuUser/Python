import numpy as np

# ============================================================
# Lesson 16 — NumPy Exercises
# ============================================================

# 1. Convert List to 1D Array
print("1. Convert List to 1D Array")
lst = [12.23, 13.32, 100, 36.32]
arr1 = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr1, "\n")

# 2. Create 3x3 Matrix (values from 2 to 10)
print("2. Create 3x3 Matrix (2 to 10)")
arr2 = np.arange(2, 11).reshape(3,3)  # 2..10, reshaped 3x3
print(arr2, "\n")

# 3. Null Vector (10) & Update Sixth Value
print("3. Null Vector (size 10) & update sixth value")
arr3 = np.zeros(10)
print("Original:", arr3)
arr3[5] = 11  # index starts at 0, sixth value = index 5
print("Updated sixth value to 11:", arr3, "\n")

# 4. Array from 12 to 38
print("4. Array from 12 to 38")
arr4 = np.arange(12, 38)
print(arr4, "\n")

# 5. Convert Array to Float Type
print("5. Convert Array to Float Type")
arr5 = np.array([1,2,3,4])
print("Original array:", arr5)
arr5_float = arr5.astype(float)
print("Converted to float:", arr5_float, "\n")

# 6. Celsius to Fahrenheit Conversion
print("6. Celsius to Fahrenheit Conversion")
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = (celsius * 9/5) + 32
print("Values in Celsius:", celsius)
print("Values converted to Fahrenheit:", fahrenheit, "\n")

# 7. Append Values to Array
print("7. Append Values to Array")
arr7 = np.array([10, 20, 30])
to_append = [40, 50, 60, 70, 80, 90]
arr7_appended = np.append(arr7, to_append)
print("Original array:", arr7)
print("After appending:", arr7_appended, "\n")

# 8. Array Statistical Functions
print("8. Array Statistical Functions")
arr8 = np.random.rand(10)  # 10 random elements between 0 and 1
mean8 = np.mean(arr8)
median8 = np.median(arr8)
std8 = np.std(arr8)
print("Random array:", arr8)
print("Mean:", mean8)
print("Median:", median8)
print("Standard Deviation:", std8, "\n")

# 9. Find min and max in 10x10 array
print("9. Find min and max in 10x10 array")
arr9 = np.random.rand(10,10)
min9 = np.min(arr9)
max9 = np.max(arr9)
print("10x10 Random Array:\n", arr9)
print("Minimum value:", min9)
print("Maximum value:", max9, "\n")

# 10. Create 3x3x3 Array with random values
print("10. 3x3x3 Random Array")
arr10 = np.random.rand(3,3,3)
print(arr10)
