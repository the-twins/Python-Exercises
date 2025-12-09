import random


if __name__ == '__main__':
    random_integer = []
    for i in range(0, 100):
        random_integer.append(random.randint(1, 10))
    random_integer.sort(reverse=True)
    print(random_integer)
    