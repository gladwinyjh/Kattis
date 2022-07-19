from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(pq, D, adj_list, fuel_prices, c, e):
    while pq:
        cost, city, fuel = heappop(pq)

        if city == e:
            # Reached destination
            return cost
        
        if D[(city, fuel)] == cost:
            # At each city, can choose to fuel up x number of times till c
            # Don't know how much to top up fuel to, so keep adding 1
            if fuel < c and D[(city, fuel+1)] > cost + fuel_prices[city]:
                D[(city, fuel+1)] = cost + fuel_prices[city]
                heappush(pq, (D[(city, fuel+1)], city, fuel+1))      
            
            # If there is enough fuel, travel to neighbour if shortest distance can be updated
            for neighbour, travel in adj_list[city]:
                if fuel >= travel and D[(neighbour, fuel-travel)] > cost:
                    D[(neighbour, fuel-travel)] = cost
                    heappush(pq, (cost, neighbour, fuel-travel))
    
    return 'impossible'


def main():
    n, m = map(int, stdin.readline().split())
    
    # This is fuel prices PER LITRE, not fuel price of a full tank
    fuel_prices = list(map(int, stdin.readline().split()))
    
    adj_list = [[] * n for _ in range(n)]
    for i in range(m):
        u, v, d = map(int, stdin.readline().split())
        adj_list[u].append((v, d))
        adj_list[v].append((u, d))

    for i in range(int(stdin.readline())):
        c, s, e = map(int, stdin.readline().split())

        D = defaultdict(lambda: float('inf'))
        # (city, fuel) = cost
        D[(s, 0)] = 0

        pq = []
        # (smallest cost at city x and fuel level y, city x, fuel level y)
        heappush(pq, (D[(s, 0)], s, 0))
        
        print(dijkstra(pq, D, adj_list, fuel_prices, c, e))


if __name__ == '__main__':
    main()
