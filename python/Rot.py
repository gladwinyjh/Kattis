from sys import stdin


def main():
    R, C = map(int, stdin.readline().split())

    table = []
    for i in range(R):
        table.append(list(stdin.readline().rstrip()))

    angle = int(stdin.readline())
    
    # Same for 0 deg and 360 deg: just print row
    if angle == 0 or angle == 360:
        [print(''.join(row)) for row in table]
    
    # 90 deg: for each row from the back, print each cell going up a row each time
    # Hit top of row: end of loop, go next column
    elif angle == 90:
        for i in range(C):
            for j in range(R-1, -1, -1):
                print(table[j][i], end='')

            print()
    
    # 180 deg: Reverse table and reverse row
    elif angle == 180:
        [print(''.join(reversed(row))) for row in reversed(table)]
    
    # 270 deg: Similar to 90 deg, but go through rows inside of reverse columns
    elif angle == 270:
        for i in range(C-1, -1, -1):
            for j in range(R):
                print(table[j][i], end='')

            print()
    
    # For 45/135/225/315 angles, find the starting position for each of the rows/col
        # Store the starting positions as will need to refer back to it for the start of each word
    # With a new table of ' ', replace with appropriate letter
    # Increment or decrement row and col to get to position
        # Ex: 45 deg -> 1 row down, 1 col down each letter in each row in table
    

    elif angle == 45:
        new_table = [[' '] * (R+C-1) for _ in range(R+C-1)]
        start_col = R-1
        for i in range(R):
            # new_row follows i here because words are printed from exactly the top of the table
            new_row = i
            # Starting column of CURRENT WORD
            new_col = start_col
            for j in range(C):
                new_table[new_row][new_col] = table[i][j]
                # Next letter in word is 1 down, 1 right
                new_row += 1
                new_col += 1
            
            # Starting column of next word is one col back from current word
            start_col -= 1
        
        [print(''.join(row)) for row in new_table]

    elif angle == 135:
        new_table = [[' '] * (R+C-1) for _ in range(R+C-1)]
        start_col = R-1
        start_row = R+C-2
        for i in range(R):
            new_row = start_row
            new_col = start_col
            for j in range(C-1, -1, -1):
                new_table[new_row][new_col] = table[i][j]
                new_row -= 1
                new_col += 1

            start_col -= 1
            start_row -= 1
        
        [print(''.join(row)) for row in new_table]

    elif angle == 225:
        new_table = [[' '] * (R+C-1) for _ in range(R+C-1)]
        start_col = 0
        start_row = R-1
        for i in range(R):
            new_row = start_row
            new_col = start_col
            for j in range(C-1, -1, -1):
                new_table[new_row][new_col] = table[i][j]
                new_row += 1
                new_col += 1

            start_col += 1
            start_row -= 1
        
        [print(''.join(row)) for row in new_table]

    elif angle == 315:
        new_table = [[' '] * (R+C-1) for _ in range(R+C-1)]
        start_col = 0
        start_row = C-1
        for i in range(R):
            new_row = start_row
            new_col = start_col
            for j in range(C):
                new_table[new_row][new_col] = table[i][j]
                new_row -= 1
                new_col += 1

            start_col += 1
            start_row += 1
        
        [print(''.join(row)) for row in new_table]


if __name__ == '__main__':
    main()
