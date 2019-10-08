#!/usr/bin/env python3

list = [8, 92, 36, 5, 87, 1, 9, 5, 6, 8]
print('List: ' + str(list))

print('Number to search for:')
try:
    term = int(input('> '))
except ValueError:
    print('Not a number!')
    exit()
try:
    print('Number ' + str(term) + ' is earliest located at index ' + str(list.index(term)))
except ValueError:
    print(str(term) + ' is not in list!')
