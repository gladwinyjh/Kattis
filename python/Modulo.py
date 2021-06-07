t = int(input())

for i in range(t):
    n = int(input())

    map = {}
    
    for j in range(n):
        s = int(input())

        if s not in map:
            map[s] = 1
        else:
            map[s] += 1
    
    print(len(map))

