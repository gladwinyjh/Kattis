def main():
    n = int(input())
    heights = list(map(int, input().split()))
    count = 1

    # Dictionary containing balloon heights needed for consecutive clearance with 1 shot
    # Key: Height of balloon, Value: Number of balloons of that height needed
    heightsNeeded = {}
    # Height needed for 1st balloon
    heightsNeeded[heights[0]-1] = 1
    for i in range(1, n):
        if heights[i] not in heightsNeeded:
            # If current balloon height not required yet
            # we need a new arrow to clear it
            count += 1 
        elif heightsNeeded[heights[i]] > 1:
            # There is a needed for this balloon to be popped
            # Decrement value for that height if more than 1 balloon needed
            heightsNeeded[heights[i]] -= 1
        else:
            # If only 1 balloon needed to be popped, delete key altogether
            del heightsNeeded[heights[i]]

        # Add the height needed to pop current balloon to dict
        # Increment value by 1 if there is already a previously selected balloon
        # that shares height with current balloon (i.e need more heights[i]-1 balloons now)
        if heights[i] - 1 not in heightsNeeded:
            heightsNeeded[heights[i]-1] = 1
        else:
            heightsNeeded[heights[i]-1] += 1

    print(count)


if __name__ == '__main__':
    main()