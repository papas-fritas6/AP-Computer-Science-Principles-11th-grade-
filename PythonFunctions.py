import os
def n():
  os.system('clear');
#functions
'''A function is a block of code which only runs when it is called. You can pass data, known as parameter, into a function. A function can get data as a result'''
#Creating a function
#In python, a function is created using the def keyword
def my_function():
  print("Hello from a function");
#Calling a function
#To call a function, use the function name followed by paranthesis
my_function()
#Example
def my_functions (fname):
  print(fname + " Joaquin")
my_functions("pizza")
#PARAMETERS OR ARGUMENTS
#The terms parameter and argument can be used for the same thing : information that are passed into a function
n()
#A parameter is the variable listed inside the parenthesis in the function definition
#An argument is the value that is sent to the function when it is called
def mY_function (fname, lname):
  print(fname+" "+lname)
mY_function("Me gusta", "fausto")
#Python Class
#To create a class, use keyboard class
#Create a class named Myclass, with a property named x:
n()
class Myclass:
  x=5
#Create an object
#Now we can use the class name MyClass to create an object
#Create an object named G1, and print the value of x:
p1 =Myclass()
print(p1.x)
#The _init_() function to assign values for name and age:
#Ex. Create a class named Person, use the _init_() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
"""note the _init_() function is called automatically everytime the class is being used to create a new object
Python inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class
Parent class is the class being inherited from, also called /base class/
Child class is the class that inherits from another class, also called /derived class/
Any class can be a parent, so syntax is the same as creating other class
Ex. create a class named Person, with first name and last name properties, and a printname method:"""
class person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
  def printname(self):
    print(self.fname, self.lname)
'''Use the Person class to create an object, and then execute the printname method '''
x= person("me gusta", "fausto")
x.printname()
n()
'''Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
Ex. Assign: Create a class named student, which will inherit the properties and methods from the parent class'''
class student(Person):
  pass
  '''Ex: Use the Student class to create and object, and then execute the printname method'''
  x= Student("moco", "choclo")
  x.printname()
