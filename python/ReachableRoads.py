def dfs(endPoint, adjList, visited):
    # Set current endpoint to visited
    visited[endPoint] = True
    # Get all neighbours and do DFS on them if not visited
    # Return to main() when all endpoints in this component is visited
    for neighbour in adjList[endPoint]:
        if not visited[neighbour]:
            dfs(neighbour, adjList, visited)
            

def main():
    n = int(input())

    for i in range(n):
        m = int(input())
        r = int(input())
        # Create Adjacency List
        adjList = [[]*m for _ in range(m)]

        # Add neighbours to adjacency list
        for j in range(r):
            endOne, endTwo = map(int, input().split())
            adjList[endOne].append(endTwo)
            adjList[endTwo].append(endOne)

        # Number of connected endpoints
        numComponents = 0
        # Visited List of endpoints. All are not visited initially
        visited = [False] * m
        for j in range(m):
            # Endpoint is in new component
            if not visited[j]:
                numComponents += 1
                # Do Depth first search to connect all endpoints in this component
                dfs(j, adjList, visited)
        
        # Since roads connect components
        # To connect all components, need minimally number of components - 1 roads
        print(numComponents - 1)


if __name__ == '__main__':
    main()