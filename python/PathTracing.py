from sys import stdin


def main():
    # Store the min and max bounds for row and col relative to the starting position
    min_r = 0
    max_r = 0
    min_c = 0
    max_c = 0
    # Starting position
    start = [0, 0]
    # Path for reconstruction
    path = []
    for line in stdin:
        direction = line.rstrip()
        
        # Update min and maxes, and append to path after each directional change
        if direction == 'up':
            start[1] -= 1
            min_r = min(min_r, start[1])
            path.append([-1, 0])
        elif direction == 'down':
            start[1] += 1
            max_r = max(max_r, start[1])
            path.append([1, 0])
        elif direction == 'left':
            start[0] -= 1
            min_c = min(min_c, start[0])
            path.append([0, -1])
        else:
            start[0] += 1
            max_c = max(max_c, start[0])
            path.append([0, 1])
    
    # Starting position in a grid with (0, 0) at the top left
    true_start = [-min_r, -min_c]
    # Total number of rows and cols, + 1 they are the change relative to the intial starting point
    rows = max_r - min_r + 1
    cols = max_c - min_c + 1

    grid = [[' '] * cols for _ in range(rows)]
    grid[true_start[0]][true_start[1]] = 'S'
    
    for r, c in path:
        true_start[0] += r
        true_start[1] += c
        # Path may go back to visited cells or the starting positions
        # Don't need to change those cells to '*'
        if grid[true_start[0]][true_start[1]] == ' ':
            grid[true_start[0]][true_start[1]] = '*'
    
    # Last coordinate is the ending
    grid[true_start[0]][true_start[1]] = 'E'
    
    # Print map
    print('#'  * (cols+2))
    for row in grid:
        print('#', end='')
        [print(cell, end='') for cell in row]
        print('#')
    print('#' * (cols+2))


if __name__ == '__main__':
    main()

