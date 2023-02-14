from sys import stdin


def main():
    N = int(stdin.readline())
    item = stdin.readline().rstrip()
    
    for count in range(N,0,-1):
        if count == 1:
            print(f'{count} bottle of {item} on the wall, {count} bottle of {item}.')
            print(f'Take it down, pass it around, no more bottles of {item}.')
            return
        else:
            print(f'{count} bottles of {item} on the wall, {count} bottles of {item}.')
            if count-1 == 1:
                print(f'Take one down, pass it around, {count-1} bottle of {item} on the wall.') 
            else:
                print(f'Take one down, pass it around, {count-1} bottles of {item} on the wall.')

        print('\n') 
        

if __name__ == '__main__':
    main()