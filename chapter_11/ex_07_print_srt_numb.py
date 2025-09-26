if __name__ == '__main__':
    while True:
        print('Enter string or empty line to quit:')
        text = input()
        if(text == ''):
            break
        print('Enter a number:')
        numb = int(input())
        print(text[:numb])
