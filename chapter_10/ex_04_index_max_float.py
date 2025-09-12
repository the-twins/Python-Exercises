def index(numb: list[float]) -> int:
    """Returns the index of the largest value strored in an array_of_float"""
    largest_numb = max(numb)
    numb_index = numb.index(largest_numb)
    return numb_index

    
if __name__ == '__main__':
    numb = []
    n = 1
    print("Let's create a list of 10 numbers")
    while(n != 11):
        print('Enter float:')
        numb.append(float(input()))
        n += 1
    print('The index of the largest value is', index(numb))
