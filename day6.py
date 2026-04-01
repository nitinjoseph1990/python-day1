#Task 1: Encapsulation (User Class)

class user :
    _user_name : None
    _pwd       : None
    
    def __init__(self,_user_name,_pwd):
        self._user_name = _user_name
        
    def register(self):
        print("Registering user:"+self._user_name)
    
    def login(self):
        print("Logging in:"+self._user_name)
        
# Testing

    from Encapsulation import user 



user1 =user("john", "1234")

user1.register()
user1.login()

#Task 2: Inheritance (User → Student, Faculty, TempFaculty)

class user :         # parent class
    
    
    def register (self) :
        print("User Registered Successfully")
        
    def login (self) :
        print("User Logged In Successfully")   
        
        
class student (user) :                  # child class
   
   
    def student_greet (self) :       
        print("Hello Student")    
        
        
class faculty (user) :                    # child class 2
    
    def faculty_greet (self) :
        print ("Hello Faculty")
        
        
class tempfaculty (faculty) :     #TempFaculty (Multilevel)
    def tempfaculty_greet (self) :
        print("Hello Temp Faculty")      
        
        
# Testing

    from inheritance import user,student,faculty,tempfaculty
print("----- Student Object -----")
s = student()
s.register()          
s.login()             
s.student_greet()  


print("\n----- Faculty Object -----")
f = faculty()
f.register()          
f.login()             
f.faculty_greet()  

print("\n-----Temp Faculty Object -----")
t = tempfaculty()
t.register()              
t.login()                 
t.faculty_greet()         
t.tempfaculty_greet()  


#Task 3: Method Overriding

class User:                     # Parent Class
    def greet(self):
        print("Welcome User")



class Student(User):                  # Child Class 1 (Override)
    
    def greet(self):
        print("Welcome Student")


# Child Class 2 (Override)
class Faculty(User):                          # Child Class 2 (Override)
    
    def greet(self):
        print("Welcome Faculty")  
        
        
# Testing
 
from method_overriding import User,Student,Faculty

u = User()
s = Student()
f = Faculty()

print("----- Calling greet() -----")
u.greet()   
s.greet()   
f.greet()         


#Task 4: Method Chaining
 class user :
    
    def register (self) :
        print("registred")
        return self


    def login (self) :
        print("logined")
        return self
    
    
    def greet (self) :
        print("enjoy everyone")
        return self

# Testing

 from method_chaining import user


 user = user()

 user.login().greet().register()
 
# Task 5: Combined Real-Time System
class User:
    users_count = 0  # class variable

    def __init__(self, username, pwd):
        self.__username = username
        self.__pwd = pwd
        User.users_count += 1

    def get_username(self):
        return self.__username

    def register(self):
        print(f"{self.__username} registered")
        return self

    def login(self):
        print(f"{self.__username} logged in")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self

# Testing

from combined_day6task import User,Student,Faculty

s = Student("Nitin", "1234")
f = Faculty("Joseph", "5678")

print("----- Student  -----")
s.login().greet().register()

print("\n----- Faculty  -----")
f.login().greet().register()

print("\nTotal Users Created:", User.users_count)
      
                 