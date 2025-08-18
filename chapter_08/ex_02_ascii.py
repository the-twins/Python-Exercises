numb = 0
stop = False
while True:
    print("Enter text to be analyzed (& to quit):")
    line = input()
    for i in line:
        if(i == '&'):
            stop = True
            break
        elif(i == '\t'):
            print(i, '= \\t', end = ' ')
            numb += 1
        else:
            ascii_value = ord(i)
            numb += 1
            print(i, '=', ascii_value, end = ' ')
            if(numb % 10 == 0):
                print()
    if(stop == True):
        break
    numb = 0
    print('\\n')
    print()
    