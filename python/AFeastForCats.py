import math

# Dense Prims used because of densely connected graph
# Because we are able to store milk at each cat,
# We theoretically should not lose more milk than needed for travelling because we always should take the necessary amount only
# So its just a standard MST problem
def dense_prims(adjList, C, M):
    MST = []
    # Total cost of travelling to the cats
    cost = 0
    # Boolean visited list to check if cat has been visited
    visited = [False]*C
    # List to store the minimum distance to that cat
    A = [math.inf]*C

    s = 0
    A[s] = 0
    
    while len(MST) != C:
        cost += min(A)
        
        # Early exit if already exceed amount of milk available
        if cost + C > M:
            break

        minIndex = A.index(min(A))
        MST.append(minIndex)
        visited[minIndex] = True
        A[minIndex] = math.inf

        for neighbour in adjList[minIndex]:
            if not visited[neighbour[1]] and A[neighbour[1]] > neighbour[0]:
                A[neighbour[1]] = neighbour[0]

    return cost


def main():
    T = int(input())

    for i in range(T):
        M, C = map(int, input().split())
        adjList = [[]*C for _ in range(C)]

        for j in range(int(C*(C-1)/2)):
            catOne, catTwo, dist = map(int, input().split())
            adjList[catOne].append((dist, catTwo))
            adjList[catTwo].append((dist, catOne))

        # Remember that cats also consume 1mm of milk
        if dense_prims(adjList, C, M) + C <= M:
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    main()
