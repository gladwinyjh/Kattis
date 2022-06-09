from sys import stdin
from collections import deque, defaultdict
import math


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True


def within_grid(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def generate_grid(n):
    # Generate grid
    # Notice that the grid subsets that end with even squares (i.e x^2 where x is even)
    # have their greatest value in the top left corner of their grid subset
    # Ex: 2^2 = 4, 4 is the top left corner of the square grid subset of 1-4
    #   : 8^2 = 64, 64 is the top left corner as well

    # So we know the direction of numbers in descending order: right -> down -> left -> up
        # Direction changes when it reaches the end of the grid
        # or when it encounters a higher value than itself/i.e value has already been set before

        # So each time we experience this, we change directions
        # And we keep repeating the order: after up -> right -> down -> ...

    grid = [[-1] * int(math.sqrt(n)) for _ in range(int(math.sqrt(n)))]
    # Use dictionary to store positions of values for easy look up later
    coordinates = {}
    
    # Start in descending order, from top left (Since we know even squares are always top left corner)
    row = 0
    col = 0
    
    # Variable used to navigate DIR list
    i = 0
    # DIR list: [right, down, left, up]
    DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    while n >= 1:
        # Store in dictionary
        coordinates[n] = (row, col)
        # Update grid
        grid[row][col] = n
        
        new_row = row + DIR[i][0]
        new_col = col + DIR[i][1]
        # Check if directional change is needed
        if not within_grid(new_row, new_col, grid) or grid[new_row][new_col] != -1:
            # Increment i by 1
            # Modulus by 4 so that it will loop back after 'up' back to 'right'
            i = (i+1) % 4
        
        # Get new coordinates
        row += DIR[i][0]
        col += DIR[i][1]
        # Decrement n
        n -= 1

    return grid, coordinates


def BFS(q, y, visited, coordinates, grid):
    # DIR list to check all 4 directions
    DIR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # Variable to record path lengths so far from source
    path_length = 0
    while q:
        queue_length = len(q)
        
        # Process all values for current path length
        while queue_length:
            val = q.popleft()

            if val == y:
                # Reached destination
                # Because it is BFS, the first occurrence of val == y is the shortest path length
                # Return this length
                return path_length

            for i in range(4):
                # Check up, down, left, right
                new_row = coordinates[val][0] + DIR[i][0]
                new_col = coordinates[val][1] + DIR[i][1]
                
                # New position is within grid, is not a prime number (can only go to non-prime), and has not yet been visited
                if within_grid(new_row, new_col, grid) and not is_prime(grid[new_row][new_col]) and not visited[(new_row, new_col)]:
                    # Mark it as visited to prevent revisiting
                    visited[(new_row, new_col)] = 1
                    # Add next position to queue
                    q.append(grid[new_row][new_col])
            
            queue_length -= 1
        
        # Finished processing all positions for current path length
        # Increment path length for next positions
        path_length += 1
    
    # If reached here, queue is empty and destination was not reached
    return 'impossible'


def main():
    # Generate spiral grid of 1-10000 
    # This gives us a 100x100 grid, and dictionary 'coordinates' of all the integer's positions in the grid
    grid, coordinates = generate_grid(10000)
    case = 1
    while True:
        try:
            x, y = map(int, input().split())
            
            q = deque([x])
            # Mark source as visited, rest unvisited
            visited = defaultdict(lambda: 0)
            visited[coordinates[x]] = 1
            
            # Breadth First Search
            print(f'Case {case}: {BFS(q, y, visited, coordinates, grid)}')

        except EOFError:
            return
        
        case += 1


if __name__ == '__main__':
    main()
