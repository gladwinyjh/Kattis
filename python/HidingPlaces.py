from collections import deque


def withinBoard(row, col):
    return 0 <= row < 8 and 0 <= col < 8


def main():
    col_id = 'abcdefgh'
    n = int(input())

    for i in range(n):
        start = input()
        col = col_id.index(start[0])
        row = 8 - int(start[1])

        board = [[-1] * 8 for _ in range(8)]
        # Enqueue starting position, number of jumps so far = 0
        q = deque([(row, col, 0)])
        
        # Record the maximum number of jumps seen
        max_jumps = 0
        # BFS
        while q:
            row, col, num_jumps = q.popleft()
            # Update position's number of jumps on the board
            board[row][col] = num_jumps
            # Update max jumps if possible
            max_jumps = max(max_jumps, num_jumps)
            
            # Traverse knights next position
            DIR = [[-1, -2], [1, -2], [1, 2], [-1, 2], [-2, -1], [-2, 1], [2, -1], [2, 1]]
            for i in range(8):
                new_row = row + DIR[i][0]
                new_col = col + DIR[i][1]

                # Check if still within board, and that board position have not yet been visited
                if withinBoard(new_row, new_col) and board[new_row][new_col] == -1:
                    # Increment num_jumps
                    q.append((new_row, new_col, num_jumps+1))
        
        # Get the positions of the max_jumps from board
        # Start from top row, leftmost col each row
        ret = []
        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                if col == max_jumps:
                    # Convert from 0-based indexing to chess notations
                    ret.append(col_id[col_idx] + str(8-row_idx))

        print(max_jumps, ' '.join(ret))
        

if __name__ == '__main__':
    main()
