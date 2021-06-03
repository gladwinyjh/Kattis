from collections import deque

cases = int(input())

for i in range(cases):
    p = input()
    n = int(input())
    input_list = input().strip('[]')

    if not input_list: #Empty list
        input_list = []
    else:
        input_list = deque(map(int, input_list.split(',')))

    #Initially not reversed
    reversed = False

    error = False

    for j in range(len(p)):

        if p[j] == 'R':
            if not reversed:
                reversed = True
            else:
                reversed = False
        
        else:
            if p[j] == 'D' and len(input_list) == 0:
                print("error") #Empty list
                error = True
                break 
        
            else:
                if reversed:
                    input_list.pop()
                
                else:
                    input_list.popleft()

    
    if error:
        continue

    #Final list is reversed
    if reversed:
        final_list = []
        for j in range(len(input_list)):
            final_list.append(input_list.pop())
        
        print(str(final_list).replace(' ', '')) #Remove whitespace
    
    else:
        print(str(list(input_list)).replace(' ', '')) #Remove whitespace