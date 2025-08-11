count = 0
ei = False
stop = False
while True:
    line = input()
    for i in line:
        if(i != 'i'):
            ei = False
        if(i == 'i'):
            if(ei == True):
                count += 1
                ei = False
        if(i == '#'):
            stop = True
            break
        if(i == 'e'):
            ei = True
    if(stop == True):
        break
print('The', count, 'times the sequence "ei" occurs.')
