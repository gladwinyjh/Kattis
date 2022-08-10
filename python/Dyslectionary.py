from sys import stdin


def solve(words, max_length):
    for word in words:
        # Reverse string again, right justify based on max length
        print(word[::-1].rjust(max_length))


def main():
    words = []
    max_length = 0
    for line in stdin:
        # End of test case, and there is a next one
        if line == '\n':
            # Sort list
            solve(sorted(words), max_length)
            # Clear list, and reset max length
            words = []
            max_length = 0
            print()
            continue
        
        # Reverse the word since sorting based on back of string
        line = line.rstrip()[::-1]
        # To update the number of spaces to right justify, keep track of the max string length of input
        max_length = max(max_length, len(line))
        words.append(line)
    
    # This is for the last test case
    solve(sorted(words), max_length)


if __name__ == '__main__':
    main()
