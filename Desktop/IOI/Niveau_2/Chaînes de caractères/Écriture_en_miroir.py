n = int(input())

for _ in range(n):
   ch = str(input())
   for idx in range(len(ch)-1, -1, -1):
      print(ch[idx], end='')
   print()