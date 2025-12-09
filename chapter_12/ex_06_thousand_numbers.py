import random


if __name__ == '__main__':
    random_integer = []
    count = 0
    for i in range(0, 1000):
        random_integer.append(random.randint(1, 10))
    for i in range(1, 11):
        for j in random_integer:
            if(i == j):
                count += 1
        print(i, 'appears', count, 'times.')
        count = 0        
    