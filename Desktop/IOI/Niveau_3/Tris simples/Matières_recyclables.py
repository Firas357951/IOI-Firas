N = int(input())
L = []
for _ in range(N):
    L.append(str(input()))

L.sort()
for element in L:
    print(element)

