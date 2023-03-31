N = int(input())
L = []
while N >= 1:
    r = N % 2
    N = N // 2
    L.append(r)

if N == 0:
   print(0)
for idx in range(len(L)-1, -1, -1):
    print(L[idx], end='')  