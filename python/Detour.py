from sys import stdin
from heapq import heappush, heappop


def dijkstra(start, adj_list, n):
    D = [float('inf')] * n
    D[start] = 0
    pq = []
    heappush(pq, (D[start], start))
    
    # List to store the point that should be visited if on shortest path from that point to (1)
    avoid = [-1 for _ in range(n)]
    while pq:
        dist, inter = heappop(pq)
        
        # No early exit as we want to find from all points

        if D[inter] == dist:
            for other_inter, travel in adj_list[inter]:
                if D[other_inter] > dist + travel:
                    D[other_inter] = dist + travel
                    # Update avoid list
                    # Going from destination to source, store inter in avoid[other_inter]
                    avoid[other_inter] = inter
                    heappush(pq, (D[other_inter], other_inter))
    
    return avoid


def get_route(avoid, adj_list, n):
    pq = []
    heappush(pq, 0)
    visited = set([0])
    prev = [-1 for _ in range(n)]
    prev[0] = 0
    
    while pq:
        inter = heappop(pq)
        
        if inter == 1:
            # Regurgitate out path from prev list
            path = []
            while prev[inter] != inter:
                path.append(inter)
                inter = prev[inter]
            
            path.append(0)
            # Path is in reverse
            return path[::-1]

        for other_inter, travel in adj_list[inter]:
            # Bus only visit a point once
            # Bus cannot take the route that is enroute to shortest path from current point
            if (other_inter not in visited and
                    other_inter != avoid[inter]):
                prev[other_inter] = inter
                visited.add(other_inter)
                heappush(pq, other_inter)


def main():
    n, m = map(int, stdin.readline().split())
    
    adj_list = [[] * n for _ in range(n)]
    for i in range(m):
        a, b, d = map(int, stdin.readline().split())
        adj_list[a].append((b, d))
        adj_list[b].append((a, d))
    
    avoid = dijkstra(1, adj_list, n)
    bus_routes = get_route(avoid, adj_list, n)

    if bus_routes:
        print(len(bus_routes), *bus_routes)
    else:
        # Bus routes will be None if (1) is unreachable from (0) while avoiding optimal routes
        print('impossible')


if __name__ == '__main__':
    main()
    # At any given point, bus will not take the path that next path that will lead it to the shortest path
        # Ex: At (2), shortest path from (2) to (1) goes to (5) next. Bus will not go to (5) if it is at (2)

    # Need to find what is the next optimal move from each point to the destination so that 
    # bus can avoid it
        # Dijkstra from (1) to all other points will give the shortest distance from each point to (1)
            # At each point, maintain the next node to visit for shortest path (to be avoided)

    # Dijkstra from (0), at each point, try all unvisited neighbours except the avoided ones
