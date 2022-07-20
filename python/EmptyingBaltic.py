from sys import stdin
from heapq import heappush, heappop


def within_grid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def main():
    h, w = map(int, stdin.readline().split())

    grid = []
    for i in range(h):
        grid.append(list(map(int, stdin.readline().split())))

    i, j = map(int, stdin.readline().split())
    
    water_drained = grid[i-1][j-1]
    pq = []
    heappush(pq, (water_drained, i-1, j-1))
    
    # Stores the negative of maximum amount of water that can be drained from current cell
    D = [[float('inf')] * w for _ in range(h)]
    # Water at which drain is located at will drain completely at the spot (i.e no flowing to other cells)
    D[i-1][j-1] = water_drained
    
    # Dijkstra from drain to all cells below sea level
    total_drained = 0
    while pq:
        max_drained, r, c = heappop(pq)

        if D[r][c] == max_drained:
            total_drained += -1 * max_drained

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue

                    new_r = r + i
                    new_c = c + j
                    
                    # 1) Within the grid
                    # 2) Grid is below sea level: water cannot flow against gravity up to land
                    # 3) Current maximum that can be drained from cell is greater than maximum of the negative of water that can be drained from neighbouring cell and current cell
                    if (within_grid(new_r, new_c, grid) and
                            grid[new_r][new_c] < 0 and 
                            D[new_r][new_c] > max(grid[new_r][new_c], max_drained)):
                        D[new_r][new_c] = max(grid[new_r][new_c], max_drained)
                        heappush(pq, (D[new_r][new_c], new_r, new_c))

    print(total_drained)


if __name__ == '__main__':
    main()

    """
        -------SEA LEVEL--------- 
                        __-1__ 
                __-2__
        __-3__    
        
        If drain is placed at -2, the sea level there will be at -2, and the water drained will be 2
        The cell at -3 can only drain to -2 because the drain is at -2, so the water drained there will also be 2
        The cell at -1 can only drain to -1 because that is where the land starts under water, so water drained there will be 1

        Can see that the water drained on a cell depends on its altitude, and its neighbouring cells altitude
        Negative of max(neighbour altitude, cell altitude) will give the max water drained at a cell when comparing with all 8 neighbours

    """
