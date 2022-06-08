from sys import stdin
from heapq import *


def dijkstra(D, pq, adjList, k, dest):
    while pq:
        time, k_so_far, node = heappop(pq)

        if node == dest:
            # Found destination node, return the shortest time
            return time

        if k_so_far == k:
            # Cannot exceed k, so skip
            continue
        
        if time == D[k_so_far][node]:
            # Shortest time so far for a given k and node
            for neighbour, weight in adjList[node]:
                if D[k_so_far + 1][neighbour] > time + weight:
                    # If time can be shorter, shorten it and add it to pq
                    D[k_so_far + 1][neighbour] = time + weight
                    heappush(pq, (D[k_so_far + 1][neighbour], k_so_far + 1, neighbour))
    
    # Unable to reach destination node, return -1
    return -1


def main():
    TC = int(stdin.readline())
    
    for i in range(TC):
        _  = stdin.readline()
        V = int(stdin.readline())

        adjList = [[]*V for _ in range(V)]
        # Populate adjacency list
        for j in range(V):
            edges = list(map(int, stdin.readline().split()))
            if edges[0] == 0:
                continue
            for k in range(1, len(edges)-1, 2):
                adjList[j].append((edges[k], edges[k+1]))

        Q = int(stdin.readline())
        while Q:
            s, t, k = map(int, stdin.readline().split())
            
            # Use 2D list to store shortest distance to reach node for a given k
            # range(k+1) because k >= 1
            D = [[float('inf')] * V for _ in range(k+1)]
            # Intialise: Source counts as a junction (so k_so_fart == 1), and the total distance travelled so far == 0
            D[1][s] = 0 

            pq = []
            # Push source to pq
            heappush(pq, (0, 1, s))
            
            # Dijkstra each time because source is changing 
            print(dijkstra(D, pq, adjList, k, t))

            Q -= 1

        print()


if __name__ == '__main__':
    main()
