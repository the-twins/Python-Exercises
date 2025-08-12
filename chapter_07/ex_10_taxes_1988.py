RATE1 = 0.15
RATE2 = 0.28
TAX_BREAK_1 = 17850.0
TAX_BREAK_2 = 23900.0
TAX_BREAK_3 = 29750.0
TAX_BREAK_4 = 14875.0
tax = 0
print("Enter the number of your category:")
print("1) Single (15% of first $17,850 plus 28% of excess)")
print("2) Head of Household (15% of first $23,900 plus 28% of excess)")
print("3) Married, Joint (15% of first $29,750 plus 28% of excess)")  
print("4) Married, Separate (15% of first $14,875 plus 28% of excess)")
print("5) quit")
while True:
    numb = int(input())
    if(numb == 1):
        print("Enter your salary: ")
        salary = float(input())
        if(salary <= TAX_BREAK_1):
            tax = salary * RATE1
        else:
            tax = (TAX_BREAK_1 * RATE1) + ((salary - TAX_BREAK_1) * RATE2)
        print("The gross pay =", salary, "the taxes =", tax, "and the net pay =", salary - tax)
    if(numb == 2):
        print("Enter your salary: ")
        salary = float(input())
        if(salary <= TAX_BREAK_2):
            tax = salary * RATE1
        else:
            tax = (TAX_BREAK_2 * RATE1) + ((salary - TAX_BREAK_2) * RATE2)
        print("The gross pay =", salary, "the taxes =", tax, "and the net pay =", salary - tax)
    if(numb == 3):
        print("Enter your salary: ")
        salary = float(input())
        if(salary <= TAX_BREAK_3):
            tax = salary * RATE1
        else:
            tax = (TAX_BREAK_3 * RATE1) + ((salary - TAX_BREAK_3) * RATE2)
        print("The gross pay =", salary, "the taxes =", tax, "and the net pay =", salary - tax)
    if(numb == 4):
        print("Enter your salary: ")
        salary = float(input())
        if(salary <= TAX_BREAK_4):
            tax = salary * RATE1
        else:
            tax = (TAX_BREAK_4 * RATE1) + ((salary - TAX_BREAK_4) * RATE2)
        print("The gross pay =", salary, "the taxes =", tax, "and the net pay =", salary - tax)
    if(numb == 5):
        break
    print("Enter the number of your category:")
    print("1) Single (15% of first $17,850 plus 28% of excess)")
    print("2) Head of Household (15% of first $23,900 plus 28% of excess)")
    print("3) Married, Joint (15% of first $29,750 plus 28% of excess)")  
    print("4) Married, Separate (15% of first $14,875 plus 28% of excess)")
    print("5) quit")
    