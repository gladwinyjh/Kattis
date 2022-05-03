def main():
    pieces = list(map(int, input().split()))
    
    # Bubble sort with early termination
    # Each time a swap occurs, print out the ordering of the pieces
    for i in range(5):
        swapped = False
        for j in range(0, 5-i-1):
            if pieces[j] > pieces[j+1]:
                swapped = True
                pieces[j], pieces[j+1] = pieces[j+1], pieces[j]
                print(*pieces)

        if not swapped:
            return


if __name__ == '__main__':
    main()
