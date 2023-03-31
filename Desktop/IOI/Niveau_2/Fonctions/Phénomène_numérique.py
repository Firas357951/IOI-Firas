def Next(n):
   if n % 2 == 0:
      return n // 2
   else:
      return 3*n + 1
      
n = int(input())
while n != 1:
   n = Next(n)
   print(n, end=' ')