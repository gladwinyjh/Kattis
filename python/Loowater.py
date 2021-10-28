# Need to chop of all heads
# Each knight can only chop off one head.
    # Knight height must be >= diameter of head
# Knight paid a wage = one gold coin for each cm of his height
# PQ or sorting

def main():
    while True:
        n, m = map(int, input().split())

        if n == m == 0:
            break

        heads = []
        heights = []

        for i in range(n):
            heads.append(int(input()))
        
        for i in range(m):
            heights.append(int(input()))

        # One knight only can slay one head
        # If more heads than knights, doomed
        if n > m:
            print("Loowater is doomed!")
            continue
        
        # Sort both heads and heights in ascending order
        sortedHeads = sorted(heads)
        sortedHeights = sorted(heights)

        gold = 0
        headSlained = 0
        heightIndex = 0

        # Greedily match each head will smallest possible height 
        for i in range(len(sortedHeads)):
            # If current knight cannot slay current head
            # Current knight will not be able to slay a bigger head
            # So each time we go to a bigger head, 
            # we start from the heightIndex and not from 0
            for j in range(heightIndex, len(sortedHeights)):
                # Go to next knight for next head OR
                # Go to next knight for current head because current knight height too small
                heightIndex += 1
                if sortedHeads[i] > sortedHeights[j]:
                    # Go to next knight
                    continue
                else:
                    headSlained += 1
                    gold += sortedHeights[j]
                    break
        
        # All heads slained
        if headSlained == n:
            print(gold)
        else:
            print("Loowater is doomed!")


if __name__ == '__main__':
    main()