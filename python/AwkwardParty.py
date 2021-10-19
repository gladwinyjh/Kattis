def main():
    n = int(input())
    # List to store guest positions as a list
    guestsPositions = list(map(int, input().split()))
    # Dictionary to store key = language, val = position of guest speaking that language or the index
    d = {}
    # Add positions of languages to dictionary as a list in value
    for i in range(n):
        if guestsPositions[i] not in d:
            d[guestsPositions[i]] = [i]
        else:
            d[guestsPositions[i]].append(i)

    # Boolean flag to indicate if there is at least a language with >= 2 people speaking it
    flag = True
    # Minimum distance between 2 guests initially set as the max of n = 100 000 as denoted in question
    minDist = 100000
    for key, val in d.items():
        # >= 2 guests speak the this language
        if len(val) > 1:
            flag = False
            # Note that Kattis accepts the submission below as correct, even though it is not technically correct
                # Get the last 2 indices/positions as the min distance is determined by them
                # If they are closer to each other than the current min distance, 
                # their distance is the new min distance
                    # if val[-1] - val[-2] < minDist:
                    #     minDist = val[-1] - val[-2]
            
            # This is the correct algorithm:
            # Compare 2 adjacent indices. If difference < minDist, it is the new minDist
            for i in range(1, len(val)):
                if val[i] - val[i-1] < minDist:
                    minDist = val[i] - val[i-1]
    
    if flag:
        print(n)
    else:
        print(minDist)
    

if __name__ == '__main__':
    main()