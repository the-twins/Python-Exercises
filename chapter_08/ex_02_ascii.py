numb = 0
let = 64
stop = False
while True:
    print("Enter text to be analyzed (& to quit):")
    line = input()
    for i in line:
        ascii_value = ord(i)
        if(i == '&'):
            stop = True
            break               
        elif(ascii_value < 32):
            if(ascii_value == 9):
                print('\\t =', ascii_value, end = ' ')
            else:
                print('^', end = '')
                print(chr(let + ascii_value), '=', ascii_value, end = ' ')
            numb += 1 
        else:
            numb += 1
            print(i, '=', ascii_value, end = ' ')
            if(numb % 10 == 0):
                print()
    if(stop == True):
        break
    numb = 0
    print('\\n = 10')
    print()
