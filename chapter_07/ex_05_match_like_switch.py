point = 0
ex_mark = 0
stop = False
while True:
    line = input()
    for i in line:
        match i:
            case '#':
                stop = True
                break
            case '.':
                i = '!'
                point += 1
                print(i, end = '')
                continue
            case '!':
                i = '!!'
                ex_mark += 1
        print(i, end = '')
    if(stop == True):
        break
    print()
print("\nThe point has been replaced", point, "times, exclamation mark has been "
      "replaced", ex_mark, "times.")
