money = 1
sum = 0
print('Enter the number of days: ')
days = int(input())
all_days = days
while(days > 0):
    sum += money
    money += 1
    days -= 1
print('In', all_days, 'days you will earn', sum, 'dollars.')
