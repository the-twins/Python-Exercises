import sys

print("Command-line arguments:")
for i in reversed(sys.argv[1:]):
    print(i, end=' ')
