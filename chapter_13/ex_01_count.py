import sys

if __name__ == '__main__':
    print('Enter the file name:')
    name = input()
    try:
        with open(name, 'r') as f:
            some_text = f.read()
            count = len(some_text)
            if(count == 0):
                print("Can't open", name, "or the file does not contain character")
            else:
                print(some_text)
                print('File', name, 'has', count, 'characters')
    except FileNotFoundError:
        print('Error. File', name, 'not found')
    