def main():
    n, m = map(int, input().split())
    # Dictionary used to store (notes:instruments)
    d = {}

    for i in range(n):
        # Instrument variable assigned to list of notes 
        instrument = list(map(int, input().split()))
        
        # Add notes to dictionary as keys, and the instruments that can play those notes as its values in a list
        for j in range(1,instrument[0]+1):
            if instrument[j] in d:
                d[instrument[j]].append(i)
            else:
                d[instrument[j]] = [i]
    
    notes = list(map(int, input().split()))
    
    # Number of switches needed to play all notes
    switches = 0
    
    # current_valid stores set of instruments that can play all notes till a certain index
    # Intialise as set of instruments that can play first note d[notes[0]]
    current_valid = set(d[notes[0]])
    
    # Start from 2nd index to end
    # Find common instruments between current note and current_valid
    for i in range(1, len(notes)):
        current_valid = set(d[notes[i]]).intersection(current_valid)
        # If there are no common instruments, there is a need to switch instruments here
        # Replace current_valid with the current instrument to play current note, and increment switches
        if not current_valid:
            current_valid = set(d[notes[i]])
            switches += 1
    
    print(switches)


if __name__ == '__main__':
    main()
