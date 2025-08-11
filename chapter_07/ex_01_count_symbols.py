new = 0
space = 0
ch = 0
stop = False
while True:
    line = input()
    for i in line:
        if(i == '#'):
            stop = True
            break
        if(i == ' '):
            space += 1
        else:
            ch += 1
    if(stop == True):
        break
    new += 1
print("Spaces =", space, "newlines =", new, "all other characters =", ch)
