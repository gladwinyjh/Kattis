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
        

x = 1

while (True):
    n = int(input())
    

    if (n == 0):
        break

    arr = []
    for i in range(n):
        arr.append(input())

    print("Set" ,x)
    i = 0

    while (i < n/2):
        print(arr.pop(i))
        i += 1

    i = -1
    while (arr != []):
        print(arr.pop(i))

    x += 1
        