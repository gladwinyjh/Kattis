def main():
    c, n, m = map(int, input().split())
    
    # Current dict stores the current state of farm
    currentDict = {}
    # Next dict stores the state of the farm on the next day (12am)
    nextDict = {}

    for i in range(n):
        numCow = int(input())
        if numCow not in currentDict:
            currentDict[numCow] = 1
            # Important that it is a list as we will be appending numbers
            nextDict[numCow] = []
        else:
            currentDict[numCow] += 1

    # List to store days
    days = []
    for i in range(m):
        days.append(int(input()))

    # Dont need to calculate farm size until max days (50), 
    # just until the last day regulator comes. So we get the max(days)
    lastDay = max(days)

    # To store number of farms for retrieval later
    # We have to store all the farms up till the last day of checking 
    # because we dont know if days given will be in ascending order 
        # Example: d_j could be 4, 10, 0, 2, 11,...
    numberOfFarms = []

    for i in range(lastDay+1):
        # Store number of farms for this day
        numberOfFarms.append(sum(currentDict.values()))
        for key, val in currentDict.items():
            # Doubling current farm size will not reach maximum
            if key <= c/2:
                # Store doubled farm size in nextDict
                # Note that we are appending, just summing up values can screw things up
                # in the else statement where the summed value is multiplied
                    # Ex: (5 + 2*2) != (5 + 2)*2
                if key*2 not in nextDict:
                    nextDict[key*2] = [val]
                else:
                    nextDict[key*2].append(val)
            else:
                nextDict[key].append(2 * val)

        # For each key, we get a list of values corresponding to the number of new farms added to 
        # the current farm size during this day
        # Sum the number of farms for each farm size on this day
        for key, val in nextDict.items():
            nextDict[key] = sum(val)

        # Store it as current Dict
        currentDict = nextDict.copy()

        # Reset the dictionary for next day
        for key, val in nextDict.items():
            nextDict[key] = []
    
    # For each day regulator comes (in order of inputs), print number of farms for that day
    for day in days:
        print(numberOfFarms[day])

if __name__ == '__main__':
    main()