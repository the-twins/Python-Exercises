def one_word(some_text: str):
    """ Reads the first word from a line of input an array and discards the rest of the line"""
    word = ""
    mark_word = False
    for i in some_text:
        if i.isalpha() == True:
            word += i
            mark_word = True
        else:
            if(mark_word == True):
                break
    print(word)
    
    
if __name__ == '__main__':
    print('Enter text:')
    some_text = input()
    one_word(some_text)
    