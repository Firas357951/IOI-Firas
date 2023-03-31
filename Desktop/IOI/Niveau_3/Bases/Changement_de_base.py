Bd, B, n = map(int, input().split(' '))
L = input().split(' ')
s = 0
for idx in range(n):
    s += int(L[idx]) * Bd ** (n-1-idx)

L = []
while s >= 1:
    r = s % B
    s = s // B 
    L.append(r)

if len(L) == 0:
    print(0)
else:
    for idx in range(len(L)):
        print(L[len(L)-1-idx], end= ' ')
