B, n = map(int, input().split())
L = input().split(' ')

s = 0
for idx in range(n):
    s += int(L[idx]) * (B**(n-1-idx))

print(s)