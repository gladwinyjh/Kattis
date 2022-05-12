def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, size, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
        size[yroot] += size[xroot]
        return size[yroot]
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
        size[xroot] += size[yroot]
        return size[xroot]
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
        size[xroot] += size[yroot]
        return size[xroot]


def main():
    parent = {}
    rank = {}
    # Used to track the size of a building block using its representative building
    size = {}

    for i in range(int(input())):
        buildingOne, buildingTwo = input().split()
        
        # Intially each new building is its own component
        if buildingOne not in parent:
            parent[buildingOne] = buildingOne
            rank[buildingOne] = 0
            size[buildingOne] = 1

        if buildingTwo not in parent:
            parent[buildingTwo] = buildingTwo
            rank[buildingTwo] = 0
            size[buildingTwo] = 1

        parentOne = find(parent, buildingOne)
        parentTwo = find(parent, buildingTwo)
        
        if parentOne != parentTwo:
            # Buildings not connected by a bridge
            # Connect them and add the 2 sizes together
            print(union(parent, rank, size, parentOne, parentTwo))
        else:
            # Both buildings were already introduced before and have a bridge linking them before
            # So we are not introducing new buildings to this block of buildings, just building one more bridge
            # Size should not change, can print size[parentTwo] or size[parentOne]
            print(size[parentOne])
            

if __name__ == '__main__':
    main()
