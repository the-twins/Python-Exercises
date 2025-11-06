import sys


if __name__ == '__main__':
    mark = False
    numb = 1
    i = 0
    word = []
    with open('wordy', 'a+') as f:
        f.seek(0)
        while True:
            some_text = f.readline()
            i += 1
            if(len(some_text) == 0):
                break
        if(i > 0):
            numb = i
        print('Enter words to add to the file; press the #', end ='')
        print('key at the beginning of a line to terminate.')
        while True:
            words = input()
            for j in words:
                if(j == '#'):
                    mark = True
                    break
                elif j.isspace() == False:
                    word.append(j)
                else:
                    line = f'{numb}.{''.join(word)}\n'         
                    f.write(line)
                    numb += 1
                    word = []
            if(len(word) != 0):
                line = f'{numb}.{''.join(word)}\n'         
                f.write(line)
                numb += 1
                word = []                
            if(mark == True):
                break
    print('File contents:')
    try:
        with open('wordy', 'a+') as f:
            f.seek(0)
            some_text = f.read()
            print(some_text)
            print('Done!')
    except FileNotFoundError:
                print('Error. File "wordy" not found')
                sys.exit(1)
        