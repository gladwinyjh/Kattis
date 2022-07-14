from sys import stdin, setrecursionlimit
from collections import defaultdict


def DFS(adj_list, store, visited, order):
    visited[store] = 1
    
    for neighbour in adj_list[store]:
        if not visited[neighbour]:
            DFS(adj_list, neighbour, visited, order)

    order.append(store)


def toposort(adj_list, stores):
    visited = defaultdict(lambda: 0)

    order = []
    for store in stores:
        if not visited[store]:
            DFS(adj_list, store, visited, order)

    return order


def kosaraju(rev_adj_list, topo_order):
    visited = defaultdict(lambda: 0)
    
    # To store all okay regions. Each region will be a list, so okay_list will be a list of lists
    okay_list = []
    # To store all avoid stores
    avoid_list = []
    for store in reversed(topo_order):
        # Store the stores in current SCC
        SCC = []
        if not visited[store]:
            DFS(rev_adj_list, store, visited, SCC)

        if len(SCC) == 1:
            # SCCs of size == 1 should be avoided
            avoid_list.append(SCC[0])
        elif len(SCC) >= 2:
            # SCCs of size >= 2 are okay
            # Sort within this SCC before appending to okay_list
            okay_list.append(sorted(SCC))
    
    # Return both lists sorted
    return sorted(okay_list), sorted(avoid_list)


def main():
    # Increase to not get runtime error on test case 
    setrecursionlimit(5000) 

    n = int(stdin.readline())
    
    adj_list = defaultdict(list)

    # We don't know how many stores are there, so assume those listed in input are all the stores
    # Use set to store all unique stores
    stores = set()
    for i in range(n):
        A, B = stdin.readline().split()
        adj_list[A].append(B)
        stores.add(A)
        stores.add(B)
    
    # DFS Toposort
    topo_order = toposort(adj_list, stores)
    
    # Reverse graph
    rev_adj_list = defaultdict(list)
    for key, val in adj_list.items():
        for x in val:
            rev_adj_list[x].append(key)
    
    # Kosaraju to return 2 lists
        # okay list: SCCs of size >= 2
        # avoid list: SCCs of size == 1
    okay, avoid = kosaraju(rev_adj_list, topo_order)
    
    # Print all okay regions
    for region in okay:
        print('okay', *region)
    
    # Avoid stores list can be empty, so print only if it exists
    if avoid:
        print('avoid', *avoid)


if __name__ == '__main__':
    main()
