from sys import stdin


def main():
    m, n = map(int, stdin.readline().split())
    # Distance 2D 26x26 for each letter a-z
    D = [[0] * 26 for _ in range(26)]
    # Populate D. ord(char) to get the unicode integer representation. -97 to make a-z in the range of 0-25
    for i in range(m):
        u, v = stdin.readline().split()
        # 1 if there is an edge from u to v
        D[ord(u)-97][ord(v)-97] = 1
    
    # Floyd-Warshall transitive closure variant
    for k in range(26):
        for i in range(26):
            for j in range(26):
                # Bitwise AND &:
                    # D[i][k] & D[k][j] returns 1 if there is a path connecting i to k and k to j -> path connecting i to j via k
                # Bitwise OR |:
                    # D[i][j] | (D[i][k] & D[k][j]) returns 1 if there is a path directly from i to j (D[i][j]) OR there is a path from i to j via k 
                # 0 if there is no path connecting i and j(direct or indirect via k), 1 if there is 
                D[i][j] = D[i][j] | (D[i][k] & D[k][j])
    
    for i in range(n):
        a, b = stdin.readline().split()
        # Different lengths
        if len(a) != len(b):
            print('no')
            continue
        
        match = True
        for j in range(len(a)):
            # Same character
            if a[j] == b[j]:
                continue
            # No path/mapping between the 2 characters
            if D[ord(a[j])-97][ord(b[j])-97] == 0:
                match = False
                break

        if match:
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    main()
