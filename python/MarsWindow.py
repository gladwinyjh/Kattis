from sys import stdin


def main():
    y = int(stdin.readline())
    
    upper_diff = ((y - 2018) * 12) + 9
    
    # Check difference between normal float division and floor division
    # If <= 12/26, then the lower bound (i.e start of the year) must be at least within range
    if (upper_diff / 26 - upper_diff // 26) <= 12/26:
        print('yes')
    else:
        print('no')
    
    
if __name__ == '__main__':
    main()
    # EX: 2020: year difference in months = 24 months
        # Because month starts in april, actual month difference + 8 + 1 = 33 months
            # + 1 because to include same month
        # This includes the entire year, so the range of window is actually 32-12 to 32 months away
            # 20 to 32 months window
        
        # Check if x number of complete cycles fall within this window
        # 26 * x = 20 to 32
        # Divide both sides by 20, x = 0.76 to 1.23
        # Since x can only be an integer, x can be 1, so 2020 window is valid
        # Note that the range is 32/26 - 20/26 = 12/26
            # So just need to check upper bound (i.e 33 months here)
        
        # Because the difference can only be 12/26 or ~ 0.46 below the upper bound,
        # take the floor division and check if the difference between the normal division
        # and floor division is equal or below 0.46, because the lower bound must be below or equal to that
       
       
    # Another easier way is to just keep progressing the months from april 2018 at 26 months a time
    # and check if the target year is reached  