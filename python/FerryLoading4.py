from sys import stdin
from collections import deque


def main():
    c = int(stdin.readline())
    
    for i in range(c):
        # Use a deque because cars are to be processed in order of arrival(popleft)
        left = deque([])
        right = deque([])
        
        ferry_length, cars = map(int, stdin.readline().split())
        # Car lengths in cm, so convert ferry length from m to cm
        ferry_length *= 100
        
        for j in range(cars):
            car_length, arrival = stdin.readline().split()
            
            if arrival == 'left':
                left.append(int(car_length))
            else:
                right.append(int(car_length))
        
        # Number of crossings 
        num_cross = 0
        
        # Ferry load
        ferry_load = 0
        
        # Initial bank of ferry
        # True = left, False = right
        initial = True
        
        while left or right:

            # Start off with the left bank, so while statement for left bank is first
            # Subsequently, it just depends on which bank the ferry is at

            # While:
            # 1) Ferry is on the left bank
            # 2) There are cars on the left bank
            # 3) Ferry can accomodate the car at the top of the stack
            while initial and left and ferry_load + left[0] <= ferry_length:
                # Add the car to the ferry
                ferry_load += left.popleft()
            
            # Same for right 
            while not initial and right and ferry_load + right[0] <= ferry_length:
                ferry_load += right.popleft()
             
            # Ferry crosses the river
            initial = not initial
            # Unloading on the other bank
            ferry_load = 0
            # Increment number of ferry crossings
            num_cross += 1
        
        print(num_cross)                  


if __name__ == '__main__':
    main()