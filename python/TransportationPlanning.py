from sys import stdin
import math


def euclidean_dist(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)


def floyd_warshall(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], (dist[i][k] + dist[k][j]))
    
    # Return the sum. 
    # Each pair will have their distance calculated twice: dist[x][y] == dist[y][x]
    # So divide by 2
    return sum(map(sum, dist)) / 2


def main():
    while True:
        n = int(stdin.readline())

        if n == 0:
            return

        intersections = []
        D = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            x, y = map(int, stdin.readline().split())
            intersections.append((x, y))
            D[i][i] = 0
        
        m = int(stdin.readline())

        road_set = set()
        for i in range(m):
            u, v = map(int, stdin.readline().split())
            dist = euclidean_dist(intersections[u], intersections[v])
            D[u][v] = dist
            D[v][u] = dist
            # Sort it so that it can be used when checking ascending order of intersection pairs with road_set
            sorted_pair = tuple(sorted((u, v)))
            road_set.add(sorted_pair)
        
        # total commute time (TCT) before adding any road using floyd_warshall
        TCT_before = floyd_warshall(D, n)
        
        # Largest difference from original TCT_before and the new TCT
        largest_minimise = 0
        
        # Double for loop essentially gets all combinations in sorted order (n choose 2)
        for i in range(n):
            for j in range(i+1, n):
                if (i, j) not in road_set:  # New road
                    new_dist = euclidean_dist(intersections[i], intersections[j])

                    # Direct distance from i to j is shorter than indirect one stored previously
                    # If equal to or longer, no need to process this because the shortest paths for the rest will not change, TCT remains the same
                    if new_dist < D[i][j]: 
                        # Make a copy with the new distance
                        new_D = [x[:] for x in D] 
                        new_D[i][j] = new_dist
                        new_D[j][i] = new_dist
                        
                        # For every other pair of cities k and l
                        # Update the min distance between them k --> i --> j --> l and k --> j ---> i ---> l
                        for k in range(n):
                            for l in range(n):
                                new_D[k][l] = min(new_D[k][l], new_D[k][i] + new_D[i][j] + new_D[j][l])
                                new_D[k][l] = min(new_D[k][l], new_D[k][j] + new_D[j][i] + new_D[i][l])
                        
                        # Get the new total commute time 
                        # Divide by 2 same reasoning in Floyd-Warshall function
                        TCT_after = sum(map(sum, new_D)) / 2
                 
                        if TCT_before - TCT_after > largest_minimise:
                            # New largest reduction
                            largest_minimise = TCT_before - TCT_after
                            # Store the previous total commute time
                            new_TCT = TCT_after
                            # Store the road
                            # Because we are going i from 0 to n-1, j from 0 to n-1, it will be lowest-numbered intersection
                            new_road = (i, j)

        if largest_minimise == 0:
            # No new road can reduce total commute time
            print(f'no addition reduces {TCT_before:.5f}')
        else:
            print(f'adding {new_road[0]} {new_road[1]} reduces {TCT_before:.5f} to {new_TCT:.5f}')
 
        # Floyd-Warshall
            # O(n^2) time
        # Going through each combination O(n^2) time
            # Each combination does O(n^2) of work for new distance updates when no existing roads (worst case)
            # O(n^4) time
        # Total time: O(n^4) + O(n^2) ~= O(n^4)
        # O(n^2) space for distance 2d lists


if __name__ == '__main__':
    main()
