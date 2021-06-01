def calJumpingDist(n, height, best):

    currShortest = 10e9
    stack = []
    
    #Add first mountain
    i = 0
    stack.append(i)

    #keep adding to stack until all mountains are in
    while len(stack) != n:
        
        for j in range(i+1, n):

            stack.append(j)
           
            #Taller mountain in range observed
            if height[j] >= height[i]:

                #If the mountain immediately after the first mountain in stack is taller than it, then bungee cannot be between these two, move to next mountain in range (Starting mountain remains the same)
                if j != i+1:

                    #Height difference between starting mountain and current shortest mountain between
                    currJumping = height[i] - currShortest

                    if currJumping > best:
                        best = currJumping
            
                #Current mountain is new starting position
                i = j

                #Reset current shortest mountain as mountain range is changing
                currShortest = 10e9

                #Break to go to next starting mountain. 
                break

            else:
                #Found a shorter mountain
                if currShortest > height[j]:
                    currShortest = height[j]

    return best


n = int(input())

height = [int(i) for i in input().split()]
best = 0

#Forward pass
best = calJumpingDist(n, height, best)

#Backward pass
best = calJumpingDist(n, height[::-1], best)

print(best)