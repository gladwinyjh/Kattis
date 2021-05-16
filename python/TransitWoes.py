def inTime(walkArr, rideArr, intArr):
    elapsed = 0

    for i in range(len(walkArr)-1):
        elapsed += walkArr[i]

        if (elapsed%intArr[i] != 0):
            elapsed += (intArr[i] - elapsed%intArr[i])
        
        
        elapsed += rideArr[i]
    
    elapsed += walkArr[-1]

    return elapsed
        




s, t, n = map(int,input().split())

walkArr = []
walkTime = input()

for i in range(n+1):
    walkArr.append(int(walkTime.split()[i]))

rideArr = []
rideTime = input()

for i in range(n):
    rideArr.append(int(rideTime.split()[i]))

intArr = []
intTime = input()

for i in range(n):
    intArr.append(int(intTime.split()[i]))


totElapsed = inTime(walkArr, rideArr, intArr)

if (totElapsed <= t):
    print("yes")
else:
    print("no")