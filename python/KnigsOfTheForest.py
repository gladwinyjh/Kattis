from sys import stdin
from heapq import heappush, heappop


def main():
    k, n = map(int, stdin.readline().split())
    y, p = map(int, stdin.readline().split())
    
    # PQ for sorting by year of entry: earlier at the front of PQ
    mooses = []
    # Add Algtav to PQ
    heappush(mooses, (y, p))
    
    # Dictionary for easy reference between year of entry and strength
    # Because strength of moose is unique
    d = {}
    d[-p] = y

    for i in range(n+k-2):
        y_, p_ = map(int, stdin.readline().split())
        
        # Push to PQ
        heappush(mooses, (y_, p_))
        # Store in dictionary
        # Key: negative strength (for later PQ is a min heap), Value: year of entry
        d[-p_] = y_
    
    # Starting year is 2011
    curr_year = 2011

    # PQ for sorting by strength
    # Stronger moose will be in the front
    pool = []
    
    while mooses:
        # Fill up pool(regardless of year of entry)
        while len(pool) < k:
            year, strength = heappop(mooses)
            # Push to PQ NEGATIVE strength because of min heap
            # So stronger is in the front
            heappush(pool, -strength)
        
        next_alpha_strength = heappop(pool)
        
        # Since unique strengths, if == p, this is Algtav
        if -next_alpha_strength == p:
            print(curr_year)
            return
         
        next_alpha_year = d[next_alpha_strength]
        
        # Current year is behind next moose in queue
        # So fast forward to this moose's year of entry
        if next_alpha_year > curr_year:
            curr_year = next_alpha_year
        else:
            # Just process next moose in queue per normal
            curr_year += 1
    
    # If there is still moose remaining, it is Algtav (all moose processed before Algtav)
    # Insufficient data, prob because a moose with higher strength may arrive the following year
    #   Ex Sample 2: Moose can arrive in 2015 with strength 6 to be alpha over Algtav
    print('unknown')


if __name__ == '__main__':
    main()
