from sys import stdin
from collections import deque


def within_maze(row, col, R, C):
    return 0 <= row < R and 0 <= col < C


def BFS(joe_queue, fire_queue, maze, visited, R, C):
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    earliest_time = 0
    
    while joe_queue:
        # Spread the fire first FOR THE CURRENT MINUTE 
        fire_queue_length = len(fire_queue) 
        while fire_queue_length:
            row, col = fire_queue.popleft()

            for i in range(4):
                new_row = row + DIR[i][0]
                new_col = col + DIR[i][1]

                if within_maze(new_row, new_col, R, C) and maze[new_row][new_col] == '.':
                    # Replace with 'F' to prevent additional checking in future loops
                    maze[new_row][new_col] = 'F'
                    fire_queue.append((new_row, new_col))

            fire_queue_length -= 1
       
        # Do the same thing with Joe
        joe_queue_length = len(joe_queue)
        while joe_queue_length:
            ROW, COL = joe_queue.popleft()
            
            # Reached the edge of the maze
            # Because queue is used, this is the earliest time
            # Return True for exit found, earliest + 1 (need 1 more move to exit maze)
            if ROW == 0 or ROW == R-1 or COL == 0 or COL == C-1:
                return (True, earliest_time + 1)

            for i in range(4):
                new_ROW = ROW + DIR[i][0]
                new_COL = COL + DIR[i][1]

                if (within_maze(new_ROW, new_COL, R, C) and 
                        not visited[new_ROW][new_COL] and
                        maze[new_ROW][new_COL] == '.'):
                    visited[new_ROW][new_COL] = 1
                    joe_queue.append((new_ROW, new_COL))

            joe_queue_length -= 1
        
        # Increment minute passed
        earliest_time += 1
    
    # Unable to escape maze
    # Return False for exit not found, the 2nd item can be anything really
    return (False, earliest_time)


def main():
    R, C = map(int, stdin.readline().split())
    maze = []
    visited = [[0] * C for _ in range(R)]
    fire_queue = deque()
    joe_queue = deque()

    for i in range(R):
        row = list(stdin.readline())[:-1]
        for j in range(C):
            if row[j] == 'J':
                joe_queue.append((i, j))
                visited[i][j] = 1
                row[j] = '.'

            if row[j] == 'F':
                fire_queue.append((i, j))
        
        maze.append(row)
    
    # Multi-source double BFS flood fill
    # Returns (boolean for whether exit is found, earliest time elapsed)
    found_exit = BFS(joe_queue, fire_queue, maze, visited, R, C)
    
    if found_exit[0]:
        # Found the exit, return the earliest time
        print(found_exit[1])
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    main()
