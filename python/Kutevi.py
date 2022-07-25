from sys import stdin


def get_angles(angle, possible_angles, mirko):
    # Mark current angle as visited
    possible_angles[angle] = 1
    
    # For each angle in mirko
    for x in mirko:
        # Get the addition of the current angle and this angle
        add = (angle + x) % 360
        # Get the subtraction of the current angle and this angle
        sub = (angle - x + 360) % 360
        
        # If the angles have not yet been visited, visit them
        if not possible_angles[add]:
            get_angles(add, possible_angles, mirko)
        if not possible_angles[sub]:
            get_angles(add, possible_angles, mirko)


def main():
    N, K = map(int, stdin.readline().split())
    
    mirko = list(map(int, stdin.readline().split()))
    
    # Visited list of all angles 0 to 360, but 360 is the same as 0 so till 359
    possible_angles = [0] * 359
    
    # Initially at 0 deg
    get_angles(0, possible_angles, mirko)
    
    # For each selected slavko angle, check if the angle can be visited by mirko's angles
    for selected in map(int, stdin.readline().split()):
        if possible_angles[selected]:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
