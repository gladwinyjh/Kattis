from sys import stdin
from collections import deque


def euclidean(c1, c2):
    # Sqrt not really necessary
    return (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2


def BFS(elsa_q, father_q, visited_elsa, visited_father, floor, elsa_graph, father_graph):
    elsa_reach = False
    father_reach = False

    while elsa_q or father_q:
        
        elsa_q_length = len(elsa_q)
        while elsa_q_length:
            elsa_r, elsa_c = elsa_q.popleft()
            
            if floor[elsa_r][elsa_c] == 'G':
                elsa_reach = True
                break
            
            for new_elsa_r, new_elsa_c in elsa_graph[(elsa_r, elsa_c)]:
                if not visited_elsa[new_elsa_r][new_elsa_c]:
                    visited_elsa[new_elsa_r][new_elsa_c] = 1
                    elsa_q.append((new_elsa_r, new_elsa_c))

            elsa_q_length -= 1
        
        father_q_length = len(father_q)
        while father_q_length:
            father_r, father_c = father_q.popleft()

            if floor[father_r][father_c] == 'G':
                father_reach = True
                break
            
            for new_father_r, new_father_c in father_graph[(father_r, father_c)]:
                if not visited_father[new_father_r][new_father_c]:
                    visited_father[new_father_r][new_father_c] = 1
                    father_q.append((new_father_r, new_father_c))
            
            father_q_length -= 1

        if father_reach and elsa_reach:
            print('SUCCESS')
            return
        elif elsa_reach and not father_reach:
            print('GO FOR IT')
            return
        elif father_reach and not elsa_reach:
            print('NO CHANCE')
            return

    print('NO WAY')


def main():
    A, F = map(int, stdin.readline().split())
    L, W = map(int, stdin.readline().split())
    
    floor = []
    elsa_graph = {}
    father_graph = {}
    elsa_queue = deque()
    father_queue = deque()
    visited_elsa = [[0] * W for _ in range(L)]
    visited_father = [[0] * W for _ in range(L)]
    
    for i in range(L):
        row = list(stdin.readline().rstrip())
        for j in range(W):
            if row[j] == 'S':
                elsa_queue.append((i, j))
                father_queue.append((i, j))
                visited_elsa[i][j] = 1
                visited_father[i][j] = 1
            
            if row[j] != 'B':
                elsa_graph[(i, j)] = set()
                father_graph[(i, j)] = set()
            
        floor.append(row)
    
    # Processing step: Find neighbours for each tile. Do for Elsa and father
    for pos, neighbours in elsa_graph.items():
        for other_pos, other_neighbours in elsa_graph.items():
            if pos == other_pos:
                continue
            
            dist = euclidean(pos, other_pos)
            
            # Row must be same OR columns must be same, and must be within F
            if ((pos[0] == other_pos[0] or pos[1] == other_pos[1]) and
                dist <= F**2):
                    father_graph[pos].add(other_pos)
            
            # No restrictions for Elsa, distance just be within A
            if dist <= A**2:
                elsa_graph[pos].add(other_pos)
    
    # Standard double flood fill BFS, just retrieve neighbours from respective dictionaries
    BFS(elsa_queue, father_queue, visited_elsa, visited_father, floor, elsa_graph, father_graph)


if __name__ == '__main__':
    
    # Double flood fill BFS problem with a twist
        # Elsa and father can only jump to specific tiles around them
            # Elsa -> Any tile within a distance of A units
                # Complicated
            # Father -> Vertical and horizontal adjacent tiles within a distance of F units
                # Relatively easier

    # How do we know which tiles can be travelled by Elsa and father
        # Method 1:
            # At each tile duing BFS
                # Check all tiles in a circular radius of A units to get the tiles Elsa can travel to next
                    # Complicated as need to keep generating tiles for each popped tile, then need to process them to check if they can be added to queue

        # Method 2 (used here):
            # Preprocessing
                # For each tile on the floor, check the euclidean distance with every other tile
                # If distance <= A units away, Elsa can travel to it from this tile
                # Store the tiles that she can travel to from this tile in a dictionary as a set

                # For the father,
                    # Since only can move 2 axes, if the 2 tiles for comparison have the same row OR the same col, the father can travel there
                        # Vertical travel -> same col, different row
                        # Horizontal travel -> same row, different col
                    
                    # Likewise, store the tiles in his own dictionary as a set
    
    # Double flood fill BFS:
        # Each outermost iteration corresponds to a unit of time
        # During each iteration, both Elsa and father will make one jump to a next tile
            # Doesnt matter who goes first 
            # To get tiles to travel to next, use respective dictionaries
        
        # See who reaches the goal tile first


    # Time:
        # Going through each row in grid: W times. Total L times -> O(L*W)
        # Constructing adjacency dictionaries: for all positions, go through all other positions -> O((L^2 * W*2))
        # BFS: Done twice, worst case all edges have to be processead -> O(2(V+E)) ~= O((L*W) + (L*W)^2) -> O(L*W + L^2 * W*2)

        # Overall: O(2(L*W)^2 + L*W), where L*W = area of floor input

    # Space:
        # Floor grid: O(L*W)
        # Elsa and father each need 
            # visited 2d list: O(L*W)
            # adjacency dictionary: (L*W)* (L*W) = O((L*W)^2)
            # queue: O(L*W)
        
        # Overall: O(4(L*W) + 2(L*W)^2)
                
    main()
