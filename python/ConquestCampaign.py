from collections import deque


def withinGrid(x, y, grid):
    return 1 <= x <= len(grid) and 1 <= y <= len(grid[0])


def main():
    R, C , N = map(int, input().split())
    num_cells = R * C
    grid = [[0] * C for _ in range(R)]
    
    q = deque()
    for i in range(N):
       q.append(tuple(map(int, input().split())))
    
    day = 0
    # Multi-source BFS
    while q:
        # Only process the day's cells
        q_length = len(q)

        while q_length:
            x, y = q.popleft()

            if grid[x-1][y-1] == 0:
                # Mark cell as conquered
                grid[x-1][y-1] = 1
                # 1 less cell to conquer
                num_cells -= 1
                
                # Conquer adjacent horizontal and vertical cells
                DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for i in range(4):
                    new_x = x + DIR[i][0]
                    new_y = y + DIR[i][1]
                    # Check if next cell is within grid
                    if withinGrid(new_x, new_y, grid):
                        q.append((new_x, new_y))
            
            q_length -= 1

        # End of day, increment day 
        day += 1
        
        # If there are already no cells remaining to be conquered, exit loop
        if num_cells == 0:
            break

    print(day)


if __name__ == '__main__':
    main()
