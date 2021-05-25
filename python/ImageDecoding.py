first = True

while (True):
    n = int(input())

    if (n == 0):
        break
    
    length = 0
    error = False

    if not first:
        print("\n", end='')

    for i in range(n):
        
        arr = input().split()
        symbol1 = arr.pop(0)

        arr = [int(n) for n in arr]

        if (i == 0):
            length = sum(arr)
            first = False
        elif (length != sum(arr)):
            error = True
        

        if (symbol1 == '#'):
            symbol2 = '.'
        else:
            symbol2 = '#'
        
        for i in range(len(arr)):
            if (i%2==0):
                print(symbol1 * int(arr[i]), end='')
            else:
                print(symbol2 * int(arr[i]), end='')
        
        print("\n", end='')
        
    if (error):
        print("Error decoding image")