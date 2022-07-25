from sys import stdin


def main():
    l, w = map(int, stdin.readline().split())
    
    # Smallest weight possible with length l = 1 * l (all 'a')
    # Largest weight possible with length l = 26 * l (all 'z')
    if l > w or 26 * l < w:
        print('impossible')
        return
    
    # Initialise with all 'a'
    word = [1] * l
    # Intial weight
    weight = sum(word)
    
    # Change letter one index at a time
    for i in range(l):
        # Keep incrementing letter and weight at index i till weight reaches w or letter reaches 'z'
        while weight < w and word[i] < 26:
            word[i] += 1
            weight += 1
        
        if weight == w:
            [print(chr(x + 96), end='') for x in word]
            return


if __name__ == '__main__':
    main()
