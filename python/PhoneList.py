import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    phoneList = []
    for j in range(n):
        phoneList.append(sys.stdin.readline().strip('\n'))

    sortedList = sorted(phoneList)
    
    consistent = True
    for j in range(0, n-1):
        if not consistent:
            break

        else:
            if sortedList[j+1].startswith(sortedList[j]):
                consistent = False
                break

    if consistent:
        print("YES")
    else:
        print("NO")