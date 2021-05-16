def min(l,d,x):
    min = d
    a = 0
    
    for i in range(l,d+1):
        a = sum(int(digit) for digit in str(i))

        if (a == x and min > i):
            min = i
            return min

    return min

    

def max(l,d,x):
    max = 0
    a = 0
    
    for i in range(l,d+1):
        a = sum(int(digit) for digit in str(i))

        if (a == x and max < i):
            max = i

    return max



l = int(input())
d = int(input())
x = int(input())

print(min(l,d,x))
print(max(l,d,x))