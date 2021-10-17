def main():
    n = int(input())
    for i in range(n):
        loc = list(map(int, input().split()))

        # Equation of line is given as Ax + By + C = 0 OR y = mx + c
        # y = mx + c -> mx - y + c = 0 -> dy/dx * x - y + c = 0 -> dy*x - dx*y + dx*c = 0
        # We can see that A = dy, B = -dx
        # C = dx*c = y*dx - dy*x = -B*y - A*x
        A = loc[3] - loc[1] 
        B = -(loc[2] - loc[0]) 
        C = -B*loc[1] - A*loc[0]

        m = int(input())

        # Dictionary to store key = city name, value = city coordinates. Cities given are unique
        cities = {}
        for j in range(m):
            city = list(input().split())
            cities[city[0]] = [int(city[1]), int(city[2])]
        
        # List to store cities that have minimum distance to hurricane line
        # Printing cities as output will therefore be in order of input
        greatestDanger = []
        # Set minimum numerators or 'distance' to inf initially
        dangerDistance = float('inf')
        for city, coor in cities.items():
            # Perpendicular distance formula = |Ax + By + C| / sqrt(A^2 + B^2)
            # Dont need to calculate denominator as it only scales the distance
            # We only need to calculate numerator, referred to as 'distance' here
            num = abs(A*coor[0] + B*coor[1] + C)

            # If current 'distance' = current minimum 'distance'
            if num < dangerDistance:
                # Set minimum to current
                dangerDistance = num
                # If there is already a previously stored city
                if greatestDanger:
                    # Empty the list
                    greatestDanger = []
                greatestDanger.append(city)
            # There has been a city that is minimum equidistant to line vs this city
            elif num == dangerDistance:
                greatestDanger.append(city)

        print(*greatestDanger)

  

if __name__ == '__main__':
    main()