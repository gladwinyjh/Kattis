# Sum of 7 dwarves == 100. Find 2 of them such that sum will be 100. Only exists 1 solution.

def main():
    hats = []
    hatSum = 0

    for i in range(9):
        hats.append(int(input()))
        hatSum += hats[-1]

    # Difference to be obtained
    diff = hatSum - 100

    for i in range(9):
        for j in range(i+1,9):
            # Unique solution found
            if hats[i] + hats[j] == diff:
                for k in range(9):
                    # Print hat values except the 2 dwarves
                    if k != i and k != j:
                        print(hats[k])
    

        
if __name__ == '__main__':
    main()