import sys


if __name__ == '__main__':
    numb = len(sys.argv)
    if(numb < 2):
        print('Invalid input on command line')
    for i in range(1, numb):
        with open(sys.argv[i], 'r') as f:
            some_data = f.read()
            print(some_data)
            