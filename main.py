if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as my_file:
        Content = my_file.read()
        pairs = Content.splitlines()
        counter = 0
        overlapcounter = 0
        #print(pairs)
        elfs = []
        for i in pairs:
            s1, s2 = i.split(",")
            #this way the first pair is stored in the variable s1 while the other is stored in s2
            s1_start, s1_end = map(int, s1.split("-"))
            s2_start, s2_end = map(int, s2.split("-"))
            if (s1_start <= s2_start and s1_end >= s2_end) or (s2_start <= s1_start and s2_end >= s1_end):
                counter += 1
            if (set(range(s1_start, s1_end + 1)) & (set(range(s2_start, s2_end + 1)))):
                #first thing you create a set in the range s1_start - s1_end and do the same for s2
                #you then use the & operator: when the sets have an intersection, then it means they overlap
                #each and every time we see an overlap we increment our counter by 1
                overlapcounter += 1
        print(counter)
        print(overlapcounter)

