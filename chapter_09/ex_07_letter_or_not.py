def index_numb(ch: str) -> int:
    """Takes a character as an argument and returns the numerical location if the character is a
    letter and returns -1 otherwise"""
    numb = ord(ch)
    if(numb >= 65 and numb <= 90):
        return numb - 64
    elif(numb >= 97 and numb <= 122):
        return numb - 96
    else:
        return -1
        
        
if __name__ == '__main__':
    stop = False
    print("Enter text to count characters(& to quit):")
    while True:
        line = input()
        for i in line:
            if(i == '&'):
                stop = True
                break
            else:
                index_n = index_numb(i)
                if(index_n > 0):
                    print('"', i, '" is letter. Numerical location =', index_n)
                else:
                    print('"', i, '" is not letter.')             
        if(stop == True):
            break
