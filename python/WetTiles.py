from collections import deque

# Function to check if tile coordinates are within grid
def withinGrid(y, x, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def floodfill(grid, leaks, T):
    q = deque()
    # Visited 2d list to keep track of the tiles that have been visited
    visited = [[0]*len(grid[0]) for _ in range(len(grid))]

    for i in range(0, len(leaks), 2):
        # Append(y,x, time elapsed)
        # Time elapsed starts from 1 because the water spreads AFTER first minute
        q.append((len(grid) - 1 -(leaks[i+1] - 1), leaks[i]-1, 1))
    
    # For counting the number of wet spots to be returned
    wetSpots = 0
    while q:
        y, x, timeVisited = q.popleft()
        
        # Time must be within stipulated
        # Tile must be within the grid
        # Tile must not be a wall
        # Tile must not have been visited before
        if timeVisited <= T and withinGrid(y, x, grid) and grid[y][x] != 'W' and visited[y][x] == 0:
            # Mark tile as visited
            visited[y][x] = 1
            # Increase number of wet spots
            wetSpots += 1
            
            # Check up down left right tiles. Increase the time elapsed
            q.append((y-1, x, timeVisited+1))
            q.append((y+1, x, timeVisited+1))
            q.append((y, x-1, timeVisited+1))
            q.append((y, x+1, timeVisited+1))
    
    return wetSpots


def main():
    while True:
        specs = list(map(int, input().split()))
        if len(specs) == 1:
            return

        grid = [[-1]*specs[0] for _ in range(specs[1])]
        
        leaks = []
        while len(leaks) < 2 * specs[3]:
            inp = input()
            [leaks.append(int(x)) for x in inp.split()]

        # Add leaks to grid
        # Remember that grid is 1 indexed in question and y-axis starts from bottom
        # specs[1] - 1 makes it start from bottom for y-axis
        # Both axis do a - 1 so that it can be read as 0 indexed for grid
        for i in range(0, len(leaks), 2):
            grid[specs[1] - 1 - (leaks[i+1]-1)][leaks[i]-1] = 'L'

        walls = []
        while len(walls) < 4 * specs[-1]:
            inp = input()
            [walls.append(int(x)) for x in inp.split()]
        
        # Add walls to grid
        for i in range(0, len(walls), 4):
            x1 = walls[i]-1 
            x2 = walls[i+2]-1 
            y1 = specs[1]-1-(walls[i+1]-1)
            y2 = specs[1]-1-(walls[i+3]-1)
            
            # Same x and y for both coordinates = only that tile is a wall
            if x1 == x2 and y1 == y2:
                grid[y1][x1] = 'W'
            
            # Wall is horizontal
            elif x1 == x2 and y1 != y2:
                if y1 <= y2:
                    for j in range(y1, y2+1):
                        grid[j][x1] = 'W'
                else:
                    for j in range(y2, y1+1):
                        grid[j][x1] = 'W'

            # Wall is vertical 
            elif x1 != x2 and y1 == y2:
                if x1 <= x2:
                    for j in range(x1, x2+1):
                        grid[y1][j] = 'W'
                else:
                    for j in range(x2, x1+1):
                        grid[y1][j] = 'W'

            # Wall is diagonal
            else:
                if x1 >= x2:
                    k = y2
                    for j in range(x2, x1+1):
                        grid[k][j] = 'W'
                        if y1 > y2:
                            k += 1
                        else:
                            k -= 1
                else:
                    k = y1
                    for j in range(x1, x2+1):
                        grid[k][j] = 'W'
                        if y1 > y2:
                            k -= 1
                        else:
                            k += 1
        
        # Perform multisource BFS flood fill
        print(floodfill(grid, leaks, specs[2]))


if __name__ == '__main__':
    main()
