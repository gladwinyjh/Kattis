import math

def calDist(i, j, list):

    x1, y1 = list.get(i)[0], list.get(i)[1]
    x2, y2 = list.get(j)[0], list.get(j)[1]

    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskals(list, s, p):
    mst = []
    parent = []
    rank = []

    for node in range(p):
        parent.append(node)
        rank.append(0)

    cc = p

    for i in range(len(list)):
        u, v, w = list[i]
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            mst.append([u,v,w])
            union(parent, rank, x, y)
            cc -= 1
        
        #Each cc set must have at least one with a satellite channel, so it stops at s because at s, each cc set MUST have one satellite channel
        if cc == s: 
            break

    return mst


n = int(input())

for i in range(n):
    s, p = map(int, input().split())

    coordinates = {}

    for i in range(p):
        x, y = map(int, input().split())
        coordinates[i] = [x,y]


    edgeList = []
    for i in range(p):
        for j in range(i+1,p):
            edgeList.append([i, j, calDist(i, j, coordinates)])
    
    sortedList = sorted(edgeList, key= lambda item: item[2])
    
    if p == 2:
        print("%.2f" % sortedList[0][2])
        continue

    mst = kruskals(sortedList, s, p)
    print("%.2f" %mst[-1][2])