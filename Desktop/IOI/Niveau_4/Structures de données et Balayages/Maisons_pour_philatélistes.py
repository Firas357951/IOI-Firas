import sys

N = int(input())
L = list(map(int, sys.stdin.readline().strip().split()))

def distance(x, y):
    return abs(x-y)

L.sort()

min = 10**8 
for idx in range(len(L)-1):
    d = distance(L[idx], L[idx+1])
    if d < min:
        min = d

print(min)
        




























