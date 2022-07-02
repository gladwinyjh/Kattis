from sys import stdin


def find_parent(parent, i):
    if parent[i] == i:
        return i

    return find_parent(parent, parent[i])


def union(parent, rank, parent_u, parent_v):
    if rank[parent_u] < rank[parent_v]:
        parent[parent_u] = parent_v
    elif rank[parent_u] > rank[parent_v]:
        parent[parent_v] = parent_u
    else:
        parent[parent_v] = parent_u
        rank[parent_u] += 1


def kruskals(edge_list, n):
    MST = []
    parent = []
    rank = []

    for i in range(n):
        parent.append(i)
        rank.append(0)

    for i in range(len(edge_list)):
        u, v, w = edge_list[i]
        parent_u = find_parent(parent, u)
        parent_v = find_parent(parent, v)

        if parent_u != parent_v:
            MST.append((u, v, w))

            if len(MST) == n-1:
                # MST already completed, print last weight added
                print(w)
                return

            union(parent, rank, parent_u, parent_v)
    
    print('IMPOSSIBLE')


def main():
    n, m = map(int, stdin.readline().split())

    edge_list = []
    for i in range(m):
        u, v, w = map(int, stdin.readline().split())
        edge_list.append((u, v, w))

    edge_list.sort(key=lambda x: x[2])
    
    # Kruskals process edges in ascending order
    # When the MST is completed, the last edge added in will be the largest in the MST
    # This is the minimum driving range
    kruskals(edge_list, n)


if __name__ == '__main__':
    main()

    # Time:
        # Read and store edge_list: O(m)
        # Sort edge list: O(logm)
        # Kruskals: O(mlogn)
        # Total: O(mlogn + logm + m)
    
    # Space:
        # edge list: O(m)
        # rank, parent, MST lists: O(n) each
        # Total: O(m + 3n)
