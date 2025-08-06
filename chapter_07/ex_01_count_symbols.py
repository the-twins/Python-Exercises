text = ""
new = 0
space = 0
ch = 0
stop = False
while True:
    line = input()
    if(line):
        text += line
        new += 1    
        for i in text:
            if(i == '#'):
                stop = True
                ch -= 1
            if(i == ' '):
                space += 1
            else:
                ch += 1
    if(stop == True):
        break
print("Spaces =", space, "newlines =", new, "all other characters =", ch)
