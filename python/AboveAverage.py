import math


c = int(input())

for i in range(c):
    sum = 0
    arr = list(map(int, input().split()))
    n = arr.pop(0)

    for score in arr:
        sum += score
    
    average = sum/len(arr)
    count = 0

    for score in arr:
        if (score > average):
            count += 1

    perc = (count/len(arr)) * 100

    print("%.3f" % perc + "%")        