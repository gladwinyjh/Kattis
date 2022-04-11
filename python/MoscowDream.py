def main():
    a, b, c, n = map(int, input().split())
    
    # NO cases:
    # 1) There is not at least 1 easy, medium and hard problem
    # 2) The number of problems n is less than 3; require at least 1 easy, medium and hard
    # 3) Sum of problems a+b+c is not equal to number of problems required n.
    if a==0 or b==0 or c==0 or n<3 or a+b+c<n:
        print('NO')
    else:
        print('YES')
        

if __name__ == '__main__':
    main()
