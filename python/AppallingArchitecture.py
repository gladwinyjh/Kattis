def main():
    h, w = map(int, input().split())
    # Number of components present in structure
    components = 0
    # Left and rightmost markers
    left = -1
    right = -1

    # List of zeros to store locations of components
    blueprint = [0] * w
    
    for i in range(h):
        line = input()
        for j in range(len(line)):
            if line[j] != '.': # Is a component
                components += 1
                blueprint[j] += 1
                # For last row
                if i == h-1:
                    # Leftmost point have not been encountered
                    if left == -1:
                        # Store leftmost point. 
                        # Note position starts from 1
                        left = j+1
                    # Store rightmost point
                    # Note position starts from 1
                    right = j+1
    
    # Get center of gravity
    # Average of (number of components at each distance * distance)
    total = [(i+1) * blueprint[i] for i in range(len(blueprint))]
    center_of_gravity = sum(total) / components

    if center_of_gravity + 0.5 < left: # Leftmost bound
        print('left')
    elif center_of_gravity - 0.5 > right: # Rightmost bound
        print('right')
    else:
        print('balanced')


if __name__ == '__main__':
    main()