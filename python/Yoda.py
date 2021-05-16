import math

def Check(lst):
    
    if (max(lst) == ""):
        return "YODA"
        
    else:
        if (max(lst) == "0"):
            return "0"

        str = ""
        return str.join(lst)


a = list(input())
b = list(input())

length = min(len(a), len(b))

for i in range(1,length+1):

    if (int(a[-i]) > int(b[-i])):
        b[-i] = ""
    
    elif (int(a[-i]) < int(b[-i])):
        a[-i] = ""


a = Check(a)
b = Check(b)

print(a)
print(b)        