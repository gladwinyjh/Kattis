from sys import stdin


def main():
    N, S, R = map(int, stdin.readline().split())
    
    damaged = set(map(int, stdin.readline().split()))

    reserve = list(map(int, stdin.readline().split()))
    
    # Check to replace team-1 kayak first before team+1 kayak
    for team in reserve:
        if team in damaged:
            # 1st priority is to replace own team's kayak
            damaged.remove(team)
        elif team-1 in damaged:
            damaged.remove(team-1)
        elif team+1 in damaged:
            damaged.remove(team+1)

    print(len(damaged))


if __name__ == '__main__':
    main()
