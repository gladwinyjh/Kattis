from collections import deque


def withinGrid(row, col, grid):
        return 0 <= col < len(grid[0]) and 0 <= row < len(grid)


def main():
    N, M = map(int, input().split())

    grid = []
    q = deque()
    for i in range(N):
        row = list(input())
        # Add intial water sources to queue
        for idx, x in enumerate(row):
            if x == 'V':
                q.append((i, idx))
        grid.append(row)
    
    # Visited 2d grid to check if cell has been visited before
    visited = [[0]*M for _ in range(N)]
    while q:
        row, col = q.popleft()
        
        # Coordinates are within grid
        # Cell has not been visited before
        # Cell is not a stone cell (Stone cells dont do anything)
        if withinGrid(row, col, grid) and not visited[row][col] and grid[row][col] != '#':
            # Mark as visited
            visited[row][col] = 1
            # Change air cell to 'V'
            grid[row][col] = 'V'
            
            # Check if cell below if valid
            if withinGrid(row+1, col, grid):
                # If cell below this new water cell is an air cell, add it to the queue
                if grid[row+1][col] == '.':
                    q.append((row+1, col))
                # if cell below this new water cell is a stone cell, add the left and right cell to the queue
                if grid[row+1][col] == '#':
                    q.append((row, col-1))
                    q.append((row, col+1))

    for row in grid:
        print(''.join(row))


if __name__ == '__main__':
    main()
