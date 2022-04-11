def main():
   N = int(input())

   # Store prices into list
   prices = []
   for i in range(N):
       prices.append(int(input()))

   # Sort prices in ascending order
   prices.sort()

   sum_prices = sum(prices)
   discount = 0
   # Maximise discount by ensuring the cheapest book in the group is as expensive as possible
   # Every 3rd book from the back of sorted list is free. Stop when there are <3 books available and sum up discount
   for i in range(N-3, -1, -3):
       discount += prices[i]

   print(sum_prices - discount) 


if __name__ == '__main__':
    main()
