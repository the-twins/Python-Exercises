if __name__ == '__main__':
    while True:
        print('Enter string or empty line to quit:')
        text = input()
        if(text == ''):
            break
        for i in reversed(text):
            print(i, end='')
        print()
        