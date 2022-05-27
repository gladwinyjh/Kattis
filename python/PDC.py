def find_PDC(N, v, mem):
    # Number of combinations = 1 when:
        # v == 0: No descents -> Only 1 case when set is in ascending order
        # v == N-1: Only 1 case when set is in descending order 
    if v == 0 or v == N - 1:
        return 1

    if mem[N][v] > 0:
        # Previous PDC already set, so just return it
        return mem[N][v]

    # From a N-1 to N, we can either maintain the same number of v((N-1, v) -> (N, v)) or increase it by 1 ((N-1, v-1) -> (N, v))
        # Case 1 Same v: Put next n between any 2 elements that already form a descent or put it at the end of the set
        # Case 2 Increase by 1: Put next n in the front of the set or between 2 elements that do not form a descent
    # To get the number of permutations for a given N and v:
        # Case 1:
            # There are a total of v descents. So we only have these v descents to choose from to insert n 
            # + 1 because we can put n at the end of the set
            # So total (v+1) ways. But find_PDC returns the number of permutations, so for each permutation there are (v+1) ways, so multiply
        
        # Case 2:
            # For a permutation with v descents, there are a total of (N-1) - v remaining slots where left and right elements dont form a descent
            # + 1 because we can put n at the front of the set too
            # So total = (N-1) - v + 1 = (N - v) ways. Then multiply because above logic from Case 1 applies
    mem[N][v] = ((v+1) * find_PDC(N-1, v, mem) + (N-v) * find_PDC(N-1, v-1, mem)) % 1001113

    return mem[N][v]
   

def main():
    P = int(input())
    mem = [[0] * 100 for _ in range(101)]

    for i in range(P):
        K, N, v = map(int, input().split())
        print(K, find_PDC(N, v, mem))


if __name__ == '__main__':
    main()