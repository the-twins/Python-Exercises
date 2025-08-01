first = []
second = []
print("Enter eight numbers: ")
for i in range(0, 8):
    first.append(float(input()))
    if(i == 0):
        second.append(first[0])
    else:
        second.append(second[i-1] + first[i])
numb = 0
while(numb <= 7):
    print(first[numb], end = ' ')
    numb += 1
print()
numb = 0
while(numb <= 7):
    print(round(second[numb],2), end = ' ')
    numb += 1
