import sys
with open(sys.argv[1], 'r') as my_file:
    Content = my_file.read()
    Cal = Content.splitlines()
    print(Cal)
    elfs = []
    total = 0
    for i in Cal:
        if (i == ''):
            elfs.append(total)
            total=0
        else:
            total += int(i)
    elfs.append(total)
    tC = 0
    for i in range(0, 3):
        tC += max(elfs)
        print(max(elfs))
        elfs.remove(max(elfs))
    print(tC)


