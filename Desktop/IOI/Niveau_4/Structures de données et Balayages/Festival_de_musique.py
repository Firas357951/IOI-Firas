import sys

N, NbG = map(int, input().split())
L = list(map(int, sys.stdin.readline().strip().split()))

Memo = [0] * NbG
Zero = [True] * NbG
n = NbG

for i, element in enumerate(L):
    Memo[element-1] += 1
    if Zero[element-1]:
        n -= 1
        Zero[element-1] = False
    if n ==0:
        idx = i
        break

start = 0
fin = idx+1
List = []

while fin < N:
    while Memo[L[start]-1] > 1 and len(List) == 0:
        Memo[L[start]-1] -= 1
        if Memo[L[start]-1] == 0:
            List.append(L[start])
        start += 1
        
    Memo[L[start]-1] -= 1
    if Memo[L[start]-1] == 0:
        List.append(L[start])
    if Memo[L[fin]-1] == 0:
        List.remove(L[fin])
    Memo[L[fin]-1] += 1
    start += 1
    fin += 1

if fin == N:
    while Memo[L[start]-1] > 1 and len(List) == 0:
        Memo[L[start]-1] -= 1
        if Memo[L[start]-1] == 0:
            List.append(L[start])
        start += 1
min = fin - start
print(min)

















