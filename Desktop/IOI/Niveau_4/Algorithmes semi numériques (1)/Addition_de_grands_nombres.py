def sum(B, *kwargs):
    s = 0
    for element in kwargs:
        s += element
    if s >= B:
        r = 1
    else:
        r = 0
    return (r, (s) % B)

B, N1, N2 = map(int, input().split())
L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

N = max(N1, N2)
R = [0] * N

if N2 > N1:
    L1, L2 = L2, L1
    N1, N2 = N2, N1
L2 = [0] * (N1 - N2) + L2
idx = N - 1
r = 0
while (idx >= 0):
    r, result = sum(B, L1[idx], L2[idx], r)
    R[idx] = result
    idx -= 1
    
if r != 0:
    R = [r] + R
    
for element in R:
    print(element, end=' ')









