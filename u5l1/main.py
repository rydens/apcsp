#!/usr/bin/env python3
import skilstak.colors as c
import math

print(c.green + "Hey, what's the range? Format it as 'x-y'")
startrange = input(c.cyan + '> ' + c.red).split('-')

while True:
    try:
        median = math.floor((int(startrange[0]) + int(startrange[1])) / 2)
    except ValueError:
        print(c.red + 'Wrong Format!')
        exit()

    
    print(c.green + 'Is your number higher or lower? Or even correct!?')
    print(median)
    answer = input(c.cyan + '> ' + c.red)
    if answer == 'higher':
        startrange[0] = median
    elif answer == 'lower':



