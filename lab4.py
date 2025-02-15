#Python Iterators
#ex1-iter() method
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#ex2
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#ex3- Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#ex4
mystr = "banana"

for x in mystr:
  print(x)

#ex5-Create an Iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self): #method
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#ex6-StopIteration (stop after 20 iterations)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self 
  
  def __next__(self):
    if self.a <= 20:
      x = self.a 
      self.a +=1
      return x
    else :
      raise StopIteration 
    
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x) # nu,bers from 1-20

#Python Polymorphism
#ex1-Function Polymorphism(len() function) String
x = "Hello World!"

print(len(x)) #12

#ex2-Tuple
mytuple = ("apple", "banana", "cherry")

print(len(mytuple)) #3

#ex3-Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict)) #3

#ex4-Class Polymorphism ( method move())
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move() # output : Drive! Sail! Fly!

#ex5- Inheritance Class Polymorphism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()  #Ford Mustang Move! Ibiza Touring 20 Sail! Boeing 747 Fly!

#Python Scope
#ex1-Local Scope
def myfunc():
  x = 300
  print(x)

myfunc()

#ex2-Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#ex3-Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#ex4-Naming Variables
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#ex5-Global Keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#ex6
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

#ex7-Nonlocal Keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x #hello

print(myfunc1())

#Python Modules
#ex1-Create a Module
def greeting(name):
  print("Hello, " + name)

#ex2-Use a Module
import mymodule # type: ignore

mymodule.greeting("Jonathan")

#ex3-Variables in Module
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#ex6
import mymodule # type: ignore

a = mymodule.person1["age"]
print(a)

#ex6-Re-naming a Module
import mymodule as mx # type: ignore

a = mx.person1["age"]
print(a)

#ex7-Built-in Modules
import platform

x = platform.system()
print(x)

#ex8-Using the dir() Function
import platform

x = dir(platform)
print(x)

#ex9-Import From Module
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#ex10
from mymodule import person1 # type: ignore

print (person1["age"])#36


#Python Datetime
#ex1-Python Dates
import datetime

x = datetime.datetime.now()
print(x)

#ex2-Date Output
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A")) #2025 sunday

#ex3-Creating Date Objects
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)#2020-05-17 00:00:00

#ex4-The strftime() Method
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))#June


#Python Math
#ex1-Built-in Math Functions
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y) #5 25

#ex2-abs() function
x = abs(-7.25)

print(x)

#ex3-pow(x, y) function returns 
x = pow(4, 3)

print(x)

#ex4-The Math Module
import math

#ex5-math.sqrt() method
import math

x = math.sqrt(64)

print(x)

#ex6-math.ceil() method and math.floor() method
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#ex7-math.pi constant,
import math

x = math.pi

print(x)

#Python JSON
#ex1-JSON in Python
import json

#ex2-Parse JSON
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])#30

#ex3-Convert from Python to JSON
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string: {"name": "John", "age": 30, "city": "New York"}
print(y)

#ex4-objects into JSON strings
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#ex5
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))#{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

#ex6-indent parameter
json.dumps(x, indent=4)

#ex7-separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))

#ex8-sort_keys parameter
json.dumps(x, indent=4, sort_keys=True)