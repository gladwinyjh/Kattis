def calculate(dict, words):
    result = 0 #Used to store final calculated value
    operandFlag = False #Default operand is subtraction, set to True if addition
    
    for i in range(len(words)):
        
        #Only take the variable names
        if i%2 != 0:
            #Variable name not defined in dict
            if words[i] not in dict:
                return 'unknown'
            else:
                #Result = first variable value initially, or addition to be made
                if i == 1 or operandFlag:
                    result += dict[words[i]]
                else: #Subtraction to be made: operand = False
                    result -= dict[words[i]]
                    
                #Get next operand (+ or -)
                operand = words[i+1]
                
                if operand == '+':
                    operandFlag = True
                else:
                    operandFlag = False
    
    #Return the variable name that has the same value as calculated result
    for key, value in dict.items():
        if value == result:
            return key
    
    #If it reaches here, calculated result is not in dictionary values
    return 'unknown'
                
                

def main():
    dict = {}
    while True:
        try:
            words = list(input().split())
            
            if words[0] == 'clear':
                dict.clear()
            elif words[0] == 'def':
                dict[words[1]] = int(words[2])
            else:   
                print(*words[1:], calculate(dict, words))
        
        #End of input
        except EOFError:
            break
            
        
            
if __name__ == '__main__':
    main()