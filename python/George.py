from heapq import *
from collections import defaultdict


def main():
    N, M = map(int, input().split())
    A, B, K, G = map(int, input().split())
    
    george_inter = list(map(int, input().split()))
    # Change to 0-based index
    george_inter = [x-1 for x in george_inter]
    
    # Create adjacency matrix. Easier to use than adjacency list for later
    adjMat = [[0] * N for _ in range(N)]
    for i in range(M):
        u, v, d = map(int, input().split())
        adjMat[u-1][v-1] = d
        adjMat[v-1][u-1] = d

    # We want to check if the street between 2 intersections will be occupied at a certain time
    # The occupied street will be occupied for less time over the period of its occupancy
    # Ex: At t = 0 of occupancy for a street that takes 5 min to traverse,
        # The remaining time is (5 -> 4 -> 3 -> 2 -> 1 -> 0). At remaining time == 0, Luka can enter the street
        # We want to capture the range of timings with respect to Luka's starting time
    occupied = defaultdict(lambda: (0,0)) 
    george_travel_time = 0 
    # Question did not say which intersection George starts from; assume he visits the third line intersections in order
    for i in range(1, len(george_inter)):
        traverse_time = adjMat[george_inter[i-1]][george_inter[i]] 
        occupied[(george_inter[i-1], george_inter[i])] = (george_travel_time - K, george_travel_time - K + traverse_time) 
        occupied[(george_inter[i], george_inter[i-1])] = (george_travel_time - K, george_travel_time - K + traverse_time) 
        # Update time when George reaches his next intersection
        george_travel_time += traverse_time
    
    # List to keep track of the minimal time elapsed from source
    # Initialise 0 at source, infinity for the rest of the intersections
    time_elapsed = [float('inf')] * N
    time_elapsed[A-1] = 0

    # Intitially Luka is at intersection A-1, time == 0
    pq = [(0, A-1)]
    heapify(pq)
    # Set to keep track of when all intersections are visited
    completed = set()
    
    # Modified Dijkstra's
    while pq:
        time, inter = heappop(pq)
        completed.add(inter)

        if inter == B-1:
            print(time)
            return
        
        # There will be multiple times for a given intersection enqueued
        # Only process those that give the minimal one based on the one record in time_elapsed (saves time)
        if time == time_elapsed[inter]:
            for neighbour, travel in enumerate(adjMat[inter]):
                if neighbour in completed or travel == 0:
                    # Neighbour already visited or no street exists between the 2 intersections
                    continue
                
                start, end = occupied[(inter, neighbour)]
                
                if end != 0 and start <= time < end and time_elapsed[neighbour] > end + travel:
                    # If Luka take this street currently, he has to wait for George to finish
                    # Luka have to wait till 'end' to start traversing, and will reach intersection 'neighbour' at end + travel
                    # Update and enqueue if this new time to reach 'neighbour' is the smallest thus far
                    time_elapsed[neighbour] = end + travel
                    heappush(pq, (time_elapsed[neighbour], neighbour))
                
                # If end == 0, it means that George has just finished the street and Luka can traverse through it
                # OR that George does not even traverse through the street (since default values for occupied are (0, 0))
                # So Luka proceed as per normal
                elif time_elapsed[neighbour] > time_elapsed[inter] + travel:
                    time_elapsed[neighbour] = time_elapsed[inter] + travel
                    heappush(pq, (time + travel, neighbour))
        


if __name__ == '__main__':
    main()
