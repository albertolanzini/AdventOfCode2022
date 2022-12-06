import sys
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as my_file:
        letters = my_file.read()
        #print(len(letters))
        Number = 0
        code1 = []
        size = 4
        #First off I need to create a for cycle that goes through every single element of the string
        #As it goes through the elements of the string I need to check if the element of current index is the same
        #as the next four, if it is my cycle will go on, otherwise I will print the number of letters I needed in
        #order to be able to get that condition. I could do it creating a new list, appending a value for each
        #iteration until my condition verifies. After it does I will just print the lenght of that variable and break
        #the cycle.

        for j in range(0, len(letters), 1):
            code1.append(letters[j])
        for i in range(0, len(code1), 1):
            if i < (len(code1)-4):
                if code1[i] != code1[i+1] and code1[i] != code1[i+2] and code1[i] != code1[i+3] and code1[i] != code1[i+4] and code1[i+1] != code1[i+2] and code1[i+1] != code1[i+3] and code1[i+1] != code1[i+4] and code1[i+2] != code1[i+3] and code1[i+2] != code1[i+4] and code1[i+3] != code1 [i+4]:
                    Number = i + 4
                    break
        #print(code1)
        print(Number)

        #For the second part of the exercise the message signal is no longer 4 charachters but becomes 14.
        #Since 14 is way too many to write every possible combination, I'll solve it using sets, especially
        #thanks to the property for which an element can only be added to a set once.
        size = 14
        while len(set(letters[size - 14:size])) < 14:
            size += 1
        print(size)

