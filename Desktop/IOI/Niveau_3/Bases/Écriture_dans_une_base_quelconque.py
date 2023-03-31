N, B = map(int, input().split(' '))

L = []
while N >= 1:
    r = N % B
    N = N // B 
    L.append(r)

if len(L) == 0:
    print(1)
    print(0)
else:
    print(len(L))
    for idx in range(len(L)):
        print(L[len(L)-1-idx], end= ' ')
