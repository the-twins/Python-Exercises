if __name__ == '__main__':
    while True:
        try:
            print('Enter string or empty line to quit:')
            text = input()
            if(text == ''):
                break
            print('Enter substring for searching:')
            word = input()
            index = text.index(word)
            print(index)
        except ValueError:
            print('Not found')
