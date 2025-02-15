#Write a Python program to convert degree to radian.
#Input degree: 15
#Output radian: 0.261904
import math

degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian: {:.6f}".format(radian))

#Write a Python program to calculate the area of a trapezoid.
#Height: 5
#Base, first value: 5
#Base, second value: 6
#Expected Output: 27.5
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (height * (base1 + base2)) / 2
print("Expected Output:", area)

#Write a Python program to calculate the area of regular polygon.
#Input number of sides: 4
#Input the length of a side: 25
#The area of the polygon is: 625
import math

n = int(input("Input number of sides: "))
a = float(input("Input the length of a side: "))

area = (n * a**2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)

#Write a Python program to calculate the area of a parallelogram.
#Length of base: 5
#Height of parallelogram: 6
#Expected Output: 30.0
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print("Expected Output:", area)
