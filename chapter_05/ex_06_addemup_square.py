money = 1
sum = 0
print('Enter the number of days: ')
days = int(input())
i = 1
while(i <= days):
    earn = money ** 2
    print('In', i, 'days you will earn', earn, 'dollars.')
    i += 1
    sum += earn
    money += 1
print('For all days you will earn', sum, 'dollars.')
