MAX_SYMB = 255
i = 0
print('Enter a string of no more than 255 characters: ')
line = input()
for n in reversed(line):
    print(n, end = '')
    i += 1
    if(i > MAX_SYMB):
        print('\nYou have entered too many characters. Bye.')
        break
