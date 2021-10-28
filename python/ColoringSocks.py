def main():
    S, C, K = map(int, input().split())

    socks = list(map(int, input().split()))

    sortedSocks = sorted(socks)

    # Total number of washing machines
    numMachines = 1
    # Number of socks in current machine. Load with first sock
    numSocks = 1
    # Smallest color of sock in current machine
    smallest = sortedSocks[0]
    for i in range(1,S):
        # Number of socks in current machine exceeds capacity OR
        # Color difference between current sock and smallest color sock in machine exceeds allowance
        if numSocks == C or sortedSocks[i] - smallest > K:
            # Add new machine
            numMachines += 1
            # Number of socks in new machine
            numSocks = 0
            # Current smallest sock in new machine
            smallest = sortedSocks[i]
            
        # Add current sock to machine
        numSocks += 1
    
    print(numMachines)


if __name__ == '__main__':
    main()