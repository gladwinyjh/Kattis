from sys import stdin, setrecursionlimit
from collections import defaultdict


def DFS(filename, adj_list, visited, order):
    visited[filename] = 1
    
    for successor in adj_list[filename]:
        if not visited[successor]:
            DFS(successor, adj_list, visited, order)

    order.append(filename)


def main():
    # Gonna do DFS that require increasing the limit
    # If not will get runtime error
    setrecursionlimit(100000)

    n = int(stdin.readline())
    
    visited = defaultdict(lambda: 0)
    adj_list = defaultdict(list)
    for i in range(n):
        rule = list(stdin.readline().split())
        filename = rule[0][:-1]
        if len(rule) > 1:
            [adj_list[x].append(filename) for x in rule[1:]]
     
    changed = stdin.readline().rstrip()

    # To store ordering in reverse
    order = [] 

    # DFS Topo sort, but from the changed file only
    DFS(changed, adj_list, visited, order)
    
    # Order will be in reversed
    for files in reversed(order):
        print(files)
    

if __name__ == '__main__':
    main()
