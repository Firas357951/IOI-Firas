n = int(input())
x = 0
y = 0

for _ in range(n):
   d = int(input())
   if d > 0:
      x+=d
   if d < 0:
      y +=d
      
print(x)
print(-y)
