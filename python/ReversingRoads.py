from sys import stdin
from collections import defaultdict


def DFS(adj_list, u, visited, order):
    visited[u] = 1
    for v in adj_list[u]:
        if not visited[v]:
            DFS(adj_list, v, visited, order)
    
    order.append(u)


def toposort(adj_list, m):
    visited = defaultdict(lambda: 0)

    order = []
    for i in range(m):
        if not visited[i]:
            DFS(adj_list, i, visited, order)
        
    return order


def kosaraju(rev_adj_list, order):
    visited = defaultdict(lambda: 0)

    num_SCC = 0
    for i in reversed(order):
        SCC = []
        if not visited[i]:
            num_SCC += 1
            DFS(rev_adj_list, i, visited, SCC)
    
    return num_SCC


def main():
    case = 1
    while True:
        try:
            m, n = map(int, stdin.readline().split())

        except ValueError:
            return

        adj_list = defaultdict(set)
        roads = []
        for i in range(n):
            a, b = map(int, stdin.readline().split())
            roads.append((a, b))
            adj_list[a].add(b)
        
        # First check of toposort
        order = toposort(adj_list, m)

        rev_adj_list = defaultdict(set)
        for key, val in adj_list.items():
            for x in val:
                rev_adj_list[x].add(key)

        # First check of kosaraju 
        num_SCC = kosaraju(rev_adj_list, order)
        
        # If number of SCC == 1, all cities can reach each other
        if num_SCC == 1:
            print(f'Case {case}: valid')
        else:
            # Boolean flag if reversing a road can result in number of SCC == 1
            found = False
            for a, b in roads: # Reverse each road based on input order

                # Only need to modify adjacency lists
                adj_list[b].add(a)
                adj_list[a].remove(b)
                # Do the reverse for the rev_adj_list
                rev_adj_list[a].add(b)
                rev_adj_list[b].remove(a)

                order = toposort(adj_list, m)

                num_SCC = kosaraju(rev_adj_list, order)

                if num_SCC == 1: 
                    # Found a road that can be reversed
                    print(f'Case {case}: {a} {b}')
                    found = True
                    break
                
                # Restore the adjacency and reverse adjacency lists
                adj_list[b].remove(a)
                adj_list[a].add(b)
                rev_adj_list[a].remove(b)
                rev_adj_list[b].add(a)
            
            if not found:
                print(f'Case {case}: invalid')
        
        case += 1


if __name__ == '__main__':
    main()
