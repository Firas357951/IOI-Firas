n = int(input())

x = abs(n) % 24
if n >= 0:
   print(x)
else:
   print(24 - x)