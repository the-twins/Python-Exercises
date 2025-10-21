if __name__ == '__main__':
    LITER_IN_GALLON = 3.785
    KM_IN_MILE = 1.609
    print('Enter the number of miles traveled:')
    mile = float(input())
    print('Enter the number of gallons of gasoline consumed:')
    gasoline = float(input())
    print(f'It amounts {mile / gasoline:.1f} mile-per-gallon.')
    print(f'It amounts {LITER_IN_GALLON * 100 /((mile / gasoline)* KM_IN_MILE):.1f} ' 
           'liters-per-100-km.')
            