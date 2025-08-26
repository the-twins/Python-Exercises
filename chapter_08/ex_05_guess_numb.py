mid = 50
max = 100
min = 1
guess = mid
print("Pick an integer from 1 to 100. I will try to guess ")
print("it.\nRespond with 'h' if my guess is low, 'l' if my ")
print("guess is high and 'y' if my guess is right.")
print("Uh...is your number", mid)
ans = input()
while(ans != 'y'):
    if(ans == 'h'):
        if(mid == 99):
            print("Well, then, is it 100?")
            ans = input()
            break
        min = mid
        mid += int((max - min) / 2)
        print("Well, then, is it", mid, "?")
    elif(ans == 'l'):
        if(mid == 2):
            print("Well, then, is it 1?")
            ans = input()
            break
        max = mid
        mid -= int((max - min) / 2)
        print("Well, then, is it", mid, "?")
    else:
        print("Input error. Try again:")
    ans = input()
print("I knew I could do it!")
