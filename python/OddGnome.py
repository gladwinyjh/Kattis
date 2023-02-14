from sys import stdin


def main():
    # Strictly increasing order, just do linear pass and check if in order
    n = int(stdin.readline())
    
    for i in range(n):
        gnomes = list(map(int, stdin.readline().split()))

        # Start from 2nd gnome, compare with previous gnome
        for j in range(2, len(gnomes)):
            if gnomes[j] - gnomes[j-1] != 1:
                print(j)
                # Break if king is found
                break


if __name__ == '__main__':
    main()