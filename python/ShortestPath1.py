from heapq import *
from sys import stdin


def dijkstra(D, pq, adjList):
    while pq:
        dist, node = heappop(pq)
        if dist == D[node]:
            for weight, neighbour in adjList[node]:
                if D[neighbour] > D[node] + weight:
                    D[neighbour] = D[node] + weight
                    heappush(pq, (D[neighbour], neighbour))


def main():
    while True:
        n, m, q, s = map(int, stdin.readline().split())

        if n == 0 and m == 0 and q == 0 and s == 0:
            return

        adjList = [[]*n for _ in range(n)]
        for i in range(m):
            u, v, w = map(int, stdin.readline().split())
            # One direction edges, careful!
            adjList[u].append((w, v))
        
        D = [float('inf')] * n
        D[s] = 0
        pq = []
        heappush(pq, (D[s], s))
        
        # Standard Dikjstra's for non-negative directed edges 
        dijkstra(D, pq, adjList)

        for i in range(q):
            dest = int(stdin.readline())
             
            if D[dest] == float('inf'):
                # Node not reachable since shortest distance from source have not been updated
                print('Impossible')
            else:
                print(D[dest])
        
        print()


if __name__ == '__main__':
    main()
