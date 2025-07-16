i = 1
j = 1
col = 1
for i in range(1, 6):
    for j in range(1, col + 1):
        ch = chr(numb)
        print('$', end = '') 
        j += 1        
    print()
    i += 1
    col += 1
    j = 1
