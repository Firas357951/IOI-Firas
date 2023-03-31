n = int(input())
L = [0] * n

NbPersonne = int(input())
for _ in range(NbPersonne):
   idx = int(input())
   L[idx] += 1

for element in L:
   print(element) 
