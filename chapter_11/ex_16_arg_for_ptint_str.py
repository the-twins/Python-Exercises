import sys

some_text = []
print('Enter text (empty line to quit):')
while True:
    text = input()
    if(text == ''):
        break
    some_text.append(text)
if(len(sys.argv) == 1 or sys.argv[1] == '-p'):
    for one_str in some_text:
        print(one_str)
elif(sys.argv[1] == '-u'):
    for one_str in some_text:
        print(one_str.upper())
elif(sys.argv[1] == '-l'):
    for one_str in some_text:
        print(one_str.lower())
