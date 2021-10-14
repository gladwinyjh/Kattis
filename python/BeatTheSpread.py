def main():
    n = int(input())

    for i in range(n):
        sum, absDiff = map(int, input().split())

        # scoreA + scoreB = sum
        # abs(scoraA - scoreB) = absDiff
            # scoreA - scoreB = absDiff
            # scoreB - scoreA = absDiff

        # if (sum - absDiff) is divisible by 2
            # scoreB = (sum - absDiff) / 2 (lower score)
            # scoreA = sum - scoreB (higher score)
            
        if (sum - absDiff) >= 0:
            if (sum - absDiff) % 2 == 0:
                scoreB = (sum - absDiff) // 2
                scoreA = sum - scoreB
                print(scoreA, scoreB)
                continue
        
        print('impossible')
            

if __name__ == '__main__':
    main()
