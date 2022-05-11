def main():
    n = int(input())

    temps = [int(x) for x in input().split()]
    
    max_temp = 41
    max_day = -1
    for i in range(1, len(temps)-1):
        # Check the maximum of the start and end day 
        # If this maximum is lower than our current maximum
        # Set the current maximum to this maximum, and the day to be the start day
        if max_temp > max(temps[i-1], temps[i+1]):
            max_temp = max(temps[i-1], temps[i+1])
            max_day = i-1
            
    print(max_day+1, max_temp)


if __name__ == '__main__':
    main()
