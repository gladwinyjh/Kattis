def main():
    a1_g, b1_g, a2_g, b2_g = map(int, input().split())
    a1_e, b1_e, a2_e, b2_e = map(int, input().split())

    # Building a probability list for all values possible that they can roll, into separate lists
    # Minimum roll for each == 1, max roll = b1 + b2
    # Start from 0 index so add 1 to the max. 0 value not attainable but it doesnt matter 
    prob_g = [0] * (b1_g + b2_g + 1)
    prob_e = [0] * (b1_e + b2_e + 1)

    for i in range(a1_g, b1_g+1):
        for j in range(a2_g, b2_g+1):
            prob_g[i+j] += 1

    for i in range(a1_e, b1_e+1):
        for j in range(a2_e, b2_e+1):
            prob_e[i+j] += 1

    # Probability of acquiring value = Number of possible combinations for this value / Total number of combinations
    prob_g = [x/sum(prob_g) for x in prob_g]
    prob_e = [x/sum(prob_e) for x in prob_e]

    # Probability of winner in this case is the expected value for the rolls
    # What is the expected value when Gunnar rolls vs what is the expected value when emma rolls
    # Expected value = sum of (probability of rolling value * value of roll) for all values
    expected_g = sum([x*i for i, x in enumerate(prob_g)])
    expected_e = sum([x*i for i, x in enumerate(prob_e)])

    # Dumb thing: sometimes you can get expected values that differ only by the slightest ex: 0.00001
    # So add 1e-6 to the smaller value to test
    if expected_g > expected_e + 1e-6:
        print('Gunnar')
    elif expected_g + 1e-6 < expected_e:
        print('Emma')
    else:
        print('Tie')


if __name__ == '__main__':
    main()