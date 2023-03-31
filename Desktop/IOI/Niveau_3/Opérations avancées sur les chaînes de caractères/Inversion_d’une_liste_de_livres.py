N = int(input())

L = [None] * N
for idx in range(N):
   ch = str(input())
   L[N-1-idx] = ch

for ch in L:
   print(ch)