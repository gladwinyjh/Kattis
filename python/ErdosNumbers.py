from sys import stdin
from collections import deque, defaultdict



def main():
    adj_list = defaultdict(list)
    # Set of authors
    authors_set = set()
    # Store authors from input in order
    authors = []

    for line in stdin:
        author, *coauthor = line.split()
        # Birectional edge
        adj_list[author].extend(coauthor)
        [adj_list[x].append(author) for x in coauthor]
        authors_set.add(author)
        authors.append(author)
        
    q = deque(['PAUL_ERDOS'])
    visited = set()
    visited.add('PAUL_ERDOS')
    
    # Initial Erdos number == 0
    number = 0
    # Dictionary to store authors erdos number
    erdos = {}
    # BFS flood-fill like
    while q:
        q_length = len(q)
        
        while q_length:
            name = q.popleft()

            if name in authors_set:
                erdos[name] = number
            
            for coauthor in adj_list[name]:
                if coauthor not in visited:
                    visited.add(coauthor)
                    q.append(coauthor)

            q_length -= 1

        number += 1
    
    # If name not in erdos dictionary, author is not reachable from Erdos
    for name in authors:
        [print(name, erdos[name]) if name in erdos else print(name, 'no-connection')]


if __name__ == '__main__':
    main()
    # Erdos number of a coauthor is the shortest path from Erdos to the coauthor
        # Shortest path == min number of edges

    # BFS with Erdos as source
        # Each iteration increase number by 1 starting from 0
