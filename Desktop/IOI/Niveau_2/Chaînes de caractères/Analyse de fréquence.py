L = [0] * 100

n, m = map(int, input().split())
for _ in range(n):
   Line = str(input())
   List = [len(mot) for mot in Line.split(" ")]
   for element in List:
      L[element-1] += 1

for idx, element in enumerate(L):
   if element != 0:
      print(idx+1, ":", element)