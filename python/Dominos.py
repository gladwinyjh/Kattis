from sys import stdin


def topo_DFS(adj_list, n):
    visited = [0] * n
    topo_order = []
    stack = []

    for i in range(n):
        if not visited[i]:
            stack.append(i)
            # Stores the nodes that are currently reachable starting with i, in topological order
            curr = [i]
            while stack:
                s = stack.pop()
                visited[s] = 1

                for v in adj_list[s]:
                    if not visited[v]:
                        stack.append(v)
                        # Append neighbours
                        curr.append(v)
            
            # Pop each node in curr to topo_order
            # topo_order will be topological order in reverse
            while curr:
                topo_order.append(curr.pop())
    
    return topo_order


def kosaraju_DFS(adj_list, n, topo_order):
    visited = [0] * n
    knocks = 0
    stack = []
    
    # Do DFS on each unvisited node
    # If node is unvisited, it means that it belongs to a group of nodes that has no external incoming edges, or it is the start of a new group of nodes
    # So have need 1 additional knock
    for i in reversed(topo_order):
        if not visited[i]:
            knocks += 1
            stack.append(i)

            while stack:
                s = stack.pop()
                visited[s] = 1

                for v in adj_list[s]:
                    if not visited[v]:
                        stack.append(v)
    
    return knocks


def main():
    cases = int(stdin.readline())

    while cases:
        n, m = map(int, stdin.readline().split())
        
        adj_list = [[] * n for _ in range(n)]
        for i in range(m):
            x, y = map(int, stdin.readline().split())
            adj_list[x-1].append(y-1)
        
        # ITERATIVE DFS for both topological sort and kosaraju
        # Python does not like recursive DFS when input is very large (segmentation fault)
        topo_order = topo_DFS(adj_list, n)
        
        # Kosaraju using original adjacency list
        print(kosaraju_DFS(adj_list, n, topo_order))
       
        cases -= 1

if __name__ == '__main__':
    main()

    """
    DFS reachability test to find the number of CC will not work because the graph is directed
        - Sample Input 1:
                                    1
                                    3 2
                                    1 2
                                    2 3
            gives the answer 1 because you can push 1 to make all 3 fall

        but if you modify the input to be:
                                    1
                                    3 2
                                    3 2
                                    2 1 
            DFS reachability will give 3 as the answer, when the correct answer should be 1: push 3 to make all dominoes fall

    Can do reachability test from every domino and take the minimum number of knocks, but that might be too slow

    """
