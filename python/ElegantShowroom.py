from sys import stdin
from heapq import *


def within_showroom(r, c, showroom):
    return 0 <= r < len(showroom) and 0 <= c < len(showroom[0])


def main():
    R, C = map(int, stdin.readline().split())

    showroom = []
    # Cars are 1 weight, Doors are 0 weight
    # Find cars and doors and replace them with respective weights
    for i in range(R):
        row = list(stdin.readline())[:-1]
        for j in range(C):
            if row[j] == 'c':
                row[j] = 1
            elif row[j] == 'D':
                row[j] = 0
        showroom.append(row)
    
    r, c = map(int, stdin.readline().split())
    
    D = [[float('inf')] * C for _ in range(C)]
    D[r-1][c-1] = 0

    pq = []
    heappush(pq, (0, (r-1, c-1)))
    
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # Dijkstra
    # Also possible to do BFS with 0/1 weights
        # Append left for 0 weight, append right for 1 weight
    while pq:
        num_cars, coor = heappop(pq)
        r = coor[0]
        c = coor[1]

        if r == 0 or r == R-1 or c == 0 or c == C-1:
            print(num_cars + 1)
            break

        if num_cars == D[r][c]:
            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]

                if (within_showroom(new_r, new_c, showroom) and
                        showroom[new_r][new_c] != '#' and
                        D[new_r][new_c] > num_cars + showroom[new_r][new_c]):
                    D[new_r][new_c] = num_cars + showroom[new_r][new_c]
                    heappush(pq, (D[new_r][new_c], (new_r, new_c)))
        

if __name__ == '__main__':
    main()
