from sys import stdin
from heapq import *


def within_board(r, c, board):
    return 0 <= r < len(board) and 0 <= c < len(board[0])


def dijkstra(pq, board, moves):
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    # Mappings for Direction to coordinates
    direct_map = {
            'U': (-1, 0),
            'D': (1, 0), 
            'L': (0, -1),
            'R': (0, 1)
            }
            
    # Inverse directional Mappings
    inv_direct_map = {v: k for k, v in direct_map.items()}
    
    # Mappings for clockwise 90deg turn
    clockwise_map = {
            'U': 'R',
            'R': 'D',
            'D': 'L',
            'L': 'U'
            }
            
    # Mappings for anticlockwise 90deg turn
    anticlockwise_map = {
            'U': 'L',
            'L': 'D',
            'D': 'R',
            'R': 'U'
            }
            
    # Mappings for opposite 180deg turns
    opp_map = {
        'U': 'D',
        'R': 'L',
        'L': 'R',
        'D': 'U'
    }

    while pq:
        num_moves, pos = heappop(pq)
        
        if board[pos[0]][pos[1]] == 'D':
            return pos[3]
        
        if num_moves == moves[pos[0]][pos[1]]:
            for i in range(4):
                new_r = pos[0] + DIR[i][0]
                new_c = pos[1] + DIR[i][1]
                
                # Check if within board and not a rock castle
                if within_board(new_r, new_c, board) and board[new_r][new_c] != 'C':
                    
                    # Next cell is directly in front of turtle, 'F' to go to the next cell
                    if (DIR[i][0], DIR[i][1]) == direct_map[pos[2]]:
                        new_moves = pos[3].copy()
                        if board[new_r][new_c] == 'I' and moves[new_r][new_c] > num_moves + 2: # Additional move if there is an ice castle to be broken
                            moves[new_r][new_c] = num_moves + 2
                            new_moves.extend(('X', 'F')) # Break ice -> go forward
                            new_pos = (new_r, new_c, pos[2], new_moves)
                            heappush(pq, (num_moves + 2, new_pos))
                        elif moves[new_r][new_c] > num_moves + 1: # Empty cell, just move forward
                            moves[new_r][new_c] = num_moves + 1
                            new_moves.append('F') 
                            new_pos = (new_r, new_c, pos[2], new_moves)
                            heappush(pq, (num_moves + 1, new_pos))
                            
                    # Opposite direction, turn clockwise or anticlockwise 2 times, then go forward
                    # Can either turn left twice or turn right twice. Code here chooses to turn left twice
                    elif opp_map[pos[2]] ==  inv_direct_map[(DIR[i][0], DIR[i][1])]:
                        new_moves = pos[3].copy()
                        if board[new_r][new_c] == 'I' and moves[new_r][new_c] > num_moves + 4: # Additional move if there is an ice castle to be broken
                            moves[new_r][new_c] = num_moves + 4
                            new_moves.extend(('L', 'L', 'X', 'F')) # Turn left twice -> break ice -> go forward
                            new_pos = (new_r, new_c, inv_direct_map[(DIR[i][0], DIR[i][1])], new_moves)
                            heappush(pq, (num_moves + 4, new_pos))
                        elif moves[new_r][new_c] > num_moves + 3: # Empty cell. Turn left twice -> go forward
                            moves[new_r][new_c] = num_moves + 3
                            new_moves.extend(('L', 'L', 'F'))
                            new_pos = (new_r, new_c, inv_direct_map[(DIR[i][0], DIR[i][1])], new_moves)
                            heappush(pq, (num_moves + 3, new_pos))
                    
                    # Clockwise/Anticlockwise direction once  
                    else: 
                        next_step = inv_direct_map[(DIR[i][0], DIR[i][1])]
                        
                        # Turn clockwise
                        if next_step == clockwise_map[pos[2]]: 
                            new_moves = pos[3].copy()
                            if board[new_r][new_c] == 'I' and moves[new_r][new_c] > num_moves + 3: # Additional move if there is an ice castle to be broken
                                moves[new_r][new_c] = num_moves + 3
                                new_moves.extend(('R', 'X', 'F')) # Turn right first -> Break ice -> go forward
                                new_pos = (new_r, new_c, next_step, new_moves)
                                heappush(pq, (num_moves + 3, new_pos))
                            elif moves[new_r][new_c] > num_moves + 2: # Empty cell. Turn right -> go forward
                                moves[new_r][new_c] = num_moves + 2
                                new_moves.extend(('R', 'F'))
                                new_pos = (new_r, new_c, next_step, new_moves)
                                heappush(pq, (num_moves + 2, new_pos))
                        
                        # Turn anticlockwise
                        elif next_step == anticlockwise_map[pos[2]]: 
                            new_moves = pos[3].copy()
                            if board[new_r][new_c] == 'I' and moves[new_r][new_c] > num_moves + 3: # Additional move if there is an ice castle to be broken
                                moves[new_r][new_c] = num_moves + 3
                                new_moves.extend(('L', 'X', 'F')) # Turn left first -> Break ice -> go forward
                                new_pos = (new_r, new_c, next_step, new_moves)
                                heappush(pq, (num_moves + 3, new_pos))
                            elif moves[new_r][new_c] > num_moves + 2: # Empty cell. Turn left -> go forward
                                moves[new_r][new_c] = num_moves + 2
                                new_moves.extend(('L', 'F'))
                                new_pos = (new_r, new_c, next_step, new_moves)
                                heappush(pq, (num_moves + 2, new_pos))
        
    return ['no', ' solution']


def main():
    board = []
    for i in range(8):
        row = list(stdin.readline().rstrip())
        board.append(row)
    
    moves = [[float('inf')] * 8 for _ in range(8)]
    moves[7][0] = 0
    
    # Use a PQ instead of a deque as breaking ice, turning directions can be seen as increased weights to go to the next cell (as opposed to just going forward (weight 1))
    # (number of moves made, (row, col, direction, path taken))
    pq = [(0, (7, 0, 'R', list()))]

    print(''.join(dijkstra(pq, board, moves)))
    

if __name__ == '__main__':
    main()
