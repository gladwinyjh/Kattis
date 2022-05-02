from collections import deque


def main():
    cases = int(input())

    for i in range(cases):
        n, t, m = map(int, input().split())
        # List of time at which each car will be unloaded by index 
        cars_unloaded = [-1]*m
        left_bank = deque()
        right_bank = deque()

        for j in range(m):
            arr, bank = input().split()
            
            if bank == 'left':
                left_bank.append((j, int(arr)))
            else:
                right_bank.append((j, int(arr)))
        
        # Elasped time
        elapsed = 0
        # Ferry to store cars
        ferry = []
        # Banks and location of ferry
        banks = [left_bank, right_bank]
        loc = False
        
        while left_bank or right_bank:
            # If ferry is currently loaded, unload cars and update their times in cars_unloaded
            while len(ferry) > 0:
                cars_unloaded[ferry.pop()] = elapsed
                
            # If there are cars on the current bank
            # Load until full or no cars on current bank
            if banks[loc]:
                # Load current cars waiting at the bank
                while banks[loc] and banks[loc][0][1] <= elapsed and len(ferry) < n:
                    ferry.append(banks[loc].popleft()[0])

            if len(ferry) != 0:
                # There are cars waiting at the current bank
                # Bring them over to the other bank
                elapsed += t
                loc = not loc
            else:
                # Next car arriving on current bank is > elapsed.
                # Fast forward to that time since there will be no more cars on other bank
                if banks[loc] and not banks[not loc]:
                    elapsed = banks[loc][0][1]
                    continue
                
                # No more cars arriving on this bank
                # If there are already cars before travelling to other bank, then no need to: elapsed + t
                # Else there are no cars yet, wait for a car to arrive, then travel: banks[not loc][0][1] + t
                if not banks[loc] and banks[not loc]:
                    elapsed = max(elapsed + t, banks[not loc][0][1] + t)
                    loc = not loc
                    continue

                # Next car arrives at current bank earlier than next car arrives at other bank
                # Wait until that car comes at this bank
                if banks[loc][0][1] <= banks[not loc][0][1]:
                    elapsed = banks[loc][0][1]
                else:
                    # If the car is already on the other bank, travel there directly: elapsed + t
                    # Else, wait for the car to arrive before travelling across: banks[not loc][0][1] + t
                    elapsed = max(elapsed + t, banks[not loc][0][1] + t)
                    loc = not loc 
        
        # Unload remaining cars on ferry
        while len(ferry) > 0:
            cars_unloaded[ferry.pop()] = elapsed

        print(*cars_unloaded, sep='\n')
        
        # Blank line between outputs
        if i != cases - 1:
            print()


if __name__ == '__main__':
    main()
