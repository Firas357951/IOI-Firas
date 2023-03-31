n = int(input())

L = []
for _ in range(n):
   L.append(int(input()))
L.sort()
mid = n//2
for idx in range(mid):
   print("{} {}".format(L[idx], L[n-idx-1]))