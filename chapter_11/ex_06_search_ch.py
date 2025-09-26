if __name__ == '__main__':
    while True:
        print('Enter string or empty line to quit:')
        text = input()
        if(text == ''):
            break
        print('Enter a character for searching:')
        ch = input()
        if ch in text:
            print('Found')
        else:
            print('Not found')
