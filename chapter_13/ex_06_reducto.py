import sys


if __name__ == '__main__':
    LEN = 20
    print('Enter the name of a text file:')
    name = input()
    while(len(name) > LEN):
        print('The name is too long. No more than 20 characters. Try again:')
        name = input()
    try:
        with open(name, 'r') as f:
            some_data = f.read()
    except FileNotFoundError:
        print('Error. File not found')
        sys.exit(1)        
    copy_name = name[:15] + '.red'
    n = 0
    with open(copy_name, 'w') as f_c:
        for i in some_data:
            if(n % 3 == 0):
                f_c.write(i)
            n += 1
