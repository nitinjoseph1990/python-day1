# day 1
# task1-print formating
print("hello world", end=" ")
print("welcome python")
print("laptop","mouse","keyboard", sep="|")
# task2- variables
name="Ravi"
age=22
city="Chennai"
print(name,age,city, sep="- ")
#task 3-multi assignment
Name,age,student="Meena",20,"true"
print("multi assignment:-",Name,age,student, sep="'")
#task 4-  indexing
word="python"
print("first letter :" , word[0])
print("third letter :",word[2])
print("last letter :",word[5])
#task5- arithmetic operations
print(.25+10)
print(50-20)
print(8*5)
print(100/10)
print(10%3)
print(2**4)
print(20//3)   
#task6- bodmass expression
print(3+2*5**2)    
#task7- assignment operators
num=50
num+=25
print(num)
num=100
num/=10
print(num) 
#task8- comparison operators
print(10>5)
print(20<15)
print(5==5)
print(10!=8)
print(7>=7)
print(6<=2)
#task9- string comparision
a="apple"
b="Apple"
print(a==b) #it will be false because of case sensitivity   the value os "a"and "A"are different
#task10- logical operators
print(10>5 and 5==5)
print(5>10 or 10==10)  
print(not(5>2))
#task11- membership operators
number=[10,20,30,40,50] 
print(20 in number)
print(60 in  number) 
print(30 not in number) 
#task12- swap variables
a=10
b=20
a,b=b,a
print("a =",a)
print("b =",b)  
#task13- bitwise operators
a=6
b=3
print(a ^ b)