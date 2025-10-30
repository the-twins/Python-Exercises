import sys


if __name__ == '__main__':
    ARSIZE = 1000
    if(len(sys.argv) < 2):
        print('Invalid input on command line')
        sys.exit(1)
    with open (sys.argv[1], "w") as f:
        for i in range(0, ARSIZE):
            numbers = 100.0 * i + 1.0 / (i + 1)
            f.write(str(numbers))
            f.write('\n')
    with open(sys.argv[1], "r") as f:
        print('Enter an index in the range 0 -', ARSIZE - 1)
        n = int(input())
        while(n >= 0 and n < ARSIZE):
            for i in range(0, n + 1):
                value = f.readline()
            print('The value there is', value)
            f.seek(0)
            print('Next index (out of range to quit):')
            n = int(input())
    print('Bye!')
    