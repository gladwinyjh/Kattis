from sys import stdin
from collections import deque


def main():
    N, H, L = map(int, stdin.readline().split())
    
    horror_list = set(map(int, stdin.readline().split()))

    adjList = [[] * N for _ in range(N)] 
    # Populate adjacency list. No weights needed.
    for i in range(L):
        u, v = map(int, stdin.readline().split())
        adjList[u].append(v)
        adjList[v].append(u)
    
    q = deque()
    # HI stores the minimum 'horror score' Q for each movie 
    HI = [float('inf')] * N
    for id in horror_list:
        # Q for movies in horror list is 0
        HI[id] = 0
        q.append(id)
    
    # Multi-source BFS 
    # Only way movies not on the horror list can get their Q down is by being similar to other movies
    while q:
        id = q.popleft()

        for similar in adjList[id]:
            # Movies in the horror list can only have a HI of 0, so dont update
            if similar in horror_list:
                continue
            
            # Similar movie has a Q lower(worst) than the previous worst Q for this movie
            if HI[id] < HI[similar]:
                # Q + 1
                HI[similar] = HI[id] + 1
                q.append(similar)
    
    # index returns the first occurrence of the maximum
    print(HI.index(max(HI)))


if __name__ == '__main__':
    main()
