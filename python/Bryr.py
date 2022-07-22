from sys import stdin
from collections import deque


def main():
    n, m = map(int, stdin.readline().split())
    
    adj_list = [[] * (n+1) for _ in range(n+1)]
    for i in range(m):
        a, b, c = map(int, stdin.readline().split())
        adj_list[a].append((b, c))
        adj_list[b].append((a, c))

    q = deque([(1, 0)])
    # Keep track of the number of single-lane bridges encountered from source 
    D = [float('inf')] * (n+1)
    D[1] = 0
    
    # Shortest path BFS with 0/1 weights
    # 0 weight for double-lane bridges (preferred), 1 weight for single-lane bridges
    # Append 0 double-lane bridges in front, single-lane bridges to the back
    while q:
        pos, num_single = q.popleft()

        if pos == n:
            print(num_single)
            return
        
        if D[pos] == num_single:
            for v, bridge in adj_list[pos]:
                # Check type of bridge and if D[v] can be updated
                if bridge == 1 and D[v] > num_single + 1:
                    D[v] = num_single + 1
                    q.append((v, num_single + 1))
                elif bridge == 0 and D[v] > num_single:
                    D[v] = num_single
                    # Want to process those routes with less single bridges first
                    # So append left for those with fewer single bridges
                    q.appendleft((v, num_single))


if __name__ == '__main__':
    main()
