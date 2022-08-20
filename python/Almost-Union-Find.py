from sys import stdin


def union(parent, elements, parent_p, parent_q):
    if len(elements[parent_p]) > len(elements[parent_q]):
        # For each element in the set q is in, 
        # Add the element to the set parent_p is in, and change its parent to parent_p
        for x in elements[parent_q]:
            parent[x] = parent_p
            elements[parent_p].add(x)
        
        # All elements in set of parent_q is merged into set of parent_p, can clear it
        elements[parent_q].clear()
    else:
        # Same thing as above but the other way around
        for x in elements[parent_p]:
            parent[x] = parent_q
            elements[parent_q].add(x)

        elements[parent_p].clear()


def move(parent, elements, p, q):
    # Move only 1 sole element p to the set parent_q belongs to
    elements[parent[q]].add(p)
    # Remove p from the set its parent belongs to
    elements[parent[p]].discard(p)
    # Update p's parent to q's parent
    parent[p] = parent[q]


def main():
    while True:
        inp = stdin.readline()

        if not inp:
            # End of test cases
            return

        n, m = map(int, inp.split())
        
        parent = [i for i in range(n+1)]
        elements = [set([i]) for i in range(n+1)]
    
        for i in range(m):
            op, *elems = map(int, stdin.readline().split())
            
            p = elems[0]
            if len(elems) > 1:
                q = elems[1]

                # Same set, skip
                if parent[p] == parent[q]:
                    continue

                if op == 1:
                    union(parent, elements, parent[p], parent[q])
                else:
                    move(parent, elements, p, q)
            else:
                print(len(elements[parent[p]]), sum(elements[parent[p]]))
    

if __name__ == '__main__':
    main()
