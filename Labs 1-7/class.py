#Python Classes
#1.Define a class which has at least two methods: getString:
#to get a string from console input printString: to print 
#the string in upper case.
class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

# Example Usage
obj = StringManipulator()
obj.getString()
obj.printString()

#2.Define a class named Shape and its subclass Square. 
#The Square class has an init function which takes a length
#as argument. Both classes have a area function which can 
#print the area of the shape where Shape's area is 0 by default.
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# Example 
square = Square(5)
print (square.area())  # Output: 25

#3.Define a class named Rectangle which inherits from 
#Shape class from task 2. Class instance can be constructed
# by a length and width. The Rectangle class has a method 
#which can compute the area.
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example Usage
rectangle = Rectangle(5, 3)
print(rectangle.area())  # Output: 15

#5.Write the definition of a Point class. Objects from this class should have a
#a method show to display the coordinates of the point
#a method move to change these coordinates
#a method dist that computes the distance between 2 points
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Example Usage
p1 = Point(2, 3)
p2 = Point(5, 7)
p1.show()
p2.show()
print("Distance:", p1.dist(p2))  # Output: Distance between p1 and p2


#6.Create a bank account class that has attributes owner, 
#balance and two methods deposit and withdraw. Withdrawals may not exceed 
#the available balance. Instantiate your class, make several deposits and withdrawals, 
#and test to make sure the account can't be overdrawn.
class Account:
 def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

 def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

 def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")

# Example Usage
acc = Account("John", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)  # Should not allow withdrawal

#Write a program which can filter prime numbers in a  list by using filter function. Note: Use lambda to define anonymous functions.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 3, 5, 17, 18, 29, 30, 37]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime Numbers:", prime_numbers)
