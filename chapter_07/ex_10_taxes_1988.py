def print_menu():
    """Print the menu."""
    print("Enter the number of your category:")
    print("1) Single (15% of first $17,850 plus 28% of excess)")
    print("2) Head of Household (15% of first $23,900 plus 28% of excess)")
    print("3) Married, Joint (15% of first $29,750 plus 28% of excess)")  
    print("4) Married, Separate (15% of first $14,875 plus 28% of excess)")
    print("5) quit")
    
    
RATE1 = 0.15
RATE2 = 0.28
TAX_BREAK_1 = 17850.0
TAX_BREAK_2 = 23900.0
TAX_BREAK_3 = 29750.0
TAX_BREAK_4 = 14875.0
tax = 0
tax_break = 0
while True:
    print_menu()
    numb = int(input())
    if(numb == 1):
        tax_break = TAX_BREAK_1
    elif(numb == 2):
        tax_break = TAX_BREAK_2
    elif(numb == 3):
        tax_break = TAX_BREAK_3
    elif(numb == 4):
        tax_break = TAX_BREAK_4
    elif(numb == 5):
        break
    else:
        print("Input error.")
        continue
    print("Enter your salary: ")
    salary = float(input())
    if(salary <= tax_break):
        tax = salary * RATE1
    else:
        tax = (tax_break * RATE1) + ((salary - tax_break) * RATE2)
    print("The gross pay =", salary, "the taxes =", tax, "and the net pay =", salary - tax)
    print()   
    