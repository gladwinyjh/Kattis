def find_min(k, start, end, mem):
    if k == 1:
        # One mailbox remaining, no choice but to test from from current bottom to top bounds
        return (end*(end+1)//2 - start*(start+1)//2)

    if start == end:
        # Attainable in scenario 1 when the top bound end is decremented or in scenario 2 when i is incremented till it reaches end
        # When start == end, there is no need to test further as the number of additional crackers needed is 0
        # You want to check if u can fit 'start' number of crackers into a mailbox with limit of 'end', and start == end.
        return 0

    if (k, start, end) not in mem:
        res = float('inf')
        # Range of number of crackers we want to cover is from 0 to m. Top bound is m because mailbox cannot fit more than m anyways
        # We essentially keep guessing that the number of crackers needed to destroy the mailbox be i
        # Then 2 scenarios happen
            # 1) Mailbox gets destroyed, we lose 1 mailbox(k-1), and we start testing downwards from i-1 crackers
            # 2) Mailbox does not get destroyed, continue testing up
        for i in range(start+1, end+1):
            res = min(res, i + max(find_min(k-1, start, i-1, mem), find_min(k, i, end, mem)))
        
        mem[(k, start, end)] = res
    
    return mem[(k, start, end)]


def main():
    N = int(input())
    mem = {}

    for i in range(N):
        k, m = map(int, input().split())
        print(find_min(k, 0, m, mem))


if __name__ == '__main__':
    main()
