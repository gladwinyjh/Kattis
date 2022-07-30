from sys import stdin
from heapq import heappush, heappop


def dijkstra(pq, D, adj_list, n):
    while pq:
        size, inter = heappop(pq)

        if inter == n-1:
            # Remember size is negative
            return -size

        if D[inter] == size:
            for other, factor in adj_list[inter]:
                # Keep updating minimum for the intersection
                if D[other] > size * factor:
                    D[other] = size * factor
                    heappush(pq, (D[other], other))


def main():
    while True:
        n, m = map(int, stdin.readline().split())

        if n == 0 and m == 0:
            return
        
        adj_list = [[] * n for _ in range(n)]
        for i in range(m):
            x, y, f = stdin.readline().split()
            x = int(x)
            y = int(y)
            f = float(f)
            adj_list[x].append((y, f))
            adj_list[y].append((x, f))
        
        '''
            Dijkstra
            We want the largest size to be processed first
            But since dijkstra uses min heap, we need to flip the sizes around: -1 <= size < 0
            So now the larger sizes are more negative, and those will be dequeued earlier
            
            Since the max size of Mikael is 1, we enqueue -1 to PQ

        '''
        pq = []
        # (Negative of size, current intersection)
        heappush(pq, (-1, 0))
        
        # Intialisation of D array 
        # Since we want to store the minimum now (smallest is -1), we intialise to INF
        D = [float('inf')] * n
        D[0] = -1

        print(f'{dijkstra(pq, D, adj_list, n):.4f}')


if __name__ == '__main__':
    main()
