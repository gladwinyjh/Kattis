def time(arr):
    elapsed = 0

    if (len(arr) % 2 != 0):
        return "still running"

    for i in range(len(arr)):
        if (i%2 != 0): #watch is stopped at odd indices
            elapsed += (arr[i] - arr[i-1])

    
    return elapsed




n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

print(time(arr))

