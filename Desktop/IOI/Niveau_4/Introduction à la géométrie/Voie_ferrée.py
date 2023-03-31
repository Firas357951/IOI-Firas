# we use cross product 
import sys
from math import sqrt
inp = sys.stdin.readline
def main():
    xA, yA, xB, yB = map(int, input().split())
    N = int(input())
    AB = sqrt((xB-xA)**2 + (yB-yA)**2)
    max = 0
    for _ in range(N):
        x, y = inp().split()
        result = abs((xB-xA) * (int(y)-yA) - (yB-yA) * (int(x)-xA)) / AB
        if result > max:
            max = result
            point = (x, y)
    print(*point)
main()