from sys import stdin
from collections import deque


def within_grid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def main():
    W, H = map(int, stdin.readline().split())

    grid = []
    q = deque()
    for i in range(H):
        row = list(stdin.readline().rstrip())
        for j in range(len(row)):
            if row[j] == 'P':
                q.append((i, j))
                # 'V' for visited
                row[j] = 'V'

        grid.append(row)
    
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    gold = 0
    while q:
        r, c = q.popleft()
        
        # Check if the adjacent cells are 'T'
        # Cell is determined to be risky if any of the adjacent cells is 'T', player do not know where 'T' is
        # Should not proceed further
        risk = False
        for i in range(4):
            new_r = r + DIR[i][0]
            new_c = c + DIR[i][1]

            if within_grid(new_r, new_c, grid) and grid[new_r][new_c] == 'T':
                risk = True
                break

        if risk:
            # Current cell is risky, skip
            continue

        for i in range(4):
            new_r = r + DIR[i][0]
            new_c = c + DIR[i][1]
            
            # Skip direction if next cell is visited or next cell is a wall
            if grid[new_r][new_c] == 'V' or grid[new_r][new_c] == '#':
                continue
            
            # If current cell is 'G', increment gold
            if grid[new_r][new_c] == 'G':
                gold += 1
            
            # Append to queue, mark cell as visited
            q.append((new_r, new_c))
            grid[new_r][new_c] = 'V'

    print(gold)


if __name__ == '__main__':
    main()
    # Flood fill
        # Cannot traverse further if adjacent cells contain at least one 'T'
        # Flood fill is suitable because player can travel back to visited cells to other unvisited cells to collect gold
            # Just that those visited cells won't give gold anymore
        
        # Ex:
            # G . . P . G G
                # Flood fill is same as going left all the way, then right all the way. Or right all the way then left all the way
            
