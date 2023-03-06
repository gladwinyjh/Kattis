from sys import stdin


def main():
    n = int(stdin.readline())
    pieces = list(map(int, stdin.readline().split()))
    
    pieces.sort()

    A = 0
    B = 0
    # Keep track of whose turn it is
    # Initially its alice's turn
    A_turn = True
    while pieces:
        if A_turn:
            A += pieces.pop()
            # Bob's turn next
            A_turn = False
        else:
            B += pieces.pop()
            # Alice's turn next
            A_turn = True

    print(A, B)


if __name__ == '__main__':
    main()
