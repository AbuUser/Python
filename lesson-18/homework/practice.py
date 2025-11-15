import pandas as pd

# ============================================================
# Homework 18 — Pandas Exercises
# ============================================================

# ---------------- StackOverflow Questions ----------------
df = pd.read_csv('task\\stackoverflow_qa.csv')

# 1. Questions created before 2014
before_2014 = df[df['CreationDate'] < '2014-01-01']
print("Questions created before 2014:\n", before_2014, "\n")

# 2. Questions with score > 50
score_gt_50 = df[df['Score'] > 50]
print("Questions with score > 50:\n", score_gt_50, "\n")

# 3. Questions with score between 50 and 100
score_50_100 = df[(df['Score'] >= 50) & (df['Score'] <= 100)]
print("Questions with score between 50 and 100:\n", score_50_100, "\n")

# 4. Questions answered by Scott Boston
answered_scott = df[df['OwnerUserDisplayName'] == 'Scott Boston']
print("Questions answered by Scott Boston:\n", answered_scott, "\n")

# 5. Questions answered by following 5 users
users_list = ['Scott Boston', 'Unutbu', 'Jon Skeet', 'Alice', 'Bob']  # misol
answered_5users = df[df['OwnerUserDisplayName'].isin(users_list)]
print("Questions answered by 5 specified users:\n", answered_5users, "\n")

# 6. Questions created between Mar-Oct 2014, answered by Unutbu, score < 5
mask = (
    (df['CreationDate'] >= '2014-03-01') &
    (df['CreationDate'] <= '2014-10-31') &
    (df['OwnerUserDisplayName'] == 'Unutbu') &
    (df['Score'] < 5)
)
specific_questions = df[mask]
print("Questions Mar-Oct 2014, answered by Unutbu, score < 5:\n", specific_questions, "\n")

# 7. Questions with score 5–10 OR view count > 10000
mask2 = ((df['Score'] >= 5) & (df['Score'] <= 10)) | (df['ViewCount'] > 10000)
questions_score_or_views = df[mask2]
print("Questions score 5–10 or views > 10000:\n", questions_score_or_views, "\n")

# 8. Questions not answered by Scott Boston
not_scott = df[df['OwnerUserDisplayName'] != 'Scott Boston']
print("Questions NOT answered by Scott Boston:\n", not_scott, "\n")


# ---------------- Titanic Data ----------------
titanic_df = pd.read_csv("task\\titanic.csv")

# 1. Female passengers in Class 1, age 20–30
female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'] >= 20) &
    (titanic_df['Age'] <= 30)
]
print("Female passengers in Class 1 aged 20–30:\n", female_class1_20_30, "\n")

# 2. Passengers who paid more than $100
fare_gt_100 = titanic_df[titanic_df['Fare'] > 100]
print("Passengers with fare > $100:\n", fare_gt_100, "\n")

# 3. Passengers who survived and were alone
survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) & 
    (titanic_df['SibSp'] == 0) & 
    (titanic_df['Parch'] == 0)
]
print("Passengers who survived and were alone:\n", survived_alone, "\n")

# 4. Passengers embarked from 'C' and paid > $50
embarked_c_fare_gt50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
print("Passengers embarked from 'C' and fare > $50:\n", embarked_c_fare_gt50, "\n")

# 5. Passengers with siblings/spouses AND parents/children aboard
siblings_parents = titanic_df[
    (titanic_df['SibSp'] > 0) & 
    (titanic_df['Parch'] > 0)
]
print("Passengers with siblings/spouses and parents/children aboard:\n", siblings_parents, "\n")

# 6. Passengers aged 15 or younger who didn't survive
age_le15_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]
print("Passengers aged ≤15 who did not survive:\n", age_le15_not_survived, "\n")

# 7. Passengers with cabin and fare > $200
cabin_fare_gt200 = titanic_df[
    titanic_df['Cabin'].notnull() &
    (titanic_df['Fare'] > 200)
]
print("Passengers with cabin and fare > $200:\n", cabin_fare_gt200, "\n")

# 8. Passengers with odd-numbered PassengerId
odd_id_passengers = titanic_df[titanic_df['PassengerId'] % 2 != 0]
print("Passengers with odd-numbered PassengerId:\n", odd_id_passengers, "\n")

# 9. Passengers with unique ticket numbers
unique_ticket_passengers = titanic_df[titanic_df.duplicated(subset='Ticket', keep=False) == False]
print("Passengers with unique tickets:\n", unique_ticket_passengers, "\n")

# 10. Female passengers with 'Miss' in Name and Class 1
miss_class1_female = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Pclass'] == 1)
]
print("Female passengers with 'Miss' in Name and Class 1:\n", miss_class1_female, "\n")
