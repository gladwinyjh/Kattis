from sys import stdin


def find_buttons(input_grid, triggered_row, triggered_col, r, c):
    for i in range(r):
        for j in range(c):
            # '1'
            if input_grid[i][j] == '1':
                # Case for 'P':
                #   1) This '1' is the only '1' in its row, and there are at least more than 1 '1' in its col
                #   2) Same as above but reverse row and col
                if ((triggered_row[i] == 1 and triggered_col[j] >= 1) or
                    (triggered_row[i] >= 1 and triggered_col[j] == 1)):
                    input_grid[i][j] = 'P'
                
                # Case for 'I':
                #   1) More than 1 '1's in both its row and col
                #       - Can't be 100% that this button is pressed
                elif triggered_row[i] > 1 and triggered_col[j] > 1:
                    input_grid[i][j] = 'I'
                
                # Case for impossible, '1' should be a '0':
                #   1) Row has 0 '1's
                #   2) Col has 0 '1's
                elif ((triggered_row[i] < 1 and triggered_col[j] <= 1) or
                      (triggered_row[i] <= 1 and triggered_col[j] < 1)):
                    return False
            
            # '0'
            else:
                # If there are any '1' on both the same row and column, 
                # then it is impossible since '0' should be '1'
                if triggered_row[i] >= 1 and triggered_col[j] >= 1:
                    return False
                else:
                    input_grid[i][j] = 'N'
    
    return True
 

def main():
    T = int(stdin.readline())
    
    while T:
        r, c = map(int, stdin.readline().split()) 
        
        input_grid = []
        triggered_row = [0] * r
        triggered_col = [0] * c
        for i in range(r):
            row = list(stdin.readline().rstrip())
            for j in range(c):
                # Note down the number of '1's in each row and col
                if row[j] == '1':
                    triggered_row[i] += 1
                    triggered_col[j] += 1
            
            input_grid.append(row)
        
        intepret_grid = find_buttons(input_grid, triggered_row, triggered_col, r, c)
        
        if not intepret_grid:
            # Early exit from find_buttons function when 'impossible'
            print('impossible')
        else:
            [print(''.join(row)) for row in input_grid]
        
        print('-' * 10) 
        T -= 1


if __name__ == '__main__':
    main()