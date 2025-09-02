def Fibonacci(numb: int):
    """Prints Fibonacci numbers"""
    first = 0
    sec = 1
    fib_numb = 0
    print(first)
    if(numb > 1):
        print(sec)
    for i in range(1, numb - 1):
        fib_numb = first + sec
        print(fib_numb)
        first = sec
        sec = fib_numb
    
    
if __name__ == '__main__':
    print("Enter an integer:")
    numb = int(input())
    if(numb <= 0):
        print('Bye!')
    else:
        print('Fibonacci numbers:')
        Fibonacci(numb)
    