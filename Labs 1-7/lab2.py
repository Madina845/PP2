#Python Booleans

#ex1-Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#ex2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#ex3-Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

#ex4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#ex5-Most Values are True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#ex6-Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#ex7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#ex8-Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())

#ex9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#ex10
x = 200
print(isinstance(x, int))

#Python Operators
#ex1
print(10 + 5)

#ex2-Operator Precedence
print((6 + 3) - (6 + 3))

#ex3
print(100 + 5 * 3)

#ex4
print(5 + 4 - 7 + 3)

#Python Lists
#ex1
mylist = ["apple", "banana", "cherry"]

#ex2
thislist = ["apple", "banana", "cherry"]
print(thislist)

#ex3-Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#ex4-List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#ex5-List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#ex6
list1 = ["abc", 34, True, 40, "male"]

#ex7-type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#ex8-The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Python - Access List Items
#ex1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#ex2-Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#ex3-Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#ex4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#ex5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#ex6-Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#ex7-Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Python - Change List Items
#ex1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#ex2-Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#ex3
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#ex4
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#ex5-Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Python - Add List Items
#ex1-Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#ex2-Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#ex3-Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#ex4-Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Python - Remove List Items
#ex1-Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#ex2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#ex3-Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#ex4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#ex5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#ex6
thislist = ["apple", "banana", "cherry"]
del thislist

#ex7-Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Python - Loop Lists
#ex1-Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#ex2-Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#ex3-Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#ex4-Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#Python - List Comprehension
#ex1-List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#ex2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#ex3-Condition
newlist = [x for x in fruits if x != "apple"]

#ex4
newlist = [x for x in fruits]

#ex5-Iterable
newlist = [x for x in range(10)]

#ex6
newlist = [x for x in range(10) if x < 5]

#ex7-Expression
newlist = [x.upper() for x in fruits]

#ex8
newlist = ['hello' for x in fruits]

#ex9
newlist = [x if x != "banana" else "orange" for x in fruits]

#Python - Sort Lists
#ex1-Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#ex2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#ex3-Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#ex4
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#ex5-Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#ex6-Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#ex7
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#ex8-Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Python - Copy Lists
#ex1-Use the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#ex2-Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#ex3-Use the slice Operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Python - Join Lists
#ex1-Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#ex2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#ex3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Python Tuples
#ex1
mytuple = ("apple", "banana", "cherry")

#ex2-Create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#ex3-Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#ex4-Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#ex5-Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#ex6-Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#ex7
tuple1 = ("abc", 34, True, 40, "male")

#ex8-type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#ex9-The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Python - Access Tuple Items
#ex1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#ex2-Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#ex3-Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#ex4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#ex5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#ex6-Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#ex7-Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Python - Update Tuples
#ex1-Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#ex2-Add Items-Convert into a list:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#ex3-Add tuple to a tuple.
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#ex4-Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#ex5
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Python - Unpack Tuples
#ex1-Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

#ex2
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#ex3-Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#ex4
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Python - Loop Tuples
#ex1-Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#ex2-Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#ex3-Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Python - Join Tuples
#ex1-Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#ex2-Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#Python - Tuple Methods
#Method 	Description
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found

#Python Sets
#ex1
myset = {"apple", "banana", "cherry"}

#ex2
thisset = {"apple", "banana", "cherry"}
print(thisset)

#ex3-Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#ex4
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#ex5
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#ex6-Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#ex7-Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#ex8
set1 = {"abc", 34, True, 40, "male"}

#ex9-type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

#ex10-The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Python - Access Set Items
#ex1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#ex2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#ex3
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#Python - Add Set Items
#ex1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#ex2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#ex3-Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Python - Remove Set Items
#ex1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#ex2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#ex3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#ex4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#ex5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#Python - Loop Sets
#ex1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
 #Python - Join Sets
 #  #ex1-Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#ex2- | operator 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#ex3-Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#ex4
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#ex5-Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#ex6-Update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#ex7-Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#ex8-& operator 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#ex9-intersection_update() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#ex10
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#ex11-Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#ex12- - operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

#ex13-difference_update() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#ex14-Symmetric Differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#ex15-^ operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

#ex16-symmetric_difference_update() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

#Python Dictionaries
#ex1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#ex2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#ex3-Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#ex4-Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#ex5-Dictionary Length
print(len(thisdict))

#ex6-Dictionary Items - Data Types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#ex7-type()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#ex8-The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Python - Access Dictionary Items
#ex1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#ex2
x = thisdict.get("model")

#ex3-Get Keys
x = thisdict.keys()

#ex4
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#ex5-Get Values
x = thisdict.values()

#ex6
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#ex7
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#ex8-Get Items
x = thisdict.items()

#ex9
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#ex10
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#ex11-Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Python - Change Dictionary Items
#ex1-Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#ex2-Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Python - Add Dictionary Items
#ex1-Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#ex2-Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Python - Remove Dictionary Items
#ex1-Removing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#ex2-popitem() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#ex3-del keyword
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#ex4
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

#ex5-clear() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Python - Loop Dictionaries
#ex1-Loop Through a Dictionary
for x in thisdict:
  print(x)

#ex2-Print all values
for x in thisdict:
  print(thisdict[x])

#ex3-values() method
for x in thisdict.values():
  print(x)

#ex4-keys() method
for x in thisdict.keys():
  print(x)

#ex5-items() method
for x, y in thisdict.items():
  print(x, y)

#Python - Copy Dictionaries
#ex1-Copy a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#ex2-  function dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Python - Nested Dictionaries
#ex1-Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#ex2
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#ex3-Access Items in Nested Dictionaries
print(myfamily["child2"]["name"])

#ex4-Loop Through Nested Dictionaries
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#Python If ... Else
#ex1-If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

#ex2-Indentation
a = 33
b = 200
if b > a:
  print("b is greater than a") # you will get an error

#ex3-Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#ex4-Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#ex5
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#ex6-Short Hand If
if a > b: print("a is greater than b")

#ex7-Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

#ex8
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#ex9-And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#ex10-Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#ex11-Not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#ex12-Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#ex13-The pass Statement
a = 33
b = 200

if b > a:
  pass

#Python While Loops
#ex1
i = 1
while i < 6:
  print(i)
  i += 1

#ex2-The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#ex3-The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#ex4-The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Python For Loops
#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#ex2-Looping Through a String
for x in "banana":
  print(x)

#ex3-The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#ex5-The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#ex6-The range() Function
for x in range(6):
  print(x)

#ex7
for x in range(2, 6):
  print(x)

#ex8
for x in range(2, 30, 3):
  print(x)

#ex9-Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#ex10-
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#ex11-Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#ex12-The pass Statement
for x in [0, 1, 2]:
  pass

