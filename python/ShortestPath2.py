from heapq import *
from sys import stdin


def dijkstra(D, pq, adjList):
    while pq:
        time, node = heappop(pq)

        if time == D[node]:
            for v, t_0, P, d in adjList[node]:
                if time <= t_0 and D[v] > t_0 + d:
                    # time <= t_0 can occur for P == 0 and P > 0
                    # For P == 0, it will only occur once since the path only opens once
                    # So for subsequent checks, it will not enter the elif statement

                    # There is a shorter path to v, update the path, and push (D[v], v) to pq
                        D[v] = t_0 + d
                        heappush(pq, (D[v], v))
                elif P > 0:
                    # (time - t_0) % P gives the time elapsed since the path was last open
                    # P - this to get the additional waiting time for the next opening
                    add_time = P - (time - t_0) % P
                    # This additional time can be P if time == t_0
                    # If so, there is no there is no additional waiting time needed, so reset it to 0
                    if add_time == P:
                        add_time = 0
                    
                    # Time in which you can cross edge = current time + additional waiting time
                    next_opening = time + add_time 
                    if D[v] > next_opening + d:
                        # Same as above, update if eligible
                        D[v] = next_opening + d
                        heappush(pq, (D[v], v))
                

def main():
    while True:
        n, m, q, s = map(int, stdin.readline().split())

        if n == 0:
            # EOF since n cannot be < 1
            return

        adjList = [[]*n for _ in range(n)]
        # Populate adjacency list, store P and d as well
        for i in range(m):
            u, v, t_0, P, d = map(int, stdin.readline().split())
            # Note that edges are uni-directional
            adjList[u].append((v, t_0, P, d))

        D = [float('inf')] * n
        D[s] = 0

        pq = []
        heappush(pq, (D[s], s))
       
        # Do a modified Dijkstra
        dijkstra(D, pq, adjList)
        
        for i in range(q):
                dest = int(stdin.readline())

                if D[dest] == float('inf'):
                    # Node has not been updated = node cannot be travelled to
                    print('Impossible')
                else:
                    print(D[dest])

        print()


if __name__ == '__main__':
    main()
