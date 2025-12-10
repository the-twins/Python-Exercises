import random


def rollem(numb_set: int, dice: int, sides: int):
    """Prints the result"""
    one = 0
    print('Here are', numb_set, 'sets of', dice, sides, end='-sides throws.\n')
    for i in range(0, numb_set):
        for j in range(0, dice):
            one += random.randint(1, sides)
        print(one, end=' ')
        one = 0


if __name__ == '__main__':
    random.seed()
    print('Enter the number of sets (q to stop): ')
    try:
        numb_set = int(input())
        while(numb_set > 0):
            print('How many sides (no less than 2)?')
            sides = int(input())
            if(sides < 2):
                print('Needs at least 2 sides.')
                break
            print('How many dice (no less than 1)?')
            dice = int(input())
            if(dice < 1):
                print('Need at least 1 die.')
                break
            rollem(numb_set, dice, sides)
            print('\nEnter the number of sets (q to stop): ')
            numb_set = int(input())            
    except ValueError:
        print('GOOD FORTUNE TO YOU!')
    print('Bye.')
    