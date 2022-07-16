from sys import stdin
from heapq import *
from collections import defaultdict, deque


def dijkstra(pq, D, parent, adj_list, adj_dict, peak):
    while pq:
        cost, point = heappop(pq)
        
        if point == peak:
            # No point traversing after peak
            continue

        if D[point] == cost:
            for neighbour, travel_cost in adj_list[point]:
                # Only want to visit the shortest path between 2 direct points
                # Since there can be multiple paths between 2 direct points given in the input
                if adj_dict[(point, neighbour)] == travel_cost:
                    if D[neighbour] > cost + travel_cost:
                        D[neighbour] = cost + travel_cost
                        # There is a new shorter way to reach neighbour via point
                        # Reinitialise parent[neighbour] with just point in its list
                        parent[neighbour] = [point]
                        heappush(pq, (D[neighbour], neighbour))

                    # Another shortest way to reach neighbour via same point or another point
                    elif D[neighbour] == cost + travel_cost:
                        parent[neighbour].append(point)
    
    # BFS from peak as source to entrance as destination
    q = deque([peak])
    total_cost = 0
    # Visited set so that we do not visit same point twice
    # If visit point more than once, still add total cost, but do not visit it
    vis = set()
    while q:
        point = q.popleft()
        
        if point in vis:
            continue

        vis.add(point)

        for child in parent[point]:
            # Add to total cost at each point
            total_cost += adj_dict[(child, point)]
            q.append(child)
    
    # Birectional, x 2
    return 2 * total_cost


def main():
    P, T = map(int, stdin.readline().split())
    
    # Standard adjacency list birectional
    adj_list = [[] * P for _ in range(P)]
    # Dictionary to maintain the shortest distance between any 2 direct edges
    adj_dict = defaultdict(lambda: float('inf'))
    for i in range(T):
        p1, p2, l = map(int, stdin.readline().split())
        
        # p1 and p2 can be the same
        # If same, shortest distance is to just not move
        if p1 == p2:
            continue

        adj_list[p1].append((p2, l))
        adj_list[p2].append((p1, l))

        # Update shortest distance between p1 and p2
        adj_dict[(p1, p2)] = min(adj_dict[(p1, p2)], l)
        adj_dict[(p2, p1)] = min(adj_dict[(p2, p1)], l)
    
    D = [float('inf')] * P
    D[0] = 0

    pq = []
    heappush(pq, (D[0], 0))
    
    # Parent dictionary to store predcessors for points
    # Use list as there can be multiple shortest paths
    parent = defaultdict(list)

    print(dijkstra(pq, D, parent, adj_list, adj_dict, P-1))


if __name__ == '__main__':
    main()
