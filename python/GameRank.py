def main():
    rank = 25
    matches = input()
    
    streak = 0
    stars = 0
    for match in matches:
        # Rank cannot change after Legend
        if rank == 'Legend':
            break

        if match == 'W':
            # Increase winning streak
            streak += 1
            # On a >= 3 winning streak, gain 2 stars if rank between 6 and 25
            if streak >= 3 and 6 <= rank <= 25:
                stars += 2
            # Not on winning streak, gain 1 star only
            else:
                stars += 1

        else:
            # Reset winning streak if any
            streak = 0
            # If player on rank 1-20 loses a game, he loses a star
            if rank < 21:
                stars -= 1

        if 21 <= rank <= 25:
            if stars < 0:
                # Cant go below 0 stars
                stars = 0
            
            elif stars > 2:
                # stars on wins will be either 3 or 4
                # 3 stars -> 1 star and down a rank, 4 stars -> 2 stars and down a rank
                stars -= 2
                rank -= 1

        elif 16 <= rank <= 20:
            if stars < 0:
                # Cant drop below rank 20, so reset stars
                if rank == 20:
                    stars = 0
                else:
                    # Drop rank and one star (3-1=2)
                    rank += 1
                    stars = 2
            
            elif stars > 3:
                # Max number of stars == 3, carry excess over to rank below
                stars %= 3
                rank -= 1
        
        elif 11 <= rank <= 15:
            if stars < 0:
                # Drop a rank
                rank += 1
                
                # Possible to drop to rank 16
                # If drop to rank 16, since the max number of stars is 3, stars now is 3-1 = 2
                # Else: stars now is 4-1 = 3
                if rank <= 15:
                    stars = 3
                else:
                    stars = 2

            elif stars > 4:
                # Carry excess over to rank below
                stars %= 4
                rank -= 1
        
        elif 1 <= rank <= 10:
            if stars < 0:
                rank += 1
                
                # Same logic as when 11 <= rank <= 15
                if rank <= 10:
                    stars = 4
                else:
                    stars = 3

            elif stars > 5:
                # Legend rank if rank before was 1
                if rank == 1:
                    rank = 'Legend'
                else:
                    stars %= 5
                    rank -= 1

    print(rank)


if __name__ == '__main__':
    main()
