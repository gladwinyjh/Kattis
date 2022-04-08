def main():
    # Don't actually need to use n
    n = int(input())

    # Store the knots as sets
    knotsToLearn = set(input().split())
    knotsLearnt = set(input().split())

    # Get the difference between sets
    # Since only one element, just pop() it
    print((knotsToLearn - knotsLearnt).pop())


if __name__ == '__main__':
    main()