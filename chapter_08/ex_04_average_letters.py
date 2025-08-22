word = 0
count = 0
stop = False
temp = ' '
print("Enter text to count characters(& to quit):")
while True:
    line = input()
    for i in line:
        if(i == '&'):
            stop = True
            if(temp.isalpha()):
                word += 1
            break
        elif(i.isupper()):
            count += 1
        elif(i.islower()):
            count += 1
        elif(i == ' '):
            word += 1
        temp = i
    if(stop == True):
        if(word == 0):
            print("You have not entered any words. Bye.")
        else:
            print("\nThis text contains", word, "words of", count, "letters. Average number of" 
            " letters =", int(count / word))
        break
