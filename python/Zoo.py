from sys import stdin
from collections import defaultdict, OrderedDict


def main():
    for case in range(1, 6):
        n = int(stdin.readline())

        if n == 0:
            return

        d = defaultdict(lambda: 0)
        for i in range(n):
            # Only concerned with the last word
            animal = stdin.readline().split()[-1]
            # Store the lower-case form in dictionary
            d[animal.lower()] += 1
        
        # Sort dictionary keys
        sorted_d = OrderedDict(sorted(d.items()))
        
        print(f'List {case}:')
        for animal, quantity in sorted_d.items():
            print(animal, quantity, sep=' | ')
        

if __name__ == '__main__':
    main()
