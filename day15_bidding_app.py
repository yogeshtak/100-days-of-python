import os

bids = {}

ask_for_bid = True

while ask_for_bid:

    name_check = True

    #checking for unique name
    while name_check:
        name = input("Please enter your name ")
        if name in bids.keys():
            print("Please enter a unique name, we already have someone with that name")

        else:
            name_check = False
    
    bid = int(input("Please enter your bid amount $"))

    bids[name] = bid

    more_bids = input("Is there anyone else who wants to bid? Yes or No ")

    if more_bids.lower() == "no":
        ask_for_bid = False
    
    #clearing screen so that next user cannot see previous bids
    os.system('posix')
    os.system('clear')

max_bid = max(bids, key=bids.get)

print(f"Max bid was from {max_bid} with amount ${bids[max_bid]}")