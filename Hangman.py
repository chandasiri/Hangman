# -*- coding: utf-8 -*-
# This is game of guessing movie name

from os import system, name
from time import sleep


# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    print r'''
┏┓ ┏┓ ┏━━━┓ ┏━┓ ┏┓ ┏━━━┓ ┏━┓┏━┓ ┏━━━┓ ┏━┓ ┏┓
┃┃ ┃┃ ┃┏━┓┃ ┃ ┗┓┃┃ ┃┏━┓┃ ┃ ┗┛ ┃ ┃┏━┓┃ ┃ ┗┓┃┃
┃┗━┛┃ ┃┃ ┃┃ ┃┏┓┗┛┃ ┃┃ ┗┛ ┃┏┓┏┓┃ ┃┃ ┃┃ ┃┏┓┗┛┃
┃┏━┓┃ ┃┗━┛┃ ┃┃┗┓ ┃ ┃┃┏━┓ ┃┃┃┃┃┃ ┃┗━┛┃ ┃┃┗┓ ┃
┃┃ ┃┃ ┃┏━┓┃ ┃┃ ┃ ┃ ┃┗┻━┃ ┃┃┃┃┃┃ ┃┏━┓┃ ┃┃ ┃ ┃
┗┛ ┗┛ ┗┛ ┗┛ ┗┛ ┗━┛ ┗━━━┛ ┗┛┗┛┗┛ ┗┛ ┗┛ ┗┛ ┗━┛
'''
    print("Guess the movie name in blanks from below options")
    print options
    print('Guesses Left: %d' % guesses)

movies = ['Rx100', 'padmavat', 'dil', 'stree']
guess_movie = movies[0]
guesses = 15

display = '_' * len(guess_movie)
display = list(display)
print(display)


def set_display(letter, indices):
    if indices:
        for i, index in enumerate(indices):
            display[index] = (letter + ' ')
    disp = " ".join(display)
    print(disp)

options = ('-----------------------------\n| A B C D E F G H I J K L M '
           '|\n| N O P Q R S T U V W X Y Z |\n|    0 1 2 3 4 5 6 7 8 9 '
           '   |\n-----------------------------')
clear()
# For first time, show blanks. next time set_display
print("_ " * len(guess_movie))

while guesses > 0:
    letter = raw_input("Guess a letter ")
    letter = letter.upper()
    options = options.replace(letter, ' ')
    if letter.upper() in guess_movie.upper():
        indices = [i for i, x in enumerate(guess_movie.upper())
                   if x == letter]
        clear()
        set_display(letter, indices)
        display = [i.strip() for i in display]
        if ''.join(display) == guess_movie.upper():
            print("YAY!!! You WON the game")
            break
    else:
        guesses -= 1
        indices = []
        clear()
        set_display(letter, indices)
        print("Oops! you have %s more guesses" % str(guesses))
        if guesses == 0:
            print("YOU LOSE :(")
