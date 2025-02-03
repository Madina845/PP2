#Python Functions
#ex1-Creating a Function
def my_function():
  print("Hello from a function")

#ex2-Calling a Function
def my_function():
  print("Hello from a function")

my_function()

#ex3-Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#ex4-Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#ex5
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")

#ex6-Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#ex7-Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#ex8-Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#ex9-Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#ex10-Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#ex11-Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#ex12-The pass Statement
def myfunction():
  pass

#ex13-Positional-Only Arguments
def my_function(x, /):
  print(x)

my_function(3)

#ex14
def my_function(x):
  print(x)

my_function(x = 3)

#ex15
def my_function(x, /):
  print(x)

my_function(x = 3)

#ex16-Keyword-Only Arguments
def my_function(*, x):
  print(x)

my_function(x = 3)

#ex17
def my_function(x):
  print(x)

my_function(3)

#ex18
def my_function(*, x):
  print(x)

my_function(3)

#ex19-Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#ex20-Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

#ex21-
#Python Lambda
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
def myfunc(n):
  return lambda a : a * n

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
 
#Python Classes and Objects 
#ex1
class MyClass:
  x = 5

#ex2
p1 = MyClass()
print(p1.x)

#ex3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#ex4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

#ex5
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#ex6
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#ex7
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#ex8
p1.age = 40

#ex9
del p1.age

#ex10
del p1

#ex11
class Person:
  pass


 
Python Inheritance
#ex1-Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#ex2-Create a Child Class
class Student(Person):
  pass

#ex3
x = Student("Mike", "Olsen")
x.printname()

#ex4-Add the __init__() Function
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

#ex5
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

#ex6-Use the super() Function
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#ex7-Add Properties
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

#ex8
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

#ex9-Add Methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 
Student

