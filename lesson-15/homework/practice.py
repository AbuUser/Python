import sqlite3

# ============================================================
# Lesson 15 — Review Exercises
# Roster jadvali yaratish, ma’lumot kiritish, update va query
# ============================================================

# 1. Bazani yaratish va Roster jadvalini yaratish
conn = sqlite3.connect("lesson15.db")  # lesson15.db nomli fayl yaratiladi
c = conn.cursor()

# Jadval yaratish (agar mavjud bo‘lmasa)
c.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2. Ma’lumotlarni kiritish
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

# Jadval bo‘sh bo‘lsa, ma’lumot qo‘shish
c.execute("SELECT COUNT(*) FROM Roster")
count = c.fetchone()[0]
if count == 0:
    c.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", roster_data)
    conn.commit()

# 3. Jadzia Daxni Ezri Dax ga o‘zgartirish
c.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
conn.commit()

# 4. Bajoranlarni Name va Age bilan chiqarish
c.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
rows = c.fetchall()

print("Bajoranlar jadvali:")
for row in rows:
    print(f"Name: {row[0]}, Age: {row[1]}")

# Bog‘lanishni yopish
conn.close()
