word = 0
count = 0
stop = False
letter = False
space = False
print("Enter text to count characters(& to quit):")
while True:
    line = input()
    for i in line:
        if(i == '&'):
            if(letter == True):
                if(space == False):
                    word += 1
            stop = True
            break
        elif(i.isalpha()):
            count += 1
            letter = True
            space = False
        elif(i.isspace()):
            if(letter == True):
                word += 1
            space = True
            letter = False
    if(stop == True):
        if(word == 0):
            print("You have not entered any words. Bye.")
        else:
            print("\nThis text contains", word, "words of", count, "letters. Average number of" 
            " letters =", int(count / word))
        break
    if(letter == True):
        word += 1
        letter = False
