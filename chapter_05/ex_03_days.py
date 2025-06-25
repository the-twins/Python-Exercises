DAYS_IN_WEEK = 7
print("Enter the number of days: ")
days = int(input())
while(days > 0):
    print(days, 'days equals', days // DAYS_IN_WEEK, 'weeks and', days % DAYS_IN_WEEK, 'days')
    print("Try again (enter 0 to quite): ")
    days = int(input())
