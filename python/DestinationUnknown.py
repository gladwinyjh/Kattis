from sys import stdin, setrecursionlimit
from heapq import *
from collections import defaultdict


def dijkstra(pq, D, adj_list, path, dests, reached):
    while pq:
        dist, curr_inter, prev_inter, crossed = heappop(pq)
       
        if D[curr_inter] == dist:
            # g-h birectional
            # Check if current path is along g-h 
            # Check can be placed outside if condition instead of here
            if (prev_inter, curr_inter) == path or (curr_inter, prev_inter) == path:
                crossed = True
            
            # Only add to reachable destinations if currently on shortest path
            # Check if intersection is a destination, and that g-h have been crossed prior
            # Do not skip iteration when destination is reached because this destination may be enroute to other destinations
            if curr_inter in dests and crossed:
                reached.add(curr_inter)

            for other_inter, travel in adj_list[curr_inter]:
                # Bigger equal to distance + travel as there can be multiple shortest paths from source to a destination
                if D[other_inter] >= dist + travel:
                    D[other_inter] = dist + travel
                    # Keep track of current intersection and previous intersection to mark uniqueness of path
                    # and to check if g-h will be crossed
                    heappush(pq, (D[other_inter], other_inter, curr_inter, crossed))


def main():
    setrecursionlimit(5000)

    cases = int(stdin.readline())
    while cases:
        n, m, t = map(int, stdin.readline().split())
        s, g, h = map(int, stdin.readline().split())
        
        # Adjacency list
        adj_list = [[] * (n+1) for _ in range(n+1)]
        for i in range(m):
            a, b, d = map(int, stdin.readline().split())
            adj_list[a].append((b, d))
            adj_list[b].append((a, d))

        dests = set(int(stdin.readline()) for i in range(t))
        
        D = defaultdict(lambda: float('inf'))
        D[s] = 0

        pq = []
        # (total distance travelled, current intersection, previous intersection, crossed g-h?)
        heappush(pq, (0, s, -1, False))
        
        # Set to collect reachable destinations that passed through g-h
        reached = set()
        dijkstra(pq, D, adj_list, (g, h), dests, reached)
        
        # Destinations in increasing order: sort
        for x in sorted(reached):
            print(x, end = ' ')

        print()
        
        cases -= 1


if __name__ == '__main__':
    main()
