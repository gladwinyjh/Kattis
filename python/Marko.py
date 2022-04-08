def main():
    # Dictionary to store keypad mappings
    d = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    }

    N = int(input())
    
    # Append dictionary words to a list
    wordList = []
    for i in range(N):
        wordList.append(input())
    
    S = input()

    numValidWords = 0
    for word in wordList:
        validWord = True

        # Dictionary word and array of different lengths
        # Impossible to type word, move on to next word
        if len(S) != len(word):
            continue

        for i in range(len(word)):
            # Corresponding numbers at index dont match, unable to find a valid word from dictionary
            if d[word[i]] != S[i]:
                validWord = False
                break
        
        # Word and array numbers match, word can be typed from dictionary
        if validWord:
            numValidWords += 1
        
    print(numValidWords)
        
        
if __name__ == '__main__':
    main()