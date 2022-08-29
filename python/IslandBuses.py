from sys import stdin
from collections import deque


def within_grid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def find_islands(islands, grid):
    q = deque()
    num_islands = 0

    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while islands:
        q.append(islands.pop())
        # New island, BFS from current island cell
        num_islands += 1
        while q:
            r, c = q.popleft()

            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]
                
                # Within grid
                # Island cell not yet visited(i.e not in islands set)
                if (within_grid(new_r, new_c, grid) and
                        (new_r, new_c) in islands):
                    # Mark island cell as visited by removing from set
                    islands.remove((new_r, new_c))
                    q.append((new_r, new_c))

    return num_islands


def find_bridges(bridges, grid):
    q = deque()
    num_bridges = 0

    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while bridges:
        q.append(bridges.pop())
        # New bridge, BFS from current bridge cell
        num_bridges += 1
        while q:
            r, c = q.popleft()

            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]

                # Within grid
                # Bridge cell not yet visited(i.e not in bridges set)
                if (within_grid(new_r, new_c, grid) and
                        (new_r, new_c) in bridges):
                    # Mark bridge cell as visited by remvoving it from set
                    bridges.remove((new_r, new_c))
                    q.append((new_r, new_c))
    
    return num_bridges
        

def find_buses(islands, grid):
    q = deque()
    num_buses = 0
    
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # Trying to find out the number of buses needed
    # From each island, try to traverse as far as possible, using bridges if necessary
    while islands:
        # We have a boolean flag to mark if cell is a bridge
        # This is because we won't be able to directly check it on grid
        # if we will be marking visited cells as -1 on grid
        q.append((*islands.pop(), False))
        # Starting island as visited to prevent revisiting
        grid[q[0][0]][q[0][1]] = -1
        # Each time the queue is empty and there are still island cells, there is a new bus needed to visit this island
        num_buses += 1 
        while q:
            r, c, on_bridge = q.popleft()

            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]
                
                # Within grid
                # Is not a '.' ocean
                # Is not visited
                if (within_grid(new_r, new_c, grid) and
                        grid[new_r][new_c] != '.' and
                        grid[new_r][new_c] != -1):
                    
                    # Can go from bridge to island before traversing an 'X'
                    if on_bridge and grid[new_r][new_c] == '#':
                        continue
                    
                    # Islands only
                    if grid[new_r][new_c] != 'B':
                        islands.remove((new_r, new_c))
                        # Append to queue, not on bridge
                        q.append((new_r, new_c, False))
                    else:
                        # Append to queue, on a bridge
                        q.append((new_r, new_c, True))

                    # Mark next cell as visited
                    grid[new_r][new_c] = -1

    return num_buses


def main():
    # Starting map number
    map_number = 1
    grid = []
    # Set used to store coordinates of islands: 'X' and '#'
    islands = set()
    # Set used to store coordinates of bridges: 'B'
    bridges = set()
    # Starting row index
    r = 0
    for line in stdin:
        if line == '\n':
            # Next line: process grid
            print('Map', map_number)

            # Find the number of islands
                # Will be manipulating islands set, so use a copy
                # Gist:
                    # BFS from every cell in islands unless cell is visited
            print('islands:', find_islands(islands.copy(), grid))

            # Find the number of bridges
                # Considering bridges are uni-directional, don't have to worry about bridges changing directions or crossing
                # Gist:
                    # BFS from every bridge cell only, unless cell is visited
            print('bridges:', find_bridges(bridges, grid))

            # Find the number of buses
                # Gist:
                    # BFS from every island('#' or 'X'), crossing bridges if needed
                    # If an island is isolated, it needs its own bus
                        # BFS will address this because queue will be empty
            print('buses needed:', find_buses(islands, grid))
            
            # New test case
            
            # Increase map number
            map_number += 1
            # Starting row index back to 0
            r = 0
            # Fresh empty grid
            grid = []
            # Empty islands and bridges set
            islands.clear()
            bridges.clear()
        else:
            row = list(line.rstrip())
            for c in range(len(row)):
                # Store islands coordinates in islands set
                if row[c] == '#' or row[c] == 'X':
                    islands.add((r, c))
                # Store bridges coordinates in bridges set
                elif row[c] == 'B':
                    bridges.add((r, c))

            grid.append(row)
            # Next row
            r += 1
    
    # THIS IS FOR THE LAST TEST CASE
    # EOF WILL ENTER HERE, SO NEED TO PROCESS ONE LAST TIME!
    print('Map', map_number)
    print('islands:', find_islands(islands.copy(), grid))
    print('bridges:', find_bridges(bridges, grid))
    print('buses needed:', find_buses(islands, grid))


if __name__ == '__main__':
    main()
