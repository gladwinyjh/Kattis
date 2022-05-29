from math import factorial


def nCr(n, r):
    return (factorial(n) // (factorial(r) * factorial(n - r)))


def find_perm(seq, N):   

    if N <= 2:
        # Only 1 sequence to give a given subtree
        # Look at 5 -> 4 in the given example
            # If we change it to 5 -> 4, the BST will be different
        return 1

    root = seq[0]
    
    leftChildren = []
    rightChildren = []
    for i in range(1, N):
        if seq[i] < root:
            leftChildren.append(seq[i])
        else:
            rightChildren.append(seq[i])

    num_left_seq = find_perm(leftChildren, len(leftChildren))
    num_right_seq = find_perm(rightChildren, len(rightChildren))

    # Between left and right subtree, the ordering does not matter
    # But within each each subtree, the ordering matters
    # See the given example:
        # For root 3, len(leftChildren) == 0, rightChildren = [4, 3, 5, 4]
        # In rightChildren, leftChildren = 3, rightChildren = [5, 4]
            # This 3 can be inserted anywhere along the rightChildren
            # But the rightChildren ordering is fixed for the given BST: 4 is the left child of 5
                # So 4 must be after 5 in the sequence, and 3 can be inserted anywhere
                    # [3, 5, 4], [5, 3, 4], [5, 4, 3]
                
            # So we have 3 arrangements under their root 4
            # This 4 is the right root of subtree under superroot 3, which does not have any left subtree
            # So only sequences are the ones shown
        
        # For given left and right subtrees, the number of combinations attainable are nCr
            # where n = number of left children + number of right children
            # where r = either number of left children or number of right children
                # left or right does not matter as choosing one will set the positions for the other

    # More info: https://stackoverflow.com/questions/17119116/how-many-ways-can-you-insert-a-series-of-values-into-a-bst-to-form-a-specific-tr
    return (nCr(len(leftChildren) + len(rightChildren), len(leftChildren)) * num_left_seq * num_right_seq)


def main():
    while True:
        N = int(input())

        if N == 0:
            return

        seq = list(map(int, input().split()))  
        print(find_perm(seq, N))

if __name__ == '__main__':
    main()