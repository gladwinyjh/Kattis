from math import sqrt

class Freckle:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def calDist(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


def process(node, visited, adjList, A, B, cost):
    visited[node] = True
    A[node][0] = float('inf')

    for v, w in enumerate(adjList[node]):
        if (not visited[v]) and (A[v][0] > w):
            A[v] = [w,v]
            B[v] = w
    


def prims(list, n):
    visited = [False] * n
    T = []
    costList = [float('inf')] * n
    cost = 0
    A = [[float('inf'), i] for i in range(n)]
    A[0][0] = 0
    costList[0] = 0
    T.append(0)
    process(0, visited, list, A, costList, cost) #Push source to PQ
    
    for i in range(1,n):
        w, v = min(A, key=lambda x: x[0])
        T.append(v)
        process(v, visited, list, A, costList, cost)

    for i in range(n):
        cost += costList[i]
    
    return cost


t = int(input())

for i in range(t):

    input()

    n = int(input())

    coordinates = {}

    for i in range(n):
        x, y = map(float, input().split())
        coordinates[i] = Freckle(x,y)

    adjList = [[0.0]*n for i in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            adjList[i][j] = coordinates[i].calDist(coordinates[j])
            adjList[j][i] = coordinates[i].calDist(coordinates[j])

    mstCost = prims(adjList, n)
    print("%.2f" % mstCost)
