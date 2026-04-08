# ================================
# SMART EXPENSE MANAGER
# ================================

import mysql.connector
from abc import ABC, abstractmethod
from functools import reduce

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xii031990",   
    database="expense_db"
)

cursor = conn.cursor()
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


class User(AbstractUser):
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_details(self):
        return f"User ID: {self.__user_id}, Name: {self.__name}"


class Expense(User):
    def __init__(self, user_id, name, amount, category, description, date):
        super().__init__(user_id, name)
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def get_details(self):   
        return f"{super().get_details()}, Amount: {self.amount}, Category: {self.category}, Date: {self.date}"



def add_user():
    name = input("Enter name: ")
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    print(" User added!")



def add_expense():
    user_id = int(input("Enter user ID: "))
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")

    values = """
    INSERT INTO expenses (user_id, amount, category, description, date)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(values, (user_id, amount, category, description, date))
    conn.commit()
    print(" Expense added!")



def view_expenses():
    user_id = int(input("Enter user ID: "))

    que = """
    SELECT u.name, e.amount, e.category, e.description, e.date
    FROM users u
    JOIN expenses e ON u.user_id = e.user_id
    WHERE u.user_id = %s
    """

    cursor.execute(que, (user_id,))
    data = cursor.fetchall()

    print("\n Expenses:")
    for row in data:
        print(row)

    return data



def filter_expenses(data):
    category = input("Enter category to filter: ")

    filtered = list(filter(lambda x: x[2] == category, data))

    print("\n Filtered Data:")
    for item in filtered:
        print(item)



def total_expense(data):
    amounts = list(map(lambda x: x[1], data))

    if not amounts:
        print("No data")
        return

    total = reduce(lambda x, y: x + y, amounts)
    print(" Total Expense:", total)



def category_wise(data):
    categories = set([x[2] for x in data])

    result = {cat: sum([x[1] for x in data if x[2] == cat]) for cat in categories}

    print("\n Category Wise:")
    for k, v in result.items():
        print(k, ":", v)



def monthly_report(data):
    report = {}

    for d in data:
        month = str(d[4])[:7]
        report[month] = report.get(month, 0) + d[1]

    print("\n Monthly Report:")
    for k, v in report.items():
        print(k, ":", v)



def highest_expense(data):
    if not data:
        print("No data")
        return

    highest = reduce(lambda x, y: x if x[1] > y[1] else y, data)
    print("\n Highest Expense:", highest)



def smart_insight(data):
    category_totals = {}

    for d in data:
        category_totals[d[2]] = category_totals.get(d[2], 0) + d[1]

    if not category_totals:
        print("No data")
        return

    highest = max(category_totals, key=category_totals.get)

    print(f"\n You are spending too much on {highest}")



def update_expense():
    exp_id = int(input("Enter expense ID: "))
    amount = float(input("Enter new amount: "))

    cursor.execute("UPDATE expenses SET amount=%s WHERE exp_id=%s", (amount, exp_id))
    conn.commit()

    print(" Updated!")



def delete_expense():
    exp_id = int(input("Enter expense ID: "))

    cursor.execute("DELETE FROM expenses WHERE exp_id=%s", (exp_id,))
    conn.commit()

    print(" Deleted!")



def menu():
    data = []

    while True:
        print("\n===== SMART EXPENSE MANAGER =====")
        print("1. Add User")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Filter Expenses")
        print("5. Total Expense")
        print("6. Category Wise")
        print("7. Monthly Report")
        print("8. Highest Expense")
        print("9. Smart Insight")
        print("10. Update Expense")
        print("11. Delete Expense")
        print("0. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_user()
        elif choice == 2:
            add_expense()
        elif choice == 3:
            data = view_expenses()
        elif choice == 4:
            filter_expenses(data)
        elif choice == 5:
            total_expense(data)
        elif choice == 6:
            category_wise(data)
        elif choice == 7:
            monthly_report(data)
        elif choice == 8:
            highest_expense(data)
        elif choice == 9:
            smart_insight(data)
        elif choice == 10:
            update_expense()
        elif choice == 11:
            delete_expense()
        elif choice == 0:
            print(" Exiting...")
            break
        else:
            print("Invalid choice!")


menu()