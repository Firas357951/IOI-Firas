def f(a,b):
   if a <= b:
      return a
   return b

y = int(input())
for _ in range(9):
   x = int(input())
   y = f(y, x)
print(y)