from sys import stdin
from heapq import *


def main():
    N, S, T = map(int, stdin.readline().split())
    adjMat = []
    for i in range(N):
        adjMat.append(list(map(int, stdin.readline().split())))
    
    
    D = [float('inf')] * N
    D[S] = 0

    pq = []
    heappush(pq, (D[S], S))
    
    # Positive weights, just do Dijkstra's
    # Assume that it is guaranteed that Charles can get to the meeting spot
    while pq:
        time, inter = heappop(pq)

        if inter == T:
            print(time)
            break
            
        if time == D[inter]:
            for neighbour, weight in enumerate(adjMat[inter]):
                if neighbour == inter:
                    continue
                
                if D[neighbour] > time + weight:
                    D[neighbour] = time + weight
                    heappush(pq, (D[neighbour], neighbour))


if __name__ == '__main__':
    main()
