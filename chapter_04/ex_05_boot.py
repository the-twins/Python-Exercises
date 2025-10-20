if __name__ == '__main__':
    BIT_IN_BYTE = 8
    print('Enter the download speed in megabits per second:')
    mbs = float(input())
    print('Enter the size of a file in megabytes(MB):')
    mb = float(input())
    print(f'At {mbs:.2f} megabits per second, a file of {mb:.2f} megabytes')    
    print(f'downloads in {mb * BIT_IN_BYTE / mbs:.2f} seconds.')
    