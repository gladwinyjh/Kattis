import math
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