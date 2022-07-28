from sys import stdin


def main():
    R, C = map(int, stdin.readline().split())

    grid = []
    grid.append(['#'] * C)
    for i in range(R):
        row = list(stdin.readline().rstrip())
        grid.append(row)

    for i in range(C):
        a = 0
        period = 0
        # Traverse from bottom to top.
        # Due to extra row at top, we start from R instead of R-1
        for j in range(R, -1, -1):
            # Count the number of 'a's
            if grid[j][i] == 'a':
                a += 1
            # Count the number of periods
            elif grid[j][i] == '.':
                period += 1

            # Reached an obstacle
            elif grid[j][i] == '#':
                # Start from cell below obstacle 
                new_j = j + 1
                # Periods are above apples. So push out all periods first
                # Go downwards, changing all cells to periods while there are still periods
                while period:
                    grid[new_j][i] = '.'
                    # Go down
                    new_j += 1
                    # One less period to change
                    period -= 1
                
                # Do the same for apples next
                while a:
                    grid[new_j][i] = 'a'
                    new_j += 1
                    a -= 1
        
    for row in grid[1:]:
        print(''.join(row))


if __name__ == '__main__':
    main()
