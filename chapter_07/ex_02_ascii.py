text = ''
numb = 0
stop = False
while True:
    line = input()
    if(line):
        text += line
        for i in text:
            if(i == '#'):
                stop = True
            else:
                ascii_value = ord(i)
                numb += 1
                print(i, '=', ascii_value, end = ' ')
                if(numb % 8 == 0):
                    print()
    if(stop == True):
        break
