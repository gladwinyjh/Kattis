from sys import stdin
from collections import deque


def withinGrid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def main():
    R, C = map(int, stdin.readline().split())
    
    # Visited 2d list of grid so that we can keep track of the positions the player has already visited
    # Prevents repeated visits
    visited = [[0] * C for _ in range(R)]
    # For flood fill
    flood_q = deque()
    # For tracking of possible player positions
    player_q = deque()

    grid = []
    for i in range(R):
        row = list(stdin.readline())[:-1]

        for idx, char in enumerate(row):
            if char == '*':
                # Add flood position to flood queue
                flood_q.append((i, idx))
            elif char == 'S':
                # Add player position and time elapsed to player queue
                player_q.append((i, idx, 0))
                # Mark this spot as visited by the player
                visited[i][idx] = 1
                # Since we are keeping track of where the player will be,
                # we can just replace the current position with '.' so it can be flood filled later
                char = '.'

        grid.append(row)
    
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # BFS starting from S
    # At each iteration/minute:
        # 1) Flooding takes priority. We first update the grid of the positions where flood spreaded to for this minute
        # 2) Obtain the possible next positions the player can go to 
    while player_q:
        # Do this so that it will only access new positions for current minute
        flood_q_len = len(flood_q)
        while flood_q_len:
            r, c = flood_q.popleft()

            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]
                
                # Check if new positions is within grid, and that the new position is empty
                if withinGrid(new_r, new_c, grid) and grid[new_r][new_c] == '.':
                    # Flood it
                    grid[new_r][new_c] = '*'
                    flood_q.append((new_r, new_c))

            flood_q_len -= 1
        
        # Same as above
        player_q_len = len(player_q)
        while player_q_len:
            row, col, time_elapsed = player_q.popleft()

            for i in range(4):
                new_row = row + DIR[i][0]
                new_col = col + DIR[i][1]

                if withinGrid(new_row, new_col, grid):
                    # Next position is the Den
                    # Since this is a queue, the first time this below if statement occurs
                    # it will be the smallest time_elapsed. So just print it + 1 and return
                    if grid[new_row][new_col] == 'D':
                        print(time_elapsed + 1)
                        return

                    # Next position is empty and has not been visited before
                    elif grid[new_row][new_col] == '.' and not visited[new_row][new_col]:
                        # Mark it as visited
                        visited[new_row][new_col] = 1
                        # Add new position to player queue with incremented time_elapsed
                        player_q.append((new_row, new_col, time_elapsed + 1))

            player_q_len -= 1
    
    # Unable to reach den
    print('KAKTUS')


if __name__ == '__main__':
    main()
