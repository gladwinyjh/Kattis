from sys import stdin


def find(parent, i):
    if parent[i] == i:
        return i

    return find(parent, parent[i])


def union(parent, rank, par_a, par_b):
    if rank[par_a] > rank[par_b]:
        parent[par_b] = par_a
    elif rank[par_a] < rank[par_b]:
        parent[par_a] = par_b
    else:
        parent[par_a] = par_b
        rank[par_b] += 1


def main():
    N, Q = map(int, stdin.readline().split())

    # Standard Union-Find 
    parent = [i for i in range(1000000)]
    rank = [0] * 1000000

    for i in range(Q):
        command, a, b = stdin.readline().split()
        a = int(a)
        b = int(b)

        parent_a = find(parent, a)
        parent_b = find(parent, b)
        
        if parent_a != parent_b:
            if command == '=':
                union(parent, rank, parent_a, parent_b)
            else:
                print('no')
        elif command != '=':
            print('yes')


if __name__ == '__main__':
    main()
