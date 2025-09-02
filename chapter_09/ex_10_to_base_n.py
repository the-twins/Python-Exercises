def to_base_n(numb: int, second_numb: int):
    """Prints the number that is its first argument to the number base given by the second 
    argument"""
    n = numb % second_numb
    if(numb >= second_numb):
        to_base_n(numb // second_numb, second_numb);
    print(n, end='')


if __name__ == '__main__':
    while True:
        try: 
            print('\nEnter an integer (q to quit):')
            numb = int(input())
            print('Enter second integer in the range 2-10 (q to quit):')
            second_numb = int(input())
            print('Equivalent: ')
            to_base_n(numb, second_numb)
        except ValueError:
            print('Bye!')
            break  
