# For each category, judges pick winner at random
# To maximise chances of winning, join the category with the least number of participants

def main():
    n = int(input())
    d = {}
    for i in range(n):
        costume = input()
        if costume not in d:
            d[costume] = 1
        else:
            d[costume] += 1
    
    # Get the minimum dictionary value
    minCount = min(d.values())
    # Go through dictionary and extract costumes that have the minCount to a list
    minCostumes = [key for key, val in d.items() if val==minCount]
    # Sort list
    minCostumesSorted = sorted(minCostumes)
    for j in range(len(minCostumesSorted)):
        print(minCostumesSorted[j])


if __name__ == '__main__':
    main()