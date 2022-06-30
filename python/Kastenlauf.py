from sys import stdin
from collections import defaultdict
from heapq import *
import math


def manhattan_dist(c1, c2):
    # Manhattan distance
    dist = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
    # Divide by 50 because 1 beer per 50m, round up because cannot have partial beer bottles
    return math.ceil(dist/50)


def dijkstra_minimax(pq, D, adj_list, dest):
    while pq:
        max_beers, pos = heappop(pq)
        
        # Reached destination, and max beer edge weight <= 20
        if pos == dest and max_beers <= 20:
            return True
        
        if max_beers == D[pos]:
            for travel, neighbour in adj_list[pos]:
                # Update new max edge weight
                new_max_beers = max(max_beers, travel)
                if D[neighbour] > new_max_beers:
                    # Found a lower max edge weight
                    # Update
                    D[neighbour] = new_max_beers
                    heappush(pq, (D[neighbour], neighbour))
    
    # Either unable to reach dest from start, or max edge weight from start to dest > 20
    return False


def main():
    t = int(stdin.readline())

    while t:
        num_stores = int(stdin.readline())
        coor = []
        for i in range(num_stores + 2):
            x, y = map(int, stdin.readline().split())
            coor.append((x, y))
        
        start = coor[0]
        dest = coor[-1]

        adj_list = defaultdict(set) 
        for i in range(len(coor)):
            for j in range(i+1, len(coor)):
                # Distance metric to be used per description: Manhattan
                # Divided by 50 and take round up to get the distance in beers
                beer_dist = manhattan_dist(coor[i], coor[j])
                # Positions are reachable to one another if the beer distance is <= 20
                if beer_dist <= 20:
                    adj_list[coor[i]].add((beer_dist, coor[j]))
                    adj_list[coor[j]].add((beer_dist, coor[i]))
        
        # Distance dictionary to find shortest beer distance from start to dest
        D = defaultdict(lambda: float('inf'))
        D[start] = 0
        
        pq = []
        heappush(pq, (0, start))

        # Dijkstra minimax problem
        # Find the path from start to dest that minimises the maximum beer edge weight along the path
        # This maximum beer edge weight has to be <= 20
        if dijkstra_minimax(pq, D, adj_list, dest):
            print('happy')
        else:
            print('sad')
        
        t -= 1


if __name__ == '__main__':
    main()
