from sys import stdin
from heapq import *


def within_block(r, c, block):
    return 0 <= r < len(block) and 0 <= c < len(block[0])


def dijkstra(pq, D, prev, block):
    best_cost = float('inf')
    while pq:
        total_cost, r, c = heappop(pq)
        
        # Destination is any cell in last row
        # Check if best cost to reach the cell can be improved
        # Update best cost and best path if possible
        if r == len(block)-1 and D[r][c] < best_cost:
            best_cost = D[r][c]
            best_path = (r, c)
            continue

        if D[r][c] == total_cost:
            # 8 directional movements
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue

                    new_r = r + i
                    new_c = c + j

                    if within_block(new_r, new_c, block) and D[new_r][new_c] > total_cost + block[new_r][new_c]:
                        D[new_r][new_c] = total_cost + block[new_r][new_c]
                        prev[(new_r, new_c)] = (r, c)
                        heappush(pq, (D[new_r][new_c], new_r, new_c))
    
    return best_path


def make_fracture(best_path, prev, block):
    block[best_path[0]][best_path[1]] = ' '
    
    if prev[best_path] == best_path:
        # Reached top row
        return

    make_fracture(prev[best_path], prev, block)


def main():
    while True:
        h, w = map(int, stdin.readline().split())

        if h == 0:
            return

        block = []
        for i in range(h):
            block.append(list(map(int, stdin.readline().rstrip())))
        
        # Multisource Dijkstra
        # Append all of first row to PQ
        pq = []
        D = [[float('inf')] * w for _ in range(h)]
        prev = {}
        for i in range(w):
            D[0][i] = block[0][i]
            prev[(0, i)] = (0, i)
            # (smallest cost thus far, row, col, path taken)
            heappush(pq, (D[0][i], 0, i))
        
        # Dijkstra from top row to bottom row
        best_path = dijkstra(pq, D, prev, block)
        
        # Recursively replace cells along fracture with ' '
        make_fracture(best_path, prev, block)
        
        for i in range(h):
            [print(''.join(str(x) for x in block[i]))]


if __name__ == '__main__':
    main()
