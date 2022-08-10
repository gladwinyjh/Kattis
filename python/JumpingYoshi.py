from sys import stdin
from collections import deque, defaultdict


def main():
    N = int(stdin.readline())
    
    spots = list(map(int, stdin.readline().split()))

    # If i < j, forward jump:
        # j - i = spots[j] + spots[i]
        # spots[i] + i = j - spots[j]
    
    # If i > j, backward jump:
        # i - j = spots[j] + spots[i]
        # spots[i] - i = -spots[j] - j
    
    forward = defaultdict(list)
    backward = defaultdict(list)
    for idx, spot in enumerate(spots):
        forward[spot + idx].append(idx)
        backward[spot - idx].append(idx)

    q = deque([0])
    visited = [0] * N
    visited[0] = 1

    max_travel = 0
    while q:
        pebble = q.popleft()

        max_travel = max(max_travel, pebble)
         
        for next_pebble in forward[pebble - spots[pebble]]:
            if not visited[next_pebble]:
                visited[next_pebble] = 1
                q.append(next_pebble)

        for next_pebble in backward[-spots[pebble] - pebble]:
            if not visited[next_pebble]:
                visited[next_pebble] = 1
                q.append(next_pebble)
                
    print(max_travel) 


if __name__ == '__main__':
    main()

