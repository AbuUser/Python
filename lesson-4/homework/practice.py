# ==============================
#   Dictionary Exercises
# ==============================

# 1. Sort a Dictionary by Value
my_dict = {2: 30, 1: 10, 3: 20}
print("Original dictionary:", my_dict)

# ascending
asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Ascending:", asc)

# descending
desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending:", desc)


# 2. Add a Key to a Dictionary
sample_dict = {0: 10, 1: 20}
print("Before:", sample_dict)
sample_dict[2] = 30
print("After:", sample_dict)


# 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dic = {}
for d in (dic1, dic2, dic3):
    new_dic.update(d)
print("Concatenated dictionary:", new_dic)


# 4. Generate a Dictionary with Squares
n = 5
squares = {}
for x in range(1, n+1):
    squares[x] = x * x
print("Squares (1 to 5):", squares)


# 5. Dictionary of Squares (1 to 15)
sq_dict = {}
for x in range(1, 16):
    sq_dict[x] = x * x
print("Squares (1 to 15):", sq_dict)


# ==============================
#   Set Exercises
# ==============================

# 1. Create a Set
my_set = {1, 2, 3}
print("Created set:", my_set)


# 2. Iterate Over a Set
for item in my_set:
    print("Item:", item)


# 3. Add Member(s) to a Set
my_set.add(4)
print("After adding 4:", my_set)
my_set.update([5, 6])
print("After adding multiple items:", my_set)


# 4. Remove Item(s) from a Set
my_set.remove(6)   # agar mavjud bo‘lsa
print("After removing 6:", my_set)


# 5. Remove an Item if Present in the Set
if 5 in my_set:
    my_set.remove(5)
print("Final set:", my_set)
