def sum_array(numb_first: list[int], numb_second: list[int], numb_third: list[int] ) -> list[int]:
    """Sets each element in an array to the sum of corresponding elements in two other arrays"""
    for i in range(0, 4):
        numb_third.append(numb_first[i] + numb_second[i])
    return numb_third
    
    
if __name__ == '__main__':
    numb_first = [2, 4, 5, 8]
    numb_second = [1, 0, 4, 6]
    numb_third = []
    print('First array:', numb_first)
    print('Second array:', numb_second)
    print('Third array:', sum_array(numb_first, numb_second, numb_third))
    