from sys import stdin


def main():
    while True:
        inp = list(map(int, stdin.readline().split()))
        
        # End of input
        if not inp:
            break

        seq = inp[1:]
        n = inp[0]
        
        # Boolean list to check if an absolute difference was previously seen
        elements = [False] * (n-1)
        
        # Boolean flag for jolly condition
        jolly = True
        for i in range(1, n):
            # Absolute difference
            abs_diff = abs(seq[i-1] - seq[i])
            
            # Absolute difference must fall between 1 and n-1 inclusive
            # and it must not be seen before
                # Because if it is seen before, then there are not enough pairs of integers 
                # to satisfy all differences from 1 to n-1
            if abs_diff >= 1 and abs_diff <= n-1 and not elements[abs_diff-1]:
                # Mark the absolute difference as seen
                elements[abs_diff-1] = True
            else:
                jolly = False
                # Dont need to go through further because of reasons stated above
                break

        if jolly:
            print('Jolly')
        else:
            print('Not jolly')


if __name__ == '__main__':
    main()
