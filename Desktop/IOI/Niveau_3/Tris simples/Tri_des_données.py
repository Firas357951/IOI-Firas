n = int(input())
L = list(map(int, input().split()))

L.sort()
for element in L:
   print(element, end = ' ')