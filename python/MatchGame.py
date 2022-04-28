def main():
    # These dictionaries contain the possible old and new digit pairing
    # Ex: subtractOne[6] = 5, meaning 5 can be formed by removing a matchstick from 6
    # Sets are used so that checking if digit can be formed can be done in O(1)
    subtractOne = {6:set([5]), 7:set([1]), 8:set([0,6,9]), 9:set([3,5])}
    addOne = {0:set([8]), 1:set([7]), 3:set([9]), 5:set([6,9]), 6:set([8]), 9:set([8])}
    moveOne = {0:set([6,9]), 2:set([3]), 3:set([2,5]), 5:set([3]), 6:set([0,9]), 9:set([0,6])}

    X, Y = input().split()

    different = []
    for i in range(len(X)):
        if X[i] != Y[i]:
            # Difference in digits, append the idx to different list
            different.append(i)
        
        # Since only 1 matchstick can be moved, a maximum of 2 digits can be different
        if len(different) > 2:
            print('no')
            return
    
    # One digit is different, this means that a matchstick has been moved
    if len(different) == 1:
        idx = different[0]
        
        # Check if the old digit can form a new digit by moving 1 matchstick
        if (int(X[idx]) in moveOne) and (int(Y[idx]) in moveOne[int(X[idx])]):
            print('yes')
            return
    
    # Two digits are different, this means that one matchstick was moved from one digit to another
    else:
        idxOne = different[0]
        idxTwo = different[1]

        # Take one from idxOne to give to idxTwo
        # Check that the one to be substracted can form a new digit, then check that the one to be added can form a new digit
        if (int(X[idxOne]) in subtractOne) and (int(Y[idxOne]) in subtractOne[int(X[idxOne])]) and (int(X[idxTwo]) in addOne) and (int(Y[idxTwo]) in addOne[int(X[idxTwo])]):
            print('yes')
            return
        
        # Take one from idxTwo to give to idxOne
        # Same as above, check if digits can be added and subtracted
        if (int(X[idxTwo]) in subtractOne) and (int(Y[idxTwo]) in subtractOne[int(X[idxTwo])]) and (int(X[idxOne]) in addOne) and (int(Y[idxOne]) in addOne[int(X[idxOne])]):
            print('yes')
            return
        
    print('no')


if __name__ == '__main__':
    main()
