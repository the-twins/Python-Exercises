def funct_array(numb: list[float]):
    """Compute the average of each set of five values, compute the average of all the values,
    determine the largest value of the 15 values, report the results"""
    numb_set = 1
    subtot = 0
    total = 0
    for i in range(0, 3):
        for j in range(0, 5):
            subtot += numb[i][j]
        print('Average of', numb_set, 'set of five values is', subtot / 5)
        total += subtot
        subtot = 0
        numb_set += 1
    print('Average of all the values is', round(total / 15, 2))
    max_in_row = [max(row) for row in numb]
    max_numb = max(max_in_row)
    print('The largest value of the 15 values is', max_numb)
    
    
if __name__ == '__main__':
    numb = []
    print('Create three sets of five float number each.')
    for i in range(0, 3):
        numb.append([])
        for j in range(0, 5):
            print('Please enter float number:')
            numb[i].append(float(input()))
    print(numb)
    funct_array(numb)
