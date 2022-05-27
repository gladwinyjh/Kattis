def main():
    k = int(input())
    my_ans = input()
    friend_ans = input()

    # Get the number of same and different answers 
    same_ans = 0
    diff_ans = 0
    for i in range(len(my_ans)):
        if my_ans[i] == friend_ans[i]:
            same_ans += 1
        else:
            diff_ans += 1

    # Logic:
        # For questions that your friend gets correct, you also want to get those correct
        # For questions that your friend gets wrong, you want to get those correct

        # In the different answers set, the more your friend is correct, the more wrong you are

        # So the friend should ideally get as few correct answers when it is different from yours
        # And you can maximise your correct answers when answers are different
        
    # Assume that all correct answers come from the same answer set
    # Cases:
        # 1) Number of friend correct answers > number of same answers
            # This means that friend gets correct answers in differing answers
                # Extra correct answers friend gets from different answers = k - same_ans
                # So the remaining answers you get correct = diff_ans - (k - same_ans)
        
        # 2) Number of friend correct answers == number of same answers
            # Remaining same answers both of you get wrong
            # You can still get more correct answers if you get correct for different answers

        # 3) Number of friend correct answers < number of same answers
            # Fall into same situation as Case 2 because the remaining same answers both of you get wrong
            # Any more correct answers you can get comes from the different answers 
    
    # Maximum number of correct answers you get so far:
        # Case 1)
            # min(k, same_ans) gives same_ans
        
        # Case 2)
            # k == same_ans
        
        # Case 3)
            # min(k, same_ans) gives k
    max_correct = min(k, same_ans)

    if max_correct == k: # Case 2 and 3
        print(max_correct + diff_ans)
    elif max_correct < k: # Case 1
        print(max_correct + (diff_ans - (k - max_correct)))


if __name__ == '__main__':
    main()