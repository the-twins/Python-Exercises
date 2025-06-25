FOOT_IN_CM = 30.48
INCH_IN_CM = 2.54
print('Enter a height in centimeters: ')
cm = float(input())
while(cm > 0):
    print(cm,'cm =', cm // FOOT_IN_CM, 'feet,', 
         (cm - (cm // FOOT_IN_CM) * FOOT_IN_CM) / INCH_IN_CM, 'inches')
    print('Enter a height in centimeters (<= 0 to quite): ')
    cm = float(input())
print('Bye.')
