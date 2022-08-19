from sys import stdin


def main():
    R, C = map(int, stdin.readline().split())
    
    grid = []
    for i in range(R):
        grid.append(list(stdin.readline().rstrip()))
    
    words = []

    # Go through rows and columns in grid
    # Update a starting index for the start of the next word
    # Can prob go through both rows and columns in 1 grid traversal...

    # Process rows
    for i in range(R):
        start = 0
        for j in range(C):
            # If blocked, only add if there are at least 2 letters
            if grid[i][j] == '#':
                if j > start + 1:
                    words.append(''.join(grid[i][start:j]))
                # Advance starting index of next word
                start = j+1
            
            # Reached end of row and it is not blocked and it is a valid word
            if grid[i][j] != '#' and j == C-1 and j >= start + 1:
                words.append(''.join(grid[i][start:j+1]))
    
    # Same logic for columns
    for j in range(C):
        start = 0
        for i in range(R):
            if grid[i][j] == '#':
                if i > start + 1:
                    words.append(''.join([grid[x][j] for x in range(start, i)]))
                start = i + 1

            if grid[i][j] != '#' and i == R-1 and i >= start + 1:
                words.append(''.join([grid[x][j] for x in range(start, i+1)]))

    # Get lexicographically smallest word
    print(sorted(words)[0])


if __name__ == '__main__':
    main()
