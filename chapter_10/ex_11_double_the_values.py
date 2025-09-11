def doub_array(numb: list[int]) -> list[int]:
    """Doubles all the values in array"""
    for i in range(0, 3):
        for j in range(0, 5):
            numb[i][j] = numb[i][j] * 2
    return numb
    
    
if __name__ == '__main__':
    numb = [[2, 4, 5, 8, 10], [11, 12, 13, 14, 15], [20, 21, 22, 23, 24]]
    print('Original array:',numb)
    print('Array after using function:', doub_array(numb))
    