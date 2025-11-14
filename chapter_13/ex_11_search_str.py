import sys


if __name__ == '__main__':
    if(len(sys.argv) <= 2):
        print('Invalid input on command line')
        sys.exit(1)
    try:
        with open(sys.argv[2], 'r') as f:
            while True:
                some_text = f.readline()
                if not some_text:
                    break
                if sys.argv[1] in some_text:
                    print(some_text.replace('\n', ''))
    except FileNotFoundError:
        print('Error. File not found')
        sys.exit(1)     
                