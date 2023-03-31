n = int(input())
Chngmts = int(input())
L = []
for _ in range(n):
   L.append(int(input()))

for _ in range(Chngmts):
   s = int(input())
   f = int(input())
   L[s], L[f] = L[f], L[s]

for element in L:
   print(element)