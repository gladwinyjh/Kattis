# Given that a customer waiting time depends on whether all his wood is cut
# getting the customer with the least amount of wood done earlier is the most optimal

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        # List that stores each customer's total wood size
        woodSizes = []
        for j in range(n):
            customer = list(map(int, input().split()))
            # We sum up the total size of all the customer's wood pieces
            woodSizes.append(sum(customer[1:]))
        
        if len(woodSizes) > 1:
            # Sort the customers in ascending order of total wood
            sortedWoodSizes = sorted(woodSizes)
            totTime = sortedWoodSizes[0]
            for j in range(1, len(sortedWoodSizes)):
                # Given that the total time taken for the current customer
                # depends on the completion time of the previous customer
                # Reassign sortedWoodSizes[j] each time
                sortedWoodSizes[j] = sortedWoodSizes[j] + sortedWoodSizes[j-1]
                totTime += sortedWoodSizes[j]
            print(f'{totTime/n}')
        else:
            # Only one customer
            print(woodSizes[0])
            
        
if __name__ == '__main__':
    main()