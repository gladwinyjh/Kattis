from sys import stdin
from heapq import heappop, heappush
from collections import defaultdict


class Cell():
    def __init__(self, ceil=None, floor=None):
        self.ceil = ceil
        self.floor = floor


def within_cave(r, c, cave):
    return 0 <= r < len(cave) and 0 <= c < len(cave[0])


def dijkstra(pq, D, N, M, H, cave):
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while pq:
        time_taken, r, c = heappop(pq)

        if (r, c) == (N-1, M-1):
            return time_taken

        if D[(r, c)] == time_taken:
            for i in range(4):
                new_r = r + DIR[i][0]
                new_c = c + DIR[i][1]
                
                # Conditions to be satisfied:
                    # 1) Cannot move off edge of map
                    # 2) Ceiling height of adjacent square must be >= 50 than:
                        # Floor height of current square
                        # Floor height of adjacent square
                    # 3) Ceiling height of current square must be >= 50 than floor height of adjacent square

                    # Still missing one condition which will address later, because we need to get the water level
                        # Ceiling height of adjacent square must be >= 50 than water level
                if (within_cave(new_r, new_c, cave) and
                        cave[new_r][new_c].ceil - cave[r][c].floor >= 50 and
                        cave[new_r][new_c].ceil - cave[new_r][new_c].floor >= 50 and
                        cave[r][c].ceil - cave[new_r][new_c].floor >= 50):
                    
                    # Calculate the waiting time for tide to fall to at least 50cm from ceiling of adjacent cell
                    # If dont need to wait because it is already >= 50cm, then wait_time == 0
                    wait_time = max(0, (H - (cave[new_r][new_c].ceil - 50)) / 10)
                    
                    # Get the time elapsed
                    # Either:
                        # 1) Waited at a cell at t = time_taken until t = wait_time for tide to fall to >= 50cm
                            # Have to wait till t = wait_time to enter cell
                            # time_taken < wait_time,  and we choose to wait till wait_time
                        # 2) Don't have to wait for tide to fall because already >= 50cm
                            # In this case, wait_time == 0
                            # So total time = time_taken + wait_time = time_taken

                    # Observe that is really just the max of the current time taken and the wait time
                    time = max(time_taken, wait_time)
                    
                    # Travelling time along cave must be counted only once tide started falling
                    # If time > 0, that means that we have already waited for tide to fall
                        # Either in current cell and/or from previous cells
                    # So we can start counting time via travelling
                    if time > 0:
                        # Current water height
                        water_level = H - (time * 10)
                        if water_level - cave[r][c].floor >= 20:
                            time += 1
                        else:
                            time += 10

                    if D[(new_r, new_c)] > time:
                        D[(new_r, new_c)] = time
                        heappush(pq, (D[(new_r, new_c)], new_r, new_c))


def main():
    T = int(stdin.readline())
    
    for case in range(1, T+1):
        H, N, M = map(int, stdin.readline().split())
        
        # 3D-ish grid
        # Fashioned into 2D grid with a Cell object that has attributes for the ceiling and the floor
        cave = [[0] * M for _ in range(N)]
        # 2 times for floor and ceiling
        for k in range(2):
            for i in range(N):
                row = list(map(int, stdin.readline().split()))
                for j in range(M):
                    if k == 0: # Storing ceiling, first time so create new Cell object
                        cave[i][j] = Cell(ceil=row[j])
                    else: # Storing floor
                        cave[i][j].floor = row[j]
        
        D = defaultdict(lambda: float('inf'))
        D[(0, 0)] = 0
        pq = []
        heappush(pq, (D[(0, 0)], 0, 0))

        print(f'Case #{case}: {dijkstra(pq, D, N, M, H, cave):.6f}')
       

if __name__ == '__main__':
    main()
    # Time only starts when you have to wait for the tide 
    # 3D grid 
