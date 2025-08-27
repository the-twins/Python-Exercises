def print_ch(ch : str, i : int, j : int):
    """Prints the requested character i times in j lines"""
    for lines in range (1, j + 1):
        for character in range (1, i + 1):
            print(ch, end = '')
        print()


if __name__ == '__main__':
    print("Enter one character:")
    ch = input()
    print("Enter first number:")
    i = int(input())
    print("Enter second number:")
    j = int(input())
    print_ch(ch, i, j)
