from collections import deque


def withinGrid(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def main():
    t = int(input())
    
    for k in range(t):
        w, h = map(int, input().split())
        
        building = []
        fireQueue = deque()
        personQueue = deque()
        for i in range(h):
            line = list(input())
            for idx, x in enumerate(line):
                if x == '*':
                    fireQueue.append((i, idx))
                elif x == '@':
                    personLoc = (i, idx)
                    personQueue.append(personLoc)
                    # Person location can be taken as an open space because fire can spread to it
                    line[idx] = '.'

            building.append(line)
        
        # Visited dictionary to check if person's location have already been checked before
        # Value indicates the time elapsed when the person enters the open space
        visited = {personLoc: 0}
        # Flag for exit
        escaped = False
        # Direction list to help with checking adjacent cells
        DIR = [(1,0), (-1,0), (0,1), (0,-1)] 

        # Two BFS, but fire queue first then person queue
        while personQueue:
            numFireStates = len(fireQueue)
            # Expand the fires first since they take priority
            # Go through each cell with a fire and expand them
            # Only go through the queue once (1 cycle of spreading)
            while numFireStates:
                fireRow, fireCol = fireQueue.popleft()

                for i in range(4):
                    newFireRow = fireRow + DIR[i][0]
                    newFireCol = fireCol + DIR[i][1]

                    # If within the grid and adjacent cell is an open space.
                    # If we include fires too, there will be an infinite loop
                    if withinGrid(newFireRow, newFireCol, building) and building[newFireRow][newFireCol] == '.':
                        building[newFireRow][newFireCol] = '*'
                        fireQueue.append((newFireRow, newFireCol))
                
                numFireStates -= 1
            
            numPersonStates = len(personQueue)
            # Similar to fires
            # Go through all cells where the person is at (intially only the one starting location)
            # Check if person can move in the 4 directions (fires are already accounted for in previous while loop)
            while numPersonStates:
                personRow, personCol = personQueue.popleft()
                
                # Person is at the perimeter of the building == found an exit
                # Get the time elapsed to reach this location + 1 because need one more second to escape
                if personRow == 0 or personRow == h-1 or personCol == 0 or personCol == w-1:
                    print(visited[(personRow, personCol)] + 1)
                    escaped = True
                    break
                
                for i in range(4):
                    newPersonRow = personRow + DIR[i][0]
                    newPersonCol = personCol + DIR[i][1]

                    if withinGrid(newPersonRow, newPersonCol, building) and (newPersonRow, newPersonCol) not in visited and building[newPersonRow][newPersonCol] == '.':
                        visited[(newPersonRow, newPersonCol)] = visited[(personRow, personCol)] + 1
                        personQueue.append((newPersonRow, newPersonCol))
                
                numPersonStates -= 1
            
            # Just to break out of while loop
            if escaped:
                break
        
        # Have not found an escape location
        if not escaped:
            print('IMPOSSIBLE')
        

if __name__ == '__main__':
    main()
