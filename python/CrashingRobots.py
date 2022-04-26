def move_forward(x, y, DIR, robots, robot, repeat, warehouse):
    # m variable used to indicate direction (so that less code is reused)
    if DIR == 'E' or DIR == 'N':
        m = 1
    else:
        m = -1

    if DIR == 'E' or DIR == 'W':
        # Start from 1 because 0 means stay at same spot
        for k in range(1, 1+repeat):
            # If next position is out of bounds
            # we use len(warehouse[0]) as upper bounds here because we are looking horizontally
            if x-1+k*m >= len(warehouse[0]) or x-1+k*m < 0:
                print('Robot {} crashes into the wall'.format(robot+1))
                return True

            # If next position is a robot, crash
            if warehouse[y-1][x-1+k*m] != 0:
                print('Robot {} crashes into robot {}'.format(robot+1, warehouse[y-1][x-1+k*m]))
                return True
        
        # Update positions in robots list and warehouse grid
        robots[robot][0] = x + repeat*m
        warehouse[y-1][x-1+repeat*m] = robot+1

    else:
        # Same as above
        for k in range(1, 1+repeat):
            # Same as above with exception UB is len(warehouse) because we are looking vertically
            if y-1+k*m >= len(warehouse) or y-1+k*m < 0:
                print('Robot {} crashes into the wall'.format(robot+1))
                return True
            
            # Same as above
            if warehouse[y-1+k*m][x-1] != 0:
                print('Robot {} crashes into robot {}'.format(robot+1, warehouse[y-1+k*m][x-1]))
                return True
        
        # Update positions
        robots[robot][1] = y + repeat*m
        warehouse[y-1+repeat*m][x-1] = robot+1

    # Successfully moved forward robot, set initial position to vacant 0
    warehouse[y-1][x-1] = 0
    return False


# Function to change directions
def turn(action, DIR):
    if DIR == 'E':
        if action == 'L':
            DIR = 'N'
        else:
            DIR = 'S'

    elif DIR == 'W':
        if action == 'L':
            DIR = 'S'
        else:
            DIR = 'N'

    elif DIR == 'N':
        if action == 'L':
            DIR = 'W'
        else:
            DIR = 'E'

    else:
        if action == 'L':
            DIR = 'E'
        else:
            DIR = 'W'

    return DIR


def main():
    K = int(input())

    for i in range(K):
        A, B = map(int, input().split())

        # Warehouse is a 2D grid that stores the vancacies of each cell
        # If there is no robot, value == 0, else value == robot ID starting from 1
        warehouse = [[0]*A for _ in range(B)]

        N, M = map(int, input().split())

        robots = []
        for j in range(N):
            X, Y, DIR = input().split()
            robots.append([int(X),int(Y),DIR])
            warehouse[int(Y)-1][int(X)-1] = j+1

        # Create list to store instructions
        # Need to accept all instructions before processing each one
        instructions = []
        for j in range(M):
            instructions.append(list(input().split()))

        # Process instructions
        # crash flag for if a crash occurred
        crash = False
        for j in range(len(instructions)):
            robot, action, repeat = instructions[j]
            repeat = int(repeat)
            # Robots list is indexed from 0 so whereas input starts from 1
            robot = int(robot)-1

            # Turning
            if action == 'L' or action == 'R':
                # repeat%4 here because 4 turns in the same direction == 0 turns
                for k in range(repeat%4):
                    robots[robot][2] = turn(action, robots[robot][2])

            # Moving forward
            if action == 'F':
                # Extract the current coordinates and direction the robot is facing
                x, y, direction = robots[robot][0], robots[robot][1], robots[robot][2]
                # move_forward returns True if a crash occurred
                if move_forward(x, y, direction, robots, robot, repeat, warehouse):
                    crash = True
                    # Only need to record first crash, so break here
                    break
            
        # There was no crash recorded
        if not crash:
            print('OK')


if __name__ == '__main__':
    main()
