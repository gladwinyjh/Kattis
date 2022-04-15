def main():
    grid = []
    # grid_status shows whether a tile's value can be replaced
    # 0: can be replaced, 1: cannot be replaced because it was the result of an earlier addition
    # Each time a tile undergoes addition, the resultant tile cannot be changed, so it must be flagged
    grid_status = []
    for i in range(4):
        grid.append(list(map(int, input().split())))
        grid_status.append([0] * 4)

    DIR = int(input())

    if DIR == 0:
        for i in range(4):
            for j in range(1,4):                
                # Same number, can be both zeroes
                if grid[i][j] == grid[i][j-1]:
                    grid_status[i][j-1] = 1
                    grid[i][j-1] += grid[i][j]
                    grid[i][j] = 0

                # Different numbers, left number is zero
                elif grid[i][j-1] == 0:
                    # Find the first 0 to shift
                    # By default, set it to the index of edge = 0
                    first = 0
                    found = False
                    for k in range(j-1,-1,-1):
                        if grid[i][k] != 0:
                            first = k
                            found = True
                            break
                    
                    # There is a non-zero somewhere to the left
                    if found:
                        if grid_status[i][first] == 0:
                            # If the first non-zero tile is same value, add them up
                            if grid[i][first] == grid[i][j]:
                                grid_status[i][first] = 1
                                grid[i][first] += grid[i][j]
                                grid[i][j] = 0
                                continue
                        
                        # Non-zero found: Make zero on the right grid[i][first+1] = grid[i][j]
                        grid[i][first+1] = grid[i][j]
                        grid[i][j] = 0
                    
                    else:
                        # All tiles to its left are zeroes
                        # Set most left tile grid[i][0] = grid[i][j]
                        grid[i][0] = grid[i][j]
                        grid[i][j] = 0

    elif DIR == 1:
        for i in range(1,4):
            for j in range(4):  
                # Same number, can be both zeroes
                if grid[i][j] == grid[i-1][j]: 
                    grid_status[i-1][j] = 1
                    grid[i-1][j] += grid[i][j]
                    grid[i][j] = 0 

                # Different numbers, above number is zero
                elif grid[i-1][j] == 0:

                    # Find the first 0 to shift
                    # By default, set it to the index of edge = 0
                    first = 0
                    found = False
                    for k in range(i-1,-1,-1):
                        if grid[k][j] != 0:
                            first = k
                            found = True
                            break
                    
                    # There is a non-zero somewhere above 
                    if found:
                        if grid_status[first][j] == 0:
                            # If the first non-zero tile is same value, add them up
                            if grid[first][j] == grid[i][j]:
                                grid_status[first][j] = 1
                                grid[first][j] += grid[i][j]
                                grid[i][j] = 0
                                continue

                        grid[first+1][j] = grid[i][j]
                        grid[i][j] = 0
                    
                    else:
                        # All tiles to above are zeroes
                        # Set top most tile grid[0][j] = grid[i][j]
                        grid[0][j] = grid[i][j]
                        grid[i][j] = 0

    elif DIR == 2:
        for i in range(4):
            for j in range(2,-1,-1):
                # Same number, can be both zeroes
                if grid[i][j] == grid[i][j+1]:
                    grid_status[i][j+1] = 1
                    grid[i][j+1] += grid[i][j]
                    grid[i][j] = 0

                # Different numbers, right number is zero
                elif grid[i][j+1] == 0:
                    # Find the first 0 to shift
                    # By default, set it to the index of edge = 0
                    first = 0
                    found = False
                    for k in range(j+1,4):
                        if grid[i][k] != 0:
                            first = k
                            found = True
                            break
                    
                    # There is a non-zero somewhere to the right
                    if found:
                        if grid_status[i][first] == 0:
                            # If the first non-zero tile is same value, add them up
                            if grid[i][first] == grid[i][j]:
                                grid_status[i][first] = 1
                                grid[i][first] += grid[i][j]
                                grid[i][j] = 0
                                continue

                        grid[i][first-1] = grid[i][j]
                        grid[i][j] = 0
                    
                    else:
                        # All tiles to its right are zeroes
                        # Set right most tile grid[i][3] = grid[i][j]
                        grid[i][3] = grid[i][j]
                        grid[i][j] = 0

    else:
        for i in range(2,-1,-1):
            for j in range(4):  
                # Same number, can be both zeroes
                if grid[i][j] == grid[i+1][j]: 
                    grid_status[i+1][j] = 1
                    grid[i+1][j] += grid[i][j]
                    grid[i][j] = 0 

                # Different numbers, below number is zero
                elif grid[i+1][j] == 0:

                    # Find the first 0 to shift
                    # By default, set it to the index of edge = 0
                    first = 0
                    found = False
                    for k in range(i+1,4):
                        if grid[k][j] != 0:
                            first = k
                            found = True
                            break
                    
                    # There is a non-zero somewhere to the bottom
                    if found:
                        if grid_status[first][j] == 0:
                            # If the first non-zero tile is same value, add them up
                            if grid[first][j] == grid[i][j]:
                                grid_status[first][j] = 1
                                grid[first][j] += grid[i][j]
                                grid[i][j] = 0
                                continue

                        grid[first-1][j] = grid[i][j]
                        grid[i][j] = 0
                    
                    else:
                        # All tiles to below are zeroes
                        # Set bottom most tile grid[3][j] = grid[i][j]
                        grid[3][j] = grid[i][j]
                        grid[i][j] = 0
    
    # Print rows in grid
    for row in grid:
        print(*row)


if __name__ == '__main__':
    main()
