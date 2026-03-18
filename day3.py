#Section 1: Loop Basics (1–10)
#1
for i in range(1,51):
    print(i)

 #2

for i in range(1,101) :
    if i % 2 == 0 :
        print(i)  

#3

for i in range(1,101) :
    if i % 2 ==1 :
        print(i)

#4

num = 7
for i in range(1,11): 
    print(num,"*",i,"==",num*i) 

#5
total =0
for i in range(1,101):
    total+=i
    print("sum=",total)
  
#6  
    for i in range(50,0,-1):
        print(i)

#7
count = 0
for i in range (1,101):
    if i % 3 == 0 :
        count += 1
print("count :", count) 

#8
for i in range (1,11):
    print(i**2)

#9

for i in range (1,11):
    print(i**3)    

#10
n= int(input("Enter a number: "))
for i in range (1,n+16) :
    print(i)    

#Section 2: While Loop (11–15)    
#11
i=20
while i<=20 :
    print(i)
    i+=1

#12 
num = int(input("enter the number :"))
fact = 1
i = 1
while i <= num :
    fact = fact * i
    i += 1
print("factorial is", fact)  

#13
num = int(input("enter the number :"))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)

#14
num = int(input("enter the number :"))
count = 0
while num > 0:
    num //= 10
    count += 1  
print("Number of digits:", count)

#15
while True:
    user_input = input("Enter something (type 'stop' to end): ")
    if user_input.lower() == "stop":
        print("Program stopped.")
        break
    else:
        print("You entered:", user_input)

 #Section 3: Nested Loops (16–20)
#16       
for i in range (1 , 6):
    for j in range (i):
        print("*" , end="")
    print()

#17
for i in range (1,5):
    for j in range (1,i+1):
        print(j , end="")
    print()  

#18     
for i in range (1,6) :
    for j in range (1,11) :
        print(i, "*",j,"=",i*j) 
    print()

#19 
for i in range (3):
    print("A B C")   
print()
#20
num= 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")    
        num += 1
    print()

#Section 4: String Basics (21–25)
# 21
string  ="nitinjosephjose" 
print("total characters :",len(string))
#22
string = input("Enter a string: ")
vowels = "aeiouAEIOU"   
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)
#23
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
consonant_count = 0

for char in string:
    if char.isalpha() and char not in vowels:
        consonant_count += 1

print("Number of consonants in the string:", consonant_count)
#24
string ="hello"
print(string[ : :-1])
#25
string = input("Enter a string: ")
reversed_string = ""        
for char in string:
    reversed_string = char + reversed_string  # prepend character to reverse    

if string == reversed_string:
    print("The string is a palindrome.")

#Section 5: String Slicing (26–30)  
# 26

name = "helloworld"
print(name[0:5])

#27-Print last 3 characters

name = "helloworld"
x = slice(7,10)
print(name[x])

#28-Print string in reverse using slicing
name = "helloworld"
print(name[ : :-1])

#29-Print every 2nd character

name = "helloworld"

print(name[0:10:2])

#30-Remove first and last character from string

name = "helloworld"
result = name [1:-1]
print(result)

#Section 6: List Basics (31–35)
#31-Create a list of 5 numbers and print sum
numbers = [10,20,30,40,50]
print ("sum",sum(numbers))

#32-Find maximum value in list
numbers = [10,20,30,40,50]
print("maxvalue",max(numbers))

#33-Find minimum value in list

numbers = [10,20,30,40,50]
print("maxvalue",min(numbers))

#34-Count total elements in list

numbers = [10,20,30,40,50]
print("maxvalue",len(numbers))

#35-Check if element exists in list

numbers = [10, 20, 30, 40, 50]
found = False

for num in numbers:
    if num == 30:
        found = True
        break

if found:
    print("Element exists")
else:
    print("Element not found")


#Section 7: List Operations (36–40)
#36-Add 3 elements using append()

numbers= []
numbers.append(10)
numbers.append(20)
numbers.append(30)
print("numbers in list :",numbers)

#37-Insert element at specific index

name = ["nitin","joseph","jose","raj"]
name.insert(2,"jack")
print (name)

#38-Remove element using remove()
name = ["nitin","joseph","jose","raj"]
name.remove("jose")
print(name)

name = ["nitin","joseph","jose","raj"]
del name [3]
print(name)

#39-Reverse list without using .reverse()

name = ["nitin","joseph","jose","raj"] 
reverse_list = name[ : :-1]
print(reverse_list)

#40-Sort list without using .sort()
 
name = ["nitin","joseph","jose","raj"]
  
name.sort()
print(name)
name.reverse()
print(name)