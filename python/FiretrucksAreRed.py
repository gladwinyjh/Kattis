from sys import stdin
from collections import defaultdict, deque


def BFS(q, adj_list, visited, n):
    ST = []

    while q:
        person = q.popleft()
        for neighbour, number in adj_list[person]:
            if not visited[neighbour]:
                visited[neighbour] = True

                # Early termination
                # Get the number of vertices needed to be in the MST, starting with n
                # Each time u add a vertext to the MST, n -= 1
                # When n == 0, no more vertices to be added
                n -= 1
                if n == 0:
                    return ST

                ST.append((person, neighbour, number))
                q.append(neighbour)
        
    return ST


def main():
    n = int(stdin.readline())
    
    d = {}
    adj_list = [[] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        m, *numbers = map(int, stdin.readline().split())
        for num in numbers:
            if num not in d:
                # Only need to maintain one vertex for a number
                d[num] = i
            else:
                adj_list[i].append((d[num], num))
                adj_list[d[num]].append((i, num))

    # Adjacency list does not contain all possible neighbours here because only 1 vertex is used for each key in d
    # But it does not matter because if there is an MST, you will be able to connect all vertices by some path (dont have to be the shortest)
    # Cannot generate a full adjacency list because of memory error and/or TLE of going through all neighbours for each vertex
    
    # Starting vertex for BFS can be anything from 1 to n
    # Does not matter if there is a spanning tree
    start = n
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True

    ST = BFS(q, adj_list, visited, n)

    if len(ST) != n-1:
        # Not a complete spanning tree
        print('impossible')
    else:
        [print(*x) for x in ST]
    
    
if __name__ == '__main__':
    main()
