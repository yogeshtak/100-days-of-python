word_list = ['abruptly', 'absurd','bikini','cycle','duplex', 'dwarves', 
'embezzle', 'equip','faking', 'fishhook', 'funny', 'gabby', 'galaxy',
'hyphen','icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jockey', 'jogging',
'joking','khaki', 'kilobyte','lengths', 'lucky', 'luxury','oxygen', 'pajama',]

import random
from hangman_art import stages, logo

print(logo)
lives = 6

game_on = True

word = random.choice(word_list)
word_len = len(word)

display = []
for i in range(word_len):
    display += "_"

while game_on:
    character = input(f"Guess a charachter. It is a {word_len} letter word.").lower()

    if character in display:
        print(f"You have already guessed {character}")
    
    for i in range(word_len):
        letter = word[i]
        if letter == character:
            display[i] = character
    
    if character not in word:
        print(f"{character} not in the word. You lose a life")
        lives -= 1

        if lives == 0:
            game_on = False
            print("You Lose")
    
    print(f"{''.join(display)}")

    if "_" not in display:
        game_on = False
        print("You WIN")
    
    print(stages[lives])