numb = 0
stop = False
while True:
    print("Enter text to be analyzed (# to quit):")
    line = input()
    for i in line:
        if(i == '#'):
            stop = True
            break
        else:
            ascii_value = ord(i)
            numb += 1
            print(i, '=', ascii_value, end = ' ')
            if(numb % 8 == 0):
                print()
    if(stop == True):
        break
    print()
