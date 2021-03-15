'''
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s^2

'''

import math

initial_velocity = 0
acceleration = 9.8 #due to gravity
distance = ''

while distance.isdigit() == False:
    print('Please enter the height in meters in numerical format')
    distance = input("Enter the height:")

distance = float(distance)
final_velocity = round(math.sqrt((initial_velocity**2)+ 2*acceleration*distance),2)
print('Final velocity is {} m/s'.format(final_velocity))
