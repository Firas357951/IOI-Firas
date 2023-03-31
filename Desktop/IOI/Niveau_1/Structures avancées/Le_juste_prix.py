n = int(input())
min = 1000000
idx = 0

for i in range(n):
   x = int(input())
   if x <= min :
      min = x
      idx = i+1

print(idx)   