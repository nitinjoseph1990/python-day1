# Task 1: User Info Manager (Functions + Dictionary)

users = []
def create_user(name, age, role):
   user = {
       "name": name.title(),   
       "age": age,
       "role": role
   }
   return user
users.append(create_user("Nitin",32,"data analyst"))
users.append(create_user("arun", 29, "python developer"))
users.append(create_user("priya", 23, "business analyst"))
for u in users:
   print(u)
   
# 2: Dynamic Calculator (*args)

def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers) 
    return total, avg

result = calculate_total(10, 20, 30, 40,59,87)

print("Total:", result[0] )
print("Average:", result[1])

#Task 3: Keyword Config System (**kwargs)

def system_config(**settings):
    for key, value in settings.items():
        print(key , value ,sep = ":")

system_config(mode="debug", version="1.0", user="admin",name = "nitin")

#Task 4: Factorial Service (Recursion)

def factorial(n):
    if (n < 0):
        return "Error"
    if (n == 0):
        return 1
    return n * factorial(n-1)

print("factorial value:-",factorial(7))

#Task 5: Memory Optimization (Generator)

def square_generator(num):
     value = []

     for i in range(1,num+1):
         value.append(i*i)
     return value

    
finalList = square_generator(20)

print(finalList)
   
#Yield squares instead of storing in list

def square_generator(n):
      for i in range(1,n+1):
         yield i*i
newVal = square_generator(20)

print(newVal)

for i in newVal:
    print(i)

#Task 6: Exception Handling Module

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator / denominator
    print("Result:", result)

except Exception:
    print("Error: Cannot divide by zero and cannot use letters only numbers allowed")


finally:
    print("Program Completed")
    

   
# Task 7: File Handling

    with open("team_data.txt") as t :
     print(t.read())
     print(t.closed)