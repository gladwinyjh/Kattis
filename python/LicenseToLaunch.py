def main():
    n = int(input())
    spaceJunkList = list(map(int, input().split()))

    # Find the minimum value of the list
    min_junk = min(spaceJunkList)

    # Get he first occurence of the minimum
    index_min_junk = spaceJunkList.index(min_junk)
    print(index_min_junk)
    

if __name__ == '__main__':
    main()