import math


def dense_prims(adjList, n):
    MST = []
    visited = [False] * n
    A = [math.inf] * n
    # List used to store village indices that share the cheapest edge to each index
    MST_edges = [-1] * n
    
    # Use village 0 as the source
    A[0] = 0

    while len(MST) < n:
        minIndex = A.index(min(A))
        visited[minIndex] = True
        MST.append(minIndex)
        A[minIndex] = math.inf

        for neighbour in adjList[minIndex]:
            if not visited[neighbour[1]] and A[neighbour[1]] > neighbour[0]:
                A[neighbour[1]] = neighbour[0]
                # Update cheapest edge with minIndex. +1 because villages start from 1
                MST_edges[neighbour[1]] = minIndex+1
    
    # Print out edges
    # Ignore first index as it is the source
    # Did not check if there are edges to source so MST_edges[0] == -1
    # Does not matter as any cheapest edge with source will still be reflected by the respective indices
    for i in range(1, len(MST_edges)):
        print(i+1, MST_edges[i])
            

def main():
    n = int(input())
    
    # Create adjacency list from the adjacency matrix input
    adjList = [[]*n for _ in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(len(line)):
            # Don't include distance from village to itself
            if i != j:
                adjList[i].append((line[j], j)) 
    
    # Densely connected graph, do dense prims
    dense_prims(adjList, n) 


if __name__ == '__main__':
    main()
