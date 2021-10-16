def main():
    while True:
        n, m = map(int, input().split())

        if n == m == 0:
            break

        bestTickets = 0
        bestValue = float('inf')
        bestPrice = 0
        for i in range(n):
            a, b = map(int, input().split())
            if a > m:
                # Current offer has more tickets than desired m
                continue

            # Calculate value: Price of tickets / number of tickets
            value = b / a

            # New best offer if current offer is of greater value than previous best offer
            # or if same value, the current offer gives more tickets than the previous best offer
            if value < bestValue or (value == bestValue and a > bestTickets):
                bestValue = value
                bestTickets = a
                bestPrice = b
        
        if bestPrice == 0:
            # No suitable offer 
            print('No suitable tickets offered')
        else:
            print(f'Buy {bestTickets} tickets for ${bestPrice}')


if __name__ == '__main__':
    main()