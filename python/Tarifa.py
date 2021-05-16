def getData(x, arr):
    leftOver = x

    for usage in arr:
        leftOver = leftOver - usage
        leftOver += x

    return leftOver



x = int(input())
n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

print(getData(x, arr))
