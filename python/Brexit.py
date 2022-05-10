from collections import defaultdict, deque


def main():
    C, P, X, L = map(int, input().split())
    
    # List that counts the number of partners remaining for each country. C+1 because C starts from 1
    initial = [0] * (C+1)
    # Boolean list to check if a country has left the union
    left = [False] * (C+1)
    # Dictionary to keep track of eah country's partners
    partners = defaultdict(set)

    for i in range(int(P)):
        first, second = map(int, input().split())
        # Add a partner to first and second country
        initial[first] += 1
        initial[second] += 1
        
        # Add the country number to each country
        partners[first].add(second)
        partners[second].add(first)
    
    # Country that triggers leaving is your home country
    if X == L:
        print('leave')
        return
   
    # Queue to process the countries that left
    q = deque([L])
    left[L] = True
    while q:
        # Number of home country's remaining partners <= half of what it had initially
        if len(partners[X]) <= (initial[X] / 2):
            print('leave')
            return

        country = q.popleft()

        for partner in partners[country]:
            # Remove this country from partners set 
            partners[partner].remove(country)
            
            # Partner country has <= of what it had initially AND
            # Partner country has already been registered as 'left' (so that dont enqueue same country more than once)
            if len(partners[partner]) <= (initial[partner] / 2) and not left[partner]:
                q.append(partner)
                left[partner] = True

    print('stay')


if __name__ == '__main__':
    main()
