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


input = input()
c1 = 0
c2 = 0

for letter in input:
    if (letter == "B"):
        c1 += 1
    if (letter == "W"):
        c2 += 1

if (c1 == c2):
    print(1)
else:
    print(0)

# arr.sort()

# order = input()

# abc = []

# for letter in order:
#     if (letter == "A"):
#         abc.append(arr[0])
    
#     if (letter == "B"):
#         abc.append(arr[1])
    
#     if (letter == "C"):
#         abc.append(arr[2])

# for num in abc:
#     print(str(num) + " ", end = "")
        