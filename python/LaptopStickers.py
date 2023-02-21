from sys import stdin


def main():
    L, H, K = map(int, stdin.readline().split())
    
    laptop = [['_' for _ in range(L)] for _ in range(H)]
    
    for i in range(K):
        length, height, a, b = map(int, stdin.readline().split())
        
        for j in range(height):
            for k in range(length):
                # Next coordinate/part of the sticker
                next_a = a + k
                next_b = b + j
                
                # Check if this part of the sticker is within the laptop 
                if 0 <= next_a < L and 0 <= next_b < H:
                    # Convert number to alphabet
                    # Change the current part of the laptop to that sticker
                    laptop[next_b][next_a] = chr(97+i)
    
                    
    [print("".join(row)) for row in laptop]
                
    

if __name__ == '__main__':
    main()