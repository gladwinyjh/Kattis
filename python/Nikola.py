import sys
# Increase recursion limit to not get Runtime error
sys.setrecursionlimit(3000)


def get_smallest_cost(entry_fees, curr_pos, pre_jump, cache):        
    # OOB, return inf so that min() will not choose it
    if curr_pos < 0 or curr_pos >= len(entry_fees):
        return float('inf')
    
    # Step alr visited before, just return cached value
    if cache[pre_jump][curr_pos] != float('inf'):
        return cache[pre_jump][curr_pos]
    
    # Last step
    if curr_pos == len(entry_fees) - 1:
        return entry_fees[curr_pos]
    
    # Fill cache with forward movement
    forward = get_smallest_cost(entry_fees, curr_pos + pre_jump + 1, pre_jump + 1, cache)
    
    # Fill cache with backward movement
    backward = get_smallest_cost(entry_fees, curr_pos - pre_jump, pre_jump, cache)
    
    # Update cache: entry_fee to enter current tile + minimum of forward and backward movements
    cache[pre_jump][curr_pos] = entry_fees[curr_pos] + min(backward, forward)
        
    return cache[pre_jump][curr_pos]   


def main():
    N = int(input())

    entry_fees = []
    for i in range(N):
        entry_fees.append(int(input()))
   
    # Cache to store [previous jump to reach step][min cost to reach step]
    cache = [[float('inf') for x in range(N)] for y in range(N)]     
    
    # Start from 2nd step as it is the only option from 1st step
    print(get_smallest_cost(entry_fees, 1, 1, cache))


if __name__ == '__main__':
    main()
