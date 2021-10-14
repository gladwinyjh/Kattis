# Function to get index of letter in 2D keyboard list
def get_index(keyboard, v):
    for i, x in enumerate(keyboard):
        if v in x:
            return (i, x.index(v))


# Function to calculate distance: sum of differences in x and y direction
def get_distance(x1, x2):
    distance = abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])
    return distance


def main():
    keyboard = [
        ['q','w','e','r','t','y','u','i','o','p'],
        ['a','s','d','f','g','h','j','k','l'],
        ['z','x','c','v','b','n','m']
    ]
    n = int(input())

    for i in range(n):
        typedWord, numEntries = input().split()
        d = {}
        for j in range(int(numEntries)):
            word = input()
            # To store sum of distances between each letter in 2 words
            totDistance = 0
            for k in range(len(word)):
                # If letter in position is different in both words
                if typedWord[k] != word[k]:
                    # Get the index of letter from keyboard
                    typedIndex = get_index(keyboard, typedWord[k])
                    wordIndex = get_index(keyboard, word[k])
                    # Calculate distance between positions of the 2 letters
                    distance = get_distance(typedIndex, wordIndex)
                    # Increment total distance
                    totDistance += distance

            # Store word and distance in dictionary
            d[word] = totDistance

        # Sort dictionary in ascending order: by value, if same value then key alphabetically
        sortedDict = sorted(d.items(), key=lambda t: t[::-1])
        # Print out
        for j in range(len(sortedDict)):
            print(sortedDict[j][0], sortedDict[j][1])


if __name__ == '__main__':
    main()