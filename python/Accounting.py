# Storing key-value pairs and changing its values after each RESTART is too slow for Python at least


def main():
    wealths = {}
    restart_value = 0
    
    N, Q = map(int,input().split())

    for i in range(Q):
        simulation = input().split()

        # SET:
        # Set requested key to requested value in dictionary
        if len(simulation) == 3:
            wealths[int(simulation[1])] = int(simulation[2])

        # RESTART: 
        # Set all values in dictionary to simulation[1]
        # Clear dictionary to get rid of previously SET values
        elif simulation[0] == 'RESTART':
            restart_value = int(simulation[1])
            wealths = {}

        # PRINT: 
        # If key exists in dictionary, just print its value
        # else default value here is set to restart_value
        # Default value is needed because person may not have its wealth set yet
        else:
            print(wealths.get(int(simulation[1]), restart_value))
        

        
if __name__ == '__main__':
    main()