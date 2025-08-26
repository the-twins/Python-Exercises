def print_menu():
    """Print the menu."""
    print("Enter the operation of your choice:")
    print("a. add        s. subtract")
    print("m. multiply   d. divide")
    print("q. quit")
    
    
def input_check()->float:
    """Input validation and return values."""
    while True:
        try:
            first_numb = float(input())
        except ValueError:
            first_numb = None
        if(first_numb == None):
            print("Input is not correct, please enter a number, such as 2.5, -1.78E8, or 3:")
        else:
            break
    print("Enter a second float: ")
    while True:
        try:
            second_numb = float(input())
        except ValueError:
            second_numb = None
        if(second_numb == None):
            print("Input is not correct, please enter a number, such as 2.5, -1.78E8, or 3:")
        else:
            break
    return first_numb, second_numb
            
    
print_menu()   
choice = input()
while(choice != 'q'):
    if(choice == 'a'):
        print("Enter first number: ")
        first, second = input_check()
        print(first, "+", second, "=", first + second)
    elif(choice == 's'):
        print("Enter first number: ")
        first, second = input_check()
        print(first, "-", second, "=", first - second)
    elif(choice == 'm'):
        print("Enter first number: ")
        first, second = input_check()
        print(first, "*", second, "=", first * second)
    elif(choice == 'd'):
        print("Enter first number: ")
        first, second = input_check()
        if(second == 0):
            print("Input error. You can't divide by 0. Enter a second float:")
            try:
                second = float(input())
            except ValueError:
                second = None
            while(second == None):
                print("Input error. Try entering the second float again:")
                second = float(input())
        print(first, "/", second, "=", first / second)
    else:
        print("Input error. Try again:")
        choice = input()
        continue
    print_menu()
    choice = input()
print("Bye!")
