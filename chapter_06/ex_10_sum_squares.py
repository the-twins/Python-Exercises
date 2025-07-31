sum = 0
print("Enter lower and upper integer limits: ")
low_limit = int(input())
up_limit = int(input())
while (up_limit > low_limit):
    for i in range(low_limit, up_limit + 1):
        sum += i ** 2
    print("The sums of the squares from", low_limit ** 2, "to", up_limit ** 2, "is", sum)
    sum = 0
    print("Enter next set of limits: ")
    low_limit = int(input())
    up_limit = int(input())
print("Done")
