from sys import stdin
from collections import defaultdict
from heapq import *


def dijkstra(pq, D, road_adj_list, flight_adj_list, t):
    while pq:
        cost, city, flights = heappop(pq)
        
        # Reached destination, return cost
        if city == t:
            return cost
        
        # Explore neighbouring cities via roads
        for neighbour, travel_cost in road_adj_list[city]:
            if D[(neighbour, flights)] > cost + travel_cost:
                D[(neighbour, flights)] = cost + travel_cost
                heappush(pq, (D[(neighbour, flights)], neighbour, flights))
        
        # If have not used up free flight, we can explore neighbouring cities via flying
        if flights > 0:
            for neighbour in flight_adj_list[city]:
                if D[(neighbour, flights-1)] > cost:
                    D[(neighbour, flights-1)] = cost
                    heappush(pq, (D[(neighbour, flights-1)], neighbour, flights-1))


def main():
    n, m, f, s, t = map(int, stdin.readline().split())
    
    # Populate adjacency list for roads
    road_adj_list = [[] * n for _ in range(n)]
    for i in range(m):
        i, j, c = map(int, stdin.readline().split())
        road_adj_list[i].append((j, c))
        road_adj_list[j].append((i, c))
    
    # Populate adjacency list for flights
    flight_adj_list = [[] * n for _ in range(n)] 
    for i in range(f):
        u, v = map(int, stdin.readline().split())
        flight_adj_list[u].append(v)

    D = defaultdict(lambda: float('inf'))
    # (City, number of free flights remaining) = min cost to reach there from source
    # Only have 1 free flight
    D[(s, 1)] = 0

    pq = []
    # Push: (Total cost so far, current city, number of free flights remaining)
    heappush(pq, (0, s, 1))

    print(dijkstra(pq, D, road_adj_list, flight_adj_list, t))


if __name__ == '__main__':
    main()
