def main(answerList):
    
    for i in range(len(answerList)):
        
        #Store temp value for current number
        temp = answerList[i]
        
        numList = [ _ for _ in str(answerList[i])]

        # Check for leading zeroes
        if answerList[i] > 9:
            changeList = ['1', '9']
        else:
            changeList = ['0', '1', '9']
        
        # Go through each digit in a number
        for j in range(len(numList)):
            
            #Store temp value for digit
            temp2 = numList[j]
            
            # Go through changing that digit with changeList
            for change in changeList:
                # Change the digit
                numList[j] = change

                concatenated = int(''.join([num for num in numList]))

                answerList[i] = concatenated
                    
                # Check if list is still sorted, return if not sorted
                if answerList != sorted(answerList):
                    print(*answerList)
                    return
                
                #Restore digit
                numList[j] = temp2
            
            #Restore number
            answerList[i] = temp           
    
    # If it reaches this stage, it means that it is impossible
    print('impossible')
    return
                
            

if __name__ == "__main__":
    
    n = int(input())
    
    # Read answers into a list
    answerList = [int(i) for i in input().split()]
    
    main(answerList)        