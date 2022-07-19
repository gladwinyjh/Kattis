from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(pq, D, a, b, prev, groupings, group_sizes, groups):
    while pq:
        risk, name = heappop(pq)

        if name == b:
            # Reconstruct path
            path = []
            while prev[b] != b:
                path.append(b)
                b = prev[b]
            
            path.append(a)
            
            # Return risk, and reversed of path
            # -1 because dont consider name b as an intermediary
            return risk-1, path[::-1]

        if D[name] == risk:
            # Do this way because same pair of names can belong in different groups
            # To access neighbours of name:
                # 1) Check which group name belongs to
                # 2) For each group, check all its neighbours

            # Get groups name belongs to
            for group in groupings[name]:
                # Other names in same group
                for other_name in groups[group]:
                    # New risk = current risk so far + (group size - 2) + intermediary risk
                    if D[other_name] > risk + (group_sizes[group] - 2) + 1:
                        D[other_name] = risk + (group_sizes[group] - 2) + 1
                        # Store predecessor
                        prev[other_name] = name
                        heappush(pq, (D[other_name], other_name))
            
    return -1, 'impossible'


def main():
    for line in stdin:
        a, b = line.split()

        n = int(stdin.readline())
        
        # Dictionary that store the groups number that a name belongs to
        # key: name. value: list of groups name belongs to
        groupings = defaultdict(list)
        
        # Stores number of names in each group
        group_sizes = [0] * n

        # Stores all groups
        groups = []

        for i in range(n):
            group = list(stdin.readline().split())
            groups.append(group)
            group_sizes[i] = len(group)
            for name in group:
                groupings[name].append(i)
        
        D = defaultdict(lambda: float('inf'))
        D[a] = 0

        pq = []
        heappush(pq, (0, a))

        prev = {}
        prev[a] = a

        risk, path = dijkstra(pq, D, a, b, prev, groupings, group_sizes, groups)
        
        if risk == -1:
            print('impossible')
        else:
            print(risk, *path)


if __name__ == '__main__':
    main()
