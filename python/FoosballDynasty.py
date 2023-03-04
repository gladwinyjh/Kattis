from sys import stdin
from collections import deque, defaultdict


def main():
    n = int(stdin.readline())
    
    white = deque([])
    black = deque([])

    line = deque(list(stdin.readline().split()))
    points = stdin.readline().rstrip()
    
    # Load up initial teams
    white.append(line.popleft())
    black.append(line.popleft())
    white.append(line.popleft())
    black.append(line.popleft())

    # Track which player arrives to the team first
    white_first = white[0]
    white_second = white[1]
    black_first = black[0]
    black_second = black[1]
    
    # Dictionary to store teams with the highest streak
    # Key: Streak number, Val: list of teams that have this streak
    streaks = defaultdict(list)

    # Track the team that won the previous round
    prev_winning_team = None

    # Current streak of the winning team
    streak = 0
    # Max streak seen
    max_streak = 0

    for i in range(len(points)):
        if points[i] == 'W':
            # Winning team with order preserved
            winning_team = (white_first, white_second)
            
            # Current team won previous round 
            if prev_winning_team and prev_winning_team == winning_team:
                # Increase streak
                streak += 1
                # If this is the last round, add this team and streak to dictionary
                if i == len(points) - 1:
                    streaks[streak].append(winning_team)
            
            # No previous winner, this is the first round
            elif not prev_winning_team:
                streak = 1
            
            # Previous winning team is not the same as current team
            # Add previous team and streak to dictionary
            else:
                streaks[streak].append(prev_winning_team)
                # Reset streak for current team
                streak = 1
                # If last round, add this team and streak to dictionary
                if i == len(points) - 1:
                    streaks[streak].append(winning_team)
            
            # Update previous winning team to current team for next round
            prev_winning_team = winning_team

            # Swap white team offense and defense
            white.reverse()

            # Change black's team
            line.append(black.pop())
            black.appendleft(line.popleft())

            # Older player goes to defense(index 1)
            # Newer player goes to offense(index 0)
            black_first = black[1]
            black_second = black[0]
        
        # Black won this round
        # Same process as above (maybe can make code cleaner and shorter)
        else:
            winning_team = (black_first, black_second)

            if prev_winning_team and prev_winning_team == winning_team:
                streak += 1
                if i == len(points) - 1:
                    streaks[streak].append(winning_team)

            elif not prev_winning_team:
                streak = 1
            else:
                streaks[streak].append(prev_winning_team)
                streak = 1
                if i == len(points) - 1:
                    streaks[streak].append(winning_team)

            prev_winning_team = winning_team

            black.reverse()
            line.append(white.pop())
            white.appendleft(line.popleft())

            white_first = white[1]
            white_second = white[0]
        
        # Update max streak
        if max_streak < streak:
            max_streak = streak
    
    for team in streaks[max_streak]:
        # Print out teams that have the max streak
        print(*team)


if __name__ == '__main__':
    main()
