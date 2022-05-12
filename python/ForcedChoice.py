def main():
    N, P, S = map(int, input().split())
    
    # Store all choices in a list
    choices = []
    for i in range(S):
        # Use tuple so that it is hashable when changing it into a set
        # Used set so that lookup will be fast
        inp = tuple(map(int, input().split()))
        choices.append(set(inp[1:]))
   
    # Recognise that there is no way we REMOVE those cards if the chosen prediction is one of those selected
    # Read choices from the back because we want to make sure only that one card remains
    decisions = []
    for i in range(len(choices)-1, -1, -1):
        if P in choices[i]:
            decisions.append('KEEP')
        else:
            decisions.append('REMOVE')
    
    # Decisions now store choices in reversed order
    # Simply print it in reverse
    for i in reversed(decisions):
        print(i)


if __name__ == '__main__':
    main()
