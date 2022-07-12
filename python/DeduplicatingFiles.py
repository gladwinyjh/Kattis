from sys import stdin


# Hash function defined in problem description
def hash(line):
    hash_value = 0
    for c in line:
        hash_value ^= ord(c)

    return hash_value


def main():
    while True:
        n = int(stdin.readline())

        if n == 0:
            # EOF
            return
        
        files = []
        hash_files = []
        # Store the hashed value in hash_files and each line of words in files
        for i in range(n):
            line = stdin.readline()[:-1]
            files.append(line)
            hash_files.append(hash(line))
        
        # Number of unique files is just the length of set of files
        unique_files = len(set(files))

        collisions = 0

        # For each line:
            # Check every other line if their hash values matches
            # If matched, check if both lines are the same
                # If matched and same, they are identical
                # If matched and not the same, it is a collision
                    # Increment collisions
        for i in range(len(files)):
            for j in range(i+1, len(files)):
                if hash_files[i] == hash_files[j] and files[i] != files[j]:
                    collisions += 1

        print(unique_files, collisions) 


if __name__ == '__main__':
    main()
