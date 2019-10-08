# Now this is a library, because the whole thing is now supposed to be a function, that actually returns something.
import math

def posOfNumber(term: int, sortedList: list):
    guesses = 0
    while True:
        median = math.floor((int(sortedList[0]) + int(sortedList[-1])) / 2)
        guesses += 1
        if term > median:
            sortedList[0] = median
        elif term < median:
            sortedList[-1] =  median
        elif term == median:
            try:
                return 'Position is ' + str(sortedList.index(term)) + '; Got it in ' + str(guesses) + ' guesses!'
            except ValueError:
                return str(term) + ' is not in list!'

# This down here is just for demonstration purposes, this file could easily be imported into an actual program
if __name__ == '__main__': # If this file, specifically, is actually run
    myList = [1, 7, 8, 9, 11, 12, 21, 22, 23, 24, 73, 73, 96, 99]
    print('Which number to look for?')
    item = int(input('> '))
    position = posOfNumber(item, myList)
    print(position)
