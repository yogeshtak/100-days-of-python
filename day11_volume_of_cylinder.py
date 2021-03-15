'''
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.

'''
import math

radius = int(input("Enter radius of the cylinder:"))
height = int(input("Enter height of the cylinder:"))

print(f"Volume of the cylinder is {round(math.pi*(radius**2)*height,1)}")
