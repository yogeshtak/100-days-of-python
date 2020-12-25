#day3
#15-Dec-2020

#source = https://ascii.co.uk/art
print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----/
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------/
 \_/__________________________________________________________________/

''')
#welcome message
print("Welcome to the Treasure Island")
print("Your aim is to find the treasure.")

#asking for left or right and validating respose
left_right_ask = True

while left_right_ask:
    left_right = input("Will you go left or right?\n").lower().strip()

    if left_right == "left" or left_right == "right":
        left_right_ask = False

    else:
        print("Please enter valid response: left or right")

if left_right == "right":
    print("Game Over :( ")

if left_right == "left":
    #asking for swim or wait for boat and validating response
    swim_boat_ask = True

    while swim_boat_ask:
        swim_boat = input("Do you want to swim or wait for a boat? Enter swim or boat:\n").lower().strip()

        if swim_boat == "swim" or swim_boat == "boat":
            swim_boat_ask = False

        else:
            print("Please enter a valid response: swim or boat")

    if swim_boat == 'swim':
        print("Game over :((")

    if swim_boat == 'boat':
        #asking for door color and validating response
        door_ask = True

        while door_ask:
            print("You have three doors in front of you")
            door = input("Which door will you go next? Red, Yellow or Blue?\n").lower().strip()

            if door == "red" or door == "yellow" or door == "blue":
                door_ask = False

            else:
                print("Select a valid door: Red, Yellow or Blue")
        
        if door == "yellow":
            print("YOU WON!!!!")

        else:
            print("You lost! Game over :(")
