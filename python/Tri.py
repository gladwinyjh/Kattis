import math

# def calArea(walkArr, rideArr, intArr):
#     elapsed = 0

#     for i in range(len(walkArr)-1):
#         elapsed += walkArr[i]

#         if (elapsed%intArr[i] != 0):
#             elapsed += (intArr[i] - elapsed%intArr[i])
        
        
#         elapsed += rideArr[i]
    
#     elapsed += walkArr[-1]

#     return elapsed
        

# arr = list(map(int, input().split()))
import sys

a, b, c = map(int, input().split())

if (a == b+c):
    print (str(a) + "=" + str(b) + "+" + str(c))
    sys.exit()

if (a == b-c):
    print (str(a) + "=" + str(b) + "-" + str(c))
    sys.exit()

if (a == b/c):
    print (str(a) + "=" + str(b) + "/" + str(c))
    sys.exit()

if (a == b*c):
    print (str(a) + "=" + str(b) + "*" + str(c))
    sys.exit()

if (c == a+b):
    print (str(a) + "+" + str(b) + "=" + str(c))
    sys.exit()

if (c == a-b):
    print (str(a) + "-" + str(b) + "=" + str(c))
    sys.exit()

if (c == a/b):
    print (str(a) + "/" + str(b) + "=" + str(c))
    sys.exit()  

if (c == a*b):
    print (str(a) + "*" + str(b) + "=" + str(c))
    sys.exit()  



# length = int (len(input) / 3) 

# word1 = ""
# word2 = ""
# word3 = ""

# for i in range(length):
#     word1 = word1 + input[i]

# for i in range(length):
#     word2 = word2 + input[i+length]

# if (word2 == word1):
#     print(word1)

# else:
#     for i in range(length):
#         word3 = word3 + input[i + 2*length]
    
#     print(word3)
