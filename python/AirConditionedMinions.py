def main():
    n = int(input())
    # List to store temperature ranges
    ranges = []
    for i in range(n):
        tempRange = list(map(int, input().split()))
        ranges.append(tempRange)
    
    # Sort temperature ranges based on upper bound
    sortedRanges = sorted(ranges, key=lambda x: x[1])
    rooms = 1
    # Lower temperature bound for same room
    bound = sortedRanges[0][1]
    for i in range(1, len(sortedRanges)):
        # Lower temperature bound for this minion is above current lower temperature bound
        # Need to make a new room
        if sortedRanges[i][0] > bound:
            # Set new lower temperature bound
            bound = sortedRanges[i][1]
            rooms += 1

    print(rooms)

    
if __name__ == '__main__':
    main()