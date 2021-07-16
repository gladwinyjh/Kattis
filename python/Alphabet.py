from bisect import bisect_left

def main(string):
    
    # O(n^2) solution
    # LIS = [1] * len(string)
    
    # for i in range(len(string) -1, -1, -1):
    #     for j in range(i+1, len(string)):
    #         if string[i] < string[j]:
    #             LIS[i] = max(LIS[i], 1 + LIS[j])
                
    # return 26 - max(LIS)
    
    dp = [None] * len(string)
    length = 0
    for c in string: #O(n)
        index = bisect_left(dp, c, 0, length) #O(logn)
        
        if index < 0:
            index = -(index + 1)
        
        dp[index] = c #Store only that character
        
        if index == length:
            length += 1
    
    return 26 - length


if __name__ == '__main__':
    print(main(input()))