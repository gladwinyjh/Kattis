def main():
    # Possible vowels + 'y'
    vowels = ['a','e','i','o','u','y']
    
    # Keep looping while not end of file
    while (True):
        try:
            # Store words in list
            line = list(input().split())
            # List to output altered words
            wordList = []

            for word in line:
                if word[0] in vowels: # First character in word is a vowel
                    newWord = word + "yay" # Altered word = old word + "yay"
                    wordList.append(newWord) # Append altered word to wordList
                else:
                    for i in range(1, len(word)):
                        if word[i] in vowels: # First character that is a vowel
                            # Altered word = word from vowel to end + word from start to vowel + "ay"
                            newWord = word[i:] + word[:i] + "ay"
                            # Append altered word to wordList
                            wordList.append(newWord)
                            # Go to next word
                            break
            
            # Output altered words in list
            print(*wordList)    
        except EOFError:
            return


if __name__ == '__main__':
    main()