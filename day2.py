# day2
#task1- Bitwise Operator Tasks (1–8)
#1 and
a= 10
b= 6
print(a & b) 
#2 or
x= 12
y= 5
print(x | y)    
#3 not
num= 8
print(~num)
#4 xor
a= 15
b= 9
print(a ^ b)
#5 left shift by 2
num= 7
print(num << 2)
#6 right shift by 1
num= 20
print(num >> 1)
#7
num1 =int(input("enter first number :"))
num2 =int(input("enter second number :"))
print("AND result :",num1&num2)
#8
num1 =int(input("enter first number :-"))
num2=int(input("enter second number :-"))
print("XOR result",num1^num2)
#task2- string tasks (9–14)
#9- 
a="hi"
print(a*4)
#10
a="python"
print(a*3)
#11
str1="super"
str2="man"
print(str1+str2)
#12
str1="hello"
str2=" "
str3="world"
print(str1+str2+str3)
#13
name=input("enter your name:")
print(name*5)
#14
str1=input("enter your first name:-")
str2=input("enter your last name:-")
print(str1+" "+str2)
#task3- Input & Type Casting Tasks (15–20)
#15 
name=input("enter your name:")
print("name:",type(name))
#16
age=int(input("enter your age:"))
print("age:",age)
print("age data type:",type(age))
#17
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
sum=num1+num2
print("total:",sum)
#18
num1=int(input("enter your mark english:-"))
num2=int(input("enter your mark math:-"))
avg=(num1+num2)/2
print("average mark:",avg)
#19
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
print((3*a*2)+b-2)
#20
num1=input("enter number:")
num1=int(input("enter number:"))
print("num1 data type:",type(num1))
print("num1 data type:",type(num1)) 
#task4- Unit Digit Tasks (21–25)
#21
num=input()
print(num[len(num)-1])
#22
num=int(input("enter a number:"))
print(num%10)
#23
num=int(input("enter a number:"))
print(num//10)
#24
num=int(input("enter a number:"))
print((num//10)%10)
num=12345
#25
print("last digit number:",num%10)
#26
num=int(input("enter anumber:"))
if(num>50):
    print("number is greater than 50")
else:
    print("number is less than 50")  
#27
num=int(input("enter a number:"))
if(num>50) :
    print("number is greater than 50")
else :
    print("number is less than 50")
#28
age=int(input("enter your age:"))
if(age>=18):
    print("you are adult")
else:
    print("you are minor")  
#29
num= 70
if(num>=100):
    print("number is greater than or equal to 100")
else:
    print("number is less than 100")
#30
num= -5
if(num>=0):
    print("number is greater than or equal to 0")
else:
    print("number is less than 0")  

#task6- If-Else Tasks (31–34)
# 31-Take a number and check if it is even or odd
num=34
if(num%2==0) :
    print("number is even")
else:
    print("number is odd")
#32-Take marks from user input and check if pass or fail (pass ≥ 35).
mark=int(input("enter your mark:"))
if(mark>=35):
    print("you are pass")
else:
    print("you are fail")  
#33-Take a number and check if it is positive or negative 
num=0
if(num>0):
    print("number is positive") 
elif(num<0):
    print("number is negative") 
else:
      print("number is positive")                 
#34-Take a number and check if it is greater than 10 or not.

num=-9
if(num>10):
    print("number is greater than 10")
elif(num<10):
    print("number is less than 10")
else:
    print("number is equal to 10") 

#task7-Nested If Tasks (35–37)
# 35-Create a program for job eligibility, Conditions- 1-Age ≥ 18, 2-Height ≥ 160 cm, 3-Weight ≥ 60 kg.Print selected or rejected.
name=input("enter your name:")
age=int(input("enter your age:"))
height=int(input("enter your height in cm:"))   
weight=int(input("enter your weight in kg:"))

if(age>=18):
    if(height>=160):
        if(weight>=60):
            print(name,"you are selected")
        else:
            print(name,"you are rejected-under weight")
    else:
        print(name,"you are rejected-under height")
else:
    print(name,"you are rejected-under age")
#36-Create a college admission program:Conditions- 1-Age ≥ 17, 2-Marks ≥ 60. Print selected or rejected.

name=input("enter your name::")
age=int(input("enter your age:")) 
marks=int(input("enter your marks:"))

if(age>=17):
    if(marks>=60):
        print(name,"you are selected")
    else:
        print(name,"you are rejected-under marks")  
else: 
    print(name,"you are rejected-under age")
#37- Create a sports selection program: Conditions- 1-Age ≥ 16, 2-Height ≥ 150 cm, 3-Weight ≥ 50 kg. Print selected or rejected. 

name=input("enter your name:")
age=int(input("enter your age:"))
height=int(input("enter your height in cm:"))
weight=int(input("enter your weight in kg:"))   
if(age>=16):
    if(height>=150):
        if(weight>=50):
            print(name,"you are selected")
        else:
            print(name,"you are rejected-under weight")
    else:
        print(name,"you are rejected-under height")
else:
    print(name,"you are rejected-under age")

#task8- Match Statement Tasks (38–40)
#38
day=int(input("enter day number:"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

#39

colour=int(input("enter colour number:"))
match colour:
    case 1:
        print("RED")
    case 2:
        print("BLUE")
    case 3:
        print("GREEN")  

#40

fruits=int(input("enter fruit number:"))
match fruits:
    case 1:
        print("APPLE")
    case 2:
        print("MANGO")
    case 3:
        print("ORANGE")
    case 4:
        print("BANANA")    
