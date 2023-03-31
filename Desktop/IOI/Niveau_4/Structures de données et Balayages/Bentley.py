##Méthode optimisée

N = int(input())
L = list(map(int, input().split()))

List = [None] * N
s = 0

for idx, element in enumerate(L):
   s += element
   List[idx] = s   

Min = 0
M = 0
for element in List:
   if element < Min:
      Min = element
   if (element - Min) > M:
      M = element - Min
print(M)


## Méthode naive

N = int(input())
L = list(map(int, input().split()))

M = max(L)
for largeur in range(1, N+1):
   List = [0]
   for idx in range(N - largeur + 1):
      s = sum(L[idx : idx+ largeur])
      List.append(s)
   
   Max = max(List)
   if Max > M:
      M = Max
      
print(M)




