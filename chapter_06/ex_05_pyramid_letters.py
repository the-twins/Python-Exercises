code_ch_l = 65
code_ch_r = 64
print('Enter any capital letter: ')
ch = str(input())
letter_code = ord(ch)
i = 1
j = 1
g = 1
col = 1
space = ' '
numb = letter_code - code_ch_r
numb_space = numb
numb_lett_r = 1
for i in range(1, numb + 1):
    print(numb_space * space, end = '') 
    for j in range(1, col + 1):
        print(chr(code_ch_l), end = '')
        code_ch_l += 1
        code_ch_temp = code_ch_r
        if(j < i):
            j += 1
        else:
            for g in range(1, numb_lett_r):
                print(chr(code_ch_r), end = '')
                code_ch_r -= 1
                if(g < i - 1):
                    g += 1                
    print()
    numb_space -= 1
    code_ch_l = 65
    code_ch_r = code_ch_temp + 1
    numb_lett_r += 1
    i += 1
    col += 1
    j = 1
    g = 1
    