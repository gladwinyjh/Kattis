def main():
    N = input()
    M = input()
    
    # Find the first occurrence of 0 in string M
    # If the length of M == 1, that can only mean M = 1
    # non_one stores the index of the first 0
    if len(M) == 1:
        non_one = 0
    else:
        non_one = len(M) - 1 
    
    # Quotient will be < 1
    if non_one >= len(N):
        # Get the number of 0s to be placed before N
        diff = non_one - len(N)
        print('0.', end='')
        print('0' * diff, end='')
        print(N)
        return
    
    # decimal is the index in N which N[decimal:] is the remaining string
    decimal = len(N) - non_one
    # Print the string to that point
    print(N[:decimal], end='')
    
    # Find the last non zero in the string
    non_zero = decimal
    for i in range(len(N)-1, decimal, -1):
        if N[i] != '0':
            non_zero = i
            break
    
    # If there are no non zeros left, then there is no need to print the decimal division will leave no remainder
    # Else (this if statement), print the decimal point and the rest of the string till the non_zero index (inclusive)
    if non_zero != decimal:
        print('.', end='')
        print(N[decimal:non_zero+1])
            
    
if __name__ == '__main__':
    main()
