molec_in_gr = 3.0 * (10 ** -23)
quart_in_gr = 950
print('Enter the water value in quarts: ')
amount = int(input())
print('There are', (amount * quart_in_gr) / molec_in_gr, 'molecules in this volume')
