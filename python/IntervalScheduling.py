from sys import stdin


def main():
    n = int(stdin.readline())
    intervals = []
    for i in range(n):
        start, end = map(int, stdin.readline().split())
        intervals.append((start, end))
    
    # Sort intervals based on ascending order of end times
    intervals.sort(key=lambda x: x[1])
    
    count = 1
    # Record end time of last interval
    # Intially is the first one
    last_end = intervals[0][1]
    for i in range(1, n):
        # End time of last interval is <= start time of next interval 
        if last_end <= intervals[i][0]:
            # Set end time of last interval to be end time of current interval
            last_end = intervals[i][1]
            count += 1

    print(count)


if __name__ == '__main__':
    main()
