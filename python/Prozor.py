def main():
    R, S, K = map(int, input().split())
    picture = []
    
    for i in range(R):
        picture.append(list(input()))
    
    max_flies = 0
    # Position racket
    # Start from 1 to R-2 because we are only accounting for the hittable area
    # You cannot hit flies on the perimeter of the picture because the edges have nowhere to go 
    for i in range(1, R-1):
        for j in range(1, S-1):
            
            # Check if entire racket will be within picture
            if i + (K-2) >= R or j + (K-2) >= S:
                continue

            # Starting from the top corner of hittable area
            # Count the number of flies
            flies = 0
            # Range == K-2 for each axis because we dont include the left, right, top, bottom of racket
            for k in range(K-2):
                for l in range(K-2):
                    if picture[i+k][j+l] == '*':
                        flies += 1
            
            if flies > max_flies:
                max_flies = flies
                # Top corner coordinates of racket
                row = i - 1
                col = j - 1

    for i in range(row, row+K):
        if i == row or i == row+K-1:
            # '+' for the corners of the racket
            picture[i][col] = '+'
            picture[i][col+K-1] = '+'
        else:
            # '|' for the vertical sides of the racket
            picture[i][col] = '|'
            picture[i][col+K-1] = '|'

    # Start from col+1 and go till 2nd last col+1+hittable width - 1 = col+1+(K-2)-1 = col+K-2. So top bound non inclusive col+K-2+1
    for i in range(col+1, col+K-1):
        # '-' for horizontal sides of the racket, top and bottom only
        picture[row][i] = '-'
        picture[row+K-1][i] = '-'

    print(max_flies)
    [print(''.join(row)) for row in picture]


if __name__ == '__main__':
    main()