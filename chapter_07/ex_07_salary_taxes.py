HOURLY_RATE = 10.0
OVERTIME = 1.5
TAX_FIRST = 0.15
TAX_FIRST_SUM = 300
TAX_SECOND_SUM = 150
OVER_TAX = 450
TAX_SECOND = 0.2
TAX_THIRD = 0.25
HOURS_PER_WEEK = 40
print('Enter the number of hours worked:')
hours = int(input())
total = 0
tax = 0
if(hours <= HOURS_PER_WEEK):
    total = hours * HOURLY_RATE
else:
    total = (HOURS_PER_WEEK * HOURLY_RATE) + ((hours - HOURS_PER_WEEK) * HOURLY_RATE * OVERTIME)
if(total <= TAX_FIRST_SUM):
    tax = total * TAX_FIRST
elif(total <= OVER_TAX):
    tax = (TAX_FIRST_SUM * TAX_FIRST) + ((total - TAX_FIRST_SUM) * TAX_SECOND)
else:
    tax = (TAX_FIRST_SUM * TAX_FIRST) + ( TAX_SECOND_SUM * TAX_SECOND) + ((total - OVER_TAX) * 
           TAX_THIRD)        
print('The gross pay =', total, 'the taxes =', tax, 'and the net pay =', total - tax)
