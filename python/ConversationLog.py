def main():
    m = int(input())
    # Dictionaries to store users + messages, words + frequencies
    userDict = {}
    wordDict = {}
    for i in range(m):
        message = list(input().split())
        user = message.pop(0)
        # Add user as key, message as value
        if user not in userDict:
            userDict[user] = message
        else:
            userDict[user].extend(message)
        # Add word as key, frequency of that word as value
        for word in message:
            if word not in wordDict:
                wordDict[word] = 1
            else:
                wordDict[word] += 1
    
    # Get the unique words in each user's messages
    for key, val in userDict.items():
        userDict[key] = set(val)

    # Sort words based on frequency in descending order (-x[1])
    # If same, then alphabetically (x[0])
    # Return in the form of (word, freq)
    sortedWords = sorted(wordDict.items(), key=lambda x: (-x[1], x[0]))

    # Boolean to check if there is at least one common word
    noWords = True
    for word, freq in sortedWords:
        # Boolean to check if current word is common to all users
        common = True
        for key, val in userDict.items():
            # If current word is not mentioned by a user, word is not common
            if word not in userDict[key]:
                common = False
                break
        
        # If word is common, print word
        # Since words are taken from sortedWords, it does not need any more processing
        if common:
            noWords = False
            print(word)
    
    # No common words
    if noWords:
        print('ALL CLEAR')
 

if __name__ == '__main__':
    main()