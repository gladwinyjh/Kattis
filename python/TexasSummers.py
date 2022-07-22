from sys import stdin, stdout
from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(pq, D, prev, adj_list):
    while pq:
        sweat, spot = heappop(pq)
        
        # Reached class
        if spot == len(D)-1:
            shade_path = []
            # Get path with shades
            while prev[spot] != spot:
                if 0 <= spot < len(D)-2:
                    shade_path.append(spot)

                spot = prev[spot]
            
            # Empty shady path = did not go through shady spots
            if not shade_path:
                return ['-']
            else:
                # Path is in reversed, so return reversd list
                return shade_path[::-1]
        
        if D[spot] == sweat:
            for other_spot, dist in adj_list[spot]:
                if D[other_spot] > dist + sweat:
                    D[other_spot] = dist + sweat
                    prev[other_spot] = spot
                    heappush(pq, (D[other_spot], other_spot))


def main():
    n = int(stdin.readline())
    
    spots = []
    # n shady spots + dorm + class = n+2 total spots (0 to n+1 inclusive)
    for i in range(n+2):
        x, y = map(int, stdin.readline().split())
        spots.append((x, y))
    
    # Generate adjacency list here to not get TLE
    # Can calculate total sweat on the fly, but will get TLE
    adj_list = [[] * (n+2) for _ in range(n+2)]
    # Complete graph
    for i in range(n+2):
        for j in range(n+2):
            if i == j:
                continue

            # Euclidean distance
            # But square the entire thing because sweat proportional to square of time, and time is proportional to distance
            sweat = (spots[i][0] - spots[j][0])**2 + (spots[i][1] - spots[j][1])**2
            adj_list[i].append((j, sweat))
    
    D = [float('inf')] * (n+2)
    D[n] = 0

    pq = []
    heappush(pq, (0, n))

    prev = [-1] * (n+2)
    prev[n] = n
    
    # Generate path from dorm to class
    # Because sweat rate always resets when you reach ANY vertex, there is no need to store current sweat rate
        # Will always be 0 for each dequeue
    path = dijkstra(pq, D, prev, adj_list)

    [print(spot) for spot in path]


if __name__ == '__main__':
    main()
