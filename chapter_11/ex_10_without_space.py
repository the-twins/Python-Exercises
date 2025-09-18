def del_space(some_text: str):
    """Takes a string as an argument and removes the spaces from the string."""
    word = []
    for i in some_text:
        if i.isspace() == True:
            continue
        else:
            word.append(i)   
    print(''.join(word))
    
    
if __name__ == '__main__':
    while True:
        print('Enter text to remove spaces or empty line to quit:')
        some_text = input()
        if(some_text == ""):
            break
        del_space(some_text)
        some_text = ""
    print('Bye!')
        