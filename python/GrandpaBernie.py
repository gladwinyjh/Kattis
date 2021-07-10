# Store each country into a dict as key -> O(1)
# Each dict contains a sorted list, where keys contain values of years -> sorting O(nlgn)
# Each query goes to key (O(1)) and to the index of the value (O(number of visits for that country))


def main():
    num_trips = int(input())
    
    dict = {}
    
    for i in range(num_trips):
        country, year = input().split()
        
        if country not in dict:
            dict[country] = []

        dict[country].append(int(year))    
        
    for val in dict.values():
        val.sort()
        
    num_query = int(input())
    
    for i in range(num_query):  
        country, k = input().split()
        
        print(dict[country][int(k)-1])
    
    

if __name__ == '__main__':
    main()