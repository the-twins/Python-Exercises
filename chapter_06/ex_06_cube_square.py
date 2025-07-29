print("Enter lower limit: ")
low_limit = int(input())
print("Enter upper limit: ")
up_limit = int(input())
print('INTEGER  |      SQUARE       |     CUBE')
print('----------------------------------------')
for i in range(low_limit, up_limit + 1):
    print(low_limit,'            ', end = '')
    print(low_limit ** 2, end = '')
    print('              ', low_limit ** 3)
    low_limit += 1
