import math

# def inTime(walkArr, rideArr, intArr):
#     elapsed = 0

#     for i in range(len(walkArr)-1):
#         elapsed += walkArr[i]

#         if (elapsed%intArr[i] != 0):
#             elapsed += (intArr[i] - elapsed%intArr[i])
        
        
#         elapsed += rideArr[i]
    
#     elapsed += walkArr[-1]

#     return elapsed
        



t = int(input())


for i in range(t):
    record = input()
    arr = []
    lower = 0

    for i in range(len(record.split())):
        arr.append(int(record.split()[i]))

    for i in range(len(arr)):
        if (arr[i] != 1 and arr[i] != 0):
            if (arr[i-1] * 2 < arr[i]):
                lower += (arr[i] - arr[i-1] * 2)
    
    print(lower)

            