import random


NUMB = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}


if __name__ == '__main__':
    random.seed()
    time = 1
    print(' 1   2   3   4   5   6   7   8   9   10')
    print('----------------------------------------')
    while(time <= 10):
        for i in range(0, 1000):
            n = random.randint(1, 10)
            if n in NUMB:
                NUMB[n] += 1
        for j in NUMB:
            print(f'{NUMB[j]:03}', end=' ')
            NUMB[j] = 0
        time += 1
        print()        
