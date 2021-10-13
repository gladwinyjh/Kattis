# Team stats are independent
# To find specific stat, follow paths

# Total games played
    # Need wins, draws, losses

# Wins
    # Need total games played, draws, losses OR
        # Wins = total games played - draws - losses
    # Need total points, draws OR
        # Wins = (total points - draws * 1) // 3
    # Need total points, total games played, losses
        # Wins + draws = Total games played - losses
        # Wins*3 + draws = Total points
        # Wins = (Total points - total games played + losses) // 2
    # Total games played, wins, draws are unknown. Need total points, losses

            # Wins*3 + draws = total points
            # Wins = (total_points - 100 + losses) // 2

# Draws
    # Need total games played, wins, losses OR
        # Draws = total games played - wins - losses
    # Need total points, wins
        # Draws = (total points - wins * 3) / 1

# Losses
    # Need total games played, wins, draws OR
        # Losses = total games played - wins - draws
    # Need total points, wins, draws
        # Losses = total points - wins * 3 - draws * 1

# Total points
    # Need wins, draws
        # wins * 3 + draws * 1

# Special case: 0 games played
    # Sets all to 0

# Special case: Team loses all games, need total games played, losses
    # If team loses all games, wins, draws, points = 0

# Special case: If total points < 3, there has to be 0 wins. Need total points
    # Draws = total points / 1

# Always continue if not at last if condition, if not stat will be checked more than once

def main():
    n = int(input())

    for i in range(n):
        teamStat = list(input().split())

        # No games played
        if teamStat[0] == '0':
            teamStat[1] = 0
            teamStat[2] = 0
            teamStat[3] = 0
            teamStat[4] = 0
            print(*teamStat)
            continue
        
        # One of wins, draws, losses is 100, then the others are 0 and total games played = 0
        if '100' in teamStat[1:4]:
            index = teamStat[1:4].index('100') + 1
            if index == 1:
                teamStat[2] = 0
                teamStat[3] = 0
            elif index == 2:
                teamStat[1] = 0
                teamStat[3] = 0
            else:
                teamStat[1] = 0
                teamStat[2] = 0
            
            teamStat[0] = 100

        # Special case for if total games played = 100 and 
        # Only 1 draw or 1 loss and the rest are wins
        # Because more than 1 will result in multiple solutions
        if teamStat[4] == '300':
            teamStat[0] = 100
            teamStat[1] = 100
            teamStat[2] = 0
            teamStat[3] = 0
            print(*teamStat)
            continue

        elif teamStat[4] == '298':
            teamStat[0] = 100
            teamStat[1] = 99
            teamStat[2] = 1
            teamStat[3] = 0
            print(*teamStat)
            continue
        elif teamStat[4] == '297':
            teamStat[0] = 100
            teamStat[1] = 99
            teamStat[2] = 0
            teamStat[3] = 1
            print(*teamStat)
            continue

        # Special case: all losses
        # Put here so that int(teamStat[4]) < 3 won't get triggered since int('?') cannot be compared to 3
        if teamStat[0] == teamStat[3] != '?':
            teamStat[1] = 0
            teamStat[2] = 0
            teamStat[4] = 0

        d = {}
        for j, val in enumerate(teamStat):
            if val == '?':
                d[j] = val

        # Check if any 2 (wins, draws, losses) = 100, then the other is 0
        if 1 in d and 2 not in d and 3 not in d:
            if int(teamStat[2]) + int(teamStat[3]) == 100:
                teamStat[1] = 0
                del d[1]
        
        elif 2 in d and 1 not in d and 3 not in d:
            if int(teamStat[1]) + int(teamStat[3]) == 100:
                teamStat[2] = 0
                del d[2]
        
        elif 3 in d and 1 not in d and 2 not in d:
            if int(teamStat[1]) + int(teamStat[2]) == 100:
                teamStat[3] = 0
                del d[3]

        while d:
            if 4 not in d:
                # If no points, wins + draw = 0
                if int(teamStat[4]) == 0:
                    # If stat was '?'
                    if 1 in d:
                        teamStat[1] = 0
                        del d[1]
                    if 2 in d:
                        teamStat[2] = 0
                        del d[2]
                # Special case: total points < 3. Points can't be negative so don't need lower bound
                elif int(teamStat[4]) < 3:
                    # If stat was '?'
                    if 1 in d:
                        teamStat[1] = 0
                        del d[1]
                    if 2 in d:
                        teamStat[2] = int(teamStat[4])
                        del d[2]

            if teamStat[0] == '?' and 1 not in d and 2 not in d and 3 not in d:
                teamStat[0] = int(teamStat[1]) + int(teamStat[2]) + int(teamStat[3])
                del d[0]
            
            if teamStat[1] == '?':
                if 0 not in d and 2 not in d and 3 not in d:
                    teamStat[1] = int(teamStat[0]) - int(teamStat[2]) - int(teamStat[3])
                    del d[1]
                    continue

                if 2 not in d and 4 not in d:
                    teamStat[1] = (int(teamStat[4]) - int(teamStat[2]))//3 # // to get rid of decimal point
                    del d[1]
                    continue

                if 0 not in d and 3 not in d and 4 not in d:
                    teamStat[1] = (int(teamStat[4]) - int(teamStat[0]) + int(teamStat[3]))//2
                    del d[1]
                    continue
                
                if 2 in d:
                    teamStat[1] = int(teamStat[4]) // 3
                    teamStat[2] = int(teamStat[4]) - teamStat[1] * 3
                    del d[1]
                    del d[2]
                    
                    if 0 in d and 3 not in d:
                        teamStat[0] = teamStat[1] + teamStat[2] + int(teamStat[3])
                        del d[0]
                        break
                    elif 3 in d and 0 not in d:
                        teamStat[3] = int(teamStat[0]) - teamStat[1] - teamStat[2]
                        del d[3]
                        break

            if teamStat[2] == '?':
                if 0 not in d and 1 not in d and 3 not in d:
                    teamStat[2] = int(teamStat[0]) - int(teamStat[1]) - int(teamStat[3])
                    del d[2]
                    continue

                if 1 not in d and 4 not in d:
                    teamStat[2] = int(teamStat[4]) - int(teamStat[1])*3
                    del d[2]
                    continue

            if teamStat[3] == '?':
                if 0 not in d and 1 not in d and 2 not in d:
                    teamStat[3] = int(teamStat[0]) - int(teamStat[1]) - int(teamStat[2])
                    del d[3]
                    continue

                if 1 not in d and 2 not in d and 4 not in d:
                    teamStat[3] = int(teamStat[4]) - int(teamStat[1])*3 - int(teamStat[2])
                    del d[3]
            
            if teamStat[4] == '?' and 1 not in d and 2 not in d:
                teamStat[4] = int(teamStat[1])*3 + int(teamStat[2])
                del d[4]

        print(*teamStat)

if __name__ == '__main__':
    main()