if __name__ == '__main__':
    print('Enter your name:')
    name = input()
    print('Enter your surname:')
    surname = input()
    n = len(name)
    s = len(surname)
    print(f'{name} {surname}')
    print(f'{n:>{n}} {s:>{s}}'.format(n, s))
    print(f'{name} {surname}')
    print(f'{n:<{n}} {s:<{s}}'.format(n, s))
    