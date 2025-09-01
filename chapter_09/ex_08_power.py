def power(n: float, p: int) -> float:
    """Raises numbers to integer powers"""
    pow = 1
    for i in range(1, abs(p) + 1):
        pow *= n
    if(p < 0):
        if(n == 0):
            return 0
        return 1 / pow
    return pow
    
    
if __name__ == '__main__':
    while True:
        try: 
            print('Enter a number:')
            n = float(input())
            print('Enter an integer power to which the first number will be raised '
                  '(letter to quit):')
            p = int(input())
            print(n, 'to the power', p, 'is', power(n, p))
            print('Try again or letter to quit')
        except ValueError:
            print('You enter letter. Hope you enjoyed this power trip -- bye!')
            break
            