
# Task 1: Use super() properly

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id



class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees



class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary



class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration


#Testing

from super import User,Student,Faculty,TempFaculty


s1 = Student("Nitin", 101, "Computer Science", 50000)
f1 = Faculty("Joseph", 201, 60000)
t1 = TempFaculty("Jose", 301, 40000, "6 months")


print(s1.name, s1.id, s1.dept, s1.fees)
print(f1.name, f1.id, f1.salary)
print(t1.name, t1.id, t1.salary, t1.duration)

#===================================================================================

# Task 2: Apply Abstraction
from abc import ABC , abstractmethod

class Abstractuser(ABC) :
    @abstractmethod
    def get_details(self) :
        pass
    
    
    
 
class Student(Abstractuser) :
    def get_details(self) :
        print("Hi student")
        
        
class Faculty(Abstractuser) :
    def get_details(self) :
        print("Hi faculty")        
        

#Testing

from abstraction import Abstractuser,Student,Faculty


s = Student()
f = Faculty()

s.get_details()
f.get_details()

#========================================================================================================


# Task 3: Sorting using key
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


students = [
    Student("Nitin", 50000),
    Student("Rahul", 30000),
    Student("Anu", 40000)
]

faculty = [
    Faculty("John", 60000),
    Faculty("David", 80000),
    Faculty("Sara", 55000)
]


students.sort(key=lambda x: x.fees)

faculty.sort(key=lambda x: x.salary)


print("Students sorted by fees:")
for s in students:
    print(s.name, s.fees)

print("\nFaculty sorted by salary:")
for f in faculty:
    print(f.name, f.salary)
    
#===============================================================================

#    Task 4: Use map()
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


students = [
    Student("Nitin", 70000),
    Student("Joseph", 50000),
    Student("JOSE", 20000)
]

names = list(map(lambda s: s.name, students))
fees = list(map(lambda f: f.fees, students))
print(".....NAME....")
print(names)
print("\n....FEES...")
print(fees)

#==========================================================================
 #Task 5: Use filter()

class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


students = [
    Student("Nitin", 60000),
    Student("Ram", 30000),
    Student("Anupama", 70000)
]

faculty = [
    Faculty("Johny", 25000),
    Faculty("David", 40000),
    Faculty("Sony", 35000)
]


high_fee_students = list(filter(lambda s: s.fees > 50000, students))


high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))


print("High fee students:")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nHigh salary faculty:")
for f in high_salary_faculty:
    print(f.name, f.salary)
    
 #====================================================================   
    
    
 #   Task 6: Use reduce()


from functools import reduce

class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


students = [
    Student("Nitin", 20000),
    Student("Rohan", 30000),
    Student("Anu", 35000)
]

faculty = [
    Faculty("John", 35000),
    Faculty("David", 50000),
    Faculty("Sara", 30000)
]


total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)


print("Total Fees:", total_fees)
print("Total Salary:", total_salary)


# Task 7: Higher Order Function

def process_users(data, func):
    return list(map(func, data))

nums = [1, 2, 3, 4]

result = process_users(nums, lambda x: x * 2,)

print(result)

def process_users(users, func):
    return list(map(func, users))


students = ["Nitin", "Rahul", "Anu"]

result = process_users(students, lambda x: x.upper())

print(result)

#==========================================================================================================================
# combined project
from functools import reduce

class User:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        pass


class Student(User):
    def __init__(self, name, fees):
        super().__init__(name)
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, Salary: {self.salary}"



students = [
    Student("Nitin", 90000),
    Student("Joseph", 60000),
    Student("Jose", 50000)
]

faculty = [
    Faculty("Joe", 25000),
    Faculty("Don", 40000),
    Faculty("Sara", 35000)
]


print("All Student Details:")
for d in map(lambda s: s.get_details(), students):
    print(d)

print("\nAll Faculty Details:")
for d in map(lambda f: f.get_details(), faculty):
    print(d)


students.sort(key=lambda s: s.fees)
faculty.sort(key=lambda f: f.salary)

print("\nSorted Students (by fees):")
for s in students:
    print(s.name, s.fees)

print("\nSorted Faculty (by salary):")
for f in faculty:
    print(f.name, f.salary)


high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\nHigh Fee Students:")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nHigh Salary Faculty:")
for f in high_salary_faculty:
    print(f.name, f.salary)
    
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\nTotal Fees:", total_fees)
print("Total Salary:", total_salary)