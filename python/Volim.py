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
        

# arr = list(map(int, input().split()))
import sys

k = int(input())
n = int(input())

time = 210
flag = True

for i in range(n):
    tokens = input().split()
    t = int(tokens[0])
    ans = tokens[1]

    time -= t

    if (time <= 0 and flag): #explode
        print(k)
        flag = False

    elif (ans != "T"):
        continue
    
    k += 1
    if (k == 9):
        k = 1
