from sys import stdin
from heapq import *


def within_terrain(r, c, terrain):
    return 0 <= r < len(terrain) and 0 <= c < len(terrain[0])


def dijkstra(pq, D, terrain):
    DIR = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    minimax = float('inf') 

    while pq:
        curr_max, r, c = heappop(pq)
        
        # Each time we reach the right side of the terrain
        # Update the minimax value
        if c == len(terrain[0])-1:
            minimax = min(minimax, curr_max)
            # Don't need to do anymore travelling
            continue

        for i in range(4):
            new_r = r + DIR[i][0]
            new_c = c + DIR[i][1]

            if within_terrain(new_r, new_c, terrain):
                new_max = max(terrain[new_r][new_c], curr_max)
                
                if D[new_r][new_c] > new_max:
                    D[new_r][new_c] = new_max
                    heappush(pq, (new_max, new_r, new_c))
        
    return minimax


def main():
    r, c = map(int, stdin.readline().split())
    
    terrain = []
    D = [[float('inf')] * c for _ in range(r)]
    pq = []
    for i in range(r):
        row = list(map(int, stdin.readline().split()))

        # Intially, only 1 edge from path to itself
        D[i][0] = row[0]
        terrain.append(row)
        heappush(pq, (row[0], i, 0))
    
    # Minimax Dijkstra, with multiple sources (all vertices from first col) and no end target
    # D will be a 2d list that contains the minimax of the vertex to any vertex from the first col
    print(dijkstra(pq, D, terrain))
   

if __name__ == '__main__':
    main()
