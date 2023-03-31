import sys

N, P = map(int, input().split())
L = [None] * P
memo = [True] * (P+1)
for idx in range(P):
    L[idx] = int(sys.stdin.readline().strip())

i = 1
B = False
for idx in range(P):
    if idx > 0:
        print(i)
    if L[idx] <= P:
        memo[L[idx]-1] = False
        while not(memo[i-1]) and i <= P :
            i += 1
if i == N + 1 :
    print(-1)
else:
    print(i)

    





