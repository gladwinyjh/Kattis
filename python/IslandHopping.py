import math


def cal_dist(islandOne, islandTwo, graph):
    dX = graph[islandOne][0] - graph[islandTwo][0]
    dY = graph[islandOne][1] - graph[islandTwo][1]

    # Euclidean distance
    return math.sqrt(dX**2 + dY**2)


def dense_prims(adjList, N):
    # List to store MST
    MST = []
    # To store min cost of going to island index
    costs = [0] * N
    # Intialise list that store smallest distance among all island to an index
    A = [math.inf] * N
    # Boolean visited list
    visited = [False] * N

    # Add source s to tree
    # MST.append(0)
    # Initialise A[s] = 0
    A[0] = 0

    # While not all islands are in MST
    while len(MST) != N:
        # Get index of minimum distance
        minIndex = A.index(min(A))
        # Add island index to MST
        MST.append(minIndex)
        # Set island to visited
        visited[minIndex] = True
        A[minIndex] = math.inf

        for neighbour in adjList[minIndex]:
            # Neighbour island not yet visited AND 
            # Distance from neighbour island to current island is smaller than that stored in A
            if not visited[neighbour[0]] and A[neighbour[0]] > neighbour[1]:
                # Replace smallest distance
                A[neighbour[0]] = neighbour[1]
                costs[neighbour[0]] = neighbour[1]

    # Return sum of smallest lengths to each island
    return sum(costs)


def main():
    n = int(input())

    for i in range(n):
        m = int(input())
        adjList = [[] * m for _ in range(m)]
        graph = {}
        
        # Store coordinates in graph
        # Key = index of island. Value = x and y coordinates of island
        for j in range(m):
            x, y = map(float, input().split())
            graph[j] = (x, y)

        for j in range(m):
            for k in range(j+1, m):
                # Get Euclidean distance
                distance = cal_dist(j, k, graph)
                # Add to adjacency list
                adjList[k].append((j, distance))
                adjList[j].append((k, distance))
                
        # Do Dense variant of Prim's Algorithm due to dense graph
        # For Python, Kruskal's may not be fast enough (TLE)
        print(dense_prims(adjList, m))
        

if __name__ == '__main__':
    main()