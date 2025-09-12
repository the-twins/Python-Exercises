ROWS = 3
COLS = 5


def average_row(n: list[float]):
    """Computes the average of each set of five values and prints it"""
    subtot = 0
    for i in n:
        subtot += i
    print('Average of set of five values is', round(subtot / COLS, 2))
    

def average_all(numb: list[list[float]]) -> float:
    """Computes the average of all the values and returns it"""
    subtot = 0
    total = 0
    for i in range(0, ROWS):
        for j in range(0, COLS):
            subtot += numb[i][j]
        total += subtot
        subtot = 0
    return round(total / (ROWS * COLS), 2)
    
    
def largest_value(numb: list[list[float]]) -> float:
    """Determine the largest value of the 15 values and returns it"""
    max_in_row = [max(row) for row in numb]
    max_numb = max(max_in_row)
    return max_numb
    
    
if __name__ == '__main__':
    numb = []
    array =[]
    print('Create three sets of five float number each.')
    for i in range(0, ROWS):
        numb.append([])
        for j in range(0, COLS):
            print('Please enter float number:')
            numb[i].append(float(input()))
    print(numb)
    for n in numb:
        average_row(n)
    print('Average of all the values is', average_all(numb))
    print('The largest value of the 15 values is', largest_value(numb))
    