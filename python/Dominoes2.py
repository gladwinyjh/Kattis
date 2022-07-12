from sys import stdin


def DFS(u, visited, adj_list, fall_over):
    # Mark domino as visited
    visited[u] = 1
    # Each time a domino falls, increment fall_over
    # Integer += 1 creates a new object, so the original fall_over value remains unchanged
        # So we need to return fall_over each time
    fall_over += 1

    for v in adj_list[u]:
        if not visited[v]:
            fall_over = DFS(v, visited, adj_list, fall_over)
    
    return fall_over


def main():
    TC = int(stdin.readline())
    while TC:
        n, m, l = map(int, stdin.readline().split())
        
        # Create adjacency list
        adj_list = [[] * n for _ in range(n)]
        for i in range(m):
            x, y = map(int, stdin.readline().split())
            adj_list[x-1].append(y-1)
        
        pushed = []
        visited = [0] * n
        # Store the pushed dominoes by hand
        for i in range(l):
            z = int(stdin.readline())
            pushed.append(z-1)
        
        # Number of dominoes that fall over
        fall_over = 0
        # Multi-source DFS
        for i in range(len(pushed)):
            if not visited[pushed[i]]:
                fall_over = DFS(pushed[i], visited, adj_list, fall_over)

        print(fall_over)

        TC -= 1


if __name__ == '__main__':
    main()
