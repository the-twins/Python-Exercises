numb = 65
i = 1
j = 1
col = 1
for i in range(1, 7):
    for j in range(1, col + 1):
        ch = chr(numb)
        print(ch, end = '') 
        j += 1
        numb += 1        
    print()
    i += 1
    col += 1
    j = 1
