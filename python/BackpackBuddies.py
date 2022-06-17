from sys import stdin
from heapq import *


def dijkstra(pq, dist, adj_list, player):
    while pq:
        hours, cabin, time_remaining = heappop(pq)
        
        # Arrived at cabin n-1, returned the shortest number of hours to arrived here
        if cabin == len(dist) - 1:
            return hours

        if hours == dist[cabin]:
            for neighbour, travel_time in adj_list[cabin]:
                # Player 0 is Dr. Knight
                if player == 0:
                    # Dr. Knight can travel and stop between 2 cabins
                    if time_remaining < travel_time:
                        # Need to stop between cabins to rest for 12 hours
                        if dist[neighbour] > hours + travel_time + 12:
                            dist[neighbour] = hours + travel_time + 12
                            # The excess time needed to complete trail once Dr. Knight wakes up
                            # is travel_time - time_remaining. So new remaining time is 12 - that
                            heappush(pq, (dist[neighbour], neighbour, 12 - (travel_time - time_remaining)))

                    # Else: time_remaining >= travel_time
                    # Travel as per normal, update and push to PQ if can reach neighbour faster
                    elif dist[neighbour] > hours + travel_time:
                        dist[neighbour] = hours + travel_time
                        heappush(pq, (dist[neighbour], neighbour, time_remaining - travel_time))
                
                # Player 1 is Mr. Day
                elif player == 1:
                    # Mr. Day can only travel to other cabin if the time_remaining is at least the travel_time
                    # If not he must rest at the current cabin
                    if time_remaining < travel_time:
                        # Stay at current cabin for time_remaining + wait 12 hours till next day + travel_time
                        if dist[neighbour] > hours + time_remaining + 12 + travel_time:
                            dist[neighbour] = hours + time_remaining + 12 + travel_time
                            # Start on new day, so new time_remaining = 12 - travel_time
                            heappush(pq, (dist[neighbour], neighbour, 12 - travel_time))
                    
                    # Same as above, travel as per normal
                    # Update and push to PQ if can reach neighbour faster
                    elif dist[neighbour] > hours + travel_time:
                        dist[neighbour] = hours + travel_time
                        heappush(pq, (dist[neighbour], neighbour, time_remaining - travel_time))


def main():
    number_cabins, number_trails = map(int, stdin.readline().split())

    adj_list = [[] * number_cabins for _ in range(number_cabins)]
    for i in range(number_trails):
        u, v, d = map(int, stdin.readline().split())
        # 0 <= d <= 12 so player will always be able to travel from one cabin to another
        # Player will not get stuck at a cabin if there is a trail for it

        # There can be multiple trails between the same 2 cabins
        # Can prob check if current trail is shorter than an existing trail between same 2 cabins and replace it
        # since ideally will take the shorter trail. 
        # But it does not really matter for Dijkstra, since it will filter out only the shortest to a cabin
        adj_list[u].append((v,d))
        adj_list[v].append((u,d))
    
    arrival_times = []
    for i in range(2):
        dist = [float('inf')] * number_cabins
        dist[0] = 0

        pq = []
        # Push source to PQ
        # (shortest distance to cabin, cabin number, hours remaining to travel)
        heappush(pq, (0, 0, 12))
        
        # Do Dijkstras each for Dr. Knight and Mr. Day
        # Dr. Knight is chosen as i == 0, Mr. Day as i == 1
        # Record down arrival times at cabin n-1 in arrival_times list
        arrival_times.append(dijkstra(pq, dist, adj_list, i))
    
    # Print difference in arrival times
    print(arrival_times[1] - arrival_times[0])


if __name__ == '__main__':
    main()
