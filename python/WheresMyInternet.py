import sys

#Increase recursion limit due to large number of recursions to be performed when n is large
sys.setrecursionlimit(30000)

def dfs(u, visited, adjList):
    visited[u] = True

    for v in adjList[u]:
        if not visited[v]:
            dfs(v, visited, adjList)
    

n, m = map(int, input().split())

adjList = {}
visited = {}
for i in range(n):
    adjList[i] = []
    visited[i] = False

for i in range(m):
    a, b = map(int, input().split())

    adjList[a-1].append(b-1)
    adjList[b-1].append(a-1)

#DFS using house 1 as the starting vertex to get all houses connected to 1
dfs(0, visited, adjList)

#Sort dictionary so that output will be in increasing order
visited = dict(sorted(visited.items()))

connected = True
for i, x in visited.items():

    #These houses have not been visited, hence are not reachable from house 1
    if x == False:
        print(i+1)
        connected = False

if connected:
    print("Connected")
