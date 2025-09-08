def harmonic(first: float, second: float) -> float:
    """Returns the harmonic mean of the two numbers"""
    return 2 / (1 / first + 1 / second)
    
    
if __name__ == '__main__':
    print('Enter first float:')
    first = float(input())
    print('Enter second float:')
    second = float(input())
    try:
        print(round(harmonic(first, second), 2))
    except ZeroDivisionError:
        print("Input error. You can't divide by 0.")
    