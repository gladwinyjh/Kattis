from sys import stdin


def main():
    n, X = map(int, stdin.readline().split())

    prices = list(map(int, stdin.readline().split()))
    prices.sort()
    
    num_items = 1
    for i in range(len(prices)-1):
        if prices[i] + prices[i+1] > X:
            break
        else:
            num_items += 1

    print(num_items)


if __name__ == '__main__':
    main()
    # From all the items, pick a group of them
    # such that any 2 in this subset > X

    # Sort ascending
    # Compare prices between 2 adjacent right items
        # If both prices > X, then no need to check for rest of the items alr
