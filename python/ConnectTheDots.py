def processImage(image, numItems, d):
    # Lazy way of doing it. Can also use chr method
    asciiList = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Get sub-list of elements to be in image
    # Since if element of index k is in image, all elements before it (0 to k-1) must also be in image
    subList = asciiList[:numItems]

    for i in range(1, len(subList)):
        # Get the difference in rows (dr) and in columns (dc)
        # Note that one of these have to be 0 since 
        # problem stated 'connected dots will always be vertically or horizontally related'
        dr = abs(d[subList[i]][0] - d[subList[i-1]][0])
        dc = abs(d[subList[i]][1] - d[subList[i-1]][1])

        # Vertical difference present, i.e there is a difference in rows 
        if dr != 0:
            # Since difference is in columns, column remains constant
            col = d[subList[i]][1]
            for k in range(min(d[subList[i]][0], d[subList[i-1]][0])+1,max(d[subList[i]][0], d[subList[i-1]][0])):
                # Get the next row
                row = k

                # Change the element in the image
                if image[row][col] == '-':
                    image[row][col] = '+'
                elif image[row][col] == '.':
                    image[row][col] = '|'
        
        # Horizontal difference present, i.e there is a difference in columns
        elif dc != 0:
            # Since difference is in columns, row remains constant
            row = d[subList[i]][0]
            for k in range(min(d[subList[i]][1], d[subList[i-1]][1])+1,max(d[subList[i]][1], d[subList[i-1]][1])):
                # Get the next column
                col = k

                # Change the element in the image
                if image[row][col] == '|':
                    image[row][col] = '+'
                elif image[row][col] == '.':
                    image[row][col] = '-'

    # Unwrap list of lists
    for row in image:
        print("".join(row))


def main():
    # Keep taking in images
    while (True):
        # Dictioanary to store dot-coordinate mappings
        d = {}
        # Image list to store lines
        image = []
        # Store number of dots present in an image
        numItems = 0
        # Used for indexing purposes, to go to next row
        r = 0

        # Keep taking in lines
        while (True):
            try:
                line = list(input())
                if line: # Valid line present
                    # Add line (as a list) to image list
                    image.append(line)
                    for c in range(len(line)):
                        if line[c] != '.':
                            # Increment number of dots present
                            numItems += 1
                            # Add type of dot to dictionary, with coordinates as value
                            d[line[c]] = [r,c]
                else:
                    # Blank line encountered. Process image
                    processImage(image, numItems, d)
                    # Print blank line below
                    print()
                    break
                
                # Go to next row
                r += 1

            # End of file, process last image and return
            except EOFError:
                # Process image. Do not need to print blank line after.
                processImage(image, numItems, d)
                return
        

if __name__ == '__main__':
    main()