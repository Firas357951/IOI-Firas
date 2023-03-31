def intersection(min, max, a, b):   
   if a > max or b < min:
      return False
   return True

min = int(input())
max = int(input())

n = int(input())
i = 0
for _ in range(n):
   a = int(input())
   b = int(input()) 
   if intersection(min, max, a, b):
      i += 1

print(i)   