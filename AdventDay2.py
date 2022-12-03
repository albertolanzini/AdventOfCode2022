import sys
with open(sys.argv[1], 'r') as my_file:
    Content = my_file.read()
    #print(Content)
    guide=Content.splitlines()
    print(guide)
    score=0
    for i in guide:
        if(i=="A X"):
            score=score+3
        if(i=="A Y"):
            score=score+4
        if(i=="A Z"):
            score=score+8
        if(i=="B X"):
            score=score+1
        if(i=="B Y"):
            score=score+5
        if(i=="B Z"):
            score=score+9
        if(i=="C X"):
            score=score+2
        if(i=="C Y"):
            score=score+6
        if(i=="C Z"):
            score=score+7
        print(score)







    """
            if(i=="A X"):
                score=score+4
            if(i=="A Y"):
                score=score+8
            if(i=="A Z"):
                score=score+3
            if(i=="B X"):
                score=score+1
            if(i=="B Y"):
                score=score+5
            if(i=="B Z"):
                score=score+9
            if(i=="C X"):
                score=score+7
            if(i=="C Y"):
                score=score+2
            if(i=="C Z"):
                score=score+6
            print(score)
            
            """
