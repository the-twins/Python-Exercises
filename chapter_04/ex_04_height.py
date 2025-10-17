if __name__ == '__main__':
    INCH_IN_FEET = 12.0
    print('Enter your name:')
    name = input()
    print('Enter your height in inches:')
    height = float(input())
    print(f'{name} you are {height / INCH_IN_FEET} feet tall')
    