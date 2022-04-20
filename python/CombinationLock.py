def rotate(curr, nxt, num_rotations, angle_per_mark):
    if nxt > curr:
        num_rotations += angle_per_mark * ((40 - nxt) + curr)
    else:
        num_rotations += angle_per_mark * abs(curr - nxt)
    
    return num_rotations


def main():
    while True:
        angle_per_mark = 360/40
        num_rotations = 720

        initial, first, second, third = map(int, input().split())
        
        if initial == 0 and first == 0 and second == 0 and third == 0:
            return
        
        # For clockwise rotations, marks are decreasing as the dial is rotated
        # If next mark <= previous mark, then it is just the difference between both marks
        # If next mark > previous mark, then we have to rotate to 0 first, then rotate to the next mark
            # So rotations = prev mark + (40 + next mark)

        # Similar idea for anticlockwise rotations 


        # First
        num_rotations = rotate(initial, first, num_rotations, angle_per_mark)
        
        num_rotations += 360

        # Second
        num_rotations = rotate(second, first, num_rotations, angle_per_mark)

        # Third
        num_rotations = rotate(second, third, num_rotations, angle_per_mark)

        print(int(num_rotations))


if __name__ == '__main__':
    main()
