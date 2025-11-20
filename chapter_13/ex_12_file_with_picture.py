import sys


SYMB = {'0': ' ', '1': '.', '2': "'", '3': ',', '4': ':', '5': '*', '6': '=', '7': '@', '8': '%',
        '9': '#', '\n': '\n'}
        
        
if __name__ == '__main__':
    picture = []
    try:
        with open('picture.txt', 'r') as f:
            some_text = f.read()
            for i in some_text:
                picture.append(SYMB.get(i, ' '))
    except FileNotFoundError:
        print('Error. File not found')
        sys.exit(1)
    result_string = ''.join(picture)
    with open('new_picture.txt', 'w') as f:
        f.write(result_string)
    print(result_string)
