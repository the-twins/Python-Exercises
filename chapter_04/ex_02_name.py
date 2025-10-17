if __name__ == '__main__':
    print('Enter your name:')
    name = input()
    a = len(name)
    a += 3
    print('"{}"'.format(name))
    print('"{:20}"'.format(name))
    print('"{:>20}"'.format(name))
    print('"{}   "'.format(name))
    