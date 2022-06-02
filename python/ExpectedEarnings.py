def main():
    n, k, p = map(float, input().split())
    # 2 outcomes here:
        # 1) Win
            # Expected value = Total profit (n - k) * prob of winning (p)
                # Careful! It is not n * prob as it costs k to play!

        # 2) Loss
            # Expected value = Total profit (-k) * prob of losing (1-p)

    # Do a summation
    expected_earnings = ((n - k) * p) + (-k * (1 - p))
    if expected_earnings < 0:
        print('spela')
    else:
        print('spela inte!')
    

if __name__ == '__main__':
    main()
