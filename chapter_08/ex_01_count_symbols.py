symb = 0
stop = False
print("Enter text to count characters(& to quit):")
while True:
    line = input()
    for i in line:
        if(i == '&'):
            stop = True
            break
        else:
            symb += 1
    if(stop == True):
        break
    symb += 1  # for the symbol '\n'
print("There are", symb, "characters in the text.")
        