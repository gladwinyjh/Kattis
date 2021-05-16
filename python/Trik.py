def trik(n):

    currPos = 1

    for letter in str(n):
        if (letter == "A"):
            if (currPos == 1):
                currPos = 2
            
            elif (currPos == 2):
                currPos = 1
        
        if (letter == "B"):
            if (currPos == 2):
                currPos = 3
            
            elif (currPos == 3):
                currPos = 2

        if (letter == "C"):
            if (currPos == 1):
                currPos = 3
            
            elif (currPos == 3):
                currPos = 1      

    return currPos


n = input()

print(trik(n))

