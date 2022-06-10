from sys import stdin
from itertools import permutations


def main():
    words = []
    for line in stdin.readlines():
        [words.append(x) for x in line.split()]
    
    # Get permutations of 2 joined words
    # Because they can be repeated, use set to only get unique permutations
        #Ex: 'bb' + 'b' is the same as 'b' + 'bb' are different permutations but the same word
    unique = set()
    for perm in permutations(words, 2):
        unique.add(''.join(perm))

    for val in sorted(unique):
        # Print sorted values 
        print(val)
    

if __name__ == '__main__':
    main()
