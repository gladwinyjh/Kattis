# Matching parentheses problem
# When found a mismatch, just output the paratheses and the index, otherwise 'ok so far'
def main():
    length = int(input())
    L = input()

    stack = []
    for idx, c in enumerate(L):
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        elif c != ' ':
            if not stack:
                print(c, idx)
                return

            if ((c == ')' and stack[-1] != '(') or 
                (c == ']' and stack[-1] != '[') or 
                (c == '}' and stack[-1] != '{')):
                print(c, idx)
                return
            else:
                stack.pop()
    
    print('ok so far')


if __name__ == '__main__':
    main()