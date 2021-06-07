class Land:
    def __init__(self, r, c):
        self.r = r
        self.c = c


def dfs(land, visited, arr, r, c, dr, dc):

    #Visited adjacent cells if not visited and within map and not water
    #If returns, the entire block is one island
    #Optimistic flood fill: clouds is land
    for row in dr:
        if 0 <= land.r+row < r and arr[land.r+row][land.c] != 'W' and visited[land.r+row][land.c] == 0 and row != 0:
            visited[land.r+row][land.c] = 1
            dfs(Land(land.r+row, land.c), visited, arr, r, c, dr, dc)

    for col in dc:
        if 0 <= land.c+col < c and arr[land.r][land.c+col] != 'W' and visited[land.r][land.c+col] == 0 and col != 0:
            visited[land.r][land.c+col] = 1
            dfs(Land(land.r, land.c+col), visited, arr, r, c, dr, dc)



r, c = map(int, input().split())

arr = [[]* c for _ in range(r)] 
visited = [[0]* c for _ in range(r)] 
landList = []

for i in range(r):
    arr[i] = list(input())

    for j in range(c):
        if arr[i][j] == 'L':
            landList.append(Land(i,j))
        

count = 0
dr = [x for x in range(-1, 2)]
dc = [x for x in range(-1, 2)]

for land in landList:
    if (visited[land.r][land.c] == 0):
        visited[land.r][land.c] = 1
        dfs(land, visited, arr, r, c, dr, dc)
        count += 1

print(count)