import sys

if __name__ == '__main__':
    print('Enter the name of the first text file:')
    name_one = input()
    print('Enter the name of the second text file:')
    name_two = input()
    try:
        with open(name_one, 'r') as f_one, open(name_two, 'r') as f_two :
            while True:
                line = f_one.readline()
                line_two = f_two.readline()
                if not line and not line_two:
                    break
                if not line:
                    continue
                else:
                    print(line.replace('\n', ''))
                if not line_two:
                    continue
                else:
                    print(line_two.replace('\n', ''))
    except FileNotFoundError:
        print('Error. File not found')
        sys.exit(1)
        