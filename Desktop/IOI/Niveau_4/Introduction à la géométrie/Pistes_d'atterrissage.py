import sys
from math import sqrt
inp = sys.stdin.readline
def main():
    x, y = map(int, input().split())
    N = int(input())
    min = 20000
    for _ in range(N):
        xA, yA, xB, yB = map(int, inp().split())
        AB = sqrt((xB-xA)**2 + (yB-yA)**2)
        position = ((xB-xA) * (x-xA) + (yB-yA) * (y-yA)) / AB**2
        if position <= 0:
            result = sqrt((x-xA)**2 + (y-yA)**2)
        elif position >= 1:
            result = sqrt((x-xB)**2 + (y-yB)**2)
        else:
            result = abs((xB-xA) * (y-yA) - (yB-yA) * (x-xA)) / AB
        if result < min:
            min = result
            piste = xA, yA, xB, yB
    print(*piste)
main()