# -------------------------------
# 1. Mini Project: Employee Management System
# -------------------------------
mployees=[]
def add_employee():
    employees.append({"name":input("Name:"),"age":int(input("Age:")),"role":input("Role:"),"salary":float(input("Salary:"))})
def display():
 print(employees)
def delete_employee(n): 
    global employees
    employees=[e for e in employees if e["name"]!=n]
add_employee(); display(); delete_employee(input("Delete:")); display()


# -------------------------------
# 2.Mini Project: Student Report Card
# -------------------------------
def report():
    name = input("Name: ")
    m1 = int(input("English: "))
    m2 = int(input("Maths: "))
    m3 = int(input("Science: "))
    
    total = m1 + m2 + m3
    avg = total / 3
    
    grade = "A+" if avg >= 90 else "A" if avg >= 80 else "B+" if avg >= 70 else "B" if avg >=40 else "failed"
    
    print(f"{name} | Total: {total} | Avg: {avg:.2f} | Grade: {grade}")

report()


# -------------------------------
# 3. Mini Project: Shopping Cart System
# -------------------------------

cart = [
    {"name": "Laptop", "price": 50000, "qty": 1},
    {"name": "Mouse", "price": 500, "qty": 2}
]

cart.append({"name": "Keyboard", "price": 1500, "qty": 1})

for item in cart:
    if item["name"] == "Mouse":
        cart.remove(item)

total = 0
print("Cart Items:\n")

for item in cart:
    item_total = item["price"] * item["qty"]
    total += item_total
    print(f"{item['name']} - {item['price']} x {item['qty']} = {item_total}")

print("\nTotal Bill:", total)


# -------------------------------
# 4. Mini Project: Login & User Validation
# -------------------------------

users = {
    "nitin": "1234",
    "rahul": "abcd",
    "anu": "pass"
}

username = input("enter user name:-")
password = input("enter password:-")

if username in users and users[username] == password:
    print("Login Successful ")
else:
    print("Invalid Username or Password ")




# -------------------------------
# 5.Mini Project: Unique Visitor Counte
# -------------------------------
visitors = set()

visitors.add("Nitin")
visitors.add("Rahul")
visitors.add("Anu")
visitors.add("Nitin")   

print("Visitors:", visitors)

print("Total Unique Visitors:", len(visitors))

# -------------------------------
# 6.Mini Project: String Formatter Tool
# -------------------------------

name = input("Name: ")
product = input("Product: ")

print(f"{name} bought {product}")
print(name.ljust(10, "*"))
print(name.rjust(10, "*"))
print(name.center(10, "*"))


# -------------------------------
# 7.Mini Project : Bank Account System
# -------------------------------

account = {
    "name": "Nitin",
    "balance": 1000
}


def deposit(amount):
    account["balance"] += amount
    print("Deposited:", amount)


def withdraw(amount):
    account["balance"] -= amount
    print("Withdrawn:", amount)
    

def check_balance():
    print("Account Holder:", account["name"])
    print("Balance:", account["balance"])


deposit(4000)
withdraw(300)
withdraw(2000) 
check_balance()


# -------------------------------
# 8.Mini Project: Voting System
# -------------------------------

votes = {"Alice": 0, "Bob": 0, "Charlie": 0}


votes["Alice"] += 1
votes["Bob"] += 1
votes["Alice"] += 1
votes["Charlie"] += 1
votes["Alice"] += 1


print("Votes:")
for name in votes:
    print(name, ":", votes[name])


winner = max(votes, key=votes.get)
print("Winner is:", winner)



# -------------------------------
# 9. Mini Project: Course Enrollment System
# -------------------------------

students = {
    "Nitin": ["Python", "SQL"],
    "Rahul": ["Java"]
}

students["Anu"] = ["C++", "HTML"]

students["Rahul"].append("Python")

for name, courses in students.items():
    print(name, ":", ",",courses)
    

# -------------------------------
# 10. Mini Project : Number Utility Tool
# -------------------------------
num = int(input("\nEnter number: "))
print(" binary value :- {:b}".format(num))
print(" octal value :- {:o}".format(num))
print(" hexa value :- {:x}".format(num))


money = 20000000000
print("have money {:,}".format(money))

num = 213
print("213 scientific value :- {:e}".format(num))
