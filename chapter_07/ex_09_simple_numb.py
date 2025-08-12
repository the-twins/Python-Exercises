mark = True
print('Enter a positive integer:')
numb = int(input())
for i in range(2, numb + 1):
    if(i == 2):
        print(i, 'is a prime number')
        continue
    if(i == 3):
        print(i, 'is a prime number')
        continue
    for j in range(2, int(i / 2 + 2)):
        if(i % j == 0):
            mark = False
            break
    if(mark == True):
        print(i, 'is a prime number')
    mark = True
