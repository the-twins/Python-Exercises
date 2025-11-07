import sys


def count(text: str, ch: str) -> int:
    """Returnes count of the character"""
    count = 0
    for i in text:
        if(i == ch):
            count += 1
    return count


if __name__ == '__main__':
    if(len(sys.argv) <= 1):
        print('Invalid input on command line')
        sys.exit(1)
    if(len(sys.argv) == 2):
        print('Enter text to count the number of characters:')
        text = input()
        print('This text contains', count(text, sys.argv[1]), 'characters', sys.argv[1])
    else:
        numb = len(sys.argv)
        for i in range (2, numb):
            try:
                with open(sys.argv[i], 'r') as f:
                    text = f.read()
                    print('File', sys.argv[i], 'contains', count(text, sys.argv[1]), 'characters',
                          sys.argv[1])
            except FileNotFoundError:
                print('Error. File', sys.argv[i],'not found')           
                