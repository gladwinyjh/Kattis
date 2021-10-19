def main():
    n = int(input())
    itemPrices = list(map(int, input().split()))
    # Sort items in ascending order
    sorteditemPrices = sorted(itemPrices)

    discount = 0
    # If there are at least 3 items in list
    if len(sorteditemPrices) >= 3:
        # Traverse list from 3rd most expensive item and decrement by 3 each time until 3rd cheapest or cheapest
        # This ensures that the more expensive items are discounted first
        for i in range(len(sorteditemPrices)-3, -1, -3):
            discount += sorteditemPrices[i]

    print(discount)

if __name__ == '__main__':
    main()