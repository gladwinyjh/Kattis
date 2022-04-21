def main():
    W = int(input())
    N = int(input())
    
    tot_area = 0
    # Sum up the area of all the broken pieces
    for i in range(N):
        width, length = map(int, input().split())
        tot_area += width * length
    
    # Length = Total area / Width
    print(int(tot_area / W))


if __name__ == '__main__':
    main()
