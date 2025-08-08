count_numb_even = 0
count_numb_odd = 0
sum_even_numb = 0
sum_odd_numb = 0
print("Enter integer ('0' to quit):")
while True:
    numb = int(input())
    if(numb == 0):
        break 
    if(numb % 2 == 0):
        count_numb_even += 1
        sum_even_numb += numb
    if(numb % 2 != 0):
        count_numb_odd += 1
        sum_odd_numb += numb
if(count_numb_even == 0):
    print("You can't divide by 0.")
else:
    print('The total number of even integers =', count_numb_even, 'the average value of the even '
          'integers =', sum_even_numb / count_numb_even)
if(count_numb_odd == 0):
    print("You can't divide by 0.")
else:
    print('The total number of odd integers =', count_numb_odd, 'the average value of the odd '
          'integers =', sum_odd_numb / count_numb_odd)
