HOURLY_RATE_1 = 8.75
HOURLY_RATE_2 = 9.33
HOURLY_RATE_3 = 10.0
HOURLY_RATE_4 = 11.20
OVERTIME = 1.5
TAX_FIRST = 0.15
TAX_FIRST_SUM = 300
TAX_SECOND_SUM = 150
OVER_TAX = 450
TAX_SECOND = 0.2
TAX_THIRD = 0.25
HOURS_PER_WEEK = 40
total = 0
print('******************************************************************')
print('Enter the number corresponding to the desired pay rate or action:');
print('1) $8.75/hr   2) $9.33/hr')
print('3) $10.00/hr  4) $11.20/hr')
print('5) quit')
print('******************************************************************')
numb = int(input())
while True:
    match numb:
        case 1:
            print('Enter the number of hours worked:')
            hours = int(input())
            if(hours <= HOURS_PER_WEEK):
                total = hours * HOURLY_RATE_1
            else:
                total = (HOURS_PER_WEEK * HOURLY_RATE_1) + ((hours - HOURS_PER_WEEK) * 
                         HOURLY_RATE_1 * OVERTIME)
        case 2:
            print('Enter the number of hours worked:')
            hours = int(input())
            if(hours <= HOURS_PER_WEEK):
                total = hours * HOURLY_RATE_2
            else:
                total = (HOURS_PER_WEEK * HOURLY_RATE_2) + ((hours - HOURS_PER_WEEK) * 
                         HOURLY_RATE_2 * OVERTIME)
        case 3:
            print('Enter the number of hours worked:')
            hours = int(input())
            if(hours <= HOURS_PER_WEEK):
                total = hours * HOURLY_RATE_3
            else:
                total = (HOURS_PER_WEEK * HOURLY_RATE_3) + ((hours - HOURS_PER_WEEK) * 
                         HOURLY_RATE_3 * OVERTIME)
        case 4:
            print('Enter the number of hours worked:')
            hours = int(input())
            if(hours <= HOURS_PER_WEEK):
                total = hours * HOURLY_RATE_4
            else:
                total = (HOURS_PER_WEEK * HOURLY_RATE_4) + ((hours - HOURS_PER_WEEK) * 
                         HOURLY_RATE_4 * OVERTIME)
        case 5:
            break
        case _:  # This is the default case
            print(f'Unknown status code: {numb}. Try again:')
            numb = int(input())
            continue            
    tax = 0
    if(total <= TAX_FIRST_SUM):
        tax = total * TAX_FIRST
    elif(total <= OVER_TAX):
        tax = (TAX_FIRST_SUM * TAX_FIRST) + ((total - TAX_FIRST_SUM) * TAX_SECOND)
    else:
        tax = (TAX_FIRST_SUM * TAX_FIRST) + ( TAX_SECOND_SUM * TAX_SECOND) + ((total - OVER_TAX) * 
               TAX_THIRD)        
    print('The gross pay =', total, 'the taxes =', tax, 'and the net pay =', total - tax)
    print('******************************************************************')
    print('Enter the number corresponding to the desired pay rate or action:');
    print('1) $8.75/hr   2) $9.33/hr')
    print('3) $10.00/hr  4) $11.20/hr')
    print('5) quit')
    print('******************************************************************')
    numb = int(input())