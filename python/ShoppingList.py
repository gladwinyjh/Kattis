n, m = map(int, input().split())
setList = []

for i in range(n):
    setList.append(set(input().split()))

intersectionSet = set.intersection(*setList)
print(len(intersectionSet))

for item in sorted(intersectionSet):
    print(item)