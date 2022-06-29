from sys import stdin
from heapq import *


def within_vault(r, c, vault):
    return 0 <= r < len(vault) and 0 <= c < len(vault[0])


def minimax(pq, largest_climb, vault):
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while pq:
        climb, r, c = heappop(pq)
        
        if r == len(vault)-1 and c == len(vault[0])-1:
            return climb

        if climb == largest_climb[r][c]:
            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]

                if within_vault(new_r, new_c, vault):
                    # If climb to next pos is negative, there is 0 cost
                    weight = max(vault[new_r][new_c] - vault[r][c], 0)
                    # Get the max of the largest climb from source to prev position, and current climb from prev position to current position
                    distance = max(climb, weight)
                    
                    # Update largest climb to current position from source if previously recorded is larger
                    if largest_climb[new_r][new_c] > distance:
                        largest_climb[new_r][new_c] = distance
                        heappush(pq, (distance, new_r, new_c))


def main():
    M, N = map(int, stdin.readline().split())

    vault = []
    for i in range(M):
        vault.append(list(map(int, stdin.readline().rstrip().split())))
    
    # largest_climb 2D array to store largest climb from source to a position
    # Initial max climb from source to a position is infinity, then we try to minimise this in minimax
    largest_climb = [[float('inf')] * N for _ in range(M)]
    # Max climb from source to source is 0
    largest_climb[0][0] = 0

    pq = []
    heappush(pq, (largest_climb[0][0], 0, 0))

    # Minimax modified Dijkstra
    print(minimax(pq, largest_climb, vault))


if __name__ == '__main__':
    main()
