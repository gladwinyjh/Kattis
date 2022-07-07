from sys import stdin
from collections import defaultdict


def DFS(adj_list, character, visited, order):
    visited[character] = 1
    for v in adj_list[character]:
        if not visited[v]:
            DFS(adj_list, v, visited, order)

    order.append(character)


def main():
    N = int(stdin.readline())
    
    # Stores the characters and their spoken language
    # Key: character, val: spoken language
    characters = {}

    # Stores the characters that can understand a language
    # Key: language, val: characters
    understand = defaultdict(list)
    for i in range(N):
        name, speak, *x = stdin.readline().split()
        characters[name] = speak

        for j in x:
            # Character can understand these languages
            understand[j].append(name)
        
        # Character can understand own spoken language
        understand[speak].append(name)
    
    # Create adjacency list for toposort
    # Key: character, val: characters that can understand the language spoken by the key (including key itself)
    adj_list = defaultdict(list)
    for key, val in characters.items():
        for name in understand[val]:
            adj_list[key].append(name)
    
    # DFS Toposort
    visited = defaultdict(lambda: 0)
    # Topo order in reversed
    order = []
    for key, val in characters.items():
        if not visited[key]:
            DFS(adj_list, key, visited, order)

    # Reverse adjacency list for Kosaraju
    rev_adj_list = defaultdict(list)
    for key, val in adj_list.items():
        for x in val:
            rev_adj_list[x].append(key)
    
    # DFS Kosaraju
    visited = defaultdict(lambda: 0)

    # Track the maximum SCC size
    # We only keep the largest SCC and discard all characters belonging to the rest of the SCCs
    max_SCC_size = 0
    for c in reversed(order): 
        # List to store current SCC
        SCC = []
        if not visited[c]:
            DFS(rev_adj_list, c, visited, SCC)
            # Update largest SCC
            max_SCC_size = max(max_SCC_size, len(SCC))
    
    # Discard the rest, print out how many characters to discard
    print(N - max_SCC_size)


if __name__ == '__main__':
    main()
    
    # DFS Toposort -> O(V+E)
    # Form SCC -> Kosaraju -> O(V+E)
        # Sort SCC based on size -> O(nlogn), where n is the number of SCCs
        # Only keep the largest SCC 
            # Get size of largest SCC -> O(1)
            # Substract total vertices from the size to get the number of vertices to be removed -> O(1)
