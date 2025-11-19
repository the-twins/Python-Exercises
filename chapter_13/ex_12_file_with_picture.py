import sys


if __name__ == '__main__':
    picture = []
    try:
        with open('picture.txt', 'r') as f:
            some_text = f.read()
            for i in some_text:
                if i == '0':
                    picture.append(' ')
                elif i == '1':
                    picture.append('.')
                elif i == '2':
                    picture.append("'")
                elif i == '3':
                    picture.append(',')
                elif i == '4':
                    picture.append(':')
                elif i == '5':
                    picture.append('*')
                elif i == '6':
                    picture.append('=')
                elif i == '7':
                    picture.append('@')
                elif i == '8':
                    picture.append('%')
                elif i == '9':
                    picture.append('#')
                elif i == '\n':
                    picture.append('\n')
    except FileNotFoundError:
        print('Error. File not found')
        sys.exit(1)
    result_string = ''.join(picture)
    with open('new_picture.txt', 'w') as f:
        f.write(result_string)
    print(result_string)
