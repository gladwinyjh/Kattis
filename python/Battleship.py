def main():
    t = int(input())

    for i in range(t):
        fleets = []
        ships = []

        w, h, n = map(int, input().split())
        
        # Stores the fleet maps for players one and two in fleets list
        for j in range(2):
            player = []
            for j in range(h):
                player.append(list(input()))
            
            # Counts the number of ships for the player and append to ships
            ships.append(sum(row.count('#') for row in player))
            fleets.append(player)

        shotOrders = []
        for j in range(n):
            shotOrders.append(list(map(int, input().split())))
        
        # In python, True == 1 and False == 0
        # We can use that to access the different players since there are only 2 of them, by using 'not'
        playerTargeted = True
        for j in range(len(shotOrders)):
            x, y = shotOrders[j]
            
            # Shot hit ship
            if fleets[playerTargeted][h-1-y][x] == '#':
                # Reduced the number of ships for the targeted player
                ships[playerTargeted] -= 1
                # Set the cell on the map to be empty
                fleets[playerTargeted][h-1-y][x] = '_'
                 
                if ships[playerTargeted] == 0:
                    # If targeted player is player two, player two still has 1 more chance to shoot
                    # If targeted player is player one, then this is currently player one's last chance to shoot
                        # So no more shots after this. Theoretically, this should be the last shot of the game
                    if playerTargeted:
                        playerTargeted = not playerTargeted
                    else:
                        break
                    
            else:
                # Enters else statement if shot missed. Change players
                playerTargeted = not playerTargeted

        if ships[0] == 0 and ships[1] != 0:
            print('player two wins')
        elif ships[0] != 0 and ships[1] == 0:
            print('player one wins')
        else:
            print('draw')


if __name__ == '__main__':
    main()
