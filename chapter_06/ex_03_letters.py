numb = 70
i = 1
j = 1
for i in range(1, 7):
    for j in range(1, i + 1):
        ch = chr(numb)
        print(ch, end = '')
        numb -= 1        
    print()
    numb = 70
