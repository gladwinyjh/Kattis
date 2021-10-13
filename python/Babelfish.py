def main():
    wordDict = {}
    # Boolean to check if input should be added to dict or is a message
    message = False
    while True:
        try:
            line = input()
            # Blank line, skip this, subsequent lines will be messages
            if not line:
                message = True
                continue
            
            # If adding words to dict, 
            # take in words and meanings from line
            if not message:
                word, dialect = line.split()
                wordDict[dialect] = word

            else:
                # Check if word is in dict
                if line not in wordDict:
                    print('eh')
                else:
                    print(wordDict[line])
        # No more inputs
        except EOFError:
            return


if __name__ == '__main__':
    main()