def main():
    n, p, m = map(int, input().split())
    # Dictionary to store (player name: points)
    players = {}
    # Set to store all winners
    winners = set()
    
    # Name does not matter
    for i in range(n):
        _ = input()

    for i in range(m):
        player, points = input().split()
        
        # If player has already won, go to next line
        if player in winners:
            continue
        
        # Initialise 0 value for player if player does not exist in dictionary
        # Else add the points to the value
        players[player] = players.get(player, 0) + int(points)
        
        # Meet the minimum points p
        if players[player] >= p:
            winners.add(player)
            print(f'{player} wins!')
    
    # No winners if set is empty
    if not winners:
        print('No winner!')


if __name__ == '__main__':
    main()
