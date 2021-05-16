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
from itertools import permutations

input = input()
arr = list([int(d) for d in input])

smallest = 1000000

perm = permutations(arr)
next = 0

for i in list(perm):
    curr = ""

    for j in i:
        curr = curr + str(j)

    
    if (int(curr) - int(input) < smallest and int(curr) > int(input)):
        smallest = int(curr) - int(input)
        next = int(curr)
    

print(next)

