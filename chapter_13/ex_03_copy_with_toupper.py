import sys

if __name__ == '__main__':
    print('Enter the name of a text file:')
    name = input()
    print('Enter the name of output file:')
    copy_name = input()
    try:
        with open(name, 'r') as f:
            some_text = f.read()
        with open(copy_name, 'w') as fc:
                fc.write(some_text.upper())
                print('Done')
    except FileNotFoundError:
        print('Error. File not found')
        