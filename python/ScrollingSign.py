def main():
    n = int(input())
    for i in range(n):
        k, w = map(int, input().split())
        # Store words in message to list
        words = []
        for j in range(w):
            words.append(input())
        
        # Since start off with blanks/spaces, 
        # to get to the first word, we need to flip k times
        count = k

        # For each word in message starting with the second word
        for j in range(1, len(words)):
            # Get previous word
            word = words[j-1]
            # For each character in a word
            for l in range(k):
                # Break if previous word suffix is current word prefix
                # Suffix starts from complete length to 0 as l increases
                if word[l:k] == words[j][:k-l]:
                    break
                # Increase number of flips needed to get from previous word to current word
                count += 1
                
        print(count)
  

if __name__ == '__main__':
    main()