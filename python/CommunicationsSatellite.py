import math


def cal_dist(satelliteOne, satelliteTwo, graph):
    dX = graph[satelliteOne][0] - graph[satelliteTwo][0]
    dY = graph[satelliteOne][1] - graph[satelliteTwo][1]

    # Euclidean distance - radii of both satellites
    return math.sqrt(dX**2 + dY**2) - graph[satelliteOne][2] - graph[satelliteTwo][2]


def dense_prims(adjList, N):
    # List to store MST
    MST = []
    # To store min cost of going to satellite index
    costs = [0] * N
    # Intialise list that store smallest distance among all satellites to an index
    A = [math.inf] * N
    # Boolean visited list
    visited = [False] * N

    # Add source s to tree
    # MST.append(0)
    # Initialise A[s] = 0
    A[0] = 0

    # While not all satellites are in MST
    while len(MST) != N:
        # Get index of minimum distance
        minIndex = A.index(min(A))
        # Add satellite index to MST
        MST.append(minIndex)
        # Set satellite to visited
        visited[minIndex] = True
        A[minIndex] = math.inf

        for neighbour in adjList[minIndex]:
            # Neighbour satellite not yet visited AND 
            # Distance from neighbour satellite to current satellite is smaller than that stored in A
            if not visited[neighbour[0]] and A[neighbour[0]] > neighbour[1]:
                # Replace smallest distance
                A[neighbour[0]] = neighbour[1]
                costs[neighbour[0]] = neighbour[1]

    # Return sum of smallest lengths to each satellite
    return sum(costs)


def main():
    N = int(input())
    graph = {}
    adjList = [[] * N for _ in range(N)]

    for i in range(N):
        X, Y, R = map(int, input().split())
        # Add satellite X, Y, R to graph
        graph[i] = (X, Y, R)
    
    for i in range(N):
        for j in range(i+1, N):
            # Get Euclidean distance
            distance = cal_dist(i, j, graph)
            # Add to adjacency list
            adjList[i].append((j, distance))
            adjList[j].append((i, distance))

    # Do Dense variant of Prim's Algorithm due to dense graph
    # For Python, Kruskal's may not be fast enough (TLE)
    print(dense_prims(adjList, N))


if __name__ == '__main__':
    main()