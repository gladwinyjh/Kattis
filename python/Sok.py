def main():
    A, B, C = map(float, input().split())
    I, J, K = map(float, input().split())
    
    # Get the min multiplier needed to finish one juice
    min_juice = min(A/I, B/J, C/K)
    
    # Quantity of juice - min multiplier * recipe gives the leftover
    # There will always be one juice with 0 leftover
    # Format to 6 dp
    print("{:.6f} {:.6f} {:.6f}".format(A - min_juice * I,
        B - min_juice * J,
        C - min_juice * K))


if __name__ == '__main__':
    main()
