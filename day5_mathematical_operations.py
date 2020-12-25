#day5
#17-Dec-2020

#importing external library
import math

def math_op():
    #input
    a = int(input("Enter a number?"))
    b = int(input("Enter another number?"))
    #sum
    print(f"Sum of these two numbers is: {round(a+b,2)}")
    #subtraction
    print("NEXT IS DIFFERENCE LARGER NUMBER - SMALLER NUMBER")
    if a > b:
        print(f"Difference of these two numbers is: {round(a-b,2)}")
    if b > a:
        print(f"Difference of these two numbers is: {round(b-a,2)}")
    #product
    print(f"Product of these two numbers is: {round(a*b,2)}")
    #division (quotient)
    print(f"The quotient when a is divided by b: {a//b}")
    #remainder
    print(f"The remainder when a is divided by b: {a%b}")
    #finding log
    print(f"result of log with base 10 a:{math.log(a,10)}")
    #power
    print(f"a with power b: {a**b}")

math_op()