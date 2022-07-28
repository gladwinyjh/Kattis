from sys import stdin


def within_grid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def flow_down(grid, basin, r, c, letter, DIR):
    max_r = r
    max_c = c
    max_drop = 0
    for i in range(4):
        new_r = r + DIR[i][0]
        new_c = c + DIR[i][1]
        
        # Find the adjacent cell that gives the largest drop in altitude
        # Since direction is specific, store the first encounter if tie (i.e dont check if equal drop)
        if within_grid(new_r, new_c, grid) and grid[r][c] - grid[new_r][new_c] > max_drop:
            max_drop = grid[r][c] - grid[new_r][new_c]
            max_r = new_r
            max_c = new_c
    
    if (max_r, max_c) != (r, c): # Found a lower cell
        # Next cell alr assign a basin 
        if basin[max_r][max_c] != -1:
            # Assign current cell to that basin
            basin[r][c] = basin[max_r][max_c]
            # Update last encountered basin number
            letter[0] = basin[max_r][max_c]
        else:
            # If adjacent cell still unassigned, can still explore lower down
            flow_down(grid, basin, max_r, max_c, letter, DIR)
    else:
        # Current cell is the lowest of all 4 adjacent cells and is unassigned a basin
        # Assign it to be a sink
        if basin[r][c] == -1:
            basin[r][c] = letter[1]
            # Update last encountered basin number
            letter[0] = letter[1]
            # Increment next sink number
            letter[1] += 1


def main():
    T = int(stdin.readline())

    for i in range(1, T+1):
        H, W = map(int, stdin.readline().split())

        grid = []
        basin = [[-1] * W for _ in range(H)]
        for j in range(H):
            grid.append(list(map(int, stdin.readline().split())))
        
        # Order of direction matters: North, West, East, South
        DIR = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        # Stores [last encountered basin number for current cell during DFS, next basin]
        letter = [1, 1]
        for j in range(H):
            for k in range(W):
                # If current basin already has a label, no need to explore from it
                if basin[j][k] == -1:
                    # DFS, only going through a specific direction
                    flow_down(grid, basin, j, k, letter, DIR)
                    
                    # If basin[j][k] is still unassigned, it means that the DFS did not reach a sink
                    # So assign it the basin number of the last encountered cell, letter[0]
                    if basin[j][k] == -1:
                        basin[j][k] = letter[0]

        print(f'Case #{i}:')
        for row in basin:
            [print(' '.join([chr(x + 96) for x in row]))]


if __name__ == '__main__':
    main()
