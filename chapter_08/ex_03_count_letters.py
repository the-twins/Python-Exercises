symb = 0
count_up = 0
count_low = 0
stop = False
print("Enter text to count characters(& to quit):")
while True:
    line = input()
    for i in line:
        if(i == '&'):
            stop = True
            break
        elif(i.isupper()):
            count_up += 1
        elif(i.islower()):
            count_low += 1
        else:
            symb += 1
    if(stop == True):
        break
    symb += 1  # for the symbol '\n'
print("\nThe number of uppercase letters =", count_up, ", the number of lowercase letters =",
      count_low,"and the number of other characters =", symb)
