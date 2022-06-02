def main():
    N = int(input())

    passwords_prob = []
    for i in range(N):
        password, prob = input().split()
        # Storing actual password not required
        passwords_prob.append(float(prob))
    
    # 'Optimal order' = Try passwords with higher probability first
    # So sort in descending order of probabilities
    passwords_prob.sort(reverse=True)
    
    # Expected number of attempts = Summation(prob of success for each attempt * number of attempts)
    # Index + 1 gives the number of attempts since we move on to the next password on the next attempt
    expected_trials = 0
    for idx, prob in enumerate(passwords_prob):
        expected_trials += (idx+1)*(prob)

    print(expected_trials)


if __name__ == '__main__':
    main()
