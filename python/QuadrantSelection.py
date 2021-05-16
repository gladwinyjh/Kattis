def num(x,y):

    if (x > 0 and y > 0):
        return 1
    elif (x > 0 and y < 0):
        return 4
    elif (x < 0 and y < 0):
        return 3
    else:
        return 2


x = int(input())
y = int(input())

print(num(x,y))