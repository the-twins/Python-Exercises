import sys

print("Enter a first float: ")
try:
    first_numb = float(input())
except ValueError:
    first_numb = None
while first_numb is not None:
    print("Enter a second float: ")
    second_numb = float(input())
    if(first_numb * second_numb == 0):
        print('Error: Division by 0')
        sys.exit(1)
    print((first_numb - second_numb) / (first_numb * second_numb))
    print("Enter a first float or q to quit: ")
    try:
        first_numb = float(input())
    except ValueError:
        first_numb = None
