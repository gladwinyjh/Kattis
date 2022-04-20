def main():
    n = int(input())

    # List to store restaurants
    places = []
    # List to store sets of menu items
    items_list = []

    for i in range(n):
        num_places = int(input())
        places.append(input())
        items_set = set()
        
        # Make the menu items a set
        for j in range(num_places):
            items_set.add(input())
        
        # Append menu items set to items_list list
        items_list.append(items_set)
    
    # Flag for if there is a suitable restaurant
    found = False
    for idx, items in enumerate(items_list):
        # Found the first restaurant
        if 'pea soup' in items and 'pancakes' in items:
            # Get the name of the restaurant
            print(places[idx])
            found = True
            break
    
    # No restaurants found
    if not found:
        print('Anywhere is fine I guess')


if  __name__ == '__main__':
    main()
