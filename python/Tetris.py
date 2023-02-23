from sys import stdin


def main():
    # Base of the pieces in each orientation
    # Ex: [-1, 0, 0] means: _
    #                        |__
    pieces = {
        1: [[0], [0, 0, 0, 0]],
        2: [[0, 0]],
        3: [[0, 0, -1], [-1, 0]],
        4: [[-1, 0, 0], [0, -1]],
        5: [[0, 0, 0], [0, -1], [-1, 0, -1], [-1, 0]],
        6: [[0, 0, 0], [0, 0], [0, -1, -1], [-2, 0]],
        7: [[0, 0, 0], [0, -2], [-1, -1, 0], [0, 0]]
    }

    C, P = map(int, stdin.readline().split()) 
    
    field = list(map(int, stdin.readline().split()))
    
    num_ways = 0
    
    # For each orientation of the piece
    for orientation in pieces[P]: 
        # Slide the piece over the field
        # Do element wise addition 'mask' of the base of the piece with the top of the field
        for i in range(0, len(field) - len(orientation) + 1):
            # field[i:len(orientation)+i], only concern with the mask as the piece slides over the top of the field
            # If there are no gaps, new_field_part should be a list with the same integer values
            new_field_part = [a + b for a, b in zip(orientation, field[i:len(orientation)+i])]
            
            # len(set(new_field_part)) != 1 means that there are gaps
            if len(set(new_field_part)) == 1:
                num_ways += 1
                
    print(num_ways)
               

if __name__ == '__main__':
    main()
    # Mentioned about number of columns but not rows, so assume that height of field is not a problem