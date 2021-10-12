def main():
    numberofScores = int(input())
    timeH = 0
    timeA = 0
    
    homeScore = 0
    awayScore = 0

    for i in range(numberofScores):
        team, points, timeScored = input().split()
        points = int(points)
        min, sec = map(int, timeScored.split(':'))
        timeScoredSeconds = min * 60 + sec

        # This if and elif statement will only trigger after 1st score
        # prevTimeScored will have a value by then
        if homeScore > awayScore:
            # Duration in which Home team has been in the lead
            timeH += timeScoredSeconds - prevTimeScored
        elif awayScore > homeScore:
            # Duration in which Away team has been in the lead
            timeA += timeScoredSeconds - prevTimeScored

        # Record previous score timing
        prevTimeScored = timeScoredSeconds

        # Add score here as 
        # adding it in front will screw up if statement
        if team == 'H':
            homeScore += points
        else:
            awayScore += points

    # If last score recorded, check for total scores
    # If draw, dont add time to any team
    if homeScore > awayScore:
        timeH += 32*60 - timeScoredSeconds
    elif homeScore < awayScore:
        timeA += 32*60 - timeScoredSeconds


    # Convert time back to correct format
    timeHMinutes, timeHSeconds = str(timeH // 60), str(timeH % 60)
    timeAMinutes, timeASeconds = str(timeA // 60), str(timeA % 60)

    # Set one leading 0 if seconds < 10
    if int(timeHSeconds) < 10:
        timeHSeconds = timeHSeconds.zfill(2)

    if int(timeASeconds) < 10:
        timeASeconds = timeASeconds.zfill(2)


    if homeScore > awayScore:
        print('H', timeHMinutes + ':' + timeHSeconds, timeAMinutes + ':' + timeASeconds)
    else:
        print('A', timeHMinutes + ':' + timeHSeconds, timeAMinutes + ':' + timeASeconds)
        

if __name__ == '__main__':
    main()