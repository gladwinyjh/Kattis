def main():
    N, M = map(int, input().split())

    if N > M:
        if N - M == 1:
            print(f'Dr. Chaz needs 1 more piece of chicken!')
        else:
            print(f'Dr. Chaz needs {N-M} more pieces of chicken!')
    elif M - N == 1:
        print(f'Dr. Chaz will have 1 piece of chicken left over!')
    else:
        print(f'Dr. Chaz will have {M-N} pieces of chicken left over!')


if __name__ == '__main__':
    main()
