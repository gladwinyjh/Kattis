from sys import stdin


def main():
    n, m = map(int, stdin.readline().split())
    
    # Gnomes status from 1 to n
    gnomes = [1] * (n+1)
    
    taken_list = [] 
    # Mark and record which gnomes are taken
    for i in range(m):
        removed = int(stdin.readline())
        taken_list.append(removed)
        gnomes[removed] = 0
    
    # We want to print the gnome that is before the next gnome on the taken_list, then print the next gnome on the taken list
    # Repeat until no more gnomes on the taken list
    # Use 'next_gnome' to define our search range each iteration
    # Ex: Sample Input 1
        # taken_list = [1, 4, 2]

        # First iteration: taken_list[i] = 1, next_gnome = 1, gnomes[next_gnome] = 1
            # Do not enter inner for loop
            # print(taken_list[i]) = 1

        # Second iteration: taken_list[i] = 4, next_gnome = 1, gnomes[next_gnome] = 1
            # Enter inner for loop for j in range(1, 4)
                # If gnome not taken gnomes[j] == 1, it has not been printed yet because we print taken gnomes first
                    # So we print it print(j), and increment next_gnome
                
                # In this case: gnomes[1] == 0 -> gnomes[2] == 0 -> gnomes[3] == 1
                    # So we print 3
        
        # Repeat until end of taken_list
        
        # Any remaining gnomes are within gnomes[next_gnome:], print those that are not taken(printed)

                
    next_gnome = 1
    for i in range(len(taken_list)):
        for j in range(next_gnome, taken_list[i]):
            if gnomes[j] == 1:
                print(j)

            next_gnome += 1

        print(taken_list[i])

    
    [print(next_gnome + idx) for idx, val in enumerate(gnomes[next_gnome:]) if val == 1]


if __name__ == '__main__':
    main()
