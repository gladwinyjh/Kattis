from sys import stdin
from collections import deque


def within_town(r, c, town):
    return 0 <= r < len(town) and 0 <= c < len(town[0])


def main():
    n = int(stdin.readline())
    
    town = []
    # To record the number of '1' cells in the town
    num_1 = 0
    q = deque()
    # To store shortest path from any '3' cell to the current cell (i, j)
    D = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        row = list(stdin.readline().rstrip())
        for j in range(n):
            if row[j] == '3': # Starting points are '3's
                q.append((i, j, 0))
                D[i][j] = 0
            
            if row[j] == '1':
                num_1 += 1
        
        town.append(row)
    
    # Update max distance
    max_dist = -1
    # Direction list for navigation
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]] 

    # Multisource BFS
    while num_1:  # while there are still '1's to reach
        r, c, dist = q.popleft()

        if town[r][c] == '1':
            # Number of '1's left reduce by 1
            num_1 -= 1
            max_dist = max(max_dist, dist)
            # Note that we continue BFS here as the shortest path from another '1' to any '3' can pass through other '1' cells
        
        for i in range(4):
            new_r = r + DIR[i][0]
            new_c = c + DIR[i][1]

            if within_town(new_r, new_c, town) and D[new_r][new_c] > dist + 1:
                # Only the shortest path gets stored and updated
                D[new_r][new_c] = dist + 1
                q.append((new_r, new_c, dist+1))

    print(max_dist)


if __name__ == '__main__':
    # Do BFS from all '3' cells with goal at all '1' cells. If do BFS from '1' cells it will be too slow
    # But do not stop BFS when reach '1' cell because might have to travel to other '1' cells via this '1' cell
    main()
