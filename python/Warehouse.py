import math


t = int(input())

for i in range(t):
    n = int(input())

    d = {}

    for i in range(n):
        item, num = input().split()
        
        if item not in d:
            d[item] = int(num)
        else:
            d[item] += int(num)
    
    dSorted = []
    dSorted = sorted(d, key=lambda x: (-d[x], x))
    
    print(len(dSorted))
    for item in dSorted:
        print(item, d.get(item))