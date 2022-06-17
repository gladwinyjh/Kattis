from sys import stdin
from heapq import *


def dijkstra(pq, adj_list, dist):
    while pq:
        distance, town = heappop(pq)

        if distance == dist[town]:
            for neighbour, travel in adj_list[town]:
                if dist[neighbour] > distance + travel:
                    dist[neighbour] = distance + travel
                    heappush(pq, (dist[neighbour], neighbour))
                

def main():
    while True:
        N, M, A, K = map(int, stdin.readline().split())
        
        if N == 0:
            return
        
        # Create adjacency list
        adj_list = [[] * (N+1) for _ in range(N+1)]
        for i in range(M):
            T_1, T_2, D = map(int, stdin.readline().split())
            adj_list[T_1].append((T_2, D))
            adj_list[T_2].append((T_1, D))

        dist = [float('inf')] * (N+1)
        
        # Dijkstra for each alien base
        # Obtain the dist list which gives the closest distance from the alien base to each town
        # Dont have to recreate dist list each time as the alien bases are added in and not removed
        for i in range(A):
            alien_base = int(stdin.readline())

            dist[alien_base] = 0
            pq = []
            heappush(pq, (0, alien_base))
            
            # Dijkstra
            dijkstra(pq, adj_list, dist)
            
            # Count how many towns are at least K distance away from an alien base
            safe_towns = 0
            # Start from index 1 as N starts from 1
            for safety_distance in dist[1:]:
                if safety_distance >= K:
                    safe_towns += 1
            
            print(safe_towns)

        print()


if __name__ == '__main__':
    main()
