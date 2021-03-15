'''
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ∆T degrees Celsius can be
computed using the formula:

q = mC∆T.

Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.

Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.
'''

def heatcapacity():

  xyz = False
  while xyz == False:
    initial_temp = input("Enter initial temperature of water in degree celcius:")
    if initial_temp.isalpha() == False:
      initial_temp = float(initial_temp)
      xyz = True

  abc = False
  while abc == False:
    final_temp = input("Enter final temperature of water in degree celcius:")
    if final_temp.isalpha() == False:
      final_temp = float(final_temp)
      abc = True
  
  lmn = False
  while lmn == False:
    mass = input("Enter mass of water in grams:")
    if mass.isalpha() == False:
      mass = float(mass)
      lmn = True

  #DIFFERENCE IN TEMPERATURE
  diff_temp = final_temp - initial_temp

  energy = mass*4.186*diff_temp
  energy_kwh = energy*0.0000002778
  cost_energy = energy_kwh*0.089
  print(f"Energy required to go from {initial_temp} degree celcius to {final_temp} degree celcius is: {energy} J")
  print(f"With 8.9 cents per Kilo Watt hour rate, It would cost you {cost_energy}USD")

heatcapacity()