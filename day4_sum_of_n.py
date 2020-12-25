#day4
#16-Dec-2020

#function to calculate sum of n numbers
def sumofn():
    #validating input for positive number
  while True:
    n = input("Enter a positive integer?")
    try:
      val = int(n)
      if val < 0:
        print("This is not positive integer")
        continue
      break
    except ValueError:
      print("This is not an int")
    #formula for sum of n numbers
  sum1 = (val*(val+1))/2
  print(f"Sum of first {val} positive numbers is: {sum1}")

sumofn()