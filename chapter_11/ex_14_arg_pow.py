import sys

try:
    numb = float(sys.argv[1])
    pow = int(sys.argv[2])
    print(round(numb ** pow, 2))
except Exception:
    print('Invalid input on command line.')
