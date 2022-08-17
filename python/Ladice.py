from sys import stdin


def find(parent, i):
    if parent[i] == i:
        return i

    return find(parent, parent[i])


def union(parent, rank, size, x, y):
    if rank[x] > rank[y]:
        parent[y] = x
        size[x] += size[y]
    elif rank[x] < rank[y]:
        parent[x] = y
        size[y] += size[x]
    else:
        parent[y] = x
        rank[x] += 1
        size[x] += size[y]


def main():
    N, L = map(int, stdin.readline().split())

    parent = [i for i in range(L+1)]
    rank = [0] * (L+1)
    # Group drawers together
    # Keep track of sizes of each group
    size = [1] * (L+1)

    for i in range(N):
        A, B = map(int, stdin.readline().split())

        parent_A = find(parent, A)
        parent_B = find(parent, B)

        if size[parent_A] == 0:
            if size[parent_B] == 0:
                # Not enough space in group drawer A is in and group drawer B is in
                print('SMECE')
                continue
            else:
                # Store in drawer B
                # Decrease size of group drawer B is in by 1
                size[parent_B] -= 1
                print('LADICA')
        else:
            # Store in drawer A
            # Decrease size of group drawer A is in by 1
            size[parent_A] -= 1
            print('LADICA')

        if parent_A != parent_B:
            # Union both groups if they are not already a group
            # Combine both drawer sizes and assign the size to the parent of the group with the larger rank
            union(parent, rank, size, parent_A, parent_B)


if __name__ == '__main__':
    main()
