# If train has capacity, station passengers should board until full
# Train should start and finish journey empty
    # No passengers should wait at the last station

def main():
    C, n = map(int, input().split())
    # Current capacity of train. Initially train should be empty 
    currCap = 0
    # Flag for if case is impossible
    impossible = False
    for i in range(n):
        # Store information about passengers leaving, boarding, staying on station
        info = list(map(int, input().split()))
        # Update current capacity
        # Current capacity = Previous capacity - passengers leaving train + passengers boarding train
        currCap = currCap - info[0] + info[1]

        # Conditions in which information is impossible
            # 1. Train is not empty at first station
            # 2. Current train capacity has exceeded capacity or is below 0
            # 3. Current train capacity is within capacity, but there are still passengers waiting at the station
                # These passengers should be able to board the train
        if (i == 0 and info[0] > 0) or (currCap > C) or (currCap < 0) or (0 <= currCap < C and info[2] > 0):
            impossible = True

        # Another condition in which information is impossible
            # 4. After last station, if current capacity is not 0 or if there are people waiting for train
        if i == n-1:
            if currCap > 0 or info[2] > 0:
                impossible = True

    if impossible:
        print('impossible')
    else:
        print('possible')


if __name__ == '__main__':
    main()