N = int(input())

L = []
for _ in range(N):
    x, y = map(int, input().split())
    L.append((x, y))
L = sorted(L, key=lambda x:(x[1],x[0]))

for tuple in L:
    print(tuple[0], tuple[1])