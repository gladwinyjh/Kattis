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
        


while (True):
    n = int(input())

    if (n == 0):
        break

    arr1 = []
    for i in range(n):
        arr1.append(int(input()))

    arr1Sort = sorted(arr1)
    
    arr2 = []
    for i in range(n):
        arr2.append(int(input()))
    
    arr2Sort = sorted(arr2)

    for i in range(n):
        print(arr2Sort[arr1Sort.index(arr1[i])])

    print("\n")
        
