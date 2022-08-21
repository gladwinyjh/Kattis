from sys import stdin
from collections import deque


def within_grid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def main():
    N, M = map(int, stdin.readline().split())
    
    # Pad grid with a thickness of 1 of sea around all sides
    grid = [[0] * (M+2)]
    for i in range(N):
        row = [0]
        row.extend(list(map(int, stdin.readline().rstrip())))
        row.append(0)
        grid.append(row)

    grid.append([0] * (M+2))
    
    # Start with top left cell, it is always the sea because of padding
    q = deque([(0, 0)])
    # Mark it as visited to prevent revisits
    grid[0][0] = -1
    
    DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    coast_length = 0
    # BFS floodfill
    while q:
        r, c = q.popleft()
        
        # Land
        if grid[r][c] == 1:
            # Increment length
            coast_length += 1
            # Don't include this cell as any other land cells will be within island
            continue
        
        # 4 side, so 4 directions
        for i in range(4):
            new_r = r + DIR[i][0]
            new_c = c + DIR[i][1]
            
            # Within grid and not visited(only for sea cells)
            if within_grid(new_r, new_c, grid) and grid[new_r][new_c] >= 0:
                # If sea cell, mark it as visited
                # Land cells can still be visited from other sides (max 4 times)
                if grid[new_r][new_c] == 0:
                    grid[new_r][new_c] = -1
                
                # Add to queue
                q.append((new_r, new_c))


    print(coast_length)


if __name__ == '__main__':
    main()
