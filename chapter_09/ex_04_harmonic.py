def harmonic(first: float, second: float) -> float:
    """Returns the harmonic mean of the two numbers"""
    if((1 / first + 1 / second) == 0):
        print("Input error. You can't divide by 0.")
    else:
        return 2 / (1 / first + 1 / second)
    
    
if __name__ == '__main__':
    print('Enter first float:')
    first = float(input())
    print('Enter second float:')
    second = float(input())
    if(first == 0 or second == 0):
        print('Input error. Bye.')
    else:
        print(round(harmonic(first, second), 2))
