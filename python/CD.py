import sys
#input() is too slow for test case 2, use stdin.readline() instead

while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break
    
    
    jackSet = set()
    jillSet = set()

    for i in range(n):
        num = int(sys.stdin.readline()) 

        count = jackSet.add(num)


    for i in range(m):
        num = int(sys.stdin.readline())

        count = jillSet.add(num)

    #Find intersection
    print(len(jackSet&jillSet))
