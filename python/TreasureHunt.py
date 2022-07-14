from sys import stdin
from collections import defaultdict
from heapq import *


def dijkstra(pq, D, K, grid):
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
    
    while pq:
        day, stamina, r, c = heappop(pq)

        if grid[r][c] == 'G':
            return day

        if day == D[(stamina, r, c)]:
            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]

                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] != '#':
                    # Plain. S and G are counted as plains
                    if grid[new_r][new_c] == '.' or grid[new_r][new_c] == 'S' or grid[new_r][new_c] == 'G':
                        # Have at least 1 stamina to travel, Spend 1 stamina to travel
                        # Day when arrived at new cell is shorter than current shortest day for given stamina
                        if stamina >= 1 and D[(stamina-1, new_r, new_c)] > day:
                            D[(stamina-1, new_r, new_c)] = day
                            heappush(pq, (day, stamina-1, new_r, new_c))
                        
                        # Have less than 1 stamina. Rest till next day and spend 1 stamina to travel
                        elif D[(K-1, new_r, new_c)] > day + 1:
                            D[(K-1, new_r, new_c)] = day + 1
                            heappush(pq, (day+1, K-1, new_r, new_c))
                    
                    # Forest
                    if grid[new_r][new_c] == 'F':
                        # Have at least 2 stamina to travel, spend 2 stamina to travel
                        if stamina >= 2 and D[(stamina-2, new_r, new_c)] > day:
                            D[(stamina-2, new_r, new_c)] = day
                            heappush(pq, (day, stamina-2, new_r, new_c))
                        
                        # 1 <= K <= 100. So K must be >= 2 to be able to even travel to forest
                        elif K >= 2 and D[(K-2, new_r, new_c)] > day + 1:
                            D[(K-2, new_r, new_c)] = day + 1
                            heappush(pq, (day+1, K-2, new_r, new_c))
                    
                    # Mountain
                    if grid[new_r][new_c] == 'M':
                        # Have at least 3 stamina to travel, spend 3 stamina to travel
                        if stamina >= 3 and D[(stamina-3, new_r, new_c)] > day:
                            D[(stamina-3, new_r, new_c)] = day
                            heappush(pq, (day, stamina-3, new_r, new_c))
                        
                        # K must be >= 3 to even travel to mountain
                        elif K >= 3 and D[(K-3, new_r, new_c)] > day + 1:
                            D[(K-3, new_r, new_c)] = day + 1
                            heappush(pq, (day+1, K-3, new_r, new_c))
    
    # Unable to reach G
    return -1


def main():
    N, M, K = map(int, stdin.readline().split())
    
    grid = []
    D = defaultdict(lambda: float('inf'))
    pq = []

    for i in range(N):
        row = list(stdin.readline().rstrip())
        for j in range(M):
            if row[j] == 'S':
                # (day, stamina, row, col)
                # Start from day 1
                heappush(pq, (1, K, i, j))
                D[(K, i, j)] = 1
    
        grid.append(row)

    print(dijkstra(pq, D, K, grid))
           

if __name__ == '__main__':
    main()
