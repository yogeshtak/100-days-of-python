'''
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.

'''
import math

radius = ''
while radius.isdigit() == False:
    print("Please enter radius in numeric format only")
    radius = input('Enter radius of cylinder: ')
radius = int(radius)

height = ''
while height.isdigit() == False:
    print("Please enter height in numeric format only")
    height = input('Enter radius of cylinder: ')
height = int(height)

print(f"Volume of the cylinder is {round(math.pi*(radius**2)*height,1)}")
