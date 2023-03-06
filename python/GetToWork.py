from sys import stdin


def main():
    C = int(stdin.readline())

    for i in range(1, C+1):
        N, T = map(int, stdin.readline().split())
        E = int(stdin.readline())
        
        # Store employee numbers for each town
        # Start from 1 so leave index 0
        employees = [0] * (N+1)

        # Store capacities of car capacities for each town
        # In a list for each employee/car for each town
        capacity = [[] for _ in range(N+1)]
        for j in range(E):
            H, P = map(int, stdin.readline().split())
            
            # Same town as office, don't need a car
            if H == T:
                continue

            employees[H] += 1
            capacity[H].append(P)

        [town.sort() for town in capacity if town]
        
        # Number of vehicles commuting out of town
        num_vehicles = [0] * (N+1)
        
        # Impossible case flag
        impossible = False
        for j in range(1, len(employees)):
            # Employees in this town need to travel to office
            while employees[j]:
                # There are employees still at the town, but not enough travel capacity
                if not capacity[j]:
                    impossible = True
                    break
                
                # Fill up next car
                num_vehicles[j] += 1

                # Capacity of largest car is less than number of employees remaining in town
                # Fill car up and move on to next town
                if capacity[j][-1] >= employees[j]:
                    break

                # Need another car
                else:
                    # Remaining number of employees that need a car from this town
                    # New car needed (pop)
                    employees[j] -= capacity[j].pop()
        
            if impossible:
                break

        if impossible:
            print(f"Case #{i}: IMPOSSIBLE")
        else:
            print(f"Case #{i}: {' '.join(str(x) for x in num_vehicles[1:])}")


if __name__ == '__main__':
    main()
    # Seems like employee in same town as office = no need for car
    # Minimise number of cars coming out of each town
        # Sort cars take those with larger capacity first
        # Deduct from employees from each town after filling cars
