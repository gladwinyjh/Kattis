from collections import deque
import math


def main():
    c = int(input())

    for i in range(c):
        n, t = map(int, input().split())
        buttons = list(map(int, input().split()))
        # Used to check if timing has already been visited
        visited = [False] * 3601
        # Used to keep track of minimum number of presses needed to reach a timing
        presses = [math.inf] * 3601

        # Enqueue starting 0 seconds initially
        q = deque([0])
        # Set 0 seconds to visited
        visited[0] = True
        # Number of presses to reach 0 seconds = 0
        presses[0] = 0

        # Do a variant of Breadth First Search
        while q:  
            timing = q.popleft()
            for button in buttons:
                # Lower and upper bounds of timings
                newTiming = max(0, min(timing + button, 3600))
                if not visited[newTiming]:    
                    visited[newTiming] = True

                    # Number of presses needed to reach new timing is shorter than previously recorded
                    if presses[newTiming] > presses[timing] + 1:
                        # New number of presses = number of presses to reach current timing + 1
                        presses[newTiming] = presses[timing] + 1
                        q.append(newTiming)

        # Start from t since only concerned with extra seconds
        for j in range(t, len(presses)):
            # First occurrence of a press is the minimum number of extra seconds
            if presses[j] != math.inf:
                # Print number of presses, difference between that timing and desired timing t
                print(presses[j], j-t)
                break


if __name__ == '__main__':
    main()