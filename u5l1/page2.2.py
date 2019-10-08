#!/usr/bin/env python3
import math

startrange = [1, 7, 8, 9, 11, 12, 21, 22, 23, 24, 73, 73, 96, 99]

guesses = 0
print('What number should I try to guess, from the list?')
print('List: ' + str(startrange))
try:
    term = int(input('> '))
    if term not in startrange:
        print('Not in list!')
        exit()
except ValueError:
    print('A number, please!')
    exit()

while True:
    median = math.floor((int(startrange[0]) + int(startrange[-1])) / 2)
    if term > median:
        startrange[0] = median
        guesses += 1
    elif term < median:
        startrange[-1] =  median
        guesses += 1
    elif term == median:
        guesses += 1
        print('Position is ' + str(startrange.index(term)) + '; Got it in ' + str(guesses) + ' guesses!')
        exit()
