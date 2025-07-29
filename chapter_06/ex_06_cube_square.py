print("Enter lower limit: ")
up_limit = int(input())
print("Enter upper limit: ")
low_limit = int(input())
print('INTEGER  |      SQUARE       |     CUBE')
print('----------------------------------------')
for up_limit in range(up_limit, low_limit + 1):
    print(up_limit,'            ', end = '')
    print(up_limit ** 2,end = '')
    print('              ', up_limit ** 3)
    up_limit += 1
