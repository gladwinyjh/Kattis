import math

def calDist(x,y,arr):
    dist = 0
    s = 1
    
    while (s != 9):
        for i in range(3):
            for j in range(3):
                if (arr[i][j] == s+1):
                    s = s+1
                    dist += math.sqrt((j-y)**2 + (i-x) **2)
                    x = i
                    y = j
                    continue
    
    return dist
        

# arr = list(map(int, input().split()))

arr = []


for i in range(3):
    arr.append([int(x) for x in input().split()])

for i in range(3):
    for j in range(3):
        if (arr[i][j] == 1):
            x1 = i #source
            y1 = j



print(calDist(x1, y1, arr))
    

        
