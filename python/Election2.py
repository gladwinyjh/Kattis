def main():
    candidates = {}
    n = int(input())
    # Store candidates and their parties in a dictionary
    for i in range(n):
        candidate = input()
        party = input()
        candidates[candidate] = party

    votes = {}
    m = int(input())
    # If there are no votes, then it is a tie
    if m == 0:
        print('tie')
        return
    
    max_vote = 0
    # Record the maximum number of votes for a candidate
    for i in range(m):
        candidate = input()
        if candidate in candidates:
            votes[candidate] = votes.get(candidate, 0) + 1
            max_vote = max(max_vote, votes[candidate])
    
    # All votes are given to candidates that do not belong to dictionary, tie
    if not votes:
        print('tie')
        return

    found_winner = -1
    for candidate, votes in votes.items():
        if votes == max_vote:
            if found_winner == -1:
                # Found first winner
                found_winner = candidate
            else:
                # Found more than 1 winner, tie
                print('tie')
                return
    
    print(candidates[found_winner])


if __name__ == '__main__':
    main()
