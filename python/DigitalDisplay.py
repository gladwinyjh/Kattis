def main():
    clock_dict = {
            '0': ['+---+','|   |','|   |','+   +','|   |','|   |','+---+'],
            '1': ['    +','    |','    |','    +','    |','    |','    +'],
            '2': ['+---+','    |','    |','+---+','|    ','|    ','+---+'],
            '3': ['+---+','    |','    |','+---+','    |','    |','+---+'],
            '4': ['+   +','|   |','|   |','+---+','    |','    |','    +'],
            '5': ['+---+','|    ','|    ','+---+','    |','    |','+---+'],
            '6': ['+---+','|    ','|    ','+---+','|   |','|   |','+---+'],
            '7': ['+---+','    |','    |','    +','    |','    |','    +'],
            '8': ['+---+','|   |','|   |','+---+','|   |','|   |','+---+'],
            '9': ['+---+','|   |','|   |','+---+','    |','    |','+---+'],
            ':': [' ',' ','o',' ','o',' ', ' ']
            }

    while True:
        time = input()
        
        if time == 'end':
            print('end')
            return
        
        # zip() iterates tuples with corresponding elements from each of the lists
        # join() with a newline
        print("\n".join("{}  {}  {}  {}  {}".format(a, b, c, d, e) for a, b, c, d, e in zip(clock_dict[time[0]], clock_dict[time[1]], clock_dict[time[2]], clock_dict[time[3]], clock_dict[time[4]])))

        # Python print() prints newline at the end by default, so only 1 \n is needed here
        print('\n')


if __name__ == '__main__':
    main()
