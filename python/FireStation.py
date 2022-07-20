from sys import stdin
from heapq import heappush, heappop


def dijkstra(pq, D, adj_list, fire_stations):
    max_dist = -1
    while pq:
        dist, inter = heappop(pq)

        if D[inter] == dist:
            # Enter here = shortest distance to intersection
            # If not a fire_station, update the maximum distance 
            if inter not in fire_stations:
                max_dist = max(D[inter], max_dist)

            for other_inter, travel in adj_list[inter]:
                if D[other_inter] > travel + dist:
                    D[other_inter] = travel + dist
                    heappush(pq, (D[other_inter], other_inter))

    return max_dist


def main():
    t = int(stdin.readline())
    # t >= 1, so below blank line intake will always be valid
    _ = stdin.readline()

    while t:
        f, num_inter = map(int, stdin.readline().split())
        
        D = [float('inf')] * (num_inter+1)
        fire_stations = set()
        pq = []
        for i in range(f):
            fire_inter = int(stdin.readline())
            fire_stations.add(fire_inter)
            D[fire_inter] = 0
            heappush(pq, (0, fire_inter))
        
        adj_list = [[] * (num_inter+1) for _ in range(num_inter+1)]

        # Below deals with Runtime Error
        # Because end of test case can be shown in either an EOF or a blank line
        # Read until EOF
        for line in stdin:
            # If newline, the next line will be going to the next case, so process this case
            if line == '\n':
                break
            u, v, d = map(int, line.split())
            adj_list[u].append((v, d))
            adj_list[v].append((u, d))
        
        # Dijkstra from fire stations to all other intersections
        max_dist = dijkstra(pq, D, adj_list, fire_stations)
        
        max_inter = 1
        for i in range(1, num_inter+1):
            # Don't repeat dijkstra for existing fire stations because alr did before
            if i in fire_stations:
                continue
            
            pq = []
            # Assign intersection i with a fire station
            fire_stations.add(i)

            D = [float('inf')] * (num_inter+1)
            for station in fire_stations:
                D[station] = 0
                heappush(pq, (0, station))
            
            # Dijkstra from all fire stations to all other intersections with newly added fire station
            new_max_dist = dijkstra(pq, D, adj_list, fire_stations)
            
            # Update max distance if it can be reduced
            # Keep track of intersection number with max_inter
            if new_max_dist < max_dist:
                max_inter = i
                max_dist = new_max_dist
            
            # Remove added fire station
            fire_stations.remove(i)
        
        print(max_inter)
        print()

        t -= 1


if __name__ == '__main__':
    main()
