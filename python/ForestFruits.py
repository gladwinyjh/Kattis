from sys import stdin
from heapq import heappush, heappop


def dijkstra(pq, D, adj_list, fruits, fruits_set, C):
    while pq:
        dist, clearing = heappop(pq)

        if D[clearing] == dist:
            # Because we only want to update the shortest distance to clearing with fruit
            # So put this if statement in here and not outside!!
            if clearing in fruits_set:
                fruits[clearing] = dist * 2
                
            for v, dist_to in adj_list[clearing]:
                if D[v] > dist + dist_to:
                    D[v] = dist + dist_to
                    heappush(pq, (D[v], v))


def main():
    V, E, C, K, M = map(int, stdin.readline().split())
    
    adj_list = [[] * (V+1) for _ in range(V+1)]
    for i in range(E):
        u, v, w = map(int, stdin.readline().split())
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    
    # Distance to clearing with fruits
    fruits = [float('inf')] * (V+1)
    # Set to check if clearing has a batch of fruits
    fruits_set = set(map(int, stdin.readline().split()))

    D = [float('inf')] * (V+1)
    D[1] = 0
    
    pq = []
    heappush(pq, (0, 1))

    dijkstra(pq, D, adj_list, fruits, fruits_set, C)
    # Sort so smaller distances are placed towards the front of list
    fruits.sort()
    
    # Only need to consider either the first K distances or the first M distances
    # If K < M, we will loop back to first index after K days before we reach day M
        # So consider fruits[:K]
    
    # If K > M, we will only access each index once because K is too large to loop back
        # So consider fruits[:M]

    # If K == M, no difference if we take [:M] or [:K]
    if K <= M:
        max_walk = max(fruits[:K])
    else:
        max_walk = max(fruits[:M])
    
    # If there is an INF in the first K or first M distances, there are not enough reachable clearings with fruits
    if max_walk == float('inf'):
        print(-1)
    else:
        print(max_walk)


if __name__ == '__main__':
    main()
