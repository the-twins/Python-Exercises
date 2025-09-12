def difference(numb: list[float]) -> float:
    """Returns the difference between the largest and smallest elements of an array_of_float"""
    largest_numb = max(numb)
    smallest_numb = min(numb)
    return largest_numb - smallest_numb

    
if __name__ == '__main__':
    numb = []
    n = 1
    print("Let's create a list of 10 numbers")
    while(n != 11):
        print('Enter float:')
        numb.append(float(input()))
        n += 1
    print('The difference between the largest and smallest elements is', difference(numb))
