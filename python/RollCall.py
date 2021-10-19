def main():
    # Dictionary to store key = last name, val = first name
    nameDict = {}
    # Dictionary to keep track of duplicated first names
    firstNames = {}
    while True:
        try:
            firstName, lastName = input().split()
            if lastName not in nameDict:
                nameDict[lastName] = [firstName]
            else:
                nameDict[lastName].append(firstName)
            
            if firstName not in firstNames:
                firstNames[firstName] = 1
            else:
                firstNames[firstName] += 1
            
        except EOFError:
            break
    
    # Extract duplicated first names
    duplicateFirstNames = []
    for key, val in firstNames.items():
        if val > 1:
            duplicateFirstNames.append(key)

    # Sort name dictionary based on last names
    sortedLastNames = sorted(nameDict.items(), key=lambda x: x[0])

    for key, val in sortedLastNames:
        # Only 1 person have this last name
        if len(val) == 1:
            if val[0] in duplicateFirstNames:
                # Multiple last names, so need to print both first and last name
                print(val[0], key)
            else:
                print(val[0])
        # Multiple people have this last name
        else:
            # Since first name list of each last name is not sorted, sort it first
            sortedFirstNames = sorted(val)
            for firstName in sortedFirstNames:
                if firstName in duplicateFirstNames:
                    # Multiple last names, so need to print both first and last name
                    print(firstName, key)
                else:
                  print(firstName)
                

if __name__ == '__main__':
    main()