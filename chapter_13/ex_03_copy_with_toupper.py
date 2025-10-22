import sys

if __name__ == '__main__':
    print('Enter the name of a text file:')
    name = input()
    print('Enter the name of output file:')
    copy_name = input()
    try:
        with open(name, 'rb') as f:
            some_text = f.read()
            count = len(some_text)
            if(count == 0):
                print("Can't open", name, "or the file does not contain character")
            else:
                with open(copy_name, 'wb') as fc:
                    fc.write(some_text.upper())
                    print('Done')
    except FileNotFoundError:
        print('Error. File not found')
        