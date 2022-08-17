from sys import stdin
from collections import defaultdict


def find(parent, i):
    if parent[i] == i:
        return i

    return find(parent, parent[i])


def union(parent, rank, size, x, y):
    # Combine the smaller rank network under the larger rank one
    # Add the sizes together
    if rank[x] < rank[y]:
        parent[x] = y
        size[y] += size[x]
        # Return the larger size
        return size[y]
    elif rank[x] > rank[y]:
        parent[y] = x
        size[x] += size[y]
        # Return the larger size
        return size[x]
    else:
        parent[y] = x
        rank[x] += 1
        size[x] += size[y]
        return size[x]


def main():
    T = int(stdin.readline())

    while T:
        # Union-Find
        parent = {}
        rank = defaultdict(lambda: 0)
        # Keep track of number of friends in curent network
        size = defaultdict(lambda: 1)

        for i in range(int(stdin.readline())):
            f1, f2 = stdin.readline().split()
            if f1 not in parent:
                parent[f1] = f1

            if f2 not in parent:
                parent[f2] = f2

            parent_f1 = find(parent, f1)
            parent_f2 = find(parent, f2)

            if parent_f1 != parent_f2:
                # 2 people from different networks, combine them together to form a larger network
                print(union(parent, rank ,size, parent_f1, parent_f2))
            else:
                # Same parent, print size[parent_f1] or size[parent_f2]
                print(size[parent_f2])

        T -= 1


if __name__ == '__main__':
    main()
