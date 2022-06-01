from sys import stdin


def solve(inp, i, j, mem):
    # i keeps track of the the index of the input string
    # j keeps track of the target string 
        # Can also be viewed as how many char into 'welcome to code jam' is attained

    # Base case 1: j reaches the end of the target string:
        # Valid subsequence found in inp
    if j == len(target):
        return 1
    
    # Base case 2: i reaches the end of the input string, but before a complete subsequence is found
    if i == len(inp):
        return 0
    
    # Already calculated previously
    if mem[i][j] != -1:
        return mem[i][j]
    
    # Intialise with 0
    mem[i][j] = 0
    for k in range(i, len(inp)):
        # Character at k of inp matches character j of target
        if inp[k] == target[j]:
            # Move to the next character of inp and target
            # Modulo here because value may overflow before finished calculations
            mem[i][j] += solve(inp, k+1, j+1, mem) % 10000

    return mem[i][j]


def main():
    global target
    target = 'welcome to code jam'
    T = int(stdin.readline())

    for i in range(1, T+1):
        inp = stdin.readline()
        # If input string is not as long as target, no chance there will be a subsequence
        if len(inp) < len(target): 
            print(f'Case #{i}: 0000')
            continue
        
        mem = [[-1] * (len(target)+1) for _ in range(len(inp)+1)]
        ans = solve(inp, 0, 0, mem)
        print(f'Case #{i}: {ans:04}')


if __name__ == '__main__':
    main()
