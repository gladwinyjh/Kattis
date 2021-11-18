from collections import deque


def pushButton(settings, row, col):
    # Convert tuple of tuples to list of lists for incrementing
    settings = list(map(list,settings))

    # Increment same row by 1
    # Modulus 4 so that values remain between 0 and 3
    for i in range(3):
        settings[row][i] += 1
        settings[row][i] = settings[row][i] % 4

        if i != row: # Don't double increment settings[row][col]
            settings[i][col] += 1
            settings[i][col] = settings[i][col] % 4
    
    # Convert list of lists back to tuple of tuples
    settings = tuple(map(tuple,settings))

    return settings


def main():
    display = []
    for i in range(3):
        row = tuple(map(int, input().split()))
        display.append(row)
    
    # Enqueue (initial display, number of moves) to queue
    q = deque([(tuple(display), 0)])

    # Dictionary to check if a particular display configuration have been visited before,
    # so that BFS will not go into infinite loop
    # Value of each key does not really matter...the number of moves is just used as value here
    # Note that the purpose of using tuples is so that display configurations can be used as dictionary keys
    visitedDisplays = {tuple(display): 0}

    # Perform Breadth First Search
    # From initial configuration, explore every possible configuration by pressing each button once (one more move)
    # Stop when configuration reaches 9 zeroes, or when queue is empty (tested all possible configurations)
    while q:
        # Settings is the display in the form of a tuple of tuples
        # numMoves is the number of moves needed to reached this display from initial display
        settings, numMoves = q.popleft()

        # Check if current display numbers are all zero
        # Return the number of moves needed to reach this display
        if sum(map(sum, settings)) == 0:
            return numMoves

        # Push each button
        for i in range(3):
            for j in range(3):
                # Get the new display in the form of tuple of tuples
                newDisplay = pushButton(settings, i, j)
                
                # If new display has not yet been seen before
                if newDisplay not in visitedDisplays:
                    visitedDisplays[newDisplay] = numMoves + 1
                    # Add (current display, number of moves to get there) to queue
                    q.append((newDisplay, numMoves + 1))
    
    # Return -1 if not possible
    return -1
                

if __name__ == '__main__':
    print(main())