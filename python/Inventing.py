from sys import stdin


def find_parent(parent, i):
    if parent[i] == i:
        return i

    return find_parent(parent, parent[i])


def union(parent_u, parent_v, parent, rank, size):
    if rank[parent_u] > rank[parent_v]:
        parent[parent_v] = parent_u
        size[parent_u] += size[parent_v]
    elif rank[parent_u] < rank[parent_v]:
        parent[parent_u] = parent_v
        size[parent_v] += size[parent_u]
    else:
        parent[parent_v] = parent_u
        size[parent_u] += size[parent_v]
        rank[parent_u] += 1


def kruskals(edge_list, N):
    parent = []
    rank = []
    # Keep track of size of components the vertex is in
    size = []
    complete_weight = 0

    for i in range(N+1):
        parent.append(i)
        rank.append(0)
        # Intially each component consists of one vertex 
        size.append(1)

    for i in range(len(edge_list)):
        u, v, w = edge_list[i]
        parent_u = find_parent(parent, u)
        parent_v = find_parent(parent, v)
        
        # Take every vertex in 1 component and connect to to every vertex in other component
            # Total size[parent_u] * size[parent_v] number of connections
        # Give it weight of w + 1
            # If weight of w, there will be more than one MST
                # For the UNIQUE MST to only use this edge given in input, all other edges connecting these 2 components have to be greater than this one
                # If same weight, there will be more than one MST
                # If weight > w, the smallest edge weight will be the one given in the input (what we want)
                    # So we take the next biggest: w+1
        # We -1 from the total because we will be double counting this edge from u to v
            # u and v are already connected via w. But now we are assigning them with weight w+1. So we just deduct 1 from this edge
        
        # The edges need to be sorted (like in Kruskals)
            # If not processed in ascending order, when a smaller edge arrives, a new MST can be formed by taking the smaller edge to join the 2 components
        complete_weight += (size[parent_u] * size[parent_v]) * (w + 1) - 1

        # Subsequently we just combine this 2 components together like in Kruskals
        union(parent_u, parent_v, parent, rank, size)

    print(complete_weight)


def main():
    T = int(stdin.readline())

    for i in range(T):
        _ = stdin.readline()

        N = int(stdin.readline())
        edge_list = []
        for j in range(N-1):
            u, v, w = map(int, stdin.readline().split())
            edge_list.append((u, v, w))
        
        edge_list.sort(key=lambda x: x[2])
        
        # Insane way to use Kruskals
        kruskals(edge_list, N)


if __name__ == '__main__':
    main()
