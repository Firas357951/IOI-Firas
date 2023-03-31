## Optimized method
import sys

def point(p1, milieu):
    p2 = (2 * milieu[0] - p1[0], 2 * milieu[1] - p1[1])
    if (p2[0] >= 0 and p2[0] <= 100) and (p2[1] >= 0 and p2[1] <= 100):
        return p2
    return
N = int(input())

Grille = [['.'] * 101 for _ in range(101)]
points = [None] * N
for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    Grille[x][y] = 'p'
    points[i] = (x, y)
points.sort()
n = 0
for idx in range(1, N-1):
    milieu = points[idx]
    for i in range(idx):
        p1 = points[i] 
        p2 = point(p1, milieu)
        if p2 != None:
            if Grille[p2[0]][p2[1]] == 'p':
                n += 1
                break
print(n)
        

## 1st Method but do not pass 30% of tests
import sys

def Milieu(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
def isint(number):
    if int(number) == number:
        return True
    return False

N = int(input())

Grille = [['.'] * 101 for _ in range(101)]
points = [None] * N
for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    Grille[x][y] = 'p'
    points[i] = (x, y)
points.sort()
n = 0
memo = [[False] * 101 for _ in range(101)]
for idx in range(N):
    for i in range(idx+2, N):
        p1 = points[idx]
        p2 = points[i]
        milieu = Milieu(p1, p2)
        if isint(milieu[0]) and isint(milieu[1]):
            xm = int(milieu[0])
            ym = int(milieu[1])
            if Grille[xm][ym] == 'p' and not(memo[xm][ym]):
                memo[xm][ym] = True
                n += 1
print(n)
        




    