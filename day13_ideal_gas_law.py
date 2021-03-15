'''
The ideal gas law is a mathematical approximation of the behavior of gasses as
pressure, volume and temperature change. It is usually stated as:
PV = nRT
where P is the pressure in Pascals, V is the volume in liters, n is the amount of
substance in moles, R is the ideal gas constant, equal to 8.314 J/mol K , and T is the
temperature in degrees Kelvin.

Write a program that computes the amount of gas in moles when the user supplies
the pressure, volume and temperature. Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit.

'''

gas_constant = 8.314

pressure = float(input("Please enter the pressure in Pascals:"))
volume = float(input("Please enter the volume in liters"))
temperature = float(input("please enter the temperature in degrees Kelvin"))

gas_moles = (pressure*volume)/(gas_constant*temperature)

print(f"Gas in moles is {gas_moles}")