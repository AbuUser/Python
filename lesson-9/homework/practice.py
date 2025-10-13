# ============================
# 📘 Homework — Lesson 9: OOP
# ============================

# 1. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

c = Circle(5); print("1) Circle — Area:", c.area(), "Perimeter:", c.perimeter())

# 2. Person Class
from datetime import date

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def get_age(self):
        return date.today().year - self.birth_year

p = Person("Ali", "Uzbekistan", 2000); print("2) Person — Age:", p.get_age())

# 3. Calculator Class
class Calculator:
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b): return a / b if b != 0 else "Division by zero!"

calc = Calculator(); print("3) Calculator — Add:", calc.add(5, 3), "Div:", calc.div(10, 2))

# 4. Shape and Subclasses
class Shape:
    def area(self): pass
    def perimeter(self): pass

class CircleShape(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * (self.r ** 2)
    def perimeter(self): return 2 * 3.14 * self.r

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5

class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2
    def perimeter(self): return 4 * self.s

sq = Square(4); print("4) Square — Area:", sq.area(), "Perimeter:", sq.perimeter())

# 5. Binary Search Tree Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self): self.root = None

    def insert(self, value):
        if not self.root: self.root = Node(value)
        else: self._insert(self.root, value)
    def _insert(self, cur, value):
        if value < cur.value:
            if cur.left: self._insert(cur.left, value)
            else: cur.left = Node(value)
        else:
            if cur.right: self._insert(cur.right, value)
            else: cur.right = Node(value)
    def search(self, value):
        return self._search(self.root, value)
    def _search(self, cur, value):
        if not cur: return False
        if cur.value == value: return True
        if value < cur.value: return self._search(cur.left, value)
        return self._search(cur.right, value)

bst = BST(); bst.insert(5); bst.insert(3); bst.insert(7); print("5) BST — Search 3:", bst.search(3))

# 6. Stack Data Structure
class Stack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None

st = Stack(); st.push(1); st.push(2); print("6) Stack — Pop:", st.pop())

# 7. Linked List Data Structure
class LLNode:
    def __init__(self, data): self.data = data; self.next = None

class LinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        new_node = LLNode(data)
        if not self.head: self.head = new_node
        else:
            cur = self.head
            while cur.next: cur = cur.next
            cur.next = new_node

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def delete(self, data):
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if prev: prev.next = cur.next
                else: self.head = cur.next
                return
            prev = cur
            cur = cur.next

ll = LinkedList(); ll.insert(10); ll.insert(20); ll.delete(10); print("7) LinkedList — Display:", end=" "); ll.display()

# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self): self.items = {}
    def add_item(self, name, price): self.items[name] = self.items.get(name, 0) + price
    def remove_item(self, name): self.items.pop(name, None)
    def total(self): return sum(self.items.values())

cart = ShoppingCart(); cart.add_item("apple", 3); cart.add_item("banana", 2); print("8) Cart — Total:", cart.total())

# 9. Stack with Display
class DisplayStack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def display(self): print("Stack content:", self.items)

ds = DisplayStack(); ds.push(1); ds.push(2); ds.display()

# 10. Queue Data Structure
class Queue:
    def __init__(self): self.items = []
    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else None

q = Queue(); q.enqueue(5); q.enqueue(10); print("10) Queue — Dequeue:", q.dequeue())

# 11. Bank Class
class Bank:
    def __init__(self): self.accounts = {}
    def create_account(self, name, balance=0): self.accounts[name] = balance
    def deposit(self, name, amount): self.accounts[name] += amount
    def withdraw(self, name, amount):
        if self.accounts[name] >= amount: self.accounts[name] -= amount
        else: print("Insufficient funds")
    def balance(self, name): return self.accounts.get(name, 0)

bank = Bank(); bank.create_account("Ali", 100); bank.deposit("Ali", 50); bank.withdraw("Ali", 30)
print("11) Bank — Balance Ali:", bank.balance("Ali"))
