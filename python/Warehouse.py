import math

# def compare(item1, item2):
#     if (get(item1) > get(item2)):
#         return 1
#     elif (get(item2) > get(item1)):
#         return -1
    
#     elif (get(item1) == get(item2)):
#         return (item1 > item2)

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