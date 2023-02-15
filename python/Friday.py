from sys import stdin


def main():
    T = int(stdin.readline())
    
    for i in range(T):
        D, M = map(int, stdin.readline().split())
        
        months = list(map(int, stdin.readline().split()))
        
        # Can't have Friday 13th if there are less than 13 days in the year 
        if D < 13:
            print(0)
            continue
            
        # Count number of F13s
        count = 0
        # Check first month first
        if months[0] >= 13:
            count += 1
        
        # Get the starting day of the next month
        # If Sunday, next_start == 0, monday == 1, etc.. 
        next_start = months[0] % 7
        
        for j in range(1, len(months)):
            # If Sunday and at least 13 days in this month, increment
            if not next_start and months[j] >= 13:
                count += 1

            # Get the starting day of the next month
            # (Starting day of current month + number of days in this month) % 7
            next_start = (next_start + months[j]) % 7
                
        print(count)
    

if __name__ == '__main__':
    main()
    # Friday 13th only can occur for months with at least 13 days 
    # Check the starting day of each month (1st month of the year starts on Sunday always)
        # For the 13th of each month to fall on Friday, the first of the month has to be a Sunday