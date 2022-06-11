from sys import stdin
from heapq import *


def within_cave(r, c, cave):
    return 0 <= r < len(cave) and 0 <= c < len(cave[0])


def dijkstra(pq, dist, risk_map, D, cave):
    while pq:
        risk, pos = heappop(pq)

        if pos == D:
            # Found a diamond
            return risk

        if risk == dist[pos[0]][pos[1]]:
            for i in range(4):
                new_r = pos[0] + DIR[i][0]
                new_c = pos[1] + DIR[i][1]
                
                # Check that it is within cave, it is not a wall, and new accumulated risk is lower than current stored one
                if (within_cave(new_r, new_c, cave) and
                        cave[new_r][new_c] != '#' and
                        dist[new_r][new_c] > dist[pos[0]][pos[1]] + risk_map[new_r][new_c]):
                    dist[new_r][new_c] = dist[pos[0]][pos[1]] + risk_map[new_r][new_c]
                    heappush(pq, (dist[new_r][new_c], (new_r, new_c)))


def main():
    L, W = map(int, stdin.readline().split())
    
    cave = []
    empty = []
    dist = [[float('inf')] * W for _ in range(L)] 
    # Take in cave input
    # Note down coordinates of the entrance E and diamond D
    for i in range(L):
        row = list(stdin.readline())[:-1]
        for j in range(len(row)):
            if row[j] == ' ':
                empty.append((i, j))
            elif row[j] == 'E':
                E = (i, j)
                # Distance from source to source = 0
                dist[i][j] = 0
            elif row[j] == 'D':
                D = (i, j)
                
        cave.append(row)
    
    # To help with navigation
    global DIR
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    # The 'risk' defined in the problem is the chance that the grue will be found the moment you step into the cave
    # Because the grue moves with uniform probability to adjacent empty cells
    # the more sides a cell share with other empty cells, the higher the chance a grue can be found in the cell
    # Ex: Cell A shares 4 sides with empty cells -> A has a risk of 4
    #   : Cell B shares 1 side with an empty cell -> B has a risk of 1

    # Note that the max number of sides a cell can share is 4 because its a square
    # The grue stops moving once you enter the cave, so the risk is fixed per cell
    # To get the least risk, we find the path that has the least accumulated risk over the cells you travel across
    # To get the likelihood, we take this accumulated risk and divide it by the total risk of all the empty cells

    # Use a map to mark the risks of each empty cell
    # It is like the cost of entering the cell
    risk_map = [[0] * W for _ in range(L)]
    # Variable to store the total risk of all the empty cells
    total_risk = 0
    for pos in empty:
        # Check adjacent cells for empty cells
        for i in range(4):
            new_r = pos[0] + DIR[i][0]
            new_c = pos[1] + DIR[i][1]
            
            # Empty cell found -> Increment the risk for that cell
            if within_cave(new_r, new_c, cave) and cave[new_r][new_c] == ' ':
                 risk_map[pos[0]][pos[1]] += 1
                 total_risk += 1
    
    # Push source to PQ
    pq = []
    heappush(pq, (0, E))
    
    # Do Dijkstra's and print the result for the accumulated risk of entering D: dist[D]
    # The total risk can never go below 0 because problem states that there are at least 2 empty cells
    # So dont need to worry about division by zero
    print(f'{dijkstra(pq, dist, risk_map, D, cave) / total_risk:.6f}')


if __name__ == '__main__':
    main()
