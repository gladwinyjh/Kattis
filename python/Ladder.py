from sys import stdin
import math


def main():
    h, v = map(int, stdin.readline().split())
    
    # Trigonometry
    # Opposite side = h, angle = v in radians
    # sin(v) = opp/hyp --> h/sin(v) = height of ladder

    print(math.ceil(h/math.sin(math.radians(v))))


if __name__ == '__main__':
    main()
