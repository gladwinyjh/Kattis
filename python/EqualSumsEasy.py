from itertools import combinations


def solve(line):
    subsets = {}
    
    # Start from 1 as all are distinct, so cannot have > 1 number that are the same
    for i in range(1, len(line)):
        for combination in combinations(line, i):
            sum_comb = sum(combination)
            if sum_comb in subsets:
                # Found another combination that has the same sum, return both combinations
                return (combination, subsets[sum_comb])
            
            # New sum, store its combination
            subsets[sum_comb] = combination

    return 'Impossible'


def main():
    T = int(input())

    for i in range(1, T+1):
        line = list(map(int, input().split()))[1:]
        ans = solve(line)
        print(f'Case #{i}:')
        if len(ans) == 2:
            [print(*x) for x in ans]
        else:
            print(ans)


if __name__ == '__main__':
    main()
