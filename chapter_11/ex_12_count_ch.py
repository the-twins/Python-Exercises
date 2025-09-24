print('Enter text (empty line to quit):')
some_text = []
count_words = 0
count_up = 0
count_low = 0
count_digit = 0
count_punct = 0
mark_word = False
while True:
    text = input()
    if(text == ''):
        break
    some_text.append(text)
for i in some_text:
    for j in i:
        if j.isspace() == False:
            mark_word = True
            if j.isupper() == True:
                count_up += 1
            elif j.islower() == True:
                count_low += 1
            elif j.isnumeric() == True:
                count_digit += 1
            else:
                count_punct += 1              
        else:
            if(mark_word == True):
                count_words += 1
                mark_word == False
    count_words += 1                
print('Words =', count_words - 1, 'uppercase letters =', count_up, 'lowercase letters =', 
      count_low, 'punctuation characters =', count_punct, 'digits =', count_digit)
