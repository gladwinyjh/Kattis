from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict


def dijkstra(pq, D, k, POS_DICT):
    while pq:
        dist, curr, r, c = heappop(pq)

        if curr == k:
            return dist

        if D[r][c] == dist:
            # Get all of next tile positions from POS_DICT
            for next_r, next_c in POS_DICT[curr + 1]:
                # Manhattan distance
                dist_away = abs(r - next_r) + abs(c - next_c)
                
                # Update shortest distance
                if D[next_r][next_c] > dist + dist_away:
                    D[next_r][next_c] = dist + dist_away
                    heappush(pq, (D[next_r][next_c], curr + 1, next_r, next_c))

    return -1


def main():
    n, k = map(int, stdin.readline().split())
    
    POS_DICT = defaultdict(list)
    pq = []
    D = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        row = list(map(int, stdin.readline().split()))
        for j in range(n):
            POS_DICT[row[j]].append((i, j))
            
            if row[j] == 1:
                # (distance so far, tile number, row, column)
                heappush(pq, (0, 1, i, j))
                D[i][j] = 0

    print(dijkstra(pq, D, k, POS_DICT))



if __name__ == '__main__':
    main()
    # Store  all positions of each number tile in dictionary
    # At each position BFS to next number tile by iterating through all possible positions in dictionary
        # Calculate manhattan distance each time
        # May be good to use PQ so that smallest distances get processed first

    # If use PQ, return value once reached
    # If regular Q, return the max of the distances each time reach k
