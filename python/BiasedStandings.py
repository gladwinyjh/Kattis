def main():
    t = int(input())

    for i in range(t):
        _ = input()
        n = int(input())
        # Dictionary to store preferred standings
        preferred = {}

        for j in range(n):
            # Name of team is trivial
            _, place = input().split()
            # Store preferred standings in dictionary
            if int(place) in preferred:
                preferred[int(place)] += 1
            else:
                preferred[int(place)] = 1
        
        # List to store standings that were not preferred by any team
        left = []
        for j in range(1, n+1):
            if j in preferred:
                # One team gets to be in this standing
                # Since there can be multiple teams that desire this standing, -1
                preferred[j] -= 1
            else:
                left.append(j)

        # List to store the number of standings remaining after assigning standings to teams
        leftovers = []
        for key, val in preferred.items():
            for _ in range(val):
                leftovers.append(key)

        # Sort leftovers list
        sortedLeftovers = sorted(leftovers)
        badness = 0
        for j in range(len(sortedLeftovers)):
            # Get the absolute difference between remaining standings to be filled and preferred standings
            badness += abs(sortedLeftovers[j]-left[j])

        print(badness)


if __name__ == '__main__':
    main()