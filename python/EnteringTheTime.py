from sys import stdin
from collections import deque
from time import sleep


def BFS(q, visited, curr_h1, curr_h2, curr_m1, curr_m2):
    while q:
        h1, h2, m1, m2, times = q.popleft()
        
        if (h1, h2, m1, m2) == (curr_h1, curr_h2, curr_m1, curr_m2):
            return times
        
        time = [h1, h2, m1, m2]
        for i in range(len(time)):
            digit = time[i]

            for delta in (-1, 1): # Either increase or decrease digit by 1
                new_digit = digit + delta
                
                # 0-9
                # Last digit
                if i == 3:
                    # No additional restrictions on the last digit
                    # So only must fall between 0 to 9
                    if new_digit == 10:
                        new_digit = 0
                    elif new_digit == -1:
                        new_digit = 9
                    
                    if (h1, h2, m1, new_digit) not in visited:
                        visited.add((h1, h2, m1, new_digit))
                        new_times = times.copy()
                        new_times.append((h1, h2, m1, new_digit))
                        q.append((h1, h2, m1, new_digit, new_times))
                
                # 0-5
                # 3rd digit
                elif i == 2:
                    # Additional restriction: Must fall within 0 to 5
                    # So there won't be a situation where it will be -1 or 10
                    if new_digit == 6 or new_digit == -1:
                        continue
                    
                    if (h1, h2, new_digit, m2) not in visited:
                        visited.add((h1, h2, new_digit, m2))
                        new_times = times.copy()
                        new_times.append((h1, h2, new_digit, m2))
                        q.append((h1, h2, new_digit, m2, new_times))
                
                # 0-3
                # 2nd digit
                elif i == 1:
                    # Additional restrictions:
                        # If 2nd digit == 10, that means 1st digit is 0 or 1, which can take 0 to 9 for 2nd digit
                        # So reseting it to 0 will be fine
                            # Will not be given a situation: 25:00 or 29:00 to begin with

                        # If 2nd digit == -1, in order for it to go back to 9, the 1st digit MUST be < 2
                            # Ex: 19:00 or 09:00
                    if new_digit == 10:
                        if time[0] < 2:
                            new_digit = 0
                        else:
                            # Other situations where 2nd digit == 10 is not possible
                            continue
                    elif new_digit == -1:
                        if time[0] < 2:
                            new_digit = 9
                        else:
                            # Other situations where 2nd digit == -1 is not possible
                            continue
                    
                    if (h1, new_digit, m1, m2) not in visited:
                        visited.add((h1, new_digit, m1, m2))
                        new_times = times.copy()
                        new_times.append((h1, new_digit, m1, m2))
                        q.append((h1, new_digit, m1, m2, new_times))
                
                # 0-2
                # 1st digit
                else:
                    # Additional restrictions:
                        # New digit must fall between 0 and 2 inclusive
                    if new_digit == 3 and new_digit == -1:
                        continue
                    
                    if (new_digit, h2, m1, m2) not in visited:
                        visited.add((new_digit, h2, m1, m2))
                        new_times = times.copy()
                        new_times.append((new_digit, h2, m1, m2))
                        q.append((new_digit, h2, m1, m2, new_times))
        

def main():
    clock = stdin.readline()
    clock_h1 = int(clock[0])
    clock_h2 = int(clock[1])
    clock_m1 = int(clock[3])
    clock_m2 = int(clock[4])

    curr = stdin.readline()
    curr_h1 = int(curr[0])
    curr_h2 = int(curr[1])
    curr_m1 = int(curr[3])
    curr_m2 = int(curr[4])   
    
    # Keep track of visited times, don't want repetition
    visited = set()
    visited.add((clock_h1, clock_h2, clock_m1, clock_m2))
    # (current time split up to digits, time path taken)
    q = deque([(clock_h1, clock_h2, clock_m1, clock_m2, [(clock_h1, clock_h2, clock_m1, clock_m2)])])
    
    # Clock is set to a valid time, so BFS explore increasing and decreasing by 1 for each digit
    # Store path, return first time it reaches goal time
    times = BFS(q, visited, curr_h1, curr_h2, curr_m1, curr_m2)
    print(len(times))
    [print(str(x[0]) + str(x[1]) + ':' + str(x[2]) + str(x[3])) for x in times]


if __name__ == '__main__':
    main()
