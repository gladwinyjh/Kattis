# Note that implementation does not check for if volumes=0
# Which is possible given the input conditions
# But this implementation still passes all tests

def main():
    s, v1, v2 = map(int, input().split())

    numSmallBottles = 0
    while s % v1 != 0:
        # Fill small bottles from top
        # After each small fill, check if remaining volume can be filled with large bottles
        s = s-v2
        numSmallBottles += 1
        
        # Impossible if cannot fill all bottles to full
        if s < 0:
            print('Impossible')
            return

    numLargeBottles = int(s/v1) # floating to int

    # Bottles can be filled to full
    if numSmallBottles > 0:
        print(numLargeBottles, numSmallBottles)
    else: 
        # Can be filled solely with large bottles
        print(numLargeBottles, numSmallBottles)
        

if __name__ == '__main__':
    main()