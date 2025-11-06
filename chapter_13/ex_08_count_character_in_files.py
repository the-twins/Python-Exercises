import sys


if __name__ == '__main__':
    count = 0
    ch = sys.argv[1]
    if(len(sys.argv) < 2):
        print('Invalid input on command line')
        sys.exit(1)
    elif(len(sys.argv) == 2):
        try:
            print('Enter the file name:')
            name = input()
            with open(name, 'r') as f:
                some_text = f.read()
                for i in some_text:
                    if(i == ch):
                        count += 1
            print('File', name, 'contains', count, 'characters', ch)
        except FileNotFoundError:
            print('Error. File', name,'not found')
            sys.exit(1)
    else:
        numb = len(sys.argv)
        for i in range (2, numb):
            try:
                with open(sys.argv[i], 'r') as f:
                    some_text = f.read()
                    for j in some_text:
                        if(j == ch):
                            count += 1
                    print('File', sys.argv[i], 'contains', count, 'characters', ch)
                    count = 0
            except FileNotFoundError:
                print('Error. File', sys.argv[i],'not found')           
                