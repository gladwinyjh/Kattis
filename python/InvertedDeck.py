from sys import stdin

def main():
    n = int(input())

    cards = [int(x) for x in stdin.readline().split()]
    
    # Only 1 card in deck, so swap it with itself (0+1, 0+1)
    if len(cards) == 1:
        print(1, 1)
        return
    
    found = False
    i = 0
    while i < len(cards)-1:
        if cards[i] > cards[i+1]:
            if not found:
                # Found first subsequence
                found = True
            else:
                # A contiguous subsequence was already found
                # It is impossible to have more than 1 of them per question
                print('impossible')
                return
            
            # Traverse deck until end of deck or when the next card is more than the current card (ascending, end of subsequence)
            while i < len(cards)-1 and cards[i] >= cards[i+1]:
                i += 1
            
            # Record the last index to be flipped. This is the smallest number in the subsequence
            end = i

            # Reverse traverse deck from that end point till either front of the deck or when the next card [i-1] is smaller than current card
            while i > 0 and cards[i] <= cards[i-1]:
                i -= 1
            
            # Current i is the start of the subsequence. This is the largest number in the subsequence
            start = i
            
            # Check if the card before the start is larger than the last card in the subsequence, if i > 0 as cards[start-1] will wrap
            # Ex: [3, 5, 4, 3, 1, 6] --> sequence = [5, 4, 3, 1]. If flipped: [3, 1, 3, 4, 5, 6] NOT VALID
            # because cards[start-1] == 3 and cards[end] == 1
            if i > 0 and cards[start-1] > cards[end]:
                print('impossible')
                return
            
            # We are done with this subsequence and want to check for any more subsequences further down
            # So change i back to end where it was at before
            i = end

        i += 1

    if not found:
        # List is sorted, so just take any of the same index to swap
        print(1, 1)
    else:
        # Rarities start from 1, so add 1
        print(start+1, end+1)


if __name__ == '__main__':
    main()
