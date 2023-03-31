n,m = map(int, input().split()) 
L = list(map(int, input().split()))

def max(List):
   if len(List) == 0:
      return
   Max = List[0]
   i = 0
   for idx, element in enumerate(List):
      if element > Max:
         Max = element
         i = idx
   return (Max, i)
   
for idx in range(m):
   Max = max(L)[0]
   print(Max, end=' ')
   L.remove(Max)
