keyboard = {
    '1': [0,0],'2': [1,0],'3': [2,0],
    '4': [0,1],'5': [1,1],'6': [2,1],
    '7': [0,2],'8': [1,2],'9': [2,2],
    '0': [1,3]
}

def findClosest(number):
    valid = True
    # Go through each digit from 2nd to end
    # Check if digit is valid
    for i in range(1, len(number)):
        # Not valid number if current digit position is to the left or above previous digit position
        if keyboard[number[i]][0] < keyboard[number[i-1]][0] or keyboard[number[i]][1] < keyboard[number[i-1]][1]:
            valid = False
            break
    
    return valid


def main():
    T = int(input())
    while (T > 0):
        number = int(input())

        diff = 0
        while (True):
            # Check closest below
            if findClosest(str(number - diff)):
                print(number - diff)
                break
            # Check closest above
            elif findClosest(str(number + diff)):
                print(number + diff)
                break
            
            # If no valid positions, increment difference by 1
            diff += 1

        T -= 1


if __name__ == '__main__':
    main()