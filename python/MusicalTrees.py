from bisect import bisect_left


def closest_tree(trees, p):
    # bisect_left returns the insertion point of the element if it does not exist in the list
    pos = bisect_left(trees, p)

    # Closest tree is the first tree in the list. Tree could be same distance as person
    if pos == 0:
        return pos

    # Tree of the same distance not found, but closest tree is the last tree in the list
    if pos == len(trees):
        return -1

    # In between trees, check the trees to the left and right of it
    # Take the closest tree OR if left and right same distance, take the left one
    tree_before = trees[pos - 1]
    tree_after = trees[pos]
    if tree_after - p < p - tree_before:
        return pos
    else:
        return pos-1

def main():
    n, m = map(int, input().split())
    people = list(map(int, input().split()))
    trees = list(map(int, input().split()))
    
    # Sort trees list for binary search
    trees.sort()
    
    # Boolean list to check if a tree is already taken
    taken = [False] * m

    for i in range(len(people)):
        # Find the closest tree to this person with binary search
        idx = closest_tree(trees, people[i])
        
        # Does not matter who takes the tree first since each person has only a specific tree to take
        if not taken[idx]:
            # Mark tree as taken
            taken[idx] = True
            # One less person without a tree
            n -= 1
            # Early exit if each person has a tree already
            if n == 0:
                break
    
    # Number of people remaining without a tree
    print(n)
        

if __name__ == '__main__':
    main()
