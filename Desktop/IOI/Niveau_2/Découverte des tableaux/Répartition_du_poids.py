n = int(input())
L = []
s = 0
for _ in range(n):
   x = float(input())
   L.append(x)
   s += x
   
for element in L:
   print(s/n - element)
   