import sys
from math import sqrt
inp = sys.stdin.readline
def main():
    xA, yA, xB, yB = map(int, input().split())
    N = int(input())
    AB = sqrt((xB-xA)**2 + (yB-yA)**2)
    for _ in range(N):
        x, y = inp().split()
        result = ((xB-xA) * (int(x)-xA) + ((yB-yA) * (int(y)-yA))) / AB
        print(result)
main()