#!/usr/bin/env python3
import skilstak.colors as c
import math

print(c.base2 + "Ryan Densmore's U5L1 Number Guesser\n")
print(c.blue + 'Think of a number, and let me guess it!')
print(c.green + "What's the range of numbers it's in? Format it as 'x-y'")
startrange = input(c.cyan + '> ' + c.red).split('-')

if int(startrange[1]) < int(startrange[0]):
    print(c.red + "Wrong Format!")
    print(c.magenta + 'Reload to play again!')
    exit()

guesses = 0

while True:
    try:
        median = math.floor((int(startrange[0]) + int(startrange[1])) / 2)
    except ValueError:
        print(c.red + 'Wrong Format!')
        print(c.magenta + 'Reload to play again!')
        exit()

    
    print(c.green + 'Is your number ' + c.cyan + 'higher ' + c.green + 'or' + c.cyan + ' lower' + c.green + '? Or even ' + c.cyan + 'correct' + c.green + '!?')
    print(median)
    answer = input(c.cyan + '> ' + c.red).lower()
    if answer == 'higher':
        startrange[0] = median
        guesses += 1
    elif answer == 'lower':
        startrange[1] =  median
        guesses += 1
    elif answer == 'correct':
        guesses += 1
        print(c.green + 'Awesome! Good Game. Got it in ' + c.cyan + str(guesses) + c.green + ' guesses!')
        print(c.magenta + 'Reload to play again!')
        exit()
    else:
        print(c.red + 'Not an option!')
