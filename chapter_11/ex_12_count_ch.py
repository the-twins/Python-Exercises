import string

print('Enter text (empty line to quit):')
some_text = []
count_words = 0
count_up = 0
count_low = 0
count_digit = 0
count_punct = 0
while True:
    text = input()
    if(text == ''):
        break
    words = text.split()
    count_words += len(words)
    some_text.append(text)
for i in some_text:
    for j in i:
        if not j.isspace():
            if j.isupper():
                count_up += 1
            elif j.islower():
                count_low += 1
            elif j.isnumeric():
                count_digit += 1
            elif j in string.punctuation:
                count_punct += 1
print('Words =', count_words, '\nuppercase letters =', count_up, '\nlowercase letters =', 
      count_low, '\npunctuation characters =', count_punct, '\ndigits =', count_digit)
