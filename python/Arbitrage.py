from sys import stdin
import math
from collections import defaultdict


def floyd_warshall(currency_codes, D):
    for k in currency_codes:
        for i in currency_codes:
            for j in currency_codes:
                D[(i, j)] = min(D[(i, j)], (D[(i, k)] + D[(k, j)]))
                # Early exit, TLE if don't
                if i == j and D[(i, j)] < 0:
                    return True

    return False

def main():
    while True:
        C = int(stdin.readline())
        if C == 0:
            return

        currency_codes = list(stdin.readline().split())
        R = int(stdin.readline())

        D = defaultdict(lambda: float('inf'))
        for i in range(R):
            u, v, rate = stdin.readline().split()
            pay, receive = map(int, rate.split(':'))

            # Conversion rates from currency x to currency x can be direct or indirect
            # Direction conversion rate = 1
            # Indirect conversion rate = (pay x/receive y) * (pay y/receive a) * ... * (pay b/receive x)
                # If this is more than 1, then there is a profit
                # So LHS > 1 for arbitrage
            # Natural log the both sides so it becomes an addition
                # ln(pay x/receive y) + ln(pay y/receive a) + ... + ln(pay b/receive x) < ln(1)
                # Some cycle from x back to x < 0
                # So that problem reduces to a negative cycle detection, source = dest
            D[(u, v)] = math.log(int(pay) / int(receive))

        for code in currency_codes:
            D[(code, code)] = 0
        
        if floyd_warshall(currency_codes, D):
            print('Arbitrage')
        else:
            print('Ok')

   
if __name__ == '__main__':
    main()
