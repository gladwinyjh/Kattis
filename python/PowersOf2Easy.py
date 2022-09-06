from sys import stdin


def main():
    n, e = map(int, stdin.readline().split())

    target = 2**e
    
    count = 0
    for i in range(n+1):
        if str(target) in str(i):
            count += 1

    print(count)


if __name__ == '__main__':
    main()
