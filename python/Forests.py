from sys import stdin
from collections import defaultdict


def main():
    P, T = input().split()
    # Use set as we do not want repeated pairs (question lies, there are actually repeated pairs of i and j)
    d = defaultdict(set)
    
    for line in stdin.readlines():
        i, j = line.split()
        d[i].add(j)
    
    # For each value in the dictionary, sort the trees, then use a tuple so that they are hashable
    # Place them all in a set to get the unique sets of trees, then get the number of unique sets of trees
    ret = len({tuple(sorted(val)) for val in d.values()})
    if len(d) < int(P):
        # There are people that are not registered in dictionary if len(d) < number of people
        # Which means that they did not hear any tree fall
        # We have to count that as a possible opinion, so + 1
        print(ret + 1)
    else:
        print(ret)


if __name__ == '__main__':
    main()
