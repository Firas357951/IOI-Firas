nbOperations = int(input())

L = [0] * 10
for _ in range(nbOperations):
   idx = int(input()) - 1
   q = int(input())
   L[idx] += q
   
for element in L:
   print(element)