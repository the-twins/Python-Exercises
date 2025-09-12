def reverse(numb: list[float]):
    """Reverses the contents of an array of float""" 
    numb.reverse()

    
if __name__ == '__main__':
    numb = []
    n = 1
    print("Let's create a list of 10 numbers")
    while(n != 11):
        print('Enter float:')
        numb.append(float(input()))
        n += 1
    print(numb)
    reverse(numb)
    print(numb)
    