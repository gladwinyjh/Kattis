from sys import stdin
from collections import deque


def within_grid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def BFS(q, t, grid, visited):
    elapsed = 0
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        q_length = len(q)

        while q_length:
            r, c = q.popleft()
            
            # On the boundary and within time limit
            if ((r == 0 or r == len(grid)-1 or c == 0 or c == len(grid[0])-1) and
                    elapsed <= t):
                return elapsed


            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]
                
                """
                    Conditions for new coordinates
                        1) Must be within grid
                        2) Must not be on fire (i.e != 1)
                        3) Must not have been visited (to prevent repeated visits)
                        4) If required to come from a certain direction, check if currently on that direction
                           If not required, then just enter

                """
                if (within_grid(new_r, new_c, grid) and
                        grid[new_r][new_c] != '1' and
                        not visited[new_r][new_c]):
                    if (grid[new_r][new_c] == '0' or
                            (grid[new_r][new_c] == 'U' and DIR[i] == [1, 0]) or
                            (grid[new_r][new_c] == 'D' and DIR[i] == [-1, 0]) or
                            (grid[new_r][new_c] == 'L' and DIR[i] == [0, 1]) or
                            (grid[new_r][new_c] == 'R' and DIR[i] == [0, -1])):
                        visited[new_r][new_c] = 1
                        q.append((new_r, new_c))
            
            q_length -= 1

        elapsed += 1

    return 'NOT POSSIBLE'


def main():
    t, N, M = map(int, stdin.readline().split())
    
    visited = [[0] * M for _ in range(N)]
    grid = []
    q = deque()
    for i in range(N):
        row = list(stdin.readline().rstrip())
        for j in range(M):
            if row[j] == 'S':
                q.append((i, j))
                visited[i][j] = 1

        grid.append(row)
    
    # Flood fill BFS
    print(BFS(q, t, grid, visited))


if __name__ == '__main__':
    main()
