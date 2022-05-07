from collections import deque


def withinGrid(n, m, row, col):
    if row < 0 or col < 0 or row > n-1 or col > m-1:
        return False

    return True


def main():
    n, m = map(int, input().split())
    visited = [[False]*m for _ in range(n)]

    grid = []
    for i in range(n):
        row = [int(e) for e in list(input())]
        grid.append(row)
    
    numMoves = 0
    q = deque([(0, 0, numMoves)])
    visited[0][0] = True
    
    # Do BFS
    while q:
        row, col, numMoves = q.popleft()
        
        # Direction list to help in navigation x and y coordinates
        DIR = [[0,1],[0,-1],[1,0],[-1,0]]

        for i in range(4):
            new_row = row + grid[row][col] * DIR[i][0]
            new_col = col + grid[row][col] * DIR[i][1]
            
            # Check if the new (x,y) is within the grid, and that that tile has not been visited before
            if withinGrid(n, m, new_row, new_col) and not visited[new_row][new_col]:
                # BFS, first encounter with the target tile will always be the least number of moves to get there
                # Return the number of moves + 1 more move to get there
                if new_row == n-1 and new_col == m-1:
                    return numMoves + 1
                # Tile is visited
                visited[new_row][new_col] = True
                q.append((new_row, new_col, numMoves+1))

    return -1


if __name__ == '__main__':
    print(main())
