import sys
from typing import List, Any

with open(sys.argv[1], 'r') as my_file:
    Content = my_file.read()
    Letters = Content.splitlines()
    #print(Letters)
    fsth = []
    sndh = []
    somma = 0
    elfs = []
    #print(type(elfs))

    for j in Letters:
        elfs.append(j)
        if len(elfs)==3:
            commonC = ''.join(
                (set(elfs[0]).intersection(elfs[1])).intersection(elfs[2])
            )
            x = commonC.islower()
            if x == True:
                somma = somma + ord(commonC) - ord('a') + 1
            else:
                if len(commonC) == 0:
                    break
                else:
                    somma = somma + ord(commonC) - ord('A') + 27
            elfs = []
    print(somma)
    '''
    for i in Letters:
        print(len(i))
        fsth=slice(0,(len(i)//2))
        sndh=slice(len(i)//2,len(i))
        print(i[fsth], i[sndh])
        commonC=''.join(
            set(i[fsth]).intersection(i[sndh])
        )
        print(commonC)
        #print(type(commonC))
        x = commonC.islower()
        if x == True:
            somma= somma + ord(commonC) - ord('a') + 1
            #print(sum)
        else:
            if len(commonC) == 0:
                break
            else:
                somma = somma + ord(commonC) - ord('A') + 27
            #print(sum)

    print(somma)
    '''
