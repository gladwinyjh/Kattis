def findWinner(state, c):
    wins = 0
    for i in range(3):
        # Check if row contains same character
        row_set = set(state[i])
        if len(row_set) == 1 and c in row_set: 
            wins += 1

        # Check if columns contain same character
        col_set = set([row[i] for row in state])
        if len(col_set) == 1 and c in col_set:
            wins += 1
        
        # Check for diagonal lines
        if i == 0 and state[i][0] == state[1][1] == state[2][2] == c:
            wins += 1

        if i == 2 and state[i][0] == state[1][1] == state[0][2] == c:
            wins += 1
        
        # More than two win states = not possible because that will mean > 5 of this character is needed
        if wins > 2:
            return wins
    
    # If wins == 0, player does not have a line
    return wins


def main(): 
    N = int(input())

    for i in range(N):
        curr_state = []
        
        # Count the number of Xs and Os
        # Store game state in curr_state variable
        numX = 0
        numO = 0
        for j in range(3):
            row = input()
            numX += row.count('X')
            numO += row.count('O')

            curr_state.append(list(row))
        
        # findWinner function finds the number of Xs or number of Os that occupy the entire line
        state_X = findWinner(curr_state, 'X')
        state_O = findWinner(curr_state, 'O')

        # Cannot have more Os than Xs under any circumstance and num of Xs can only be at most one more than num of Os
        if numO > numX or numX - numO > 1:
            print('no')

        elif ((state_X >= 1 and state_O == 0 and numX > numO) or 
                (state_O == 1 and state_X == 0 and numO == numX) or 
                (state_X == 0 and state_O == 0)):
            """  
            Conditions for valid state:
                1) At least 1 line of Xs, 0 lines of Os, and number of Xs > number of Os
                    - state_X can take max value of 2, when the last X placed fills 2 lines (giving a total of 5Xs and 4 Os)
                    - Last condition because the game will end before the next O can be placed

                2) 1 line of Os, 0 lines of Xs, and number of Xs == number of Os
                    - Impossible for state_O to be more than 1 because then numO > numX
                    - Last condition because game will end before next X is placed, so same number of Xs and Os
                
                3) Tie game or no winner yet 

            """
            print('yes')
        else:
            print('no')

        # Blank line between inputs
        # Store in dummy variable
        if i != N-1:
            _ = input() 


if __name__ == '__main__': 
    main()
