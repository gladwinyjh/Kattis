from sys import stdin
from collections import deque


def kahn(adj_list, indeg, stages, curr_q=False):
    q = [deque(), deque()]
    
    # q[0] stores the stages beginning in lab 1
    # q[1] stores the stages beginning in lab 2
    # Intially queues are only filled with stages with indeg == 0
    # Queues will only store stages that are ready to be added to the topo order
    # Want to minimise switches, so deque only empty for each queue

    for idx, val in enumerate(indeg):
        if val == 0:
            if stages[idx] == 1:
                q[0].append(idx)
            else:
                q[1].append(idx)    

    switches = 0
    while q[0] or q[1]:
        while q[curr_q]:
            stage = q[curr_q].popleft()

            for next_stage in adj_list[stage]:
                indeg[next_stage] -= 1
                
                if indeg[next_stage] == 0:
                    # Add to the correct queue depending on lab
                    q[stages[next_stage]-1].append(next_stage)
        
        # Switch queues 
        curr_q = not curr_q
        switches += 1 
    
    # Will count 1 extra because switches += 1 is put at the end
    return switches-1


def main():
    T = int(stdin.readline())
    
    while T:
        n, m = map(int, stdin.readline().split())
        stages = list(map(int, stdin.readline().split()))
        
        adj_list = [[] for _ in range(n)]
        indeg = [0] * n 
        for i in range(m):
            i, j = map(int, stdin.readline().split())
            adj_list[i-1].append(j-1)
            indeg[j-1] += 1
        
        # Want to minimise switches
        # This means that once we start with a certain lab, we want to keep it that way until there are no more stages for that lab

        # Do Kahn twice
        # Find the minimum of (starting from lab 1 vs starting from lab 2)
        # Use copy of indeg because indeg will be altered
        print(min(kahn(adj_list, indeg[:], stages, False), kahn(adj_list, indeg[:], stages, True)))        

        T -= 1


if __name__ == '__main__':
    main()
