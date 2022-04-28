class Player():
    def __init__(self):
        self.wins = 0
        self.losses = 0

    def getAverage(self):
        # Undefined: division by 0, so wins + losses == 0
        if self.wins + self.losses == 0:
            print('-')
        else:
            print('{:.3f}'.format(self.wins/(self.wins + self.losses)))


def play(m1, m2):
    # Tie
    if m1 == m2:
        return 0
    
    # Left player wins 
    if ((m1 == 'rock' and m2 == 'scissors') or 
            (m1 == 'scissors' and m2 == 'paper') or
            (m1 == 'paper' and m2 == 'rock')):
        return 1
    
    # Else right player wins
    return 2


def main():
    while True:
        t = input()
        
        if t == '0':
            return
        
        n, k = map(int, t.split())
        
        players = []
        for i in range(n):
            players.append(Player())

        
        for i in range(k*n*(n-1)//2):
            p1, m1, p2, m2 = input().split()
            # Get the outcome of the game
            outcome = play(m1,m2)
            
            # Update each players wins and losses. Ties dont update anything
            if outcome == 1:
                players[int(p1)-1].wins += 1
                players[int(p2)-1].losses += 1

            elif outcome == 2:
                players[int(p1)-1].losses += 1
                players[int(p2)-1].wins += 1
        
        # Print average
        for player in players:
            player.getAverage()
        
        print()


if __name__ == '__main__':
    main()
