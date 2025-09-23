def menu():
    """Prints the menu."""
    print('1) Print the original list of strings.')
    print('2) Print the strings in ASCII collating sequence.')
    print('3) Print the strings in order of increasing length.')
    print('4) Print the strings in order of the length of the first word in the string.')
    print('5) Quit.')
    print('Enter a number:')
    
    
def print_line(some_text: list[str]):
    """Prints the original list of strings."""
    for i in some_text:
        print(i)
    
    
def print_ascii(some_text: list[str]):
    """Prints the strings in ASCII collating sequence"""
    for i in sorted(some_text):
        print(i)
        
        
def print_len_list(some_text: list[str]):
    """Prints the strings in order of increasing length."""
    sorted_len = sorted(some_text, key=len)
    print(sorted_len)


def first_word(text: str)->int:
    """Returns the length of the first word"""
    n = 0
    mark_word = False
    for i in text:
        if i.isspace() == False:
            n += 1
            mark_word = True
        else:
            if(mark_word == True):
                break 
    return n                
  
  
def print_len_first_word(some_text: list[str]):
    """Print the strings in order of the length of the first word in the string."""
    sorted_len = sorted(some_text, key=first_word)
    print(sorted_len)
    
    
if __name__ == '__main__':
    some_text = []
    print('Input up to lines 10 (empty line to quit)')
    for i in range(10):
        text = input()
        if(text == ''):
            break
        some_text.append(text)           
    while True:
        menu()
        n = int(input())
        if(n == 1):
            print_line(some_text)           
        elif(n == 2):
            print_ascii(some_text)
        elif(n == 3):
            print_len_list(some_text)
        elif(n == 4):
            print_len_first_word(some_text)
        elif(n == 5):
            break
        else:
            print('Input error. Try again.')
       