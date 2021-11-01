arr = list(map(int, input().split()))
arr.sort()
order = input()
abc = []

for letter in order:
    if (letter == "A"):
        abc.append(arr[0])
    
    if (letter == "B"):
        abc.append(arr[1])
    
    if (letter == "C"):
        abc.append(arr[2])

for num in abc:
    print(str(num) + " ", end = "")     
