def main():
    # Create keyboard mapping dictionary
    # Note that backslash \ is \\ and apostrophe ' is \' and space is just space
    keyboard = {
            '1':'`','2':'1','3':'2','4':'3','5':'4','6':'5','7':'6','8':'7','9':'8','0':'9','-':'0','=':'-',
            'W':'Q','E':'W','R':'E','T':'R','Y':'T','U':'Y','I':'U','O':'I','P':'O','[':'P',']':'[','\\':']',
            'S':'A','D':'S','F':'D','G':'F','H':'G','J':'H','K':'J','L':'K',';':'L','\'':';',
            'X':'Z','C':'X','V':'C','B':'V','N':'B','M':'N',',':'M','.':',','/':'.',' ':' '
            }

    # Because undefined number of lines are being accepted
    while True:
        try:
            line = list(input())
            # Replace character with one from left
            for i in range(len(line)):
                line[i] = keyboard[line[i]]

            # Join characters from list back to string
            print(''.join(line))

        except:
            return


if __name__ == '__main__':
    main()
