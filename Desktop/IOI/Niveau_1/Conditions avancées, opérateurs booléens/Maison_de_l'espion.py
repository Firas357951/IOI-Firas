min_x = int(input())
max_x = int(input())

min_y = int(input())
max_y = int(input())
i = 0
n = int(input())
for _ in range(n):
   x = int(input())
   y = int(input())
   if x in range(min_x, max_x+1):
      if y in range(min_y, max_y+1):
         i += 1

print(i)