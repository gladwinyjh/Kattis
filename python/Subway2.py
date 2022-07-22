from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop


# Get euclidean distance between 2 (x, y)
def euclidean_dist(x1, y1, x2, y2):
    # Distance of points are given in metres
    # Convert to km *0.001
    return (((x1 - x2)**2 + (y1 - y2)**2)**0.5) * 0.001


def dijkstra(pq, D, adj_list, school_x, school_y):
    while pq:
        time_taken, x, y = heappop(pq)

        if (x, y) == (school_x, school_y):
            # Reached school, * 60 to get time in minutes, then round off (NOT ROUND UP OR ROUND DOWN)
            return round(time_taken * 60)

        if D[(x, y)] == time_taken:
            # Walk to any subway stop
            for stop_x, stop_y in adj_list.keys():
                walk_to_subway = euclidean_dist(x, y, stop_x, stop_y) / 10
                if D[(stop_x, stop_y)] > walk_to_subway + time_taken:
                    D[(stop_x, stop_y)] = walk_to_subway + time_taken
                    heappush(pq, (D[(stop_x, stop_y)], stop_x, stop_y))
            
            # Walk to school
            walk_to_school = euclidean_dist(x, y, school_x, school_y) / 10
            if D[(school_x, school_y)] > walk_to_school + time_taken:
                D[(school_x, school_y)] = walk_to_school + time_taken
                heappush(pq, (D[(school_x, school_y)], school_x, school_y))

            # If at a subway stop, can take the subway along same line to adjacent stops
            for stop_x, stop_y in adj_list[(x, y)]: # Will be empty list if (x, y) is not a subway stop
                take_subway = euclidean_dist(x, y, stop_x, stop_y) / 40
                if D[(stop_x, stop_y)] > take_subway + time_taken:
                    D[(stop_x, stop_y)] = take_subway + time_taken
                    heappush(pq, (D[(stop_x, stop_y)], stop_x, stop_y))


def main():
    home_x, home_y, school_x, school_y = map(int, stdin.readline().split())
    
    adj_list = defaultdict(list)
    for line in stdin:
        # Till [:-2] to ignore -1 -1
        stops = list(map(int, line.split()))[:-2]

        # Each line has at least 2 stops per description
        # So dont need to check if line only contains 1 stop
        for i in range(0, len(stops)-2, 2):
            adj_list[(stops[i], stops[i+1])].append((stops[i+2], stops[i+3]))
            adj_list[(stops[i+2], stops[i+3])].append((stops[i], stops[i+1]))
    
    D = defaultdict(lambda: float('inf'))
    # Only the position matters since only concerned with distance and not how we end up in a certain position
        # Ex: If we have a threshold for how many subway trips to take, then may need to store that in D
    D[(home_x, home_y)] = 0
    pq = []
    heappush(pq, (0, home_x, home_y))
    
    # The vertices in our graph are the starting point, school, and all the subways stops
    # At each vertex, we can choose to either:
        # 1) Walk directly to school
        # 2) Walk directly to ANY subway point
        # 3) Take the subway if we are at any subway point
            # Only can take to adjacent stops
    print(dijkstra(pq, D, adj_list, school_x, school_y))


if __name__ == '__main__':
    main()
