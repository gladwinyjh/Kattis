from sys import stdin
from collections import deque


def within_grid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def BFS(q, grid, visited, n, l):
    num_moves = 0
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        # Reached limit to the number of moves
        # Return no solution
        if num_moves > l:
            return 'NO SOLUTION'

        q_length = len(q)
        
        # Move robot one at the time
        # Process queue completely for each move
        while q_length:
            positions = q.popleft()
                
            # Robot 1 reached X'
            if grid[positions[1][0]][positions[1][1]] == 'X':
                return num_moves
            
            # For each robot 1 to n inclusive, try moving in all directions
            for i in range(1, n+1):
                r = positions[i][0]
                c = positions[i][1]

                for j in range(4):
                    new_r = r
                    new_c = c
                    
                    # Keep moving in a direction until next cell is:
                        # 1) Out of grid
                        # 2) A wall
                        # 3) A position of a robot
                    while (within_grid(new_r, new_c, grid) and
                            grid[new_r][new_c] != 'W'):
                        
                        # Because positions stores the initial robots position,
                        # Ignore the same position flag for the first iteration
                        # For other iterations when the robot is at a different position,
                            # Same positions flag will be for other robots only
                        if ((new_r, new_c) not in positions.values() or
                                positions[i] == (new_r, new_c)):
                            # Keep moving in the direction
                            new_r += DIR[j][0]
                            new_c += DIR[j][1]
                        else:
                            # Next position is same as other robots, stop moving further
                            break
                    
                    # Cannot move in this direction AT ALL
                    # This is if while loop is not entered at all
                    if new_r == r and new_c == c:
                        continue
                    
                    # At this point, the new position is 1 step ahead of the limit it can go
                        # Because while loop adds before checking if valid
                        # So need to go back one position
                    new_r -= DIR[j][0]
                    new_c -= DIR[j][1]
                    
                    # While loop and its interior if loop was accessed
                    # Check if position is same as initial position again
                    if new_r == r and new_c == c:
                        continue
                    
                    # Make a copy of the dictionary
                    new_positions = positions.copy()
                    # Change robot's position to new position
                    new_positions[i] = (new_r, new_c)
                    
                    # Get the new current positions of all the robots
                    # Only the position of 1 robot has changed
                    # There is prob a better and faster way to do this...
                    curr = []
                    for k, v in new_positions.items():
                        curr.append((k, v))
                    
                    curr = tuple(curr)
                    # Check if the current positions have been visited before
                    if curr not in visited:
                        visited.add(curr)
                        # Add to queue if not visited
                        q.append(new_positions)

            q_length -= 1
        
        num_moves += 1
    
    # Reached end of BFS with no solution
    return 'NO SOLUTION'
        

def main():
    n, w, h, l = map(int, stdin.readline().split())
    
    grid = []
    q = deque()
    robot_pos = {}
    curr = []
    for i in range(h):
        row = list(stdin.readline().rstrip())
        for j in range(len(row)):
            if row[j] != '.' and row[j] != 'W' and row[j] != 'X':
                robot_pos[int(row[j])] = (i, j)
                curr.append((int(row[j]), (i, j)))
                row[j] = '.'

        grid.append(row)
    
    # Used to keep track of the positions of all the robots
    visited = set()
    # Store current position of robots
    visited.add(tuple(curr))

    q.append(robot_pos)
    
    # BFS essentially try every direction for every robot one at a time
    # Keep track of the states of the robots to prevent revisiting the same states
    print(BFS(q, grid, visited, n, l))


if __name__ == '__main__':
    main()
