'''
From Sample Input 1

1000, 980, 960, 940, 10
  s    b     
  ---------------------
  s         b
       s    b
  ---------------------
  s              b
       s         b
            s    b
  ---------------------
  s                   b
       s              b
            s         b
                 s    b

s = sell, b = buy
Observe that we are always extending the buy day by one from all possible sell and buy options
However we dont need to calculate all possible options at each day if we store the maximum for each day

For the current day
extend the previous day maximum sell day by 1 day and compare it with: buying the previous day and selling today
'''
def main():
    N, K =  map(int, input().split())

    prices = [int(x) for x in input().split()]
    
    # Store the first 2 days
    max_profits = [100*prices[0] - 100*prices[1] - 2*K]
    # Start from the 3rd day
    for i in range(2, len(prices)):
        # + 100*prices[i-1] : reverting the sell from previous day
        # - 100*prices[i]: sell today instead
        # -K because holding crypto for one more day
        max_profits.append(max(max_profits[i-2] + 100*prices[i-1] - 100*prices[i] - K, 100*prices[i-1] - 100*prices[i] - 2*K))

    print(max(max(max_profits), 0))


if __name__ == '__main__':
    main()
   
