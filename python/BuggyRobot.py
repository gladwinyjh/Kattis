from sys import stdin
from heapq import *
from collections import defaultdict


def within_grid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def main():
    H, W = map(int, stdin.readline().split())

    grid = []
    pq = []
    for i in range(H):
        row = list(stdin.readline().rstrip())
        for j in range(W):
            if row[j] == 'S':
                s = (i, j)

        grid.append(row)
        
    friend = stdin.readline()
    
    DIR_DICT = {
            (-1, 0): 'U',
            (1, 0): 'D',
            (0, -1): 'L',
            (0, 1): 'R'
            }

    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    D = defaultdict(lambda: float('inf'))
    # (row, col, curr_friend_index) = number of deviations after processing friend's command at index 
    D[(s[0], s[1], 0)] = 0
    
    # (number of deviations, row, col, friend index)
    heappush(pq, (0, s[0], s[1], 0))
    
    """
    Do BFS from starting position
    
    At each position we have 3 options while there are still friend's moves to be processed:
        1) Use friend's move
            - No deviation occurs
            - Go to friend's next move after -> friend index += 1

        2) Skip friend's move (aka removing move)
            - Number of deviations += 1
            - Not going to use friend's current move in the future
                - So friend index += 1

        3) Use another move different from friend (aka inserting move)
            - Ex: if friend goes 'U', we go 'D', 'L', 'R'
            - Number of deviations += 1
            - Friend index to be processed next remains the same because we can still follow friends current move next

    If reached 'G' before or when friend's moves are all processed, the rest of his moves (if any) are redundant
        - No movement needed after reaching 'G'
        - No additional deviations

    If have not reached 'G' by the time all friend's moves are processed, continue BFS until reach 'G'
        - No more skipping moves
        - Do 1) and 3) but dont need to change friend index and every additional move is one more deviation (inserting moves at end)
    
    Store the smallest amount of deviations at each position and current friend index in D

    """
    while pq:
        deviations, r, c, curr_index = heappop(pq)
        
        # Reached 'G', just print deviations
        if grid[r][c] == 'G':
            print(deviations)
            break
        
        if curr_index < len(friend):
            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]

                if not within_grid(new_r, new_c, grid) or grid[new_r][new_c] == '#':
                    # Stay at current position
                    new_r = r
                    new_c = c
                
                # Do what friend does at current index
                if DIR_DICT[(DIR[i][0], DIR[i][1])] == friend[curr_index]:
                    if D[(new_r, new_c, curr_index+1)] > deviations:
                        D[(new_r, new_c, curr_index+1)] = deviations
                        heappush(pq, (deviations, new_r, new_c, curr_index+1))
                else:
                    # Insert another move to the left of current index
                    if D[(new_r, new_c, curr_index)] > deviations + 1:
                        D[(new_r, new_c, curr_index)] = deviations + 1
                        heappush(pq, (deviations+1, new_r, new_c, curr_index))

                # Skip current index, equivalent to removing 
                if D[(r, c, curr_index+1)] > deviations + 1:
                    D[(r, c, curr_index+1)] = deviations + 1
                    heappush(pq, (deviations+1, r, c, curr_index+1))
        
        else: # Have not reached 'G' after using all of friend's moves
            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]

                if within_grid(new_r, new_c, grid) and grid[new_r][new_c] != '#' and D[(new_r, new_c, curr_index)] > deviations + 1:
                    D[(new_r, new_c, curr_index)] = deviations + 1
                    heappush(pq, (deviations+1, new_r, new_c, curr_index))


if __name__ == '__main__':
    main() 
