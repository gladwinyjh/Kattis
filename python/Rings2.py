from sys import stdin
from collections import deque


def within_grid(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def main():
    n, m = map(int, stdin.readline().split())
    
    grid = []
    for i in range(n):
        grid.append(list(stdin.readline().rstrip()))
    
    # Queue to be used for BFS
    # (row, col, next ring number)
    q = deque()
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # Go through grid to check find the number of ring 1 trees
    for i in range(n):
        for j in range(m):
            # Not a tree
            if grid[i][j] != 'T':
                continue
            
            # All 'T' along the border of the grid have to be ring 1
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                q.append((i, j, 2)) # Next ring number == 2
                # Assign current tree cell as '1' for ring 1
                grid[i][j] = '1'
                
            else:
                # For those 'T' not along border, check 4 edges: UP DOWN LEFT RIGHT for any '.' ring 0 
                for k in range(4):
                    new_i = i + DIR[k][0]
                    new_j = j + DIR[k][1]

                    if within_grid(new_i, new_j, grid) and grid[new_i][new_j] == '.':
                        q.append((i, j, 2))
                        grid[i][j] = '1'
    
    # Initial number of rings
    # If queue is empty, the grid contains 0 trees
    if q:
        rings = 1
    else:
        rings = 0
    
    # BFS from outer rings to inner rings
    # Update number of rings after queue is emptied each iteration
    while q:
        ring_length = len(q)

        while ring_length:
            i, j, next_ring = q.popleft()
            
            # Check 4 edges
            # Any unassigned tree that shares an edge with this tree is assigned 'next_ring'
            for k in range(4):
                new_i = i + DIR[k][0]
                new_j = j + DIR[k][1]
                
                # Within grid and cell is a tree that has yet to be assigned a ring number
                if within_grid(new_i, new_j, grid) and grid[new_i][new_j] == 'T':
                    # Add to queue 
                    q.append((new_i, new_j, next_ring+1))
                    # Assign ring number to tree
                    grid[new_i][new_j] = str(next_ring)

            ring_length -= 1
        
        rings += 1
    
    # Number of rings will be 1 extra
    # Check the number of rings to determine how much to right justify
    if rings - 1 < 10:
        fill = 2
    else:
        fill = 3

    for row in grid:
        # Print each cell with right justify
        # Dont end each cell with new line
        [print(cell.rjust(fill, '.'), end='') for cell in row]
        # Print blank so that there will be a newline after each row
        print()


if __name__ == '__main__':
    main()
