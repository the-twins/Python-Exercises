INCH_IN_FOOT = 12
CM_IN_INCH = 2.54
print('Enter a height in centimeters: ')
cm = float(input())
while(cm > 0):
    inch = cm / CM_IN_INCH
    print(cm,'cm =', inch // INCH_IN_FOOT, 'feet,', round(inch % INCH_IN_FOOT, 2), 'inches')
    print('Enter a height in centimeters (<= 0 to quit): ')
    cm = float(input())
print('Bye.')
