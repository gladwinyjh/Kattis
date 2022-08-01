from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop


def update_vol(i, j, vols, D, poured, c, pq):
    # If cup i has liquid, pour into cup j
    if vols[i] and vols[j] < c[j]:
        # Additional volume needed to fill cup j to full
        to_full = c[j] - vols[j]
        # Lists are mutable, so only change values for the copy as we will need to preserve original list
        vols_copy = vols[:]

        # If additional volume is more than what is in cup i,
        # then can just empty cup i completely into cup j
        if to_full >= vols[i]:
            # Pour into cup j
            vols_copy[j] += vols_copy[i]
            # New poured volume
            new_poured = poured + vols_copy[i]
            # Empty cup i
            vols_copy[i] = 0
            # For dictionary hashing
            new_vols = tuple(vols_copy)
            
            # Update if possible for this combination of volumes
            if D[new_vols] > new_poured:
                D[new_vols] = new_poured
                heappush(pq, (new_poured, vols_copy))
        
        # Additional volume is less than what is in cup i,
        # Pour from cup i until cup j is full
        else:
            # Additional volume to fill cup j to full
            volume = c[j] - vols_copy[j]
            # Remove this volume from cup i
            vols_copy[i] -= volume
            # Cup j is now full
            vols_copy[j] = c[j]
            # New poured volume
            new_poured = poured + volume
            new_vols = tuple(vols_copy)
            
            # Update if possible for this combination of volumes
            if D[new_vols] > new_poured:
                D[new_vols] = new_poured
                heappush(pq, (new_poured, vols_copy))
                

def dijkstra(pq, D, V, c):
    while pq:
        
        poured, vols = heappop(pq)

        if vols[0] == V:
            return poured
        
        if D[tuple(vols)] == poured:
            # Get every pair of cups
            for i in range(len(vols)):
                for j in range(i+1, len(vols)):
                    # If both cups are empty or both cups are maxed out, skip
                    if ((not vols[i] and not vols[j]) or
                        (vols[i] == c[i] and vols[j] == c[j])):
                        continue
                    
                    # Try pouring liquid from cup i to cup j
                    update_vol(i, j, vols, D, poured, c, pq)
                    # Try pouring liquid from cup j to cup i
                    update_vol(j, i, vols, D, poured, c, pq)

    return 'impossible'
           

def main():
    n, *c, V = map(int, stdin.readline().split())
    
    # Starting volumes, first cup is full, rest are empty
    start = [c[0]] + [0] * (n-1)
    D = defaultdict(lambda: float('inf'))
    D[tuple(start)] = 0

    pq = []
    heappush(pq, (0, start))
    
    # Dijkstra
    # Try pouring from a cup to every other cup completely or until the other cup if full
    print(dijkstra(pq, D, V, c))


if __name__ == '__main__':
    main()
