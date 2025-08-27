def chline(ch : str, i : int, j : int):
    """Prints the requested character in columns i through j"""
    for space in range (1, i):
        print(" ", end = '')
    for character in range (i, j + 1):
        print(ch, end = '')


if __name__ == '__main__':
    print("Enter one character:")
    ch = input()
    print("Enter first number:")
    i = int(input())
    print("Enter second number:")
    j = int(input())
    chline(ch, i, j)
    