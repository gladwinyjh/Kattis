from sys import stdin


def main():
    T = int(stdin.readline())
    for i in range(T):
        R, P, D = map(int, stdin.readline().split())
         
        ingredients = []
        scaling_factor = D / P
        
        for j in range(R):
            name, weight, percentage = stdin.readline().split()
            weight = float(weight)
            # Keep percentage from 0-1
            percentage = float(percentage) / 100
            # Append to list to maintain order during printing
            ingredients.append([name, weight, percentage])

            if percentage == 1:
                # Found the 100% one, get the scaled weight of the main ingredient
                scaled_weight_main = weight * scaling_factor
        
        # Follow instructions and print 
        print(f'Recipe # {i+1}')
        for ingredient in ingredients:
            print(f'{ingredient[0]} {ingredient[2] * scaled_weight_main:.1f}')
            
        print(f"{40 * '-'}")
    
    
if __name__ == '__main__':
    main()