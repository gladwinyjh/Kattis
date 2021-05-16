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
        

c = int(input())

for i in range(c):
    sum = 0
    
    arr = list(map(int, input().split()))

    n = arr.pop(0)

    for score in arr:
        sum += score
    
    average = sum/len(arr)
    count = 0

    for score in arr:
        if (score > average):
            count += 1

    perc = (count/len(arr)) * 100

    print("%.3f" % perc + "%")
        