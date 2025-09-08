def max_integer(numb: list[int]) -> int:
    """Returns the largest value stored in an array-of-int""" 
    largest_numb = max(numb)
    return largest_numb

    
if __name__ == '__main__':
    numb = []
    n = 1
    print("Let's create a list of 10 integer")
    while(n != 11):
        print('Enter integer:')
        numb.append(int(input()))
        n += 1
    print('The largest value is', max_integer(numb))
