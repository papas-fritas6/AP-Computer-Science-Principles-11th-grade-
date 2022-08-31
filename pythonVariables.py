#Printing commands
x = 5
y = "John"
a = 4
A = "Bob"
print(x, y)
print(a, A)
# A will not overwrite a
#  "=" in programming means "Assigned to" Ex. 5 is assigned to variable x
#                 Legal Variable Names
# Variables can’t begin with capital
# no spaces (can be replaced with underscores, dashes, etc.)
# Can’t begin with a number
# It is case sensitive and CANNOT contain alpha-numeric characters [A-z or 0-9]
# the "#" can also mean "not equal to"
# in programming, it's often more about being efficient rather than effective
#Python allows you to assign many values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(x, y, z)
#Python allows you to assign one value to multiple variables
c = 1
d = 1
e = 1
print(c, d, e)
x = y = z = "Orange"
# RANDOM NUMBER
import os
import random
os.system('clear')
print(random.randrange(1, 10))

#Concatenation
#To concatenate or combine 2 strings you can use the + operator
#Add " " between the variables
a, b = "hola", "Juan"
c = a + " " + b
print(c)
# String format
age = "36"
text = "My name is patricia, I am " + age
print(text)
os.system('clear')
# Python Boolean
#it uses 2 values true or false, it evaulates any expression to true or false, python then evaluates amd reitrms to a boolean answer
print(10 > 9)
print(10 == 9)
#1 equal means assign, 2 equals mean equal to
print(10 < 9)
# Boolean in a condition (an if statement)
os.system('clear')
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is greater than a")
#evaluate values and variables
#evaluate a string and a number
print(bool("Hello"))
print(bool(15))
#Python operators
#Examples 
x=15
y=2
# print x % y
print(x//y) #the floor divison // rounds the result down to the nearest whole number
os.system('clear')
x, y = 2, 15
z= "hello"
if x<y:
  print("true")
print (z)
os.system('clear')
