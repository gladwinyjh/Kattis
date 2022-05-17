def main():
    m, l = map(int, input().split())
    M, L = map(int, input().split())
    t_m, t_l = map(int, input().split())

    # Go through all possible cases
    
    # l between m and starting point
    # bring l to m 
        # Because if it will either bring l closer to L or it wouldnt make any difference
        # Ex: 0...l....m....M....L -> bringing l towards m reduces time
        #   : L...0....l....m....M -> no difference because we still need to traverse to the left
        #   : 0...L....l....m....M -> no difference same as above
        #   : 0...l....L....m....M -> bringing l towards m reduces time
        #   : 0...l....m....L....M -> bringing l towards m reduces time
    if 0 >= l >= m or m >= l >= 0:
        time_m = abs(l) + abs(m-l) + abs(M-m)
        time_l = time_m + abs(m-M) + abs(L-m)

        if time_m <= t_m and time_l <= t_l:
            print('possible')
            return
    
    # m between l and starting point
    # bring m to l
        # Reasoning similar to above
    if 0 >= m >= l or l >= m >= 0:
        time_l = abs(m) + abs(l-m) + abs(L-l)
        time_m = time_l + abs(l-L) + abs(M-l)

        if time_m <= t_m and time_l <= t_l:
            print('possible')
            return
    
    # Last 2 are general cases

    # Get m first then l
    time_m = abs(m) + abs(M-m)
    time_l = time_m + abs(l-M) + abs(L-l)
    
    if time_m <= t_m and time_l <= t_l:
        print('possible')
        return 
    
    # Get l first then m
    time_l = abs(l) + abs(L-l)
    time_m = time_l + abs(m-L) + abs(M-m)

    if time_m <= t_m and time_l <= t_l:
        print('possible')
        return
    
    # All cases are impossible
    print('impossible')


if __name__ == '__main__':
    main()
