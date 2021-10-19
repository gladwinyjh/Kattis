# If two letter sequences overlap (like at and to in the word baton) just replace the first one (in this case resulting in b@on)
# If two letter sequences start at the same location (like be and bee in been) replace the longer one (in this case resulting in bn)
# If the letter sequence starts with an upper-case letter, then the abbreviation should also be in upper-case (if appropriate)
# No substituted letter should later be part of another substitution

def main():
    # Store each abbreviations to dictionary
    d = {}
    d['at'] = '@'
    d['and'] = '&'
    d['one'] = d['won'] = '1'
    d['to'] = d['too'] = d['two'] = '2'
    d['for'] = d['four'] = '4'
    d['bea'] = d['be'] = d['bee'] = 'b'
    d['sea'] = d['see'] = 'c'
    d['eye'] = 'i'
    d['oh'] = d['owe'] = 'o'
    d['are'] = 'r'
    d['you'] = 'u'
    d['why'] = 'y'

    n = int(input())
    for i in range(n):
        # Take in text as a list
        text = list(input().split())
        # Traverse each word in text
        for j in range(len(text)):
            # Traverse from front to back
            for k in range(len(text[j])):
                
                # Since len(text[j]) can be altered within loop
                # if len(text[j]) <= k, k cannot go further. This is to prevent index out of range error.
                if len(text[j]) <= k:
                        break

                # Don't need to check for replacements if word only consist of 1 letter
                # Put here instead of outside as len(text[j]) can be altered to 1 within this loop
                if len(text[j]) > 1:
                    # Boolean for if first letter in substring is uppercase
                    upper = False
                    if text[j][k].isupper():
                        upper = True
                        # Replace uppercase letter with lowercase so that we can find it in dictionary
                        text[j] = text[j].replace(text[j][k], text[j][k].lower())

                    # Traverse from back to k  
                    for l in range(len(text[j]), k, -1):
                        # Substring k:l matches with a key in dictionary
                        if text[j][k:l] in d:
                            # Replace substring with value
                            text[j] = text[j].replace(text[j][k:l], d[text[j][k:l]])
                            # Since no substituted letter can be part of another substitution, break
                            break

                    # If previously established that first letter in substring is uppercased
                    # and was changed to lowercase
                    if upper:
                        # Change lowercase back to uppercase
                        text[j] = text[j].replace(text[j][k], text[j][k].upper())

        # Print unwrapped text
        print(*text)


if __name__ == '__main__':
    main()