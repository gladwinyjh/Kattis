from sys import stdin
from collections import deque, defaultdict


def within_dungeon(level, row, col, dungeon):
    return 0 <= level < len(dungeon) and 0 <= row < len(dungeon[0]) and 0 <= col < len(dungeon[0][0])


def BFS(q, dungeon, visited, E):
    # Check up and down first, then north south east west
    DIR = [[1, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

    time_elapsed = 0
    while q:
        # Concerned with how many minutes, so only process queue length each minute
        # Then increment time_elapsed after processing for the minute 
        q_length = len(q)

        while q_length:
            cell = q.popleft()
            
            # Reached end point, return 
            if cell == E:
                return f'Escaped in {time_elapsed} minute(s).'
            
            for i in range(6):
                new_level = cell[0] + DIR[i][0]
                new_row = cell[1] + DIR[i][1]
                new_col = cell[2] + DIR[i][2]

                if (within_dungeon(new_level, new_row, new_col, dungeon) and
                        dungeon[new_level][new_row][new_col] != '#' and
                        not visited[(new_level, new_row, new_col)]):
                    visited[(new_level, new_row, new_col)] = 1
                    q.append((new_level, new_row, new_col))

            q_length -= 1

        time_elapsed += 1
    
    # Unable to reach, return Trapped!
    return f'Trapped!'


def main():
    while True:
        L, R, C = map(int, stdin.readline().split())

        if L == 0 and R == 0 and C == 0:
            return

        dungeon = []
        # Populate dungeon
            # For each level, append input as a string to level list. Append level to dungeon list
            # Note positions of starting and ending
        for i in range(L):
            level = []
            for j in range(R): 
                row = stdin.readline()[:-1]

                if 'S' in row:
                    S = (i, j, row.index('S'))

                if 'E' in row:
                    E = (i, j, row.index('E'))

                level.append(row)

            dungeon.append(level)
            _ = stdin.readline()
     
        q = deque([S])
        # Starting position as visited. Default not visited : 0
        visited = defaultdict(lambda: 0)
        visited[S] = 1
        # Standard BFS, but now just have to additionally check one more dimension
        print(BFS(q, dungeon, visited, E)) 


if __name__ == '__main__':
    main()
