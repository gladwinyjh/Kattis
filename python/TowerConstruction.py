def main():
    n = int(input())
    # List to store bricks
    bricks = list(map(int, input().split()))

    # Start with one tower
    count = 1
    for i in range(1,n):
        # If current brick is smaller than prev brick, start new tower
        if bricks[i] > bricks[i-1]:
            count += 1

    print(count)


if __name__ == '__main__':
    main()