def main():
    a, b, h = map(int, input().split())
    
    distanceCovered = 0
    steps = 0
    for i in range(h):
        distanceCovered += a
        steps += 1
        if distanceCovered >= h:
            print(steps)
            break
        
        distanceCovered -= b


if __name__ == '__main__':
    main()