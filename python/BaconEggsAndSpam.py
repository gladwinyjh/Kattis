from sys import stdin
from collections import OrderedDict


def main():
    while True:
        n = int(stdin.readline())

        if n == 0:
            return

        d = {}
        for i in range(n):
            order = list(stdin.readline().split())
            for j in order[1:]:
                if j not in d:
                    d[j] = [order[0]]
                else:
                    d[j].append(order[0])
        
        # Sort dictionary by key. Use ordered dict so sorted order is preserved.
        sorted_d = OrderedDict(sorted(d.items())) 
        for key, val in sorted_d.items():
            # Key = food, val = list of names.
            # Sort this list of names and print them out in a line
            print(key, ' '.join(sorted(val)))
                

if __name__ == '__main__':
    main()
