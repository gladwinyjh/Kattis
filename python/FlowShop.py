def main():
    N, M = map(int, input().split())

    times = []
    for i in range(N):
        times.append(list(map(int, input().split())))

    # tot_time stores the total time needed for each swather 1...N
    tot_time = [0] * N

    for j in range(M):
        # Time to make first swather is independent of other swathers
        # Just the sum of its stages
        tot_time[0] += times[0][j]
        
        # Start i from 1 as first swather is calculated alr from above
        for i in range(1,N):
            # At each stage, update time to build ith swather after jth stage:
            # Get max(time to build ith swather at (j-1)th stage, time to build (i-1)th swather after jth stage) + time for jth stage for ith swather
            tot_time[i] = max(tot_time[i], tot_time[i-1]) + times[i][j]

    print(*tot_time)



if __name__ == '__main__':
    main()
