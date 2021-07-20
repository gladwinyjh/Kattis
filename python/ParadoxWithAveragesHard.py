#Check mean of both
#Get all CS students values that lies between these 2 means NOT INCLUSIVE
#If any ONE of these students transfer to Econs, the joke will hold true
#Print length of list of values
    

def average(lst):
    return sum(lst)/len(lst)

def main():
    n = int(input())
    
    for i in range(n):
        input() #Blank line
        
        num_cs, num_econ = map(int,input().split())
        
        cs_list = list(map(int,input().split()))
        
        econ_list = list(map(int,input().split()))
        
        mean_cs = average(cs_list)
        mean_econ = average(econ_list)

        found = list(filter(lambda x: mean_econ < x < mean_cs, cs_list))
        
        print(len(found))


if __name__ == '__main__':
    main()