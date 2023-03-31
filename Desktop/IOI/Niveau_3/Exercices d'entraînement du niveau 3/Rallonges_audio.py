import sys
inp = sys.stdin.readline
N = int(input())

P11 = []
P00 = []
s0 = 0
for _ in range(N):
    C1, C2, L = map(int, inp().strip().split())
    if (C1 == 0 and C2 == 1) or (C1 == 1 and C2 == 0):
        s0 += L
    elif C1 == 0 and C2 == 0:
        P00.append(L)
    else:
        P11.append(L)

if len(P11) == 0:
    print(-1)
else:
    P00.sort(reverse = True)
    P11.sort(reverse = True)
    if len(P00) < len(P11):
        k = len(P00) + 1
    else:
        k = len(P11)
    for idx in range(k):
        s0 += P11[idx]
    for idx in range(k-1):
        s0 += P00[idx]
    print(s0)
     


