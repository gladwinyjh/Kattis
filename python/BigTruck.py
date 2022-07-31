from sys import stdin
from heapq import heappush, heappop


def dijkstra(pq, D, F, t, adj_list, n):
    while pq:
        dist, items, loc = heappop(pq)

        if D[loc] == dist and F[loc] == items:
            if loc == n:
                return [dist, items]

            for b, d in adj_list[loc]:
                # If distance can be shorter, always update both D and F
                # Regardless if it takes less items
                if D[b] > dist + d:
                    D[b] = dist + d
                    F[b] = items + t[b-1]
                    heappush(pq, (D[b], items + t[b-1], b))
                # If distance is same, and can take more items
                # Take more items
                elif D[b] == dist + d and F[b] < items + t[b-1]:
                    F[b] = items + t[b-1]
                    heappush(pq, (D[b],  items + t[b-1], b))
    
    return ['impossible']


def main():
    n = int(stdin.readline())
    
    t = list(map(int, stdin.readline().split()))

    adj_list = [[] * (n+1) for _ in range(n+1)]
    for i in range(int(stdin.readline())):
        a, b, d = map(int, stdin.readline().split())
        adj_list[a].append((b, d))
        adj_list[b].append((a, d))
    
    # Stores the shortest distance from start to a location
    D = [float('inf')] * (n+1)
    D[1] = 0
    
    # Stores the largest amount of items from start to a location
    F = [float('inf')] * (n+1)
    F[1] = t[0]

    pq = []
    # Remember starting point can have items to take: t[1-1] = t[0]
    heappush(pq, (0, t[0], 1))

    print(*dijkstra(pq, D, F, t, adj_list, n))


if __name__ == '__main__':
    main()
