import math


def main():
    n = int(input())
    
    # Grill timing list to store the number of burgers on the grill at any time point
    # 43201 because of the upper bound of t
    grill = [0] * 43201
    
    # min_start to store the lowest index of grill to start checking later
    # max_end same concept but for highest index of grill
    # Both not necessary, but thought that it might save some time (same runtime either way)
    min_start = 43202
    max_end = 1
    for i in range(n):
        d, t = map(int, input().split())
        # Update min_start and max_end
        min_start = min(min_start, t-2*d)
        max_end = max(max_end, t)

        # Because the cook only need to be present at these 3 point of time during the burger process
        # Do not need to be present in between, so just increment 1 at these indices
        # t-2*d for the placing of new patty
        # t-d for flipping
        # t for removing and serving
        grill[t-2*d] += 1
        grill[t-d] += 1
        grill[t] += 1
    
    min_cooks = 1
    for i in range(min_start, max_end+1):
        # Update the minimum number of cooks needed
        # Since a cook can handle 2 patties, do a division and round up
        min_cooks = max(min_cooks, math.ceil(grill[i]/2))

    print(min_cooks)
    

if __name__ == '__main__':
    main()
