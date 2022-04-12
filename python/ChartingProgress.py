def main():
    # Keep receiving inputs
    while True:
        try:
            inp = input()
            # 'end' marks the index of the last '*' to be printed
            end = 0
            # while loop executes if input is not blank line
            while inp:
                # Count the number of '*' in the line
                num_records = inp.count('*')

                # Print '.' times until the start of '*'s
                # Then print '*' num_records times
                # Then print '.' end times to fill remaining gap
                print(('.' * (len(inp) - num_records - end) + ('*' * num_records) + ('.' * end))) 
                
                # Increment end to shift ending position backwards depending on number of '*' encountered this line
                end += num_records
                
                # Receive new input
                inp = input()
            
            # Print new line when there is a blank input
            print('\n')

        except:
            # End of file; return
            return


if __name__ == '__main__':
    main() 
