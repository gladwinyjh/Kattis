from sys import stdin
from collections import defaultdict


def main():
    laps_recorded, laps_needed, num_start_numbers = map(int, stdin.readline().split())
    
    # Default dict of 0
    participants = defaultdict(lambda: 0)
    # List of start numbers to keep track of who finished the race (completed all the laps)
    # Use dictionary for large input, list result in memory exceed error
    laps_completed = defaultdict(lambda: 0)

    for i in range(laps_recorded):
        start_number, lap_time = stdin.readline().split()
        start_number = int(start_number)
        
        # Participant of this start number has completed a lap
        laps_completed[start_number] += 1

        # Process lap times and convert all to seconds
        mm, ss = lap_time.split('.')
        lap_time_seconds = int(mm) * 60 + int(ss)
        
        # Increment timings of participant in dictionary
        participants[start_number] += lap_time_seconds
    
    # Sort by dictionary values, if same then by key
    # Returns a sorted list of tuples of (key, val)
    for start_number, timing in sorted(participants.items(), key=lambda x:(x[1], x[0])):
        # Only print start number if participant completed laps needed to finish the race
        if laps_completed[start_number] == laps_needed:
            print(start_number)


if __name__ == '__main__':
    main()
    # Use a dictionary to store participants times
        # Key: starting number, val: time in seconds (convert)
    
    # Sort and print
