sum_one = 1.0
sum_two = 1.0
print("Enter the limit integer: ")
limit = int(input())
while(limit > 0):
    for i in range (2, limit + 1):
        sum_one += 1.0 / i
        if(i % 2 > 0):
            sum_two += 1.0 / i
        else:
            sum_two -= 1.0 / i
    print("1.0 + 1.0/2.0 + 1.0/3.0 + 1.0/4.0 + ... =", sum_one)
    print("1.0 - 1.0/2.0 + 1.0/3.0 - 1.0/4.0 + ... =", sum_two)
    sum_one = 1.0
    sum_two = 1.0
    print("Enter the limit integer or 0 to quit: ")
    limit = int(input())
