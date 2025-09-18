def one_word(some_text: str, numb: int):
    """ Reads the first word from a line of input an array and discards the rest of the line and
    accepts a second parameter specifying the maximum number of characters that can be read"""
    word = []
    count = 0
    mark_word = False
    for i in some_text:
        if i.isspace() == False and count < n:
            word.append(i)
            count += 1
            mark_word = True
        else:
            if(mark_word == True):
                break
    print(''.join(word))
    
    
if __name__ == '__main__':
    print('Enter the word length:')
    n = int(input())
    print('Enter text:')
    some_text = input()
    one_word(some_text, n)
    