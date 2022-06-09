from heapq import *
from sys import stdin


def dijkstra(D, pq, adjList, num_ways, t):
    while pq:
        dist, node = heappop(pq)

        if dist == D[node]:
            for neighbour, weight in adjList[node]:
                new_dist = D[node] + weight
                
                # Shortest distance to reach neighbour is same as shortest distance to reach here via this new path
                # So increment the number of ways to reach this neighbour by the number of ways to reach the predecessor
                if D[neighbour] == new_dist:
                    num_ways[neighbour] += num_ways[node]
                    
                if D[neighbour] > new_dist:
                    # Found a shorter distance, update shortest distance
                    D[neighbour] = new_dist
                    # Number of ways to reach this neighbour = number of ways to reach predecessor
                    num_ways[neighbour] = num_ways[node]
                    heappush(pq, (D[neighbour], neighbour))
         

def main():
    V, E = map(int, stdin.readline().split())

    adjList = [[] * V for _ in range(V)]
    for i in range(E):
        u, v, w = map(int, stdin.readline().split())
        adjList[u].append((v, w))

    s, t = map(int, stdin.readline().split())

    D = [float('inf')] * V
    D[s] = 0
    
    # List that stores the number of ways to reach source to a node
    # Initialise with 1 for source (source to source only 1 way), and 0 for other nodes
    num_ways = [0] * V
    num_ways[s] = 1

    pq = []
    heappush(pq, (D[s], s))
    
    # Modified Dijkstra
    dijkstra(D, pq, adjList, num_ways, t)
    
    # Just print the number of ways to reach the destination node
    print(num_ways[t])

   
if __name__ == '__main__':
    main()
