def main():
    n = int(input())

    dirt = list(map(int, input().split()))

    # List that stores the days in which dirty push is given
    dirtDays = []

    # List that stores the days elapsed from each dirty push
        # Dirt at each index corresponds to day in which dirty push is given in dirtDays
    dirtiness = []

    # Counter to store number of cleanups
    cleanup = 0
    for i in range(1,366):
        # If current day is the day dirty push is done
        if i in dirt:
            # Append current day to dirtDays
            dirtDays.append(i)
            # Append days elapsed of this dirty push to dirtiness
                # 0 because 0 days elapsed so far
            dirtiness.append(0)

        # Sum of all the dirt accumulated from the days
        dirtSum = sum(dirtiness)
        # 2 conditions for cleanup
            # 1. Allowing dirt to accumulate to next day will reach or surpass 20
                # Perikles do not want that; she wants to clean before that happens
            # 2. End of the year (i == 365) AND if there is some dirt
                # Important that there is still dirt inside to be cleaned
        if dirtSum + 1 * len(dirtDays) >= 20 or (i == 365 and len(dirtDays) > 0):
            cleanup += 1
            # Reset
            dirtiness = []
            dirtDays = []
        else:
            # Increment dirt from all days by 1 for next day
            for j in range(len(dirtDays)):
                dirtiness[j] += 1
    
    print(cleanup)


if __name__ == '__main__':
    main()