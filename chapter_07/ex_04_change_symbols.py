point = 0
ex_mark = 0
stop = False
while True:
    line = input()
    for i in line:
        if(i == '#'):
            stop = True
            break
        if(i == '.'):
            i = '!'
            point += 1
            print(i, end = '')
            continue
        if(i == '!'):
            i = '!!'
            ex_mark += 1
        print(i, end = '')
    if(stop == True):
        break
    print()
print("\nThe point has been replaced", point, "times, exclamation mark has been "
      "replaced", ex_mark, "times.")
