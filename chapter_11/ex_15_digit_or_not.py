digit = True
if __name__ == '__main__':
    while True:
        print('Enter string or empty line to quit:')
        text = input()
        if(text == ''):
            break
        clean_text = text.strip()
        if not clean_text.isnumeric():
            print('Not a number.')
        else:
            print('A number.')
