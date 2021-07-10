def main():
  
    while True:     
        possibleNumbers = [True for i in range(10)]
        
        # Dishonest flag
        dishonest = False
        
        while True:
            # Read Ollie's guess
            guess = int(input()) 
            
            # If guess is 0, end of script
            if guess == 0:
                return
        
            # Read Stan's response
            response = input()
            
            if response == 'too high':
                
                # If guess is new
                if possibleNumbers[guess-1]:
                    # Set False to guess till 10
                    for i in range(guess-1, 10):
                        possibleNumbers[i] = False
                
                #Check if there is at least 1 possible number
                #If guess is new and Stan is saying its too high, then there must be a 'True' smaller than the guess
                #if guess is repeated, same thing
                if True not in possibleNumbers[:guess]:
                    dishonest = True
                    
            elif response == 'too low':
                
                # If guess is new
                if possibleNumbers[guess-1]:
                    # Set False to 0 to guess
                    for i in range(0, guess):
                        possibleNumbers[i] = False
                
                #Check if there is at least 1 number bigger
                #If guess is new and Stan is saying its too low, then there must be a 'True' larger than the guess
                #if guess is repeated, same thing
                if True not in possibleNumbers[guess:]:
                    dishonest = True
            
            else:
                
                #If guess is new 
                if possibleNumbers[guess-1]:
                    # Break out when response is 'right on'
                    break
                else:
                    #Stan is lying as guess was previously not guessed as right on, or number was previously identified as False
                    dishonest = True
                    break
            
        if dishonest:
            print('Stan is dishonest')
        else:
            print('Stan may be honest')
 

if __name__ == '__main__':
    main()