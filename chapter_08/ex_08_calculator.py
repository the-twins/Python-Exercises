def print_menu():
    """Print the menu."""
    print("Enter the operation of your choice:")
    print("a. add        s. subtract")
    print("m. multiply   d. divide")
    print("q. quit")
    
    
def float_input() -> float:
    """Input validation and return values."""
    print("Enter number: ")
    while True:
        try:
            return float(input())
        except ValueError:
            print("Input is not correct, please enter a number, such as 2.5, -1.78E8, or 3:")
    

def get_choice() -> str:
    """Input validation and return values."""
    print_menu()
    while True:
        choice = input()
        if choice in ['a', 's', 'm', 'd', 'q']:  
            return choice
        print("Input error. Try again.")
        print_menu()
        
        
if __name__ == '__main__':
    choice = get_choice()   
    while(choice != 'q'):
        first = float_input()
        second = float_input()
        if(choice == 'a'):
            print(first, "+", second, "=", first + second)
        elif(choice == 's'):
            print(first, "-", second, "=", first - second)
        elif(choice == 'm'):
            print(first, "*", second, "=", first * second)
        elif(choice == 'd'):
            while(second == 0):
                print("Input error. You can't divide by 0. Enter a second float:")
                second = float_input()
            print(first, "/", second, "=", first / second)
        choice = get_choice()
    print("Bye!")
