n = int(input())

min_x = 1000000
min_y = 1000000
max_x = 0
max_y = 0

for _ in range(n):
   x = int(input())
   y = int(input())
   if x < min_x:
      min_x = x
   if y < min_y:
      min_y = y
   if x > max_x:
      max_x = x
   if y > max_y:
      max_y = y

p = ( (max_x - min_x) + (max_y - min_y) ) * 2
print(p)