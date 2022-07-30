from sys import stdin


def main():
    inp = stdin.readline().rstrip()
    
    # Collect all the possible substrings from input
    macros = set()
    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            macros.add(inp[i:j])
    
    # Brute force search
    # For each substring, count the number of non-overlapping occurrences in the input
    min_count = len(inp)
    for m in macros:
        occur = inp.count(m)
        
        # Macros replace each substring with a single 'M'
        # So altered input = len(inp) - (len(m) * occurr) + (occur * 1)
        new_length = occur + len(inp) - len(m) * occur 

        # Also need to include macro as part of length so + len(m)
        # Update the minimum lengths
        min_count = min(min_count, new_length + len(m))
        
    print(min_count)
    
    
if __name__ == '__main__':
    main()
