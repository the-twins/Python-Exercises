mark = True
print('Enter a positive integer:')
numb = int(input())
for i in range(2, numb + 1):
    for j in range(2, i // 2 + 1):
        if(i % j == 0):
            mark = False
            break
    if(mark == True):
        print(i, 'is a prime number')
    mark = True
