import math

# def calArea(walkArr, rideArr, intArr):
#     elapsed = 0

#     for i in range(len(walkArr)-1):
#         elapsed += walkArr[i]

#         if (elapsed%intArr[i] != 0):
#             elapsed += (intArr[i] - elapsed%intArr[i])
        
        
#         elapsed += rideArr[i]
    
#     elapsed += walkArr[-1]

#     return elapsed
        



n = int(input())
valArr = []
timeArr = []
area = 0

for i in range(n):
    t, v = map(float,input().split())
    t = t/1000

    timeArr.append(t)
    valArr.append(v)

    if (i > 0):
        area += ((valArr[i-1] + v)/2) * (t - timeArr[i-1])

    
print(area)



            