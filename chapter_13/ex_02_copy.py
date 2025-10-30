import sys

if __name__ == '__main__':
    try:
        if(len(sys.argv) != 3):
            print('Invalid input on command line')
        else:        
            with open(sys.argv[1], 'rb') as f:
                some_data = f.read()
            with open(sys.argv[2], 'wb') as fc:
                fc.write(some_data)
                print('Done')
    except FileNotFoundError:
        print('Error. File not found')
    