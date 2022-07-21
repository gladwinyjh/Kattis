from sys import stdin
from collections import deque


def BFS(i, n, min_trees, adj_list):
    q = deque([(i, -1)])
    # visited store the number of trees in a path when encountering tree at this index including this tree
    visited = [float('inf')] * n
    visited[i] = 1

    while q:
        tree, prev_tree = q.popleft()

        for neighbour in adj_list[tree]:
            # Cycle, or first time visiting neighbour tree (since visited initialised at inf)
            # Found another route to reach neighbour with less number of trees, like a shortcut
            # 'Ditch' the previous path and use this path by updating visited[neighbour]
            # and enqueueing
            if visited[neighbour] > visited[tree] + 1:
                visited[neighbour] = visited[tree] + 1
                q.append((neighbour, tree))
            
            # End of a cycle, neighbour tree belongs to another path
            # If neighbour tree is not the same as previous tree (tree and neighbour tree directly connected),
            # update the minimum number of trees for cycle
            elif neighbour != prev_tree:
                # Number of trees = number of trees along path when first encountered neighbour tree
                # - number of trees along path when first encounted current tree
                min_trees = min(min_trees, visited[tree] + visited[neighbour] - 1)
    
    return min_trees


def main():
    n, m = map(int, stdin.readline().split())
    
    adj_list = [[] * n for _ in range(n)]
    for i in range(m):
        u, v = map(int, stdin.readline().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    min_trees = float('inf')
    # BFS from each tree
    for i in range(n):
        min_trees = BFS(i, n, min_trees, adj_list)

    if min_trees < float('inf'):
        print(min_trees)
    else:
        print('impossible')
           

if __name__ == '__main__':
    main()
