import bisect
from sys import stdin


def main():
    N, H = map(int, stdin.readline().split())
    stalag = []
    stalac = []
    
    for i in range(N):
        height = int(stdin.readline())
        if i % 2 == 0:
            # Stalagmites are even
            stalag.append(height)
        else:
            # Stalacmites are odd
            stalac.append(height)

    # Firefly will hit all obstacles >= a certain height regardless of their ordering
    # So sort them and find the number of collisions
    stalac.sort()
    stalag.sort()

    best = N
    num_levels = 0
    for i in range(H):
        # Find the number of collisions using binary search
        # The height of the obstacles start from 1, so add 1 to i
        top_collisions = len(stalac) - bisect.bisect_left(stalac, i+1)
        bot_collisions = len(stalag) - bisect.bisect_left(stalag, H-i)
        collisions = top_collisions + bot_collisions

        if collisions < best:
            # Found new minimum collisions
            best = collisions
            num_levels = 1
        elif collisions == best:
            # Found exisiting minimum
            num_levels += 1
    
    print(best, num_levels)


if __name__ == '__main__':
    main()