MOLEC_IN_GR = 3.0 * (10 ** -23)
QUART_IN_GR = 950
print('Enter the water value in quarts: ')
amount = int(input())
print('There are', (amount * QUART_IN_GR) / MOLEC_IN_GR, 'molecules in this volume')
