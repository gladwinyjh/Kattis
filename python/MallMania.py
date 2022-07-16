from sys import stdin
from collections import deque, defaultdict


def BFS(q, dest, visited):
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
    min_dist = 0
    while q:
        q_length = len(q)

        while q_length:
            a, s = q.popleft()

            if (a, s) in dest:
                return min_dist

            for i in range(4):
                new_a = a + DIR[i][0]
                new_s = s + DIR[i][1]

                if 0 < new_a < 2000 and 0 < new_s < 2000 and not visited[(new_a, new_s)]:
                    visited[(new_a, new_s)] = 1
                    q.append((new_a, new_s))

            q_length -= 1

        min_dist += 1


def main():
    while True:
        p1 = int(stdin.readline())
        
        if p1 == 0:
            return
        
        q = deque()
        visited = defaultdict(lambda: 0)
        perimeter1 = []

        while len(q) != p1:
            line = list(map(int, stdin.readline().split()))
            for i in range(0, len(line), 2):
                q.append((line[i], line[i+1]))
                visited[(line[i], line[i+1])] = 1
        
        p2 = int(stdin.readline())
        dest = set()
        
        while len(dest) != p2:
            line = list(map(int, stdin.readline().split()))
            for i in range(0, len(line), 2):
                dest.add((line[i], line[i+1]))
        
        # Multisource BFS
        # Return distance once reached any of the coordinates in dest
        print(BFS(q, dest, visited))


if __name__ == '__main__':
    # Code is correct, but will give TLE on Kattis using Python 3
    main()
