from sys import stdin


def main():
    inp = stdin.readline().rstrip()

    ans = []
    open_b = 0
    i = 0
    while i < len(inp):
        if inp[i] == '{':
            # Each time '{' is introduced, its contents will be indented by 2 spaces
            ans.append(' ' * open_b + '{')
            # 2 spaces indent
            open_b += 2
            
            # Go to next index
            i += 1
        elif inp[i] == '}':
            # Each time '}' is introducted, it will be outdented by 2 spaces
            if i == len(inp) - 1:
                # Last '}' always without indentation
                ans.append('}')
            else:
                # 2 spaces outdent
                open_b -= 2
                string = ' ' * open_b + '}'
                # If a ',' follows, it belongs to the same line
                if inp[i+1] == ',':
                    string += ','
                    # Increase index for the ','
                    i += 1

                ans.append(string)

            # Go to next index
            i += 1
        else:
            # Not brackets
            # Content within brackets are indented by 2 * open_b
            string = ' '  * open_b
            # Store string until a ',' or '}' is reached
            while inp[i] != ',' and inp[i] != '}':
                string += inp[i]
                i += 1
            
            if inp[i] == ',':
                # If ',' then it belongs on the same line as the contents
                string += ','
                # Account for ',' go to next index
                i += 1
            
            ans.append(string)

    for x in ans:
        print(x)


if __name__ == '__main__':
    main()
