from sys import stdin
from collections import defaultdict, deque


def main():
    n = int(stdin.readline())
    
    while n:
        _ = stdin.readline()

        s = int(stdin.readline())
        
        DIR_DICT = {
                'N': (0, -1),
                'S': (0, 1),
                'E': (1, 0),
                'W': (-1, 0)
                }

        adj_list = defaultdict(list)
        # Start coordinates set to (0, 0)
        # Does not really matter what it is set to as coordinates are relative
        curr = (0, 0)
        for i in range(s):
            # Change in x and y coordinate
            dir_delta = DIR_DICT[stdin.readline().rstrip()]
            # New position 
            new_pos = (curr[0] + dir_delta[0], curr[1] + dir_delta[1])
            # Birectional path
            adj_list[curr].append(new_pos)
            adj_list[new_pos].append(curr)
            # Last curr will be food source
            curr = new_pos

        q = deque([(0, 0, 0)])
        visited = set((0, 0))
        
        # BFS from colony (0, 0) to food source (curr)
        while q:
            x, y, steps = q.popleft()
            
            if (x, y) == curr:
                print(steps)
                break

            for v in adj_list[(x, y)]:
                if v not in visited:
                    visited.add(v)
                    q.append((v[0], v[1], steps+1))

        n -= 1


if __name__ == '__main__':
    main()
