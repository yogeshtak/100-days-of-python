#welcome greeting message
print("Welcome to the Tip Calculator")

#asking for bill amount
ask = True

while ask == True:
    total_bill = input("what was the total bill?\n")

    try:
        total_bill = int(total_bill)
        ask = False
            
    except ValueError:
        print("This is not a valid amount. Please do not use $ or any currency sign")

#asking for tip percentage
ask_tip = True

while ask_tip:
    tip = input("What percentage of tip would you like to give? Enter between 0 to 100.\n")

    try:
        tip = int(tip)/100
        ask_tip = False

    except ValueError:
        print("Invalid tip percentage. Use a number between 0 and 100.")

#asking for number people to split
ask_people = True

while ask_people:
    people = input("How many people to split the bill into?\n")

    try:
        people = int(people)
        ask_people = False

    except ValueError:
        print("Invalid number of people.")

#printing final output 
final_amount = float(total_bill) + float(total_bill*tip)
print(f"Each person should pay {final_amount/people}")


    
