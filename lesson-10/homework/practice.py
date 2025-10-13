# ======================== Lesson-10: OOP Projects ========================
# Author: Abdulaziz
# Date: 2025-10-13
# Topic: ToDo List, Blog System, Banking System
# ==========================================================================

# =============================== PROJECT 1 ===============================
#                      📝 ToDo List Application
# ==========================================================================

from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✅ Completed" if self.completed else "❌ Incomplete"
        return f"Task: {self.title} | Due: {self.due_date} | {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"'{title}' marked as complete.")
                return
        print("Task not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        found = False
        for task in self.tasks:
            if not task.completed:
                print(task)
                found = True
        if not found:
            print("All tasks are completed!")

# --- Test Project 1 ---
todo = ToDoList()
todo.add_task(Task("Math HW", "Solve 20 equations", "2025-10-14"))
todo.add_task(Task("Grocery", "Buy fruits and bread", "2025-10-15"))
todo.list_all_tasks()
todo.mark_task_complete("Math HW")
todo.list_incomplete_tasks()


# =============================== PROJECT 2 ===============================
#                      📰 Simple Blog System
# ==========================================================================

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date = datetime.now()

    def __str__(self):
        return f"[{self.date.strftime('%Y-%m-%d %H:%M')}] {self.title} by {self.author}\n{self.content}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("No posts yet.")
        for post in self.posts:
            print(post)
            print("-" * 40)

    def display_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author == author:
                print(post)
                print("-" * 40)
                found = True
        if not found:
            print(f"No posts found by {author}")

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f"'{title}' deleted.")
                return
        print("Post not found.")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                print(f"'{title}' updated.")
                return
        print("Post not found.")

    def latest_posts(self, n=3):
        for post in self.posts[-n:]:
            print(post)
            print("-" * 40)

# --- Test Project 2 ---
blog = Blog()
blog.add_post(Post("OOP in Python", "Today we learned classes", "Abdulaziz"))
blog.add_post(Post("GitHub Tips", "Push and Pull Commands", "Ali"))
blog.list_posts()
blog.display_by_author("Abdulaziz")
blog.edit_post("OOP in Python", "We also learned about inheritance.")
blog.latest_posts(2)


# =============================== PROJECT 3 ===============================
#                      🏦 Simple Banking System
# ==========================================================================

class Account:
    def __init__(self, number, holder, balance=0):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def __str__(self):
        return f"Account {self.number} | Holder: {self.holder} | Balance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, number):
        for acc in self.accounts:
            if acc.number == number:
                return acc
        return None

    def transfer(self, from_num, to_num, amount):
        from_acc = self.find_account(from_num)
        to_acc = self.find_account(to_num)
        if from_acc and to_acc and from_acc.balance >= amount:
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            print(f"Transferred {amount} from {from_num} to {to_num}")
        else:
            print("Transfer failed.")

    def list_accounts(self):
        for acc in self.accounts:
            print(acc)

# --- Test Project 3 ---
bank = Bank()
a1 = Account(101, "Abdulaziz", 1000)
a2 = Account(102, "Ali", 500)
bank.add_account(a1)
bank.add_account(a2)
bank.list_accounts()
a1.deposit(200)
a2.withdraw(100)
bank.transfer(101, 102, 300)
bank.list_accounts()
