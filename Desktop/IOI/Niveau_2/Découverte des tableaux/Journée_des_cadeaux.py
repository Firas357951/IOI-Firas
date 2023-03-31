n = int(input())
L = []

for _ in range(n):
   L.append(int(input()))
   L.sort()
   
if n % 2 == 1:
   print(L[n//2])
else:
   print((L[n//2] + L[n//2-1])/2)