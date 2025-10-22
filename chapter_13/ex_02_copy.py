import sys

if __name__ == '__main__':
    print('Enter the file name:')
    name = input()
    try:
        with open(name, 'rb') as f:
            some_text = f.read()
            count = len(some_text)
            if(count == 0):
                print("Can't open", name, "or the file does not contain character")
            else:
                with open(sys.argv[1], 'wb') as fc:
                    fc.write(some_text)
                    print('Done')
    except FileNotFoundError:
        print('Error. File not found')
    except Exception:
        print('Invalid input on command line')
        