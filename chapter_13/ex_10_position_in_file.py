import sys

if __name__ == '__main__':
    print('Enter the name of the text file:')
    name = input()
    try:
        with open(name, 'r') as f:
            some_text = f.read()
            max_numb = len(some_text)
            while True:
                print('Enter a file position (negative number to quit):')
                numb = int(input())
                if(numb > max_numb):
                    print('The position in the file must not exceed', max_numb)
                    continue
                if(numb < 0):
                    break
                f.seek(numb)
                some_text = f.read()
                for i in some_text:
                    if (i == '\n'):
                        break
                    print(i, end='')
                print()
            print('Bye!')
    except FileNotFoundError:
        print('Error. File not found')
        sys.exit(1)     
                