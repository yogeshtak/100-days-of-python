word_list = ['abruptly', 'absurd','bikini','cycle','duplex', 'dwarves', 
'embezzle', 'equip','faking', 'fishhook', 'funny', 'gabby', 'galaxy',
'hyphen','icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jockey', 'jogging',
'joking','khaki', 'kilobyte','lengths', 'lucky', 'luxury','oxygen', 'pajama',]

import random
from hangman_art import stages, logo

print(logo)

game_on = True

word = random.choice(word_list)
word_len = len(word)

display = ''
for i in range(word_len):
    display += "_ "

while game_on:
    character = input(f"Guess a charachter. It is a {word_len} letter word.").lower()
    display = ''

    for char in word:
        if char == character:
            display += f'{character} '

        else:
            display += '_ '
    
    if di

    

print(word)
print(display)