def main():
    digits = input()
    counter = [0] * 10

    for digit in digits:
        if digit == '0':
            i = 9
        else:
            i = int(digit) - 1
        
        counter[i] += 1
    
    for i in range(len(counter)):
        if counter[i] == 0:
            print(i+1)
            return
    
    # Get the minimum count of digits
    minCount = min(counter)
    # Get the index of first element that has this minimum
    # This element is digit - 1
    minIndex = counter.index(minCount)

    if minIndex == 9:
        # Digit 0 has the minimum occurrences.
        # minCount + 1 because inability to assemble will
        # occur on the next occurrence of this digit
        print('1' + '0'*(minCount + 1))
    else:
        # Another digit has the minimum occurrences
        # str(minIndex + 1) gets the actual digit in string format
            # +1 because it was stored as int(digit) - 1
        # The smallest will occur at the next occurrence of digit
            # Ex: Digit = 3
            #     Occurrences: 3, 33, 333, 3333, ...
        print(str(minIndex+1) * (minCount+1))
            
        
if __name__ == '__main__':
    main()