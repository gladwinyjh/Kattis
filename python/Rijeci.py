def main():
    K = int(input())
    
    if K == 1:
        print(0, 1)
        return

    # 0 to K presses, so total K+1
    mem = [(0, 0)] * (K + 1)

    # Base cases:
        # 0 presses: 1 A, 0 B
        # 1 press: 0 A, 1 B
    mem[0] = (1, 0)
    mem[1] = (0, 1)

    for i in range(2, K+1):
        # Fibonnaci sequence: current = addition of 2 previous
        # Do all the way to K presses
        mem[i] = (mem[i-1][0]+mem[i-2][0], mem[i-1][1]+mem[i-2][1])
    
    print(mem[K][0], mem[K][1])


if __name__ == '__main__':
    main()