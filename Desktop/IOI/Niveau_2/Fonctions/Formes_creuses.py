line = int(input())

n = int(input())
m = int(input())

triangle = int(input())

for _ in range(line):
   print("X", end='')
   
print()
print()

for y in range(n):
   for x in range(m):
      if (y == 0) or (y == n-1) or (x == 0) or (x == m-1):  
         print("#", end='')
      else:
         print(" ", end='')
   print()

print()

for y in range(1, triangle+1):
   for x in range(1, y + 1):
      if (y == 1) or (y == x) or (x == 1) or (y == triangle):
         print("@", end='')
      else:
         print(" ", end='')
   print()