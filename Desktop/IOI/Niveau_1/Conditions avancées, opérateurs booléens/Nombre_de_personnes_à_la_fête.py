n = int(input())
s = 0
max = 0
for _ in range(2*n):
   i = int(input())
   if i > 0:
      s += 1
   else:
      s -= 1
   if s > max:
      max = s 

print(max)