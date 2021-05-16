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
        



n = int(input())
g = 9.81

for i in range(n):
    v, deg, x, h1, h2 = map(float,input().split())
    deg = math.radians(deg)

    lower = h1 + 1
    upper = h2 - 1

    t = x/(v * math.cos(deg))
    y = (v * t * math.sin(deg)) - (0.5 * g * pow(t,2))

    if (lower <= y <= upper):
        print("Safe")
    else:
        print("Not Safe")


# walkArr = []
# walkTime = input()

# for i in range(n+1):
#     walkArr.append(int(walkTime.split()[i]))

# rideArr = []
# rideTime = input()

# for i in range(n):
#     rideArr.append(int(rideTime.split()[i]))

# intArr = []
# intTime = input()

# for i in range(n):
#     intArr.append(int(intTime.split()[i]))


# totElapsed = inTime(walkArr, rideArr, intArr)

# if (totElapsed <= t):
#     print("yes")
# else:
#     print("no")