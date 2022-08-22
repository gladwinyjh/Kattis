from sys import stdin
from collections import deque


def within_diagram(r, c, diagram):
    return 0 <= r < len(diagram) and 0 <= c < len(diagram[0])


def BFS(q, diagram):
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    border = set()
    while q:
        letter, r, c, direct = q.popleft()
        border.add((r, c))
        
        # Intersection: continue in direction of travel
        # Assumed that labels 'A' and 'B' will not lie on an intersection, so direct will not be empty
            # If not loop borders will be ambiguous 
        # If condition specified in problem statement
        if (diagram[r-1][c] == 'X' and 
                diagram[r+1][c] == 'X' and 
                diagram[r][c-1] == 'X' and 
                diagram[r][c+1] == 'X' and
                diagram[r-1][c-1] == '.' and
                diagram[r-1][c+1] == '.' and
                diagram[r+1][c-1] == '.' and
                diagram[r+1][c+1] == '.'):
            
            # Keep going in that direction
            if direct == 'U' and (r-1, c) not in border:
                q.append((letter, r-1, c, direct))
            elif direct == 'D' and (r+1, c) not in border:
                q.append((letter, r+1, c, direct))
            elif direct == 'L' and (r, c-1) not in border:
                q.append((letter, r, c-1, direct))
            elif direct == 'R' and  (r, c+1) not in border:
                q.append((letter, r, c+1, direct))
            
            # Do not process any further
            continue

        for i in range(4):
            new_r = r + DIR[i][0]
            new_c = c + DIR[i][1]
            
            # Keep track of direction of travel
            # From DIR list
            if i == 0:
                new_direct = 'D'
            elif i == 1:
                new_direct = 'U'
            elif i == 2:
                new_direct = 'R'
            else:
                new_direct = 'L'
            
            # Next cell must be:
            #   1) Within diagram
            #   2) Not a valid border path
            #   3) A border path that has yet to be visited
            if (within_diagram(new_r, new_c, diagram) and 
                    diagram[new_r][new_c] == 'X' and 
                    (new_r, new_c) not in border):
                q.append((letter, new_r, new_c, new_direct))
    
    # At this stage, border set will contain all coordinates of our border

    # Remember we pad our diagram with 'O'
    # Now we can flood fill from anywhere on the padding to record the exterior cells that do not belong to the loop
    # Here, we start from top left corner
    q = deque([(0, 0)])
    exterior = set()
    exterior.add((0, 0))
    while q:
        r, c = q.popleft()

        for i in range(4):
            new_r = r + DIR[i][0]
            new_c = c + DIR[i][1]
            
            # Cells that are:
            #   1) Still within the diagram
            #   2) Not along the border
            #   3) Has yet to be visited

            # These cells are unvisited exterior cells
            if (within_diagram(new_r, new_c, diagram) and 
                    (new_r, new_c) not in border and 
                    (new_r, new_c) not in exterior):
                exterior.add((new_r, new_c))
                q.append((new_r, new_c))
    
    # Flood fill rest of the cells to get interior cells
    # Not really necessary, since by default the rest of the cells will be the interior
    # Doing it here so that is more logical flow
    # If not checking interior = checking if not on border or on exterior
    filled = False
    interior = set()
    for i in range(len(diagram)):
        for j in range(len(diagram[0])):
            # Find the first (i, j) that belongs on the interior
            if (i, j) not in border and (i, j) not in exterior:
                q = deque([(i, j)])
                interior.add((i, j))

                while q:
                    r, c = q.popleft()

                    for i in range(4):
                        new_r = r + DIR[i][0]
                        new_c = c + DIR[i][1]

                        if (within_diagram(new_r, new_c, diagram) and 
                                (new_r, new_c) not in border and 
                                (new_r, new_c) not in exterior and 
                                (new_r, new_c) not in interior):
                            interior.add((new_r, new_c))
                            q.append((new_r, new_c))
                
                # Only need to fill once, so break
                filled = True
                break

        if filled:
            break

    return interior, border


def main():
    r, c = map(int, stdin.readline().split())
    
    # Pad the diagram with a neutral 'O' on all sides
    diagram = [['O'] * (c+2)]
    for i in range(1, r+1):
        row = ['O']
        row.extend(list(stdin.readline().rstrip()))
        row.append('O')
        for j in range(len(row)):
            # 'A' and 'B' labels will be our starting points for BFS
            if row[j] == 'A':
                a_r = i
                a_c = j
            elif row[j] == 'B':
                b_r = i
                b_c = j

        diagram.append(row)

    diagram.append(['O'] * (c+2))
    
    # BFS for A
    q = deque([('A', a_r, a_c, '')])
    # Returns the coordinates of the interior of Loop A and the border of Loop A
    a_interior, a_border = BFS(q, diagram)
    
    # BFS for B
    q = deque([('B', b_r, b_c, '')])
    # Returns the coordinates of the interior of Loop B and the border of Loop B
    b_interior, b_border = BFS(q, diagram)
    
    # Traverse entire diagram
    exclusive_A = 0
    exclusive_B = 0
    area_inter = 0
    for i in range(len(diagram)):
        for j in range(len(diagram[0])):
            if ((i, j) in a_interior and 
                    ((i, j) not in b_interior and (i, j) not in b_border)):
                # Cell belongs in interior of A and (not in interior of B and not on border of B)
                # Exclusive A ++
                exclusive_A += 1
            elif ((i, j) in b_interior and 
                    ((i, j) in a_interior and (i, j) not in a_border)):
                # Cell belongs in interior of B and (not in interior of A and not on border of A)
                # Exclusive B ++
                exclusive_B += 1
            elif (i, j) in a_interior and (i, j) in b_interior:
                # Cell belongs in both of the loops of the interiors
                area_inter += 1

    print(exclusive_A, exclusive_B, area_inter)


if __name__ == '__main__':
    main()
