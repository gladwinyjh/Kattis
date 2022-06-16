from sys import stdin
from collections import deque


def within_map(row, col, N, M):
    return 0 <= row < N and 0 <= col < M


def BFS(pos_queue, visited, grid, countries, dist, N, M):
    while pos_queue:
        row, col = pos_queue.popleft()
        
        # Cell has been processed before
        if visited[row][col]:
            continue

        visited[row][col] = 1

        cell = grid[row][col]
        
        if cell != 'W':
            # Check if the shortest path to reach this country cell is smaller than current stored in dictionary
            countries[cell] = min(countries[cell], dist[row][col])
        
        # Double for loop to simulate horizontal, diagonal, vertical movements
        for i in range(-1,2):
            for j in range(-1,2):
                # Same spot, so skip
                if i == 0 and j == 0:
                    continue
                new_row = row + i
                new_col = col + j
                
                # New position within map
                if within_map(new_row, new_col, N, M):
                    new_cell = grid[new_row][new_col]
                    
                    # Next cell is same as current cell
                        # Both 'W', dont need to increment borders crossed
                        # Both same country, dont need to increment as well
                    # Only update dist cell if the dist is shorter than prev stored in dist list (TLE if dont do so)
                    if new_cell == cell and dist[new_row][new_col] > dist[row][col]:
                        dist[new_row][new_col] = dist[row][col]
                        pos_queue.append((new_row, new_col))

                    # Else both cells are different
                        # 'W' and country: not a border, but because we start at -1, incrementing it = 0 (no border)
                        # 2 different countries: border
                    # Same thing, only update if there is a need to (TLE if dont do so)
                    elif dist[new_row][new_col] > dist[row][col] + 1:
                        dist[new_row][new_col] = dist[row][col] + 1
                        pos_queue.append((new_row, new_col))


def main():
    N, M = map(int, stdin.readline().split())

    grid = []
    visited = [[0] * M for _ in range(N)]
    water_queue = deque()
    # Dictionary to store countries and their borders crossed
    countries = {}
    # List to store shortest path or least number of borders crossed from water to cell
    dist = [[float('inf')] * M for _ in range(N)]

    for i in range(N):
        row = list(stdin.readline())[:-1]

        for j in range(M):
            # Store 'W' instead of countries as you will get TLE if u try to BFS from every country cell to a water cell
            # So instead, start from each 'W' and find the countries
            if row[j] == 'W':
                water_queue.append((i, j))
                # -1 because later when we find a different border we increment by 1
                # and the first water to country border will be 0 (not count as a border)
                dist[i][j] = -1
            elif row[j] not in countries:
                # Store countries in dictionary, initial borders crossed set to infinity as we want the minimum
                countries[row[j]] = float('inf')

        grid.append(row)
    
    # BFS from each water cell
    # Keep track of shortest path using dist list
    BFS(water_queue, visited, grid, countries, dist, N, M)
    
    # Sort and print dictionary 
    for country, landlockedness in sorted(countries.items()):
        print(country, landlockedness)


if __name__ == '__main__':
    main()
