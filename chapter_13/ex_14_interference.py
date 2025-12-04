import sys


SYMB = {0: ' ', 1: '.', 2: "'", 3: ',', 4: ':', 5: '*', 6: '=', 7: '@', 8: '%', 9: '#'}
        
        
if __name__ == '__main__':
    all_sum = 0
    n = 0
    mark = False
    picture = []
    some_text = []
    try:
        with open('picture_inter.txt', 'r') as f:
            while True:
                some_line = f.readline()
                if not some_line:
                    break           
                some_text.append(some_line)
                max_line = len(some_line)
        some_text_c = [s.strip() for s in some_text]                
        for i in range(0, len(some_text_c)):
            for j in range(0, max_line):
                if(i > 0):
                    all_sum += int(some_text_c[i - 1][j])
                    n += 1
                    if(abs(int(some_text_c[i][j]) - int(some_text_c[i - 1][j])) > 1):
                        mark = True
                if(j > 0):
                    all_sum += int(some_text_c[i][j - 1])
                    n += 1
                    if(abs(int(some_text_c[i][j]) - int(some_text_c[i][j - 1])) > 1):
                        mark = True
                if(i != len(some_text_c) - 1):
                    all_sum += int(some_text_c[i + 1][j])
                    n += 1
                    if(abs(int(some_text_c[i][j]) - int(some_text_c[i + 1][j])) > 1):
                        mark = True
                if(j != max_line - 1):
                    all_sum += int(some_text_c[i][j + 1])
                    n += 1
                    if(abs(int(some_text_c[i][j]) - int(some_text_c[i][j + 1])) > 1):
                        mark = True
                if(mark == True):
                    symb = int(all_sum / n)
                else:
                    symb = int(some_text_c[i][j])                  
                picture.append(SYMB.get(symb, ' '))
                all_sum = 0
                n = 0
                mark = False 
            picture.append('\n')             
    except FileNotFoundError:
        print('Error. File not found')
        sys.exit(1)
    result_string = ''.join(picture)
    with open('new_picture_interf.txt', 'w') as f:
        f.write(result_string)
    print(result_string)
