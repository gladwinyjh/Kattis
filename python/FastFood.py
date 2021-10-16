# From sample inputs, assume that sticker types completely do not overlap
    # A specific sticker type cannot be part of 2 prizes
def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        # List to store sticker types for each prize
            # Each index corresponds to a prize. At each index is a list of sticker types
        prizeList = []
        # List to store cash prize money for each prize
        cashList = []
        for j in range(n):
            prize = list(map(int, input().split()))
            k = prize[0]
            prizeList.append(prize[1:k+1])
            cashList.append(prize[-1])
        # Store stickers coach has
        stickers = list(map(int, input().split()))
        cashClaimed = 0

        # For a given prize, retrieve the sticker types needed
        for j in range(len(prizeList)):
            # No more than 100 stickers of each type
            minStickers = 100
            # Find the minimum number of stickers
                # This quantity is the bottleneck from claiming more of this prize
                    # Ex: If prize requires sticker [1, 2] 
                        # and you only have 3 of sticker 1, and 2 of sticker 2,
                        # you cannot claim more than 2 of this prize
            for sticker in prizeList[j]:
                # Quantity of current sticker type is less than the max number of stickers
                # [sticker-1] because stickers start from 1 and not 0
                if stickers[sticker-1] < minStickers:
                    minStickers = stickers[sticker-1]

            # Get the cash to be claimed for this prize
            cashClaimed += minStickers * cashList[j]
        
        print(cashClaimed)


if __name__ == '__main__':
    main()