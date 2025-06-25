MIN_IN_HOUR = 60
print("Enter time in minutes: ")
min = int(input())
while(min > 0):
    print("It's", min // MIN_IN_HOUR, "hours and", min % MIN_IN_HOUR, "minutes")
    print("Try again (enter 0 to quite): ")
    min = int(input())
    