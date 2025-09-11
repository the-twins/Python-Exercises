def sum_rain_in_months(RAIN: list[float]) -> float:
    """ For each year, sum rainfall for each month and print. Returns total."""
    subtot = 0
    total = 0
    year = 0
    print('YEAR    RAINFALL (inches)')
    for i in range(0, 5):
        for j in range(0, 12):
            subtot += RAIN[i][j]
        print(2010 + year,'    ', round(subtot, 2))
        total += subtot
        subtot = 0
        year += 1
    return total
    
    
def average_rain(RAIN: list[float], total: float):
    """Prints average"""
    YEARS = 5
    subtot = 0
    print('\nThe yearly average is', round(total / YEARS, 2),' inches.\n')
    print('MONTHLY AVERAGES:\n')
    print('Jan  Feb  Mar Apr May Jun Jul  Aug  Sep  Oct Nov  Dec')
    for i in range(0, 12):
        for j in range(0, 5):
            subtot += RAIN[j][i]
        print(round(subtot / YEARS, 2), end=' ')
        subtot = 0
            

if __name__ == '__main__':
    RAIN = [
        [4.3, 4.3, 4.3, 3.0, 2.0, 1.2, 0.2, 0.2, 0.4, 2.4, 3.5, 6.6],
        [8.5, 8.2, 1.2, 1.6, 2.4, 0.0, 5.2, 0.9, 0.3, 0.9, 1.4, 7.3],
        [9.1, 8.5, 6.7, 4.3, 2.1, 0.8, 0.2, 0.2, 1.1, 2.3, 6.1, 8.4],
        [7.2, 9.9, 8.4, 3.3, 1.2, 0.8, 0.4, 0.0, 0.6, 1.7, 4.3, 6.2],
        [7.6, 5.6, 3.8, 2.8, 3.8, 0.2, 0.0, 0.0, 0.0, 1.3, 2.6, 5.2]]
    total = sum_rain_in_months(RAIN)
    average_rain(RAIN, total)
    