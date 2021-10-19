def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        d = {}

        largestPackage = 0
        count = 0
        for j in range(n):
            id = int(input())
            if id not in d:
                # Snowflake not repeated
                count += 1
            else:
                count = min(count+1, j-d[id])

            d[id] = j
            largestPackage = max(count, largestPackage)

        print(largestPackage)


if __name__ == '__main__':
    main()