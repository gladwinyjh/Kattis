def main():
    vowels = ['a','e','i','o','u','y']

    while True:
        n = int(input())
        # Break out of loop if n = 0
        if n == 0:
            break

        bestCount = 0
        for i in range(n):
            word = input()
            # If only 1 word given, that word is the favorite word
            if n == 1:
                favoriteWord = word
                break

            count = 0
            for j in range(1, len(word)):
                if word[j] == word[j-1] and word[j] in vowels:
                    count += 1
            
            # If current word has more pairs of double vowels
            # than previous recorded words, current word is new favorite word
            if count > bestCount:
                bestCount = count
                favoriteWord = word
        
        print(favoriteWord)   
            

if __name__ == '__main__':
    main()