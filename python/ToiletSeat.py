def main():
    seatSequence = input()
    length = len(seatSequence)

    # For counting seat adjustments for 3 policies
    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(1, length):
        # Current preference != previous preference
        if seatSequence[i] != seatSequence[i-1]:
            # First user, only need to consider what current user needs to do
            # As there is no previous user
            # If seat preference is same as initial seat condition, do not need to
            # adjust anything
            # else(this case), add 1 to all cases
            if i == 1:
                count1 += 1
                count2 += 1
                count3 += 1

            else:
                # 'D' preferred
                if seatSequence[i-1] == 'U':
                    # First policy, seat will be 'U'
                    # Previous user does not need to adjust 
                    # Current user needs to adjust to 'D'
                    count1 += 1
                
                    # Second policy, seat will be 'D'
                    # Previous user needs to adjust seat to 'D'
                    # Current user do not need to adjust 
                    count2 += 1

                    # Third policy, seat will be 'U'
                    # Previous user does not need to adjust 
                    # Current user needs to adjust to 'D'
                    count3 += 1
                
                # 'U' preferred
                else:
                    # First policy, seat will be 'U'
                    # Previous user needs to set seat up to 'U'
                    # Current user do not need to adjust
                    count1 += 1

                    # Second policy, seat will be 'D'
                    # Previous user do not need to adjust
                    # Current user needs to adjust to 'U'
                    count2 += 1
                    
                    # Third policy, seat will be 'D'
                    # Previous user do not need to adjust 
                    # Current user needs to adjust to 'U'
                    count3 += 1
    
        # Current preference == previous preference
        # No adjustments for first user if it is the same
        elif i != 1:
            # 'U' preferred
            if seatSequence[i-1] == 'U':
                # First policy, seat will be 'U'
                # Previous user does not need to adjust
                # Current user does not need to adjust

                # Second policy, seat will be in 'D'
                # Previous user needs to adjust seat to 'D'
                # Current user needs to adjust seat to 'U'
                count2 += 2

                # Third policy, seat will be in 'U'
                # No adjustments needed

            # 'D' preferred
            else:
                # First policy, seat will be 'U'
                # Previous user needs to adjust seat to 'U'
                # Current user needs to adjust seat to 'D'
                count1 += 2

                # Second policy, seat will be 'D'
                # No adjustments needed

                # Third policy, seat will be 'D'
                # No adjustments needed

        # FOR LAST USER    
        # Because we only considered what previous user needed to do based on policy
        # and what the current user needs to do,
        # We need to consider last user as above test cases do not consider what
        # last person will do after using the toilet seat
        if i == length-1:
            if seatSequence[i] == 'U':
                # First policy, no adjustments needed

                # Second policy, adjust seat to 'D'
                count2 += 1

                # Third policy, no adjustments needed
            
            else:
                # First policy, adjust seat to 'U'
                count1 += 1

                # Second policy, no adjustments needed

                # Third policy, no adjustments needed

    print(count1)
    print(count2)
    print(count3)


if __name__ == '__main__':
    main()