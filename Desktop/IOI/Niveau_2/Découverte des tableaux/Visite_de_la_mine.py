n = int(input())
L = []
Invert = [2, 1, 3, 5, 4]

for _ in range(n):
   L.append(int(input()) - 1)
   
for idx in range(len(L)-1, -1, -1):
   print(Invert[L[idx]]) 