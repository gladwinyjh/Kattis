# Start at a given floor
# Explore a floor using up and down buttons
# Do BFS
    # Append to queue (nextFloor, number of presses) 
    # if adding or removing floors are within bounds and have not yet been visited yet

    # If floor == g, return number of presses needed. That will be the minimum
    # If queue is empty, floor cannot reach g -> 'use the stairs'

from collections import deque


def visitFloor(currFloor, floors, up):
    if up:
        if 1 <= currFloor + floors <= 1e6:
            return currFloor + floors
    else:
        if 1 <= currFloor - floors <= 1e6:
            return currFloor - floors
    
    # Out of bounds, elevator remains where it is at
    return currFloor


def main():
    f, s, g, u, d = map(int, input().split())
    numPushes = 0

    q = deque([(s, numPushes)])
    visitedFloors = {s: numPushes}
    
    while q:
        currFloor, numberOfPushes = q.popleft()

        if currFloor == g:
            return numberOfPushes
        
        upFloor = visitFloor(currFloor, u, True)
        downFloor = visitFloor(currFloor, d, False)

        if upFloor not in visitedFloors:
            visitedFloors[upFloor] = numberOfPushes + 1
            q.append((upFloor, numberOfPushes+1))
        
        if downFloor not in visitedFloors:
            visitedFloors[downFloor] = numberOfPushes + 1
            q.append((downFloor, numberOfPushes+1))

    return 'use the stairs'
        

if __name__ == '__main__':
    print(main())