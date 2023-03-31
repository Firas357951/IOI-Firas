import sys

N, R = map(int, input().split())
L= list(map(int, input().split()))

List = [None] * N
s = 0
for idx, element in enumerate(L):
   s += element
   List[idx] = s 

for _ in range(R):
   start, end = map(int, sys.stdin.readline().strip().split())
   if start == 1:
      print(List[end-1])
   else:
      print(List[end-1] - List[start-2])





























